'''
Created on 2014. 4. 9.

@author: jongki

total number of teeth : 8
Data from KUM2-11-07-20

'''
# -*- coding: cp949 -*-

from __future__ import division


from constant import CONST
from class_specimen import Specimen, Canal
import os

specimens = []
directory_name = os.getenv('TOOTH_DATA') + '/v3d_mxl/'
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


s = Specimen('MXL02')
s.tooth_position = CONST.UR
s.note=''
s.canal_type = 0
ps1 = '''
    4.47211 3.15117 0.55702 
    4.44028 2.97610 0.97081 
    4.53577 2.89653 1.68699 
    4.58352 3.03976 2.78512 
    4.55169 3.13525 3.72411 
    4.50394 3.26257 5.02914 
    4.53577 3.24666 6.38191 
    4.50394 3.24666 7.43230 
    4.77450 3.07159 8.48269 
    4.94956 2.78512 9.51717 
    5.33152 2.14852 10.94952 
'''
ps2 = '''
    4.45620 3.13525 0.55702 
    4.45620 2.96019 1.12996 
    4.66309 2.92836 2.19627 
    4.99731 3.00793 3.32623 
    5.23603 3.13525 4.51986 
    5.69757 3.15117 5.61799 
    6.22276 3.15117 6.82753 
    6.19093 3.08751 7.92567 
    5.93629 2.92836 8.92831 
    5.72940 2.72146 9.70815 
    5.76123 2.40317 10.36066 
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

s = Specimen('MXL03')
s.tooth_position = CONST.UL
s.note=''
s.canal_type = 0
ps1 = '''
    3.43764 4.01058 1.30503 
    3.53313 3.74002 1.71882 
    3.66045 3.56496 2.24401 
    3.86734 3.45355 3.02385 
    4.09015 3.31032 4.09015 
    4.16973 3.24666 4.91773 
    4.20156 3.23074 5.88855 
    4.32888 3.32623 6.89119 
    4.39254 3.53313 7.86201 
    4.82224 3.93100 8.78508 
    5.10871 4.29705 9.50125 
'''
ps2 = '''
    5.20421 4.20156 1.38460 
    5.07688 3.96283 1.67107 
    5.01322 3.72411 1.90980 
    4.93365 3.59679 2.40317 
    4.86999 3.50130 3.05568 
    4.96548 3.38989 3.77185 
    5.22012 3.31032 4.44028 
    5.49067 3.23074 5.17237 
    5.66574 3.19891 5.93629 
    5.74531 3.29440 6.77979 
    5.71348 3.45355 7.54371 
    5.68165 3.80368 8.38720 
    5.79306 4.28113 9.08746 
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
    
        
s = Specimen('MXL04')
s.tooth_position = CONST.UR
s.note=''
s.canal_type = 0
ps1 = '''
    5.15646 3.24666 1.05039 
    5.12463 3.42172 1.52784 
    5.10871 3.48538 2.24401 
    5.07688 3.56496 3.02385 
    4.98139 3.59679 3.80368 
    4.85407 3.58087 4.75858 
    4.90182 3.48538 5.66574 
    5.02914 3.34215 6.73204 
    5.09280 3.19891 7.86201 
    5.29969 3.03976 8.86465 
    5.53842 2.67372 10.05828 
    5.66574 2.64189 10.82220 
'''
ps2 = '''
    7.05034 3.42172 1.67107 
    6.98668 3.56496 2.10078 
    6.81162 3.64453 2.81695 
    6.65247 3.66045 3.54904 
    6.57289 3.64453 4.20156 
    6.36600 3.62862 4.90182 
    6.30234 3.61270 5.57025 
    6.17502 3.58087 6.50923 
    6.60472 3.56496 7.48005 
    7.08217 3.54904 8.57818 
    7.27315 3.37398 9.37393 
    7.46413 3.16708 10.31292 
    8.08482 2.78512 11.14050 
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

        
s = Specimen('MXL05')
s.tooth_position = CONST.UL
s.note=''
s.canal_type = 0
ps1 = '''
    5.88855 2.81695 0.92307 
    6.01587 3.00793 1.55967 
    6.20685 2.94427 2.59414 
    6.33417 2.91245 3.45355 
    6.41374 2.88061 4.21747 
    6.55698 2.91245 4.88590 
    6.79570 2.86470 5.47476 
    6.82753 2.80104 6.14319 
    6.74796 2.73738 6.93894 
    6.57289 2.62597 7.73469 
    6.28642 2.45091 8.57818 
    5.93629 2.25993 9.40576 
    5.87263 1.83022 10.16968 
'''
ps2 = '''
    5.88855 2.81695 0.92307 
    5.87263 2.99202 1.79839 
    5.92038 2.92836 2.45091 
    5.88855 2.88061 3.32623 
    5.66574 2.91245 4.39254 
    5.34744 2.92836 5.09280 
    5.07688 2.97610 5.76123 
    4.85407 2.97610 6.76387 
    4.83816 2.84878 7.63920 
    4.58352 2.57823 8.38720 
    4.61535 2.19627 9.21478 
    4.71084 1.67107 10.32884 
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

s = Specimen('MXL06')
s.tooth_position = CONST.UR
s.note=''
s.canal_type = 0
ps1 = '''
    5.79306 3.51721 0.60477 
    5.76123 3.48538 0.81166 
    5.79306 3.43764 1.11405 
    5.95221 3.34215 1.79839 
    6.12727 3.18300 2.35542 
    6.28642 3.03976 3.00793 
    6.42966 2.96019 3.70819 
    6.38191 2.94427 4.45620 
    6.28642 3.02385 5.07688 
    6.12727 3.15117 5.71348 
    5.85672 3.32623 6.46149 
    5.58616 3.54904 7.19358 
    5.33152 3.80368 7.87792 
    5.12463 4.28113 8.72142 
    5.14054 4.64718 9.35802 
'''
ps2 = '''
    4.31296 3.50130 1.35277 
    4.39254 3.43764 1.60741 
    4.47211 3.37398 1.94163 
    4.63127 3.26257 2.46682 
    4.71084 3.10342 3.10342 
    4.69492 3.00793 3.72411 
    4.66309 2.94427 4.36071 
    4.61535 3.00793 4.82224 
    4.48803 3.08751 5.69757 
    4.47211 3.26257 6.58881 
    4.44028 3.58087 7.44822 
    4.40846 3.94692 8.16439 
    4.47211 4.39254 8.86465 
    4.63127 4.71084 9.48534 
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
        
s = Specimen('MXL07')
s.tooth_position = CONST.UR
s.note=''
s.canal_type = 0
ps1 = '''
    2.48274 2.51457 0.74800 
    2.56231 2.57823 0.89124 
    2.65780 2.72146 1.19362 
    2.83287 2.86470 1.54375 
    3.02385 2.94427 1.86205 
    3.29440 3.08751 2.22810 
    3.56496 3.21483 2.56231 
    3.77185 3.35806 3.00793 
    4.04241 3.50130 3.46947 
    4.28113 3.58087 3.97875 
    4.39254 3.61270 4.71084 
    4.23339 3.53313 5.50659 
    4.15381 3.46947 6.22276 
    4.23339 3.32623 6.98668 
    4.40846 3.11934 7.86201 
    4.55169 2.92836 8.48269 
    4.69492 2.76921 8.94423 
'''
ps2 = '''
    4.39254 2.43499 1.38460 
    4.45620 2.54640 1.57558 
    4.63127 2.70555 1.81431 
    4.82224 2.88061 2.08486 
    5.01322 3.11934 2.46682 
    5.02914 3.35806 2.91245 
    5.04505 3.51721 3.37398 
    5.15646 3.64453 3.80368 
    5.26786 3.69228 4.37662 
    5.45884 3.74002 4.98139 
    5.71348 3.74002 5.42701 
    5.90446 3.74002 5.84080 
    6.27051 3.70819 6.44557 
    6.52515 3.58087 6.89119 
    6.77979 3.34215 7.36864 
    7.03443 3.03976 7.83018 
    7.20949 2.72146 8.25988 
    7.32090 2.45091 8.73733 
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
    
        
s = Specimen('MXL0A')
s.tooth_position = CONST.UL
s.note=''
s.canal_type = 0
ps1 = '''
    5.10871 3.59679 0.89124 
    5.20421 3.43764 1.35277 
    5.31561 3.13525 1.94163 
    5.18829 2.92836 2.72146 
    5.29969 2.86470 3.85143 
    5.26786 2.83287 5.29969 
    5.29969 2.97610 6.31825 
    5.55433 3.29440 7.49596 
    5.80897 3.67636 8.37129 
    6.03178 4.07424 9.27844 
'''
ps2 = '''
    6.39783 3.48538 0.79575 
    6.28642 3.37398 1.16179 
    6.12727 3.15117 1.75065 
    6.04770 3.00793 2.43499 
    5.98404 2.94427 2.97610 
    5.69757 2.88061 3.89917 
    5.90446 2.84878 4.66309 
    6.17502 2.83287 5.44293 
    6.31825 2.91245 6.14319 
    6.58881 3.02385 6.76387 
    6.95485 3.23074 7.38456 
    7.12992 3.50130 8.00524 
    7.16175 3.72411 8.43495 
    7.00260 3.96283 9.00789 
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

        
s = Specimen('MXL0B')
s.tooth_position = CONST.UR
s.note=''
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
ps1 = '''
    4.59943 1.84614 1.06630 
    4.61535 2.11670 1.63924 
    4.64718 2.29176 2.18035 
    4.72675 2.53048 2.86470 
    4.83816 2.75329 3.94692 
    4.88590 2.89653 5.34744 
    4.80633 2.78512 6.30234 
    5.04505 2.53048 7.32090 
    5.33152 2.00529 8.27580 
    5.42701 1.67107 8.88057 
'''
ps2 = '''
    6.79570 2.56231 0.82758 
    6.71613 2.67372 1.27320 
    6.79570 2.80104 1.89388 
    6.85936 2.84878 2.53048 
    6.77979 2.92836 3.43764 
    7.00260 3.05568 4.66309 
    7.20949 3.03976 5.68165 
    7.14583 2.96019 6.38191 
    7.05034 2.72146 7.16175 
    6.77979 2.32359 8.00524 
    6.09544 1.70290 8.81691 
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
