# -*- coding: cp949 -*-
'''
Created on 2015. 5. 16.

@author: jongki
'''

from __future__ import division

import helpers_contours as du  # collection of utility function
from constant import CONST
from specimens.class_specimen import Specimen

roots = []
bounding_box_range = [(-2, 12), (-4, 10), (0, 14)]
#directory_name = 'E:/0.jongki.data/Dropbox/15.Develop/tooth-data/v3d_ljkrp1/'
directory_name = 'D:/Dropbox/15.Develop/tooth-data/v3d_ljkrp1/'
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
# 0 - BLX01

s = Specimen('BLX01')
s.tooth_position=CONST.LR
s.note='check all'
s.canal_len_1 = 15.5
s.furcation_pos_1 = 13.6 
s.canal_len_2 = 15.1
s.furcation_pos_2 = 12.7 

#mesio-buccal pre-instrumentation

#BLX01-buccal
ps1_pre = '''
    5.38080 6.51360 15.84150
    5.25690 6.60210 15.46980
    5.09760 6.77910 14.90340
    4.99140 7.04460 14.12460
    4.79670 7.11540 13.39890
    4.21260 7.11540 12.31920
    3.59310 7.38090 11.18640
    3.15060 7.85880 10.17750
    2.79660 8.26590 8.67300
    2.79660 8.51370 6.99150
    3.13290 8.76150 5.13300
    3.48690 8.70840 3.87630
    3.89400 8.42520 3.07980
    4.07100 8.19510 2.61960
    4.30110 8.01810 2.19480
    4.61970 7.91190 1.73460
'''

ps1_post = '''
    5.32770 6.51360 15.85920
    5.13300 6.74370 15.08040
    4.99140 6.86760 14.19540
    4.46040 7.02690 13.04490
    3.92940 7.25700 12.03600
    3.29220 7.68180 10.70850
    2.92050 8.19510 8.99160
    2.97360 8.40750 7.69950
    3.15060 8.53140 6.19500
    3.54000 8.46060 4.47810
    4.10640 8.21280 2.33640
    4.35420 8.10660 1.25670
    '''
ps2_pre = '''
    5.38080 6.51360 15.85920
    5.22150 6.65520 15.36360
    5.06220 6.90300 14.62020
    4.88520 7.08000 13.71750
    4.44270 7.00920 12.62010
    3.73470 6.40740 11.57580
    3.23910 5.68170 10.28370
    3.04440 5.32770 8.67300
    3.16830 5.31000 7.16850
    3.50460 5.09760 5.66400
    3.89400 4.86750 4.44270
    4.42500 5.00910 3.00900
    4.81440 4.77900 1.84080
    '''
ps2_post = '''
    5.38080 6.51360 15.85920
    5.22150 6.65520 15.36360
    5.06220 6.90300 14.62020
    4.88520 7.08000 13.71750
    4.44270 7.00920 12.62010
    3.73470 6.40740 11.57580
    3.23910 5.68170 10.28370
    3.04440 5.32770 8.67300
    3.16830 5.31000 7.16850
    3.50460 5.09760 5.66400
    3.89400 4.86750 4.44270
    4.42500 5.00910 3.00900
    4.81440 4.77900 1.84080
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
# 1 - BLX02

s = Specimen('BLX02')
s.tooth_position=CONST.LR
s.note='check all'
s.canal_len_1 = 15.5
s.furcation_pos_1 = 13.6 
s.canal_len_2 = 15.1
s.furcation_pos_2 = 12.7 

#mesio-buccal pre-instrumentation

#BLX02-buccal
ps1_pre = '''
    5.38080 6.51360 15.84150
    5.25690 6.60210 15.46980
    5.09760 6.77910 14.90340
    4.99140 7.04460 14.12460
    4.79670 7.11540 13.39890
    4.21260 7.11540 12.31920
    3.59310 7.38090 11.18640
    3.15060 7.85880 10.17750
    2.79660 8.26590 8.67300
    2.79660 8.51370 6.99150
    3.13290 8.76150 5.13300
    3.48690 8.70840 3.87630
    3.89400 8.42520 3.07980
    4.07100 8.19510 2.61960
    4.30110 8.01810 2.19480
    4.61970 7.91190 1.73460
'''

ps1_post = '''
    5.34540 6.53130 15.85920
    5.29230 6.60210 15.55830
    5.16840 6.70830 15.18660
    5.13300 6.84990 14.79720
    5.00910 6.95610 14.05380
    4.67280 7.00920 13.29270
    4.07100 7.20390 12.17760
    3.50460 7.50480 11.11560
    3.06210 7.91190 9.96510
    2.88510 8.37210 8.21280
    3.11520 8.56680 6.28350
    3.52230 8.49600 4.54890
    3.96480 8.31900 2.79660
    4.26570 8.17740 1.62840
    '''
ps2_pre = '''
    5.38080 6.51360 15.85920
    5.22150 6.65520 15.36360
    5.06220 6.90300 14.62020
    4.88520 7.08000 13.71750
    4.44270 7.00920 12.62010
    3.73470 6.40740 11.57580
    3.23910 5.68170 10.28370
    3.04440 5.32770 8.67300
    3.16830 5.31000 7.16850
    3.50460 5.09760 5.66400
    3.89400 4.86750 4.44270
    4.42500 5.00910 3.00900
    4.81440 4.77900 1.84080
    '''
ps2_post = '''
    5.38080 6.51360 15.85920
    5.22150 6.65520 15.36360
    5.06220 6.90300 14.62020
    4.88520 7.08000 13.71750
    4.44270 7.00920 12.62010
    3.73470 6.40740 11.57580
    3.23910 5.68170 10.28370
    3.04440 5.32770 8.67300
    3.16830 5.31000 7.16850
    3.50460 5.09760 5.66400
    3.89400 4.86750 4.44270
    4.42500 5.00910 3.00900
    4.81440 4.77900 1.84080
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
# 2 - PTU01

s = Specimen('PTU01')
s.tooth_position=CONST.LR
s.note='check all'
s.canal_len_1 = 15.5
s.furcation_pos_1 = 13.6 
s.canal_len_2 = 15.1
s.furcation_pos_2 = 12.7 

#mesio-buccal pre-instrumentation

ps1_pre = '''
    5.38080 6.51360 15.84150
    5.25690 6.60210 15.46980
    5.09760 6.77910 14.90340
    4.99140 7.04460 14.12460
    4.79670 7.11540 13.39890
    4.21260 7.11540 12.31920
    3.59310 7.38090 11.18640
    3.15060 7.85880 10.17750
    2.79660 8.26590 8.67300
    2.79660 8.51370 6.99150
    3.13290 8.76150 5.13300
    3.48690 8.70840 3.87630
    3.89400 8.42520 3.07980
    4.07100 8.19510 2.61960
    4.30110 8.01810 2.19480
    4.61970 7.91190 1.73460
'''
ps1_post = '''
    5.38080 6.51360 15.85920
    5.18610 6.67290 15.25740
    5.09760 6.88530 14.51400
    4.47810 7.06230 12.93870
    3.66390 7.46940 11.46960
    3.04440 8.01810 10.00050
    2.92050 8.38980 8.21280
    3.25680 8.47830 5.98260
    3.62850 8.46060 4.05330
    4.03560 8.30130 2.47800
    4.28340 8.17740 1.32750    
    '''
ps2_pre = '''
    5.38080 6.51360 15.85920
    5.22150 6.65520 15.36360
    5.06220 6.90300 14.62020
    4.88520 7.08000 13.71750
    4.44270 7.00920 12.62010
    3.73470 6.40740 11.57580
    3.23910 5.68170 10.28370
    3.04440 5.32770 8.67300
    3.16830 5.31000 7.16850
    3.50460 5.09760 5.66400
    3.89400 4.86750 4.44270
    4.42500 5.00910 3.00900
    4.81440 4.77900 1.84080
    '''
ps2_post = '''
    5.38080 6.51360 15.85920
    5.22150 6.65520 15.36360
    5.06220 6.90300 14.62020
    4.88520 7.08000 13.71750
    4.44270 7.00920 12.62010
    3.73470 6.40740 11.57580
    3.23910 5.68170 10.28370
    3.04440 5.32770 8.67300
    3.16830 5.31000 7.16850
    3.50460 5.09760 5.66400
    3.89400 4.86750 4.44270
    4.42500 5.00910 3.00900
    4.81440 4.77900 1.84080
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
# 3 - RCP01

s = Specimen('RCP01')
s.tooth_position=CONST.LR
s.note='check all'
s.canal_len_1 = 15.5
s.furcation_pos_1 = 13.6 
s.canal_len_2 = 15.1
s.furcation_pos_2 = 12.7 

#mesio-buccal pre-instrumentation

ps1_pre = '''
    5.38080 6.51360 15.84150
    5.25690 6.60210 15.46980
    5.09760 6.77910 14.90340
    4.99140 7.04460 14.12460
    4.79670 7.11540 13.39890
    4.21260 7.11540 12.31920
    3.59310 7.38090 11.18640
    3.15060 7.85880 10.17750
    2.79660 8.26590 8.67300
    2.79660 8.51370 6.99150
    3.13290 8.76150 5.13300
    3.48690 8.70840 3.87630
    3.89400 8.42520 3.07980
    4.07100 8.19510 2.61960
    4.30110 8.01810 2.19480
    4.61970 7.91190 1.73460
'''
ps1_post = '''
    5.34540 6.51360 15.85920
    5.23920 6.63750 15.52290
    5.07990 6.86760 14.72640
    4.84980 6.99150 13.78830
    4.28340 7.18620 12.47850
    3.85860 7.41630 11.68200
    3.36300 7.75260 10.56690
    3.09750 7.96500 9.78810
    2.88510 8.19510 8.77920
    2.84970 8.37210 7.55790
    2.99130 8.44290 6.31890
    3.29220 8.46060 5.02680
    4.00020 8.40750 2.70810
    4.28340 8.33670 1.69920
    '''
ps2_pre = '''
    5.38080 6.51360 15.85920
    5.22150 6.65520 15.36360
    5.06220 6.90300 14.62020
    4.88520 7.08000 13.71750
    4.44270 7.00920 12.62010
    3.73470 6.40740 11.57580
    3.23910 5.68170 10.28370
    3.04440 5.32770 8.67300
    3.16830 5.31000 7.16850
    3.50460 5.09760 5.66400
    3.89400 4.86750 4.44270
    4.42500 5.00910 3.00900
    4.81440 4.77900 1.84080
    '''
ps2_post = '''
    5.38080 6.51360 15.85920
    5.22150 6.65520 15.36360
    5.06220 6.90300 14.62020
    4.88520 7.08000 13.71750
    4.44270 7.00920 12.62010
    3.73470 6.40740 11.57580
    3.23910 5.68170 10.28370
    3.04440 5.32770 8.67300
    3.16830 5.31000 7.16850
    3.50460 5.09760 5.66400
    3.89400 4.86750 4.44270
    4.42500 5.00910 3.00900
    4.81440 4.77900 1.84080
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
# 4 - BLX_PTU

s = Specimen('BLX_PTU')
s.tooth_position=CONST.LR
s.note='check all'
s.canal_len_1 = 15.5
s.furcation_pos_1 = 13.6 
s.canal_len_2 = 15.1
s.furcation_pos_2 = 12.7 

#mesio-buccal pre-instrumentation

#BLX01 - post
ps1_pre = '''  
    5.32770 6.51360 15.85920
    5.13300 6.74370 15.08040
    4.99140 6.86760 14.19540
    4.46040 7.02690 13.04490
    3.92940 7.25700 12.03600
    3.29220 7.68180 10.70850
    2.92050 8.19510 8.99160
    2.97360 8.40750 7.69950
    3.15060 8.53140 6.19500
    3.54000 8.46060 4.47810
    4.10640 8.21280 2.33640
    4.35420 8.10660 1.25670
'''
#PTU01-post
ps1_post = '''
    5.38080 6.51360 15.85920
    5.18610 6.67290 15.25740
    5.09760 6.88530 14.51400
    4.47810 7.06230 12.93870
    3.66390 7.46940 11.46960
    3.04440 8.01810 10.00050
    2.92050 8.38980 8.21280
    3.25680 8.47830 5.98260
    3.62850 8.46060 4.05330
    4.03560 8.30130 2.47800
    4.28340 8.17740 1.32750    
    '''
ps2_pre = '''
    5.38080 6.51360 15.85920
    5.22150 6.65520 15.36360
    5.06220 6.90300 14.62020
    4.88520 7.08000 13.71750
    4.44270 7.00920 12.62010
    3.73470 6.40740 11.57580
    3.23910 5.68170 10.28370
    3.04440 5.32770 8.67300
    3.16830 5.31000 7.16850
    3.50460 5.09760 5.66400
    3.89400 4.86750 4.44270
    4.42500 5.00910 3.00900
    4.81440 4.77900 1.84080
    '''
ps2_post = '''
    5.38080 6.51360 15.85920
    5.22150 6.65520 15.36360
    5.06220 6.90300 14.62020
    4.88520 7.08000 13.71750
    4.44270 7.00920 12.62010
    3.73470 6.40740 11.57580
    3.23910 5.68170 10.28370
    3.04440 5.32770 8.67300
    3.16830 5.31000 7.16850
    3.50460 5.09760 5.66400
    3.89400 4.86750 4.44270
    4.42500 5.00910 3.00900
    4.81440 4.77900 1.84080
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
