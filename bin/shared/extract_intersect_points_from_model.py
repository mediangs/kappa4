# -*- coding: utf-8 -*
import operator
from math import tan, radians

import dist_util as du
from geom import vector


def _is_plane_intersect_with_line_segment(p, t, vtx1, vtx2):
    """
    :param p: 평면위의 한 점
    :param t: 법선벡터
    :param vtx1: 선분의 끝점
    :param vtx2: 선분의 끝점
    :return:
    """
    # x(intersection) is in btn vtx1 and vtx2
    return True if t.dot(p - vtx1) * t.dot(p - vtx2) < 0 else False


def _intersected_line_segments_from_facet(p, t, facet):
    """
    :param p: 평면위의 한 점
    :param t: 평면법선벡터
    :param facet: 공간상의 삼각형 좌표
    :return:
    """
    vtx_a, vtx_b, vtx_c = facet  # three vertexes in a facet(triangle)
    combinations = [[vtx_a, vtx_b], [vtx_a, vtx_c], [vtx_b, vtx_c]]
    intersections = [c for c in combinations if _is_plane_intersect_with_line_segment(p, t, c[0], c[1])]
    # x좌표 값울 기준으로 정렬, 중복을 체크하기 위해
    return sorted([sorted(e, key=operator.itemgetter(0)) for e in intersections])


def _intersected_point_from_line_segment(p, t, line_segment):
    """
    :param p:  평면위의 한 점
    :param t:  평면법선벡터
    :param line_segment: [선분끝점1, 선분끝점2, 법선벡터1, (법선벡터2)]
    :return: [intersected_point, 선분끝점1, 선분끝점2, 법선벡터1, 법선벡터2]
    """
    if len(line_segment) > 4:
        print(f'more number of nomrals({len(line_segment) - 2}) than expected, 2 normals are expected')
        v1, v2, n1, n2 = line_segment[0:4]
    elif len(line_segment) == 4:
        v1, v2, n1, n2 = line_segment
    else:
        v1, v2, n1 = line_segment
        n2 = n1

    v1, v2 = vector(v1), vector(v2)
    k = t.dot(p - v2) / t.dot(v1 - v2)
    assert (0 < k < 1)
    # if (v1-v2).length() > .5 : print (v1-v2).length()
    intersected_point = (v1 - v2) * k + v2

    return [intersected_point, v1, v2, n1, n2]


def _is_std_clockwise_relation(v1, v2, normal):
    return True if v1.clockwise_angle_between(v2, normal) < 0 else False


def _common_normal_of_pair_of_vectors(n1, n2):
    """
    :param n1: [법선벡터1-1, 법선벡터1-2]
    :param n2: [법선벡터2-1, 법선벡터2-2]
    :return:
    n1과 n2의 교집합을 찾고 없으면 4개의 평균을 반환
    """
    n1, n2 = [vector(x) for x in n1], [vector(x) for x in n2]
    normal = [x for x in n1 if x in n2]
    return normal[0] if len(normal) > 0 else (n1[0] + n1[1] + n2[0] + n2[1]).unit()


def is_clockwise_relation(e1, e2):
    """
    :param e1: [p1_intersect, p1_leaf1, p1_leaf2, p1_normal1, p1_normal2 ]
    :param e2: [p2_intersect, p1_leaf1, p1_leaf2, p2_normal1, p2_normal2 ]
    :return:
    """
    normal = _common_normal_of_pair_of_vectors(e1[3:5], e2[3:5])
    return _is_std_clockwise_relation(e1[0], e2[0], normal)


def _sort_linked_elements(seed, elements, is_right_direction):
    """
    :param seed: [p1_intersect, p1_leaf1, p1_leaf2, p1_normal1, p1_normal2 ]
    :param elements: [[], [],...]
    :param t: normal vector of the current plane
    :param is_right_direction:
    :return:
    """
    # 첫번째 요소가 찿는 기준점
    linked_elements = [[seed[0].clockwise_angle_between(x[0], _common_normal_of_pair_of_vectors(seed[3:5], x[3:5])), x]
                       for x in elements]
    linked_elements.append([0, seed])
    linked_elements.sort(key=lambda x: x[0])  # sort by relation(angle)
    points = [x[1] for x in linked_elements]

    if (is_right_direction and seed == points[0]) or (not is_right_direction and seed == points[-1]):
        return points
    else:
        # distances = [seed[0].distance(x[0]) for x in points]
        # print(f'----bug {is_right_direction = } {distances = }')
        return list(reversed(points))


def _check_connectivity(e1, e2):
    """
    :param e1: [p1_intersect, p1_leaf1, p1_leaf2, p1_normal1, p1_normal2 ]
    :param e2: [p1_intersect, p1_leaf1, p1_leaf2, p1_normal1, p1_normal2 ]
    :return:
    e1과 e2의 leaf에 같은 점이 존재하는지 체크
    """
    LEFT, RIGHT = 1, 2
    return True if (e1[LEFT] in [e2[LEFT], e2[RIGHT]]) or (e1[RIGHT] in [e2[LEFT], e2[RIGHT]]) else False


def _seed_index_having_neighbors(cp):
    """
    contour_points점을 하나씩 체크해서 연결점이 있는 인덱스를 반환
    :param cp:
    :return: contour_points의 인덱스
    """
    seed_index = 0
    while seed_index < len(cp):
        seed = cp.pop(seed_index)
        cpis = [i for i, e2 in enumerate(cp) if _check_connectivity(seed, e2)]

        if len(cpis) > 0:
            return seed_index

        cp.insert(seed_index, seed)
        seed_index += 1
    return -1


def _segment_from_contour_using_indices(contour_points, indices, seed, is_right):
    """
    contour_points의 점들중 해당 indices의 점들로 segment를 만듦
    segment에 seed는 뺌
    :param contour_points:
    :param indices:
    :param seed:
    :param is_right:
    :return:
    """

    segment = [contour_points[i] for i in indices]
    segment = _sort_linked_elements(seed['point'], segment, is_right)
    if not is_right:  # left direction
        assert (seed['point'] == segment[-1])
        segment = segment[0:-1]
    else:
        # [MX52-pre-db] 7.30 --> 7.30mm section analysis 에서 assertion error raise
        # assert (seed['point'] == segment[0])
        segment = segment[1:]

    return segment


def probing_next_connection_of_points(indices, contour_points):
    """

    :param indices: contour_points 중 probing할 점들의 index
    :param contour_points:
    :return:
    """
    points = [contour_points[i] for i in indices]

    # 뽑아낸 점들은 list에서 삭제
    for e in sorted(indices, reverse=True): del contour_points[e]

    for i, p in enumerate(points):
        probings = [i for i, e2 in enumerate(contour_points) if _check_connectivity(p, e2)]
        # print(f'{i}, {len(probings)}')
        if len(probings) > 0:
            return indices[i]

    return -1


def _update_seed_segment(left_segment, left_side_indices, right_segment, right_side_indices, seed, seed_segment):
    # 왼쪽 segment 추가
    if seed['first_loop'] or seed['from'] == 'head':  # 왼쪽 추가
        seed_segment[0:0] = left_segment

    elif len(left_segment) > 0:
        seed_segment.extend(left_segment)

    # seed_point 추가
    if seed['first_loop']:
        seed_segment.append(seed['point'])

    elif seed['from'] == 'head' and len(left_segment) > 0:
        seed_segment.insert(len(left_segment), seed['point'])

    elif len(left_segment) > 0 and len(right_segment) > 0:
        pass
        # print(f'it should not happen!!!! {seed}= ')
        # print(f'{left_side_indices = } {right_side_indices = }')
        # seed_segment.insert(len(left_segment), seed['point'])

    elif not seed['first_loop'] and len(right_segment) > 0:
        seed_segment.append(seed['point'])
        if len(left_segment): print('   Seed point added(end)')

    # 오른쪽 segment추가
    if len(left_segment) > 0 and not seed['first_loop']:
        pass
    else:
        seed_segment.extend(right_segment)

    return seed_segment


def ordered_outlines_from_contour_points(contour_points, closing_distance_limit=10000):
    """
    :param contour_points: contour points with neighbors and normal vactor
        [[point, leaf1, leaf2, normal1, normal2],...]
    :param closing_distance_limit:
    :return:
        list of sorted segments

    처음에는 right direction, 끝나면 left_direction으로 진행
    첫번째 점은 left와 right 다 있음
    """


    # print(contour_points)
    close_segment = True
    echo_info = False
    inital_data_length = len(contour_points)
    all_segments, seed_segment = [], []

    seed_index = _seed_index_having_neighbors(contour_points[:])
    seed = {'point': contour_points.pop(seed_index), 'from': 'tail', 'source': 'contour', 'first_loop': True}

    """
    data에서 seed와 연결된 항목을 검색
    1. first_loop에서 seed의 left and right side에서 찾고, seed_segment의 tail에 붙임
    2. seed_segment의 끝요소를 seed로 하고 right side를 찾아 계속 tail에 붙임
    3. 2.의 과정이 끝나 연결된 점이 없으면, seed_segment의 첫번째를 seed로 하고 left side 를 찾아 seed segment의 앞에 붙임
    4. 3.의과정에서 연결점이 없으면, seed_segment의 양끝점의 거리(A)와 seed_segment의 끝점과, contour_points 점들간의 거리(B)를 비교
        A > B  면, seed_segment와 contour_points의 가까운 점을 강제도 연결함   
    5.  A < B  면, seed segment를 all segments에 추가함
    2. 1.의 과정을 반복
    """
    while contour_points:
        both_side_indices = [i for i, e2 in enumerate(contour_points) if _check_connectivity(seed['point'], e2)]

        if len(both_side_indices) == 0:  # 뒤에서 검색해 왔는데 연결점 없는 경우
            # 만일 seed_segment의 마지막 element에
            # 연결된 점들이 없다면, seed_segment의 첫번쨰 element와 연결된 점을 찾음

            # 원상복구, 직전에 pop한 점을 다시넣음
            assert (seed['source'] == 'seed' and seed['from'] == 'tail')
            seed_segment.append(seed['point'])

            # seed_segment의 앞쪽으로 검색시작함
            seed.update({'point': seed_segment.pop(0), 'from': 'head', 'source': 'seed', 'first_loop': False})
            both_side_indices = [i for i, e2 in enumerate(contour_points) if _check_connectivity(seed['point'], e2)]
            if len(both_side_indices) == 0:  # 앞에서 연결시도했는데 연결점 없는 경우
                # 원상복구, 앞쪽에서 pop했기떄문에 다시 집어넣음
                assert (seed['source'] == 'seed' and seed['from'] == 'head')
                seed_segment.insert(0, seed['point'])

                # 현재 Segment에 더 이상 연결된 점이 없을 경우
                # 첫번째와 마지막의 거리가 인접점보다 멀다면 강제로 연결함
                closing_dist = seed_segment[0][0].distance(seed_segment[-1][0])
                nearest_points = [[seed_segment[-1][0].distance(x[0]), i] for i, x in enumerate(contour_points)]
                nearest_points.sort(key=lambda x: x[0])

                '''
                강제 연결시 문제점: 만일 clsoing diatance가 ##너무## 길면, 모든 점들이 다 연결됨
                '''
                if nearest_points[0][0] < closing_dist < closing_distance_limit:  # 강제 연결
                    print(f'  ========CONNECTING LOGICALLY SEPARATED POINTS========= ')
                    # contour_points에서 가장 가까운 점을 뽑아 seed_segment끝에 넣고
                    seed_segment.append(contour_points.pop(nearest_points[0][1]))
                    # seed_segment의 끝점을 뽑아 seed에 넣음
                    seed.update({'point': seed_segment.pop(), 'from': 'tail', 'source': 'contour',
                                 'first_loop': False})
                    both_side_indices = [i for i, e2 in enumerate(contour_points) if
                                         _check_connectivity(seed['point'], e2)]

                else:  # closing, and new seed retrival
                    # closing
                    seed_segment.append(seed['point'])
                    if not close_segment: seed_segment.pop()
                    if len(seed_segment) > 0:
                        all_segments.append([x[0] for x in seed_segment])
                    if echo_info: print(f'----NEW SEGMENT BEGIN {len(all_segments) =}--------')

                    # 새로운 seed를 contour_points에서 꺼냄
                    seed_index = _seed_index_having_neighbors(contour_points[:])
                    if seed_index != -1:
                        seed_segment = []  # start a new segment
                        seed.update({'point': contour_points.pop(seed_index), 'from': 'tail', 'source': 'contour',
                                     'first_loop': True})
                        both_side_indices = [i for i, e2 in enumerate(contour_points) if
                                             _check_connectivity(seed['point'], e2)]
                    else:
                        if echo_info: print(f'No seed remains, remain {len(contour_points) = }')
                        break

        left_side_indices = [i for i in both_side_indices if is_clockwise_relation(seed['point'], contour_points[i])]
        right_side_indices = [i for i in both_side_indices if
                              not is_clockwise_relation(seed['point'], contour_points[i])]
        if echo_info: print(f'{len(left_side_indices) = }  {len(right_side_indices) = }')

        # 예외상황 처리 1 : 왼쪽으로 진행하는데, seed의 오른쪽에 연결점이 새로 나온 경우
        if seed['from'] == 'head' and len(right_side_indices) > 0 and not seed['first_loop']:
            if echo_info: print('EXCEPTION1:')
            i = probing_next_connection_of_points(both_side_indices, contour_points[:])
            if i != -1:
                both_side_indices = left_side_indices = [i]
                right_side_indices = []

        # 예외상황 처리 2 : 오는쪽으로 진행하는데, seed의 왼쪽에 연결점이 새로 나온경우
        if seed['from'] == 'tail' and len(left_side_indices) > 0 and not seed['first_loop']:
            if echo_info: print('EXCEPTION2:')
            i = probing_next_connection_of_points(both_side_indices, contour_points[:])
            if i != -1:
                both_side_indices = right_side_indices = [i]
                left_side_indices = []

        left_segment = _segment_from_contour_using_indices(contour_points, left_side_indices, seed, is_right=False)
        right_segment = _segment_from_contour_using_indices(contour_points, right_side_indices, seed, is_right=True)
        seed_segment = _update_seed_segment(left_segment, left_side_indices,
                                            right_segment, right_side_indices, seed, seed_segment)

        seed.update({'first_loop': False})

        # 뽑아낸 점들은 list에서 삭제
        for e in sorted(both_side_indices, reverse=True): del contour_points[e]

        # seed를 segment의 마지막 인자로 부여, 만일 seed_segment가 하나(seed_point만 있다면?)
        if len(seed_segment) > 1:
            seed.update({'point': seed_segment.pop(), 'from': 'tail', 'source': 'seed'})

        if not contour_points:
            if close_segment: seed_segment.append(seed_segment[0])
            if len(seed_segment) > 0: all_segments.append([x[0] for x in seed_segment])
            if echo_info: print('======= END OF ONE SESSION ============')

    if echo_info:
        seg_len = [len(x) for x in all_segments]
        print(f'{inital_data_length = }, {sum(seg_len) = }, {len(all_segments) = }')

    return all_segments


def scattered_section_contour_from_facets(p, t, facets, normals, magnification_ratio):
    """
    주어진 평면과(point p와 normal vector t)
    v3d 모델이 교차하는 점들의 집합(윤곽선)을 구함
    :param magnification_ratio:
    :param p: (curve 위의) point
    :param t: normal vector
    :param facets: 삼각형 메쉬의 모임, v3d 모델 또는 STL 모델
    :return: list of vertexes
    """

    # ===========================================================================
    # default_search_range : p를 기준으로 z축으로 facets을 검색할 범위
    #          .
    #         /|
    #        / |
    #       /  | tan(A)*IMAGE_WIDTH = SEARCH_RANGE
    #      /A  |
    #     +----+
    #    IMAGE_WIDTH
    # ===========================================================================

    # todo: IMAGE WIDTH change according to image dimensions
    IMAGE_WIDTH = 8 * magnification_ratio  # MX의 경우 8mm 이상되어야함
    SEARCH_RANGE_UPPER = SEARCH_RANGE_LOWER = max(
        abs(tan(radians(du.angle_btn_vectors(t, vector([0, 0, 1])))) * IMAGE_WIDTH), 0.5)

    intersect_line_segments = []  # list pair of vertes in between intersecting point is loacted
    contours_with_neighbors = []

    # Get intersecting facets

    '''
    # partial function을 이용해서 구현해봄
    from functools import partial
    facets_range = [x for x in facets if p[2] - SEARCH_RANGE_LOWER < x[0][2] < p[2] + SEARCH_RANGE_UPPER]
    func_get_intersect_line = partial(_intersected_line_segments_from_facet, p, t)
    intersect_lines = [x for x in list(map(func_get_intersect_line, facets_range)) if x != []]
    flat_intersect_lines = [line for lines in intersect_lines for line in lines]
    # print(f'result {flat_intersect_lines}')
    '''

    for facet, normal in [(x, normals[i]) for i, x in enumerate(facets)
                          if p[2] - SEARCH_RANGE_LOWER < x[0][2] < p[2] + SEARCH_RANGE_UPPER]:

        intersect_lines = _intersected_line_segments_from_facet(p, t, facet)

        for line in intersect_lines:

            if pre_exist_line_indices := [i for i, p in enumerate(intersect_line_segments) if
                                          (p[0] == line[0] and p[1] == line[1]) or (
                                                  p[0] == line[1] and p[1] == line[0])]:
                assert (len(pre_exist_line_indices) == 1)
                intersect_line_segments[pre_exist_line_indices[0]].append(normal)
            else:
                line.append(normal)
                intersect_line_segments.append(line)

    '''
    # removing duplicate lines
    다음과 같이 점의 순서만 바뀐경우 sorting을 해서중복을 찾아냄
    [[1,2,3],[4,5,6]], [[4,5,6], [1,2,3]]
    '''
    # intersect_line_segments = sorted([sorted(e, key=operator.itemgetter(0)) for e in intersect_line_segments])
    # intersect_line_segments = (list(k for k, m in itertools.groupby(intersect_line_segments)))

    # Get intersecting vertexes(points) from facets
    for v in intersect_line_segments:
        point_with_neighbors = _intersected_point_from_line_segment(p, t, v)
        contours_with_neighbors.append(point_with_neighbors)

    # 새로은 sorting algo test
    # test_segment(deepcopy(contours_with_neighbors))

    return contours_with_neighbors


# def test_segment(intersect_contour_points_with_neighbors):
#     segments = ordered_outlines_from_contour_points(intersect_contour_points_with_neighbors)
#     import model3d
#     bounding_box_range = [(0, 60), (30, 120), (0, 200)]
#     model3d.init(bounding_box_range)
#     for seg in segments:
#         model3d.plot_points(seg)
#     for seg in segments:
#         if len(seg) > 5:
#             pass
#             # chart3d.plot_marker(seg[0][:1], ['b'])
#             # chart3d.plot_marker(seg[1][:1], ['m'])
#             # chart3d.plot_marker(seg[2][:1], ['y'])
#             # chart3d.plot_marker(seg[-2][:1], ['r'])
#             # chart3d.plot_marker(seg[-1][:1], ['g'])
#
#     model3d.show()


def test2():
    from tmp_points import contours_with_neighbors as points

    p = [[vector(y[0]), vector(y[1]), vector(y[2]), y[3], y[4]] for y in points]

    segments = ordered_outlines_from_contour_points(p, closing_distance_limit=3.5)

    import model3d
    bounding_box_range = [(0, 60), (30, 120), (0, 200)]
    model3d.init(bounding_box_range)
    for seg in segments[:]:
        model3d.plot_points(seg)
    for seg in segments:
        if len(seg) > 5:
            pass
            # chart3d.plot_marker(seg[0], ['b'])
            # chart3d.plot_marker(seg[1], ['m'])
            # chart3d.plot_marker(seg[2], ['y'])
            # chart3d.plot_marker(seg[-2], ['r'])
            # chart3d.plot_marker(seg[-1], ['g'])

    model3d.show()


if __name__ == '__main__':
    test2()
