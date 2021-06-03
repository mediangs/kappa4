# -*- coding: utf-8 -*
from __future__ import division

import collections
from math import sin, radians

from constant import CONST
from vector_class import vector
from helpers_geom import is_two_line_segments_intersect_in_XY_plane, degree_between_vectors, mindist_btn_contours, mindist_btn_contours_old, mindist_btn_contour_and_point
from named_tuples import CanalDimension

INFINITE_VALUE = 10000.0
AngleVtx = collections.namedtuple('AngleVtx', 'angle vtx')


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
            dist_angle = degree_between_vectors(major_axis_vector, vtx_body - canal_center, major_axis_tangent_vector)
            vtx_canal = angled_point_from_vertices(canal_center, major_axis_vector, major_axis_tangent_vector,
                                                   canal_contour, dist_angle, magnification_ratio)
            dist = (vector(vtx_canal) - vector(vtx_body)).length()
            iteration_loop += 1

            if dist < mindist:
                vs_body_mindist, vs_canal_mindist, mindist, mindist_angle = vtx_body, vtx_canal, dist, dist_angle

    print(f'{iteration_loop=}')
    return vs_body_mindist, vs_canal_mindist, mindist, mindist_angle


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
        cur_angle = degree_between_vectors(major_axis_vector, (vtx - central_point), tangent_vector)
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
            cur_angle = degree_between_vectors(major_axis_vector, (vtx - major_point), tangent_vector)
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
            cur_angle = degree_between_vectors(major_axis_vector, (vtx - major_point), tangent_vector)
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
