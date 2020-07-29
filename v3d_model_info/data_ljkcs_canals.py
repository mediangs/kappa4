# -*- coding: cp949 -*-
'''
Created on 2014. 4. 7.

@author: jongki
'''

from __future__ import division
from constant import CONST
from class_specimen import Specimen, Canal
import os

specimens = []
directory_name = os.getenv('TOOTH_DATA') + '/v3d_ljkcs/'
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


# mesio-buccal pre
ljkcs01_mb_pre = '''
    6.10650 6.51360 17.87700
    5.98260 6.42510 17.62920
    5.84100 6.30120 17.34600
    5.73480 6.14190 16.86810
    5.45160 5.85870 15.93000
    4.92060 5.75250 14.93880
    4.31880 5.64630 14.07150
    3.62850 5.09760 12.95640
    3.15060 4.67280 11.73510
    2.83200 4.24800 10.03590
    2.88510 4.01790 8.33670
    3.15060 3.84090 6.76140
    3.32760 3.89400 5.96490
    3.69930 4.21260 5.13300
    4.38960 4.40730 3.87630
'''

# 4th version
# BUCCAL - POST
ljkcs01_mb_post = '''
    6.07110 6.47820 17.84160
    5.84100 6.23040 17.23980
    5.71710 6.08880 16.65570
    5.27460 5.84100 15.71760
    4.70820 5.66400 14.74410
    3.91170 5.23920 13.48740
    3.32760 4.86750 12.40770
    2.95590 4.53120 11.04480
    2.90280 4.31880 9.61110
    3.06210 4.23030 8.40750
    3.32760 4.12410 6.83220
    3.71700 4.24800 5.31000
    4.14180 4.49580 3.73470
    '''

# LINGUAL - PRE
ljkcs01_ml_pre = '''
    6.08880 6.51360 17.87700
    5.89410 6.35430 17.45220
    5.75250 6.17730 16.97430
    5.52240 5.89410 16.16010
    5.00910 5.82330 15.04500
    4.28340 6.28350 14.10690
    3.73470 6.92070 13.09800
    3.39840 7.25700 12.12450
    3.18600 7.48710 10.38990
    3.20370 7.34550 9.02700
    3.38070 7.43400 7.80570
    3.92940 7.48710 5.89410
    4.24800 7.46940 4.81440
    4.42500 7.50480 3.98250
    '''

ljkcs01_ml_post = '''
    6.07110 5.84100 17.15130
    5.64630 5.71710 16.30170
    5.09760 5.77020 15.57600
    4.49580 6.14190 14.70870
    3.92940 6.56670 13.69980
    3.46920 6.99150 12.65550
    3.22140 7.31010 11.08020
    3.36300 7.39860 9.13320
    3.61080 7.41630 7.62870
    4.05330 7.34550 5.46930
    4.44270 7.29240 3.52230
    '''

ljkcs01_db_pre = '''
    11.75280 6.70830 17.36370
    11.27490 6.47820 16.76190
    11.02710 6.30120 16.37250
    10.54920 6.10650 16.08930
    10.08900 5.92950 15.57600
    9.71730 5.84100 14.63790
    9.43410 5.69940 13.38120
    9.15090 5.41620 11.18640
    8.90310 5.31000 9.20400
    8.61990 5.22150 7.66410
    8.44290 5.20380 6.72600
    8.24820 5.41620 5.54010
    7.96500 5.41620 4.46040
    '''
ljkcs01_db_post = '''
    11.73510 6.63750 17.29290
    11.43420 6.44280 17.15130
    11.15100 6.28350 16.90350
    10.56690 6.12420 16.37250
    10.00050 6.00030 15.50520
    9.64650 5.78790 14.35470
    9.31020 5.55780 12.72630
    9.00930 5.39850 10.79700
    8.79690 5.31000 9.27480
    8.46060 5.29230 7.25700
    8.21280 5.36310 5.71710
    7.94730 5.41620 4.70820
    '''
ljkcs01_dl_pre = '''
    11.75280 6.70830 17.31060
    11.38110 6.53130 16.79730
    11.06250 6.31890 16.40790
    10.63770 6.14190 16.12470
    10.30140 6.10650 15.89460
    9.82350 6.12420 15.08040
    9.39870 6.24810 13.55820
    9.25710 6.53130 12.08910
    9.15090 6.61980 10.90320
    9.06240 6.63750 9.75270
    8.79690 6.60210 8.12430
    8.53140 6.65520 6.86760
    8.21280 6.77910 5.50470
    7.89420 7.02690 4.23030
    '''
ljkcs01_dl_post = '''
    11.75280 6.63750 17.32830
    11.15100 6.30120 16.83270
    10.56690 6.12420 16.33710
    10.10670 6.03570 15.64680
    9.69960 6.12420 14.63790
    9.43410 6.24810 13.20420
    9.16860 6.40740 11.15100
    8.85000 6.53130 9.09780
    8.44290 6.65520 6.69060
    8.01810 6.79680 4.63740   
    '''


###########
# 0 - LJKCS01

s = Specimen('LJKCS01')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

cnl_pre_mb = Canal(name='pre-mb', length=15.5, furcation_pos=13.6,
                   pts_canal=ljkcs01_mb_pre, pts_opposite=ljkcs01_ml_pre, is_buccal_side=True,
                   path=s.get_default_path(directory_name, canal_pre_suffix))

cnl_pre_ml = Canal(name='pre-ml', length=15.1, furcation_pos=12.7,
                   pts_canal=ljkcs01_ml_pre, pts_opposite=ljkcs01_mb_pre, is_buccal_side=False,
                   path=s.get_default_path(directory_name, canal_pre_suffix))

cnl_blx_mb = Canal(name='blx-mb', length=15.5, furcation_pos=13.6,
                   pts_canal=ljkcs01_mb_post, pts_opposite=ljkcs01_ml_pre, is_buccal_side=True,
                   path=s.get_default_path(directory_name, canal_post_suffix))

cnl_blx_ml = Canal(name='blx-ml', length=15.1, furcation_pos=12.7,
                   pts_canal=ljkcs01_ml_post, pts_opposite=ljkcs01_mb_pre, is_buccal_side=False,
                   path=s.get_default_path(directory_name, canal_post_suffix))

cnl_pre_mb.cnls_cmp_name = ['blx-mb']
cnl_pre_ml.cnls_cmp_name = ['blx-ml']

s.canals.append(cnl_pre_mb)
s.canals.append(cnl_pre_ml)
s.canals.append(cnl_blx_mb)
s.canals.append(cnl_blx_ml)

cnl_pre_db = Canal(name='pre-db', length=13.6, furcation_pos=12.1,
                   pts_canal=ljkcs01_db_pre, pts_opposite=ljkcs01_dl_pre, is_buccal_side=True,
                   path=s.get_default_path(directory_name, canal_pre_suffix))
cnl_pre_dl = Canal(name='pre-dl', length=13.6, furcation_pos=12.2,
                   pts_canal=ljkcs01_dl_pre, pts_opposite=ljkcs01_db_pre, is_buccal_side=False,
                   path=s.get_default_path(directory_name, canal_pre_suffix))
cnl_blx_db = Canal(name='blx-db', length=13.6, furcation_pos=12.1,
                   pts_canal=ljkcs01_db_post, pts_opposite=ljkcs01_dl_post, is_buccal_side=True,
                   path=s.get_default_path(directory_name, canal_post_suffix))
cnl_blx_dl = Canal(name='blx-dl', length=13.6, furcation_pos=12.2,
                   pts_canal=ljkcs01_dl_post, pts_opposite=ljkcs01_db_pre, is_buccal_side=False,
                   path=s.get_default_path(directory_name, canal_post_suffix))

cnl_pre_db.cnls_cmp_name = ['blx-db']
cnl_pre_dl.cnls_cmp_name = ['blx-dl']

s.canals.append(cnl_pre_db)
s.canals.append(cnl_pre_dl)
s.canals.append(cnl_blx_db)
s.canals.append(cnl_blx_dl)

specimens.append(s)

###########
# 0 - LJKCS01M

s = Specimen('LJKCS01M')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-mb', length=15.5, furcation_pos=13.6, cnls_cmp_name=['blx-mb'],
                      pts_canal=ljkcs01_mb_pre, pts_opposite=ljkcs01_ml_pre, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

s.canals.append(Canal(name='pre-ml', length=15.1, furcation_pos=12.7, cnls_cmp_name=['blx-ml'],
                      pts_canal=ljkcs01_ml_pre, pts_opposite=ljkcs01_mb_pre, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

s.canals.append(Canal(name='blx-mb', length=15.5, furcation_pos=13.6,
                      pts_canal=ljkcs01_mb_post, pts_opposite=ljkcs01_ml_pre, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_post_suffix)))

s.canals.append(Canal(name='blx-ml', length=15.1, furcation_pos=12.7,
                      pts_canal=ljkcs01_ml_post, pts_opposite=ljkcs01_mb_pre, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_post_suffix)))

specimens.append(s)

###########
# 1 - LJKCS01D

s = Specimen('LJKCS01D')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)


s.canals.append(Canal(name='pre-db', length=13.6, furcation_pos=12.1, cnls_cmp_name=['blx-db'],
                      pts_canal=ljkcs01_db_pre, pts_opposite=ljkcs01_dl_pre, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

s.canals.append(Canal(name='pre-dl', length=13.6, furcation_pos=12.2, cnls_cmp_name=['blx-dl'],
                      pts_canal=ljkcs01_dl_pre, pts_opposite=ljkcs01_db_pre, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

s.canals.append(Canal(name='blx-db', length=13.6, furcation_pos=12.1,
                      pts_canal=ljkcs01_db_post, pts_opposite=ljkcs01_dl_post, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_post_suffix)))

s.canals.append(Canal(name='blx-dl', length=13.6, furcation_pos=12.2,
                      pts_canal=ljkcs01_dl_post, pts_opposite=ljkcs01_db_pre, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_post_suffix)))

specimens.append(s)




###########
# 2 - LJKCS05M

s = Specimen('LJKCS05M')
s.tooth_position = CONST.LR
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

# buccal pre
mb_pre = '''
    3.38070 3.82320 19.85940
    3.32760 3.84090 19.66470
    3.20370 3.77010 19.31070
    3.23910 3.66390 18.81510
    3.27450 3.55770 18.30180
    3.22140 3.41610 17.62920
    3.22140 3.29220 16.69110
    3.13290 3.25680 15.59370
    3.16830 3.39840 14.30160
    3.32760 3.57540 13.15110
    3.54000 3.84090 12.14220
    3.78780 4.05330 11.29260
    4.01790 4.28340 10.00050
    '''
# buccal post
mb_post = '''
    3.34530 3.82320 19.82400
    3.27450 3.78780 19.52310
    3.25680 3.66390 18.99210
    3.22140 3.52230 18.40800
    3.18600 3.39840 17.59380
    3.15060 3.30990 16.47870
    3.20370 3.39840 14.90340
    3.36300 3.62850 13.50510
    3.57540 3.87630 12.14220
    3.85860 4.14180 10.74390
    4.01790 4.33650 9.61110
    '''
# lingual pre
ml_pre = '''
    3.15060 5.09760 19.54080
    3.02670 5.07990 19.36380
    2.84970 5.07990 19.11600
    2.81430 5.15070 18.81510
    2.76120 5.16840 18.33720
    2.74350 5.25690 18.05400
    2.72580 5.38080 17.55840
    2.69040 5.57550 17.02740
    2.65500 5.77020 16.47870
    2.76120 6.01800 15.77070
    2.90280 6.33660 14.76180
    2.97360 6.40740 13.64670
    3.09750 6.33660 12.47850
    3.45150 6.26580 11.39880
    3.68160 6.26580 10.81470
    3.78780 6.33660 10.21290
    '''
# lingual post
ml_post = '''
    3.04440 5.02680 19.55850
    2.88510 5.04450 19.23990
    2.74350 5.13300 18.63810
    2.67270 5.39850 17.84160
    2.67270 5.71710 16.90350
    2.76120 5.96490 15.94770
    2.95590 6.24810 14.37240
    3.22140 6.33660 12.76170
    3.55770 6.33660 10.90320
    3.77010 6.31890 9.82350
    '''


s.canals.append(Canal(name='pre-mb', length=10.1, furcation_pos=8.9, cnls_cmp_name=['blx-mb'],
                      pts_canal=mb_pre, pts_opposite=ml_pre, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

s.canals.append(Canal(name='pre-ml', length=9.7, furcation_pos=8.7, cnls_cmp_name=['blx-ml'],
                      pts_canal=ml_pre, pts_opposite=mb_pre, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

s.canals.append(Canal(name='blx-mb', length=10.1, furcation_pos=8.9,
                      pts_canal=mb_post, pts_opposite=ml_pre, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_post_suffix)))

s.canals.append(Canal(name='blx-ml', length=9.7, furcation_pos=8.7,
                      pts_canal=ml_post, pts_opposite=mb_pre, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_post_suffix)))

specimens.append(s)

###########
# 3 - LJKCS06M

s = Specimen('LJKCS06M')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

ml_pre = '''
3.22140 6.56670 20.46120
3.00900 6.31890 19.70010
2.74350 6.17730 18.70890
2.63730 5.82330 17.45220
2.74350 5.34540 16.23090
2.83200 4.81440 15.11580
2.97360 4.37190 13.98300
3.32760 4.31880 12.58470
3.78780 4.47810 11.46960
4.05330 4.46040 10.74390
4.33650 4.38960 10.03590
    '''

ml_post = '''
3.16830 6.53130 20.40810
2.95590 6.31890 19.59390
2.69040 5.92950 18.26640
2.69040 5.29230 16.86810
2.77890 4.88520 15.66450
2.99130 4.54890 14.40780
3.32760 4.37190 13.00950
3.77010 4.30110 11.36340
4.26570 4.21260 9.89430
    '''

mb_pre = '''
3.18600 6.54900 20.44350
2.99130 6.31890 19.66470
2.70810 6.17730 18.51420
2.61960 6.19500 17.20440
2.76120 6.38970 16.12470
2.90280 6.51360 14.51400
3.25680 6.28350 13.04490
3.85860 5.92950 11.50500
4.31880 5.87640 10.67310
4.61970 5.98260 10.00050
    '''

mb_post = '''
3.15060 6.51360 20.39040
2.95590 6.31890 19.62930
2.74350 6.23040 18.74430
2.61960 6.26580 17.62920
2.65500 6.38970 16.30170
2.90280 6.40740 14.76180
3.18600 6.33660 13.64670
3.55770 6.23040 12.53160
3.91170 6.10650 11.45190
4.54890 6.05340 9.94740
    '''

s.canals.append(Canal(name='pre-mb', length=11.0, furcation_pos=8.5, cnls_cmp_name=['blx-mb'],
                      pts_canal=mb_pre, pts_opposite=ml_pre, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

s.canals.append(Canal(name='pre-ml', length=11.1, furcation_pos=8.9, cnls_cmp_name=['blx-ml'],
                      pts_canal=ml_pre, pts_opposite=mb_pre, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

s.canals.append(Canal(name='blx-mb', length=11.0, furcation_pos=8.5,
                      pts_canal=mb_post, pts_opposite=ml_pre, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_post_suffix)))

s.canals.append(Canal(name='blx-ml', length=11.1, furcation_pos=8.9,
                      pts_canal=ml_post, pts_opposite=mb_pre, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_post_suffix)))

specimens.append(s)


###########
# 4 - LJKCS10M

s = Specimen('LJKCS10M')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

# buccal pre
mb_pre = '''
6.05340 4.49580 17.39910
5.91180 4.60200 17.13360
5.59320 4.72590 17.06280
5.11530 4.84980 16.99200
4.63740 4.95600 16.83270
4.08870 5.02680 16.51410
3.54000 5.13300 16.00080
3.11520 5.32770 15.09810
2.90280 5.59320 13.96530
2.77890 5.85870 13.04490
2.81430 6.07110 11.68200
3.09750 5.96490 10.24830
3.34530 6.07110 9.32790
3.57540 6.21270 8.81460
    '''

# buccal post
mb_post = '''
5.92950 4.51350 17.23980
5.54010 4.65510 17.15130
5.23920 4.69050 17.06280
4.93830 4.76130 16.99200
4.47810 4.86750 16.77960
3.87630 5.02680 16.39020  
3.27450 5.23920 15.64680
2.92050 5.48700 14.60250
2.81430 5.82330 12.92100
2.99130 5.96490 11.55810
3.20370 6.14190 10.05360
3.57540 6.24810 8.69070
    '''
# lingual pre
ml_pre = '''
6.00030 4.51350 17.31060
5.71710 4.40730 17.15130
5.23920 4.26570 17.00970
4.58430 4.19490 16.88580
4.01790 4.19490 16.60260
3.52230 4.17720 16.21320
3.15060 4.12410 15.61140
2.90280 3.91170 14.54940
2.74350 3.77010 13.52280
2.72580 3.61080 12.19530
2.99130 3.78780 10.79700
3.20370 4.05330 9.75270
3.48690 4.17720 8.60220
    '''
# lingual post
ml_post = '''
5.94720 4.51350 17.25750
5.52240 4.46040 17.11590
5.06220 4.51350 17.09820
4.79670 4.42500 16.99200
4.40730 4.37190 16.83270
3.77010 4.21260 16.39020
3.27450 4.07100 15.71760
2.88510 3.87630 14.70870
2.79660 3.80550 13.87680
2.83200 3.75240 12.47850
2.97360 3.77010 11.16870
3.43380 4.15950 8.58450
    '''

s.canals.append(Canal(name='pre-mb', length=10.5, furcation_pos=8.1, cnls_cmp_name=['blx-mb'],
                      pts_canal=mb_pre, pts_opposite=ml_pre, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

s.canals.append(Canal(name='pre-ml', length=10.6, furcation_pos=8.3, cnls_cmp_name=['blx-ml'],
                      pts_canal=ml_pre, pts_opposite=mb_pre, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

s.canals.append(Canal(name='blx-mb', length=10.5, furcation_pos=8.1,
                      pts_canal=mb_post, pts_opposite=ml_pre, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_post_suffix)))

s.canals.append(Canal(name='blx-ml', length=10.6, furcation_pos=8.3,
                      pts_canal=ml_post, pts_opposite=mb_pre, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_post_suffix)))

specimens.append(s)


###########
# 4 - LJKCS04

s = Specimen('LJKCS04')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

mb_post = '''
6.40740 5.39850 20.99220
6.42510 5.39850 20.37270
6.08880 5.59320 19.22220
5.61090 5.62860 18.19560
4.99140 5.34540 16.70880
4.51350 4.99140 15.11580
4.38960 4.81440 13.66440
4.35420 4.76130 12.58470
4.37190 4.72590 11.20410
4.28340 4.69050 9.66420
   '''

ml_post = '''
6.40740 5.41620 21.00990
6.42510 5.39850 20.42580
6.15960 5.64630 19.38150
5.78790 5.75250 18.40800
5.07990 5.78790 17.13360
4.47810 5.94720 15.85920
3.98250 6.00030 14.49630
3.73470 5.92950 12.85020
3.73470 5.80560 11.68200
3.84090 5.62860 9.66420
    '''

d_post = '''
6.40740 5.39850 20.97450
6.40740 5.39850 20.10720
6.56670 5.31000 19.52310
6.61980 5.25690 18.35490
6.63750 5.15070 16.97430
6.58440 5.09760 15.59370
6.49590 5.09760 13.85910
6.37200 5.13300 11.84130
6.30120 5.15070 10.67310
6.23040 5.13300 9.45180
    '''

BPV = '''
4.90290 1.66380 9.92970
4.70820 7.92960 9.92970
'''

mb_pre, ml_pre, d_pre = mb_post, ml_post, d_post

s.canals.append(Canal(name='pre-mb',  cnls_cmp_name=['blx-mb'],
                      pts_canal=mb_pre, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

s.canals.append(Canal(name='pre-ml',  cnls_cmp_name=['blx-ml'],
                      pts_canal=ml_pre, pts_vector=BPV, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

s.canals.append(Canal(name='pre-d',  cnls_cmp_name=['blx-d'],
                      pts_canal=d_pre, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

s.canals.append(Canal(name='blx-mb',
                      pts_canal=mb_post, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_post_suffix)))

s.canals.append(Canal(name='blx-ml',
                      pts_canal=ml_post, pts_vector=BPV, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_post_suffix)))

s.canals.append(Canal(name='blx-d',
                      pts_canal=d_post, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_post_suffix)))

specimens.append(s)



###########
# 4 - LJKCS08

s = Specimen('LJKCS08')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

m_post = '''
5.55780 4.60200 21.45240
5.23920 5.09760 20.81520
4.92060 5.36310 20.12490
4.51350 5.43390 19.00980
4.03560 5.41620 17.46990
3.78780 5.22150 15.61140
3.82320 5.07990 14.28390
3.98250 4.93830 12.65550
4.14180 4.86750 11.46960
4.42500 4.76130 10.24830
4.53120 4.79670 9.23940
   '''

d_post = '''
10.54920 4.49580 20.97450
10.28370 4.60200 20.63820
9.87660 4.65510 20.00100
9.45180 4.65510 18.62040
9.09780 4.61970 17.09820
8.77920 4.53120 15.32820
8.44290 4.54890 13.80600
8.03580 4.56660 11.94750
7.57560 4.61970 10.35450
7.13310 4.74360 9.18630
    '''

BPV = '''
6.15960 1.30980 6.70830
5.75250 8.67300 6.70830
'''

m_pre, d_pre = m_post, d_post

s.canals.append(Canal(name='pre-m',  cnls_cmp_name=['blx-m'],
                      pts_canal=m_pre, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

s.canals.append(Canal(name='pre-d',  cnls_cmp_name=['blx-d'],
                      pts_canal=d_pre, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

s.canals.append(Canal(name='blx-m',
                      pts_canal=m_post, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_post_suffix)))

s.canals.append(Canal(name='blx-d',
                      pts_canal=d_post, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_post_suffix)))

specimens.append(s)



###########
# 4 - LJKCS11

s = Specimen('LJKCS11')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

mb_pre = '''
4.46874 5.65216 21.07196
4.22146 5.75814 20.48908
4.02716 5.79346 19.78256
3.81521 5.74048 18.93474
3.62092 5.58151 17.83963
3.49727 5.31656 16.35594
3.40896 4.66303 14.50132
3.49727 4.39809 13.17660
3.85053 4.46874 11.53394
4.23912 4.62771 9.99726
4.45108 4.59238 9.18476
   '''

ml_pre = '''
4.45108 5.65216 21.05430
4.18613 5.74048 20.38310
3.93885 5.82879 19.42930
3.65624 5.89944 18.21055
3.49727 5.97009 16.77985
3.44429 6.04075 15.03121
3.56793 6.07607 13.22959
3.86820 5.93477 11.95785
4.18613 5.68749 10.95106
4.52173 5.63450 9.78530
4.73368 5.63450 9.14943
   '''

d_pre = '''
8.99047 5.51086 19.88854
8.76085 5.54618 19.42930
8.65487 5.56385 18.84642
8.54889 5.61683 17.99860
8.46058 5.66982 16.56789
8.33694 5.68749 14.87225
8.14264 5.58151 13.28258
7.87770 5.58151 11.90486
7.61275 5.58151 10.47416
7.31248 5.51086 9.25541
    '''

BPV = '''
6.60596 1.04212 6.72960
5.84645 9.48503 6.72960
'''

s.canals.append(Canal(name='pre-mb',
                      pts_canal=mb_pre, pts_opposite=ml_pre, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

s.canals.append(Canal(name='pre-ml',
                      pts_canal=ml_pre, pts_opposite=mb_pre, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

s.canals.append(Canal(name='pre-d',
                      pts_canal=d_pre, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

specimens.append(s)



###########
# 4 - LJKCS12

s = Specimen('LJKCS12')
s.tooth_position = CONST.LL
s.note = 'check all'
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

mb_pre = '''
7.61275 4.41575 18.89941
7.55976 4.50407 18.42251
7.54210 4.99863 17.55702
7.73639 5.36955 16.86817
7.84237 5.75814 16.03800
8.17797 6.21738 14.96056
8.35460 6.53531 14.21872
8.49590 6.81792 12.91165
8.33694 6.58830 11.48095
7.84237 6.27037 10.26220
7.48911 6.51765 8.83150
7.11819 6.67661 8.19563
   '''

ml_pre = '''
7.41846 3.76222 18.95240
7.24183 3.46195 18.35186
7.17118 3.40896 17.82197
7.24183 3.39130 16.77985
7.45379 3.44429 15.96735
7.80705 3.55026 14.76627
8.24862 3.76222 12.91165
8.19563 4.04483 11.48095
7.94835 4.57472 10.52715
7.48911 4.85733 9.36139
6.87091 4.91031 8.24862
   '''

d_pre = '''
2.63179 4.61004 18.82876
2.61412 4.78667 18.35186
2.68478 4.92798 17.39806
2.96738 5.05162 15.61409
3.37363 5.31656 13.54752
3.76222 5.38722 11.79888
4.41575 5.35189 9.94427
5.05162 5.52852 7.98368
    '''

BPV = '''
6.42933 9.74998 6.42933
6.81792 1.83695 6.42933
'''

s.canals.append(Canal(name='pre-mb',
                      pts_canal=mb_pre, pts_opposite=ml_pre, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

s.canals.append(Canal(name='pre-ml',
                      pts_canal=ml_pre, pts_opposite=mb_pre, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

s.canals.append(Canal(name='pre-d',
                      pts_canal=d_pre, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_pre_suffix)))

specimens.append(s)



