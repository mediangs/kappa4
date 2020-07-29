# -*- coding: cp949 -*-
'''
Created on 2019. 6. 23.

@author: jongki
'''

from __future__ import division

import os

from class_specimen import Specimen, Canal
from constant import CONST

directory_name = os.getenv('TOOTH_DATA') + '/stl_ljkrp/'
specimens = []
bounding_box_range = [(-2, 12), (-4, 10), (0, 14)]
canal_pre_suffix = '-canal.stl'
body_suffix = '-body.stl'

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

s = Specimen('ljkrp')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)


mb_pre = '''
5.366029 6.525118 0.599091
5.176844 6.674575 1.173963
5.030398 7.019057 2.109275
4.714388 7.119726 3.255291
3.863570 7.201030 4.728746
2.999709 7.959655 6.692860
2.743892 8.505924 8.834526
2.983515 8.646104 10.703538
3.409115 8.805276 12.356708
3.939306 8.440889 13.422571
4.219018 8.009228 14.135477
4.583006 7.794048 14.660057
'''
BPV = '''
2.79660 8.26590 8.67300
3.04440 5.32770 8.67300
'''

s.canals.append(
    Canal(name='pre-mb', length=0.0, furcation_pos=0.0,
          pts_canal=mb_pre, pts_vector=BPV,
          is_buccal_side=True, path=v3d_path))

specimens.append(s)
