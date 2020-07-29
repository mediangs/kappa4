'''
Created on 2014. 4. 22.

@author: jongki

total number of teeth : 6
Data from LK01 ~ 80 12-01-01 ~ 12-08-21

'''
# -*- coding: cp949 -*-

from __future__ import division


from constant import CONST
from class_specimen import Specimen, Canal
import os

specimens = []
directory_name = os.getenv('TOOTH_DATA') + '/v3d_mxlk/'
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

s = Specimen('LK102')
s.tooth_position = CONST.UR
s.note=''
s.canal_type = 0
ps1 = '''
    5.69757 3.89917 0.58885
    5.72940 3.81960 0.90715
    5.69757 3.75594 1.25729
    5.57025 3.67636 1.57558
    5.37927 3.54904 2.14852
    5.18829 3.37398 3.07159
    5.22012 3.26257 3.99466
    5.25195 3.05568 5.36335
    5.34744 3.02385 6.12727
    5.31561 3.05568 7.17766
    5.36335 3.26257 8.35537
    5.29969 3.56496 9.27844
    5.06097 3.86734 10.07420
    4.59943 4.37662 11.31556
'''
ps2 = '''
    4.24930 3.66045 1.86205
    4.39254 3.58087 2.18035
    4.66309 3.43764 2.68963
    4.75858 3.35806 3.07159
    4.75858 3.21483 3.83551
    4.66309 3.05568 4.72675
    4.51986 2.97610 5.74531
    4.10607 2.94427 6.76387
    3.59679 3.00793 7.97341
    3.34215 3.24666 8.96014
    3.15117 3.43764 9.53308
    2.89653 4.01058 10.55164
    2.97610 4.42437 11.18824
    2.92836 4.72675 11.63386
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
    
s = Specimen('LK103')
s.tooth_position = CONST.UL
s.note=''
s.canal_type = 0
ps1 = '''
    3.69228 3.75594 1.20954
    3.69228 3.94692 1.48009
    3.70819 3.94692 1.70290
    3.74002 3.81960 2.05303
    3.78777 3.61270 2.43499
    3.78777 3.45355 2.81695
    3.72411 3.27849 3.38989
    3.61270 3.08751 4.09015
    3.56496 2.89653 5.17237
    3.59679 2.86470 5.80897
    3.59679 2.88061 6.76387
    3.62862 2.99202 7.75060
    3.78777 3.21483 8.76916
    3.99466 3.62862 9.78773
    4.20156 3.93100 10.45615
    4.53577 4.39254 11.28373
'''
ps2 = '''
    4.91773 3.40581 2.92836
    4.80633 3.31032 3.23074
    4.85407 3.19891 3.58087
    4.91773 3.02385 4.05833
    4.98139 2.84878 4.75858
    4.83816 2.80104 5.39518
    4.93365 2.72146 6.06361
    5.37927 2.65780 7.01851
    5.68165 2.72146 7.87792
    5.99995 2.89653 8.64185
    6.22276 3.24666 9.43760
    6.46149 3.67636 10.16968
    6.47740 4.10607 10.80628
    6.27051 4.51986 11.44288
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
    
s = Specimen('LK108')
s.tooth_position = CONST.UR
s.note=''
s.canal_type = 0
ps1 = '''
    2.73738 2.65780 0.62068
    2.68963 2.68963 0.87532
    2.59414 2.72146 1.28911
    2.61006 2.73738 1.76656
    2.64189 2.73738 2.21218
    2.72146 2.75329 2.81695
    2.91245 2.73738 3.58087
    3.16708 2.80104 4.34479
    3.31032 2.83287 5.49067
    3.46947 2.78512 6.47740
    3.66045 2.62597 7.33681
    3.93100 2.46682 7.97341
    4.26522 2.35542 8.35537
    4.91773 2.00529 8.86465
    5.41110 1.94163 9.81955
'''
ps2 = '''
    5.55433 2.96019 2.10078
    5.42701 3.02385 2.40317
    5.42701 3.10342 2.88061
    5.47476 3.11934 3.19891
    5.52250 3.16708 3.77185
    5.57025 3.26257 4.31296
    5.60208 3.27849 4.88590
    5.61799 3.29440 5.33152
    5.61799 3.31032 5.74531
    5.57025 3.24666 6.25459
    5.87263 3.18300 6.76387
    6.23868 3.05568 7.33681
    6.55698 2.83287 7.75060
    6.70021 2.64189 8.03707
    6.81162 2.40317 8.57818
    6.85936 2.14852 9.15112
    6.84345 1.94163 9.81955
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
    
s = Specimen('LK14')
s.tooth_position = CONST.UR
s.note=''
s.canal_type = 0
ps1 = '''
6.76387 3.24666 0.89124
6.68430 3.18300 1.32094
6.60472 3.10342 1.70290
6.58881 3.26257 2.18035
6.73204 3.42172 2.62597
6.82753 3.53313 3.03976
7.06626 3.64453 3.86734
7.16175 3.67636 4.63127
7.30498 3.70819 5.39518
7.35273 3.80368 6.31825
7.12992 3.89917 7.33681
6.62064 4.10607 8.10073
6.09544 4.32888 8.70550
5.69757 4.69492 9.43760
5.53842 5.18829 10.48798
'''
ps2 = '''
4.39254 3.19891 1.46418
4.44028 3.07159 2.02120
4.50394 3.10342 2.81695
4.37662 3.31032 3.45355
4.24930 3.53313 4.18565
4.04241 3.66045 4.88590
3.53313 3.78777 5.58616
3.42172 3.81960 6.06361
2.96019 4.04241 7.49596
3.07159 4.31296 8.29171
3.35806 4.61535 8.89648
3.88326 4.99731 9.62857
4.13790 5.42701 10.45615
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
    
s = Specimen('LK18')
s.tooth_position = CONST.UL
s.note=''
s.canal_type = 0
ps1 = '''
4.48803 4.07424 0.62068
4.45620 3.78777 0.93898
4.39254 3.59679 1.19362
4.26522 3.38989 1.54375
4.18565 3.19891 1.95754
4.13790 3.11934 2.33950
4.09015 3.03976 2.75329
4.13790 2.91245 3.29440
4.09015 2.91245 3.96283
3.97875 2.91245 4.56760
3.91509 3.00793 5.26786
3.91509 3.07159 5.96812
3.94692 3.23074 6.79570
4.13790 3.45355 7.75060
4.31296 3.78777 8.70550
4.77450 4.13790 9.50125
4.98139 4.71084 10.29700
'''
ps2 = '''
6.47740 3.26257 2.53048
6.39783 3.13525 2.68963
6.35008 3.05568 2.97610
6.31825 2.99202 3.58087
6.23868 2.92836 4.28113
6.19093 2.89653 4.98139
6.01587 3.00793 5.96812
5.99995 3.10342 6.89119
6.28642 3.18300 7.84609
6.58881 3.24666 8.35537
6.81162 3.45355 8.86465
6.77979 3.93100 9.43760
6.41374 4.45620 10.13785
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
    
s = Specimen('LK71')
s.tooth_position = CONST.UR
s.note=''
s.canal_type = 0
ps1 = '''
2.06895 1.55967 0.55702
2.13261 1.57558 0.74800
2.24401 1.60741 0.97081
2.43499 1.60741 1.22546
2.65780 1.78248 1.57558
2.83287 1.98937 2.18035
2.88061 2.32359 3.00793
2.86470 2.48274 3.80368
2.97610 2.51457 4.63127
3.02385 2.35542 5.64982
3.11934 2.18035 6.79570
3.35806 1.79839 7.78243
3.66045 1.33686 8.73733
3.85143 1.01856 9.53308
4.02649 0.85941 10.10602
'''
ps2 = '''
5.99995 2.10078 2.37133
5.98404 2.21218 2.62597
5.88855 2.49865 3.13525
5.88855 2.65780 3.54904
5.96812 2.70555 4.18565
6.09544 2.70555 4.53577
6.22276 2.73738 4.91773
6.22276 2.64189 6.09544
6.31825 2.57823 6.85936
6.35008 2.10078 8.35537
6.11136 1.76656 8.83282
5.95221 1.55967 9.15112
5.52250 1.05039 10.10602
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
    
s = Specimen('LK80')
s.tooth_position = CONST.UL
s.note=''
s.canal_type = 0
ps1 = '''
1.84614 5.22012 1.27320
1.90980 5.17237 1.41643
1.97346 5.04505 1.54375
2.13261 4.93365 1.70290
2.33950 4.79041 1.92571
2.49865 4.67901 2.24401
2.72146 4.44028 2.65780
2.88061 4.15381 3.19891
2.94427 3.89917 3.83551
2.99202 3.66045 4.56760
2.97610 3.54904 5.52250
3.07159 3.53313 6.35008
3.51721 3.56496 7.46413
3.94692 3.94692 8.83282
4.24930 4.28113 10.04236
'''
ps2 = '''
5.18829 4.51986 2.75329
5.31561 4.36071 2.94427
5.37927 4.20156 3.13525
5.41110 3.99466 3.42172
5.45884 3.75594 3.86734
5.49067 3.56496 4.50394
5.49067 3.46947 5.04505
5.47476 3.32623 5.99995
5.47476 3.26257 7.11400
5.34744 3.45355 8.25988
5.45884 3.78777 9.05563
5.79306 4.07424 9.62857
5.87263 4.34479 9.97870
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

