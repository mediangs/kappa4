# -*- coding: cp949 -*-
'''
Created on 2014. 4. 9.

@author: jongki
'''

from __future__ import division

import helpers_contours as du  # collection of utility function
from specimens.class_specimen import Specimen

roots = []
bounding_box_range = [(-5, 11), (-5, 11), (-2, 14)] # [(-4, 12), (-4, 12), (-2, 14)]
directory_name = 'E:/0.jongki.data/Dropbox/15.Develop/tooth-data/v3d_mn/'
canal_suffix = '-canal-zoff.v3d'
body_suffix = '-solid-body-zoff.v3d'

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


s = Specimen('MN01')
s.location = CONST.LL
s.note='13-3-19-check all'
s.furcation_pos_1 = 7.5 
s.furcation_pos_2 = 8.8 
s.canal_type = 2
ps1 = '''
    4.96548 3.38989 1.05039 
    4.88590 3.31032 1.41643 
    4.98139 3.15117 1.98937 
    5.29969 3.02385 2.97610 
    5.64982 2.97610 3.50130 
    5.90446 2.88061 4.24930 
    6.14319 2.81695 4.99731 
    6.38191 2.75329 6.06361 
    6.50923 2.83287 7.09809 
    6.46149 3.05568 8.13256 
    6.52515 3.37398 8.99198 
    6.63655 3.50130 9.37393 
'''
ps2 = '''
    4.94956 3.37398 1.05039 
    4.88590 3.26257 1.49601 
    4.98139 3.11934 2.16444 
    4.85407 2.99202 3.23074 
    4.34479 2.80104 4.58352 
    4.18565 2.70555 5.52250 
    3.88326 2.62597 6.66838 
    3.93100 2.70555 7.57554 
    4.24930 3.16708 8.83282 
    4.24930 3.54904 9.73998 
    4.15381 3.70819 10.10602 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN02')
s.location = CONST.LL
s.note='13-3-19-check all'
s.furcation_pos_1 = 10.6 
s.furcation_pos_2 = 9.4 
s.canal_type = 3
ps1 = '''
    6.39783 3.46947 0.65251 
    6.28642 3.35806 1.09813 
    6.22276 3.31032 1.40052 
    6.19093 3.10342 1.71882 
    6.28642 2.97610 2.19627 
    6.47740 2.88061 2.72146 
    6.79570 2.75329 3.45355 
    7.27315 2.46682 4.85407 
    7.48005 2.35542 6.55698 
    7.54371 2.48274 8.11665 
    7.38456 2.76921 9.73998 
    7.16175 3.15117 11.31556 
    7.33681 3.43764 12.54102 
'''
ps2 = '''
    2.67372 3.24666 1.46418 
    2.65780 3.23074 1.87797 
    2.65780 3.11934 2.48274 
    2.67372 2.91245 3.54904 
    2.68963 2.65780 4.56760 
    2.73738 2.40317 5.57025 
    3.08751 2.24401 6.63655 
    3.26257 2.27584 7.44822 
    3.51721 2.40317 8.43495 
    3.64453 2.62597 9.53308 
    3.94692 2.99202 10.69488 
    4.21747 3.29440 11.63386 
    4.34479 3.42172 12.50919 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN03')
s.location = CONST.LL
s.note='13-3-19-apex는 확인, coronal 확인중 crash'
s.furcation_pos_1 = 9.1 
s.furcation_pos_2 = 8.5 
s.canal_type = 3
ps1 = '''
    4.39254 2.25993 0.65251 
    4.42437 2.38725 1.16179 
    4.37662 2.51457 1.84614 
    4.21747 2.61006 2.78512 
    4.09015 2.73738 3.48538 
    4.09015 2.81695 4.37662 
    4.15381 2.80104 5.61799 
    4.09015 2.78512 6.65247 
    3.97875 2.54640 8.21214 
    4.20156 2.02120 9.99462 
    4.09015 1.32094 11.41105 
'''
ps2 = '''
    6.17502 2.16444 1.41643 
    6.31825 2.48274 1.79839 
    6.47740 2.70555 2.35542 
    6.52515 2.88061 3.05568 
    6.68430 2.86470 4.10607 
    6.47740 2.84878 5.93629 
    6.58881 2.78512 6.82753 
    6.66838 2.56231 7.90975 
    6.62064 2.27584 9.07155 
    6.27051 1.86205 10.42433 
    6.28642 1.54375 11.25190 
    6.60472 1.17771 11.95216 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN04')
s.location = CONST.LL
s.note='13-3-19-apex check, coronal crash, direction???'
s.furcation_pos_1 = 9.7 
s.furcation_pos_2 = 9.8 
s.canal_type = 2
ps1 = '''
    5.26786 2.68963 0.85941 
    5.37927 2.84878 1.67107 
    5.36335 2.92836 3.02385 
    5.09280 3.02385 4.15381 
    4.36071 3.26257 5.93629 
    3.88326 3.37398 7.46413 
    3.83551 3.40581 8.40312 
    3.91509 3.23074 9.69223 
    4.07424 2.86470 10.77446 
    3.94692 2.51457 11.72935 
'''
ps2 = '''
    5.28378 2.70555 0.87532 
    5.47476 2.89653 2.03712 
    5.87263 2.96019 3.26257 
    6.38191 3.15117 4.91773 
    6.79570 3.24666 5.85672 
    7.14583 3.31032 6.92302 
    7.14583 3.15117 9.27844 
    6.95485 2.84878 10.34475 
    6.90711 2.54640 11.63386 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN06')
s.location = CONST.LL
s.note='13-3-19-apex check, coronal spot check'
s.furcation_pos_1 = 8.0 
s.furcation_pos_2 = 7.7 
s.canal_type = 2
ps1 = '''
    6.01587 3.37398 1.09813 
    6.04770 3.08751 1.49601 
    6.09544 2.75329 2.21218 
    6.11136 2.45091 3.56496 
    6.15910 2.40317 5.10871 
    6.46149 2.53048 6.70021 
    6.60472 2.84878 8.13256 
    6.01587 3.05568 8.84874 
    5.92038 3.38989 9.62857 
    6.07953 3.66045 10.28109 
'''
ps2 = '''
    5.33152 3.11934 0.81166 
    5.47476 3.05568 1.19362 
    5.55433 2.83287 1.83022 
    5.41110 2.53048 2.83287 
    5.29969 2.43499 3.51721 
    5.01322 2.40317 5.09280 
    4.74267 2.51457 6.31825 
    4.59943 2.83287 7.71877 
    4.82224 3.11934 8.64185 
    5.14054 3.40581 9.48534 
    5.18829 3.85143 10.47207 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN10')
s.location = CONST.LR
s.note='13-3-19-check all'
s.furcation_pos_1 = 10.2 
s.furcation_pos_2 = 10.2 
s.canal_type = 2
ps1 = '''
    4.77450 4.10607 0.62068 
    4.85407 3.94692 1.03447 
    4.88590 3.72411 1.57558 
    4.72675 3.56496 2.11670 
    4.56760 3.45355 2.59414 
    4.64718 3.24666 3.29440 
    4.55169 3.05568 4.13790 
    4.44028 2.86470 5.01322 
    4.36071 2.70555 5.80897 
    4.29705 2.56231 6.70021 
    4.23339 2.48274 7.63920 
    4.55169 2.61006 8.89648 
    5.01322 2.88061 9.77181 
    5.52250 3.23074 10.64713 
'''
ps2 = '''
    5.37927 4.09015 0.41379 
    5.42701 4.01058 0.85941 
    5.63391 3.85143 1.55967 
    5.87263 3.78777 1.97346 
    6.01587 3.62862 2.49865 
    6.07953 3.34215 3.42172 
    6.09544 3.10342 4.23339 
    6.09544 2.84878 5.17237 
    6.23868 2.62597 6.23868 
    6.62064 2.48274 7.43230 
    6.89119 2.54640 8.27580 
    6.90711 2.72146 9.15112 
    6.74796 3.00793 10.02645 
    6.55698 3.37398 10.74262 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN11')
s.location = CONST.LL
s.note='13-3-19-check all'
s.furcation_pos_1 = 9.1 
s.furcation_pos_2 = 8.2 
s.canal_type = 3
ps1 = '''
    4.56760 2.46682 0.84349 
    4.55169 2.78512 1.52784 
    4.47211 3.03976 2.05303 
    4.53577 3.34215 3.07159 
    4.56760 3.54904 4.15381 
    4.90182 3.59679 5.80897 
    4.83816 3.56496 6.90711 
    4.58352 3.45355 8.00524 
    4.74267 3.24666 9.40576 
    4.80633 3.05568 10.74262 
    4.98139 2.89653 11.33148 
'''
ps2 = '''
    6.30234 1.98937 0.84349 
    6.27051 2.14852 1.27320 
    6.28642 2.43499 1.73473 
    6.44557 2.84878 2.67372 
    6.55698 3.16708 3.75594 
    6.54106 3.37398 5.02914 
    6.47740 3.37398 6.90711 
    6.73204 3.23074 8.11665 
    6.70021 3.10342 9.08746 
    6.79570 2.83287 10.39249 
    6.97077 2.72146 10.98135 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN12')
s.location = CONST.LL
s.note='13-3-19-check all'
s.furcation_pos_1 = 8.1 
s.furcation_pos_2 = 8.9 
s.canal_type = 2
ps1 = '''
    6.09544 4.47211 0.57294 
    6.19093 4.18565 1.48009 
    6.81162 4.07424 2.67372 
    7.12992 3.97875 3.62862 
    7.43230 3.77185 4.77450 
    7.43230 3.53313 5.64982 
    7.51188 3.66045 6.62064 
    7.28907 3.83551 7.48005 
    7.43230 4.36071 8.46678 
    7.17766 4.59943 9.26253 
    7.19358 4.86999 10.31292 
'''
ps2 = '''
    6.09544 4.47211 0.57294 
    5.88855 4.12198 1.63924 
    5.17237 3.69228 2.81695 
    4.94956 3.53313 3.43764 
    4.75858 3.34215 4.53577 
    4.66309 3.27849 5.93629 
    4.75858 3.29440 6.92302 
    4.90182 3.61270 7.92567 
    5.22012 4.13790 8.91240 
    5.60208 4.93365 10.18560 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN15')
s.location = CONST.LL
s.note='13-3-19-check all'
s.furcation_pos_1 = 8.1 
s.furcation_pos_2 = 8.1 
s.canal_type = 3
ps1 = '''
    7.30498 5.44293 0.71617 
    7.33681 5.06097 1.49601 
    7.25724 4.71084 2.32359 
    7.24132 4.13790 3.69228 
    7.49596 3.81960 4.85407 
    7.44822 3.69228 5.84080 
    7.28907 3.62862 6.74796 
    6.98668 3.70819 8.38720 
    6.70021 3.88326 9.42168 
    6.35008 3.96283 10.59939 
'''
ps2 = '''
    4.86999 5.14054 0.42970 
    4.85407 5.04505 1.16179 
    4.77450 4.86999 1.87797 
    4.69492 4.45620 2.89653 
    4.71084 4.04241 4.12198 
    4.59943 3.85143 5.04505 
    4.66309 3.77185 5.79306 
    4.75858 3.75594 7.12992 
    4.85407 3.78777 8.18031 
    4.85407 3.99466 9.62857 
    4.40846 4.15381 11.01318 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN16')
s.location = CONST.LR
s.note='check Buccal, lingual'
s.furcation_pos_1 = 9.6 
s.furcation_pos_2 = 9.4 
s.canal_type = 3
ps1 = '''
    5.20421 4.98139 1.05039 
    5.22012 4.55169 1.35277 
    5.36335 4.05833 2.10078 
    5.79306 3.81960 2.92836 
    6.09544 3.62862 3.91509 
    6.39783 3.32623 5.42701 
    6.60472 3.40581 7.25724 
    6.58881 3.64453 9.00789 
    6.82753 4.04241 10.82220 
    7.24132 4.16973 11.64978 
'''
ps2 = '''
    4.47211 4.96548 0.57294 
    4.45620 4.72675 0.84349 
    4.42437 4.42437 1.30503 
    4.24930 4.04241 1.95754 
    4.12198 3.70819 2.75329 
    4.18565 3.53313 3.54904 
    4.21747 3.16708 5.23603 
    4.18565 3.16708 6.77979 
    4.09015 3.42172 8.40312 
    4.02649 3.69228 9.77181 
    4.07424 3.93100 10.85403 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN17')
s.location = CONST.LL
s.note='check all, direction???'
s.furcation_pos_1 = 11.2 
s.furcation_pos_2 = 9.7 
s.canal_type = 3
ps1 = '''
    5.53842 4.99731 0.57294 
    5.64982 4.93365 1.12996 
    6.12727 4.79041 2.13261 
    6.54106 4.53577 3.00793 
    7.00260 4.10607 4.32888 
    7.54371 3.66045 6.58881 
    8.06890 3.72411 8.83282 
    8.19623 3.97875 10.44024 
    8.21214 4.31296 12.01583 
    8.29171 4.48803 12.90706 
'''
ps2 = '''
    4.18565 4.55169 1.49601 
    4.48803 4.56760 2.03712 
    4.58352 4.39254 2.80104 
    4.50394 4.10607 3.66045 
    4.48803 3.78777 4.82224 
    4.31296 3.53313 6.12727 
    4.34479 3.42172 7.32090 
    4.31296 3.42172 8.27580 
    4.42437 3.58087 9.69223 
    4.74267 3.94692 11.06092 
    4.93365 4.15381 12.30229 
    4.98139 4.31296 13.05030 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN19')
s.location = CONST.LL
s.note='check all'
s.furcation_pos_1 = 9.7 
s.furcation_pos_2 = 9.4 
s.canal_type = 2
ps1 = '''
    5.41110 4.32888 1.19362 
    5.60208 3.96283 1.43235 
    5.95221 3.81960 1.79839 
    6.30234 3.69228 2.61006 
    6.57289 3.56496 4.32888 
    6.81162 3.59679 6.23868 
    6.84345 3.66045 7.65511 
    6.98668 3.86734 9.11929 
    6.81162 4.16973 10.40841 
    6.70021 4.50394 11.58612 
    6.79570 4.74267 12.33412 
'''
ps2 = '''
    5.41110 4.31296 1.19362 
    5.49067 3.96283 1.44826 
    5.39518 3.74002 1.83022 
    5.29969 3.43764 2.72146 
    5.23603 3.24666 4.44028 
    5.06097 3.24666 5.98404 
    5.17237 3.45355 8.24397 
    5.36335 3.89917 10.47207 
    5.28378 4.36071 11.68161 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN23')
s.location = CONST.LL
s.note='check all'
s.furcation_pos_1 = 8.4 
s.furcation_pos_2 = 7.6 
s.canal_type = 3
ps1 = '''
    6.50923 3.69228 0.98673 
    6.54106 3.38989 1.48009 
    6.55698 3.03976 2.24401 
    6.36600 2.78512 3.18300 
    6.47740 2.68963 4.34479 
    6.93894 2.73738 5.96812 
    7.03443 2.86470 7.06626 
    6.77979 2.99202 7.67103 
    6.58881 3.31032 9.10338 
    6.57289 3.51721 9.91504 
'''
ps2 = '''
    5.01322 3.45355 1.14588 
    5.07688 3.18300 1.60741 
    5.14054 2.91245 2.32359 
    5.12463 2.72146 3.18300 
    4.91773 2.62597 4.32888 
    4.48803 2.64189 5.85672 
    4.45620 2.91245 7.28907 
    4.69492 3.16708 8.38720 
    4.48803 3.50130 9.59674 
    4.18565 3.62862 10.13785 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN24')
s.location = CONST.LR
s.note='check all'
s.furcation_pos_1 = 8.1 
s.furcation_pos_2 = 7.6 
s.canal_type = 3
ps1 = '''
    4.98139 3.89917 1.19362 
    4.94956 3.62862 1.60741 
    4.88590 3.35806 2.14852 
    4.99731 3.19891 2.64189 
    4.94956 2.99202 3.77185 
    4.69492 2.96019 5.12463 
    4.29705 3.18300 6.66838 
    4.36071 3.62862 8.24397 
    4.64718 4.29705 10.07420 
'''
ps2 = '''
    6.12727 3.88326 1.12996 
    6.11136 3.62862 1.59150 
    6.09544 3.24666 2.45091 
    6.27051 3.05568 3.56496 
    6.73204 2.99202 4.86999 
    7.11400 3.29440 6.92302 
    7.00260 3.59679 8.06890 
    7.05034 4.10607 9.43760 
    7.27315 4.37662 10.23335 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN25')
s.location = CONST.LL
s.note='ck all'
s.furcation_pos_1 = 9.4 
s.furcation_pos_2 = 9.8 
s.canal_type = 3
ps1 = '''
    7.05034 5.01322 1.00265 
    7.03443 4.91773 1.62333 
    7.09809 4.56760 2.54640 
    7.19358 4.07424 3.59679 
    7.38456 3.46947 5.01322 
    7.54371 3.24666 6.76387 
    7.38456 3.34215 8.18031 
    7.19358 3.64453 9.21478 
    7.03443 3.97875 10.24926 
    6.90711 4.40846 11.20416 
'''
ps2 = '''
    3.11934 4.80633 0.47745 
    3.18300 4.90182 0.76392 
    3.26257 4.91773 1.43235 
    3.59679 4.50394 2.40317 
    3.93100 4.16973 3.26257 
    4.29705 3.54904 4.63127 
    4.28113 3.18300 6.14319 
    4.18565 3.24666 7.73469 
    4.34479 3.53313 9.13521 
    3.99466 4.01058 10.53573 
    3.58087 4.26522 11.52246 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN26')
s.location = CONST.LL
s.note='check all, direction ??'
s.furcation_pos_1 = 9.3 
s.furcation_pos_2 = 9.5 
s.canal_type = 2
ps1 = '''
    7.40047 1.83022 1.75065 
    6.85936 2.67372 3.08751 
    6.36600 3.26257 4.20156 
    5.55433 3.77185 5.18829 
    5.01322 4.01058 6.19093 
    4.69492 3.91509 7.65511 
    4.77450 3.66045 8.96014 
    4.82224 3.27849 10.28109 
    4.72675 2.97610 11.09275 
'''
ps2 = '''
    7.38456 1.83022 1.75065 
    6.97077 2.46682 2.73738 
    6.82753 2.99202 3.89917 
    7.03443 3.72411 5.26786 
    7.33681 4.09015 6.50923 
    7.70286 4.26522 8.11665 
    7.41639 4.05833 9.53308 
    7.12992 3.74002 10.55164 
    6.93894 3.43764 11.64978 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN27')
s.location = CONST.LR
s.note='ck all'
s.furcation_pos_1 = 9.8 
s.furcation_pos_2 = 7.8 
s.canal_type = 3
ps1 = '''
    4.72675 4.47211 0.73209 
    4.83816 4.32888 1.22546 
    4.93365 4.02649 1.87797 
    4.72675 3.75594 2.91245 
    4.48803 3.61270 3.93100 
    4.23339 3.51721 5.36335 
    4.02649 3.54904 6.71613 
    3.97875 3.70819 7.89384 
    4.21747 4.10607 9.64449 
    4.48803 4.36071 10.36066 
    4.45620 4.47211 10.98135 
'''
ps2 = '''
    6.85936 4.59943 0.82758 
    7.00260 4.40846 1.32094 
    7.11400 4.16973 1.73473 
    7.19358 3.80368 2.80104 
    7.38456 3.72411 4.37662 
    7.62328 3.74002 5.76123 
    7.79835 3.86734 7.16175 
    7.79835 4.09015 8.33946 
    7.54371 4.31296 9.54900 
    7.52779 4.53577 10.29700 
    7.67103 4.69492 11.20416 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN28')
s.location = CONST.LR
s.note='check all , direction ?'
s.furcation_pos_1 = 9.1 
s.furcation_pos_2 = 9.2 
s.canal_type = 3
ps1 = '''
    4.59943 5.01322 0.81166 
    4.58352 4.69492 1.25729 
    4.40846 4.20156 2.10078 
    4.34479 3.88326 3.19891 
    4.36071 3.72411 4.20156 
    4.44028 3.61270 5.82489 
    5.06097 3.75594 8.32354 
    5.61799 3.91509 9.42168 
    5.76123 4.09015 10.36066 
    5.82489 4.34479 11.28373 
'''
ps2 = '''
    7.59145 5.42701 1.32094 
    7.54371 5.33152 1.55967 
    7.46413 4.99731 1.95754 
    7.30498 4.48803 2.59414 
    7.44822 4.07424 3.48538 
    7.48005 3.78777 4.44028 
    7.14583 3.62862 5.82489 
    7.19358 3.61270 6.98668 
    7.25724 3.74002 7.90975 
    6.92302 3.91509 9.08746 
    6.70021 4.21747 10.20151 
    6.79570 4.31296 11.04501 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN29')
s.location = CONST.LR
s.note='ck all'
s.furcation_pos_1 = 9.9 
s.furcation_pos_2 = 9.4 
s.canal_type = 2
ps1 = '''
    6.30234 4.67901 0.74800 
    6.22276 4.45620 1.27320 
    5.98404 4.10607 1.90980 
    5.90446 3.70819 2.80104 
    5.68165 3.31032 3.85143 
    5.45884 3.10342 4.96548 
    5.07688 2.86470 6.65247 
    4.59943 2.86470 8.03707 
    4.39254 2.89653 9.00789 
    4.64718 3.08751 10.18560 
    4.67901 3.27849 11.44288 
'''
ps2 = '''
    6.31825 4.69492 0.74800 
    6.25459 4.50394 1.17771 
    6.09544 4.10607 1.90980 
    6.06361 3.59679 2.94427 
    6.28642 3.27849 4.15381 
    6.50923 3.02385 5.33152 
    6.79570 2.80104 6.90711 
    6.95485 2.78512 8.24397 
    7.08217 2.86470 9.46942 
    6.93894 3.02385 10.42433 
    6.90711 3.24666 11.57021 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN30')
s.location = CONST.LL
s.note='ck all'
s.furcation_pos_1 = 10.0 
s.furcation_pos_2 = 8.7 
s.canal_type = 3
ps1 = '''
    5.10871 2.40317 0.73209 
    5.12463 2.54640 0.97081 
    5.02914 2.78512 1.36869 
    4.82224 3.16708 1.89388 
    4.51986 3.58087 2.73738 
    4.34479 3.81960 3.53313 
    4.20156 4.01058 4.50394 
    4.09015 4.12198 5.41110 
    4.09015 4.20156 6.17502 
    4.04241 4.15381 7.65511 
    3.85143 4.09015 9.05563 
    3.97875 3.99466 10.04236 
    4.15381 3.75594 11.50654 
'''
ps2 = '''
    7.24132 2.49865 1.51193 
    7.19358 2.84878 1.90980 
    7.20949 3.26257 2.61006 
    7.30498 3.46947 3.15117 
    7.43230 3.86734 4.29705 
    7.46413 4.05833 5.25195 
    7.40047 4.13790 6.33417 
    7.40047 4.09015 7.38456 
    7.17766 3.91509 8.70550 
    7.01851 3.69228 9.85138 
    6.90711 3.48538 10.72671 
    6.93894 3.45355 11.42697 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN31')
s.location = CONST.LR
s.note='ck all nice shape'
s.furcation_pos_1 = 10.6 
s.furcation_pos_2 = 9.4 
s.canal_type = 3
ps1 = '''
    4.16973 4.28113 0.38196 
    4.26522 4.13790 0.85941 
    4.18565 3.94692 1.44826 
    4.13790 3.86734 2.02120 
    4.09015 3.69228 2.88061 
    3.85143 3.40581 3.93100 
    3.66045 3.29440 4.77450 
    3.40581 3.31032 5.55433 
    3.23074 3.24666 6.84345 
    3.29440 3.32623 8.21214 
    3.59679 3.61270 9.97870 
    3.99466 3.88326 11.58612 
'''
ps2 = '''
    6.73204 4.20156 0.89124 
    6.71613 4.05833 1.43235 
    6.73204 3.86734 2.08486 
    6.74796 3.69228 2.73738 
    7.00260 3.56496 3.53313 
    7.28907 3.35806 4.48803 
    7.54371 3.19891 5.36335 
    7.75060 3.13525 6.12727 
    8.02116 3.13525 7.20949 
    8.02116 3.27849 8.30763 
    7.79835 3.56496 9.66040 
    7.75060 4.02649 11.74527 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN33')
s.location = CONST.LR
s.note='ck all nice shape'
s.furcation_pos_1 = 10.0 
s.furcation_pos_2 = 9.1 
s.canal_type = 3
ps1 = '''
    6.41374 3.13525 0.50928 
    6.58881 3.15117 0.95490 
    6.92302 3.16708 1.68699 
    7.19358 3.43764 2.64189 
    7.49596 3.64453 3.50130 
    7.70286 3.89917 5.12463 
    7.73469 3.93100 6.50923 
    7.65511 3.88326 8.05299 
    7.40047 3.61270 9.78773 
    7.28907 3.13525 11.31556 
'''
ps2 = '''
    3.53313 3.13525 0.60477 
    3.64453 3.13525 1.11405 
    3.66045 3.29440 1.76656 
    3.74002 3.46947 2.32359 
    3.77185 3.59679 3.07159 
    3.74002 3.80368 3.99466 
    3.81960 4.04241 5.85672 
    3.94692 3.91509 7.68694 
    4.04241 3.46947 9.40576 
    4.12198 3.18300 10.61530 
    4.15381 3.03976 11.39514 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN37')
s.location = CONST.LR
s.note='ck all hypercementosis'
s.furcation_pos_1 = 8.4 
s.furcation_pos_2 = 8.5 
s.canal_type = 3
ps1 = '''
    6.46149 2.14852 1.81431 
    6.57289 2.37133 2.40317 
    6.79570 2.78512 3.16708 
    6.92302 3.07159 3.91509 
    7.14583 3.23074 4.67901 
    7.25724 3.42172 5.72940 
    7.25724 3.51721 6.82753 
    7.41639 3.56496 8.73733 
    7.27315 3.53313 9.58083 
    6.93894 3.50130 10.61530 
    6.57289 3.45355 11.71344 
'''
ps2 = '''
    4.56760 1.68699 0.95490 
    4.64718 1.86205 1.43235 
    4.55169 2.32359 2.19627 
    4.34479 2.76921 3.00793 
    4.09015 3.27849 4.40846 
    4.01058 3.50130 5.92038 
    4.05833 3.56496 7.14583 
    4.10607 3.56496 8.27580 
    4.09015 3.42172 9.81955 
    4.07424 3.32623 10.83811 
    4.01058 3.29440 11.79301 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN38')
s.location = CONST.LL
s.note='ck all'
s.furcation_pos_1 = 10.7 
s.furcation_pos_2 = 10.9 
s.canal_type = 3
ps1 = '''
    5.47476 1.51193 0.62068 
    5.55433 1.67107 1.03447 
    5.53842 1.94163 1.48009 
    5.50659 2.11670 1.86205 
    5.31561 2.27584 2.80104 
    4.96548 2.61006 3.72411 
    4.67901 3.21483 5.44293 
    4.26522 3.58087 7.14583 
    3.91509 3.53313 8.48269 
    3.67636 3.23074 9.93096 
    3.99466 2.96019 10.86995 
    4.16973 2.33950 12.11131 
'''
ps2 = '''
    5.80897 1.63924 0.52519 
    6.09544 1.76656 0.82758 
    6.19093 1.86205 1.06630 
    6.35008 2.08486 1.46418 
    6.50923 2.19627 2.05303 
    6.54106 2.24401 2.68963 
    6.79570 2.49865 3.67636 
    6.84345 2.76921 4.47211 
    6.97077 3.18300 5.49067 
    7.06626 3.62862 7.12992 
    6.92302 3.54904 8.91240 
    6.81162 3.11934 10.66305 
    6.92302 2.70555 12.09540 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN45')
s.location = CONST.LR
s.note='ck all direction ???'
s.furcation_pos_1 = 9.3 
s.furcation_pos_2 = 8.6 
s.canal_type = 3
ps1 = '''
    6.89119 2.67372 1.22546 
    6.95485 2.86470 1.65516 
    6.89119 3.08751 2.18035 
    6.71613 3.21483 2.94427 
    6.57289 3.26257 3.61270 
    6.47740 3.37398 4.12198 
    6.60472 3.43764 4.71084 
    6.60472 3.51721 5.60208 
    6.76387 3.56496 6.70021 
    6.89119 3.61270 7.54371 
    6.92302 3.51721 9.03972 
    6.71613 3.31032 9.85138 
    6.70021 3.07159 10.91769 
    6.79570 2.96019 11.64978 
'''
ps2 = '''
    3.80368 2.62597 1.25729 
    3.88326 2.83287 1.81431 
    3.99466 3.03976 2.35542 
    4.16973 3.08751 3.02385 
    4.31296 3.03976 3.85143 
    4.42437 3.15117 4.91773 
    4.42437 3.16708 6.11136 
    4.32888 3.19891 7.94158 
    4.64718 3.11934 9.45351 
    5.02914 2.96019 10.86995 
    4.93365 2.72146 12.09540 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN46')
s.location = CONST.LL
s.note='ck all'
s.furcation_pos_1 = 7.9 
s.furcation_pos_2 = 8.0 
s.canal_type = 3
ps1 = '''
    6.97077 3.99466 1.28911 
    6.84345 3.83551 1.71882 
    6.66838 3.54904 2.24401 
    6.66838 3.32623 2.73738 
    6.82753 3.10342 3.42172 
    7.06626 2.94427 4.21747 
    7.11400 2.76921 5.37927 
    6.97077 2.62597 6.47740 
    6.93894 2.59414 7.09809 
    6.55698 2.75329 8.73733 
    6.50923 2.86470 9.88321 
    6.55698 2.94427 10.48798 
'''
ps2 = '''
    4.79041 3.31032 1.22546 
    4.61535 3.32623 1.63924 
    4.37662 3.23074 2.16444 
    4.28113 3.13525 2.72146 
    4.12198 3.03976 3.31032 
    4.05833 2.89653 4.02649 
    4.01058 2.70555 5.01322 
    4.13790 2.53048 6.31825 
    4.32888 2.54640 7.67103 
    4.63127 2.78512 8.91240 
    4.74267 3.03976 9.89913 
    4.74267 3.18300 10.44024 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN50')
s.location = CONST.LR
s.note='ck all'
s.furcation_pos_1 = 9.0 
s.furcation_pos_2 = 8.5 
s.canal_type = 3
ps1 = '''
    6.98668 1.16179 0.63660 
    6.97077 1.32094 0.97081 
    7.01851 1.57558 1.59150 
    7.19358 1.89388 2.43499 
    7.27315 2.21218 3.29440 
    7.60737 2.53048 4.42437 
    7.60737 2.81695 5.18829 
    7.76652 2.96019 6.50923 
    7.83018 2.89653 7.76652 
    7.78243 2.72146 8.96014 
    7.43230 2.45091 9.97870 
    7.25724 2.14852 11.14050 
'''
ps2 = '''
    4.69492 0.90715 0.81166 
    4.66309 1.01856 1.11405 
    4.58352 1.28911 1.78248 
    4.42437 1.70290 2.67372 
    4.23339 2.10078 3.67636 
    4.12198 2.45091 4.67901 
    3.99466 2.78512 6.07953 
    4.16973 2.80104 7.38456 
    4.44028 2.64189 8.73733 
    4.67901 2.37133 9.80364 
    4.85407 2.02120 11.01318 
    4.80633 1.92571 11.55429 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN51')
s.location = CONST.LL
s.note='ck all'
s.furcation_pos_1 = 9.1 
s.furcation_pos_2 = 8.6 
s.canal_type = 3
ps1 = '''
    3.27849 2.53048 0.68434 
    3.38989 2.53048 1.22546 
    3.56496 2.61006 2.24401 
    3.50130 2.65780 2.64189 
    3.53313 2.78512 3.46947 
    3.75594 2.97610 4.28113 
    3.94692 3.02385 4.77450 
    3.88326 3.11934 5.55433 
    3.72411 3.15117 6.17502 
    3.61270 3.16708 6.39783 
    3.54904 3.15117 7.08217 
    3.66045 3.11934 8.22805 
    4.07424 2.94427 9.42168 
    4.48803 2.76921 10.36066 
    4.69492 2.61006 11.06092 
'''
ps2 = '''
    5.49067 2.18035 0.63660 
    5.47476 2.21218 1.00265 
    5.52250 2.37133 1.55967 
    5.72940 2.51457 2.05303 
    6.04770 2.59414 2.49865 
    6.33417 2.78512 3.37398 
    6.47740 2.96019 4.36071 
    6.79570 3.07159 5.01322 
    7.03443 3.13525 5.90446 
    7.22541 3.15117 6.70021 
    7.22541 3.13525 7.25724 
    7.17766 2.99202 8.38720 
    6.98668 2.72146 9.29436 
    6.85936 2.56231 10.01053 
    6.95485 2.32359 10.53573 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN52')
s.location = CONST.LR
s.note='check all complex canal direction???'
s.furcation_pos_1 = 9.3 
s.furcation_pos_2 = 8.3 
s.canal_type = 3
ps1 = '''
    7.25724 2.10078 0.92307 
    7.14583 2.24401 1.22546 
    7.14583 2.32359 1.71882 
    7.12992 2.51457 2.57823 
    7.00260 2.61006 3.15117 
    7.16175 2.73738 3.94692 
    7.20949 2.86470 4.55169 
    7.30498 2.89653 5.17237 
    7.14583 3.02385 5.71348 
    6.76387 3.10342 6.36600 
    6.66838 3.05568 6.74796 
    6.47740 3.05568 7.28907 
    6.60472 3.11934 7.87792 
    7.00260 2.86470 8.64185 
    7.00260 2.72146 9.23070 
    6.71613 2.48274 10.13785 
    6.55698 2.29176 10.80628 
'''
ps2 = '''
    4.28113 2.02120 1.46418 
    4.37662 2.24401 1.90980 
    4.48803 2.46682 2.49865 
    4.58352 2.62597 3.10342 
    4.79041 2.80104 3.74002 
    4.74267 2.96019 4.69492 
    4.64718 3.03976 5.55433 
    4.51986 3.11934 6.68430 
    4.31296 3.00793 7.44822 
    4.32888 2.94427 8.02116 
    4.51986 2.75329 9.00789 
    4.74267 2.38725 10.20151 
    4.86999 2.18035 10.77446 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN53')
s.location = CONST.LR
s.note='ck all'
s.furcation_pos_1 = 10.3 
s.furcation_pos_2 = 9.5 
s.canal_type = 3
ps1 = '''
    7.63920 1.35277 0.55702 
    7.76652 1.62333 1.01856 
    7.71877 1.90980 1.67107 
    7.59145 2.35542 2.30767 
    7.62328 2.62597 2.94427 
    7.75060 2.97610 3.75594 
    7.83018 3.24666 4.64718 
    7.68694 3.38989 5.47476 
    7.49596 3.56496 6.46149 
    7.32090 3.70819 7.70286 
    7.17766 3.72411 8.99198 
    6.87528 3.77185 10.09011 
    6.62064 3.66045 11.50654 
'''
ps2 = '''
    3.88326 2.19627 1.54375 
    3.80368 2.29176 1.87797 
    3.72411 2.43499 2.33950 
    3.62862 2.59414 2.83287 
    3.64453 2.80104 3.40581 
    3.56496 2.96019 3.86734 
    3.66045 3.24666 4.58352 
    3.74002 3.51721 5.55433 
    4.02649 3.72411 6.57289 
    4.15381 3.75594 7.28907 
    4.47211 3.81960 8.45086 
    4.82224 3.83551 9.67632 
    5.01322 3.77185 10.51981 
    4.88590 3.45355 12.04765 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN55')
s.location = CONST.LR
s.note='ck all'
s.furcation_pos_1 = 8.0 
s.furcation_pos_2 = 7.4 
s.canal_type = 3
ps1 = '''
    7.32090 1.48009 1.00265 
    7.36864 1.71882 1.28911 
    7.43230 1.97346 1.70290 
    7.46413 2.33950 2.51457 
    7.55962 2.72146 3.72411 
    7.63920 2.86470 4.58352 
    7.63920 2.96019 5.25195 
    7.60737 2.99202 6.01587 
    7.57554 3.00793 7.43230 
    7.54371 2.91245 8.25988 
    7.33681 2.81695 9.08746 
    7.32090 2.51457 10.15377 
'''
ps2 = '''
    4.99731 1.86205 1.83022 
    4.98139 2.21218 2.21218 
    4.86999 2.54640 2.75329 
    4.69492 2.73738 3.40581 
    4.66309 2.86470 4.01058 
    4.63127 2.91245 4.58352 
    4.50394 3.08751 5.53842 
    4.45620 3.10342 6.50923 
    4.50394 3.08751 7.75060 
    4.53577 2.97610 8.80099 
    4.45620 2.84878 9.96279 
    4.29705 2.76921 10.53573 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN58')
s.location = CONST.LL
s.note='#check all'
s.furcation_pos_1 = 11.2 
s.furcation_pos_2 = 10.5 
s.canal_type = 2
ps1 = '''
    4.48803 3.66045 0.70026 
    4.80633 3.58087 1.57558 
    5.17237 3.67636 2.40317 
    5.36335 3.58087 3.03976 
    5.88855 3.40581 4.37662 
    6.19093 3.21483 5.36335 
    6.50923 3.05568 6.31825 
    6.63655 3.03976 8.00524 
    6.76387 3.03976 9.18295 
    6.90711 3.19891 10.72671 
    6.44557 3.38989 11.88850 
    6.36600 3.51721 12.76383 
'''
ps2 = '''
    4.48803 3.62862 0.70026 
    4.64718 3.56496 1.52784 
    4.74267 3.67636 2.45091 
    4.58352 3.32623 4.24930 
    4.61535 3.15117 5.20421 
    4.42437 2.99202 6.09544 
    4.26522 2.89653 7.06626 
    4.31296 2.92836 9.03972 
    4.39254 3.05568 10.12194 
    4.40846 3.24666 11.02910 
    4.50394 3.46947 12.30229 
    4.48803 3.59679 12.92298 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN63')
s.location = CONST.LR
s.note='-'
s.furcation_pos_1 = 8.7 
s.furcation_pos_2 = 8.1 
s.canal_type = 2
ps1 = '''
    5.90446 4.55169 0.70026 
    5.88855 4.24930 1.41643 
    5.72940 3.88326 2.11670 
    5.58616 3.58087 2.75329 
    5.07688 3.34215 3.46947 
    4.74267 3.15117 4.48803 
    4.71084 3.05568 5.87263 
    4.47211 3.15117 7.24132 
    4.51986 3.27849 8.11665 
    4.72675 3.43764 9.37393 
    5.41110 3.51721 10.31292 
    5.74531 3.61270 10.90177 
'''
ps2 = '''
    5.90446 4.53577 0.70026 
    5.92038 4.31296 1.27320 
    5.92038 3.70819 2.54640 
    6.06361 3.37398 3.53313 
    6.62064 3.18300 4.51986 
    7.03443 3.07159 5.42701 
    7.22541 3.02385 6.54106 
    7.28907 3.16708 8.02116 
    7.38456 3.27849 9.46942 
    7.75060 3.50130 10.48798 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN64')
s.location = CONST.LL
s.note=''
s.furcation_pos_1 = 9.6 
s.furcation_pos_2 = 9.2 
s.canal_type = 2
ps1 = '''
    6.58881 1.95754 0.85941 
    6.46149 2.03712 1.14588 
    6.03178 2.24401 1.68699 
    5.69757 2.32359 2.02120 
    5.04505 2.56231 3.05568 
    4.50394 2.76921 4.40846 
    4.13790 3.00793 6.25459 
    4.05833 3.03976 7.62328 
    4.12198 3.02385 8.67367 
    4.32888 2.73738 9.85138 
    4.21747 2.54640 10.75854 
'''
ps2 = '''
    6.57289 1.95754 0.85941 
    6.65247 2.16444 1.49601 
    6.98668 2.38725 2.38725 
    7.17766 2.75329 3.51721 
    7.12992 3.15117 4.90182 
    7.09809 3.35806 6.33417 
    6.93894 3.29440 7.81426 
    6.76387 3.15117 9.02380 
    6.70021 2.78512 10.15377 
    6.76387 2.62597 10.66305 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN66')
s.location = CONST.LL
s.note='#check all'
s.furcation_pos_1 = 9.2 
s.furcation_pos_2 = 8.7 
s.canal_type = 2
ps1 = '''
    5.68165 1.86205 1.75065 
    5.76123 1.78248 2.10078 
    5.79306 1.81431 2.45091 
    5.79306 2.14852 3.00793 
    5.69757 2.72146 3.99466 
    5.37927 3.05568 4.79041 
    4.79041 3.23074 5.74531 
    4.48803 3.27849 6.54106 
    4.05833 3.21483 7.63920 
    4.02649 2.89653 9.18295 
    4.07424 2.51457 10.58347 
    3.86734 2.16444 11.71344 
'''
ps2 = '''
    5.68165 1.84614 1.75065 
    5.79306 1.78248 2.16444 
    5.85672 1.86205 2.59414 
    5.93629 2.24401 3.32623 
    5.96812 2.88061 4.40846 
    6.17502 3.11934 5.12463 
    6.39783 3.24666 6.01587 
    6.93894 3.34215 7.46413 
    6.82753 3.19891 8.46678 
    6.44557 2.84878 9.70815 
    6.09544 2.49865 10.83811 
    6.04770 2.25993 11.44288 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

    
s = Specimen('MN67')
s.location = CONST.LR
s.note=''
s.furcation_pos_1 = 9.2 
s.furcation_pos_2 = 8.7 
s.canal_type = 2
ps1 = '''
    7.06626 2.21218 0.82758 
    6.92302 2.37133 1.51193 
    6.85936 2.68963 2.59414 
    7.00260 2.78512 3.64453 
    7.20949 2.88061 5.09280 
    6.60472 2.91245 6.65247 
    6.74796 2.73738 7.79835 
    7.05034 2.56231 8.51452 
    7.05034 2.29176 10.05828 
    7.11400 1.98937 11.14050 
'''
ps2 = '''
    7.05034 2.21218 0.82758 
    6.82753 2.41908 1.75065 
    6.66838 2.62597 2.76921 
    6.27051 2.73738 3.69228 
    5.34744 2.86470 5.17237 
    5.58616 2.88061 6.58881 
    5.26786 2.75329 7.79835 
    5.06097 2.54640 9.00789 
    4.88590 2.32359 10.21743 
    4.66309 2.10078 11.29965 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)

        