from __future__ import division

from math import pi
import numpy as np
from shapely.geometry import Polygon

from rotate import get_rotated_points, rotation_matrix_for_the_plane

EPSILON = 1e-7


def rotated_polygon_object(c, n, P0):  # center, normal, points

    P0_r = get_rotated_points(c, n, P0)
    # assert all(abs(np.hstack((P0_r[:,2], P1_r[:,2])) - c[2]) < EPSILON)
    pg0 = Polygon(P0_r[:, :2])
    return pg0


def outline_centroid(c, n, P0):
    """

    :param c: center
    :param n: normal
    :param P0: points
    :return:
    """
    P0_r = get_rotated_points(c, n, P0, [0, 0, 1.0])
    rot_matrix =rotation_matrix_for_the_plane(c, n, [0, 0, 1.0])
    inverse_rot_matrix = np.linalg.inv(rot_matrix)
    translation_vector = inverse_rot_matrix.dot(P0_r[0]) - P0[0]

    z_coord = P0_r[0][2]
    centroid_xy_plane = np.array(Polygon(P0_r[:, :2]).centroid)
    centroid_xyz_plane = np.append(centroid_xy_plane, z_coord)
    centroid_of_original_plane = inverse_rot_matrix.dot(centroid_xyz_plane)

    return centroid_of_original_plane - translation_vector


def outline_area(c, n, P0):  # center, normal, points
    return rotated_polygon_object(c, n, P0).area


def outline_roundness(c, n, P0): # center, normal, points
    """
    https://en.wikipedia.org/wiki/Roundness_(object)

    A common definition used in digital image processing (image analysis) for characterizing 2-D shapes is:
    Circularity = Perimeter^2 / (4 * pi * Area).
    This ratio will be 1 for a circle and greater than 1 for non-circular shapes.

    Another definition is the inverse of that:
    Circularity = (4 * pi * Area) / Perimeter^2, which is 1 for a perfect circle and goes down
    as far as 0 for highly non-circular shapes.

    :param c:
    :param n:
    :param P0:
    :return:
    """
    polygon = rotated_polygon_object(c, n, P0)
    perimeter = polygon.length
    area = polygon.area
    return (4*pi*area)/(perimeter)**2


def test():
    import point_data as p

    area = outline_area(p.c, p.n, p.P0)
    roundness = outline_roundness(p.c, p.n, p.P0)
    centeroid = outline_centroid(p.c, p.n, p.P0)

    print(f'{area=}')
    print(f'{roundness=}')
    print(f'{centeroid=}')


if __name__ == '__main__':
    test()

