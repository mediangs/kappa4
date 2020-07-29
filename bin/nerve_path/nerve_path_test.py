from math import sqrt
from nerve_path import Nerve_path

class vector(list):
    def __add__(self, other):
        assert len(self) == len(other)
        return vector([self[i] + other[i] for i in range(len(self))])
    def __sub__(self, other):
        assert len(self) == len(other)
        return vector([self[i] - other[i] for i in range(len(self))])
    def __mul__(self, other):
        return vector([x * other for x in self])
    def __truediv__(self, other):
        return vector([x / other for x in self])
    def length(self):
        return sqrt(sum(x * x for x in self))
    def dot(self, other):
        assert len(self) == len(other)
        return sum([self[i] * other[i] for i in range(len(self))])
    def cross(self, other):
        assert len(self) == len(other) == 3
        return vector([self[1] * other[2] - self[2] * other[1],
                       self[2] * other[0] - self[0] * other[2],
                       self[0] * other[1] - self[1] * other[0]])
    @staticmethod
    def format(v):
        return '(' + ', '.join('%.2f' % x for x in v) + ')'


def convert_2_points(ps):
    '''
    convert points in string format to vector points, i.e., convert
        ps = '5.29056 2.96091 1.60821   4.94487 2.47995 2.16432   ...'
      to
        [[5.29056, 2.96091, 1.60821], [4.94487 2.47995 2.16432], ...]
    '''
    plist = [float(x) for x in ps.split()]
    return [plist[i * 3:(i + 1) * 3] for i in range(len(plist) // 3)]

def first_test():
    bounding_box = [(-2, 12), (-4, 10), (0, 14)]
    ps1, ps2 = '''
        5.29056 2.96091 1.60821
        4.94487 2.47995 2.16432
        4.47894 2.37474 3.09618
        3.90780 2.34468 4.44888
        3.47193 2.25450 5.98194
        2.97594 2.23947 7.66530
        2.76552 2.29959 9.22842
        2.79558 2.52504 11.06208
        3.05109 2.91582 12.68532
    ''', '''
        6.80859 2.85570 2.04408
        6.62823 2.63025 2.58516
        6.49296 2.52504 3.69738
        6.41781 2.41983 5.44086
        6.50799 2.34468 7.84566
        6.62823 2.32965 9.37872
        6.37272 2.52504 11.48292
        6.19236 2.94588 13.22640
    '''
    return convert_2_points(ps1), convert_2_points(ps2), bounding_box


def stat(curve):
    alen = curve.get_appr_len()
    print('len: %.2f' % alen)
    n = 50
    for i in range(0, n + 1):
        u = l = i / n
        u1 = curve.length_to_parameter(l)  # parameter u corresponding to l
        print('%.2f: %s, %s,' % (u, vector.format(curve.get_pos(u)), vector.format(curve.get_pos(u1))), end='')
        print('%.3f, %.2f, %.2f' % (alen * l, curve.get_curvature(l), curve.get_torsion(l)))
    n = 100000
    print('max. curvature =', max(curve.get_curvature(i / n) for i in range(0, n + 1)))


pts1, pts2, lim = first_test()

c1, c2 = Nerve_path.create(pts1), Nerve_path.create(pts2)

stat(c1)
