# -*- coding: cp949 -*-
'''
Created on 2018. 10. 21.

@author: jongki
'''

from __future__ import division

import os

from class_specimen import Specimen, Canal
from constant import CONST

directory_name = os.getenv('TOOTH_DATA') + '/v3d_g19/'
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

s = Specimen('G19.1L')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
5.82989 3.37820 0.18530
5.80138 3.19290 0.59867
5.97243 3.27842 1.06905
6.15773 3.27842 1.76750
6.15773 3.19290 2.93632
6.15773 2.95058 3.80582
6.10071 2.55147 5.07442
6.25751 2.29489 6.28601
6.51408 2.12385 7.41208
6.81341 2.09534 8.50964
6.94170 2.19512 9.64996
6.94170 2.43743 10.69050
6.81341 2.73677 11.73104
'''

ml_pre = '''
5.35950 3.24991 0.39911
5.30249 3.32118 1.02629
4.94614 3.34969 1.25435
4.88912 3.30693 2.03832
4.83211 3.22140 2.60848
4.70382 3.22140 3.23566
4.46150 3.03610 3.96261
4.23344 2.70826 5.20271
3.96261 2.33766 6.71363
3.64902 2.25213 8.12478
3.53499 2.25213 9.46466
3.50648 2.40893 10.63348
3.64902 2.76528 11.74530
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
# 0 - G19.

s = Specimen('G19.2M')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
4.21918 3.12163 0.45613
4.33322 3.05036 0.84099
4.21918 3.12163 1.46816
3.96261 3.26417 2.05258
3.67753 3.40671 2.65124
3.37820 3.47798 3.23566
2.93632 3.43521 4.03388
2.66550 3.44947 4.80360
2.45169 3.32118 5.50204
2.30915 3.19290 6.49982
2.23788 3.07886 7.48335
2.20937 3.05036 8.48113
2.30915 3.00759 9.37913
2.53721 3.26417 10.20586
2.67975 3.52074 10.67625
'''

ml_pre = '''
5.13144 5.67309 0.84099
5.01741 5.40227 1.39689
4.77509 5.37376 1.73899
4.53277 5.40227 2.05258
4.34747 5.51630 2.30915
4.13366 5.57331 2.65124
3.93410 5.61608 2.97909
3.77731 5.68735 3.27842
3.60626 5.75862 3.62052
3.34969 5.91541 4.27620
3.13588 6.11497 5.01741
2.96483 6.20049 5.57331
2.86505 6.41430 6.12922
2.73677 6.71363 7.25529
2.75102 6.84192 7.92522
2.79378 6.88468 8.96577
2.99334 6.65662 9.97780
3.16439 6.32878 10.71901
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
# 0 - G19.5L

s = Specimen('G19.5L')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
6.37154 4.29045 0.52740
6.49982 3.91985 1.06905
6.61386 3.54925 1.83877
6.61386 3.29267 2.45169
6.59960 3.10737 3.27842
6.75640 2.80804 4.24769
6.99871 2.60848 5.35950
7.24103 2.40893 6.02944
7.51186 2.38042 7.08424
7.65440 2.40893 8.13903
7.64014 2.56572 9.36488
7.62589 2.96483 10.66199
7.46910 3.39245 11.71679
'''

ml_pre = '''
6.40005 4.26195 0.49889
6.12922 3.82007 1.68197
5.88690 3.60626 2.22362
5.70160 3.30693 3.12163
5.63033 3.06461 3.93410
5.24547 2.99334 4.60404
5.08868 2.86505 5.54481
4.87487 2.73677 6.51408
4.71807 2.72251 7.75418
4.60404 2.83655 8.85173
4.61830 2.99334 9.76399
4.67531 3.36394 10.89006
4.71807 3.70604 11.74530
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
# 0 - G19.7C

s = Specimen('G19.7C')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
4.77509 3.44947 0.28508
4.46150 3.56350 1.14032
4.07664 3.66328 1.93854
3.66328 3.74880 2.60848
3.12163 3.84858 3.50648
2.63699 3.82007 4.81785
2.42318 3.62052 6.02944
2.43743 3.39245 7.04148
2.60848 3.09312 7.88246
2.62274 2.90782 7.98224
2.62274 2.90782 8.26732
2.63699 2.90782 8.26732
'''

ml_pre = '''
6.21474 3.32118 0.69845
6.37154 3.19290 1.46816
6.18624 3.22140 2.18086
6.18624 3.20715 2.82229
6.30027 3.20715 3.32118
6.49982 3.19290 3.84858
6.81341 3.19290 4.50426
6.94170 3.24991 5.28823
6.91319 3.24991 6.34303
6.81341 3.09312 7.11275
6.61386 3.02185 7.65440
6.40005 2.82229 8.25307
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
# 0 - G19.8M

s = Specimen('G19.8M')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
5.94392 2.15235 0.45613
5.87265 2.12385 1.79600
5.91541 2.39467 3.05036
6.12922 2.65124 4.20493
6.54259 2.69401 5.27398
6.97021 2.80804 6.68513
7.12700 2.79378 7.96799
7.16976 2.62274 9.06554
7.22678 2.36616 10.10609
7.34081 2.03832 11.07536
7.44059 1.73899 12.00187
'''

ml_pre = '''
3.05036 1.75324 1.12607
2.92207 1.68197 1.66772
3.00759 1.83877 2.10959
3.20715 2.15235 2.89356
3.26417 2.30915 3.60626
3.20715 2.48020 4.47576
2.95058 2.52296 5.37376
2.83655 2.62274 6.21474
2.86505 2.69401 7.24103
2.79378 2.66550 8.35284
3.06461 2.48020 9.62145
3.34969 2.23788 10.64774
3.50648 1.95280 11.63126
3.56350 1.88153 12.00187
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
# 0 - G19.10L

s = Specimen('G19.10L')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
5.95817 1.41115 0.47038
6.00093 1.63921 0.88375
5.95817 1.76750 1.16883
5.61608 1.85302 1.52518
5.24547 2.22362 2.10959
5.04592 2.49445 2.77953
4.83211 2.73677 3.52074
4.70382 2.89356 4.20493
4.70382 3.06461 4.81785
4.50426 3.15013 5.40227
4.36172 3.17864 5.75862
4.33322 3.27842 6.54259
4.24769 3.26417 6.99871
4.39023 3.26417 7.45484
4.16217 3.16439 8.15329
4.00537 3.09312 8.75196
3.84858 2.93632 9.17958
3.84858 2.90782 9.42189
3.79156 2.76528 9.77824
3.76306 2.76528 10.00631
3.67753 2.70826 10.17736
3.64902 2.70826 10.43393
3.62052 2.63699 10.63348
3.72029 2.56572 10.77602
'''

ml_pre = '''
6.08646 1.46816 0.68419
6.27176 1.58219 1.02629
6.44281 1.72473 1.26861
6.41430 2.12385 1.91004
6.37154 2.59423 2.92207
6.31452 2.86505 3.86283
6.32878 3.06461 4.56128
6.40005 3.19290 5.21696
6.47132 3.23566 5.92966
6.54259 3.23566 6.54259
6.65662 3.16439 7.32656
6.68513 3.06461 8.02500
6.62811 3.03610 8.63792
6.71363 2.93632 8.99427
6.77065 2.85080 9.23659
6.71363 2.83655 9.32212
6.77065 2.65124 9.84951
6.77065 2.43743 10.34840
6.57109 2.25213 10.89006
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
# 0 - G19.11L

s = Specimen('G19.11L')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
7.18402 0.94076 0.22806
7.16976 1.39689 0.79822
6.98446 1.81026 1.56794
6.69938 2.30915 2.57997
6.67087 2.72251 3.39245
6.92744 3.20715 4.44725
7.18402 3.63477 5.57331
7.32656 3.86283 6.78490
7.42633 3.99112 8.05351
7.48335 3.99112 9.07980
7.39783 3.96261 10.20586
7.32656 3.77731 10.97558
7.21252 3.66328 11.55999
'''

ml_pre = '''
4.29045 0.76972 0.00000
4.30471 1.32562 1.02629
4.57553 1.71048 1.85302
4.83211 2.09534 2.50870
4.94614 2.48020 3.40671
4.88912 2.90782 4.33322
4.58979 3.17864 5.13144
4.16217 3.44947 6.05795
3.86283 3.63477 7.15551
3.64902 3.72029 8.31008
3.50648 3.69179 9.45040
3.56350 3.63477 10.46244
3.64902 3.44947 11.51723
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
# 0 - G19.14C

s = Specimen('G19.14C')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
5.37376 3.96261 1.61070
5.08868 3.60626 2.22362
4.86061 3.36394 3.00759
5.28823 3.39245 4.30471
5.67309 3.70604 6.02944
6.24325 3.83433 7.91097
6.40005 3.52074 9.40764
6.14347 3.03610 10.44818
6.08646 2.56572 11.14663
6.08646 2.33766 11.73104
'''

ml_pre = '''
4.39023 3.83433 0.84099
4.54703 3.86283 1.46816
4.46150 3.67753 2.06683
4.66106 3.52074 2.29489
4.70382 3.36394 3.00759
4.33322 3.36394 4.23344
3.79156 3.52074 5.80138
3.43521 3.52074 7.32656
3.20715 3.20715 8.62367
3.46372 2.72251 9.84951
3.72029 2.05258 10.87580
3.69179 1.73899 11.73104
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
# 0 - G19.15L

s = Specimen('G19.15L')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
4.09090 1.88153 0.71270
4.24769 1.59645 1.49667
4.43299 1.36838 2.39467
4.73233 1.41115 3.23566
5.00315 1.78175 4.14791
4.90338 2.49445 5.35950
4.60404 2.99334 6.47132
4.30471 3.23566 7.64014
3.90560 3.33544 8.75196
3.59201 3.30693 9.84951
3.47798 3.20715 10.69050
3.57775 2.93632 11.67403
'''

ml_pre = '''
4.56128 1.38264 0.88375
4.57553 1.43965 1.45391
4.88912 1.25435 1.93854
5.01741 1.19734 2.48020
5.08868 1.28286 3.03610
5.31674 1.51092 3.77731
5.70160 1.88153 4.60404
5.95817 2.32340 5.50204
6.20049 2.55147 6.24325
6.41430 2.75102 7.21252
6.59960 2.79378 8.02500
6.77065 2.90782 9.03704
6.72789 2.90782 9.90653
6.62811 2.59423 10.77602
6.35728 2.30915 11.65977
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
# 0 - G19.16C

s = Specimen('G19.16C')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
5.15995 6.38579 0.35635
5.53055 6.08646 1.26861
5.74436 5.65884 2.33766
5.97243 5.25973 3.39245
6.42855 4.96039 4.26195
6.62811 4.64680 5.14569
6.71363 4.37598 6.31452
6.58535 4.29045 7.25529
6.24325 4.31896 8.18180
6.28601 3.96261 8.79472
'''

ml_pre = '''
5.15995 6.38579 0.35635
5.34525 6.17198 0.95502
5.18846 5.71585 1.71048
5.27398 5.44503 2.52296
5.45928 5.08868 3.29267
5.30249 4.68957 4.06239
5.10293 4.26195 4.97465
4.73233 3.89134 6.11497
4.64680 3.83433 7.16976
4.73233 3.89134 7.93948
4.91763 4.04814 8.75196
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
# 0 - G19.17M

s = Specimen('G19.17M')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
5.50204 1.66772 0.31359
5.55906 1.93854 0.66994
5.67309 2.16661 1.12607
5.68735 2.32340 1.63921
5.71585 2.57997 2.66550
5.74436 2.76528 3.43521
5.84414 2.99334 4.13366
6.01519 3.29267 5.15995
6.18624 3.42096 5.94392
6.34303 3.37820 7.14125
6.45706 3.26417 8.16754
6.54259 2.87931 9.42189
6.61386 2.63699 10.20586
6.47132 2.36616 10.90431
'''

ml_pre = '''
3.05036 1.68197 1.19734
3.06461 2.09534 1.81026
2.86505 2.26639 2.89356
2.69401 2.45169 4.06239
2.36616 2.65124 5.33100
2.23788 2.77953 6.35728
2.25213 2.69401 7.73992
2.42318 2.43743 9.16532
2.69401 2.08108 10.39117
2.92207 2.08108 11.03260
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
# 0 - G19.20L

s = Specimen('G19.20L')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
5.80138 1.04054 0.57016
6.21474 1.28286 1.18308
6.45706 1.55369 1.95280
6.51408 1.76750 2.66550
6.51408 2.00981 3.50648
6.68513 2.30915 4.44725
6.85617 2.55147 5.57331
6.88468 2.67975 6.68513
6.94170 2.57997 7.91097
7.08424 2.49445 9.09405
7.29805 2.28064 10.16310
7.26954 2.09534 10.94707
7.18402 1.85302 11.58850
'''

ml_pre = '''
5.73011 1.01203 0.31359
5.24547 1.46816 1.08330
4.77509 1.62496 1.82451
4.51852 1.81026 3.09312
4.07664 2.00981 4.17642
3.62052 2.19512 5.34525
3.50648 2.28064 6.77065
3.50648 2.22362 8.01075
3.44947 2.06683 9.27935
3.34969 1.76750 10.53371
3.53499 1.49667 11.57425
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
# 0 - G19.29M

s = Specimen('G19.29M')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
4.27620 1.52518 0.31359
4.44725 1.68197 0.79822
4.67531 1.95280 1.55369
4.90338 2.16661 2.43743
5.08868 2.33766 3.27842
5.27398 2.49445 4.34747
5.43077 2.46594 5.27398
5.43077 2.40893 6.37154
5.81563 2.38042 7.36932
5.88690 2.28064 8.28157
5.87265 2.08108 9.15107
5.81563 1.89578 9.92078
'''

ml_pre = '''
3.60626 1.25435 1.36838
3.76306 1.63921 1.71048
3.82007 1.93854 2.56572
3.63477 2.13810 3.66328
3.59201 2.25213 4.83211
3.63477 2.26639 5.98668
3.66328 2.22362 6.89894
3.66328 2.06683 8.09627
3.52074 1.89578 9.12256
3.46372 1.43965 10.13459
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
# 0 - G19.34L

s = Specimen('G19.34L')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
6.30027 3.27842 0.86949
6.61386 3.79156 1.65346
6.82767 3.90560 2.55147
7.04148 3.83433 3.60626
7.31230 3.74880 4.57553
7.58313 3.54925 5.40227
7.75418 3.50648 5.98668
7.96799 3.30693 6.87043
8.11053 3.17864 7.65440
8.26732 3.00759 8.53815
8.15329 2.67975 9.59294
7.99649 2.52296 10.46244
7.64014 2.25213 11.27491
'''

ml_pre = '''
5.81563 3.46372 1.26861
5.70160 3.87709 2.00981
5.64458 4.01963 2.73677
5.57331 4.04814 3.40671
5.37376 4.03388 4.27620
5.06017 4.04814 5.24547
4.67531 4.03388 6.27176
4.29045 3.79156 7.34081
4.07664 3.53499 8.39561
4.01963 3.30693 9.46466
4.16217 3.00759 10.30564
4.34747 2.55147 11.26066
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
# 0 - G19.35L

s = Specimen('G19.35L')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
6.32878 3.74880 0.32784
6.10071 3.54925 0.76972
6.15773 3.46372 1.39689
6.10071 3.22140 2.18086
6.15773 2.85080 3.09312
6.45706 2.52296 4.09090
6.69938 2.22362 5.06017
6.75640 2.03832 6.21474
7.02722 1.95280 7.29805
7.18402 2.03832 8.68069
7.32656 2.03832 9.87802
7.39783 2.25213 10.90431
7.29805 2.46594 11.91634
7.18402 2.57997 12.37247
'''

ml_pre = '''
4.50426 3.46372 1.66772
4.50426 3.22140 2.28064
4.40449 2.92207 3.24991
4.29045 2.67975 4.11941
4.07664 2.33766 5.07442
3.96261 2.12385 6.22900
3.96261 1.95280 7.36932
3.80582 1.95280 8.39561
3.72029 1.98131 9.47891
3.83433 2.06683 10.66199
4.04814 2.28064 11.64552
4.26195 2.46594 12.37247
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
# 0 - G19.42C

s = Specimen('G19.42C')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
6.79916 2.19512 0.58441
6.59960 2.15235 1.06905
6.37154 2.08108 1.53943
6.05795 1.96705 2.08108
5.67309 1.91004 2.99334
5.31674 1.96705 3.91985
5.14569 2.08108 4.84636
4.78934 2.43743 6.14347
4.86061 2.99334 7.44059
4.87487 3.44947 8.48113
5.03166 3.80582 9.33637
4.97465 3.77731 10.30564
'''

ml_pre = '''
7.09849 2.29489 0.27083
6.92744 2.20937 0.89800
6.87043 2.13810 1.59645
7.05573 2.13810 2.15235
7.54037 2.22362 2.99334
7.76843 2.26639 3.93410
7.92522 2.35191 4.97465
7.79694 2.65124 6.27176
7.56887 3.12163 7.45484
7.14125 3.60626 8.50964
6.88468 3.89134 9.32212
7.09849 4.00537 9.93504
7.21252 4.09090 10.44818
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
# 0 - G19.43L

s = Specimen('G19.43L')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
6.45706 3.80582 0.61292
6.11497 3.56350 1.04054
6.02944 3.46372 1.45391
5.90116 3.24991 2.09534
5.78712 3.07886 2.85080
5.75862 2.90782 3.70604
5.73011 2.75102 4.23344
5.84414 2.60848 5.18846
5.87265 2.48020 6.07220
5.95817 2.38042 6.99871
6.28601 2.32340 7.86821
6.69938 2.29489 8.76621
6.84192 2.32340 9.69272
6.98446 2.49445 10.57647
7.01297 2.69401 11.43171
'''

ml_pre = '''
6.42855 3.77731 0.65568
6.07220 3.56350 1.19734
6.00093 3.43521 1.59645
5.84414 3.22140 2.29489
5.61608 3.07886 3.05036
5.50204 2.86505 3.93410
5.44503 2.69401 4.84636
5.33100 2.56572 5.90116
5.08868 2.49445 7.11275
4.78934 2.39467 8.13903
4.56128 2.57997 9.20808
4.39023 2.80804 10.30564
4.39023 3.13588 11.18939
4.39023 3.22140 11.54574
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
# 0 - G19.44M

s = Specimen('G19.44M')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
4.90338 3.24991 0.62718
5.11719 2.75102 1.62496
5.08868 2.63699 2.60848
5.00315 2.52296 3.70604
4.76084 2.45169 4.77509
4.43299 2.56572 5.91541
4.30471 2.77953 6.95595
4.41874 3.06461 7.96799
4.58979 3.39245 8.75196
5.03166 3.69179 9.37913
'''

ml_pre = '''
6.49982 3.50648 0.52740
6.74214 3.06461 1.21159
6.88468 2.87931 2.08108
7.08424 2.80804 3.03610
7.25529 2.75102 4.09090
7.45484 2.77953 5.08868
7.56887 2.92207 6.25751
7.42633 3.16439 7.46910
7.18402 3.54925 8.48113
6.67087 3.89134 9.43615
6.55684 4.04814 10.10609
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
# 0 - G19.50M

s = Specimen('G19.50M')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
7.01297 2.32340 1.36838
6.45706 2.36616 1.96705
6.40005 2.25213 2.95058
6.37154 2.16661 3.93410
6.48557 2.13810 5.03166
6.64236 2.10959 6.14347
6.84192 2.19512 7.21252
7.01297 2.40893 8.40986
6.98446 2.72251 9.74974
7.01297 2.96483 10.59072
7.12700 3.13588 11.73104
'''

ml_pre = '''
3.63477 3.36394 2.15235
3.40671 2.87931 3.15013
3.27842 2.66550 4.03388
3.27842 2.57997 4.88912
3.30693 2.52296 6.20049
3.53499 2.66550 7.61164
3.77731 2.85080 8.65218
4.03388 3.13588 9.63570
4.30471 3.39245 10.49094
3.91985 3.83433 11.71679
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
# 0 - G19.51C

s = Specimen('G19.51C')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
7.59738 1.91004 0.44187
7.46910 1.71048 1.56794
7.39783 1.82451 2.77953
7.11275 2.23788 3.87709
6.92744 2.55147 5.31674
6.78490 2.69401 6.62811
6.72789 2.82229 7.98224
6.65662 2.69401 8.99427
6.47132 2.43743 9.63570
6.11497 2.38042 10.29139
6.72789 2.29489 11.21790
6.64236 2.38042 12.10165
6.69938 2.60848 12.55777
'''

ml_pre = '''
7.29805 1.85302 0.48464
7.05573 1.76750 1.26861
6.31452 1.83877 2.12385
5.61608 2.16661 2.85080
5.03166 2.69401 4.23344
4.74658 2.95058 5.45928
4.44725 3.05036 6.45706
4.36172 3.05036 7.31230
4.27620 2.96483 8.26732
4.53277 2.76528 9.13681
4.86061 2.63699 9.73548
4.91763 2.43743 10.44818
4.41874 2.38042 11.28917
3.89134 2.60848 12.11590
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
# 0 - G19.55M

s = Specimen('G19.55M')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
4.58979 1.35413 0.42762
4.80360 1.58219 1.41115
5.08868 1.99556 2.50870
5.35950 2.35191 3.63477
5.64458 2.63699 4.74658
5.92966 2.80804 5.82989
6.17198 2.77953 6.75640
6.37154 2.75102 7.85395
6.42855 2.52296 9.07980
6.55684 2.22362 10.09183
6.78490 2.02407 11.11812
'''

ml_pre = '''
2.92207 2.10959 1.58219
3.02185 2.19512 2.56572
3.05036 2.40893 3.52074
2.95058 2.55147 4.68957
2.92207 2.66550 5.74436
2.95058 2.63699 6.87043
3.05036 2.55147 7.92522
3.27842 2.43743 8.90875
3.50648 2.22362 9.92078
3.80582 1.82451 11.01834
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
# 0 - G19.57M

s = Specimen('G19.57M')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
3.72029 3.27842 0.32784
3.82007 2.92207 0.96927
3.96261 2.66550 1.73899
3.90560 2.49445 2.42318
3.62052 2.33766 3.05036
3.46372 2.18086 3.74880
3.36394 2.02407 4.54703
3.26417 1.92429 5.51630
3.26417 2.05258 6.88468
3.19290 2.43743 8.23881
3.33544 2.67975 9.23659
3.47798 2.96483 9.99205
3.77731 3.16439 10.66199
'''

ml_pre = '''
5.63033 3.10737 0.51314
5.71585 3.02185 1.09756
5.68735 2.63699 1.78175
5.68735 2.46594 2.49445
5.80138 2.40893 3.10737
6.11497 2.35191 3.89134
6.34303 2.28064 5.04592
6.42855 2.33766 5.98668
6.42855 2.43743 6.98446
6.40005 2.70826 8.29583
6.40005 3.15013 9.42189
6.27176 3.47798 10.19161
6.14347 3.57775 10.63348
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
# 0 - G19.58C

s = Specimen('G19.58C')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
5.64458 3.34969 0.57016
5.48779 3.40671 1.32562
5.67309 3.32118 2.32340
6.00093 3.16439 3.43521
6.45706 3.05036 4.94614
6.87043 3.10737 6.20049
7.15551 3.32118 7.69716
7.06998 3.74880 8.80897
6.85617 4.34747 10.14885
6.88468 4.44725 11.46022
'''

ml_pre = '''
4.57553 3.53499 0.52740
4.57553 3.47798 1.39689
4.56128 3.30693 2.18086
4.54703 3.19290 2.97909
4.67531 2.97909 4.06239
4.49001 2.89356 5.20271
4.49001 2.95058 6.59960
4.68957 3.24991 8.06776
5.15995 3.82007 9.60720
5.25973 4.27620 10.43393
4.76084 4.26195 11.57425
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
# 0 - G19.66C

s = Specimen('G19.66C')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
6.88468 0.98353 0.51314
7.15551 1.46816 1.78175
7.52611 1.92429 3.10737
7.82545 2.30915 4.47576
7.88246 2.36616 6.05795
7.85395 2.28064 7.61164
7.76843 1.92429 9.15107
7.64014 1.61070 10.61923
7.39783 1.46816 11.78806
'''

ml_pre = '''
4.33322 1.62496 0.81248
4.53277 2.06683 2.02407
4.30471 2.40893 3.24991
3.94836 2.79378 4.84636
3.89134 2.79378 6.40005
4.03388 2.49445 8.09627
4.11941 2.38042 9.40764
4.33322 1.98131 10.83304
3.79156 1.46816 12.21568
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
# 0 - G19.71C

s = Specimen('G19.71C')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
2.45169 2.63699 1.25435
2.57997 2.85080 2.35191
2.55147 2.97909 3.32118
2.30915 3.10737 4.30471
2.15235 3.16439 5.45928
2.23788 2.97909 6.84192
2.39467 2.73677 7.99649
2.79378 2.46594 9.13681
3.19290 2.09534 10.19161
3.56350 2.12385 11.04685
3.43521 2.02407 11.51723
'''

ml_pre = '''
6.55684 3.37820 0.91226
6.68513 3.56350 1.93854
6.89894 3.74880 2.83655
7.22678 3.83433 3.77731
7.62589 3.86283 5.21696
7.65440 3.53499 6.68513
7.59738 3.19290 8.18180
7.59738 2.70826 9.49316
7.51186 2.42318 10.43393
7.51186 2.23788 11.17514
7.46910 2.52296 11.55999
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
# 0 - G19.73L

s = Specimen('G19.73L')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
6.20049 4.07664 1.22584
6.25751 3.54925 2.26639
6.37154 3.27842 3.32118
6.58535 3.27842 4.56128
6.67087 3.39245 6.05795
7.06998 3.49223 7.36932
7.26954 3.54925 8.55240
7.45484 3.36394 9.76399
7.45484 3.22140 10.96133
7.34081 2.87931 12.04463
7.25529 2.55147 12.61479
'''

ml_pre = '''
5.53055 3.54925 1.32562
5.38801 3.37820 2.20937
4.94614 3.02185 3.32118
4.47576 2.90782 4.49001
4.09090 2.93632 6.18624
3.86283 2.96483 7.54037
3.77731 3.05036 9.16532
3.83433 2.90782 10.37691
3.83433 2.87931 11.34618
3.89134 2.57997 12.14441
3.97687 2.32340 12.61479
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
# 0 - G19.73L2

s = Specimen('G19.73L2')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
6.97021 5.14569 0.65568
7.38357 4.61830 1.61070
7.61164 3.99112 2.83655
7.55462 3.47798 3.93410
7.78268 3.15013 4.84636
7.96799 2.93632 5.71585
8.21030 2.79378 6.81341
8.38135 2.66550 7.92522
8.38135 2.49445 8.99427
8.38135 2.45169 10.26288
8.26732 2.42318 11.44596
8.02500 2.57997 12.27269
'''

ml_pre = '''
3.87709 4.43299 1.99556
3.89134 3.69179 2.99334
4.04814 3.26417 3.82007
4.06239 2.99334 4.60404
3.97687 2.85080 5.47354
3.80582 2.76528 6.32878
3.69179 2.72251 7.22678
3.50648 2.60848 8.08202
3.37820 2.57997 9.03704
3.26417 2.55147 10.09183
3.20715 2.57997 11.03260
3.29267 2.72251 12.28695
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
# 0 - G19.76C

s = Specimen('G19.76C')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
4.97465 4.61830 0.96927
5.61608 4.27620 1.73899
5.88690 3.64902 3.33544
5.82989 3.37820 4.61830
5.63033 3.07886 5.74436
5.20271 3.00759 7.32656
5.01741 3.16439 8.60942
5.00315 3.43521 9.67847
5.21696 3.67753 10.64774
4.97465 3.91985 11.55999
4.86061 3.91985 12.18717
'''

ml_pre = '''
5.94392 4.71807 0.96927
6.18624 4.43299 1.75324
6.45706 4.07664 2.29489
6.52833 3.77731 3.00759
6.79916 3.40671 4.29045
6.67087 3.10737 5.43077
6.65662 2.99334 6.87043
6.69938 3.02185 8.33859
6.61386 3.23566 9.35062
6.37154 3.46372 10.36266
6.41430 3.66328 11.55999
7.04148 4.04814 12.22993
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
# 0 - G19.78C

s = Specimen('G19.78C')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
4.76084 2.00981 0.49889
4.63255 2.48020 0.85524
4.90338 2.49445 1.66772
4.81785 2.52296 2.48020
4.60404 2.57997 3.44947
4.16217 2.70826 4.87487
3.91985 2.92207 6.00093
3.76306 3.10737 6.99871
3.49223 3.22140 7.96799
3.40671 3.26417 9.55018
3.52074 3.16439 10.83304
3.82007 2.89356 11.91634
'''

ml_pre = '''
5.45928 2.70826 0.94076
5.20271 2.45169 1.98131
5.30249 2.45169 2.80804
5.67309 2.50870 3.87709
6.27176 2.76528 5.03166
6.67087 3.05036 5.92966
7.45484 3.43521 7.08424
7.83970 3.69179 8.26732
7.98224 3.62052 9.56443
7.79694 3.34969 11.08961
7.52611 3.10737 11.97336
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
# 0 - G19.87C

s = Specimen('G19.87C')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
7.72567 1.45391 3.56350
7.38357 1.96705 3.90560
7.34081 2.19512 4.33322
7.32656 2.35191 4.87487
7.38357 2.43743 5.11719
7.31230 2.42318 5.77287
7.75418 2.62274 6.10071
8.05351 2.69401 6.51408
7.96799 2.67975 7.04148
7.86821 2.65124 7.81119
7.81119 2.72251 8.39561
7.72567 2.90782 9.10831
7.69716 3.06461 9.59294
7.41208 3.26417 10.16310
7.38357 3.52074 10.84729
7.69716 3.60626 11.40320
'''

ml_pre = '''
6.68513 1.18308 3.47798
6.28601 1.66772 3.70604
6.00093 1.98131 4.19068
5.45928 2.13810 4.86061
4.87487 2.28064 5.43077
4.34747 2.28064 6.18624
4.07664 2.38042 7.24103
4.01963 2.49445 8.32434
4.10515 2.99334 9.62145
4.20493 3.36394 10.61923
4.23344 3.60626 11.48872
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
# 0 - G19.89C

s = Specimen('G19.89C')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
6.25751 2.26639 0.61292
6.55684 2.57997 1.53943
6.84192 2.55147 2.59423
7.06998 2.52296 3.52074
7.09849 2.60848 4.61830
7.12700 2.93632 5.73011
6.78490 3.24991 6.82767
6.69938 3.66328 7.83970
6.92744 3.66328 8.53815
'''

ml_pre = '''
4.39023 2.49445 0.48464
4.33322 2.73677 1.46816
4.44725 2.69401 2.56572
4.50426 2.57997 3.56350
4.44725 2.69401 4.60404
4.44725 3.05036 5.63033
4.61830 3.32118 6.58535
4.60404 3.42096 7.25529
4.30471 3.66328 7.82545
4.14791 3.19290 8.62367
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
# 0 - G19.90C

s = Specimen('G19.90C')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
6.34303 1.24010 0.65568
6.68513 1.42540 1.06905
7.04148 1.45391 2.00981
6.98446 1.53943 2.36616
6.89894 1.71048 2.99334
6.88468 1.82451 3.67753
6.87043 1.98131 4.37598
6.97021 2.13810 4.77509
7.09849 2.18086 5.21696
7.24103 2.38042 5.73011
7.29805 2.39467 6.18624
7.35506 2.39467 6.94170
7.35506 2.36616 7.68291
7.41208 2.22362 8.72345
7.44059 2.12385 9.59294
7.46910 1.98131 10.29139
7.35506 1.79600 10.73326
7.26954 1.49667 11.38895
'''

ml_pre = '''
4.47576 1.26861 0.81248
4.56128 1.45391 0.98353
4.63255 1.59645 1.66772
4.67531 1.65346 2.05258
4.77509 1.73899 2.38042
4.87487 1.81026 2.69401
4.97465 1.86727 3.07886
4.96039 1.95280 3.44947
4.90338 2.03832 3.97687
4.87487 2.12385 4.36172
4.76084 2.19512 4.80360
4.58979 2.32340 5.25973
4.39023 2.40893 5.88690
4.30471 2.40893 6.54259
4.29045 2.36616 7.19827
4.34747 2.33766 7.86821
4.33322 2.06683 8.72345
4.50426 1.86727 9.64996
4.71807 1.53943 10.33415
4.71807 1.26861 11.10387
4.78934 1.14032 11.40320
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
# 0 - G19.94L

s = Specimen('G19.94L')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
5.70160 3.10737 0.44187
5.33100 2.87931 1.65346
5.06017 2.69401 2.79378
4.86061 2.43743 3.96261
4.77509 2.25213 5.03166
4.44725 2.19512 6.30027
4.27620 2.10959 7.64014
4.21918 2.29489 8.85173
4.39023 2.63699 10.07758
4.47576 3.07886 10.84729
4.53277 3.27842 11.40320
'''

ml_pre = '''
5.61608 3.13588 0.31359
6.25751 3.05036 1.36838
6.67087 2.99334 2.03832
7.01297 2.89356 2.99334
7.29805 2.66550 4.10515
7.46910 2.55147 5.17420
7.61164 2.50870 6.51408
7.65440 2.53721 7.35506
7.71141 2.57997 8.29583
7.68291 2.69401 9.27935
7.42633 2.90782 10.13459
7.01297 3.22140 11.06110
6.84192 3.39245 11.38895
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
# 0 - G19.96C

s = Specimen('G19.96C')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
6.45706 4.98890 0.55591
6.31452 3.73455 1.79600
6.32878 3.22140 2.70826
6.64236 2.85080 3.44947
6.98446 2.40893 4.40449
7.05573 2.10959 5.43077
6.98446 2.12385 6.55684
6.87043 2.26639 7.68291
6.81341 2.57997 8.70919
6.75640 3.02185 9.56443
6.64236 3.09312 10.14885
'''

ml_pre = '''
4.47576 4.58979 0.75546
4.33322 3.74880 1.49667
4.19068 3.37820 2.40893
4.03388 3.09312 3.29267
3.89134 2.82229 4.23344
3.83433 2.55147 5.20271
3.93410 2.52296 6.05795
4.11941 2.55147 6.89894
4.27620 2.57997 7.69716
4.33322 2.79378 8.40986
4.39023 2.99334 9.26510
4.21918 3.40671 9.99205
4.03388 3.12163 10.53371
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
# 0 - G19.CX5

s = Specimen('G19.CX5')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
v3d_path=s.get_default_path(directory_name, canal_pre_suffix)

mb_pre = '''
6.91319 4.07664 0.17105
7.06998 3.97687 0.79822
6.97021 3.89134 1.29711
6.91319 3.86283 1.96705
6.97021 3.89134 2.62274
7.08424 3.84858 3.43521
7.34081 3.86283 4.39023
7.61164 3.67753 5.63033
7.73992 3.43521 6.79916
7.69716 2.89356 8.16754
7.25529 2.28064 9.35062
7.45484 1.95280 10.36266
7.39783 1.88153 10.84729
'''

ml_pre = '''
3.89134 3.49223 1.32562
3.76306 3.72029 2.13810
3.70604 3.70604 2.79378
3.49223 3.54925 3.59201
3.19290 3.40671 4.44725
2.92207 3.22140 5.53055
2.92207 2.79378 6.87043
3.22140 2.36616 8.03926
3.70604 1.88153 9.09405
4.19068 1.36838 10.04907
3.79156 1.28286 10.86155
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

