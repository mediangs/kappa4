from functools import reduce
import excel_helper
import rotate as ro
import numpy as np
import dist_util as du
from constant import CONST
from geom import vector


def normal_vector_of_canal_orifices_plane(orifice_points):

    # assume MB, DB, P sequence in orifice_points
    MB, DB, P = np.array(orifice_points[CONST.MB]), np.array(orifice_points[CONST.DB]), np.array(orifice_points[CONST.P])

    # the cross product is a vector normal to the plane
    return du.unit_vector(np.cross(DB - MB, P - MB))


def tooth_laterality(orifice_points): # left or right

    MB, DB, P = orifice_points[CONST.MB], orifice_points[CONST.DB], orifice_points[CONST.P]

    # return the value of z-axis
    return np.cross((P-MB), (DB-MB))[2]


def landmarks_transform_into_XY_plane(projecting_points, orifices, orifice_origin, orifice_on_xaxis):
    """
    :param projecting_points: points to transform
    :param orifices: MB, DB, P, MB2 sequence
    :param orifice_origin:
    :param orifice_on_xaxis:
    :return:
    """
    #                 (Y-axis)
    #              *     |
    #                    |
    #                    |        orifice_on_xaxis
    #     ---------------*---------*--------- (X-axis)
    #      orifice_origin|
    #              (0,0) |
    # 3D rotation, rotated to XY plane

    center = [0, 0, 0]

    r_ps = ro.get_rotated_points(center, normal_vector_of_canal_orifices_plane(orifices), projecting_points)
    r_orifices = ro.get_rotated_points(center, normal_vector_of_canal_orifices_plane(orifices), orifices)

    # Translate the whole orifice_points
    r_ps -= r_ps[orifice_origin]
    r_orifices -= r_orifices[orifice_origin]

    # 2D rotation
    # assume calculate angle on XY plane
    r_angle = du.angle_between(np.dot(r_ps[orifice_on_xaxis], np.array([[1.0, 0.0, 0.0],
                                                                        [0.0, 1.0, 0.0],
                                                                        [0.0, 0.0, 0.0]])), [1.0, 0.0, 0.0])

    X_COORD, Y_COORD = 0, 1
    r_angle = 2 * np.pi - r_angle if r_orifices[orifice_on_xaxis][Y_COORD] < 0 else r_angle
    r_matrix = ro.rotation_matrix_2d(r_angle)

    r_ps = np.dot(r_ps, r_matrix)
    r_orifices = np.dot(r_orifices, r_matrix)

    # vertical flip in case of opposite side
    if tooth_laterality(r_orifices) < 0:
        r_ps = np.dot(r_ps,  np.array([[1.0, 0.0, 0.0],
                                       [0.0, -1.0, 0.0],
                                       [0.0, 0.0, 1.0]]))

    return r_ps


def plot_orifices_boundary(model3d, P, marker=None):
    marker_list = ['bo', 'mo', 'ro', 'co']
    for i in range(len(P)-1):
        model3d.plot_points([P[i], P[i + 1]], marker)
        model3d.plot_points([P[i]], marker_list[i % len(marker_list)])

    model3d.plot_points([P[len(P) - 1]], marker_list[len(P) - 1 % len(marker_list)])
    model3d.plot_points([P[0], P[-1]], marker)


def landmarks_coords_collector(specimens):
    from class_model import ModelData

    canal_orifice_coords = {}
    landmarks_coords = {}

    for specimen in specimens:
        for canal in specimen.canals:
            md = ModelData(specimen, canal_ref=canal.name, read_model=False)
            canal_orifice_coords.update({md.crv_name.split('-')[-1]: md.pts_of_crv_ref[-5]})

        if all(key in canal_orifice_coords for key in ('mb', 'db', 'p', 'mb2')):
            orifices_coord = [canal_orifice_coords['mb'], canal_orifice_coords['db'],
                              canal_orifice_coords['p'], canal_orifice_coords['mb2']]
        elif all(key in canal_orifice_coords for key in ('mb', 'db', 'p')):
            orifices_coord = [canal_orifice_coords['mb'], canal_orifice_coords['db'], canal_orifice_coords['p']]
        else:
            orifices_coord = None
            print(f' {canal_orifice_coords.keys()} : Insufficient orifice info - skipped')

        landmarks_coords.update({specimen.name: {'orifices': orifices_coord,
                                                 'central_fossa': specimen.central_fossa,
                                                 'long_axis': specimen.long_axis}})
        canal_orifice_coords = {}

    return landmarks_coords


def landmarks_measurement(mb, db, p, mb2, crossing):

    mb, db, p = vector(mb), vector(db), vector(p)
    mb2 = None if mb2 is None else vector(mb2)
    crossing = None if crossing is None else vector(crossing)

    mp_length = (p - mb).length()
    dp_length = (p - db).length()
    md_length = (db - mb).length()
    dmp_angle = (db - mb).angle_between(p - mb)
    mdp_angle = (mb - db).angle_between(p - db)
    mpd_angle = (mb - p).angle_between(db - p)
    measurements = {'mp_length': mp_length, 'dp_length': dp_length, 'md_length': md_length,
                    'dmp_angle': dmp_angle, 'mdp_angle': mdp_angle, 'mpd_angle': mpd_angle}

    if mb2:
        mm2_length = (mb - mb2).length()
        m2p_length = (mb2 - p).length()
        pmm2_angle = 0.0 if mm2_length ==0 else (p - mb).angle_between(mb2 - mb)
        mp_m2_dist = distance_btn_line_and_point(mb, p, mb2)
        measurements.update({'mm2_length': mm2_length, 'm2p_length': m2p_length,
                             'mp_m2_dist': mp_m2_dist, 'pmm2_angle': pmm2_angle})

    if crossing:
        cm_length = (mb-crossing).length()
        cd_length = (db-crossing).length()
        cp_length = (p-crossing).length()
        measurements.update({'cm_length': cm_length, 'cd_length': cd_length, 'cp_length': cp_length})

    return measurements


def landmarks_coord_transformation(coords, orifice_origin, orifice_on_xaxis):
    orifice_coords = coords['orifices']
    merged_coords = orifice_coords[:]
    merged_coords.append(coords['central_fossa'])
    merged_coords.extend(coords['long_axis'])

    r_merged = landmarks_transform_into_XY_plane(merged_coords, orifice_coords, orifice_origin, orifice_on_xaxis)

    r_orifices = r_merged[:len(orifice_coords)]
    r_long_axis = r_merged[-2:].tolist()
    r_central_fossa = r_merged[-3:-2][0].tolist()

    r_crossing = du.intersection_point_of_plane_and_line(vector([0, 0, 0]), vector([0, 0, 1]), vector(r_central_fossa),
                                                         vector(r_long_axis[1]) - vector(r_long_axis[0]))

    return r_orifices, r_crossing, r_central_fossa, r_long_axis


def export_landmarks_measurement(orifices, excel_workbook=None):

    from collections import OrderedDict

    headings = ['ToothID', 'mpLength', 'dpLength', 'mdLength', 'dmpAngle', 'mdpAngle', 'mpdAngle',
                'mm2Length', 'm2pLength', 'pmm2Angle', 'mp_m2_dist', 'cmLength', 'cdLength', 'cpLength']
    result = OrderedDict(zip(headings, ['' for _ in range(len(headings))]))
    column_header = ','.join(result.keys())

    print(column_header)

    # Add sheet & change sheet name
    if excel_workbook:
        worksheet = excel_workbook.Sheets.Add()
        # Fill column header
        excel_helper.fill_a_row_to_sheet(worksheet, column_header, 1)

    cur_row_of_sheet = 2

    for orifice in orifices:
        result['ToothID'] = orifice['id']
        result['mpLength'] = '%.3f' % orifice['analysis']['mp_length']
        result['dpLength'] = '%.3f' % orifice['analysis']['dp_length']
        result['mdLength'] = '%.3f' % orifice['analysis']['md_length']
        result['dmpAngle'] = '%.3f' % orifice['analysis']['dmp_angle']
        result['mdpAngle'] = '%.3f' % orifice['analysis']['mdp_angle']
        result['mpdAngle'] = '%.3f' % orifice['analysis']['mpd_angle']
        result['mm2Length'] = '' if 'mm2_length' not in orifice['analysis'] else '%.3f' % orifice['analysis']['mm2_length']
        result['m2pLength'] = '' if 'm2p_length' not in orifice['analysis'] else '%.3f' % orifice['analysis']['m2p_length']
        result['pmm2Angle'] = '' if 'pmm2_angle' not in orifice['analysis'] else '%.3f' % orifice['analysis']['pmm2_angle']
        result['mp_m2_dist'] = '' if 'mp_m2_dist' not in orifice['analysis'] else '%.3f' % orifice['analysis']['mp_m2_dist']
        result['cmLength'] = '%.3f' % orifice['analysis']['cm_length']
        result['cdLength'] = '%.3f' % orifice['analysis']['cd_length']
        result['cpLength'] = '%.3f' % orifice['analysis']['cp_length']

        row_data = reduce(lambda x, y: x + ',' + y, result.values())
        print(row_data)
        if excel_workbook:
            excel_helper.fill_a_row_to_sheet(worksheet, row_data, cur_row_of_sheet)
        cur_row_of_sheet += 1



def normalize_4by3(arr):
    x = (4-arr.shape[0]) * 3
    arr = arr.reshape(-1)
    b = np.pad(arr, (0, x), 'constant', constant_values=0)
    return b.reshape(4, -1)


def distance_btn_line_and_point(p1, p2, p3):
    """
    line p1 ------+--------- p2
                  |
                 p3
    :param p1:
    :param p2:
    :param p3:
    :return:
    """
    d = np.linalg.norm(np.cross(p2 - p1, p1 - p3)) / np.linalg.norm(p2 - p1)
    return d


def radius_of_circle_contain_points(center, points, percentile):
    x0 = center[0]
    y0 = center[1]
    x = [x[0] for x in points]
    y = [x[1] for x in points]
    r = np.sqrt((x - x0) ** 2 + (y - y0) ** 2)
    r0 = np.percentile(r, percentile)
    n_within = (r < r0).sum()
    return r0, n_within


def landmarks_relation_analysis(landmarks_coord):
    orifices_relation = []

    for k, coords in landmarks_coord.items():

        r_orifices, r_crossing, r_central_fossa, r_long_axis = landmarks_coord_transformation(coords, CONST.MB, CONST.P)

        measurements = landmarks_measurement(r_orifices[CONST.MB], r_orifices[CONST.DB], r_orifices[CONST.P],
                                             None if len(r_orifices) < 4 else r_orifices[CONST.MB2], r_crossing)

        orifices_relation.append({'id': k, 'ps': coords, 'analysis': measurements})
        print(measurements)

    return orifices_relation


def export_landmarks_relation(specimens):
    import win32com.client as win32  # Excel export

    coordinates = landmarks_coords_collector(specimens)
    landmarks_relation = landmarks_relation_analysis(coordinates)
    xl = win32.gencache.EnsureDispatch('Excel.Application')
    xl.Visible = True
    wb = xl.Workbooks.Add()
    export_landmarks_measurement(landmarks_relation, wb)


def draw_landmarks_relation(specimens, orifice_origin, orifice_on_xaxis, grid=True):
    import model3d_matplot as model3d

    coordinates = landmarks_coords_collector(specimens)

    if CONST.DB not in (orifice_origin, orifice_on_xaxis): #for MB -- P
        bounding_box = [(-1, 7), (-2, 4), (-3, 3)]
    elif CONST.MB not in (orifice_origin, orifice_on_xaxis): #for DB -- P
        bounding_box = [(-2, 6), (-2, 4), (-3, 3)]
    else: #for MB -- DB
        bounding_box = [(-2, 6), (-6, 1), (-3, 3)]

    model3d.init(bounding_box, grid)

    r_mbs, r_dbs, r_ps, r_mb2s, r_corssings, r_central_fossas = [], [], [], [], [], []

    for k, coords in coordinates.items():

        r_orifices, r_crossing, r_central_fossa, r_long_axis = landmarks_coord_transformation(coords, orifice_origin, orifice_on_xaxis)

        plot_orifices_boundary(model3d, r_orifices, 'y:')
        # model3d.plot_points(r_long_axis, 'r-')
        # model3d.plot_points([crossing_point], 'bo')

        r_mbs.append(r_orifices[CONST.MB])
        r_dbs.append(r_orifices[CONST.DB])
        r_ps.append(r_orifices[CONST.P])
        r_corssings.append(r_crossing)
        r_central_fossas.append(r_central_fossa)

        if len(r_orifices) == 4:
            r_mb2s.append(r_orifices[CONST.MB2])

    mean_mb = np.array(r_mbs).mean(axis=0)
    mean_db = np.array(r_dbs).mean(axis=0)
    mean_p = np.array(r_ps).mean(axis=0)
    mean_mb2 = np.array(r_mb2s).mean(axis=0)
    mean_cross = np.array(r_corssings).mean(axis=0)
    mean_central_fossa = np.array(r_central_fossas).mean(axis=0)

    # r0, n_within = radius_of_circle_contain_points(np.array(mean_db), r_dbs, 80)
    # model3d.plot_circle(mean_mb, r0, color='r', fill=False)

    plot_orifices_boundary(model3d, [mean_mb, mean_db, mean_p, mean_mb2], 'r-')
    plot_orifices_boundary(model3d, [mean_mb, mean_db, mean_p], 'b-')
    model3d.plot_points([mean_cross, mean_central_fossa], 'r-')
    model3d.plot_points([mean_cross], 'rX', markersize=8)
    model3d.plot_points([mean_central_fossa], 'mX', markersize=8)

    mertics = landmarks_measurement(mean_mb, mean_db, mean_p, mean_mb2, mean_cross)

    model3d.text3d(f'MB({mertics["dmp_angle"]:.1f}`)', mean_mb)
    #model3d.text3d(f'MB({mertics["pmm2_angle"]:.1f}` / {mertics["dmp_angle"]:.1f}`)', mean_mb)
    model3d.text3d(f'DB({mertics["mdp_angle"]:.1f}`)', mean_db)
    model3d.text3d(f'P({mertics["mpd_angle"]:.1f}`)', mean_p)
    model3d.text3d(f'MB2({mertics["mp_m2_dist"]:.2f}mm)', mean_mb2)

    model3d.text3d(f'{mertics["mp_length"]:.1f}mm', np.array([mean_mb, mean_p]).mean(axis=0))
    model3d.text3d(f'{mertics["dp_length"]:.1f}mm', np.array([mean_db, mean_p]).mean(axis=0))
    model3d.text3d(f'{mertics["md_length"]:.1f}mm', np.array([mean_mb, mean_db]).mean(axis=0))
    model3d.text3d(f'{mertics["mm2_length"]:.1f}mm', np.array([mean_mb, mean_mb2]).mean(axis=0))
    model3d.text3d(f'{(vector(mean_cross) - vector(mean_central_fossa)).length():.1f}mm', np.array([mean_cross, mean_central_fossa]).mean(axis=0))

    # mean_cross point와 mb, db, p의 관계
    model3d.text3d(f'{mertics["cm_length"]:.1f}mm', np.array([mean_mb, mean_cross]).mean(axis=0), 'r')
    model3d.text3d(f'{mertics["cd_length"]:.1f}mm', np.array([mean_db, mean_cross]).mean(axis=0), 'r')
    model3d.text3d(f'{mertics["cp_length"]:.1f}mm', np.array([mean_p, mean_cross]).mean(axis=0), 'r')
    model3d.plot_points([mean_cross, mean_mb], 'r:')
    model3d.plot_points([mean_cross, mean_db], 'r:')
    model3d.plot_points([mean_cross, mean_p], 'r:')

    model3d.show()


def test():
    import data_mx6 as data_set
    specimens = data_set.specimens[:]
    # export_landmarks_relation(specimens)
    draw_landmarks_relation(specimens, orifice_origin=CONST.MB, orifice_on_xaxis=CONST.P, grid=False)


# def test2():
#     from constant import CONST
#     ps1 = [[1., 1., 1.2], [2.2, 1.2, 1.3], [1.3, 2., 0.6]]
#     ps2 = [[1.2, 1.3, 1.1], [2.5, 1.3, 1.4], [2.5, 2.2, 1.3]]
#     ps3 = [[0.5, 0.5, 0.7], [0.6, 2.3, 1.1], [1.9, 1.2, 1.3]]
#
#     ps1r = landmarks_transform_into_XY_plane(ps1, CONST.DB, CONST.P)
#     ps2r = landmarks_transform_into_XY_plane(ps2, CONST.DB, CONST.P)
#     ps3r = landmarks_transform_into_XY_plane(ps3, CONST.DB, CONST.P)
#
#
#     import model3d
#     model3d.init([(-3, 3), (-3, 3), (-3, 3)], grid=True)
#     plot_orifices_boundary(model3d, ps1, 'r:')
#     plot_orifices_boundary(model3d, ps1r, 'r-')
#
#     plot_orifices_boundary(model3d, ps2, 'b-')
#     plot_orifices_boundary(model3d, ps2r, 'b-')
#
#     plot_orifices_boundary(model3d, ps3, 'm-')
#     plot_orifices_boundary(model3d, ps3r, 'm-')
#
#     model3d.show()
#

if __name__ == '__main__':
    test()
