'''
Created on 2014. 4. 9.

@author: jongki

total number of teeth : 16
Data from KUM-10-11-08

'''

# -*- coding: cp949 -*-


from __future__ import division


from constant import CONST
from class_specimen import Specimen, Canal
import os

specimens = []
directory_name = os.getenv('TOOTH_DATA') + '/v3d_mxk/'
bounding_box_range = [(-10, 20), (-10, 20), (-2, 28)]
canal_suffix = '-canal-zoff.v3d'
body_suffix = '-solid-body-zoff.v3d'

#===============================================================================
# --based on v-works image
# RIGHT                             Apical 
#      .....                          ^
#     . DB  .                         |
#      .....         ...              |
#                  .     .            |  
#                  .  P  .            | 
#      ....          ...              |
#    .  MB  .                         | 
#      ....                         Coronal
# 
#===============================================================================


s = Specimen('MXK02')
s.tooth_position = CONST.UL
s.note=''
s.canal_type = 0
ps1 = '''
    3.21483 11.04501 2.67372 
    3.11934 10.82220 3.31032 
    3.24666 10.47207 4.10607 
    3.37398 10.05828 5.02914 
    3.53313 9.64449 6.17502 
    3.78777 9.26253 7.54371 
    3.81960 8.97606 9.03972 
    4.07424 8.84874 10.59939 
    4.26522 8.94423 11.42697 
    4.83816 8.88057 12.31821 
    5.44293 8.88057 13.43226 
'''
ps2 = '''
    3.21483 11.04501 2.67372 
    3.11934 10.91769 3.11934 
    3.18300 10.63122 3.85143 
    3.31032 10.21743 4.74267 
    3.59679 9.67632 6.01587 
    4.13790 9.10338 7.19358 
    4.64718 8.59410 8.62593 
    5.41110 8.08482 9.73998 
    5.69757 7.98933 10.44024 
    5.88855 8.14848 11.55429 
    6.14319 8.21214 12.31821 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-mb',
                      pts_canal=ps1, pts_opposite=ps2, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-mb2',
                      pts_canal=ps2, pts_opposite=ps1, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

#==============================

s = Specimen('MXK04')
s.tooth_position = CONST.UR
s.note=''
s.canal_type = 0
ps1 = '''
    10.21743 11.90442 1.20954 
    10.47207 11.84076 1.68699 
    10.69488 11.68161 2.48274 
    10.91769 11.45880 3.78777 
    11.07684 11.20416 5.12463 
    11.10867 11.23599 6.42966 
    10.98135 11.26782 7.63920 
    10.66305 11.07684 8.84874 
    10.24926 10.85403 9.96279 
    9.96279 10.72671 10.88586 
'''
ps2 = '''
    10.21743 11.90442 1.20954 
    10.47207 11.80893 1.75065 
    10.66305 11.68161 2.45091 
    10.91769 11.17233 3.75594 
    11.04501 10.79037 4.64718 
    11.04501 10.31292 5.72940 
    10.91769 9.73998 7.00260 
    10.66305 9.48534 8.27580 
    9.99462 9.07155 9.73998 
    9.45351 9.07155 10.91769 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-mb',
                      pts_canal=ps1, pts_opposite=ps2, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-mb2',
                      pts_canal=ps2, pts_opposite=ps1, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

#==============================
        
s = Specimen('MXK05')
s.tooth_position = CONST.UR
s.note=''
s.canal_type = 0

ps1 = '''
    3.18300 8.27580 2.10078 
    3.18300 8.24397 2.57823 
    3.27849 8.37129 3.02385 
    3.31032 8.46678 3.43764 
    3.31032 8.49861 3.91509 
    3.43764 8.56227 4.55169 
    3.69228 8.65776 5.66574 
    3.88326 8.72142 6.77979 
    3.97875 8.62593 7.92567 
    4.04241 8.56227 8.46678 
    4.32888 8.43495 9.26253 
    4.83816 8.37129 10.02645 
    5.69757 7.98933 10.94952 
    6.39783 7.63920 11.64978 
'''
ps2 = '''
    4.39254 9.58083 3.02385 
    4.29705 9.58083 3.50130 
    4.45620 9.73998 4.23339 
    4.64718 9.89913 4.67901 
    4.77450 9.99462 5.18829 
    4.83816 10.05828 5.95221 
    4.83816 10.02645 6.77979 
    5.06097 10.24926 7.41639 
    5.37927 10.47207 8.02116 
    5.66574 10.69488 8.68959 
    6.04770 10.82220 9.32619 
    7.25724 10.56756 10.28109 
    7.67103 10.24926 10.75854 
    8.27580 9.99462 11.49063 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-mb',
                      pts_canal=ps1, pts_opposite=ps2, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-mb2',
                      pts_canal=ps2, pts_opposite=ps1, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

#==============================
    
        
s = Specimen('MXK06')
s.tooth_position = CONST.UR
s.note=''
s.canal_type = 0
ps1 = '''
    7.51188 5.22012 2.00529 
    7.48005 5.37927 2.76921 
    7.28907 5.53842 3.21483 
    6.87528 5.85672 4.10607 
    6.84345 5.95221 4.96548 
    6.84345 6.07953 6.42966 
    6.90711 5.98404 7.32090 
    7.09809 5.92038 8.08482 
    7.44822 6.33417 9.07155 
    7.98933 6.84345 10.05828 
    8.27580 7.09809 11.36331 
'''
ps2 = '''
    6.81162 6.87528 2.38725 
    6.87528 6.71613 2.73738 
    6.90711 6.58881 3.05568 
    6.84345 6.46149 3.81960 
    6.77979 6.46149 4.64718 
    6.68430 6.74796 5.92038 
    6.55698 7.51188 6.90711 
    6.55698 7.92567 7.54371 
    6.87528 8.46678 8.62593 
    7.60737 8.24397 9.64449 
    8.49861 8.46678 10.98135 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-mb',
                      pts_canal=ps1, pts_opposite=ps2, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-mb2',
                      pts_canal=ps2, pts_opposite=ps1, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

#==============================

        
s = Specimen('MXK10')
s.tooth_position = CONST.UR
s.note=''
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
ps1 = '''
    4.10607 10.40841 2.00529 
    4.01058 10.79037 2.57823 
    3.75594 10.98135 2.99202 
    3.53313 10.98135 3.75594 
    3.50130 10.94952 4.71084 
    3.43764 10.91769 5.92038 
    3.56496 10.94952 7.25724 
    3.85143 10.79037 8.43495 
    4.32888 10.72671 9.73998 
    4.48803 10.53573 10.21743 
    4.83816 10.40841 10.75854 
    5.25195 10.18560 11.55429 
    5.66574 9.80364 12.41370 
'''
ps2 = '''
    5.92038 12.12723 3.27849 
    5.82489 12.19089 3.59679 
    5.53842 12.22272 3.91509 
    5.37927 12.19089 4.51986 
    5.41110 12.19089 5.28378 
    5.44293 12.15906 6.39783 
    5.60208 12.31821 7.57554 
    6.01587 12.47736 8.56227 
    6.68430 12.25455 9.89913 
    7.03443 11.93625 10.50390 
    7.51188 11.36331 11.42697 
    7.89384 11.17233 11.90442 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-mb',
                      pts_canal=ps1, pts_opposite=ps2, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-mb2',
                      pts_canal=ps2, pts_opposite=ps1, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

#==============================
    
        
s = Specimen('MXK13')
s.tooth_position = CONST.UL
s.note=''
s.canal_type = 0
ps1 = '''
    8.40312 3.15117 3.46947 
    8.91240 3.37398 4.16973 
    9.26253 3.72411 5.15646 
    9.54900 3.91509 6.30234 
    9.73998 4.01058 7.70286 
    9.80364 4.13790 9.35802 
    9.73998 4.39254 10.69488 
    9.54900 4.90182 11.96808 
    9.35802 5.12463 12.66834 
    9.19887 5.18829 13.30494 
'''
ps2 = '''
    8.40312 3.15117 3.46947 
    8.84874 3.34215 4.07424 
    9.45351 4.01058 5.57025 
    9.86730 4.93365 6.84345 
    10.09011 5.53842 7.98933 
    10.37658 6.30234 10.24926 
    9.93096 6.77979 12.03174 
    9.58083 7.16175 12.98664 
    9.32619 7.38456 13.46409 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-mb',
                      pts_canal=ps1, pts_opposite=ps2, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-mb2',
                      pts_canal=ps2, pts_opposite=ps1, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

#==============================
    
        
s = Specimen('MXK15')
s.tooth_position = CONST.UL
s.note=''
s.canal_type = 0
ps1 = '''
    9.48534 3.69228 3.62862 
    9.86730 3.85143 4.10607 
    10.12194 4.26522 4.93365 
    10.40841 4.61535 5.85672 
    10.66305 5.02914 7.00260 
    10.79037 5.37927 8.05299 
    11.01318 5.63391 9.70815 
    10.98135 5.82489 10.88586 
    10.53573 6.20685 12.31821 
    10.09011 6.52515 13.27311 
'''
ps2 = '''
    8.40312 7.09809 4.32888 
    8.84874 7.32090 4.86999 
    9.16704 7.41639 5.69757 
    9.48534 7.60737 6.74796 
    9.73998 7.70286 7.67103 
    10.02645 7.73469 8.59410 
    10.12194 8.08482 9.45351 
    10.12194 8.40312 10.66305 
    10.02645 8.37129 11.39514 
    9.83547 7.79835 12.35004 
    9.73998 7.48005 12.89115 
'''
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-mb',
                      pts_canal=ps1, pts_opposite=ps2, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-mb2',
                      pts_canal=ps2, pts_opposite=ps1, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

#==============================

s = Specimen('MXK19')
s.tooth_position = CONST.UL
s.note=''
s.canal_type = 0
ps1 = '''
    1.78248 10.91769 1.49601 
    1.40052 10.91769 2.35542 
    1.33686 10.91769 3.15117 
    1.36869 10.91769 4.01058 
    1.55967 10.91769 5.06097 
    1.71882 10.94952 6.33417 
    1.90980 10.82220 7.67103 
    2.25993 10.72671 8.84874 
    2.45091 10.72671 10.02645 
    2.70555 10.40841 10.82220 
    3.31032 10.09011 11.99991 
    4.01058 9.51717 13.08213 
    4.58352 9.13521 14.22801 
'''
ps2 = '''
    2.13261 7.28907 2.54640 
    1.94163 7.25724 3.11934 
    1.90980 7.28907 3.78777 
    1.90980 7.35273 4.93365 
    1.90980 7.48005 5.82489 
    1.97346 7.32090 7.19358 
    2.13261 7.22541 8.40312 
    2.64189 7.48005 10.40841 
    3.18300 7.67103 11.49063 
    3.94692 7.76652 12.44553 
    4.93365 8.18031 13.62324 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-mb',
                      pts_canal=ps1, pts_opposite=ps2, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-mb2',
                      pts_canal=ps2, pts_opposite=ps1, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

#==============================

s = Specimen('MXK21')
s.tooth_position = CONST.UR
s.note=''
s.canal_type = 0
ps1 = '''
    6.87528 12.73200 2.76921 
    7.32090 12.89115 3.37398 
    7.63920 12.89115 4.07424 
    7.95750 12.82749 5.02914 
    8.11665 12.73200 5.88855 
    8.21214 12.50919 7.32090 
    8.08482 12.38187 8.49861 
    7.92567 12.19089 9.54900 
    7.70286 11.71344 10.63122 
    7.38456 11.26782 11.45880 
    7.22541 10.82220 12.22272 
    7.09809 10.56756 12.76383 
'''
ps2 = '''
    6.87528 12.73200 2.76921 
    7.57554 12.79566 3.72411 
    7.86201 12.73200 4.55169 
    8.18031 12.54102 5.63391 
    8.30763 12.31821 6.20685 
    8.46678 12.12723 6.68430 
    8.72142 11.52246 7.51188 
    8.94423 10.94952 8.33946 
    9.00789 10.56756 8.97606 
    8.94423 10.24926 9.73998 
    8.78508 10.05828 10.21743 
    8.68959 9.93096 10.50390 
    8.02116 9.32619 11.58612 
    7.73469 9.23070 12.06357 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-mb',
                      pts_canal=ps1, pts_opposite=ps2, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-mb2',
                      pts_canal=ps2, pts_opposite=ps1, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

#==============================
        
s = Specimen('MXK22')
s.tooth_position = CONST.UL
s.note=''
s.canal_type = 0
ps1 = '''
    5.76123 10.44024 2.99202 
    5.37927 10.40841 3.46947 
    4.99731 10.34475 3.94692 
    4.67901 10.18560 4.48803 
    4.32888 9.96279 5.28378 
    4.13790 9.73998 6.01587 
    4.10607 9.83547 6.65247 
    4.07424 10.02645 7.35273 
    4.32888 9.96279 8.24397 
    4.74267 9.64449 8.97606 
    5.09280 9.42168 9.58083 
    5.53842 9.26253 10.12194 
'''
ps2 = '''
    5.66574 7.89384 3.34215 
    5.31561 8.08482 3.75594 
    4.99731 8.27580 4.23339 
    4.74267 8.53044 4.64718 
    4.42437 8.81691 5.28378 
    4.20156 8.91240 5.92038 
    4.10607 8.59410 6.81162 
    4.16973 8.11665 7.48005 
    4.71084 8.11665 8.65776 
    5.22012 8.40312 9.48534 
    5.69757 8.46678 10.02645 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-mb',
                      pts_canal=ps1, pts_opposite=ps2, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-mb2',
                      pts_canal=ps2, pts_opposite=ps1, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

#==============================

s = Specimen('MXK23')
s.tooth_position = CONST.UL
s.note=''
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
ps1 = '''
    8.62593 1.78248 3.18300 
    8.78508 1.87797 3.40581 
    9.00789 2.03712 3.85143 
    9.26253 2.22810 4.61535 
    9.42168 2.32359 5.47476 
    9.51717 2.64189 6.52515 
    9.51717 2.86470 7.70286 
    9.35802 2.89653 8.81691 
    9.07155 3.08751 10.28109 
    8.68959 3.62862 11.61795 
    8.30763 4.39254 12.76383 
    8.05299 4.74267 13.30494 
'''
ps2 = '''
    9.64449 3.53313 3.62862 
    9.73998 3.66045 3.94692 
    9.93096 3.56496 4.55169 
    9.96279 3.69228 5.09280 
    10.02645 3.59679 5.95221 
    9.96279 3.62862 7.12992 
    9.99462 4.04241 8.11665 
    10.09011 4.61535 8.84874 
    10.09011 4.99731 9.54900 
    10.02645 5.22012 9.99462 
    9.89913 5.57025 10.53573 
    9.70815 5.85672 10.98135 
    9.10338 6.65247 11.84076 
    8.49861 6.90711 12.73200 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-mb',
                      pts_canal=ps1, pts_opposite=ps2, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-mb2',
                      pts_canal=ps2, pts_opposite=ps1, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

#==============================

        
s = Specimen('MXK30')
s.tooth_position = CONST.UL
s.note=''
s.canal_type = 0
ps1 = '''
    11.96808 11.01318 0.89124 
    11.99991 11.39514 1.30503 
    11.96808 11.55429 1.84614 
    11.84076 11.68161 2.48274 
    11.58612 11.64978 3.31032 
    11.55429 11.42697 4.29705 
    11.33148 11.14050 5.34744 
    10.79037 10.59939 6.49332 
    10.40841 10.02645 7.48005 
    10.05828 9.54900 8.11665 
'''
ps2 = '''
    11.96808 11.01318 0.89124 
    11.71344 11.52246 1.46418 
    11.14050 11.80893 2.32359 
    10.31292 11.64978 3.59679 
    9.58083 11.33148 4.74267 
    9.16704 11.10867 5.50659 
    8.94423 10.69488 6.49332 
    8.84874 10.34475 7.00260 
    8.94423 9.70815 8.05299 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-mb',
                      pts_canal=ps1, pts_opposite=ps2, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-mb2',
                      pts_canal=ps2, pts_opposite=ps1, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

#==============================

        
s = Specimen('MXK31')
s.tooth_position = CONST.UR
s.note=''
s.canal_type = 0
ps1 = '''
    13.65507 8.65776 1.81431 
    13.62324 8.33946 2.25993 
    13.43226 8.02116 2.61006 
    13.30494 7.73469 3.08751 
    13.24128 7.35273 4.16973 
    13.14579 7.00260 5.69757 
    13.11396 6.97077 7.38456 
    12.82749 7.09809 8.84874 
    12.54102 7.38456 10.18560 
    12.06357 7.83018 11.58612 
    11.58612 8.05299 12.38187 
    11.29965 8.08482 13.11396 
'''
ps2 = '''
    12.98664 8.21214 2.13261 
    13.05030 7.92567 2.57823 
    13.11396 7.67103 2.99202 
    13.05030 7.28907 4.01058 
    12.73200 6.90711 5.02914 
    12.57285 6.68430 6.36600 
    12.38187 6.65247 7.57554 
    12.03174 6.58881 8.53044 
    11.55429 6.62064 9.70815 
    11.33148 7.03443 10.85403 
    10.50390 7.35273 12.09540 
    9.83547 7.92567 12.79566 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-mb',
                      pts_canal=ps1, pts_opposite=ps2, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-mb2',
                      pts_canal=ps2, pts_opposite=ps1, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

#==============================
    
        
s = Specimen('MXK37')
s.tooth_position = CONST.UL
s.note=''
s.canal_type = 0
ps1 = '''
    12.82749 9.61266 0.09549 
    12.76383 9.61266 0.44562 
    12.60468 9.61266 1.01856 
    12.47736 9.64449 1.52784 
    12.31821 9.64449 2.29176 
    12.22272 9.67632 2.86470 
    11.80893 9.80364 3.81960 
    11.68161 9.80364 4.67901 
    11.58612 9.77181 5.37927 
    11.04501 9.80364 6.55698 
    10.63122 9.64449 7.38456 
    10.34475 9.45351 8.46678 
'''
ps2 = '''
    10.15377 10.24926 1.14588 
    10.18560 10.18560 1.87797 
    10.21743 10.18560 2.48274 
    10.18560 10.21743 3.21483 
    10.37658 10.21743 4.48803 
    10.44024 10.15377 5.47476 
    10.40841 10.05828 6.23868 
    10.24926 9.77181 7.19358 
    9.96279 9.38985 8.02116 
    9.73998 8.97606 8.68959 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-mb',
                      pts_canal=ps1, pts_opposite=ps2, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-mb2',
                      pts_canal=ps2, pts_opposite=ps1, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

#==============================

s = Specimen('MXK40')
s.tooth_position = CONST.UL
s.note=''
s.canal_type = 0
ps1 = '''
    13.46409 8.78508 3.27849 
    13.40043 9.26253 3.75594 
    13.20945 9.70815 4.61535 
    13.08213 9.89913 5.25195 
    12.98664 9.96279 6.11136 
    12.82749 9.96279 6.97077 
    12.66834 9.86730 7.67103 
    12.35004 9.73998 8.40312 
    12.06357 9.51717 9.00789 
    11.71344 9.51717 9.58083 
    11.45880 9.48534 9.96279 
    11.14050 9.42168 10.24926 
'''
ps2 = '''
    12.85932 9.23070 3.50130 
    13.01847 9.48534 3.81960 
    13.01847 9.64449 4.20156 
    12.85932 9.96279 4.99731 
    12.73200 10.05828 5.44293 
    12.35004 10.18560 5.88855 
    11.93625 10.28109 6.39783 
    11.77710 10.31292 6.77979 
    11.58612 10.28109 7.35273 
    11.39514 10.21743 7.86201 
    10.91769 10.05828 8.53044 
    10.72671 9.93096 8.88057 
    10.44024 9.77181 9.32619 
    10.31292 9.70815 9.77181 
    10.18560 9.54900 10.28109 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-mb',
                      pts_canal=ps1, pts_opposite=ps2, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-mb2',
                      pts_canal=ps2, pts_opposite=ps1, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

#==============================
        
s = Specimen('MXK41')
s.tooth_position = CONST.UR
s.note=''
s.canal_type = 0
ps1 = '''
    12.70017 4.99731 2.89653 
    12.73200 5.22012 3.24666 
    12.79566 5.34744 3.62862 
    12.89115 5.06097 4.45620 
    12.60468 4.90182 4.86999 
    12.57285 4.58352 5.88855 
    12.73200 4.48803 6.90711 
    12.47736 4.39254 8.05299 
    12.41370 4.36071 9.10338 
    12.28638 4.36071 10.28109 
    11.96808 4.74267 11.58612 
    11.55429 5.41110 12.76383 
    11.39514 6.01587 13.65507 
'''
ps2 = '''
    11.74527 5.12463 3.59679 
    11.84076 5.15646 3.94692 
    11.93625 4.96548 4.55169 
    12.15906 4.80633 5.12463 
    11.77710 4.64718 5.82489 
    11.45880 4.58352 6.17502 
    11.26782 4.55169 6.77979 
    11.33148 4.45620 7.76652 
    11.10867 4.42437 8.33946 
    10.91769 4.39254 9.23070 
    10.50390 4.48803 10.24926 
    9.83547 4.80633 11.45880 
    9.58083 5.41110 12.47736 
    9.35802 6.14319 13.27311 
    8.97606 6.90711 14.00520 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-mb',
                      pts_canal=ps1, pts_opposite=ps2, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-mb2',
                      pts_canal=ps2, pts_opposite=ps1, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

