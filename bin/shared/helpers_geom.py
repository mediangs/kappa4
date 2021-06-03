# -*- coding: utf-8 -*
from math import degrees, acos
import numpy as np
from matplotlib import pyplot as plt

from vector_class import vector


INFINITE_VALUE = 10000.0

def unit_vector(v):
    """ Returns the unit vector of the vector.  """
    return v / np.linalg.norm(v)


def radian_between_vectors(v1, v2):
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


def degree_between_vectors(ref_vector, target_vector, tangent_vector=None):
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


def mindist_btn_contours(contour1, contour2):
    """
        두 윤곽선(contour)간 최단 거리 구함
        예) 치료전 근관, 치근표면간 최소거리
    """
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


def curve_to_points(nerve_path, n=100):
    '''
    get list of (n + 1) points along nerve path corresponding to u from 0 to 1
    '''
    return [nerve_path.get_pos(i / n) for i in range(0, n + 1)]


def closest_distance_btn_lines(line1, line2, clampAll=True,
                               clampA0=False, clampA1=False, clampB0=False, clampB1=False):
    '''
    https://stackoverflow.com/questions/2824478/shortest-distance-between-two-line-segments
    Given two lines defined by numpy.array pairs (a0,a1,b0,b1)
    Return the closest points on each segment and their distance
    '''

    a0, a1 = line1
    b0, b1 = line2

    # If clampAll=True, set all clamps to True
    if clampAll:
        clampA0 = True
        clampA1 = True
        clampB0 = True
        clampB1 = True

    # Calculate denomitator
    A = a1 - a0
    B = b1 - b0
    magA = np.linalg.norm(A)
    magB = np.linalg.norm(B)

    _A = A / magA
    _B = B / magB

    cross = np.cross(_A, _B);
    denom = np.linalg.norm(cross) ** 2

    # If lines are parallel (denom=0) test if lines overlap.
    # If they don't overlap then there is a closest point solution.
    # If they do overlap, there are infinite closest positions, but there is a closest distance
    if not denom:
        d0 = np.dot(_A, (b0 - a0))

        # Overlap only possible with clamping
        if clampA0 or clampA1 or clampB0 or clampB1:
            d1 = np.dot(_A, (b1 - a0))

            # Is segment B before A?
            if d0 <= 0 >= d1:
                if clampA0 and clampB1:
                    if np.absolute(d0) < np.absolute(d1):
                        return a0, b0, np.linalg.norm(a0 - b0)
                    return a0, b1, np.linalg.norm(a0 - b1)


            # Is segment B after A?
            elif d0 >= magA <= d1:
                if clampA1 and clampB0:
                    if np.absolute(d0) < np.absolute(d1):
                        return a1, b0, np.linalg.norm(a1 - b0)
                    return a1, b1, np.linalg.norm(a1 - b1)

        # Segments overlap, return distance between parallel segments
        return None, None, np.linalg.norm(((d0 * _A) + a0) - b0)

    # Lines criss-cross: Calculate the projected closest points
    t = (b0 - a0);
    detA = np.linalg.det([t, _B, cross])
    detB = np.linalg.det([t, _A, cross])

    t0 = detA / denom;
    t1 = detB / denom;

    pA = a0 + (_A * t0)  # Projected closest point on segment A
    pB = b0 + (_B * t1)  # Projected closest point on segment B

    # Clamp projections
    if clampA0 or clampA1 or clampB0 or clampB1:
        if clampA0 and t0 < 0:
            pA = a0
        elif clampA1 and t0 > magA:
            pA = a1

        if clampB0 and t1 < 0:
            pB = b0
        elif clampB1 and t1 > magB:
            pB = b1

        # Clamp projection A
        if (clampA0 and t0 < 0) or (clampA1 and t0 > magA):
            dot = np.dot(_B, (pA - b0))
            if clampB0 and dot < 0:
                dot = 0
            elif clampB1 and dot > magB:
                dot = magB
            pB = b0 + (_B * dot)

        # Clamp projection B
        if (clampB0 and t1 < 0) or (clampB1 and t1 > magB):
            dot = np.dot(_A, (pB - a0))
            if clampA0 and dot < 0:
                dot = 0
            elif clampA1 and dot > magA:
                dot = magA
            pA = a0 + (_A * dot)

    return [np.linalg.norm(pA - pB), pA, pB]


def axisEqual3D(ax):
    extents = np.array([getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
    sz = extents[:,1] - extents[:,0]
    centers = np.mean(extents, axis=1)
    maxsize = max(abs(sz))
    r = maxsize/2
    for ctr, dim in zip(centers, 'xyz'):
        getattr(ax, 'set_{}lim'.format(dim))(ctr - r, ctr + r)


def fitted_plane_of_points(points, ref_vector):
    """
    points를 지나는 평면을 구함, ref_vector와 법선벡터의 방향을 맞춤

    :param t_points: np.array
    :param ref_vector: 방향
    :return: 평면의 normal vector, 평면위의 한점
    """
    chart = False

    t_points = points.T

    xs = t_points[0].tolist()
    ys = t_points[1].tolist()
    zs = t_points[2].tolist()

    # do fit
    tmp_A, tmp_b = [], []
    for i in range(len(xs)):
        tmp_A.append([xs[i], ys[i], 1])
        tmp_b.append(zs[i])
    b = np.mat(tmp_b).T
    A = np.mat(tmp_A)

    # Manual solution
    fit = (A.T * A).I * A.T * b
    errors = b - A * fit
    residual = np.linalg.norm(errors)

    a, b, c = fit[0, 0], fit[1, 0], fit[2, 0]

    # a*x + b*y + c = z
    # (-a/c) * x + (-b/c) * y + 1/c * z = 1
    # ==> normal vector (-a/c, -b/c, 1/c)

    normal_vector = np.array([-a/c, -b/c, 1/c])

    # ref_vector와 방향이 반대면 normal vector의 방향을 바꿈
    normal_vector = normal_vector * -1 if degree_between_vectors(vector(normal_vector), ref_vector) > 90 else normal_vector

    # points들의 X, Y, Z 축의 각 중간점
    median_coord = np.median(points, axis=0)
    a_point_on_plane = np.array([median_coord[0], median_coord[1],
                                 a * median_coord[0] + b * median_coord[1] + c])

    if chart:
        degrees = [f'{degree_between_vectors(vector(normal_vector.tolist()), vector(p) - vector(a_point_on_plane)):.2f}' for p in points]
        print(f'solution: {a} x + {b} y + {c} = z')
        # print(f'solution: {normal_vector[0]} x + {normal_vector[1]} y + {normal_vector[2]} z = 1')
        # print("errors: \n", errors)
        print("residual:", residual)
        print(f' angles -- {degrees}')

        plt.figure()
        ax = plt.subplot(111, projection='3d')
        ax.scatter(xs, ys, zs, color='b')
        # normal vector
        ax.plot(*zip(a_point_on_plane, a_point_on_plane + normal_vector * 10), color='r')

        # plot plane
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        X,Y = np.meshgrid(np.arange(xlim[0], xlim[1]),
                          np.arange(ylim[0], ylim[1]))
        Z = np.zeros(X.shape)
        for r in range(X.shape[0]):
            for c in range(X.shape[1]):
                Z[r, c] = fit[0] * X[r, c] + fit[1] * Y[r, c] + fit[2]
        ax.plot_wireframe(X,Y,Z, color='k')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        axisEqual3D(ax)
        plt.show()

    return normal_vector, a_point_on_plane