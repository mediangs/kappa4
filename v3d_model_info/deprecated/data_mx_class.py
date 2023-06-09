# -*- coding: cp949 -*-

'''
Created on 2014. 4. 9.

@author: jongki

data from jongki(Mx6)
�ȵ� �尩�� ������� ġ��
'''

from __future__ import division

import helpers_contours as du  # collection of utility function
from constant import CONST
from specimens.class_specimen import Specimen

roots = []
bounding_box_range = [(-10, 20), (-10, 20), (-2, 28)]
directory_name = 'E:/0.jongki.data/Dropbox/15.Develop/tooth-data/v3d_mx/'
canal_suffix = '-canal-zoff.v3d'
body_suffix = '-solid-body-zoff.v3d'


#===============================================================================
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
#===============================================================================

#===============================================================================
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
#===============================================================================


s = Specimen('MX01')
s.location = CONST.UL
s.note='13-4-14-check all'
s.furcation_pos_1 = 9.0 
s.furcation_pos_2 = 7.9 
s.canal_type = 0
ps1 = '''
    2.07018 8.26119 18.16290 
    2.24595 8.30025 17.77230 
    2.42172 8.47602 17.30358 
    2.53890 8.61273 16.71768 
    2.49984 8.74944 15.58494 
    2.55843 8.84709 14.53032 
    2.65608 8.84709 13.59288 
    2.77326 8.76897 12.14766 
    2.94903 8.26119 9.80406 
    3.33963 7.89012 8.74944 
    3.57399 7.51905 8.00730 
    3.82788 7.24563 7.22610 
'''
ps2 = '''
    5.33169 8.78850 16.60050 
    5.27310 8.86662 16.01460 
    5.07780 9.04239 15.23340 
    5.01921 9.12051 14.60844 
    4.99968 9.17910 13.78818 
    5.07780 9.14004 12.69450 
    5.40981 9.10098 11.09304 
    5.87853 9.04239 10.15560 
    6.21054 8.76897 9.29628 
    6.32772 8.28072 8.63226 
    6.21054 7.61670 7.92918 
    5.76135 7.26516 7.06986 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX02')
s.location = CONST.UR
s.note='13-4-14-check all'
s.furcation_pos_1 = 8.0 
s.furcation_pos_2 = 7.1 
s.canal_type = 0
ps1 = '''
    2.81232 3.88647 18.20196 
    2.96856 3.80835 17.88948 
    3.12480 3.57399 17.14734 
    3.18339 3.39822 16.32708 
    3.16386 3.30057 15.42870 
    3.00762 3.16386 14.41314 
    2.96856 3.12480 13.39758 
    3.20292 3.30057 12.38202 
    3.71070 3.73023 11.21022 
    4.15989 4.08177 10.38996 
    4.41378 4.60908 9.29628 
'''
ps2 = '''
    4.51143 4.12083 18.02619 
    4.43331 3.92553 17.57700 
    4.39425 3.78882 17.26452 
    4.37472 3.61305 16.60050 
    4.27707 3.47634 15.31152 
    4.31613 3.39822 14.64750 
    4.51143 3.35916 13.98348 
    4.68720 3.37869 13.20228 
    4.70673 3.43728 12.18672 
    4.68720 3.84741 10.93680 
    4.49190 4.33566 9.88218 
    4.47237 4.62861 9.33534 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX03')
s.location = CONST.UL
s.note='13-4-21-check all'
s.furcation_pos_1 = 6.8 
s.furcation_pos_2 = 7.7 
s.canal_type = 0
ps1 = '''
    2.10924 8.37837 16.30755 
    2.46078 8.39790 15.74118 
    2.77326 8.51508 15.27246 
    2.90997 8.65179 13.98348 
    3.33963 8.63226 12.96792 
    3.47634 8.53461 11.44458 
    3.82788 8.14401 9.92124 
    4.12083 7.77294 8.94474 
    4.45284 7.20657 8.24166 
'''
ps2 = '''
    3.78882 7.94871 16.56144 
    3.71070 8.22213 15.81930 
    3.71070 8.35884 15.19434 
    4.08177 8.33931 14.41314 
    4.04271 8.57367 13.28040 
    4.64814 8.49555 12.22578 
    5.37075 8.35884 11.32740 
    5.70276 8.08542 10.46808 
    5.50746 7.51905 9.33534 
    5.52699 7.03080 8.39790 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX04')
s.location = CONST.UR
s.note='13-4-21-check all'
s.furcation_pos_1 = 8.2 
s.furcation_pos_2 = 8.3 
s.canal_type = 0
ps1 = '''
    3.53493 3.32010 14.68656 
    3.59352 3.32010 13.78818 
    3.53493 3.39822 12.92886 
    3.33963 3.51540 11.60082 
    3.20292 3.59352 10.31184 
    3.32010 3.74976 8.67132 
    3.57399 4.06224 7.42140 
    4.02318 4.49190 6.05430 
    4.14036 4.68720 5.27310 
'''
ps2 = '''
    3.53493 3.30057 14.66703 
    3.63258 3.33963 13.59288 
    3.51540 3.39822 12.61638 
    3.53493 3.37869 10.97586 
    3.88647 3.32010 9.25722 
    4.37472 3.28104 8.00730 
    4.51143 3.78882 6.67926 
    4.70673 4.29660 5.54652 
    5.21451 4.70673 4.72626 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX05')
s.location = CONST.UR
s.note='13-4-21-check all'
s.furcation_pos_1 = 10.0 
s.furcation_pos_2 = 9.1 
s.canal_type = 0
ps1 = '''
    2.92950 7.49952 18.00666 
    2.87091 7.20657 17.42076 
    2.71467 6.91362 16.32708 
    2.73420 6.73785 15.07716 
    2.81232 6.58161 13.43664 
    2.87091 6.64020 12.03048 
    3.00762 6.75738 10.42902 
    3.80835 6.65973 8.90568 
    4.27707 6.67926 7.92918 
    4.68720 6.73785 7.06986 
'''
ps2 = '''
    3.73023 5.85900 17.10828 
    3.80835 6.03477 16.52238 
    3.84741 5.72229 15.81930 
    3.71070 5.56605 14.29596 
    3.80835 5.39028 12.96792 
    4.14036 5.05827 11.95236 
    4.23801 5.11686 10.85868 
    4.55049 5.31216 9.80406 
    4.82391 5.60511 9.02286 
    5.13639 5.89806 8.28072 
    5.91759 6.23007 7.18704 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX07')
s.location = CONST.UR
s.note='13-4-21-check all'
s.furcation_pos_1 = 8.6 
s.furcation_pos_2 = 7.3 
s.canal_type = 0
ps1 = '''
    4.68720 4.88250 18.20196 
    4.70673 4.84344 17.61606 
    4.47237 4.78485 16.79580 
    4.17942 4.86297 15.97554 
    3.96459 4.90203 15.07716 
    3.63258 5.13639 13.82724 
    3.69117 5.40981 12.18672 
    4.04271 5.76135 10.50714 
    4.62861 6.03477 9.25722 
    5.05827 6.21054 8.16354 
'''
ps2 = '''
    5.64417 3.65211 16.65909 
    5.42934 3.98412 15.78024 
    5.39028 3.96459 14.95998 
    5.56605 3.71070 13.82724 
    5.99571 3.43728 12.42108 
    6.07383 3.51540 11.21022 
    6.23007 3.67164 10.19466 
    6.42537 3.96459 9.37440 
    6.26913 4.70673 8.74944 
    6.50349 5.37075 7.92918 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX08')
s.location = CONST.UL
s.note='13-4-21-check all'
s.furcation_pos_1 = 7.8 
s.furcation_pos_2 = 5.8 
s.canal_type = 0
ps1 = '''
    2.85138 6.69879 17.65512 
    2.83185 6.99174 17.18640 
    3.02715 7.44093 16.36614 
    2.96856 7.73388 15.46776 
    2.59749 8.00730 14.45220 
    2.81232 8.04636 13.39758 
    3.00762 7.94871 11.79612 
    3.41775 7.51905 10.38996 
    3.71070 7.20657 9.25722 
    3.94506 6.91362 8.51508 
'''
ps2 = '''
    3.88647 7.16751 16.11225 
    4.35519 7.30422 15.50682 
    4.58955 7.40187 15.13575 
    4.76532 7.59717 14.35455 
    4.80438 7.71435 13.88583 
    4.90203 7.83153 13.14369 
    5.13639 7.87059 12.18672 
    5.09733 7.69482 10.85868 
    5.42934 7.28469 9.96030 
    5.76135 6.85503 9.21816 
    5.66370 6.19101 8.47602 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX09')
s.location = CONST.UL
s.note='13-4-21-check all'
s.furcation_pos_1 = 7.4 
s.furcation_pos_2 = 6.8 
s.canal_type = 0
ps1 = '''
    5.44887 7.08939 17.26452 
    5.62464 7.36281 16.83486 
    5.54652 7.59717 16.28802 
    5.56605 7.73388 15.70212 
    5.64417 7.85106 14.72562 
    5.48793 7.94871 13.47570 
    5.25357 7.94871 12.65544 
    4.92156 7.83153 11.83518 
    4.92156 7.65576 11.05398 
    5.01921 7.38234 10.11654 
    4.86297 6.93315 8.94474 
'''
ps2 = '''
    7.03080 7.42140 17.06922 
    6.99174 7.53858 16.71768 
    6.83550 7.61670 16.30755 
    6.77691 7.67529 15.85836 
    6.48396 7.79247 15.27246 
    6.05430 7.87059 14.41314 
    5.97618 7.98777 13.39758 
    6.21054 8.04636 12.38202 
    6.32772 7.98777 11.40552 
    6.11289 7.79247 10.50714 
    6.09336 7.51905 9.56970 
    6.30819 7.28469 9.06192 
    6.48396 7.14798 8.74944 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX10')
s.location = CONST.UR
s.note='13-4-21-check all'
s.furcation_pos_1 = 6.8 
s.furcation_pos_2 = 4.9 
s.canal_type = 0
ps1 = '''
    2.87091 3.43728 17.59653 
    2.87091 3.37869 17.18640 
    2.92950 3.24198 16.75674 
    2.94903 3.22245 16.13178 
    2.96856 3.24198 15.35058 
    3.02715 3.30057 14.64750 
    3.35916 3.35916 13.43664 
    3.53493 3.51540 12.38202 
    3.69117 3.73023 11.28834 
    4.06224 4.06224 9.99936 
    4.33566 4.27707 9.14004 
'''
ps2 = '''
    5.13639 3.18339 16.15131 
    4.98015 2.98809 15.62400 
    4.84344 2.87091 14.68656 
    4.76532 2.92950 13.71006 
    4.82391 2.98809 12.96792 
    5.05827 3.12480 12.18672 
    5.19498 3.26151 11.60082 
    5.37075 3.65211 10.66338 
    5.76135 4.02318 9.96030 
    6.36678 4.39425 9.25722 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX11')
s.location = CONST.UL
s.note='13-4-28-check all'
s.furcation_pos_1 = 8.2 
s.furcation_pos_2 = 7.7 
s.canal_type = 0
ps1 = '''
    2.18736 6.32772 17.86995 
    2.44125 6.42537 16.99110 
    2.79279 6.52302 16.01460 
    2.98809 6.58161 14.72562 
    3.06621 6.60114 13.28040 
    3.08574 6.48396 12.03048 
    3.59352 6.15195 10.66338 
    4.04271 5.83947 9.88218 
    4.31613 5.48793 9.10098 
'''
ps2 = '''
    3.35916 6.52302 17.92854 
    3.20292 6.50349 17.42076 
    3.02715 6.64020 16.44426 
    3.18339 6.67926 15.46776 
    3.74976 6.83550 14.25690 
    4.53096 7.01127 13.59288 
    5.17545 7.14798 12.69450 
    5.52699 7.06986 11.87424 
    5.78088 6.69879 10.93680 
    5.97618 6.13242 9.96030 
    6.23007 5.76135 9.49158 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX12')
s.location = CONST.UR
s.note='13-4-28-check all'
s.furcation_pos_1 = 9.4 
s.furcation_pos_2 = 9.2 
s.canal_type = 0
ps1 = '''
    5.27310 4.27707 18.41679 
    5.13639 4.12083 18.00666 
    5.01921 3.84741 17.65512 
    4.66767 3.53493 16.83486 
    4.47237 3.55446 16.05366 
    4.41378 3.59352 14.99904 
    4.25754 3.74976 13.98348 
    4.10130 3.88647 13.59288 
    4.02318 4.00365 13.00698 
    3.84741 4.27707 12.18672 
    3.73023 4.51143 11.36646 
    3.96459 4.58955 10.42902 
    4.41378 4.62861 9.72594 
    4.98015 4.64814 8.94474 
    5.39028 4.76532 8.28072 
    5.52699 4.94109 7.61670 
'''
ps2 = '''
    5.25357 4.25754 18.39726 
    5.11686 4.10130 17.96760 
    4.99968 3.74976 17.57700 
    4.82391 3.35916 16.87392 
    4.99968 2.98809 16.01460 
    5.09733 2.89044 14.99904 
    4.96062 3.08574 14.25690 
    4.84344 3.24198 13.55382 
    5.07780 3.28104 12.10860 
    5.19498 3.37869 11.09304 
    5.21451 4.06224 9.60876 
    5.33169 4.66767 8.51508 
    5.37075 4.76532 8.24166 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX13')
s.location = CONST.UL
s.note='13-4-28-check all'
s.furcation_pos_1 = 9.4 
s.furcation_pos_2 = 9.7 
s.canal_type = 0
ps1 = '''
    3.96459 8.43696 18.31914 
    4.02318 8.61273 17.77230 
    4.27707 8.74944 17.26452 
    4.49190 8.71038 16.71768 
    4.49190 8.86662 15.97554 
    4.45284 9.04239 15.11622 
    4.51143 9.21816 14.02254 
    4.60908 9.39393 12.65544 
    4.58955 9.43299 11.71800 
    4.58955 9.27675 10.38996 
    4.66767 8.98380 9.37440 
    4.74579 8.45649 8.24166 
    4.68720 8.14401 7.46046 
'''
ps2 = '''
    3.96459 8.43696 18.29961 
    4.21848 8.74944 17.34264 
    4.57002 8.67132 16.75674 
    5.15592 8.69085 16.17084 
    5.54652 8.74944 15.54588 
    5.80041 8.76897 15.11622 
    5.89806 8.90568 14.25690 
    5.76135 9.06192 13.31946 
    5.70276 9.12051 12.26484 
    6.01524 9.00333 11.32740 
    6.23007 8.78850 10.35090 
    6.23007 8.31978 9.21816 
    5.72229 8.18307 8.55414 
    5.39028 7.77294 7.73388 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX14')
s.location = CONST.UL
s.note='13-4-28-check all'
s.furcation_pos_1 = 6.7 
s.furcation_pos_2 = 6.3 
s.canal_type = 0
ps1 = '''
    9.56970 3.84741 18.45585 
    9.49158 3.94506 18.08478 
    9.53064 4.25754 17.49888 
    9.62829 4.45284 16.71768 
    9.62829 4.45284 15.78024 
    9.66735 4.57002 14.84280 
    9.72594 4.74579 13.78818 
    9.60876 4.92156 13.04604 
    8.82756 5.25357 11.75706 
    7.61670 5.54652 10.38996 
'''
ps2 = '''
    7.85106 2.89044 18.51444 
    7.85106 3.02715 18.22149 
    7.81200 3.20292 17.83089 
    7.79247 3.30057 17.22546 
    7.81200 3.35916 16.28802 
    7.92918 3.49587 15.42870 
    7.81200 3.55446 14.56938 
    7.67529 3.57399 13.67100 
    7.57764 3.74976 12.85074 
    7.57764 4.15989 12.22578 
    7.92918 4.84344 11.48364 
    7.89012 5.66370 10.58526 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX16')
s.location = CONST.UR
s.note='13-4-28-check all'
s.furcation_pos_1 = 8.2 
s.furcation_pos_2 = 7.6 
s.canal_type = 0
ps1 = '''
    4.70673 5.19498 17.98713 
    4.58955 5.15592 17.55747 
    4.51143 4.94109 17.12781 
    4.47237 4.62861 16.65909 
    4.29660 4.47237 15.95601 
    4.06224 4.49190 15.01857 
    3.98412 4.55049 13.92489 
    3.96459 4.80438 12.63591 
    4.17942 5.01921 11.34693 
    4.41378 5.17545 10.33137 
    4.74579 5.48793 9.27675 
    4.82391 5.83947 8.61273 
'''
ps2 = '''
    6.21054 3.78882 16.63956 
    5.87853 3.67164 15.97554 
    5.58558 3.55446 15.25293 
    5.52699 3.45681 14.51079 
    5.39028 3.47634 13.45617 
    5.48793 3.45681 12.20625 
    5.66370 3.47634 11.38599 
    5.80041 3.47634 10.95633 
    5.81994 3.53493 10.54620 
    5.87853 3.65211 10.17513 
    5.95665 3.96459 9.66735 
    6.15195 4.25754 9.23769 
    6.46443 4.80438 8.33931 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX17')
s.location = CONST.UL
s.note='13-4-28-check all'
s.furcation_pos_1 = 7.5 
s.furcation_pos_2 = 6.9 
s.canal_type = 0
ps1 = '''
    5.78088 7.85106 17.40123 
    5.70276 8.45649 16.56144 
    5.60511 8.96427 15.31152 
    5.50746 9.17910 13.94442 
    5.48793 9.06192 12.42108 
    5.58558 8.67132 11.01492 
    5.68323 7.89012 9.68688 
    5.66370 7.55811 8.78850 
'''
ps2 = '''
    5.76135 7.83153 17.38170 
    5.85900 8.16354 16.87392 
    6.19101 8.57367 15.78024 
    6.28866 8.74944 14.88186 
    6.38631 8.78850 13.90536 
    6.77691 8.65179 12.92886 
    6.95268 8.51508 11.87424 
    7.03080 8.18307 10.81962 
    6.71832 7.69482 9.80406 
    6.50349 7.40187 9.29628 
    6.30819 7.36281 8.63226 
    6.38631 7.61670 8.12448 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX18')
s.location = CONST.UR
s.note='13-4-28-check all'
s.furcation_pos_1 = 8.6 
s.furcation_pos_2 = 7.3 
s.canal_type = 0
ps1 = '''
    4.78485 4.84344 17.77230 
    4.72626 4.84344 17.18640 
    4.58955 4.82391 16.36614 
    4.29660 4.88250 15.50682 
    3.69117 5.17545 14.02254 
    3.49587 5.44887 12.53826 
    3.74976 5.64417 11.40552 
    4.39425 5.95665 10.19466 
    4.84344 6.07383 9.53064 
'''
ps2 = '''
    5.60511 4.10130 17.08875 
    5.44887 4.21848 16.32708 
    5.07780 4.31613 15.81930 
    4.62861 4.49190 14.95998 
    4.55049 4.35519 13.39758 
    5.19498 3.74976 11.67894 
    5.50746 3.86694 10.70244 
    5.48793 4.94109 9.41346 
    5.56605 5.44887 8.78850 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX19')
s.location = CONST.UL
s.note='13-4-28-check all'
s.furcation_pos_1 = 9.6 
s.furcation_pos_2 = 9.9 
s.canal_type = 0
ps1 = '''
    4.55049 8.49555 18.35820 
    4.66767 8.65179 17.73324 
    4.76532 8.74944 16.99110 
    4.86297 8.92521 16.20990 
    4.84344 9.37440 15.35058 
    4.99968 9.64782 14.33502 
    5.17545 9.96030 13.20228 
    5.15592 10.19466 12.34296 
    5.09733 10.37043 10.78056 
    5.19498 10.03842 9.92124 
    5.29263 9.60876 9.21816 
    5.37075 9.10098 8.28072 
    5.37075 9.00333 7.81200 
'''
ps2 = '''
    4.55049 8.49555 18.33867 
    4.62861 8.65179 17.85042 
    4.82391 8.74944 16.79580 
    5.42934 8.57367 15.78024 
    5.93712 8.30025 15.23340 
    6.11289 8.43696 14.76468 
    6.23007 8.53461 14.17878 
    6.19101 8.90568 13.47570 
    6.48396 8.94474 12.77262 
    7.12845 8.74944 11.71800 
    7.46046 8.51508 10.66338 
    7.47999 8.28072 9.76500 
    7.16751 7.98777 8.94474 
    6.73785 7.77294 8.16354 
    6.46443 7.61670 7.69482 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX20')
s.location = CONST.UR
s.note='13-4-28-check all'
s.furcation_pos_1 = 8.0 
s.furcation_pos_2 = 6.2 
s.canal_type = 0
ps1 = '''
    4.57002 5.15592 18.12384 
    4.21848 4.88250 17.53794 
    4.02318 4.76532 17.06922 
    3.84741 4.80438 16.28802 
    3.69117 4.90203 15.35058 
    3.55446 5.07780 14.10066 
    3.86694 5.37075 12.06954 
    4.68720 5.66370 10.11654 
    4.99968 5.80041 9.45252 
'''
ps2 = '''
    5.81994 3.26151 17.10828 
    5.76135 3.22245 16.71768 
    5.48793 3.30057 16.40520 
    5.27310 3.32010 15.54588 
    5.27310 3.37869 14.76468 
    5.44887 3.32010 13.82724 
    5.35122 3.55446 13.00698 
    5.48793 3.84741 11.99142 
    5.70276 4.49190 10.66338 
    6.21054 4.99968 9.29628 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX21')
s.location = CONST.UR
s.note='13-4-28-check all'
s.furcation_pos_1 = 7.6 
s.furcation_pos_2 = 7.3 
s.canal_type = 0
ps1 = '''
    2.69514 5.17545 17.26452 
    3.02715 5.03874 16.44426 
    3.00762 5.15592 15.78024 
    2.73420 5.35122 14.53032 
    2.53890 5.56605 13.00698 
    2.73420 5.74182 11.63988 
    3.20292 5.81994 10.42902 
    3.80835 5.93712 9.17910 
    4.00365 6.05430 8.74944 
'''
ps2 = '''
    3.74976 4.47237 16.56144 
    3.67164 4.60908 16.13178 
    3.63258 4.68720 15.70212 
    3.92553 4.51143 15.03810 
    4.21848 4.27707 14.29596 
    4.29660 4.14036 13.12416 
    4.27707 4.17942 12.14766 
    4.53096 4.04271 11.24928 
    4.92156 4.04271 10.23372 
    5.25357 4.33566 9.60876 
    5.27310 5.09733 8.82756 
    5.21451 5.46840 8.47602 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX23')
s.location = CONST.UL
s.note='13-4-28-check all'
s.furcation_pos_1 = 9.6 
s.furcation_pos_2 = 8.1 
s.canal_type = 0
ps1 = '''
    4.62861 10.31184 17.81136 
    4.62861 10.46808 17.59653 
    4.64814 10.72197 17.36217 
    4.80438 10.76103 17.01063 
    5.07780 10.66338 16.38567 
    5.11686 10.62432 15.40917 
    4.94109 10.70244 14.27643 
    4.70673 10.72197 12.79215 
    4.58955 10.60479 11.42505 
    4.58955 10.25325 9.94077 
    4.74579 9.76500 8.78850 
    4.76532 9.56970 8.28072 
    4.72626 9.23769 7.61670 
'''
ps2 = '''
    6.69879 9.90171 16.79580 
    6.67926 10.01889 16.58097 
    6.58161 10.17513 16.17084 
    6.50349 10.23372 15.87789 
    6.30819 10.23372 15.25293 
    6.21054 10.19466 14.66703 
    6.52302 9.94077 13.10463 
    6.91362 9.66735 12.08907 
    7.01127 9.39393 10.80009 
    7.03080 9.04239 9.62829 
    6.89409 8.78850 8.96427 
    6.56208 8.59320 8.37837 
    6.34725 8.41743 7.87059 
    6.34725 8.16354 7.44093 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX24')
s.location = CONST.UL
s.note='13-4-28-check all'
s.furcation_pos_1 = 8.3 
s.furcation_pos_2 = 7.8 
s.canal_type = 0
ps1 = '''
    4.31613 7.87059 17.65512 
    4.33566 8.18307 16.83486 
    4.35519 8.59320 15.78024 
    4.41378 8.96427 14.10066 
    4.51143 9.06192 12.61638 
    4.55049 9.02286 10.97586 
    4.58955 8.84709 9.41346 
    4.68720 8.65179 8.63226 
    4.82391 8.24166 7.81200 
    4.64814 7.69482 6.77691 
'''
ps2 = '''
    6.21054 6.77691 16.38567 
    6.52302 7.14798 15.66306 
    6.83550 7.47999 14.80374 
    6.81597 7.79247 13.63194 
    6.69879 7.98777 12.42108 
    6.71832 8.02683 10.93680 
    6.81597 7.85106 9.64782 
    6.85503 7.49952 8.67132 
    6.62067 7.05033 7.61670 
    6.38631 6.48396 6.56208 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX26')
s.location = CONST.UL
s.note='13-4-28-check all'
s.furcation_pos_1 = 8.0 
s.furcation_pos_2 = 8.2 
s.canal_type = 0
ps1 = '''
    2.36313 7.14798 17.83089 
    2.36313 7.34328 17.18640 
    2.42172 7.51905 16.56144 
    2.59749 7.77294 15.85836 
    3.04668 7.85106 14.72562 
    3.20292 7.92918 13.67100 
    3.24198 7.90965 12.14766 
    3.41775 7.75341 10.89774 
    3.57399 7.42140 9.72594 
    3.73023 7.22610 9.17910 
    4.10130 6.93315 8.47602 
'''
ps2 = '''
    4.41378 7.42140 17.71371 
    4.39425 7.59717 16.95204 
    4.43331 7.75341 16.09272 
    4.51143 7.83153 15.31152 
    4.21848 7.87059 14.72562 
    4.04271 7.90965 13.47570 
    4.31613 7.90965 12.38202 
    4.78485 7.73388 11.13210 
    5.27310 7.40187 10.46808 
    5.58558 6.75738 9.72594 
    5.66370 6.44490 8.90568 
    5.62464 6.34725 8.49555 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX27')
s.location = CONST.UR
s.note='13-4-28-check all'
s.furcation_pos_1 = 6.0 
s.furcation_pos_2 = 5.9 
s.canal_type = 0
ps1 = '''
    1.38663 5.44887 17.71371 
    1.19133 5.33169 17.30358 
    1.15227 5.21451 16.75674 
    1.19133 5.01921 15.89742 
    1.46475 4.82391 14.95998 
    1.83582 4.57002 14.21784 
    2.01159 4.55049 13.43664 
    2.34360 4.62861 12.49920 
    2.49984 4.55049 11.67894 
    3.28104 4.68720 10.58526 
    3.78882 4.82391 10.13607 
    4.17942 4.94109 9.53064 
'''
ps2 = '''
    3.61305 3.76929 16.62003 
    3.71070 3.67164 16.17084 
    3.82788 3.51540 15.54588 
    4.04271 3.37869 14.84280 
    4.27707 3.28104 13.94442 
    4.72626 3.20292 12.88980 
    4.98015 3.47634 11.79612 
    5.44887 3.94506 10.85868 
    5.83947 4.49190 10.07748 
    5.97618 4.60908 9.78453 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX28')
s.location = CONST.UR
s.note='13-4-28-check all'
s.furcation_pos_1 = 8.6 
s.furcation_pos_2 = 6.8 
s.canal_type = 0
ps1 = '''
    2.55843 2.71467 17.83089 
    2.40219 2.67561 17.34264 
    2.30454 2.57796 16.56144 
    2.30454 2.51937 15.58494 
    2.30454 2.63655 14.60844 
    2.38266 2.87091 13.31946 
    2.51937 3.20292 11.67894 
    2.85138 3.55446 10.35090 
    3.51540 3.98412 9.14004 
    4.14036 4.39425 8.00730 
'''
ps2 = '''
    3.78882 2.48031 16.69815 
    3.63258 2.49984 16.01460 
    3.61305 2.53890 15.66306 
    3.76929 2.57796 15.23340 
    4.06224 2.61702 14.49126 
    4.23801 2.69514 13.67100 
    4.39425 2.89044 12.34296 
    4.90203 2.98809 11.32740 
    5.35122 3.16386 10.27278 
    5.76135 3.45681 9.37440 
    5.87853 3.92553 8.71038 
    5.83947 4.17942 8.30025 
    5.83947 4.41378 7.94871 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX29')
s.location = CONST.UR
s.note='13-4-28-check all'
s.furcation_pos_1 = 8.8 
s.furcation_pos_2 = 9.0 
s.canal_type = 0
ps1 = '''
    4.78485 5.76135 17.24499 
    4.60908 5.37075 16.67862 
    4.04271 4.68720 15.70212 
    3.78882 4.23801 14.33502 
    3.55446 4.10130 13.20228 
    3.24198 4.17942 12.06954 
    3.14433 4.31613 10.97586 
    3.39822 4.49190 9.60876 
    3.80835 4.82391 8.08542 
    4.00365 5.11686 7.34328 
'''
ps2 = '''
    4.76532 5.74182 17.22546 
    4.80438 5.44887 16.75674 
    4.96062 5.01921 16.32708 
    4.92156 4.37472 15.58494 
    4.80438 3.92553 14.64750 
    4.94109 3.59352 13.71006 
    5.27310 3.28104 12.81168 
    5.56605 3.06621 11.83518 
    5.58558 3.08574 10.85868 
    5.60511 3.26151 9.88218 
    5.95665 3.78882 8.67132 
    6.07383 4.23801 7.92918 
    6.32772 4.57002 7.36281 
    6.48396 4.66767 7.14798 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX30')
s.location = CONST.UR
s.note='13-4-28-check all'
s.furcation_pos_1 = 7.0 
s.furcation_pos_2 = 6.6 
s.canal_type = 0
ps1 = '''
    4.25754 5.66370 17.61606 
    4.04271 5.48793 17.06922 
    3.98412 4.99968 16.20990 
    3.78882 4.68720 15.27246 
    3.73023 4.49190 14.10066 
    3.53493 4.49190 12.65544 
    3.55446 4.53096 11.60082 
    3.69117 4.78485 10.54620 
    3.84741 5.09733 9.25722 
'''
ps2 = '''
    4.99968 5.23404 17.44029 
    4.78485 5.03874 16.83486 
    4.55049 4.58955 15.74118 
    4.76532 4.21848 14.60844 
    5.01921 3.96459 13.63194 
    5.05827 3.84741 12.42108 
    5.05827 3.92553 11.17116 
    5.42934 4.17942 9.96030 
    5.62464 4.35519 9.47205 
    5.81994 4.45284 9.06192 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX32')
s.location = CONST.UR
s.note='13-4-28-check all'
s.furcation_pos_1 = 8.0 
s.furcation_pos_2 = 6.4 
s.canal_type = 0
ps1 = '''
    3.04668 6.91362 17.55747 
    2.90997 6.89409 17.20593 
    2.65608 7.05033 16.69815 
    2.46078 7.24563 16.09272 
    2.30454 7.42140 15.64353 
    2.20689 7.53858 14.99904 
    2.30454 7.63623 13.63194 
    2.59749 7.61670 12.42108 
    2.94903 7.75341 11.32740 
    3.22245 7.77294 10.54620 
    3.69117 7.75341 9.56970 
    3.71070 7.87059 8.63226 
'''
ps2 = '''
    3.80835 5.78088 16.75674 
    3.61305 5.81994 16.44426 
    3.49587 5.95665 16.03413 
    3.55446 5.93712 15.56541 
    3.71070 5.76135 14.80374 
    3.74976 5.72229 14.02254 
    3.86694 5.54652 13.16322 
    3.94506 5.56605 12.14766 
    4.25754 5.60511 11.13210 
    4.57002 5.83947 10.31184 
    4.72626 6.56208 9.25722 
    5.11686 6.77691 8.47602 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX33')
s.location = CONST.UL
s.note='13-4-28-check all'
s.furcation_pos_1 = 8.4 
s.furcation_pos_2 = 9.5 
s.canal_type = 0
ps1 = '''
    5.72229 9.27675 17.79183 
    5.85900 9.39393 17.59653 
    6.01524 9.55017 17.08875 
    6.11289 9.66735 16.05366 
    6.19101 9.82359 15.11622 
    6.15195 9.97983 13.78818 
    6.03477 10.11654 12.46014 
    5.72229 10.13607 11.01492 
    5.58558 9.97983 10.11654 
    5.66370 9.60876 9.14004 
    5.56605 9.37440 8.57367 
    5.35122 9.14004 7.61670 
'''
ps2 = '''
    5.72229 9.27675 17.77230 
    5.87853 9.39393 17.53794 
    6.03477 9.45252 17.32311 
    6.13242 9.53064 16.77627 
    6.23007 9.64782 15.81930 
    6.28866 9.80406 14.41314 
    6.44490 9.74547 13.55382 
    6.50349 9.68688 12.61638 
    6.60114 9.56970 11.79612 
    6.91362 9.14004 10.66338 
    6.99174 8.86662 9.94077 
    6.99174 8.49555 9.27675 
    6.85503 7.98777 8.65179 
    6.77691 7.85106 8.22213 
    6.69879 7.75341 7.92918 
    6.64020 7.51905 7.59717 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX35')
s.location = CONST.UL
s.note='13-4-28-check all'
s.furcation_pos_1 = 6.7 
s.furcation_pos_2 = 5.8 
s.canal_type = 0
ps1 = '''
    4.57002 9.96030 16.63956 
    4.76532 9.99936 16.42473 
    5.25357 10.25325 15.99507 
    5.78088 10.52667 15.15528 
    5.91759 10.56573 14.17878 
    5.93712 10.50714 13.00698 
    5.68323 10.52667 11.91330 
    5.60511 10.31184 11.05398 
    5.50746 9.96030 10.15560 
    5.25357 9.68688 9.17910 
    5.15592 9.53064 8.69085 
'''
ps2 = '''
    7.16751 9.04239 15.78024 
    7.30422 9.19863 15.44823 
    7.34328 9.43299 14.99904 
    7.28469 9.53064 14.45220 
    7.22610 9.55017 13.78818 
    7.26516 9.49158 13.16322 
    7.42140 9.17910 12.34296 
    7.49952 8.94474 11.56176 
    7.47999 8.84709 11.17116 
    7.03080 8.55414 10.19466 
    6.54255 8.22213 9.49158 
    6.21054 7.90965 8.78850 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX36')
s.location = CONST.UL
s.note='13-4-28-check all'
s.furcation_pos_1 = 8.5 
s.furcation_pos_2 = 7.6 
s.canal_type = 0
ps1 = '''
    6.28866 9.60876 17.08875 
    6.28866 9.92124 16.67862 
    6.26913 10.19466 16.17084 
    6.15195 10.50714 15.66306 
    5.97618 10.78056 14.92092 
    5.99571 10.93680 13.98348 
    6.07383 10.91727 12.92886 
    6.24960 10.62432 11.60082 
    6.26913 10.17513 10.27278 
    6.15195 9.45252 8.86662 
    5.87853 8.88615 7.61670 
'''
ps2 = '''
    7.75341 8.51508 16.67862 
    7.81200 8.63226 16.24896 
    7.92918 8.88615 15.46776 
    8.04636 8.90568 14.95998 
    8.14401 8.92521 14.51079 
    8.08542 9.06192 13.80771 
    8.08542 9.15957 12.92886 
    7.81200 9.37440 12.08907 
    7.61670 9.39393 11.09304 
    7.53858 9.33534 10.46808 
    7.24563 9.23769 9.66735 
    6.93315 9.12051 9.08145 
    6.85503 8.94474 8.65179 
    6.77691 8.55414 8.10495 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX37')
s.location = CONST.UL
s.note='13-4-28-check all'
s.furcation_pos_1 = 7.7 
s.furcation_pos_2 = 7.3 
s.canal_type = 0
ps1 = '''
    5.56605 9.19863 16.09272 
    5.46840 9.33534 15.97554 
    5.27310 9.62829 15.68259 
    5.25357 9.76500 15.21387 
    5.37075 9.99936 14.49126 
    5.37075 10.21419 13.82724 
    5.23404 10.52667 12.85074 
    5.05827 10.74150 11.75706 
    4.96062 10.74150 10.50714 
    5.05827 10.52667 9.37440 
    4.90203 10.19466 7.96824 
    4.72626 10.11654 7.34328 
'''
ps2 = '''
    6.07383 8.98380 16.05366 
    6.13242 9.08145 15.79977 
    6.23007 9.25722 15.21387 
    6.28866 9.47205 14.54985 
    6.40584 9.58923 13.94442 
    6.62067 9.72594 13.20228 
    6.81597 9.80406 12.38202 
    7.01127 9.92124 11.24928 
    7.06986 9.92124 10.03842 
    6.97221 9.64782 8.94474 
    6.91362 9.33534 8.22213 
    6.67926 9.12051 7.71435 
    6.56208 8.88615 7.28469 
    6.46443 8.41743 6.62067 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX38')
s.location = CONST.UL
s.note=''
s.furcation_pos_1 = 8.1 
s.furcation_pos_2 = 6.5 
s.canal_type = 0
ps1 = '''
    2.85138 7.67529 17.55747 
    3.02715 7.87059 17.18640 
    3.06621 8.22213 16.83486 
    3.20292 8.69085 16.28802 
    3.39822 9.02286 15.66306 
    3.61305 9.15957 14.84280 
    3.82788 9.17910 13.90536 
    3.80835 9.15957 12.96792 
    3.80835 9.04239 12.10860 
    4.10130 8.41743 10.78056 
    4.45284 7.96824 9.88218 
    4.55049 7.73388 9.17910 
'''
ps2 = '''
    4.78485 7.69482 16.65909 
    4.98015 7.85106 16.38567 
    5.23404 8.30025 15.89742 
    5.37075 8.57367 15.42870 
    5.37075 8.72991 14.95998 
    5.56605 8.82756 14.10066 
    5.78088 8.84709 13.43664 
    6.09336 8.80803 12.73356 
    6.19101 8.76897 12.38202 
    5.80041 7.77294 10.11654 
    5.68323 7.40187 9.56970 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX40')
s.location = CONST.UL
s.note=''
s.furcation_pos_1 = 9.8 
s.furcation_pos_2 = 8.7 
s.canal_type = 0
ps1 = '''
    4.17942 8.69085 18.28008 
    4.23801 8.69085 18.00666 
    4.35519 8.72991 17.69418 
    4.55049 8.76897 17.06922 
    4.64814 8.84709 16.44426 
    4.62861 8.82756 15.46776 
    4.66767 8.78850 14.49126 
    4.70673 8.80803 13.67100 
    4.78485 8.80803 12.61638 
    5.09733 8.65179 11.17116 
    5.21451 8.43696 10.03842 
    5.29263 7.69482 8.20260 
    5.15592 7.40187 7.46046 
'''
ps2 = '''
    6.50349 7.73388 17.34264 
    6.56208 7.79247 17.03016 
    6.65973 7.90965 16.63956 
    6.81597 7.96824 16.09272 
    6.91362 8.00730 15.35058 
    7.01127 7.90965 14.45220 
    7.08939 7.85106 13.78818 
    7.16751 7.75341 13.08510 
    7.14798 7.75341 12.30390 
    7.10892 7.75341 11.36646 
    6.95268 7.69482 10.31184 
    6.21054 7.51905 8.71038 
    6.01524 7.30422 8.08542 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX43')
s.location = CONST.UR
s.note=''
s.furcation_pos_1 = 7.2 
s.furcation_pos_2 = 6.3 
s.canal_type = 0
ps1 = '''
    5.37075 5.87853 18.33867 
    5.27310 5.56605 17.73324 
    5.05827 5.35122 16.99110 
    4.82391 4.98015 15.85836 
    4.74579 4.68720 14.56938 
    4.51143 4.94109 12.92886 
    4.62861 5.09733 12.03048 
    4.78485 5.29263 11.28834 
    5.01921 5.44887 10.54620 
    5.35122 5.58558 9.99936 
'''
ps2 = '''
    7.03080 4.25754 16.95204 
    6.81597 3.90600 16.48332 
    6.48396 3.74976 15.89742 
    6.11289 3.74976 15.15528 
    5.78088 3.78882 14.13972 
    5.97618 3.57399 13.43664 
    6.07383 3.57399 12.46014 
    6.03477 3.78882 11.79612 
    6.15195 4.21848 10.74150 
    6.21054 4.41378 10.23372 
    6.44490 4.60908 9.80406 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX45')
s.location = CONST.UL
s.note=''
s.furcation_pos_1 = 6.5 
s.furcation_pos_2 = 6.5 
s.canal_type = 0
ps1 = '''
    3.92553 5.27310 17.03016 
    4.06224 5.56605 16.48332 
    4.04271 5.74182 15.93648 
    4.12083 5.89806 15.03810 
    4.25754 6.07383 13.86630 
    4.10130 6.28866 12.92886 
    3.98412 6.38631 12.06954 
    4.14036 6.50349 10.81962 
    4.37472 6.40584 9.53064 
    4.58955 6.05430 8.24166 
    4.60908 5.78088 7.42140 
    4.49190 5.62464 6.87456 
'''
ps2 = '''
    5.56605 5.60511 17.30358 
    5.46840 5.70276 16.83486 
    5.50746 5.87853 16.32708 
    5.60511 5.93712 15.81930 
    5.68323 5.93712 15.15528 
    5.40981 6.03477 14.29596 
    5.21451 6.15195 13.63194 
    5.35122 6.30819 12.69450 
    5.60511 6.34725 11.95236 
    5.78088 6.40584 11.05398 
    5.91759 6.40584 9.92124 
    6.24960 6.03477 8.59320 
    6.44490 5.56605 7.81200 
    6.48396 5.19498 6.99174 
    6.56208 5.13639 6.40584 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX46')
s.location = CONST.UR
s.note=''
s.furcation_pos_1 = 7.5 
s.furcation_pos_2 = 6.4 
s.canal_type = 0
ps1 = '''
    1.32804 4.60908 16.52238 
    1.40616 4.62861 16.17084 
    1.52334 4.62861 15.70212 
    1.64052 4.58955 15.07716 
    1.75770 4.58955 14.25690 
    2.03112 4.49190 13.16322 
    2.20689 4.62861 12.18672 
    2.36313 4.88250 11.32740 
    2.98809 4.99968 10.07748 
    3.73023 5.09733 8.94474 
    3.98412 5.17545 8.47602 
'''
ps2 = '''
    3.06621 3.18339 16.63956 
    3.02715 3.26151 16.42473 
    2.98809 3.35916 16.09272 
    2.94903 3.39822 15.81930 
    2.87091 3.49587 15.46776 
    2.87091 3.51540 15.19434 
    2.89044 3.51540 14.76468 
    2.94903 3.43728 14.02254 
    2.98809 3.43728 13.28040 
    3.08574 3.47634 12.53826 
    3.37869 3.35916 11.87424 
    3.76929 3.41775 11.01492 
    4.08177 3.76929 10.07748 
    4.43331 4.06224 9.17910 
    4.78485 4.15989 8.71038 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MX50')
s.location = CONST.UR
s.note=''
s.furcation_pos_1 = 8.0 
s.furcation_pos_2 = 5.8 
s.canal_type = 0
ps1 = '''
    4.27707 4.80438 17.69418 
    4.17942 4.76532 17.30358 
    4.10130 4.68720 16.60050 
    4.02318 4.57002 15.81930 
    3.88647 4.55049 14.95998 
    3.71070 4.64814 13.59288 
    3.59352 4.88250 12.81168 
    3.76929 5.19498 11.56176 
    4.14036 5.50746 10.42902 
    4.25754 5.68323 9.10098 
'''
ps2 = '''
    5.93712 3.39822 15.70212 
    5.83947 3.43728 15.42870 
    5.64417 3.47634 15.03810 
    5.42934 3.45681 14.56938 
    5.23404 3.51540 13.98348 
    5.35122 3.47634 13.35852 
    5.46840 3.39822 12.81168 
    5.64417 3.32010 12.10860 
    5.76135 3.43728 11.36646 
    6.03477 3.76929 10.46808 
    6.19101 4.27707 9.92124 
    6.46443 4.99968 9.02286 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

        