'''
Created on 2014. 4. 9.

@author: jongki

data from choi jh
'''

# -*- coding: cp949 -*-

from __future__ import division
from constant import CONST
from class_specimen import Specimen, Canal
import os

specimens = []
bounding_box_range = [(-10, 20), (-10, 20), (-2, 28)]
directory_name = os.getenv('TOOTH_DATA') + '/v3d_mx4/'
canal_suffix = '-canal-zoff.v3d'
body_suffix = '-solid-body-zoff.v3d'

#####################
s = Specimen('MX4-01')
s.tooth_position = CONST.UL
s.note = ''
s.canal_type = 10

buccal = '''
    4.89280 4.01280 0.84480 
    4.78720 3.92480 1.09120 
    4.66400 3.88960 1.35520 
    4.47040 3.90720 2.28800 
    4.40000 3.94240 3.08000 
    4.36480 3.99520 4.03040 
    4.47040 4.10080 4.96320 
    4.57600 4.18880 5.86080 
    4.73440 4.20640 6.86400 
    4.76960 4.22400 7.70880 
    4.69920 4.31200 8.80000 
    4.31200 4.38240 10.48960 
'''

palatal = '''
    8.27200 4.43520 0.98560 
    8.16640 4.45280 1.24960 
    8.06080 4.45280 1.54880 
    7.70880 4.45280 2.65760 
    7.65600 4.43520 3.23840 
    7.67360 4.41760 3.76640 
    7.69120 4.45280 4.69920 
    7.72640 4.45280 6.07200 
    7.58560 4.50560 7.39200 
    7.49760 4.52320 8.64160 
    7.70880 4.57600 9.96160 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-b', furcation_pos=8.0,
                      pts_canal=buccal, pts_opposite=palatal, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-p', furcation_pos=9.0,
                      pts_canal=palatal, pts_opposite=buccal, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

#################################################
s = Specimen('MX4-02')
s.tooth_position = CONST.UL
s.note = ''
s.canal_type = 10

buccal = '''
    7.33920 2.74560 0.47520 
    7.42720 2.86880 0.72160 
    7.49760 2.95680 1.03840 
    7.56800 3.13280 1.63680 
    7.60320 3.32640 2.51680 
    7.55040 3.60800 3.55520 
    7.49760 3.87200 4.82240 
    7.56800 3.90720 6.24800 
    7.72640 3.85440 8.04320 
    7.56800 3.74880 9.53920 
    7.37440 3.64320 10.87680 
    7.35680 3.67840 12.37280 
'''

palatal = '''
    2.42880 2.09440 1.14400 
    2.48160 2.09440 1.60160 
    2.48160 2.16480 1.84800 
    2.41120 2.34080 2.51680 
    2.34080 2.42880 2.97440 
    2.16480 2.60480 3.97760 
    2.05920 2.83360 5.10400 
    2.14720 3.04480 6.60000 
    2.55200 3.13280 8.21920 
    2.86880 3.22080 9.57440 
    3.32640 3.29120 10.87680 
    3.69600 3.39680 12.61920 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-b', furcation_pos=8.0,
                      pts_canal=buccal, pts_opposite=palatal, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-p', furcation_pos=9.0,
                      pts_canal=palatal, pts_opposite=buccal, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

#################################################
s = Specimen('MX4-03')
s.tooth_position = CONST.UL
s.note = ''
s.canal_type = 10

buccal = '''
    4.59360 4.68160 0.49280 
    4.36480 4.68160 0.84480 
    4.13600 4.66400 1.12640 
    3.92480 4.57600 1.68960 
    3.76640 4.47040 2.28800 
    3.55520 4.25920 3.27360 
    3.34400 3.99520 4.22400 
    3.34400 3.81920 5.06880 
    3.41440 3.64320 5.98400 
    3.37920 3.44960 7.21600 
    3.41440 3.39680 9.92640 
    3.23840 3.46720 12.03840 
'''
palatal = '''
    9.16960 4.27680 1.14400 
    8.97600 4.22400 1.44320 
    8.83520 4.18880 1.68960 
    8.46560 4.06560 2.53440 
    8.13120 3.87200 3.59040 
    7.97280 3.71360 4.57600 
    7.84960 3.52000 5.94880 
    7.67360 3.18560 8.16640 
    7.56800 3.16800 9.39840 
    7.35680 3.16800 11.33440 
    7.07520 3.20320 12.42560 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-b', furcation_pos=8.0,
                      pts_canal=buccal, pts_opposite=palatal, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-p', furcation_pos=9.0,
                      pts_canal=palatal, pts_opposite=buccal, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

#################################################
s = Specimen('MX4-04')
s.tooth_position = CONST.UL
s.note = ''
s.canal_type = 10

buccal = '''
    5.20960 4.64640 0.70400 
    5.13920 4.71680 0.88000 
    5.03360 4.68160 1.05600 
    4.78720 4.54080 1.68960 
    4.61120 4.43520 2.35840 
    4.61120 4.11840 3.37920 
    4.69920 3.80160 4.36480 
    4.69920 3.60800 5.35040 
    4.40000 3.52000 6.47680 
    4.22400 3.39680 7.49760 
    4.13600 3.37920 9.25760 
    4.06560 3.41440 11.08800 
'''
palatal = '''
    7.92000 3.80160 1.07360 
    7.79680 3.88960 1.23200 
    7.79680 3.96000 1.40800 
    7.84960 4.01280 2.04160 
    8.02560 4.04800 2.88640 
    8.27200 3.94240 3.97760 
    8.46560 3.80160 5.66720 
    8.23680 3.71360 7.67360 
    7.81440 3.76640 9.82080 
    7.56800 3.71360 11.29920 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-b', furcation_pos=8.0,
                      pts_canal=buccal, pts_opposite=palatal, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-p', furcation_pos=9.0,
                      pts_canal=palatal, pts_opposite=buccal, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

#################################################
s = Specimen('MX4-05')
s.tooth_position = CONST.UL
s.note = ''
s.canal_type = 10

buccal = '''
    6.24800 3.71360 0.72160 
    6.44160 3.71360 0.95040 
    6.58240 3.69600 1.23200 
    6.75840 3.59040 1.54880 
    6.91680 3.62560 2.00640 
    7.09280 3.53760 2.71040 
    7.32160 3.16800 3.97760 
    7.26880 2.79840 5.73760 
    7.26880 2.72800 7.35680 
    7.16320 2.78080 8.76480 
    7.04000 2.93920 10.17280 
    6.89920 3.15040 12.39040 
'''

palatal = '''
    2.62240 4.01280 0.65120 
    2.65760 4.10080 0.95040 
    2.69280 4.11840 1.16160 
    2.79840 4.06560 2.07680 
    2.81600 3.99520 2.88640 
    2.83360 3.78400 4.01280 
    2.81600 3.59040 5.10400 
    2.92160 3.43200 6.79360 
    3.00960 3.41440 8.09600 
    3.00960 3.46720 9.78560 
    3.25600 3.46720 11.29920 
    3.59040 3.43200 12.32000 
'''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-b', furcation_pos=8.0,
                      pts_canal=buccal, pts_opposite=palatal, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-p', furcation_pos=9.0,
                      pts_canal=palatal, pts_opposite=buccal, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

#################################################
s = Specimen('MX4-06')
s.tooth_position = CONST.UL
s.note = ''
s.canal_type = 10

buccal = '''
    8.16640 5.45600 1.07360 
    8.25440 5.42080 1.40800 
    8.28960 5.33280 1.76000 
    8.18400 5.06880 2.67520 
    8.00800 4.82240 3.34400 
    7.76160 4.43520 4.29440 
    7.56800 4.18880 5.28000 
    7.63840 4.08320 6.33600 
    7.72640 3.94240 7.67360 
    7.63840 3.87200 8.76480 
    7.42720 3.92480 10.17280 
    7.21600 3.92480 11.40480 
'''

palatal = '''
    4.40000 4.27680 0.84480 
    4.36480 4.43520 0.95040 
    4.22400 4.47040 1.23200 
    4.03040 4.45280 1.61920 
    3.88960 4.38240 2.21760 
    3.64320 4.27680 3.06240 
    3.41440 4.18880 3.97760 
    3.23840 4.17120 4.96320 
    3.23840 4.15360 5.94880 
    3.36160 4.17120 7.49760 
    3.55520 4.18880 9.11680 
    3.69600 4.17120 10.31360 
    3.90720 4.10080 11.12320 
'''
s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-b', furcation_pos=8.0,
                      pts_canal=buccal, pts_opposite=palatal, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-p', furcation_pos=9.0,
                      pts_canal=palatal, pts_opposite=buccal, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)
