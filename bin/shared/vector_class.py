from __future__ import division
from math import sqrt
import numpy as np

'''
from numba import jitclass
from numba import float32
spec = [
    ('array', float32[:]),          # an array field
]
@jitclass(spec)
'''

class vector(list):
    def __add__(self, other):
        assert len(self) == len(other)

        return vector([self[i] + other[i] for i in range(len(self))])

    def __sub__(self, other):
        '''
        ASSUME 3-element vectors
        '''
        # assert len(self) == len(other)
        # return vector([self[i] - other[i] for i in xrange(len(self))])
        return vector([self[0] - other[0], self[1] - other[1], self[2] - other[2]])

    def __mul__(self, other):
        return vector([x * other for x in self])

    def __truediv__(self, other):
        return vector([x / other for x in self])

    def length(self):
        return sqrt(sum(x * x for x in self))

    def dot(self, other):
        '''
        ASSUME 3-element vectors
        '''
        # assert len(self) == len(other)
        # return sum([self[i] * other[i] for i in xrange(len(self))])
        return self[0] * other[0] + self[1] * other[1] + self[2] * other[2]

    def cross(self, other):
        assert len(self) == len(other) == 3
        return vector([self[1] * other[2] - self[2] * other[1],
                       self[2] * other[0] - self[0] * other[2],
                       self[0] * other[1] - self[1] * other[0]])

    def distance(self, other):
        '''
        ASSUME 3-element vectors
        '''
        # assert len(self) == len(other)
        # return sqrt(sum((self[i] - other[i])**2 for i in xrange(len(self))))

        # return sqrt(sum((self[i] - other[i]) * (self[i] - other[i]) for i in xrange(len(self))))

        a, b, c = self[0] - other[0], self[1] - other[1], self[2] - other[2]
        return sqrt(a * a + b * b + c * c)

        #  numpy version
        #return np.linalg.norm(np.array(self) - np.array(other))

    def angle_between(self, other):
        """ Returns the angle in radians between vectors 'v1' and 'v2'::

                > angle_between((1, 0, 0), (0, 1, 0))
                1.5707963267948966
                > angle_between((1, 0, 0), (1, 0, 0))
                0.0
                > angle_between((1, 0, 0), (-1, 0, 0))
                3.141592653589793
        """
        v1_u = self.unit()
        v2_u = other.unit()
        return np.degrees(np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)))

    def clockwise_angle_between(self, other, normal):
        """
        :param other:
        :param normal:
        :return:

          |     * (other)
          |
          |---------* (self)
          normal 이 z 축이라면  양수값 리턴
        """
        from math import atan2
        det = normal.dot(self.cross(other))
        return atan2(det, self.dot(other))

    def unit(self):
        '''
        ASSUME 3-element vectors
        '''
        mag = self.length()
        return vector([x/mag for x in self])

    def scale(self, sc):
        return vector([x * sc for x in self])

    @staticmethod
    def format(v):
        return '(' + ', '.join('%.2f' % x for x in v) + ')'


def test2():
    a, b = vector([1, 0, 0]), vector([0, 1, 0])
    print(f'{a=}')
    deg = a.clockwise_angle_between(b, vector([0, 0, 1]))

    print(f'{deg=}')


def test():

    a, b = vector([1, 0, 0]), vector([0, 1, 0])
    deg = a.clockwise_angle_between(b, vector[0, 0, 1])

    print(f'{deg=}')

    print(a.unit())
    print(a.scale(3))


    print( a.distance(b))
    print(a, b, a + b, a - [1, 1, 1], (a + b) * 2, (a + b) / 2, (a + b).length())
    print(a.dot([1, 3, 6]))
    print(vector([3, -3, 1]).cross([4, 9, 2]))


    from point_data import c, n, P0
    #r_points = get_rotated_points(c, n, P0)

    line = [[6.5272397654390995, 3.147972212206941, 3.912742407578645],
            [6.452328682259192, 3.179249855540362, 3.903525231358949]]
    line2 = [P0[0], P0[len(P0)-10]]



if __name__ == '__main__':
    test2()
