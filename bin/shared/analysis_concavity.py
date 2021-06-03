from constant import CONST
from vector_class import vector


def is_distal_concavity(is_buccal_side, tooth_position):
    if tooth_position in (CONST.UL, CONST.LR):
        return True if is_buccal_side else False
    elif tooth_position in (CONST.UR, CONST.LL):
        return False if is_buccal_side else True
    else:
        return None


def concavity_analysis(contour, c1, c2, tangent_vector, magnification_ratio, is_distal=True):
    """
    :param contour:
    :param c1:
    :param c2:
    :param tangent_vector:
    :param is_distal:
    :return:
    """

    from unused.point_to_line import point2line

    # todo : Caliberating distance btn c1 and c2 to exit function
    if len(contour) == 0 or not c1 or not c2 or vector(c1).distance(vector(c2)) < 0.5 * magnification_ratio:
        return None

    # [dist, nearest_point_on_line, point_on_contour, t, direction]
    DIST, POINT_LINE, POINT_CONTOUR, T_VALUE, DIRECTION = 0, 1, 2, 3, 4

    result = [x for x in [point2line(vtx, c1, c2, tangent_vector) for vtx in contour] if
              (x[DIRECTION] > 0 if is_distal else x[DIRECTION] < 0)]
    result_btn_canal_centers = [x for x in result if 0 < x[T_VALUE] < 1]

    if len(result_btn_canal_centers) == 0:
        return None

    try:
        lowest_contour_of_vtx = min(result_btn_canal_centers, key=lambda x: x[DIST])
        highest_contour_of_vtx_left = max([x for x in result if x[T_VALUE] < lowest_contour_of_vtx[T_VALUE]],
                                          key=lambda x: x[DIST] or [-1])
        highest_contour_of_vtx_right = max([x for x in result if x[T_VALUE] > lowest_contour_of_vtx[T_VALUE]],
                                           key=lambda x: x[DIST] or [-1])
        contour_segment_btn_left_and_right_ends = [x for x in result
                                                   if highest_contour_of_vtx_left[T_VALUE] < x[T_VALUE] <
                                                   highest_contour_of_vtx_right[T_VALUE]]
    except ValueError:
        print("   --> Concavity calcualtion error!")
        return None

    '''
               CV_P_21        CV_P_12          CV_P_22
    --------------+-------------+---------------+------------------------
               '       '        |             '    '  
          '              '      |cv_DIST '            '
       '                    '   +     '                  '
      '                                                   '
      '          ***          CV_P_11          ***      
    '''

    result2 = [point2line(x[POINT_CONTOUR], highest_contour_of_vtx_left[POINT_CONTOUR],
                          highest_contour_of_vtx_right[POINT_CONTOUR], tangent_vector)
               for x in contour_segment_btn_left_and_right_ends]

    concave_point = max(result2, key=lambda x: x[DIST])

    return [concave_point[DIST], concave_point[POINT_CONTOUR], concave_point[POINT_LINE],
            highest_contour_of_vtx_left[POINT_CONTOUR], highest_contour_of_vtx_right[POINT_CONTOUR]]