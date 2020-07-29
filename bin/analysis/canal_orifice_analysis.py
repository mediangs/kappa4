from functools import reduce
import excel_helper
import rotate as ro
import numpy as np
import dist_util as du


def get_normal_vector(orifice_points):
    from constant import CONST

    # assume MB, DB, P sequence in orifice_points
    MB, DB, P = np.array(orifice_points[CONST.MB]), np.array(orifice_points[CONST.DB]), np.array(orifice_points[CONST.P])

    # the cross product is a vector normal to the plane
    return du.unit_vector(np.cross(DB - MB, P - MB))


def get_canal_orientation(orifice_points): # left or right
    from constant import CONST
    MB, DB, P = orifice_points[CONST.MB], orifice_points[CONST.DB], orifice_points[CONST.P]

    # return the value of z-axis
    return np.cross((P-MB), (DB-MB))[2]


def get_projected_coordinate_of_orifices(orifice_points, reference_orifice, base_orifice):

    '''
    :param orifice_points:
    :param reference_orifice:
    :param base_orifice:
    :return:
    '''

    #                 (Y-axis)
    #              *     |
    #                    |
    #                    |        base_orifice
    #     ---------------*---------*--------- (X-axis)
    #   refrencee_orifice|
    #              (0,0) |


    # 3D rotation, rotated to XY plane
    center = [0, 0, 0]

    r_ps = ro.get_rotated_points(center, get_normal_vector(orifice_points), orifice_points)

    # Translate the whole orifice_points
    r_ps -= r_ps[reference_orifice]

    # 2D rotation
    # assume calculate angle on XY plane
    r_angle = du.angle_between(np.dot(r_ps[base_orifice], np.array([[1.0, 0.0, 0.0],
                                                                    [0.0, 1.0, 0.0],
                                                                    [0.0, 0.0, 0.0]])), [1.0, 0.0, 0.0])
    XAXIS, YAXIS = 0, 1
    if r_ps[base_orifice][YAXIS] < 0:
        r_angle = 2*np.pi - r_angle

    r_matrix = ro.rotation_matrix_2d(r_angle)
    r_ps = np.dot(r_ps, r_matrix)

    # vertical flip in case of opposite side
    if get_canal_orientation(r_ps) < 0:
        r_ps = np.dot(r_ps,  np.array([[1.0, 0.0, 0.0],
                                       [0.0, -1.0, 0.0],
                                       [0.0, 0.0, 1.0]]))

    return r_ps


def plot_boundary(model3d, P, marker=None):
    marker_list=['bo', 'mo', 'ro', 'co']

    for i in range(len(P)-1):
        model3d.plot_points([P[i], P[i + 1]], marker)
        model3d.plot_points([P[i]], marker_list[i % len(marker_list)])

    model3d.plot_points([P[len(P) - 1]], marker_list[len(P) - 1 % len(marker_list)])
    model3d.plot_points([P[0], P[-1]], marker)


def orifice_coordinate_collector(specimens):
    from class_model import ModelData

    orifice_coordinate = {}
    orifice_coordinates = {}

    for specimen in specimens:
        for canal in specimen.canals:
            md = ModelData(specimen, canal_ref=canal.name, read_model=False)
            orifice_coordinate.update({md.crv_name.split('-')[-1]: md.pts_of_crv_ref[-5]})

        orifice_coordinates.update({specimen.name: orifice_coordinate})
        orifice_coordinate={}

    return orifice_coordinates


def orifice_measurements_collector(P):
    from constant import CONST
    from geom import vector

    vmb, vdb, vp = vector(P[CONST.MB]), vector(P[CONST.DB]) ,vector(P[CONST.P])
    vmb2 = vector(P[CONST.MB2]) if len(P) == 4 else None

    mp_length = (vp - vmb).length()
    dp_length = (vp - vdb).length()
    md_length = (vdb - vmb).length()
    dmp_angle = (vdb - vmb).angle_between(vp - vmb)
    mdp_angle = (vmb - vdb).angle_between(vp - vdb)
    mpd_angle = (vmb - vp).angle_between(vdb - vp)

    metrics = {'mp_length': mp_length, 'dp_length': dp_length, 'md_length': md_length,
               'dmp_angle': dmp_angle, 'mdp_angle': mdp_angle, 'mpd_angle': mpd_angle}
    if vmb2:
        mm2_length = (vmb - vmb2).length()
        m2p_length = (vmb2 - vp).length()
        metrics.update({'mm2_length': mm2_length, 'm2p_length': m2p_length})

    return metrics


def orifices_data_export(orifices, excel_workbook=None):

    from collections import OrderedDict

    headings = ['ToothID', 'mpLength', 'dpLength', 'mdLength', 'dmpAngle', 'mdpAngle', 'mpdAngle',
                'mm2Length', 'm2pLength']
    result = OrderedDict(zip(headings, ['' for _ in range(len(headings))]))
    column_header = ','.join(result.keys())

    print (column_header)

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

        row_data = reduce(lambda x, y: x + ',' + y, result.values())
        print (row_data)
        if excel_workbook:
            excel_helper.fill_a_row_to_sheet(worksheet, row_data, cur_row_of_sheet)
        cur_row_of_sheet += 1


def get_orifices_analysis(specimens):
    orifice_coordinates = orifice_coordinate_collector(specimens)
    orifices = []

    for k, v in orifice_coordinates.items():
        coord = []
        if 'mb' in v and 'db' in v and 'p' in v and 'mb2' in v:
            coord = [v['mb'], v['db'], v['p'], v['mb2']]

        elif 'mb' in v and 'db' in v and 'p' in v:
            coord = [v['mb'], v['db'], v['p']]

        else:
            coord = None
            print(' {name} : Insufficient orifice info'.format(name=k))

        if coord:
            metric_analysis = orifice_measurements_collector(coord)
            orifices.append({'id': k, 'ps': coord, 'analysis': metric_analysis})
            print(metric_analysis)

    return orifices

def test():

    import data_mx_canals as data_set
    specimens = data_set.specimens[:]
    orifices = get_orifices_analysis(specimens)

    from constant import CONST
    import model3d

    #for MB -- P
    #chart3d.init([(-1, 7), (-2, 4), (-3, 3)], grid=True)

    #for DB -- P
    #chart3d.init([(-2, 6), (-4, 1), (-3, 3)], grid=True)

    #for MB -- DB
    model3d.init([(-2, 6), (-6, 1), (-3, 3)], grid=True)
    for orifice in orifices:
        ps_r = get_projected_coordinate_of_orifices(orifice['ps'], reference_orifice=CONST.MB, base_orifice=CONST.DB)
        plot_boundary(model3d, ps_r, 'y:')
    model3d.show()

    import win32com.client as win32  # Excel export
    xl = win32.gencache.EnsureDispatch('Excel.Application')
    xl.Visible = True
    wb = xl.Workbooks.Add()
    orifices_data_export(orifices, wb)


def test2():
    from constant import CONST
    ps1 = [[1., 1., 1.2], [2.2, 1.2, 1.3], [1.3, 2., 0.6]]
    ps2 = [[1.2, 1.3, 1.1], [2.5, 1.3, 1.4], [2.5, 2.2, 1.3]]
    ps3 = [[0.5, 0.5, 0.7], [0.6, 2.3, 1.1], [1.9, 1.2, 1.3]]

    ps1r = get_projected_coordinate_of_orifices(ps1, CONST.DB, CONST.P)
    ps2r = get_projected_coordinate_of_orifices(ps2, CONST.DB, CONST.P)
    ps3r = get_projected_coordinate_of_orifices(ps3, CONST.DB, CONST.P)


    import model3d
    model3d.init([(-3, 3), (-3, 3), (-3, 3)], grid=True)
    plot_boundary(model3d, ps1, 'r:')
    plot_boundary(model3d, ps1r, 'r-')

    plot_boundary(model3d, ps2, 'b-')
    plot_boundary(model3d, ps2r, 'b-')

    plot_boundary(model3d, ps3, 'm-')
    plot_boundary(model3d, ps3r, 'm-')

    model3d.show()


if __name__ == '__main__':
    test()
