# -*- coding: cp949 -*-
'''
Created on 2019. 6. 23.

@author: jongki
'''

from __future__ import division

import os

from class_specimen import Specimen, Canal
from constant import CONST

directory_name = os.getenv('TOOTH_DATA') + '/v3d_g19_mx6/'
specimens = []
bounding_box_range = [(-2, 12), (-4, 10), (0, 14)]
canal_pre_suffix = '-canal.v3d'
body_suffix = '-body.v3d'

# ondemand 에서 realign을 하고 나면 이미지가 flip되서 저장--> 좌우가 바뀜
# ===============================================================================
# LOWER LEFT
#          coronal
#          |
# (L)*     |     *(Distal)
#       *  |  *
#          *
#       *  |  *
#    *     |     * (B)
# (Mesial) |apical
#
# ===============================================================================
# LOWER RIGHT
#          coronal
#          |
# (B)*     |     *(Distal)
#       *  |  *
#          *
#       *  |  *
#    *     |     * (L)
# (Mesial) |apical
#
# ===============================================================================


###########
# 0 - G19.

s = Specimen('G19.MX6.01')
s.tooth_position = CONST.UL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
3.67069  3.65430  0.58993
3.91649  3.34295  1.29457
3.96565  3.27740  2.53998
3.96565  3.22824  3.19546
4.04759  3.09714  4.04759
3.53959  3.03159  4.65391
3.29379  2.93327  5.63713
3.11353  2.90050  6.65312
3.03159  3.04798  7.47247
3.06437  3.14630  8.58679
3.34295  3.52320  9.52085
3.68707  3.78540  10.34020
4.06398  4.12952  11.33980
4.22785  4.03120  12.07722
'''

mb2_pre = '''
3.65430  3.60514  0.55716
3.90011  3.39211  0.95045
3.98204  3.31017  1.54038
4.04759  3.26101  2.39250
4.01481  3.19546  3.31017
4.01481  3.08076  4.11314
4.53920  2.99882  4.30978
4.62113  2.86772  5.03081
5.06358  2.52360  6.17790
5.07997  2.49082  7.29221
5.26023  2.65469  8.22627
5.73545  3.08076  9.45530
5.73545  3.80178  10.29104
5.66990  4.19507  10.79903
5.57158  4.44088  11.22510
5.27661  4.83416  12.14277
'''

s.canals.append(
    Canal(name='pre-mb', length=0.0, furcation_pos=0.0,
          pts_canal=mb_pre, pts_opposite=mb2_pre,
          is_buccal_side=True, path=v3d_path))

s.canals.append(
    Canal(name='pre-mb2', length=0.0, furcation_pos=0.0,
          pts_canal=mb2_pre, pts_opposite=mb_pre,
          is_buccal_side=False, path=v3d_path))

specimens.append(s)
