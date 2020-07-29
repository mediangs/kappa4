# -*- coding: utf-8 -*
from __future__ import division

import collections
from math import acos, sin, radians, degrees

import numpy as np

from constant import CONST
from geom import vector
from named_tuples import CanalDimension

INFINITE_VALUE = 10000.0
AngleVtx = collections.namedtuple('AngleVtx', 'angle vtx')


def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)


def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            > angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            > angle_between((1, 0, 0), (1, 0, 0))
            0.0
            > angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def select_specimens(roots, names=None):
    """
    :param roots: list of specimens
    :param names: name of specimens to include analysis
    :return: list of specimens who's name in names
    """
    return roots if not names else [root for root in roots if root.name in names]


def smart_pretty(data, digit_number=4):
    if type(data) is dict:
        for k, v in data.items():
            data.update({k: pretty(v, digit_number)})
        return data
    else:
        return pretty(data, digit_number)


def pretty(lst, digit_number=4):
    depth = lambda L: (isinstance(L, list) or isinstance(L, tuple)) and max(map(depth, L)) + 1

    try:
        if depth(lst) == 0:
            return round(lst, digit_number) if type(lst) is float else lst
        elif depth(lst) == 1:
            return [round(x, digit_number) for x in lst]
        elif depth(lst) == 2:
            return [[round(x, digit_number) for x in xs] for xs in lst]
        elif depth(lst) == 3:
            return [[[round(x, digit_number) for x in xs] for xs in xss] for xss in lst]
        else:
            return '{} depth list is not supported '.format(depth(lst))

    except ValueError:
        print('   --> Empty list in pretty function')
        return lst


def time_to_string(t):
    hr = t / 3600
    mini = (t % 3600) / 60
    sec = (t % 3600) % 60
    return '%d:%d:%d' % (hr, mini, sec)


def convert_to_points(ps):
    """
    convert points in string format to vector points, i.e., convert
        ps = '5.29056 2.96091 1.60821   4.94487 2.47995 2.16432   ...'
      to
        [[5.29056, 2.96091, 1.60821], [4.94487 2.47995 2.16432], ...]
    """
    if ',' in ps:
        plist = [float(x) for x in ps.split(',')]
    else:
        plist = [float(x) for x in ps.split()]

    return [plist[i * 3:(i + 1) * 3] for i in range(len(plist) // 3)]


def shift_points(ps_2_shift, ps_vector, is_buccal_side):
    '''
    :param ps_2_shift:
    :param ps_vector: buccal side to lingual(palatal) side vector
    :param is_buccal_side:  buccal_side -->True: buccal, False : MB2, palatal, lingual
    :return:
    '''

    direction_points = convert_to_points(ps_vector)
    assert (len(direction_points) == 2)

    # 만일 buccal_side가 아니면 방향을 바꿈
    direction_vector = vector(direction_points[1]) - vector(direction_points[0]) if is_buccal_side else vector(
        direction_points[0]) - vector(direction_points[1])

    return [vector(p) + direction_vector for p in ps_2_shift]


def normalize_angle(angle, is_buccal_side, tooth_position):
    """
    curve_position : CONST.BUCCAL or CONST.LINGUAL
    tooth_position : CONST.UR, CONST.UL , CONST.LR , CONST.LL , 치아의 위치
    
    UR-B, UL-L
    LL-B, LR-L ===> Aangle
    
    UR-L, UL-B
    LL-L, LR-B ===> 360 - Angle
    """

    # ===========================================================================
    #                90   Mesial        
    #            ********************
    #          *    |                 *   0
    #   180   *    (+)           +    *
    #          *    |   ******      *
    #            ******        *****
    #               270   Distal
    # 
    # ===========================================================================

    curve_position = CONST.BUCCAL if is_buccal_side else CONST.LINGUAL

    if tooth_position in (CONST.UR, CONST.LL):
        if curve_position == CONST.BUCCAL:
            return angle

        if curve_position == CONST.LINGUAL:
            return 360 - angle

    if tooth_position in (CONST.UL, CONST.LR):
        if curve_position == CONST.BUCCAL:
            return 360 - angle

        if curve_position == CONST.LINGUAL:
            return angle

    return None


def convert_tooth_surface_to_angle(tooth_surface, is_buccal_side, tooth_position):
    """
    tooth_surface : CONST.BUCCAL or CONST.LINGUAL, 구하는 방향
    curve_position : CONST.BUCCAL or CONST.LINGUAL , main curve
    tooth_position : CONST.UR, CONST.UL , CONST.LR , CONST.LL , 치아의 위치
    """
    curve_position = CONST.BUCCAL if is_buccal_side else CONST.LINGUAL
    if tooth_position in (CONST.LL, CONST.UR):
        if curve_position == CONST.BUCCAL:
            if tooth_surface == CONST.MESIAL: return 90
            if tooth_surface == CONST.DISTAL: return 270
        if curve_position == CONST.LINGUAL:
            if tooth_surface == CONST.MESIAL: return 270
            if tooth_surface == CONST.DISTAL: return 90

    if tooth_position in (CONST.LR, CONST.UL):
        if curve_position == CONST.BUCCAL:
            if tooth_surface == CONST.MESIAL: return 270
            if tooth_surface == CONST.DISTAL: return 90
        if curve_position == CONST.LINGUAL:
            if tooth_surface == CONST.MESIAL: return 90
            if tooth_surface == CONST.DISTAL: return 270


def mindist_btn_contours(contour1, contour2):
    from scipy.spatial import distance
    ret = distance.cdist(contour1, contour2, metric='euclidean')
    min_index = np.where(ret == ret.min())

    return ret.min(), contour1[int(min_index[0])], contour2[int(min_index[1])]


def mindist_btn_contours_old(contour1, contour2):
    """
        두 윤곽선(contour)간 최단 거리 구함
        예) 치료전 근관, 치근표면간 최소거리
    """
    assert (len(contour1) > 0 and len(contour2) > 0)
    min_dist = INFINITE_VALUE
    min_p1 = min_p2 = None
    for p1 in contour1:
        cur_min_dist, p2 = mindist_btn_contour_and_point(contour2, p1)
        if cur_min_dist < min_dist:
            min_dist, min_p1, min_p2 = cur_min_dist, p1, p2

    return min_dist, min_p1, min_p2


def mindist_btn_contour_and_point(contour, point):
    """
    윤곽선(contour)과 점의 최단거리를 구함           
    Get min distance and point
    exception handling , no intersection point
    """

    min_dist = INFINITE_VALUE
    min_point = None
    if len(contour) == 0:
        return None, None
    for vtx in contour:
        if (vector(point) - vector(vtx)).length() < min_dist:
            min_dist, min_point = (vector(point) - vector(vtx)).length(), vtx

    return min_dist, min_point


def mindist_btn_contours_crossing_point(body_contour, canal_contour, canal_center,
                                        major_axis_vector, major_axis_tangent_vector, magnification_ratio):
    """
    :param body_contour:
    :param canal_contour:
    :param canal_center:
    :param major_axis_vector:
    :param major_axis_tangent_vector:
    :param magnification_ratio:
    :return:
    윤곽선(contour)과 점의 최단거리를 구함
    Get min distance and point
    exception handling , no intersection point
    """

    mindist = INFINITE_VALUE
    vs_body_mindist, vs_canal_mindist, mindist_angle = None, None, None

    if len(body_contour) == 0:
        return None, None, None, None

    min_threshold, _ = mindist_btn_contour_and_point(body_contour, canal_center)
    min_threshold_margin = 0.4 * magnification_ratio
    iteration_loop = 0
    for vtx_body in body_contour:

        if (vector(vtx_body) - vector(canal_center)).length() - min_threshold_margin < min_threshold:
            dist_angle = angle_btn_vectors(major_axis_vector, vtx_body - canal_center, major_axis_tangent_vector)
            vtx_canal = angled_point_from_vertices(canal_center, major_axis_vector, major_axis_tangent_vector,
                                                   canal_contour, dist_angle, magnification_ratio)
            dist = (vector(vtx_canal) - vector(vtx_body)).length()
            iteration_loop += 1

            if dist < mindist:
                vs_body_mindist, vs_canal_mindist, mindist, mindist_angle = vtx_body, vtx_canal, dist, dist_angle

    print(f'{iteration_loop=}')
    return vs_body_mindist, vs_canal_mindist, mindist, mindist_angle


def angle_btn_vectors(ref_vector, target_vector, tangent_vector=None):
    """
    두 벡터간 각도를 구함
    tangent_vector 가 있으면 방향을 고려함
    0~360을 리턴
    """
    dv1, dv2 = ref_vector / ref_vector.length(), target_vector / target_vector.length()
    angle = degrees(acos(dv1.dot(dv2)))

    if tangent_vector and tangent_vector.dot(dv1.cross(dv2)) < 0:
        angle = 360 - angle

    return angle


def shortest_and_longest_diameter_of_canal(central_point, major_axis_vector,
                                           major_axis_tangent_vector, contour, step_angle):
    """
    canal의 최단거리(canal의 center를 지나는) 거리를 구함
    0~180도까지 step도씩 회전시키면서 최단거리를 구함
    central_point : canal의 center
    major_axis_vector, major_axis_tangent_vector, contour, step
    """

    shortest_diameter = INFINITE_VALUE
    longest_diameter = 0

    angle_vtx_list = angle_vtx_list_around_canal(central_point, major_axis_vector,
                                                 major_axis_tangent_vector, contour)
    assert (len(angle_vtx_list) == 360)

    for i in range(int(len(angle_vtx_list) / 2)):
        p1 = angle_vtx_list[i].vtx  # vertx
        p2 = angle_vtx_list[i + 180].vtx  # opposite vertex
        if (p1 - p2).length() < shortest_diameter:
            p1s, p2s, shortest_diameter = p1, p2, (p1 - p2).length()
        if (p1 - p2).length() > longest_diameter:
            p1l, p2l, longest_diameter = p1, p2, (p1 - p2).length()

    return CanalDimension(p1s, p2s, shortest_diameter), CanalDimension(p1l, p2l, longest_diameter)


def angle_vtx_list_around_canal(central_point, major_axis_vector, tangent_vector, contour):
    target_angle = 0  # major_axis_vector를 기준으로 각도의 차이에 따라 점들을 배열함
    angle_vtx_list = []  # [AngleVtx(angle_diff, vtx), AngleVtx(), ...]
    for vtx in contour:
        cur_angle = angle_btn_vectors(major_axis_vector, (vtx - central_point), tangent_vector)
        cur_angle_diff = cur_angle - target_angle
        angle_vtx_list.append(AngleVtx(cur_angle_diff, vtx))

    angle_vtx_list.sort(key=lambda x: x.angle)  # angle_diff  기준으로 sort
    alpha, beta = abs(360 - angle_vtx_list[len(angle_vtx_list) - 1].angle), abs(angle_vtx_list[0].angle)
    vs_zero_angle = intersection_point_divided_by_angles(angle_vtx_list[len(angle_vtx_list) - 1].vtx,
                                                         angle_vtx_list[0].vtx, alpha, beta, central_point)
    angle_vtx_list.insert(0, AngleVtx(0, vs_zero_angle))
    angle_vtx_list.append(AngleVtx(360, vs_zero_angle))

    cur, last = 0, len(angle_vtx_list)
    full_angle_vtx_list = []  # [AngleVtx(angle_diff, vtx), AngleVtx(), ...]
    while True:
        for inbtn_vtx in get_inbtn_angle_vtx_list(angle_vtx_list[cur], angle_vtx_list[cur + 1], central_point):
            full_angle_vtx_list.append(inbtn_vtx)
        cur += 1
        if cur > last - 2:
            break

    # 마지막 element(360) 을 맨 앞으로 넣음, 0,1,2 ... , 359 가 되도록 배열
    full_angle_vtx_list.insert(0, AngleVtx(0, full_angle_vtx_list.pop(len(full_angle_vtx_list) - 1).vtx))
    return full_angle_vtx_list


def get_inbtn_angle_vtx_list(angle_vtx1, angle_vtx2, central_point):
    angles = range(int(angle_vtx1.angle) + 1, int(angle_vtx2.angle) + 1)
    inbtn_angle_vtx_list = []

    for angle in angles:
        alpha, beta = abs(angle_vtx2.angle - angle), abs(angle_vtx1.angle - angle)
        inbtn_vtx = intersection_point_divided_by_angles(angle_vtx2.vtx, angle_vtx1.vtx, alpha, beta, central_point)
        inbtn_angle_vtx_list.append(AngleVtx(angle, inbtn_vtx))

    return inbtn_angle_vtx_list


def intersection_point_divided_by_angles(p1, p2, alpha, beta, p_major):
    # =======================================================================
    #                   . p1
    #                 .    .
    #               .        + (intersect_point)
    #             .       .     .   
    #           .alpha.           .      
    #         .   .                 .              
    #       . .   beta                .                     
    #      *---------------------------*        
    #    p_major                        p2    
    #                                                
    # =======================================================================

    a_ratio = (p1 - p_major).length() * sin(radians(alpha))
    b_ratio = (p2 - p_major).length() * sin(radians(beta))
    return (p2 * a_ratio + p1 * b_ratio) / (a_ratio + b_ratio)


def angled_point_from_vertices(major_point, major_axis_vector, tangent_vector,
                               contour, target_angle, magnification_ratio, is_sorted=True):
    """
        특정 점(major point)에서 특정 각(target_angle)을 이루는 선과
        윤곽선(contour)과 교차점을 구함
    # ==============================================================================
    #            target_point
    #           ..*... vs       ....
    #         .. /    ..........     ...
    #      ..   /  target_angle          ..............
    #    .     +---------------->+ major_axis_vector   .
    #     .  major point                           ..
    #       .......................................
    # ========================================================================
    #  cur_angle_diff 구하기
    #                 *(A)
    #                 |
    #                 |(O)
    #   --------------+----------------
    #                /|\\
    #               / | \\
    #            (B)    (C)
    #   각 AOB가 -170 각 AOC가 -190이라면, 각 AOC는 -190 + 360 = 170임
    # ========================================================================
    #               target axis
    #            h.  |
    #              g.|.f
    #                |   .e
    #                |    .d
    #           b.   | .c
    #       a.       |
    #                |
    #  --------------+----------------
    #                |
    #                |
    #
    # 1) 점들이 a,b,c,d,...로 정렬이 되어 있다면
    #    점b를 탐색시 연결된 전후의 점 a, c를 찾고, 이중 target axis반대쪽에 있는 점이 있는지 조사함, 거리 저장
    #    점g를 탐색시 f도 반대측 인접점으로 찾음, 이전의 것들과 거리를 비교함
    # 2) 점들이 정렬 안된경우
    #    target axis에 근접한 점들을 거리와 함께 조사함
    #
    # ========================================================================

    """
    # if None in contour: return None
    SerialPoint = collections.namedtuple('SerialPoint', 'index angle distance vtx')

    POS_SLOT, NEG_SLOT = 0, 1
    nearest_apposing_vertex = [[], []]
    if is_sorted:  # 점들이 순서대로 정렬되어 있는 경우
        all_data_list = []  # [SerialPoint(index, distance, angle_diff, v), ...]
        for i, vtx in enumerate(contour):
            cur_angle = angle_btn_vectors(major_axis_vector, (vtx - major_point), tangent_vector)
            cur_angle_diff = cur_angle - target_angle
            if cur_angle_diff >= 180:
                cur_angle_diff -= 360
            elif cur_angle_diff <= -180:
                cur_angle_diff += 360

            assert (cur_angle_diff <= 180 or cur_angle_diff >= -180)
            all_data_list.append(SerialPoint(i, cur_angle_diff, (vtx - major_point).length(), vtx))

        last_index = len(all_data_list) - 1  # max(all_data_list, key=lambda x: x.index).index

        pos_angle_list = [x for x in all_data_list if x.angle > 0]  # 각도가 양수인것만 필터링
        neg_angle_list = [x for x in all_data_list if x.angle < 0]  # 각도가 음수인것만 필터링

        # 만일 모든 각도가 음수이면(점들이 한쪽으로 몰여 있는 경우)
        # 가장 작은 각도의 점을 내 보냄
        if len(pos_angle_list) == 0 or len(neg_angle_list) == 0:
            print(' ==== 외곽선이 한쪽으로 모여 있어 정확한 각도의 점을 구할수 없음 ===')
            # all_data_list.sort(key=lambda x: abs(x.angle))
            # return all_data_list[0].vtx
            return min(all_data_list, key=lambda x: abs(x.angle)).vtx

        pos_angle_list.sort(key=lambda x: abs(x.angle))  # angle_diff  기준으로 sort
        nearest_apposing_vertex[POS_SLOT] = nearest_apposing_vertex[NEG_SLOT] = pos_angle_list[0]

        for e in pos_angle_list:
            e_prev = max(all_data_list, key=lambda x: x.index) if e.index == 0 else \
                [x for x in all_data_list if x.index == e.index - 1][0]
            e_next = [x for x in all_data_list if x.index == 0][0] if e.index == last_index else \
                [x for x in all_data_list if x.index == e.index + 1][0]
            e_opp = e_prev if e_prev.angle <= 0 else e_next if e_next.angle <= 0 else None

            if e_opp and abs(e.angle - e_opp.angle) < 180 and (
                    nearest_apposing_vertex[POS_SLOT].distance + .5 > e.distance):  # 이전보다 2mm 작아지면 step으로 가정
                # print e
                # print e_opp
                nearest_apposing_vertex[POS_SLOT], nearest_apposing_vertex[NEG_SLOT] = e, e_opp

    else:  # 점들이 순서대로 정렬되어 있지 않은 경우
        pos_and_neg_list = [[], []]  # _neg, v_set_pos =[], [] # set of [distance, angle_diff, v]
        for i, vtx in enumerate(contour):
            cur_angle = angle_btn_vectors(major_axis_vector, (vtx - major_point), tangent_vector)
            cur_angle_diff = cur_angle - target_angle
            if cur_angle_diff >= 180:
                cur_angle_diff -= 360
            if cur_angle_diff <= -180:
                cur_angle_diff += 360
            assert (cur_angle_diff <= 180 or cur_angle_diff >= -180)

            pos_and_neg_list[0 if (cur_angle_diff < 0) else 1].append(
                SerialPoint(i, cur_angle_diff, (vtx - major_point).length(), vtx))

        # todo: change according to image dimensions
        JUMPING_DIST = 2 * magnification_ratio

        for i, half_list in enumerate(pos_and_neg_list):
            if not half_list:
                # 만일 모든 점들이 한쪽으로 몰려 있는경우, 원하는 각도의 점이 없는 경우 None을 반환
                print("   --> Unable to calculate the vertex of designate angle")
                return None
            else:
                half_list.sort(key=lambda x: abs(x.angle))  # angle_diff  기준으로 sort
                nearest_apposing_vertex[i] = prev_e = half_list.pop(0)
                e = half_list.pop(0) if half_list else prev_e
                while half_list and abs(e.angle) < 20:
                    if (nearest_apposing_vertex[i].distance > e.distance) and (
                            (prev_e.distance - e.distance) > JUMPING_DIST):  # 이전보다 2mm 작아지면 step으로 가정
                        nearest_apposing_vertex[i] = e
                    prev_e, e = e, half_list.pop(0)

    a, b = nearest_apposing_vertex[POS_SLOT].vtx, nearest_apposing_vertex[NEG_SLOT].vtx
    alpha, beta = abs(nearest_apposing_vertex[POS_SLOT].angle), abs(nearest_apposing_vertex[NEG_SLOT].angle)
    a_ratio = (a - major_point).length() * sin(radians(alpha))
    b_ratio = (b - major_point).length() * sin(radians(beta))
    return (b * a_ratio + a * b_ratio) / (a_ratio + b_ratio)


def intersection_point_of_plane_and_line(point_in_plane, normal_vector_of_plane, point_in_line, vector_of_line):
    """
    point_in_plane    : 평면의  임의의  점
    normal_vector_of_plane    : 평면의 법선벡터
    point_in_line     : 직선위의 임의의 점
    vector_of_line     : 직선의 벡터
    """

    t = (point_in_plane - point_in_line).dot(normal_vector_of_plane) / normal_vector_of_plane.dot(vector_of_line)

    return point_in_line if t == 0 else point_in_line + vector_of_line * t


def intersection_point_of_plane_and_curve(point, normal_vector, curve):
    """
    get intersection point of curve and plane defined by point point and
      normal_vector normal_vector (direction of normal of the plane)
    
    NOTE return None if there does not exist that point
    """
    u, inc, EPSILON = 0.0, 0.01, 0.00000001
    sign = normal_vector.dot(point - curve.get_pos(0)) > 0
    p_prev, u_prev = None, None
    while 0.0 <= u <= 1.0:
        u += inc
        p1 = curve.get_pos(u)
        if sign != (normal_vector.dot(point - p1) > 0):
            if inc <= EPSILON:
                return (vector(p1) + p_prev) / 2, (u_prev + u) / 2
            sign, inc = not sign, inc * -0.1
        p_prev, u_prev = p1, u
    return None, None


def curve_to_points(np, n=100):
    '''
    get list of (n + 1) points along nerve path corresponding to u from 0 to 1
    '''
    return [np.get_pos(i / n) for i in range(0, n + 1)]


def is_line_inside_outline(p1, p2, outline):
    """
    두 점이 하나의 폐곡선 안에 속해 있는지 체크함
    동일한 근관을 #
    """

    cross_count = 0
    prev_point = start_point = outline.pop()

    while outline:
        cur_point = outline.pop()
        if is_two_line_segments_intersect_in_XY_plane(prev_point, cur_point, p1, p2):
            cross_count += 1
        prev_point = cur_point

    if is_two_line_segments_intersect_in_XY_plane(prev_point, start_point, p1, p2):
        cross_count += 1

    return True if cross_count % 2 == 0 else False


def is_two_line_segments_intersect_in_XY_plane(AP1, AP2, BP1, BP2):
    """
    두선분이 교차하는지 체크함
    x,y축만으로 계산, z축 좌표는 무시
    폐곡선안에 특정 점이 포함되었는지 판단하기 위해 사용함
    """

    under = (BP2[1] - BP1[1]) * (AP2[0] - AP1[0]) - (BP2[0] - BP1[0]) * (AP2[1] - AP1[1])
    if under == 0: return False

    _t = (BP2[0] - BP1[0]) * (AP1[1] - BP1[1]) - (BP2[1] - BP1[1]) * (AP1[0] - BP1[0])
    _s = (AP2[0] - AP1[0]) * (AP1[1] - BP1[1]) - (AP2[1] - AP1[1]) * (AP1[0] - BP1[0])

    t, s = _t / under, _s / under

    if t < 0.0 or t > 1.0 or s < 0.0 or s > 1.0: return False
    if _t == 0 and _s == 0: return False

    # IP->x = AP1[0] + t * (double)(AP2[0]-AP1[0]);
    # IP->y = AP1[1] + t * (double)(AP2[1]-AP1[1]);
    return True


def test2():
    import point_data as pd
    import time
    s1 = time.time()
    r1 = mindist_btn_contours(pd.P0, pd.P1)
    s2 = time.time()
    r2 = mindist_btn_contours_old(pd.P0, pd.P1)
    s3 = time.time()
    print(f'r1: {r1}')
    print(f'r2: {r2}')

    print(f't1: {s2 - s1}')
    print(f't2: {s3 - s2}')


def test():
    a, b, c, d = vector([0, 0, 0]), vector([5, 5, 4]), vector([0, -5, 0]), vector([-5, 0, 4])
    print(is_two_line_segments_intersect_in_XY_plane(a, b, c, d))


if __name__ == '__main__':
    import time

    s = time.time()
    test2()
    e = time.time()
    print(e - s)

    '''
    print angle_btn_vectors(a,z)
    for x in range(-100, 100, 7 ) :
        for y in range (-100, 100, 7) :
            print angle_btn_vectors(vector([x,y,0]), a, z ),angle_btn_vectors(vector([x,y,0]), a, vector([0,0,1]) ) 

    '''
