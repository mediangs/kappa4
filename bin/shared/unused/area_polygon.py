'''
Created on 2013. 10. 16.

@author: jongki

from
http://stackoverflow.com/questions/12642256/python-find-area-of-polygon-from-xyz-coordinates

'''

import numpy as np

#unit normal vector of plane defined by points a, b, and c
def unit_normal(a, b, c):
    x = np.linalg.det([[1,a[1],a[2]],
         [1,b[1],b[2]],
         [1,c[1],c[2]]])
    y = np.linalg.det([[a[0],1,a[2]],
         [b[0],1,b[2]],
         [c[0],1,c[2]]])
    z = np.linalg.det([[a[0],a[1],1],
         [b[0],b[1],1],
         [c[0],c[1],1]])
    magnitude = (x**2 + y**2 + z**2)**.5
    return (x/magnitude, y/magnitude, z/magnitude)

#area of polygon poly
def poly_area(poly):
    if len(poly) < 3: # not a plane - no area
        return 0
    total = [0, 0, 0]
    N = len(poly)
    for i in range(N):
        vi1 = poly[i]
        vi2 = poly[(i+1) % N]
        prod = np.cross(vi1, vi2)
        total[0] += prod[0]
        total[1] += prod[1]
        total[2] += prod[2]
    result = np.dot(total, unit_normal(poly[0], poly[1], poly[2]))
    return abs(result/2)

if __name__ == '__main__':
    poly = [[0, 0, 0], [10, 0, 0], [10, 3, 4], [0, 3, 4]]
    poly_translated = [[0+5, 0+5, 0+5], [10+5, 0+5, 0+5], [10+5, 3+5, 4+5], [0+5, 3+5, 4+5]]
    print(poly_area(poly))
