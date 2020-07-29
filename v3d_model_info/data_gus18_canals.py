# -*- coding: cp949 -*-
'''
Created on 2018. 10. 21.

@author: jongki
'''

from __future__ import division

import os

from class_specimen import Specimen, Canal
from constant import CONST

directory_name = os.getenv('TOOTH_DATA') + '/v3d_gus/'
specimens = []
bounding_box_range = [(-2, 12), (-4, 10), (0, 14)]
canal_pre_suffix = '-canal-pre-zoff.v3d'
canal_post_suffix = '-canal-post-zoff.v3d'
body_suffix = '-solid-body-zoff.v3d'

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
# 0 - G18.MN011.M

s = Specimen('G18.MN011.M')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

# mesio-buccal pre -->  바꿈
ml_pre = '''
    3.27842 5.18846 0.91226
    3.06461 5.48779 1.08330
    2.86505 5.70160 1.51092
    2.72251 5.85839 2.13810
    2.59423 6.11497 3.07886
    2.35191 6.62811 4.44725
    2.26639 6.64236 5.95817
    2.36616 6.57109 7.26954
    2.50870 6.52833 8.55240
    2.92207 6.11497 9.87802
    3.33544 5.88690 10.96133
'''

# LINGUAL - PRE --> 바꿈
mb_pre = '''
    2.90782 4.68957 0.69845
    2.92207 4.49001 0.88375
    2.80804 4.40449 1.14032
    2.63699 4.30471 1.71048
    2.43743 3.94836 2.87931
    2.29489 3.60626 3.73455
    2.28064 3.19290 5.04592
    2.42318 2.75102 6.89894
    2.62274 2.80804 8.75196
    3.10737 2.97909 10.04907
    3.40671 3.43521 11.34618
    '''


s.canals.append(
    Canal(name='pre-mb', length=0.0, furcation_pos=0.0,
          pts_canal=mb_pre, pts_opposite=ml_pre,
          is_buccal_side=True, path=v3d_path))

s.canals.append(
    Canal(name='pre-ml', length=0.0, furcation_pos=0.0,
          pts_canal=ml_pre, pts_opposite=mb_pre,
          is_buccal_side=False, path=v3d_path))

specimens.append(s)


###########
# 1 - G18.MN001

s = Specimen('G18.MN001')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

# mesio-buccal pre -->  바꿈
mb_pre = '''
5.81563 4.24769 0.84099
5.10293 4.93188 1.96705
4.66106 5.54481 3.30693
4.44725 6.01519 4.37598
4.20493 6.30027 5.74436
3.97687 6.51408 6.81341
3.64902 6.47132 7.72567
'''

# LINGUAL - PRE --> 바꿈
ml_pre = '''
5.81563 4.17642 0.84099
5.06017 3.96261 1.95280
4.54703 3.70604 3.24991
4.16217 3.24991 4.58979
3.80582 2.95058 5.82989
3.36394 2.85080 6.95595
3.07886 2.99334 7.73992
'''


s.canals.append(
    Canal(name='pre-mb', length=0.0, furcation_pos=0.0,
          pts_canal=mb_pre, pts_opposite=ml_pre,
          is_buccal_side=True, path=v3d_path))

s.canals.append(
    Canal(name='pre-ml', length=0.0, furcation_pos=0.0,
          pts_canal=ml_pre, pts_opposite=mb_pre,
          is_buccal_side=False, path=v3d_path))

specimens.append(s)


