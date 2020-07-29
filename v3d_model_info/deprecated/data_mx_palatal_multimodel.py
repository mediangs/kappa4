# -*- coding: cp949 -*-

'''
Created on 2018. 12. 9.

@author: jongki

data from jongki(Mx6)
안동 장갑수 원장님의 치아
'''

from __future__ import division


from constant import CONST
from class_specimen import Specimen, Canal
import os

directory_name = os.getenv('TOOTH_DATA') + '/v3d_mx/'
roots = []
bounding_box_range = [(-10, 20), (-10, 20), (-2, 28)]
canal_suffix = '-canal-zoff.v3d'
body_suffix = '-solid-body-zoff.v3d'

# ===============================================================================
#
# LEFT                              Cornal
#      .....                          ^
#     . DB  .                         |
#      .....         ...              |
#                  .     .            |
#                  .  P  .            |
#      ....          ...              |
#    .  MB  .                         |
#      ....                         Apical
#
# ===============================================================================

# ===============================================================================
# Root canal configuration / CANAL_TYPE
#
#      *      *     *      *    *        *
#      *      *     *      *    *        *
#      *      *     *      *    *       * *
#      *       *   *       *    *      *   *
#      *         *         *    *     *     *
#      *         *         *    *     *     *
#   Type 1     Type 2      Type 3      Type 4
#
# ===============================================================================

# =====================================================
s = Specimen('MX01')
s.tooth_position = CONST.UL
s.note = '13-4-14-check all'
s.canal_type = 0
ps1 = '''
13.12416 4.53096 18.61209
13.14369 4.70673 18.04572
13.00698 4.72626 17.26452
12.67497 4.62861 15.85836
12.30390 4.78485 13.94442
11.79612 4.98015 12.26484
10.87821 5.09733 10.35090
9.68688 5.17545 8.59320
8.76897 5.03874 7.30422
'''
ps2 = '''
3.59352 5.21451 10.11654
10.66338 5.21451 10.11654
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=0.0,
                      furcation_pos_lingual=0.0,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX02')
s.tooth_position = CONST.UR
s.note = '13-4-14-check all'
s.canal_type = 0

ps1 = '''
9.45252 7.98777 17.34264
9.41346 7.87059 16.95204
9.25722 7.71435 16.20990
9.08145 7.57764 15.23340
8.80803 7.47999 13.94442
8.53461 7.46046 13.08510
7.98777 7.24563 11.87424
7.47999 7.01127 10.46808
7.14798 6.75738 9.17910
'''
ps2 = '''
3.63258 7.12845 11.79612
7.90965 7.34328 11.79612
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=8.0,
                      furcation_pos_lingual=7.1,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX03')
s.tooth_position = CONST.UL
s.note = '13-4-21-check all'
s.canal_type = 0
ps1 = '''
10.87821 3.14433 18.53397
10.78056 3.37869 17.77230
10.60479 3.67164 16.75674
10.15560 4.04271 15.07716
9.70641 4.33566 13.39758
9.14004 4.57002 11.75706
8.53461 4.90203 10.11654
7.85106 5.21451 8.78850
'''
ps2 = '''
3.32010 4.41378 10.60479
8.49555 4.45284 10.60479
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
canal_pre = Canal(name='pre',
                  furcation_pos_buccal=6.8,
                  furcation_pos_lingual=7.7,
                  pts_buccal=ps1,
                  pts_bucco_lingual_vector=ps2,
                  path=s.get_default_path(directory_name, canal_suffix))
s.canals.append(canal_pre)
roots.append(s)

# =====================================================
s = Specimen('MX04')
s.tooth_position = CONST.UR
s.note = '13-4-21-check all'
s.canal_type = 0
ps1 = '''
13.90536 3.76929 14.99904
13.71006 3.84741 14.70609
13.37805 4.00365 13.86630
12.88980 4.04271 12.10860
12.32343 4.15989 10.19466
11.46411 4.33566 8.08542
10.40949 4.64814 6.17148
9.31581 5.09733 4.60908
'''
ps2 = '''
5.99571 6.77691 6.05430
10.09701 5.07780 6.05430 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
canal_pre = Canal(name='pre',
                  furcation_pos_buccal=8.2,
                  furcation_pos_lingual=8.3,
                  pts_buccal=ps1,
                  pts_bucco_lingual_vector=ps2,
                  path=s.get_default_path(directory_name, canal_suffix))
s.canals.append(canal_pre)
roots.append(s)

# =====================================================
s = Specimen('MX05')
s.tooth_position = CONST.UR
s.note = '13-4-21-check all'
s.canal_type = 0
ps1 = '''
13.33899 4.04271 17.98713
13.08510 3.86694 17.34264
12.77262 3.82788 16.40520
12.49920 3.92553 14.92092
12.06954 4.12083 12.96792
11.42505 4.41378 11.17116
10.60479 4.99968 9.45252
9.99936 5.17545 8.12448
9.45252 5.52699 7.03080
'''
ps2 = '''
6.15195 8.61273 8.90568
10.48761 5.68323 8.90568
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
canal_pre = Canal(name='pre',
                  furcation_pos_buccal=10.0,
                  furcation_pos_lingual=9.1,
                  pts_buccal=ps1,
                  pts_bucco_lingual_vector=ps2,
                  path=s.get_default_path(directory_name, canal_suffix))
s.canals.append(canal_pre)
roots.append(s)



# =====================================================
s = Specimen('MX07')
s.tooth_position = CONST.UR
s.note = '13-4-21-check all'
s.canal_type = 0
ps1 = '''
16.03413  1.79676  18.61209
15.56541  1.64052  17.77230
14.82327  1.77723  16.60050
13.78818  2.26548  14.80374
12.92886  2.90997  12.88980
11.99142  3.59352  10.97586
11.21022  4.10130  9.56970
10.17513  5.03874  8.04636
'''
ps2 = '''
6.89409  7.44093  10.05795
11.52270  3.94506  10.05795
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
canal_pre = Canal(name='pre',
                  furcation_pos_buccal=8.6,
                  furcation_pos_lingual=7.3,
                  pts_buccal=ps1,
                  pts_bucco_lingual_vector=ps2,
                  path=s.get_default_path(directory_name, canal_suffix))
s.canals.append(canal_pre)
roots.append(s)

# =====================================================
s = Specimen('MX08')
s.tooth_position = CONST.UL
s.note = '13-4-21-check all'
s.canal_type = 0
ps1 = '''
11.36646 2.16783 18.49491
11.52270 2.46078 17.77230
11.48364 2.69514 16.99110
11.15163 3.06621 15.66306
10.46808 3.51540 13.78818
9.90171 3.84741 12.46014
8.88615 4.25754 10.15560
8.28072 4.35519 8.86662
'''
ps2 = '''
3.65211 4.21848 12.20625
9.19863 3.73023 12.20625
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
canal_pre = Canal(name='pre',
                  furcation_pos_buccal=7.8,
                  furcation_pos_lingual=5.8,
                  pts_buccal=ps1,
                  pts_bucco_lingual_vector=ps2,
                  path=s.get_default_path(directory_name, canal_suffix))
s.canals.append(canal_pre)
roots.append(s)

# =====================================================
s = Specimen('MX09')
s.tooth_position = CONST.UL
s.note = '13-4-21-check all'
s.canal_type = 0
ps1 = '''
15.99507 4.14036 18.78786
15.54588 4.53096 17.73324
14.99904 4.78485 16.36614
14.02254 4.90203 14.64750
12.83121 5.13639 12.61638
12.05001 5.27310 11.44458
10.83915 5.35122 9.76500
9.78453 5.40981 8.39790
'''
ps2 = '''
6.24960 5.31216 9.64782
10.35090 5.39028 9.64782
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=7.4,
                      furcation_pos_lingual=6.8,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX10')
s.tooth_position = CONST.UR
s.note = '13-4-21-check all'
s.canal_type = 0
ps1 = '''
12.51873 4.43331 18.26055
12.40155 4.57002 17.69418
12.14766 4.57002 17.10828
11.79612 4.68720 15.97554
11.40552 4.90203 14.60844
10.83915 5.09733 13.04604
9.97983 5.23404 11.17116
9.00333 5.33169 9.53064
'''
ps2 = '''
5.48793 6.23007 10.72197
10.01889 5.33169 10.72197
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=6.8,
                      furcation_pos_lingual=4.9,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX11')
s.tooth_position = CONST.UL
s.note = '13-4-28-check all'
s.canal_type = 0
ps1 = '''
11.22975 4.39425 16.52238
11.05398 4.57002 15.03810
10.60479 4.78485 13.16322
9.82359 4.76532 11.21022
8.84709 4.80438 9.49158
'''
ps2 = '''
4.17942 4.23801 10.83915
8.88615 4.55049 10.83915
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=8.2,
                      furcation_pos_lingual=7.7,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX12')
s.tooth_position = CONST.UR
s.note = '13-4-28-check all'
s.canal_type = 0
ps1 = '''
13.41711 2.28501 17.77230
13.26087 1.99206 17.18640
13.08510 1.95300 16.60050
12.96792 2.10924 15.93648
12.59685 2.22642 14.76468
12.03048 2.48031 13.31946
11.42505 2.79279 11.99142
10.42902 3.22245 10.35090
9.43299 3.86694 8.78850
8.72991 4.23801 7.77294
'''
ps2 = '''
6.34725 5.52699 9.17910
9.78453 3.86694 9.17910
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=9.4,
                      furcation_pos_lingual=9.2,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX13')
s.tooth_position = CONST.UL
s.note = '13-4-28-check all'
s.canal_type = 0
ps1 = '''
11.93283 2.44125 18.53397
11.97189 2.46078 17.65512
11.85471 2.51937 16.32708
11.50317 2.67561 15.23340
11.17116 3.06621 13.74912
10.64385 3.43728 12.22578
9.53064 4.12083 9.92124
8.24166 4.64814 7.65576
'''
ps2 = '''
4.68720 6.32772 8.51508
8.59320 4.47237 8.51508
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=9.4,
                      furcation_pos_lingual=9.7,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX14')
s.tooth_position = CONST.UL
s.note = '13-4-28-check all'
s.canal_type = 0
ps1 = '''
2.28501 3.51540 18.55350
2.34360 3.67164 17.88948
2.59749 3.94506 16.71768
2.89044 4.12083 15.23340
3.35916 4.31613 13.35852
3.86694 4.49190 11.91330
5.03874 4.92156 10.31184
'''
ps2 = '''
8.33931 6.38631 12.88980
4.23801 5.07780 12.88980
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=6.7,
                      furcation_pos_lingual=6.3,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX16')
s.tooth_position = CONST.UR
s.note = '13-4-28-check all'
s.canal_type = 0
ps1 = '''
13.90536 1.93347 18.43632
13.74912 1.97253 17.61606
13.43664 1.93347 16.63956
13.08510 2.22642 15.35058
12.46014 2.65608 13.78818
11.36646 3.18339 11.75706
10.68291 3.63258 10.50714
9.56970 4.58955 8.67132
'''
ps2 = '''
6.91362 6.30819 10.37043
10.44855 4.25754 10.37043
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=8.2,
                      furcation_pos_lingual=7.6,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX17')
s.tooth_position = CONST.UL
s.note = '13-4-28-check all'
s.canal_type = 0
ps1 = '''
11.69847 2.40219 18.35820
11.67894 2.49984 17.81136
11.50317 2.71467 16.75674
11.17116 2.85138 15.42870
10.68291 3.08574 13.78818
10.05795 3.49587 12.10860
9.27675 4.12083 10.19466
8.39790 4.72626 8.63226
'''
ps2 = '''
4.98015 6.01524 10.99539
9.33534 4.41378 10.99539
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=7.5,
                      furcation_pos_lingual=6.9,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)


# =====================================================
s = Specimen('MX18')
s.tooth_position = CONST.UR
s.note = '13-4-28-check all'
s.canal_type = 0
ps1 = '''
12.18672 2.85138 18.37773
12.06954 2.81232 17.77230
11.87424 2.90997 17.06922
11.60082 3.20292 15.85836
11.28834 3.51540 14.41314
10.83915 3.88647 12.49920
10.27278 4.31613 10.85868
9.06192 5.01921 8.82756
'''
ps2 = '''
5.91759 7.26516 10.38996
9.84312 4.90203 10.38996
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=8.6,
                      furcation_pos_lingual=7.3,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX19')
s.tooth_position = CONST.UL
s.note = '13-4-28-check all'
s.canal_type = 0
ps1 = '''
10.40949 1.56240 16.99110
10.37043 1.79676 16.28802
10.19466 2.16783 15.35058
9.78453 2.40219 14.10066
9.17910 2.69514 12.61638
8.67132 3.28104 10.58526
8.04636 3.65211 9.02286
7.71435 4.12083 7.69482
'''
ps2 = '''
4.58955 6.85503 8.41743
8.06589 3.80835 8.41743
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=9.6,
                      furcation_pos_lingual=9.9,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX20')
s.tooth_position = CONST.UR
s.note = '13-4-28-check all'
s.canal_type = 0
ps1 = '''
13.92489 2.01159 18.14337
13.53429 1.99206 17.38170
12.92886 2.16783 16.52238
12.57732 2.36313 15.23340
12.01095 2.77326 13.59288
11.40552 3.22245 12.30390
10.60479 3.71070 11.09304
9.82359 4.15989 9.92124
9.19863 4.35519 9.10098
'''
ps2 = '''
6.28866 6.79644 10.50714
10.09701 4.27707 10.50714
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=8.0,
                      furcation_pos_lingual=6.2,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX21')
s.tooth_position = CONST.UR
s.note = '13-4-28-check all'
s.canal_type = 0
ps1 = '''
10.89774 2.05065 17.94807
10.81962 2.42172 16.48332
10.60479 3.08574 14.80374
10.23372 3.63258 12.65544
9.72594 4.17942 10.93680
9.31581 4.57002 9.84312
8.82756 4.96062 8.63226
'''
ps2 = '''
5.62464 7.34328 10.19466
9.27675 5.07780 10.19466
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=7.6,
                      furcation_pos_lingual=7.3,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX23')
s.tooth_position = CONST.UL
s.note = '13-4-28-check all'
s.canal_type = 0
ps1 = '''
11.62035 2.98809 16.67862
11.40552 3.06621 15.93648
11.17116 3.26151 14.72562
10.91727 3.41775 13.43664
10.66338 3.63258 12.10860
10.38996 3.94506 11.01492
9.90171 4.27707 9.88218
9.23769 4.57002 8.55414
8.45649 5.23404 7.10892
'''
ps2 = '''
4.23801 6.69879 8.10495
8.04636 4.62861 8.10495
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=9.6,
                      furcation_pos_lingual=8.1,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX24')
s.tooth_position = CONST.UL
s.note = '13-4-28-check all'
s.canal_type = 0
ps1 = '''
10.05795 3.10527 18.98316
10.21419 3.10527 17.88948
10.31184 2.83185 16.83486
10.48761 2.77326 15.70212
10.48761 2.73420 14.49126
10.17513 3.00762 12.65544
9.62829 3.37869 10.97586
9.06192 3.74976 9.41346
8.55414 4.06224 8.00730
8.12448 4.45284 6.87456
'''
ps2 = '''
5.05827 6.15195 7.24563
8.10495 4.31613 7.24563
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=8.3,
                      furcation_pos_lingual=7.8,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX26')
s.tooth_position = CONST.UL
s.note = '13-4-28-check all'
s.canal_type = 0
ps1 = '''
11.95236 2.79279 18.24102
11.60082 3.06621 17.18640
11.01492 3.24198 15.93648
10.46808 3.49587 14.13972
9.72594 3.78882 12.61638
8.71038 4.10130 10.97586
7.90965 4.53096 9.37440
'''
ps2 = '''
3.24198 5.58558 10.25325
8.51508 4.70673 10.25325
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=8.0,
                      furcation_pos_lingual=8.2,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX27')
s.tooth_position = CONST.UR
s.note = '13-4-28-check all'
s.canal_type = 0
ps1 = '''
10.87821 3.53493 18.12384
10.83915 3.90600 17.03016
10.66338 4.29660 15.66306
10.33137 4.64814 14.06160
9.70641 4.92156 12.10860
9.04239 5.03874 10.07748
'''
ps2 = '''
3.69117 4.27707 10.52667
8.63226 2.67561 10.52667
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=6.0,
                      furcation_pos_lingual=5.9,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX28')
s.tooth_position = CONST.UR
s.note = '13-4-28-check all'
s.canal_type = 0
ps1 = '''
13.39758 5.54652 18.12384
13.41711 5.31216 17.57700
13.16322 5.23404 16.99110
12.87027 5.23404 16.36614
12.38202 5.25357 15.27246
11.63988 5.15592 13.51476
11.01492 5.17545 12.03048
10.07748 5.11686 10.19466
9.41346 5.07780 8.74944
9.00333 5.09733 7.81200
'''
ps2 = '''
4.58955 5.33169 9.12051
9.33534 5.09733 9.12051
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=8.6,
                      furcation_pos_lingual=6.8,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX29')
s.tooth_position = CONST.UR
s.note = '13-4-28-check all'
s.canal_type = 0
ps1 = '''
15.35058 5.39028 18.55350
14.97951 4.99968 17.69418
14.70609 4.76532 16.79580
14.25690 4.62861 15.35058
13.51476 4.55049 13.39758
12.57732 4.78485 11.67894
11.65941 4.90203 10.19466
10.85868 5.07780 9.02286
9.39393 5.19498 7.30422
'''
ps2 = '''
5.21451 7.34328 9.45252
11.50317 4.88250 9.45252
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=8.8,
                      furcation_pos_lingual=9.0,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX30')
s.tooth_position = CONST.UR
s.note = '13-4-28-check all'
s.canal_type = 0
ps1 = '''
12.61638 5.46840 18.57303
12.51873 5.39028 17.73324
12.12813 5.19498 16.48332
11.85471 5.29263 15.15528
11.30787 5.44887 13.35852
10.52667 5.66370 11.63988
9.55017 5.81994 9.92124
8.86662 5.72229 8.90568
'''
ps2 = '''
4.98015 6.71832 10.19466
9.72594 6.05430 10.19466
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=7.0,
                      furcation_pos_lingual=6.6,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX32')
s.tooth_position = CONST.UR
s.note = '13-4-28-check all'
s.canal_type = 0
ps1 = '''
11.87424 1.32804 18.06525
11.60082 1.73817 16.99110
11.07351 2.24595 15.81930
10.35090 2.81232 14.02254
9.66735 3.57399 11.99142
9.14004 4.23801 10.35090
8.43696 4.82391 8.86662
'''
ps2 = '''
6.30819 8.72991 10.85868
9.53064 4.39425 10.85868
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=8.0,
                      furcation_pos_lingual=6.4,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX33')
s.tooth_position = CONST.UL
s.note = '13-4-28-check all'
s.canal_type = 0
ps1 = '''
10.60479 0.68355 18.43632
10.35090 0.99603 17.57700
10.19466 1.32804 16.75674
9.96030 1.91394 15.42870
9.55017 2.55843 13.55382
8.96427 3.26151 11.40552
8.28072 3.98412 9.64782
7.44093 4.94109 7.77294
'''
ps2 = '''
4.47237 6.95268 8.90568
8.20260 4.00365 8.90568
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=8.4,
                      furcation_pos_lingual=9.5,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)

# =====================================================
s = Specimen('MX35')
s.tooth_position = CONST.UL
s.note = '13-4-28-check all'
s.canal_type = 0
ps1 = '''
10.78056 1.23039 18.16290
10.54620 1.50381 17.18640
10.13607 1.99206 16.17084
9.66735 2.49984 14.92092
9.17910 2.92950 13.20228
8.59320 3.65211 11.48364
7.67529 4.37472 10.07748
6.95268 5.29263 8.74944
'''
ps2 = '''
4.47237 8.71038 10.27278
7.75341 5.01921 10.27278
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)
s.canals.append(Canal(name='pre',
                      furcation_pos_buccal=6.7,
                      furcation_pos_lingual=5.8,
                      pts_buccal=ps1,
                      pts_bucco_lingual_vector=ps2,
                      path=s.get_default_path(directory_name, canal_suffix)))
roots.append(s)
