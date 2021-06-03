'''
Created on 2014. 4. 9.

@author: jongki

total number of teeth : 5
Data from KYU-12-01-09

'''

# -*- coding: cp949 -*-

from __future__ import division

import helpers_contours as du  # collection of utility function
from specimens.class_specimen import Specimen

roots = []
bounding_box_range = [(-10, 20), (-10, 20), (-2, 28)]
directory_name = 'E:/0.jongki.data/Dropbox/15.Develop/tooth-data/v3d_mxy/'
canal_suffix = '-canal-zoff.v3d'
body_suffix = '-solid-body-zoff.v3d'
ELEM_COUNT = 11

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

s = Specimen('MXY13')
s.location = CONST.UR
s.note=''
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
ps1 = '''
    8.14848 2.54640 0.82758 
    8.02116 2.62597 1.09813 
    7.76652 2.89653 1.57558 
    7.52779 3.10342 2.18035 
    7.08217 3.18300 3.08751 
    6.90711 3.23074 3.67636 
    6.71613 3.23074 4.40846 
    6.49332 3.11934 5.12463 
    6.60472 3.21483 5.85672 
    6.58881 3.23074 6.33417 
    6.47740 3.16708 6.98668 
    6.52515 3.18300 7.78243 
    6.49332 3.23074 8.40312 
    6.36600 3.29440 9.35802 
    6.14319 3.61270 10.48798 
    6.01587 3.81960 10.83811 
'''
ps2 = '''
    3.13525 3.72411 2.73738 
    3.26257 3.59679 2.94427 
    3.48538 3.34215 3.34215 
    3.89917 3.18300 3.96283 
    3.99466 3.18300 4.53577 
    3.94692 3.24666 5.29969 
    4.12198 3.21483 6.06361 
    4.28113 3.21483 6.79570 
    4.20156 3.27849 7.55962 
    4.07424 3.37398 8.54635 
    4.07424 3.45355 9.29436 
    4.10607 3.62862 10.13785 
    4.16973 3.88326 10.71079 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('MXY14')
s.location = CONST.UR
s.note=''
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
ps1 = '''
    2.62597 2.94427 1.00265 
    2.76921 3.00793 1.48009 
    2.88061 3.00793 1.92571 
    2.92836 2.92836 2.35542 
    2.84878 3.07159 2.84878 
    2.84878 3.40581 3.97875 
    2.97610 3.48538 4.91773 
    3.08751 3.48538 5.98404 
    3.10342 3.35806 7.11400 
    3.26257 3.29440 8.05299 
    3.58087 3.13525 8.84874 
    3.99466 2.91245 9.91504 
    4.51986 2.61006 10.77446 
'''
ps2 = '''
    7.51188 3.32623 0.85941 
    7.36864 3.35806 1.30503 
    7.16175 3.43764 1.63924 
    6.97077 3.43764 2.29176 
    6.84345 3.50130 3.15117 
    6.90711 3.56496 3.97875 
    6.95485 3.59679 4.96548 
    6.87528 3.64453 5.71348 
    7.08217 3.58087 6.63655 
    7.14583 3.46947 7.62328 
    7.14583 3.31032 8.78508 
    6.95485 3.15117 9.73998 
    6.82753 2.89653 10.69488 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('MXY18')
s.location = CONST.UL
s.note=''
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
ps1 = '''
    2.99202 5.12463 1.67107 
    3.26257 4.74267 2.00529 
    3.62862 4.23339 2.41908 
    4.13790 3.67636 3.03976 
    4.44028 3.15117 4.04241 
    4.83816 2.88061 4.90182 
    5.20421 2.80104 6.04770 
    5.41110 2.89653 7.22541 
    5.77714 3.26257 8.56227 
    6.06361 3.53313 9.31027 
'''
ps2 = '''
    5.98404 3.81960 0.17506 
    6.09544 3.62862 0.58885 
    6.09544 3.59679 1.19362 
    6.09544 3.67636 1.75065 
    5.84080 3.35806 2.80104 
    6.19093 2.91245 4.09015 
    6.44557 2.76921 5.17237 
    6.95485 2.76921 6.38191 
    7.24132 2.97610 7.54371 
    7.24132 3.29440 8.45086 
    6.77979 3.75594 9.45351 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('MXY30')
s.location = CONST.UR
s.note=''
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
ps1 = '''
    7.08217 4.18565 0.62068 
    7.09809 4.12198 0.89124 
    7.19358 4.02649 1.33686 
    7.24132 3.80368 2.00529 
    7.19358 3.54904 2.92836 
    7.24132 3.29440 4.01058 
    7.27315 3.15117 4.85407 
    7.38456 3.15117 5.47476 
    7.41639 3.26257 6.44557 
    7.30498 3.37398 7.05034 
    6.92302 3.54904 7.57554 
    6.57289 3.89917 8.24397 
    6.50923 4.16973 8.72142 
'''
ps2 = '''
    5.18829 4.24930 1.33686 
    5.17237 4.01058 1.86205 
    5.04505 3.80368 2.35542 
    4.98139 3.56496 3.00793 
    5.06097 3.31032 3.81960 
    5.18829 3.19891 4.88590 
    5.04505 3.24666 5.85672 
    4.88590 3.34215 6.50923 
    5.09280 3.64453 7.54371 
    5.22012 4.02649 8.25988 
    5.28378 4.20156 8.57818 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('MXY31')
s.location = CONST.UR
s.note=''
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
ps1 = '''
    3.99466 2.65780 0.46153 
    3.91509 2.68963 0.74800 
    3.88326 2.80104 1.27320 
    3.88326 2.89653 1.86205 
    3.89917 2.97610 2.61006 
    3.96283 2.97610 3.27849 
    4.01058 2.91245 4.04241 
    4.10607 2.75329 4.90182 
    4.31296 2.43499 5.92038 
    4.53577 2.19627 6.65247 
    4.94956 1.59150 7.84609 
    5.01322 1.11405 8.64185 
'''
ps2 = '''
    7.06626 2.62597 1.57558 
    7.01851 2.72146 1.92571 
    6.85936 2.80104 2.29176 
    6.79570 2.89653 2.97610 
    6.77979 2.88061 3.69228 
    6.82753 2.84878 4.51986 
    6.84345 2.67372 5.49067 
    6.85936 2.41908 6.41374 
    6.65247 1.71882 7.63920 
    6.52515 0.87532 8.67367 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    