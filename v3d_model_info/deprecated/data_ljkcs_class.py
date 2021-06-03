# -*- coding: cp949 -*-
'''
Created on 2014. 4. 7.

@author: jongki
'''

from __future__ import division

import helpers_contours as du  # collection of utility function
from specimens.class_specimen import Specimen

roots = []
bounding_box_range = [(-2, 12), (-4, 10), (0, 14)]
#directory_name = 'E:/0.jongki.data/Dropbox/15.Develop/tooth-data/v3d_ljkcs/'  #'v3d_ljkcs/'
directory_name = 'D:/Dropbox/15.Develop/tooth-data/v3d_ljkcs/'  #'v3d_ljkcs/'
canal_pre_suffix = '-canal-pre-zoff.v3d'
canal_post_suffix = '-canal-post-zoff.v3d'
body_suffix = '-solid-body-zoff.v3d'


# ondemand 에서 realign을 하고 나면 이미지가 flip되서 저장--> 좌우가 바뀜
#===============================================================================
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
#===============================================================================
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
#===============================================================================


###########
# 0 - LJKCS01M

s = Specimen('LJKCS01M')
s.tooth_position=CONST.LR
s.note='check all'
s.canal_len_1 = 15.5
s.furcation_pos_1 = 13.6 
s.canal_len_2 = 15.1
s.furcation_pos_2 = 12.7 

#mesio-buccal pre-instrumentation

ps1_pre = '''
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
ps1_pre_not_use = '''
    6.10650 6.51360 17.87700
    5.92950 6.37200 17.55840
    5.77020 6.23040 17.09820
    5.62860 5.98260 16.51410
    5.45160 5.84100 15.98310
    5.15070 5.75250 15.32820
    4.67280 5.77020 14.63790
    3.96480 5.34540 13.52280
    3.29220 4.76130 12.19530
    2.88510 4.30110 10.69080
    2.83200 4.10640 9.09780
    2.93820 3.89400 7.87650
    3.29220 3.73470 6.17730
    3.57540 4.03560 5.50470
    4.00020 4.37190 4.46040
    4.21260 4.33650 3.84090
    '''
# 4th version    
ps1_post = '''
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

ps2_pre = '''
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
ps2_post = '''
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

s.bounding_box = bounding_box_range
s.canal_pre_path  = s.get_default_path(directory_name, canal_pre_suffix)  #directory_name+s.name.strip()+'/'+s.name.strip()+canal_suffix
s.canal_post_path = s.get_default_path(directory_name, canal_post_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) #directory_name+s.name.strip()+'/'+s.name.strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
s.set_pts1_pre( du.convert_to_points(ps1_pre) )
s.set_pts2_pre( du.convert_to_points(ps2_pre) )
s.set_pts1_post( du.convert_to_points(ps1_post) )
s.set_pts2_post( du.convert_to_points(ps2_post) )

roots.append(s)

###########
# 1 - LJKCS01D

s = Specimen('LJKCS01D')
s.tooth_position=CONST.LR
s.note='check all'
s.canal_len_1 = 13.6
s.furcation_pos_1 = 12.1 
s.canal_len_2 = 13.6
s.furcation_pos_2 = 12.2  

ps1_pre = '''
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
ps1_post = '''
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
ps2_pre = '''
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
ps2_post = '''
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
s.bounding_box = bounding_box_range
s.canal_pre_path  = s.get_default_path(directory_name, canal_pre_suffix)  #directory_name+s.name.strip()+'/'+s.name.strip()+canal_suffix
s.canal_post_path = s.get_default_path(directory_name, canal_post_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) #directory_name+s.name.strip()+'/'+s.name.strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
s.set_pts1_pre( du.convert_to_points(ps1_pre) )
s.set_pts2_pre( du.convert_to_points(ps2_pre) )
s.set_pts1_post( du.convert_to_points(ps1_post) )
s.set_pts2_post( du.convert_to_points(ps2_post) )
roots.append(s)



###########
# 2 - LJKCS05M

s = Specimen('LJKCS05M')
s.tooth_position=CONST.LR
s.note='check all'
s.canal_len_1 = 10.1
s.furcation_pos_1 = 8.9 
s.canal_len_2 = 9.7
s.furcation_pos_2 = 8.7  

#buccal pre
ps1_pre = '''
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
#buccal post
ps1_post = '''
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
#lingual pre
ps2_pre = '''
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
#lingual post
ps2_post = '''
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
s.bounding_box = bounding_box_range
s.canal_pre_path  = s.get_default_path(directory_name, canal_pre_suffix)  #directory_name+s.name.strip()+'/'+s.name.strip()+canal_suffix
s.canal_post_path = s.get_default_path(directory_name, canal_post_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) #directory_name+s.name.strip()+'/'+s.name.strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
s.set_pts1_pre( du.convert_to_points(ps1_pre) )
s.set_pts2_pre( du.convert_to_points(ps2_pre) )
s.set_pts1_post( du.convert_to_points(ps1_post) )
s.set_pts2_post( du.convert_to_points(ps2_post) )
roots.append(s)


###########
# 3 - LJKCS06M

s = Specimen('LJKCS06M')
s.tooth_position=CONST.LL
s.note='check all'
s.canal_len_1 = 11.0
s.furcation_pos_1 = 8.5 
s.canal_len_2 = 11.1
s.furcation_pos_2 = 8.9  

#buccal pre
ps2_pre = '''
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
#buccal post
ps2_post = '''
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
#lingual pre
ps1_pre = '''
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
#lingual post
ps1_post = '''
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
s.bounding_box = bounding_box_range
s.canal_pre_path  = s.get_default_path(directory_name, canal_pre_suffix)  #directory_name+s.name.strip()+'/'+s.name.strip()+canal_suffix
s.canal_post_path = s.get_default_path(directory_name, canal_post_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) #directory_name+s.name.strip()+'/'+s.name.strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
s.set_pts1_pre( du.convert_to_points(ps1_pre) )
s.set_pts2_pre( du.convert_to_points(ps2_pre) )
s.set_pts1_post( du.convert_to_points(ps1_post) )
s.set_pts2_post( du.convert_to_points(ps2_post) )
roots.append(s)


###########
# 4 - LJKCS10M

s = Specimen('LJKCS10M')
s.tooth_position=CONST.LL
s.note='check all'
s.canal_len_1 = 10.5
s.furcation_pos_1 = 8.1 
s.canal_len_2 = 10.6
s.furcation_pos_2 = 8.3  

#buccal pre
ps1_pre = '''
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

ps1_pre_not_use = '''
6.00030 4.53120 17.32830
5.94720 4.63740 17.18670
5.39850 4.86750 16.99200
4.63740 4.99140 16.81500
4.03560 5.09760 16.49640
3.61080 5.11530 16.07160
3.16830 5.20380 15.38130
2.88510 5.52240 14.05380
2.76120 5.96490 12.76170
2.79660 6.08880 11.73510
3.09750 6.14190 10.47840
3.23910 6.14190 9.82350
3.54000 6.44280 8.88540
    '''
#buccal post
ps1_post = '''
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
#lingual pre
ps2_pre = '''
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
#lingual post
ps2_post = '''
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
s.bounding_box = bounding_box_range
s.canal_pre_path  = s.get_default_path(directory_name, canal_pre_suffix)  #directory_name+s.name.strip()+'/'+s.name.strip()+canal_suffix
s.canal_post_path = s.get_default_path(directory_name, canal_post_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) #directory_name+s.name.strip()+'/'+s.name.strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
s.set_pts1_pre( du.convert_to_points(ps1_pre) )
s.set_pts2_pre( du.convert_to_points(ps2_pre) )
s.set_pts1_post( du.convert_to_points(ps1_post) )
s.set_pts2_post( du.convert_to_points(ps2_post) )
roots.append(s)
