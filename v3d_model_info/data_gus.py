# -*- coding: cp949 -*-

'''
Created on 2013. 4. 14.
@author: jongki
'''
from __future__ import division
import helpers_contours as du       # collection of utility function
import const as CON          # constant       

roots = []
bounding_box_range = [(-2, 12), (-4, 10), (0, 14)]

directory_name = 'E:/0.jongki.data/Dropbox/15.Develop/tooth-data/v3d_g18/'
canal_pre_suffix = '-canal-zoff.v3d'
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
# 0-GUS02
root = range(ELEM_COUNT)
root[CON.NAME] = 'GUS02'
root[CON.POS] = CONST.LL
root[CON.NOTE] = '13-3-19-check all'
ps1_pre = '''
    5.25000 2.68500 1.57500
    5.11500 2.89500 1.87500
    4.86000 3.12000 2.29500
    4.65000 3.15000 2.62500
    4.26000 3.21000 3.64500
    3.81000 3.24000 4.72500
    3.52500 3.31500 5.92500
    3.03000 3.31500 7.39500
    2.74500 3.28500 9.10500
    2.71500 3.13500 10.33500
    2.97000 2.79000 12.13500
    3.10500 2.52000 13.24500
    '''
ps1_post = '''
    5.31000 2.70000 1.33500
    5.02500 2.97000 2.02500
    4.06500 3.27000 4.09500
    3.25500 3.33000 6.52500
    2.94000 3.16500 9.13500
    2.94000 2.80500 12.22500
    3.00000 2.64000 13.48500
    '''
ps2_pre = '''
    6.79500 2.74500 2.02500
    6.60000 2.94000 2.38500
    6.52500 3.01500 2.98500
    6.43500 3.04500 3.88500
    6.39000 3.13500 5.11500
    6.48000 3.19500 6.55500
    6.48000 3.22500 7.63500
    6.60000 3.27000 9.10500
    6.51000 3.19500 10.33500
    6.36000 2.97000 11.77500
    6.18000 2.64000 13.24500
    '''
ps2_post = '''
    6.72000 2.76000 1.90500
    6.60000 2.89500 2.32500
    6.51000 2.98500 2.83500
    6.43500 3.15000 4.99500
    6.43500 3.22500 7.36500
    6.40500 3.00000 11.08500
    6.37500 2.74500 13.42500
    '''
    
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PRE_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_pre_suffix
root[CON.CANAL_POST_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_post_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1_PRE], root[CON.PS1_POST] = du.convert_to_points(ps1_pre), du.convert_to_points(ps1_post)
root[CON.PS2_PRE], root[CON.PS2_POST] = du.convert_to_points(ps2_pre), du.convert_to_points(ps2_post)
roots.append(root)

