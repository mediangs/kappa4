
def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class _Const(object):

    # root or canal
    # MB, DB, P, MB2 = 0, 1, 2, 3
    @constant
    def MB():
        return 0

    @constant
    def DB():
        return 1

    @constant
    def P():
        return 2

    @constant
    def MB2():
        return 3

    # Tooth position : UpperRight, UpperLeft, LowerRight, LowerLeft
    # UR, UL, LR, LL = 0, 1, 2, 3
    @constant
    def UR():
        return 0

    @constant
    def UL():
        return 1

    @constant
    def LR():
        return 2

    @constant
    def LL():
        return 3

    # Curve position : BUCCAL, LINGUAL = 0, 1
    @constant
    def BUCCAL():
        return 0

    @constant
    def LINGUAL():
        return 1

    # Tooth surface : MESIAL, DISTAL, LATERAL = 0, 1, 2
    @constant
    def MESIAL():
        return 0

    @constant
    def DISTAL():
        return 1

    @constant
    def LATERAL():
        return 3

    # FileMovement(vector angle distance) = 0, 1, 2
    @constant
    def FM_VECTOR():
        return 0

    @constant
    def FM_ANGLE():
        return 1

    @constant
    def FM_DISTANCE():
        return 2

    # CanalDimension(p1, p2, width) = 0, 1, 2
    @constant
    def CD_P1():
        return 0

    @constant
    def CD_P2():
        return 1

    @constant
    def CD_WIDTH():
        return 2

    # DentinThickness(p_body, p_canal, thickness, angle)
    @constant
    def DT_P_BODY():
        return 0

    @constant
    def DT_P_CANAL():
        return 1

    @constant
    def DT_THICKNESS():
        return 2

    @constant
    def DT_ANGLE():
        return 3

   # Concavity(cv_dist, cv_p_1, cv_p12, cv_p3, cv_p4)
   # return [concave_point[DIST], concave_point[POINT_CONTOUR], concave_point[POINT_LINE],
   #         highest_contour_of_vtx_left[POINT_CONTOUR], highest_contour_of_vtx_right[POINT_CONTOUR]]

    '''
               CV_P_21        CV_P_12          CV_P_22
    --------------+-------------+---------------+------------------------
               '       '        |             '    '  
          '              '      |cv_DIST '            '
       '                    '   |     '                  '
      '                         +                          '
      '          ***          CV_P_11          ***      
    '''

    @constant
    def CV_DIST():
        return 0

    @constant
    def CV_P_11():
        return 1

    @constant
    def CV_P_12():
        return 2

    @constant
    def CV_P_21():
        return 3

    @constant
    def CV_P_22():
        return 4

CONST = _Const()



if __name__ == '__main__':
    print(CONST.LL)
    print(CONST.BUCCAL)

