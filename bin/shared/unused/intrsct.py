from __future__ import division

from math import pi, acos

import numpy as np
from shapely.geometry import Polygon

from point_data import *
from rotate import rotation_matrix_with_axis_and_degree

EPSILON = 1e-7

# center, normal, points
center, normal, outline_pre, P1 = np.array(c), np.array(n), np.array(P0), np.array(P1)
print 'normal:', normal

# rotation matrix (assuming z-component of normal n is positive)
assert normal[2] > 0
axis = np.cross(normal, [0, 0, 1])
print 'rotation axis:', axis
rotation_degree = acos(normal.dot([0, 0, 1]) / np.linalg.norm(normal))
print 'rotation degree: %.1f' % (rotation_degree * 180 / pi)
R = rotation_matrix_with_axis_and_degree(axis, -rotation_degree)

# rotated normal and points aligned to z-axis
rotated_normal = R.dot(normal)
assert abs(rotated_normal[0]) < 1e-7 and abs(rotated_normal[1]) < 1e-7
P0_r, P1_r = R.dot((outline_pre - center).T).T + center, R.dot((P1 - center).T).T + center
assert all(abs(np.hstack((P0_r[:,2], P1_r[:,2])) - center[2]) < EPSILON)

# pre- and post-tx polygons
pg0, pg1 = Polygon(P0_r[:,:2]), Polygon(P1_r[:,:2])
print 'area : %.10f, %.10f' % (pg0.area, pg1.area)

# apply buffer(0) to clean self-touching or self-crossing polygons.
pg0, pg1 = pg0.buffer(0), pg1.buffer(0)
print "area': %.10f, %.10f" % (pg0.area, pg1.area)

# interection polygon(s)
IPG = pg0.intersection(pg1)
print 'intersecting area: %.4f' % IPG.area

# charting
import model3d
import mpl_toolkits.mplot3d as a3
P0P1 = np.vstack((outline_pre, P1))
bmin, bmax = P0P1.min(axis=0), P0P1.max(axis=0)
hsize = max(bmax - bmin) * 0.6
bcenter = (bmin + bmax) / 2
lim = zip(bcenter - hsize, bcenter + hsize)

model3d.init(lim)
model3d.ax.plot(*zip(center, center + normal / 100), color='Coral')
model3d.ax.plot(*outline_pre.T, color='MediumOrchid')
model3d.ax.plot(*P1.T, color='Coral')
model3d.ax.plot(*zip(center, center + rotated_normal / 100), color='b')
model3d.ax.plot(*P0_r.T, color='g')
model3d.ax.plot(*P1_r.T, color='b')
for o in (list(IPG) if 'Collection' in IPG.geom_type else [IPG]):
    if o.geom_type == 'Polygon':
        xy = o.exterior.coords
        xyz = np.hstack((xy, np.zeros((len(xy), 1)) + center[2]))
        p3c = a3.art3d.Poly3DCollection([xyz], facecolor='0.8', edgecolor='0.8')
        model3d.ax.add_collection3d(p3c)
model3d.show()
