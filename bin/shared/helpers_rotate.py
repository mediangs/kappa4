
from __future__ import division
from math import sqrt, sin, cos, acos
import numpy as np
from shapely.geometry import Polygon


def get_rotated_points(center, normal, points, rotated_plane_normal=[0, 0, 1]):  # center, normal, points
    # rotation matrix (assuming z-component of normal n is positive)

    points = np.array(points)
    rot_matrix = rotation_matrix_for_the_plane(center, normal, rotated_plane_normal)

    # rotated normal and points aligned to z-axis
    rotated_normal = rot_matrix.dot(normal)
    assert abs(rotated_normal[0]) < 1e-7 and abs(rotated_normal[1]) < 1e-7

    return rot_matrix.dot((points - center).T).T + center


def rotation_axis_and_degree(center, normal, rotated_plane_normal):  # center, normal
    center, normal = np.array(center), np.array(normal)
    normal = normal if normal[2] > 0 else normal * -1
    assert normal[2] > 0

    # ax : rotation axis
    rot_axis = np.cross(normal, rotated_plane_normal)

    # rot : rotation degree
    rot_degree = acos(normal.dot(rotated_plane_normal) / np.linalg.norm(normal))

    return rot_axis, rot_degree


def rotation_matrix_for_the_plane(center, normal, rotated_plane_normal):  # center, normal
    # rotation matrix (assuming z-component of normal n is positive)
    center, normal = np.array(center), np.array(normal)
    normal = normal if normal[2] > 0 else normal * -1
    assert normal[2] > 0

    # ax : rotation axis
    ax = np.cross(normal, rotated_plane_normal)
    # print 'rotation axis:', ax

    # rot : rotation radian
    rot = acos(normal.dot(rotated_plane_normal) / np.linalg.norm(normal))
    # print 'rotation degree: %.1f' % (rot * 180 / pi)

    return rotation_matrix_with_axis_and_degree(ax, -rot)


def rotation_matrix_with_axis_and_degree(axis, theta):
    axis /= sqrt(np.dot(axis, axis))
    a = cos(theta / 2.)
    b, c, d = -axis * sin(theta / 2.)
    return np.array([[a * a + b * b - c * c - d * d, 2 * (b * c - a * d), 2 * (b * d + a * c)],
                     [2 * (b * c + a * d), a * a + c * c - b * b - d * d, 2 * (c * d - a * b)],
                     [2 * (b * d - a * c), 2 * (c * d + a * b), a * a + d * d - b * b - c * c]])


def rotation_matrix_2d(theta):
    return np.array(((np.cos(theta), -np.sin(theta), 0),
                     (np.sin(theta),  np.cos(theta), 0),
                     (0            ,              0, 1)))


def rotated_polygon_object(c, n, P0,  rotated_plane_normal=[0, 0, 1]):  # center, normal, points

    P0_r = get_rotated_points(c, n, P0, rotated_plane_normal)
    # assert all(abs(np.hstack((P0_r[:,2], P1_r[:,2])) - c[2]) < EPSILON)
    pg0 = Polygon(P0_r[:, :2])
    return pg0

def test():

    from point_data import c, n, P0
    r_points = get_rotated_points(c, n, P0)

    line = [[6.5272397654390995, 3.147972212206941, 3.912742407578645],
            [6.452328682259192, 3.179249855540362, 3.903525231358949]]
    line2 = [P0[0], P0[len(P0)-10]]

    r_arrow = get_rotated_points(c, n, line2)
    r_arrow *= [1,1,0]
    print('center', c)
    print(r_arrow[:, :])



def test2():
    points = [[2., 1., 1.], [1., 1., 2.], [1., 2., 1.]]
    MB, DB, P, MB2 = 0, 1, 2, 3

    center = [0, 0, 0]
    r_ps = get_rotated_points(center, get_normal_vector(points), points)

    # Translate to 0, 0 coordinate
    r_ps -= r_ps[DB]

    print(r_ps)

    r_angle = angle_between(r_ps[P], [1.0, 0.0, 0.0])

    print(r_angle)
    print(np.degrees(r_angle))

    r_matrix = rotation_matrix_2d(r_angle)
    print('rotation matrix:')
    print(r_matrix)
    r_ps2 = [r_matrix.dot(p) for p in r_ps]
    print(r_ps2)

    import model3d
    model3d.init([(-3, 3), (-3, 3), (0, 1)], grid=True)
    model3d.plot_points(r_ps, 'ro')
    model3d.plot_points(r_ps2, 'bo')

    model3d.show()


if __name__ == '__main__':
    test3()

