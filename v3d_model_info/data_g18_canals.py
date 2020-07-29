# -*- coding: cp949 -*-
'''
Created on 2018. 10. 21.

@author: jongki
'''

from __future__ import division

import os

from class_specimen import Specimen, Canal
from constant import CONST

directory_name = os.getenv('TOOTH_DATA') + '/v3d_g18/'
specimens = []
bounding_box_range = [(-2, 12), (-4, 10), (0, 14)]
canal_pre_suffix = '-canal-zoff.v3d'
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
# 0 - G18.1C

s = Specimen('G18.1C')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
5.18846 2.36616 0.82673
4.90338 3.12163 1.91004
4.44725 3.24991 2.86505
3.94836 3.36394 4.14791
3.39245 3.34969 5.61608
3.23566 3.03610 7.09849
3.17864 2.42318 8.62367
3.39245 1.91004 9.66421
3.49223 1.55369 10.39117
'''

ml_pre = '''
6.44281 2.55147 0.51314
6.99871 3.03610 1.48242
7.28379 3.09312 2.29489
7.28379 3.24991 3.52074
7.38357 3.13588 4.88912
7.18402 3.03610 6.34303
6.92744 2.75102 7.79694
6.59960 2.26639 9.23659
6.41430 1.93854 10.36266
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
# 1 - G18.2M

s = Specimen('G18.2M')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
4.74658 3.37820 0.51314
4.61830 3.36394 1.58219
4.27620 3.56350 2.40893
3.93410 3.70604 3.12163
3.52074 3.77731 3.90560
3.05036 3.74880 5.03166
2.83655 3.63477 5.88690
2.69401 3.44947 6.97021
2.65124 3.26417 8.18180
2.69401 3.26417 9.02278
2.80804 3.34969 9.76399
'''

ml_pre = '''
5.63033 5.97243 0.88375
5.24547 5.65884 1.73899
4.66106 5.81563 2.65124
4.03388 6.02944 3.77731
3.66328 6.24325 4.77509
3.30693 6.51408 5.91541
3.20715 6.88468 7.08424
3.16439 7.02722 8.50964
3.34969 7.04148 9.83526
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
# 2 - G18.3M

s = Specimen('G18.3M')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
4.41874 2.28064 0.64143
5.43077 2.08108 2.13810
6.08646 1.96705 3.54925
6.74214 1.85302 5.21696
7.21252 1.88153 7.34081
7.35506 2.42318 9.53593
6.88468 3.26417 11.24641
6.77065 3.83433 12.32971
6.74214 4.34747 12.97114
'''

ml_pre = '''
5.71585 2.50870 0.74121
5.37376 2.08108 2.20937
4.53277 1.85302 3.33544
3.96261 1.85302 4.94614
3.43521 2.08108 6.88468
3.23566 2.62274 8.92300
3.50648 3.40671 10.83304
4.01963 4.03388 12.30120
4.13366 4.37598 12.95689
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
# 0 - G18.4c

s = Specimen('G18.4C')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
4.73233 2.90782 0.21381
4.94614 3.15013 1.09756
4.77509 3.24991 2.08108
4.39023 3.49223 3.20715
3.91985 3.57775 4.56128
3.50648 3.32118 6.38579
3.22140 2.79378 8.11053
3.30693 2.32340 9.33637
2.85080 2.18086 11.03260
'''

ml_pre = '''
5.54481 2.92207 0.41337
5.73011 3.10737 0.95502
5.64458 3.16439 1.51092
5.60182 3.30693 2.32340
5.78712 3.37820 3.53499
5.97243 3.37820 4.68957
6.05795 3.16439 6.25751
5.80138 2.72251 7.85395
5.23122 2.22362 9.15107
4.84636 1.81026 10.23437
4.98890 1.49667 11.08961
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
# 0 - G18.4L

s = Specimen('G18.4L')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
5.64458 1.56794 0.68419
6.10071 2.13810 2.49445
6.55684 2.79378 4.39023
7.28379 3.34969 6.61386
7.85395 3.43521 9.17958
7.82545 3.29267 10.94707
7.65440 3.06461 12.15866
7.42633 2.89356 12.88562
'''

ml_pre = '''
3.91985 2.16661 1.35413
3.33544 2.70826 3.15013
2.87931 3.34969 5.03166
2.62274 3.57775 7.01297
2.53721 3.54925 9.13681
2.53721 3.40671 10.86155
2.99334 2.97909 12.98539
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
# 0 - G18.5M

s = Specimen('G18.5M')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
6.34303 4.56128 0.94076
6.28601 4.17642 1.82451
6.05795 3.96261 2.00981
5.91541 3.47798 2.83655
5.97243 2.70826 4.81785
6.04370 2.36616 6.79916
6.24325 2.39467 8.90875
6.14347 2.59423 10.49094
5.97243 2.96483 11.95911
'''

ml_pre = '''
4.24769 3.60626 0.89800
4.40449 3.10737 2.40893
4.20493 2.73677 4.03388
3.87709 2.35191 5.75862
3.42096 2.28064 7.18402
2.92207 2.39467 9.13681
2.86505 2.73677 10.50520
3.10737 3.15013 11.91634
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
# 0 - G18.7C

s = Specimen('G18.7C')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
4.84636 3.46372 0.27083
4.47576 3.56350 1.01203
4.17642 3.59201 1.73899
3.54925 3.77731 2.82229
2.89356 3.86283 4.03388
2.49445 3.74880 5.53055
2.49445 3.42096 7.08424
2.76528 2.89356 8.43837
2.83655 2.45169 9.60720
2.89356 2.32340 10.29139
'''

ml_pre = '''
6.22900 3.32118 0.74121
6.40005 3.24991 1.51092
6.27176 3.24991 2.28064
6.21474 3.22140 3.09312
6.48557 3.22140 3.86283
6.87043 3.19290 4.80360
6.97021 3.24991 6.00093
6.84192 3.19290 7.15551
6.44281 2.90782 8.26732
6.17198 2.49445 9.10831
6.07220 2.25213 10.30564
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
# 0 - G18.10C

s = Specimen('G18.10C')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
7.15551 3.80582 0.29933
7.42633 3.17864 1.49667
7.48335 2.67975 3.43521
7.59738 2.35191 5.27398
7.32656 2.32340 6.79916
7.51186 2.38042 7.89672
7.42633 2.59423 9.40764
7.15551 2.95058 10.56221
6.55684 3.17864 11.38895
6.27176 3.59201 12.62904
'''

ml_pre = '''
5.53055 4.16217 1.22584
5.44503 3.20715 2.72251
5.34525 2.76528 4.14791
4.98890 2.59423 5.30249
4.46150 2.53721 6.78490
4.13366 2.73677 8.49538
4.23344 3.09312 10.06332
4.19068 3.47798 11.38895
4.26195 3.53499 12.54352
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
# 0 - G18.11C

s = Specimen('G18.11C')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
3.49223 4.84636 0.66994
2.76528 4.30471 3.32118
2.43743 3.56350 5.33100
2.66550 3.05036 7.86821
3.10737 3.23566 9.74974
3.54925 3.52074 11.17514
'''

ml_pre = '''
4.03388 5.31674 0.81248
3.49223 6.40005 2.97909
3.34969 7.02722 4.88912
3.34969 6.98446 6.87043
3.52074 6.74214 8.69494
3.82007 6.30027 9.96355
4.23344 5.88690 11.08961
4.19068 5.71585 12.04463
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
# 0 - G18.12

s = Specimen('G18.12')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
4.94614 0.99778 0.74121
5.87265 1.22584 2.08108
6.51408 2.62274 3.99112
6.87043 2.67975 4.70382
7.21252 2.79378 5.80138
7.35506 2.87931 7.29805
7.55462 2.82229 8.92300
7.38357 2.59423 10.79028
6.92744 2.25213 12.20142
'''

ml_pre = '''
4.07664 1.52518 1.09756
3.83433 2.52296 2.67975
3.26417 3.20715 4.30471
2.80804 3.59201 6.15773
2.67975 3.60626 7.95373
2.80804 3.40671 9.67847
3.26417 2.90782 11.31768
3.63477 2.53721 12.18717
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
# 0 - G18.12C

s = Specimen('G18.12C')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
3.17864 1.45391 0.57016
3.44947 1.82451 1.38264
3.24991 1.98131 2.87931
3.15013 1.91004 4.31896
2.99334 1.89578 5.57331
2.86505 2.00981 7.19827
2.97909 2.28064 8.65218
3.17864 2.59423 9.82101
'''

ml_pre = '''
5.78712 1.45391 1.41115
6.12922 1.93854 2.96483
6.04370 1.98131 4.29045
5.92966 2.00981 5.75862
5.71585 2.09534 7.32656
5.31674 2.36616 8.89450
4.90338 2.82229 10.49094
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
# 0 - G18.14C

s = Specimen('G18.14C')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
5.41652 4.11941 1.19734
5.04592 3.56350 2.28064
5.15995 3.34969 3.70604
5.53055 3.60626 5.24547
6.04370 3.83433 7.08424
6.34303 3.77731 8.52389
6.42855 3.42096 9.66421
6.24325 3.03610 10.31990
'''

ml_pre = '''
4.36172 3.83433 0.74121
4.50426 3.69179 1.83877
4.73233 3.44947 2.46594
4.51852 3.29267 3.59201
4.11941 3.43521 4.93188
3.56350 3.54925 6.78490
3.24991 3.42096 7.93948
3.24991 3.00759 9.25085
3.59201 2.46594 10.29139
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
# 0 - G18.14L

s = Specimen('G18.14L')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
5.73011 3.27842 1.48242
4.57553 3.66328 3.56350
3.63477 4.13366 6.07220
2.99334 4.16217 8.72345
2.83655 3.91985 11.01834
3.02185 3.44947 12.58628
3.29267 2.82229 13.71235
'''

ml_pre = '''
6.34303 3.12163 1.28286
7.66865 3.44947 2.60848
8.53815 4.00537 4.57553
8.75196 4.19068 6.51408
8.80897 3.97687 8.68069
8.46688 3.63477 11.07536
7.76843 2.69401 13.54130
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
# 0 - G18.16L

s = Specimen('G18.16L')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
7.29805 2.33766 0.17105
7.46910 2.89356 2.40893
8.03926 3.54925 5.85839
8.26732 3.72029 8.26732
7.83970 3.40671 10.54796
7.35506 3.00759 12.17292
6.91319 2.62274 13.92616
'''

ml_pre = '''
4.87487 1.68197 1.66772
4.93188 2.50870 2.62274
4.56128 2.97909 3.40671
3.82007 3.36394 4.70382
3.24991 3.63477 6.30027
2.80804 3.66328 8.32434
2.82229 3.43521 10.33415
3.00759 3.00759 12.07314
3.23566 2.48020 13.82638
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
# 0 - G18.19L

s = Specimen('G18.19L')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
7.45484 5.03166 0.48464
7.16976 3.60626 2.60848
7.18402 2.90782 4.84636
7.24103 2.52296 6.97021
7.24103 2.55147 8.58091
7.29805 2.73677 10.47669
7.24103 3.10737 11.84507
7.06998 3.43521 12.54352
'''

ml_pre = '''
4.00537 4.91763 0.99778
3.84858 4.23344 2.45169
3.93410 3.93410 3.30693
3.37820 3.52074 4.93188
3.23566 3.26417 6.78490
3.06461 3.29267 8.65218
3.12163 3.57775 10.50520
3.23566 3.86283 11.68828
3.50648 4.10515 12.60054
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
# 0 - G18.21L

s = Specimen('G18.21L')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
4.74658 2.48020 0.79822
4.31896 3.17864 2.13810
4.61830 3.44947 3.37820
5.25973 3.54925 4.88912
5.67309 3.66328 6.35728
5.90116 3.82007 8.58091
6.14347 3.76306 10.41967
6.24325 3.54925 12.15866
6.14347 3.02185 13.88340
'''

ml_pre = '''
4.50426 2.56572 1.05480
4.04814 3.34969 2.79378
3.42096 3.26417 4.46150
2.70826 2.97909 6.32878
2.49445 2.85080 8.08202
2.38042 2.56572 9.97780
2.46594 2.19512 12.01612
2.80804 1.89578 13.27047
3.09312 1.72473 13.94041
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
# 0 - G18.22L

s = Specimen('G18.22L')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
3.49223 4.61830 0.71270
4.03388 4.44725 1.95280
4.29045 3.89134 3.39245
4.31896 3.20715 5.10293
4.19068 2.53721 7.05573
3.79156 2.12385 9.19383
3.26417 2.50870 11.57425
2.92207 3.13588 13.37025
'''

ml_pre = '''
4.54703 5.87265 1.26861
4.86061 5.40227 2.49445
5.04592 5.08868 3.52074
5.43077 4.76084 5.54481
5.88690 4.70382 7.19827
6.07220 4.71807 9.07980
5.91541 4.94614 11.06110
5.25973 5.10293 12.54352
4.80360 5.08868 13.32749
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
# 0 - G18.24

s = Specimen('G18.24')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
6.07220 1.66772 1.02629
6.20049 2.00981 1.93854
6.40005 2.48020 2.87931
6.48557 2.86505 4.26195
6.59960 3.00759 5.64458
6.74214 2.86505 7.16976
6.87043 2.75102 8.58091
6.98446 2.42318 9.90653
'''

ml_pre = '''
3.77731 1.81026 0.89800
3.69179 1.66772 1.96705
3.60626 1.99556 3.27842
3.37820 2.22362 4.60404
3.52074 2.33766 6.00093
3.63477 2.19512 7.14125
3.74880 2.08108 8.69494
4.00537 1.88153 9.96355
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
# 0 - G18.26

s = Specimen('G18.26')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
4.60404 2.18086 0.21381
4.51852 2.36616 1.51092
4.34747 2.48020 2.70826
4.21918 2.30915 3.83433
3.77731 2.22362 5.23122
3.32118 2.28064 6.61386
3.03610 2.42318 8.26732
2.97909 2.75102 9.86377
3.29267 3.13588 10.98983
3.60626 3.46372 11.84507
'''

ml_pre = '''
4.50426 1.92429 0.21381
4.66106 2.30915 1.16883
4.70382 2.45169 1.89578
5.00315 2.52296 2.87931
5.38801 2.42318 4.16217
5.84414 2.39467 5.33100
6.17198 2.49445 6.20049
6.44281 2.63699 7.42633
6.58535 2.85080 8.60942
6.51408 3.09312 9.63570
6.44281 3.42096 10.60498
6.30027 3.59201 11.20364
6.15773 3.82007 11.78806
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
# 0 - G18.30L

s = Specimen('G18.30L')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
5.15995 5.06017 0.45613
4.88912 5.08868 2.73677
4.96039 5.38801 4.47576
5.06017 5.28823 6.30027
5.44503 5.21696 8.18180
5.85839 5.08868 9.79250
6.25751 4.37598 11.98761
'''

ml_pre = '''
2.55147 3.89134 2.23788
2.22362 3.86283 4.03388
2.05258 3.94836 5.82989
2.15235 3.67753 7.78268
2.28064 3.37820 9.76399
2.52296 3.03610 10.94707
3.03610 2.87931 12.07314
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
# 0 - G18.31

s = Specimen('G18.31')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
4.96039 4.83211 0.19956
5.38801 3.99112 2.15235
5.85839 3.26417 4.16217
6.30027 2.66550 6.07220
6.98446 2.48020 8.13903
7.08424 2.63699 9.72123
6.92744 2.96483 11.18939
6.78490 3.52074 12.42949
'''

ml_pre = '''
5.00315 4.88912 0.19956
4.66106 4.39023 1.16883
4.21918 3.87709 2.23788
4.00537 3.34969 3.67753
3.74880 2.90782 5.10293
3.44947 2.60848 6.64236
3.17864 2.55147 8.53815
3.29267 2.77953 10.12034
3.47798 3.26417 11.48872
3.77731 3.64902 12.50076
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
# 0 - G18.38C

s = Specimen('G18.38C')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
4.74658 4.43299 0.68419
4.46150 3.43521 2.62274
3.87709 2.99334 4.14791
3.05036 2.67975 6.08646
2.82229 2.70826 8.35284
3.07886 3.17864 9.89228
3.34969 3.93410 11.17514
'''

ml_pre = '''
5.43077 4.51852 1.22584
5.70160 3.72029 2.57997
6.15773 3.33544 4.36172
6.37154 3.05036 6.28601
6.34303 3.09312 8.18180
6.01519 3.20715 9.53593
5.38801 4.03388 11.14663
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
# 0 - G18.40

s = Specimen('G18.40')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
4.71807 1.08330 0.44187
5.40227 1.38264 1.66772
5.87265 1.86727 3.26417
6.51408 2.42318 5.10293
6.81341 2.92207 6.61386
6.95595 3.03610 7.86821
6.92744 2.85080 9.76399
6.82767 2.40893 11.43171
'''

ml_pre = '''
4.68957 1.05480 0.44187
4.87487 1.28286 1.85302
4.93188 1.63921 2.96483
4.88912 1.89578 4.01963
4.53277 2.15235 5.37376
4.09090 2.43743 6.95595
4.01963 2.42318 8.38135
4.07664 2.22362 9.80675
4.36172 1.86727 11.43171
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
# 0 - G18.41M

s = Specimen('G18.41M')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
2.12385 3.91985 0.75546
2.67975 4.39023 2.62274
2.80804 4.63255 4.10515
2.85080 4.91763 5.77287
2.95058 5.01741 7.32656
2.87931 5.10293 8.76621
2.80804 5.07442 10.02056
'''

ml_pre = '''
 4.11941 2.82229 1.62496
4.26195 3.22140 2.50870
4.67531 3.13588 3.53499
4.91763 2.99334 4.21918
5.13144 2.79378 5.44503
5.23122 2.75102 6.89894
5.14569 2.77953 8.56665
4.88912 2.87931 9.60720
4.61830 3.00759 10.13459
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
# 0 - G18.48M

s = Specimen('G18.48M')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
5.21696 3.93410 1.35413
4.97465 4.31896 1.93854
5.06017 4.49001 2.60848
5.33100 4.50426 3.63477
5.97243 4.33322 4.70382
6.47132 4.24769 5.94392
6.77065 4.17642 7.25529
6.77065 4.17642 8.33859
6.71363 3.99112 9.29361
'''

ml_pre = '''
3.82007 4.74658 0.55591
3.72029 5.06017 1.62496
3.67753 5.45928 2.83655
3.40671 5.85839 4.21918
3.22140 5.95817 5.78712
3.10737 6.00093 7.45484
3.16439 5.95817 8.59516
3.16439 5.88690 9.23659
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
# 0 - G18.55C

s = Specimen('G18.55C')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
6.17198 3.37820 0.37060
6.04370 3.32118 1.35413
5.94392 3.10737 2.15235
6.07220 3.00759 2.80804
6.45706 2.69401 3.90560
6.71363 2.39467 5.30249
6.65662 2.36616 6.85617
6.49982 2.49445 8.29583
6.14347 2.83655 9.56443
5.98668 3.19290 10.86155
'''

ml_pre = '''
4.70382 4.10515 0.61292
4.58979 3.83433 1.19734
4.31896 4.20493 1.61070
4.13366 3.82007 2.06683
4.04814 3.34969 2.83655
4.03388 3.22140 3.40671
3.69179 3.06461 4.20493
3.36394 2.90782 5.44503
3.30693 2.87931 6.82767
3.62052 3.06461 8.29583
3.77731 3.40671 9.60720
3.56350 3.69179 10.84729
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
# 0 - G18.63

s = Specimen('G18.63')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
5.64458 3.20715 0.85524
6.25751 3.03610 2.60848
6.62811 2.48020 4.93188
6.87043 2.33766 6.97021
7.15551 2.42318 8.82323
6.92744 3.09312 10.66199
7.06998 3.44947 11.91634
7.26954 3.47798 13.18495
'''

ml_pre = '''
4.53277 3.26417 0.89800
4.07664 3.03610 2.16661
3.69179 2.70826 4.13366
3.32118 2.42318 6.18624
3.26417 2.56572 8.43837
3.34969 3.03610 9.87802
3.87709 3.43521 11.21790
4.19068 4.14791 12.27269
3.60626 4.23344 13.27047
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
# 0 - G18.67

s = Specimen('G18.67')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
4.90338 3.94836 0.48464
5.53055 3.10737 1.71048
5.97243 2.57997 2.95058
6.34303 2.29489 4.54703
6.72789 2.13810 6.14347
6.87043 1.92429 7.78268
7.05573 2.03832 9.90653
6.87043 2.39467 11.60276
6.42855 2.66550 12.47225
'''

ml_pre = '''
3.50648 4.66106 0.48464
3.69179 4.11941 1.48242
3.67753 3.56350 2.72251
3.77731 3.13588 4.46150
3.72029 2.69401 6.31452
3.52074 2.18086 8.01075
3.17864 2.06683 9.84951
3.12163 2.19512 11.33193
3.23566 2.46594 12.61479
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
# 0 - G18.69

s = Specimen('G18.69')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
5.14569 2.33766 0.66994
4.94614 2.33766 1.26861
4.68957 2.36616 2.65124
4.19068 2.95058 4.39023
3.66328 3.23566 6.41430
3.34969 3.15013 8.49538
3.34969 2.80804 10.39117
3.49223 2.39467 11.67403
'''

ml_pre = '''
5.92966 1.49667 1.18308
5.53055 2.16661 1.73899
5.81563 2.28064 2.32340
6.17198 2.56572 3.79156
6.34303 2.92207 4.84636
6.62811 3.09312 6.57109
6.87043 2.95058 8.29583
6.95595 2.69401 9.40764
6.92744 2.22362 10.74752
6.95595 1.99556 11.67403
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
# 0 - G18.MNS1

s = Specimen('G18.MNS1')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
3.87709 3.22140 0.39911
3.96261 3.44947 1.68197
3.99112 3.66328 2.90782
3.64902 3.80582 3.97687
3.24991 3.99112 5.08868
2.89356 4.03388 6.91319
2.63699 3.70604 8.40986
2.66550 3.20715 9.93504
2.86505 2.49445 11.43171
'''

ml_pre = '''
6.64236 3.80582 0.61292
6.35728 4.11941 2.75102
6.31452 4.01963 4.14791
6.61386 3.99112 5.31674
6.71363 3.76306 7.19827
6.58535 3.33544 8.85173
6.41430 2.76528 10.29139
6.15773 2.36616 11.36044
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


