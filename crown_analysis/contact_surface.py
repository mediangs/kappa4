'''
https://math.stackexchange.com/questions/99299/best-fitting-plane-given-a-set-of-points
'''

import numpy as np
import scipy.spatial as spatial
import pandas as pd

import helpers_geom
from helpers_geom import curve_to_points, intersection_point_of_plane_and_line, \
    fitted_plane_of_points
from helpers_contours import convert_to_points
from analysis_shape import outline_centroid, outline_area
from vector_class import vector
from nerve_path import Nerve_path


def boundary_of_pts(pts):
    ps = np.array(pts)
    max_bound = np.max(ps, axis=0) * 1.2
    min_bound = np.min(ps, axis=0) * .5
    return list(zip(min_bound, max_bound))


def crown_analysis(contact_pts, occlusal_pts, cej_pts, apex_pt, axes, chart=False):
    """
    :param contact_pts:
    :param occlusal_pts:
    :param cej_pts:
    :param axes: [0]: mesio-distal, [1]: bucco-lingual, [2]: occluso-apical direction
    :return:
    """
    ret = {}

    contact_normal, contact_plane_point = fitted_plane_of_points(contact_pts, axes[0])
    occlusal_normal, occlusal_plane_point = fitted_plane_of_points(occlusal_pts, axes[2])
    cej_normal, cej_plane_point = fitted_plane_of_points(cej_pts, axes[2])

    centriod_of_cej = outline_centroid(cej_plane_point, cej_normal, cej_pts)

    #교합면과 CEJ평면의 중심점을 지나는 선(normal은 CEJ 평면)이 만나는 점
    occlusal_crossing_point = intersection_point_of_plane_and_line(occlusal_plane_point, occlusal_normal,
                                                                       centriod_of_cej, cej_normal)
    ret['crown_height'] = (vector(occlusal_crossing_point)-vector(centriod_of_cej)).length()
    ret['root_length'] = (vector(apex_pt)-vector(centriod_of_cej)).length()
    ret['crown_root_ratio'] = ret['root_length'] / ret['crown_height']
    ret['contact_area'] = outline_area(contact_plane_point, contact_normal, contact_pts)
    ret['cej_area'] = outline_area(cej_plane_point, cej_normal, cej_pts)
    ret['contact_occlusal_angle'] = helpers_geom.degree_between_vectors(vector(contact_normal), vector(occlusal_normal) * -1)
    ret['contact_cej_ange'] = helpers_geom.degree_between_vectors(vector(contact_normal), vector(cej_normal))
    ret['occlusal_cej_angle'] = helpers_geom.degree_between_vectors(vector(occlusal_normal), vector(cej_normal))

    if chart:
        model3d.plot_mesh_surface(cej_plane_point, cej_normal, boundary_of_pts(cej_pts),
                                  color='y', alpha=0.3)
        model3d.plot_mesh_surface(contact_plane_point, contact_normal, boundary_of_pts(contact_pts),
                                  color='b', alpha=0.3)
        model3d.plot_mesh_surface(occlusal_plane_point, occlusal_normal, boundary_of_pts(occlusal_pts),
                                  color='g', alpha=0.3)
        model3d.plot_points(cej_pts)
        model3d.plot_points(contact_pts)
        model3d.plot_marker([centriod_of_cej], ['magenta', 'o', 3])
        model3d.plot_marker([occlusal_crossing_point], ['magenta', 'o', 3])

    return ret


def overlapping_chunk(arr):
    """
    :param arr:
    :return:
    [a,b,c,d,e] --> [[a,b], [b,c], [c,d], [d,e]]
    """
    size = 2
    step = 1
    return [arr[i: i + size] for i in range(0, len(arr), step)][:-1]


def shortest_distance_of_contours(c1, c2):
    cp1 = overlapping_chunk(c1)
    cp2 = overlapping_chunk(c2)

    results = [helpers_geom.closest_distance_btn_lines(line1, line2) for line1 in cp1 for line2 in cp2]
    results.sort(key=lambda x: x[0])
    return results[0]


def interpolated_points(sps, n=100):
    """
    :param sps:
    :param n: inerpolation 된 점의 갯수
    :return:  array of points, length of curve
    """
    ps = convert_to_points(sps)
    ps.append(ps[0])
    spline = Nerve_path.create(ps)
    return np.array(curve_to_points(spline, n)), spline.get_appr_len()


def contact_width(contact):
    result = [spatial.distance.cdist(contact, e.reshape(1, 3)).max() for e in contact]
    return max(result)


def axis_vectors(axis):
    ps = convert_to_points(axis)
    assert(len(ps) == 6)
    # Mesio-Distal, Bucco-Lingual, Occluso-Apical Vectors
    return [vector(ps[i*2 + 1]) - vector(ps[i*2]) for i in range(3)]


def desc_by_id(id):
    key = id.split('.')[0]
    kv = {'1000': '4.철기(1000년전)', '3500': '2.청동기(3500년전)', '4500': '1.신석기(5500년전', '5500': '3.청동기(2500년전)'}
    return kv[key]


def main():
    import crown_points
    import model3d_matplot as model3d

    data = crown_points.points_info()
    results = []
    chart = True

    for e in data:

        # prepare chart
        if chart:
            global model3d
            bound_box = [(-10, 20), (-10, 20), (-2, 28)]
            model3d.init(bound_box)

        axes = axis_vectors(e['axes'])
        apex_pt = convert_to_points(e['axes'])[5]
        contact_pts, _ = interpolated_points(e['contact'])
        cej_pts, cej_perimeter = interpolated_points(e['cej'])
        occlusal_pts = np.array(convert_to_points(e['occlusal']))

        max_contact_width = contact_width(contact_pts)
        contact_cej_dist, p1, p2 = shortest_distance_of_contours(contact_pts, cej_pts)
        r = {'ID': e['name'], 'desc': desc_by_id(e['name']), 'contact_cej_dist': contact_cej_dist,
             'max_contact_width': max_contact_width, 'cej_perimeter': cej_perimeter}
        r.update(crown_analysis(contact_pts, occlusal_pts, cej_pts, apex_pt, axes, chart=chart))
        results.append(r)

        print(f'ID: {e["name"]}, contact_cej_dist: {contact_cej_dist:.2f}, contact width: {max_contact_width:.2f}, contact area: {r["contact_area"]:.2f}, '
              f'cej_perimeter:{cej_perimeter:.2f}, cej_area:{r["cej_area"]:.2f}, crown root ratio:{r["crown_root_ratio"]:.2f},'
              f' crown_height: {r["crown_height"]:.2f}, '
              f'root length:{r["root_length"]:.2f}, co_angle: {r["contact_occlusal_angle"]:.1f}, '
              f'ccej_angle: {r["contact_cej_ange"]:.1f}, ocej_angle:{r["occlusal_cej_angle"]:.1f}')

        if chart:
            # model3d.plot_points([p1, p2], 'r-')
            model3d.plot_marker([p1, p2], ['magenta', 'o', 3])
            model3d.plot_marker([apex_pt], ['magenta', 'o', 3])
            model3d.show()

    df = pd.DataFrame.from_dict(results)
    df.to_excel('analysis.xlsx')


def test():
    c_ps ='12.491543,7.274590,2.559849,13.129617,7.535375,2.601371,13.539355,7.753930,2.563260,14.300272,8.008912,2.737505,14.199818,7.568250,3.487563,13.741894,7.180208,3.867875,13.219227,6.915423,3.858623,12.538903,6.547762,3.827671,11.887283,6.301996,3.772817,11.333023,6.083490,3.627730,10.974407,6.048863,3.314921,10.642883,5.984202,3.028773,10.379838,6.049638,2.577516,10.280509,6.171010,2.375025,11.025223,6.567070,2.306524,11.721344,6.911588,2.405394,12.132643,7.099453,2.485176'
    o_ps = '13.099647,10.275457,1.197713,8.602916,9.101977,1.946230,8.802448,16.156364,4.280861'
    area, angle = crown_analysis(c_ps, o_ps)

    print(f'Area of contact surface : {area}')
    print(f'Angle between contact surface and occlusal plane : {angle}')


if __name__ == '__main__':
    main()






