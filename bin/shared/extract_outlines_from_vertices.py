import numpy as np
from copy import deepcopy

from helpers_geom import is_two_line_segments_intersect_in_XY_plane
from extract_aligned_points_from_outlines import scattered_section_contour_from_facets, ordered_outlines_from_contour_points
from vector_class import vector

INFINITE_VALUE = 10000.0


def get_circle_around_point(center, tangent_vector, radius, magnification_ratio=1):
    """
    center : point
    tangent_vector : tangent vector
        점 p를 지나면서 법선벡터가 t인 평면위의 점들 중 p와의 거리가 radius 인 contour를 반환
    """
    center = vector(center)
    contour = []
    magnification_ratio = int(magnification_ratio)
    for i in range(0, 45 * magnification_ratio, 2 * magnification_ratio):
        for j in range(0, 45 * magnification_ratio, 2 * magnification_ratio):
            # tangent_vector[0], tangent_vector[1], tangent_vector[2] 가  0 인경우 체크
            p1 = None if tangent_vector[2] == 0 else vector([j, i, (
                    tangent_vector.dot(center) - j * tangent_vector[0] - i * tangent_vector[1]) / tangent_vector[2]])
            p2 = None if tangent_vector[1] == 0 else vector(
                [j, (tangent_vector.dot(center) - j * tangent_vector[0] - i * tangent_vector[2]) / tangent_vector[1], i])
            p3 = None if tangent_vector[0] == 0 else vector(
                [(tangent_vector.dot(center) - j * tangent_vector[1] - i * tangent_vector[2]) / tangent_vector[0], j, i])
            for x in [p1, p2, p3]:
                if x:
                    contour.append(center + (x - center) / (x - center).length() * radius)

    return contour


def section_outlines_from_vertices(point, normal_vector, facets, normals, is_canal, magnification_ratio):

    contours_with_neighbors = scattered_section_contour_from_facets(point, normal_vector, facets, normals,
                                                                    magnification_ratio)  # voxel search range는 default 값사용함

    # print(f'{contours_with_neighbors=}')

    if len(contours_with_neighbors) == 0:
        print('empty points')
        return [[]], [], False

    segments = ordered_outlines_from_contour_points(contours_with_neighbors,
                                                    closing_distance_limit=3.5 * magnification_ratio)
    segments = sorted(segments, key=lambda x: -len(x))
    major_segment = find_major_segment(point, deepcopy(segments))

    if not major_segment:
        if is_canal:  # 만일 curve의 점을 포함하는 근관의 contour가 없으면 임의로 만듦
            # todo: change according to image dimensions
            DIAMETER_OF_ARTIFICIAL_CANAL = 0.02 * magnification_ratio
            major_segment = sort_and_segment_vertices(
                get_circle_around_point(point, normal_vector, DIAMETER_OF_ARTIFICIAL_CANAL), None,
                is_canal, magnification_ratio)[0]
        else:
            # flattening of segments
            major_segment = [item for sublist in segments for item in sublist]

        major_segment_exist = False
    else:
        major_segment_exist = True

    return segments, major_segment, major_segment_exist


# def find_major_segment_opencv(center_point, segments):
#     """
#
#     잘안됨//잘안됨//잘안됨//잘안됨//잘안됨//잘안됨
#
#     conter point를 포함한 segment를 찾아서 반환
#     :param center_point:
#     :param segments:
#     :return:
#     """
#     import cv2
#     for segment in segments:
#         points = [np.array(x[:2], np.float32) for x in segment]
#         points = np.array(points, np.float32)
#         if cv2.pointPolygonTest(points, (center_point[0], center_point[1]), True):
#             # print('-- find major segment')
#             return segment
#
#     # print('-- cannot find major segment')
#     return None


def find_major_segment(center_point, segments):
    """
    conter point를 포함한 segment를 찾아서 반환
    :param center_point:
    :param segments:
    :return:
    """

    infinite_point = vector([INFINITE_VALUE, INFINITE_VALUE, INFINITE_VALUE])
    for segment in segments:
        cross_count, segment_org = 0, deepcopy(segment)
        prev_point = start_point = segment.pop()
        while segment:
            cur_point = segment.pop()
            if is_two_line_segments_intersect_in_XY_plane(prev_point, cur_point, center_point, infinite_point):
                cross_count += 1
            prev_point = cur_point
        if is_two_line_segments_intersect_in_XY_plane(prev_point, start_point, center_point, infinite_point):
            cross_count += 1
        if cross_count % 2 == 1:
            return segment_org

    print('        ** No contour including the point! module : sort_and_segment_vertices()')

    # todo check the value
    return None
    # return segments


def extract_outlines_from_vertices_old(point, normal_vector, facets, normals, is_canal, magnification_ratio):
    """
    # type: (object, object, object, object) -> object
    # type: (object, object, object, object) -> object

    :rtype: contour, major_contour, major_contour_exist
    """
    contours_with_neighbors = scattered_section_contour_from_facets(point, normal_vector, facets, normals,
                                                                    magnification_ratio)  # voxel search range는 default 값사용함
    contours = [x[0] for x in contours_with_neighbors]
    major_contour = sort_and_segment_vertices(contours[:], point, is_canal, magnification_ratio)[0] if contours else None

    if not major_contour:
        if is_canal:  # 만일 curve의 점을 포함하는 근관의 contour가 없으면 임의로 만듦
            # todo: change according to image dimensions
            DIAMETER_OF_ARTIFICIAL_CANAL = 0.02 * magnification_ratio
            major_contour = sort_and_segment_vertices(
                get_circle_around_point(point, normal_vector, DIAMETER_OF_ARTIFICIAL_CANAL), None,
                is_canal, magnification_ratio)[0]
        else:
            major_contour = contours[:]  # 만일 curve의 점을 포함하는 치근 contour가 없으면 sorting없이 사용
        major_contour_exist = False

    else:
        major_contour_exist = True

    return contours, major_contour, major_contour_exist


def sort_and_segment_vertices(vertices, inner_vertex=None, is_canal=True, magnification_ratio=0):
    """
        목적 : 윤곽선을 그릴때 필요함, 아티팩트 제거 가능
        기능 : 윤곽선(점들의 리스트)의 점을 인접한 순서대로 정렬함
        현재의 점에서 다음 인접한점과의 거리가 시작점과의 거리보다 길면 분리함
        만일 inside_vertex가 전달되면 inside vertex를 포함하는 선의 집합(원)을 리턴함

    vertices : 윤곽선(점들의 집합)
    inner_vertex : return contour including the inner_vertex
    is_canal : vertices가 canal이면 true, body 이면 false 전달
    """
    assert (magnification_ratio != 0)
    # 분리하지 않을 최소 점의 갯수, 큰 의미가 없는 것 같음
    MIN_POINTS_TO_SEPARATE = 2

    # mn. molar canal의 최소 diameter의 평균 0.4mm이하
    # root surface이면 간격을 넓게 설정
    # 점간 거리가 1.5mm 이상이면 분리 MN53, [9mm]에서 나는 오류 수정을 위해

    # todo: change according to image dimensions
    DIST_TO_SEPARATE = 0.2 if is_canal else 1.5
    DIST_TO_SEPARATE *= magnification_ratio

    sorted_vertices_group = []  # 분리된 점들의 그룹

    vertices = [np.array(x) for x in vertices]

    sorted_vertices = [vertices.pop()]
    while vertices:
        point = sorted_vertices[-1]
        dist_list = ((vertices - point) ** 2).sum(axis=1)  # compute distances
        nearest_ndx = dist_list.argsort()[0]  # indirect sort
        nearest_dist, nearest_vtx = dist_list[nearest_ndx], vertices[nearest_ndx]

        # =======================================================================
        #    아래와 같이 점이 배치된 경우
        #
        #         +(1)                                                       +(4)
        #                                                              +(2)
        #                                                                  +(3)
        #
        # (1) -> (2) 를 연결하면 안됨, 그래서 (1)을 isolated point(아티팩트)로 간주하고 버림
        # =======================================================================
        if len(sorted_vertices) <= MIN_POINTS_TO_SEPARATE and (nearest_dist > DIST_TO_SEPARATE):
            # print 'isolated point'
            sorted_vertices = [vertices.pop(nearest_ndx)]  # 이전 데이터는 버리고 새로 시작

        # =======================================================================
        #    아래와 같이 점이 배치된 경우
        #
        #         +(1)                                                        +(6)
        #     +(2)            +(4)                                      +(5)
        #            +(3)                                                      +(7)
        #
        # (1) -> (2) -> (3) -> (1) 로 연결하면 남은 (4)와 (5) 가 연결괴는 문제 발생함
        #    따라서 다음 인접점을 찾을때 처음 점 (sorted_points[0]) 보다 2배 이하인 점도 연결된 윤곽선으로 포함시킴
        # =======================================================================
        elif len(sorted_vertices) > MIN_POINTS_TO_SEPARATE and (
                nearest_dist > min(vector(point).distance(sorted_vertices[0]) * 2.5, DIST_TO_SEPARATE)):
            #  처음과 마지막점을 연결함, 그리고 묶음에 추가
            sorted_vertices.append(sorted_vertices[0])
            # print len(sorted_points)
            sorted_vertices_group.append([vector(x) for x in sorted_vertices])
            sorted_vertices = [vertices.pop(nearest_ndx)]
        else:
            sorted_vertices.append(vertices.pop(nearest_ndx))

    #  처음과 마지막점을 연결함, 그리고 묶음에 추가
    sorted_vertices.append(sorted_vertices[0])
    sorted_vertices_group.append([vector(x) for x in sorted_vertices])

    '''
    # 연결된 원은 두개이하라고 가정함, 조그만 아티팩트 무시함
    # 점의 갯수가 가장 많은 두개만 선택함
    # --> main canal이 아니면서 더 작은것도 있음
    '''
    # print "** number of sorted point groups : " + str(len(sorted_points_set))
    sorted_vertices_group.sort(key=lambda x: -len(x))

    if inner_vertex:
        infinite_point = vector([INFINITE_VALUE, INFINITE_VALUE, INFINITE_VALUE])
        for sorted_vertices in sorted_vertices_group:
            cross_count, sorted_vertices_org = 0, sorted_vertices[:]
            prev_point = start_point = sorted_vertices.pop()
            while sorted_vertices:
                cur_point = sorted_vertices.pop()
                if is_two_line_segments_intersect_in_XY_plane(prev_point, cur_point, inner_vertex, infinite_point):
                    cross_count += 1
                prev_point = cur_point
            if is_two_line_segments_intersect_in_XY_plane(prev_point, start_point, inner_vertex, infinite_point):
                cross_count += 1
            if cross_count % 2 == 1:
                return [sorted_vertices_org]
        import inspect
        print('        ** No contour including the point! module : sort_and_segment_vertices()')
        print('            caller: {}'.format(inspect.stack()[1]))

        return [None]

    return sorted_vertices_group


