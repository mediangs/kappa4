'''
Created on 2014. 3. 14.

@author: jongki

data from chang
mandibular incisors

'''

# -*- coding: cp949 -*-

from __future__ import division
import helpers_contours as du       # collection of utility function
import const as CON          # constant   
from vector_class import vector

roots = []
bounding_box_range = [(-10, 20), (-10, 20), (-10, 20)]
directory_name = 'E:/0.jongki.data/Dropbox/15.Develop/tooth-data/v3d_smc/'
canal_suffix = '-canal-zoff.v3d'
body_suffix = '-solid-body-zoff.v3d'
ELEM_COUNT = 11

#===============================================================================
# --based on v-works image
# RIGHT                             Apical 
#          LABIAL                     ^
#        ...........                  |
#     ...           .....             |
#   .**                  ..           |  
#   .**    .......     ..             | 
#     .....       .....               |
#                                     | 
#                                   Coronal
# 
#===============================================================================


###########
#  0-SMC01
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC01'
root[CON.POS] = CONST.LR
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
2.77309 3.79755 0.44158
2.79075 3.69157 0.65353
2.94972 3.63858 1.16576
3.07336 3.62092 1.88994
3.16168 3.62092 2.75543
3.16168 3.70923 4.08015
3.07336 3.67390 5.47553
3.03804 3.65624 6.62363
2.98505 3.69157 7.64808
2.94972 3.69157 8.16031
2.96738 3.69157 8.88449
3.02037 3.72689 9.53802
3.07336 3.77988 10.13856
    '''
ps2 = '''
2.93206 3.67390 8.60188
5.98776 3.65624 8.60188
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  1-SMC02
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC02'
root[CON.POS] = CONST.LL
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
2.93206 4.22146 0.52989
2.91440 4.04483 1.11277
2.87907 3.95651 1.60733
2.91440 3.93885 2.38451
2.98505 3.93885 3.30298
3.02037 3.93885 4.29211
3.10869 3.95651 5.29890
3.12635 3.92119 6.42933
3.09103 3.92119 7.36547
3.09103 3.81521 8.33694
3.07336 3.77988 9.53802
2.94972 3.79755 10.50949
    '''
ps2 = '''
3.09103 3.92119 6.74727
6.23504 3.99184 6.74727
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  2-SMC03
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC03'
root[CON.POS] = CONST.LR
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
3.74456 3.35597 1.48369
3.79755 3.33831 1.87228
3.92119 3.33831 2.43749
4.00950 3.33831 3.14401
3.95651 3.40896 4.20379
3.79755 3.44429 5.26357
3.77988 3.47961 6.18205
3.67390 3.49727 6.81792
3.42662 3.55026 7.73639
3.37363 3.58559 8.30161
3.32064 3.62092 9.04346
3.30298 3.62092 9.78530
3.33831 3.62092 10.49182
3.39130 3.60325 11.48095
    '''
ps2 = '''
3.37363 3.55026 8.33694
5.72281 3.55026 8.33694
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  3-SMC04
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC04'
root[CON.POS] = CONST.LL
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
3.33831 3.62092 0.47690
3.42662 3.60325 0.77717
3.55026 3.60325 1.02445
3.63858 3.60325 1.30706
3.70923 3.58559 1.66032
3.70923 3.56793 2.11956
3.69157 3.56793 2.61412
3.69157 3.56793 3.46195
3.72689 3.53260 4.38042
3.72689 3.53260 5.12227
3.72689 3.56793 6.14672
3.49727 3.60325 7.80705
3.46195 3.63858 8.54889
3.47961 3.65624 9.22009
3.56793 3.63858 9.99726
3.60325 3.58559 10.77443
3.63858 3.53260 11.51628
    '''
ps2 = '''
3.44429 3.65624 8.72552
6.64129 3.65624 8.72552
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  4-SMC05
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC05'
root[CON.POS] = CONST.LR
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
2.34918 3.39130 0.74185
2.45516 3.40896 1.05978
2.61412 3.44429 1.30706
2.84374 3.53260 1.73097
2.98505 3.56793 2.15489
3.16168 3.63858 2.86141
3.26766 3.70923 3.63858
3.42662 3.77988 4.55705
3.51494 3.77988 5.36955
3.56793 3.79755 6.28803
3.56793 3.79755 7.17118
3.51494 3.76222 8.01900
3.33831 3.74456 8.86683
3.32064 3.72689 9.57335
3.32064 3.70923 10.35052
3.35597 3.65624 11.16302
    '''
ps2 = '''
3.46195 3.77988 7.96601
6.16439 3.70923 7.96601
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  5-SMC06
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC06'
root[CON.POS] = CONST.LL
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
2.96738 3.39130 0.47690
3.10869 3.44429 0.70652
3.28532 3.42662 0.95380
3.32064 3.40896 1.16576
3.37363 3.39130 1.44837
3.42662 3.39130 1.76630
3.49727 3.39130 2.22554
3.56793 3.35597 2.93206
3.60325 3.32064 3.53260
3.65624 3.30298 4.20379
3.74456 3.30298 5.15760
3.81521 3.32064 6.53531
3.86820 3.28532 7.59509
3.83287 3.30298 9.29074
3.76222 3.33831 10.38584
3.70923 3.35597 11.30432
3.72689 3.42662 12.08149
    '''
ps2 = '''
3.85053 3.28532 9.02579
6.49998 3.30298 9.02579
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  6-SMC07
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC07'
root[CON.POS] = CONST.LL
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
3.26766 3.42662 0.49456
3.42662 3.42662 0.95380
3.49727 3.47961 1.44837
3.58559 3.55026 2.19021
3.67390 3.60325 2.93206
3.77988 3.62092 3.99184
3.79755 3.62092 4.66303
3.77988 3.65624 5.51086
3.76222 3.69157 6.57064
3.67390 3.67390 7.84237
3.62092 3.69157 9.07878
3.69157 3.77988 10.24454
3.74456 3.83287 11.26899
3.77988 3.86820 12.15214
    '''
ps2 = '''
3.76222 3.67390 7.84237
6.76493 3.67390 7.84237
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  7-SMC08
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC08'
root[CON.POS] = CONST.LR
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
3.26766 3.74456 0.49456
3.24999 3.69157 0.84782
3.33831 3.58559 1.30706
3.39130 3.55026 1.80163
3.58559 3.56793 2.43749
3.76222 3.53260 3.03804
3.88586 3.58559 3.92119
3.92119 3.60325 4.83966
3.92119 3.60325 5.75814
3.93885 3.62092 6.88857
3.86820 3.67390 8.26628
3.76222 3.60325 9.46737
3.79755 3.60325 10.91573
3.79755 3.60325 12.61138
    '''
ps2 = '''
3.76222 3.60325 9.99726
6.67661 3.53260 9.99726
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  8-SMC09
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC09'
root[CON.POS] = CONST.LR
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
3.24999 2.91440 0.44158
3.26766 2.93206 0.77717
3.35597 2.96738 1.13043
3.47961 2.98505 1.44837
3.51494 3.03804 1.87228
3.58559 3.10869 2.50815
3.65624 3.14401 3.24999
3.72689 3.17934 4.13314
3.76222 3.26766 5.26357
3.69157 3.30298 6.42933
3.69157 3.24999 7.41846
3.62092 3.23233 8.30161
3.55026 3.24999 9.60867
3.60325 3.24999 10.56247
3.51494 3.21467 11.69291
    '''
ps2 = '''
3.58559 3.21467 8.67253
6.80026 3.19700 8.67253
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  9-SMC10
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC10'
root[CON.POS] = CONST.LL
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
2.91440 3.53260 0.42391
3.00271 3.51494 0.81250
3.05570 3.47961 1.30706
3.09103 3.42662 1.80163
3.16168 3.37363 2.40217
3.28532 3.30298 3.32064
3.32064 3.21467 4.20379
3.33831 3.19700 5.15760
3.35597 3.14401 6.32335
3.39130 3.12635 7.59509
3.44429 3.12635 9.57335
3.32064 3.23233 10.95106
3.30298 3.28532 11.94019
    '''
ps2 = '''
3.35597 3.10869 7.80705
6.21738 3.14401 7.80705
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  10-SMC11
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC11'
root[CON.POS] = CONST.LL
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
2.45516 3.32064 0.47690
2.70244 3.26766 1.05978
2.82608 3.28532 1.51902
2.98505 3.30298 2.15489
3.14401 3.33831 3.14401
3.21467 3.30298 4.20379
3.17934 3.30298 5.72281
3.07336 3.39130 7.06520
3.05570 3.40896 7.94835
2.93206 3.46195 9.32606
3.03804 3.55026 10.88041
3.12635 3.58559 12.29345
    '''
ps2 = '''
3.14401 3.37363 7.31248
5.93477 3.33831 7.31248
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  11-SMC12
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC12'
root[CON.POS] = CONST.LR
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
2.87907 2.93206 0.68886
2.87907 2.94972 0.91848
2.94972 2.96738 1.16576
3.03804 3.02037 1.37771
3.12635 3.07336 1.66032
3.23233 3.12635 2.11956
3.24999 3.16168 2.68478
3.17934 3.17934 3.39130
3.10869 3.19700 4.23912
2.94972 3.21467 5.19292
2.84374 3.19700 5.82879
2.77309 3.17934 6.39401
2.75543 3.19700 7.13585
3.00271 3.23233 7.77172
3.21467 3.23233 8.19563
3.33831 3.21467 8.61954
3.35597 3.23233 9.29074
3.28532 3.26766 9.96193
3.14401 3.24999 10.66845
    '''
ps2 = '''
3.44429 3.21467 8.07199
6.25270 3.14401 8.07199
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  12-SMC13
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC13'
root[CON.POS] = CONST.LR
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
5.38722 4.29211 0.68886
5.42254 4.39809 1.02445
5.17526 4.48640 1.55434
5.01629 4.43341 2.29619
5.01629 4.39809 3.24999
4.99863 4.38042 4.27445
5.15760 4.38042 5.44020
5.24591 4.38042 6.42933
5.21059 4.36276 7.59509
5.21059 4.34510 8.97280
5.28124 4.32744 10.13856
5.35189 4.34510 11.19834
5.33423 4.34510 12.22280
    '''
ps2 = '''
5.13993 4.32744 9.06112
2.29619 4.27445 9.06112
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  13-SMC14
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC14'
root[CON.POS] = CONST.LR
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
3.67390 3.44429 0.67119
3.70923 3.42662 0.91848
3.76222 3.42662 1.16576
3.79755 3.40896 1.55434
3.83287 3.39130 2.11956
3.77988 3.37363 2.79075
3.81521 3.33831 3.63858
3.88586 3.32064 4.66303
3.86820 3.32064 5.61683
3.79755 3.33831 6.64129
3.74456 3.35597 7.38313
3.63858 3.44429 8.23096
3.72689 3.49727 8.90215
3.79755 3.58559 9.57335
3.81521 3.58559 10.31519
    '''
ps2 = '''
3.63858 3.46195 8.40759
6.37634 3.42662 8.40759
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  14-SMC15
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC15'
root[CON.POS] = CONST.LL
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
3.62092 3.55026 0.63587
3.62092 3.56793 0.88315
3.62092 3.56793 1.13043
3.62092 3.56793 1.58967
3.67390 3.55026 2.26086
3.74456 3.53260 2.86141
3.83287 3.51494 3.46195
3.92119 3.47961 4.30977
3.99184 3.44429 5.33423
4.08015 3.42662 6.74727
3.99184 3.42662 8.44291
3.95651 3.37363 10.03258
3.99184 3.40896 11.48095
    '''
ps2 = '''
3.86820 3.42662 9.09645
6.76493 3.40896 9.09645
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  15-SMC16
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC16'
root[CON.POS] = CONST.LL
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
3.26766 3.26766 0.58288
3.26766 3.23233 0.88315
3.33831 3.23233 1.20108
3.35597 3.24999 1.73097
3.37363 3.19700 2.26086
3.42662 3.17934 2.96738
3.49727 3.16168 3.77988
3.56793 3.17934 5.01629
3.58559 3.23233 6.25270
3.51494 3.30298 7.77172
3.47961 3.33831 9.11411
3.53260 3.32064 10.03258
3.49727 3.32064 11.16302
    '''
ps2 = '''
3.51494 3.28532 7.77172
6.30569 3.33831 7.77172
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  16-SMC17
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC17'
root[CON.POS] = CONST.LL
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
3.33831 3.47961 0.31793
3.28532 3.46195 0.60054
3.33831 3.49727 0.90081
3.47961 3.55026 1.16576
3.56793 3.55026 1.62500
3.70923 3.60325 2.40217
3.79755 3.62092 3.53260
3.69157 3.63858 4.76901
3.69157 3.67390 6.04075
3.65624 3.65624 7.70107
3.51494 3.63858 10.10324
3.60325 3.60325 11.12769
3.67390 3.62092 12.57606
    '''
ps2 = '''
3.67390 3.67390 8.56656
6.65895 3.67390 8.56656
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  17-SMC18
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC18'
root[CON.POS] = CONST.LL
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
4.38042 4.99863 0.52989
4.39809 4.83966 0.81250
4.52173 4.75135 1.23641
4.61004 4.69836 1.76630
4.64537 4.57472 2.43749
4.66303 4.52173 3.28532
4.62771 4.48640 4.52173
4.34510 4.45108 6.35868
4.02716 4.39809 8.26628
4.30977 4.45108 10.27987
4.66303 4.48640 11.72823
4.83966 4.39809 13.38855
    '''
ps2 = '''
3.92119 4.46874 8.81384
7.54210 4.38042 8.81384
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  18-SMC19
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC19'
root[CON.POS] = CONST.LR
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
4.25678 3.65624 0.42391
4.08015 3.67390 0.77717
4.08015 3.72689 1.41304
4.06249 3.70923 2.43749
4.08015 3.70923 3.39130
4.20379 3.76222 4.55705
4.27445 3.77988 6.14672
4.25678 3.76222 7.91302
4.09782 3.76222 9.43204
4.06249 3.77988 11.41030
    '''
ps2 = '''
4.16847 3.77988 9.90894
1.32473 3.76222 9.90894
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  19-SMC20
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC20'
root[CON.POS] = CONST.LL
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
2.64945 3.65624 0.81250
2.75543 3.63858 1.13043
2.94972 3.53260 1.69565
3.03804 3.42662 2.26086
3.03804 3.24999 3.00271
2.98505 3.14401 3.95651
2.91440 3.07336 4.76901
2.66711 3.00271 5.86412
2.49048 2.96738 6.88857
2.45516 2.94972 7.66574
2.54347 2.96738 8.69020
2.66711 3.02037 9.53802
2.98505 3.09103 10.59780
3.14401 3.16168 11.83421
3.24999 3.21467 12.54073
3.24999 3.23233 13.35323
    '''
ps2 = '''
2.61412 3.02037 9.27308
6.25270 3.49727 9.27308
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  20-SMC22
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC22'
root[CON.POS] = CONST.LR
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
3.69157 3.30298 0.67119
3.69157 3.26766 0.88315
3.77988 3.17934 1.48369
3.81521 3.16168 1.94293
3.81521 3.16168 2.79075
3.83287 3.17934 3.81521
3.74456 3.14401 4.73368
3.72689 3.12635 5.75814
3.74456 3.10869 6.32335
3.76222 3.10869 7.24183
3.70923 3.10869 7.94835
3.67390 3.12635 8.69020
3.62092 3.21467 9.78530
3.65624 3.24999 11.05704
3.69157 3.23233 12.11682
3.69157 3.24999 12.99997
    '''
ps2 = '''
3.60325 3.23233 10.93340
6.46466 3.26766 10.93340
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  21-SMC23
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC23'
root[CON.POS] = CONST.LR
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
4.13314 4.30977 0.67119
4.11548 4.32744 0.95380
4.02716 4.25678 1.37771
3.92119 4.09782 1.97826
3.92119 3.95651 2.57880
3.92119 3.83287 3.24999
3.86820 3.67390 4.23912
3.92119 3.60325 5.29890
3.90352 3.69157 6.42933
4.02716 3.77988 8.08965
4.04483 3.81521 9.43204
3.93885 3.81521 10.63313
3.92119 3.86820 11.58693
3.81521 3.85053 12.71736
3.81521 3.86820 13.56518
    '''
ps2 = '''
4.11548 3.77988 9.23775
1.23641 3.74456 9.23775
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  22-SMC24
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC24'
root[CON.POS] = CONST.LL
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
3.32064 3.10869 0.63587
3.33831 3.10869 0.91848
3.35597 3.07336 1.37771
3.37363 3.10869 1.76630
3.32064 3.10869 2.57880
3.42662 3.09103 3.70923
3.44429 3.07336 4.83966
3.60325 3.14401 6.11140
3.77988 3.12635 7.80705
3.55026 3.10869 9.11411
3.49727 3.05570 10.17389
3.44429 3.05570 10.91573
3.42662 3.05570 11.69291
    '''
ps2 = '''
3.56793 3.14401 8.63721
6.05841 3.12635 8.63721
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  23-SMC25
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC25'
root[CON.POS] = CONST.LL
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
3.81521 3.86820 0.58288
3.85053 3.85053 0.81250
3.77988 3.79755 1.16576
3.74456 3.79755 1.48369
3.86820 3.85053 2.15489
3.88586 3.90352 2.93206
3.95651 3.95651 4.30977
4.02716 3.95651 5.65216
4.09782 3.92119 6.71194
4.08015 3.90352 7.80705
4.00950 3.88586 8.69020
3.97418 3.88586 9.96193
3.95651 3.88586 11.16302
    '''
ps2 = '''
3.88586 3.86820 9.41438
6.46466 3.77988 9.41438
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  24-SMC27
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC27'
root[CON.POS] = CONST.LR
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
2.70244 3.14401 0.95380
2.73777 3.12635 1.05978
2.79075 3.10869 1.34239
2.96738 3.19700 2.08423
3.07336 3.24999 2.61412
3.17934 3.33831 3.39130
3.32064 3.42662 4.55705
3.28532 3.46195 5.75814
3.35597 3.40896 7.34781
3.33831 3.30298 9.36139
3.46195 3.23233 10.98639
3.39130 3.21467 12.64671
    '''
ps2 = '''
3.44429 3.23233 10.29753
6.07607 3.23233 10.29753
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  25-SMC28
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC28'
root[CON.POS] = CONST.LR
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
2.96738 3.63858 0.75951
3.09103 3.63858 0.93614
3.30298 3.67390 1.23641
3.42662 3.67390 1.69565
3.60325 3.60325 2.57880
3.74456 3.53260 3.67390
3.74456 3.40896 5.12227
3.77988 3.35597 6.32335
3.79755 3.40896 7.70107
3.70923 3.46195 9.57335
3.53260 3.58559 11.12769
3.49727 3.62092 12.47008
    '''
ps2 = '''
3.77988 3.49727 9.39672
6.72960 3.47961 9.39672
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)

###########
#  26-SMC30
# 
root = range(ELEM_COUNT)
root[CON.NAME] = 'SMC30'
root[CON.POS] = CONST.LL
root[CON.NOTE] = 'Single canal, no lingual canal'
root[CON.FURCATION_POS_B] = 0
root[CON.FURCATION_POS_L] = 0
root[CON.CANAL_TYPE] = 0

ps1 = '''
4.68070 4.09782 0.93614
4.64537 4.06249 1.04212
4.66303 4.08015 1.27174
4.62771 4.13314 1.62500
4.53939 4.16847 1.97826
4.50407 4.18613 2.54347
4.50407 4.20379 3.32064
4.59238 4.20379 3.99184
4.62771 4.20379 4.80434
4.89265 4.27445 5.75814
4.98097 4.30977 7.06520
4.96330 4.36276 8.61954
4.98097 4.34510 9.89128
4.92798 4.32744 11.05704
4.85733 4.39809 11.79888
4.83966 4.30977 12.89399
    '''
ps2 = '''
4.94564 4.34510 9.67932
1.96059 4.32744 9.67932
    '''
root[CON.BOUNDING_BOX] = bounding_box_range 
root[CON.CANAL_PATH] = directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+canal_suffix
root[CON.BODY_PATH] =  directory_name+root[CON.NAME].strip()+'/'+root[CON.NAME].strip()+body_suffix #'v3d/MN01/MN01-solid-body-zoff.v3d'
root[CON.PS1] = du.convert_to_points(ps1)
root[CON.PS2] = du.shift_points(root[CON.PS1], ps2)
roots.append(root)





