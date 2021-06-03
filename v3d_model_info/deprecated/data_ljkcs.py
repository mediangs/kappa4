# -*- coding: cp949 -*-
'''
Created on 2014. 3. 28.

@author: jongki
'''
from __future__ import division
import helpers_contours as du       # collection of utility function
import const as CON          # constant       

roots = []
bounding_box_range = [(-2, 12), (-4, 10), (0, 14)]

directory_name = 'v3d_ljkcs/'
canal_pre_suffix = '-canal-pre-zoff.v3d'
canal_post_suffix = '-canal-post-zoff.v3d'
body_suffix = '-solid-body-zoff.v3d'
ELEM_COUNT = 11

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
root = range(ELEM_COUNT)
root[CON.NAME] = 'LJKCS01M'
root[CON.POS] = CONST.LL
root[CON.NOTE] = '13-3-19-check all'
ps1_pre = '''
6.10650 6.53130 17.89470
5.91180 6.35430 17.48760
5.73480 6.12420 16.86810
5.50470 5.85870 16.12470
5.02680 5.78790 15.08040
4.46040 5.68170 14.28390
3.87630 5.31000 13.38120
3.29220 4.76130 12.15990
2.93820 4.42500 11.00940
2.81430 4.19490 9.85890
2.86740 4.00020 8.33670
3.09750 3.80550 7.00920
3.38070 3.89400 5.85870
3.91170 4.44270 4.56660
4.51350 4.70820 3.62850
    '''
ps1_post = '''
6.07110 6.47820 17.91240
5.91180 6.33660 17.52300
5.80560 6.17730 17.06280
5.68170 6.03570 16.54950
5.39850 5.89410 16.01850
4.74360 5.62860 14.77950
4.03560 5.32770 13.69980
3.41610 4.93830 12.62010
2.99130 4.58430 11.32800
2.88510 4.31880 9.75270
3.04440 4.19490 8.33670
3.32760 4.12410 6.86760
3.77010 4.28340 5.02680
4.12410 4.37190 3.98250
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
6.05340 5.82330 17.11590
5.85870 5.75250 16.65570
5.50470 5.71710 16.08930
5.04450 5.85870 15.46980
4.56660 6.08880 14.77950
4.08870 6.42510 14.00070
3.59310 6.88530 12.95640
3.30990 7.20390 11.77050
3.29220 7.36320 10.24830
3.52230 7.39860 8.15970
3.91170 7.39860 6.03570
4.38960 7.25700 4.01790
    '''
    
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PRE_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_pre_suffix
root[CON.CANAL_POST_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_post_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1_PRE], root[CON.PS1_POST] = du.convert_to_points(ps1_pre), du.convert_to_points(ps1_post)
root[CON.PS2_PRE], root[CON.PS2_POST] = du.convert_to_points(ps2_pre), du.convert_to_points(ps2_post)
roots.append(root)


###########
# 0 - LJKCS01D
root = range(ELEM_COUNT)
root[CON.NAME] = 'LJKCS01D'
root[CON.POS] = CONST.LL
root[CON.NOTE] = '13-3-19-check all'
ps1_pre = '''
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
ps2_post = '''
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
    
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PRE_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_pre_suffix
root[CON.CANAL_POST_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_post_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1_PRE], root[CON.PS1_POST] = du.convert_to_points(ps1_pre), du.convert_to_points(ps1_post)
root[CON.PS2_PRE], root[CON.PS2_POST] = du.convert_to_points(ps2_pre), du.convert_to_points(ps2_post)
roots.append(root)
