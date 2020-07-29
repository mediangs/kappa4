'''
Created on 2014. 4. 9.

@author: jongki

data from chang
mandibular incisors

'''

# -*- coding: cp949 -*-


from __future__ import division

import dist_util as du  # collection of utility function
from specimens.class_specimen import Specimen

roots = []
bounding_box_range = [(-10, 20), (-10, 20), (-10, 20)]
directory_name = 'E:/0.jongki.data/Dropbox/15.Develop/tooth-data/v3d_smc/'
canal_suffix = '-canal-zoff.v3d'
body_suffix = '-solid-body-zoff.v3d'
ELEM_COUNT = 11


s = Specimen('SMC01')
s.location = CONST.LR
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    5.82879 3.77989 0.44158 
    5.84645 3.67391 0.65353 
    6.00542 3.62092 1.16576 
    6.12906 3.60326 1.88994 
    6.21738 3.60326 2.75543 
    6.21738 3.69157 4.08015 
    6.12906 3.65624 5.47553 
    6.09374 3.63858 6.62363 
    6.04075 3.67391 7.64808 
    6.00542 3.67391 8.16031 
    6.02308 3.67391 8.88449 
    6.07607 3.70923 9.53802 
    6.12906 3.76222 10.13856 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC02')
s.location = CONST.LL
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    6.07607 4.29211 0.52989 
    6.05841 4.11548 1.11277 
    6.02308 4.02716 1.60733 
    6.05841 4.00950 2.38451 
    6.12906 4.00950 3.30298 
    6.16438 4.00950 4.29211 
    6.25270 4.02716 5.29890 
    6.27036 3.99184 6.42933 
    6.23504 3.99184 7.36547 
    6.23504 3.88586 8.33694 
    6.21737 3.85053 9.53802 
    6.09373 3.86820 10.50949 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC03')
s.location = CONST.LR
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    6.09374 3.35597 1.48369 
    6.14673 3.33831 1.87228 
    6.27037 3.33831 2.43749 
    6.35868 3.33831 3.14401 
    6.30569 3.40896 4.20379 
    6.14673 3.44429 5.26357 
    6.12906 3.47961 6.18205 
    6.02308 3.49727 6.81792 
    5.77580 3.55026 7.73639 
    5.72281 3.58559 8.30161 
    5.66982 3.62092 9.04346 
    5.65216 3.62092 9.78530 
    5.68749 3.62092 10.49182 
    5.74048 3.60325 11.48095 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC04')
s.location = CONST.LL
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    6.53531 3.62092 0.47690 
    6.62362 3.60325 0.77717 
    6.74726 3.60325 1.02445 
    6.83558 3.60325 1.30706 
    6.90623 3.58559 1.66032 
    6.90623 3.56793 2.11956 
    6.88857 3.56793 2.61412 
    6.88857 3.56793 3.46195 
    6.92389 3.53260 4.38042 
    6.92389 3.53260 5.12227 
    6.92389 3.56793 6.14672 
    6.69427 3.60325 7.80705 
    6.65895 3.63858 8.54889 
    6.67661 3.65624 9.22009 
    6.76493 3.63858 9.99726 
    6.80025 3.58559 10.77443 
    6.83558 3.53260 11.51628 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC05')
s.location = CONST.LR
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    5.05162 3.32065 0.74185 
    5.15760 3.33831 1.05978 
    5.31656 3.37364 1.30706 
    5.54618 3.46195 1.73097 
    5.68749 3.49728 2.15489 
    5.86412 3.56793 2.86141 
    5.97010 3.63858 3.63858 
    6.12906 3.70923 4.55705 
    6.21738 3.70923 5.36955 
    6.27037 3.72690 6.28803 
    6.27037 3.72690 7.17118 
    6.21738 3.69157 8.01900 
    6.04075 3.67391 8.86683 
    6.02308 3.65624 9.57335 
    6.02308 3.63858 10.35052 
    6.05841 3.58559 11.16302 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC06')
s.location = CONST.LL
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    5.61683 3.40896 0.47690 
    5.75814 3.46195 0.70652 
    5.93477 3.44428 0.95380 
    5.97009 3.42662 1.16576 
    6.02308 3.40896 1.44837 
    6.07607 3.40896 1.76630 
    6.14672 3.40896 2.22554 
    6.21738 3.37363 2.93206 
    6.25270 3.33830 3.53260 
    6.30569 3.32064 4.20379 
    6.39401 3.32064 5.15760 
    6.46466 3.33830 6.53531 
    6.51765 3.30298 7.59509 
    6.48232 3.32064 9.29074 
    6.41167 3.35597 10.38584 
    6.35868 3.37363 11.30432 
    6.37634 3.44428 12.08149 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC07')
s.location = CONST.LL
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    6.27037 3.42662 0.49456 
    6.42933 3.42662 0.95380 
    6.49998 3.47961 1.44837 
    6.58830 3.55026 2.19021 
    6.67661 3.60325 2.93206 
    6.78259 3.62092 3.99184 
    6.80026 3.62092 4.66303 
    6.78259 3.65624 5.51086 
    6.76493 3.69157 6.57064 
    6.67661 3.67390 7.84237 
    6.62363 3.69157 9.07878 
    6.69428 3.77988 10.24454 
    6.74727 3.83287 11.26899 
    6.78259 3.86820 12.15214 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC08')
s.location = CONST.LR
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    6.18205 3.67391 0.49456 
    6.16438 3.62092 0.84782 
    6.25270 3.51494 1.30706 
    6.30569 3.47961 1.80163 
    6.49998 3.49728 2.43749 
    6.67661 3.46195 3.03804 
    6.80025 3.51494 3.92119 
    6.83558 3.53260 4.83966 
    6.83558 3.53260 5.75814 
    6.85324 3.55027 6.88857 
    6.78259 3.60325 8.26628 
    6.67661 3.53260 9.46737 
    6.71194 3.53260 10.91573 
    6.71194 3.53260 12.61138 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC09')
s.location = CONST.LR
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    6.46466 2.89673 0.44158 
    6.48233 2.91439 0.77717 
    6.57064 2.94971 1.13043 
    6.69428 2.96738 1.44837 
    6.72961 3.02037 1.87228 
    6.80026 3.09102 2.50815 
    6.87091 3.12634 3.24999 
    6.94156 3.16167 4.13314 
    6.97689 3.24999 5.26357 
    6.90624 3.28531 6.42933 
    6.90624 3.23232 7.41846 
    6.83559 3.21466 8.30161 
    6.76493 3.23232 9.60867 
    6.81792 3.23232 10.56247 
    6.72961 3.19700 11.69291 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC10')
s.location = CONST.LL
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    5.77581 3.56792 0.42391 
    5.86412 3.55026 0.81250 
    5.91711 3.51493 1.30706 
    5.95244 3.46194 1.80163 
    6.02309 3.40895 2.40217 
    6.14673 3.33830 3.32064 
    6.18205 3.24999 4.20379 
    6.19972 3.23232 5.15760 
    6.21738 3.17933 6.32335 
    6.25271 3.16167 7.59509 
    6.30570 3.16167 9.57335 
    6.18205 3.26765 10.95106 
    6.16439 3.32064 11.94019 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC11')
s.location = CONST.LL
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    5.24592 3.28532 0.47690 
    5.49320 3.23234 1.05978 
    5.61684 3.25000 1.51902 
    5.77581 3.26766 2.15489 
    5.93477 3.30299 3.14401 
    6.00543 3.26766 4.20379 
    5.97010 3.26766 5.72281 
    5.86412 3.35598 7.06520 
    5.84646 3.37364 7.94835 
    5.72282 3.42663 9.32606 
    5.82880 3.51494 10.88041 
    5.91711 3.55027 12.29345 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC12')
s.location = CONST.LR
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    5.68748 2.86140 0.68886 
    5.68748 2.87906 0.91848 
    5.75813 2.89672 1.16576 
    5.84645 2.94971 1.37771 
    5.93476 3.00270 1.66032 
    6.04074 3.05569 2.11956 
    6.05840 3.09102 2.68478 
    5.98775 3.10868 3.39130 
    5.91710 3.12634 4.23912 
    5.75813 3.14401 5.19292 
    5.65215 3.12634 5.82879 
    5.58150 3.10868 6.39401 
    5.56384 3.12634 7.13585 
    5.81112 3.16167 7.77172 
    6.02308 3.16167 8.19563 
    6.14672 3.14401 8.61954 
    6.16438 3.16167 9.29074 
    6.09373 3.19700 9.96193 
    5.95242 3.17933 10.66845 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC13')
s.location = CONST.LR
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    2.54348 4.23912 0.68886 
    2.57880 4.34510 1.02445 
    2.33152 4.43341 1.55434 
    2.17255 4.38042 2.29619 
    2.17255 4.34510 3.24999 
    2.15489 4.32743 4.27445 
    2.31386 4.32743 5.44020 
    2.40217 4.32743 6.42933 
    2.36685 4.30977 7.59509 
    2.36685 4.29211 8.97280 
    2.43750 4.27445 10.13856 
    2.50815 4.29211 11.19834 
    2.49049 4.29211 12.22280 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC14')
s.location = CONST.LR
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    6.41166 3.40896 0.67119 
    6.44699 3.39129 0.91848 
    6.49998 3.39129 1.16576 
    6.53531 3.37363 1.55434 
    6.57063 3.35597 2.11956 
    6.51764 3.33830 2.79075 
    6.55297 3.30298 3.63858 
    6.62362 3.28531 4.66303 
    6.60596 3.28531 5.61683 
    6.53531 3.30298 6.64129 
    6.48232 3.32064 7.38313 
    6.37634 3.40896 8.23096 
    6.46465 3.46194 8.90215 
    6.53531 3.55026 9.57335 
    6.55297 3.55026 10.31519 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC15')
s.location = CONST.LL
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    6.51765 3.53260 0.63587 
    6.51765 3.55027 0.88315 
    6.51765 3.55027 1.13043 
    6.51765 3.55027 1.58967 
    6.57063 3.53260 2.26086 
    6.64129 3.51494 2.86141 
    6.72960 3.49728 3.46195 
    6.81792 3.46195 4.30977 
    6.88857 3.42663 5.33423 
    6.97688 3.40896 6.74727 
    6.88857 3.40896 8.44291 
    6.85324 3.35597 10.03258 
    6.88857 3.39130 11.48095 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC16')
s.location = CONST.LL
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    6.05841 3.32065 0.58288 
    6.05841 3.28532 0.88315 
    6.12906 3.28532 1.20108 
    6.14672 3.30298 1.73097 
    6.16438 3.24999 2.26086 
    6.21737 3.23233 2.96738 
    6.28802 3.21467 3.77988 
    6.35868 3.23233 5.01629 
    6.37634 3.28532 6.25270 
    6.30569 3.35597 7.77172 
    6.27036 3.39130 9.11411 
    6.32335 3.37363 10.03258 
    6.28802 3.37363 11.16302 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC17')
s.location = CONST.LL
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    6.32336 3.47961 0.31793 
    6.27037 3.46195 0.60054 
    6.32336 3.49727 0.90081 
    6.46466 3.55026 1.16576 
    6.55298 3.55026 1.62500 
    6.69428 3.60325 2.40217 
    6.78260 3.62092 3.53260 
    6.67662 3.63858 4.76901 
    6.67662 3.67390 6.04075 
    6.64129 3.65624 7.70107 
    6.49999 3.63858 10.10324 
    6.58830 3.60325 11.12769 
    6.65895 3.62092 12.57606 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC18')
s.location = CONST.LL
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    8.00133 4.91031 0.52989 
    8.01900 4.75134 0.81250 
    8.14264 4.66303 1.23641 
    8.23095 4.61004 1.76630 
    8.26628 4.48640 2.43749 
    8.28394 4.43341 3.28532 
    8.24862 4.39808 4.52173 
    7.96601 4.36276 6.35868 
    7.64807 4.30977 8.26628 
    7.93068 4.36276 10.27987 
    8.28394 4.39808 11.72823 
    8.46057 4.30977 13.38855 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC19')
s.location = CONST.LR
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    1.41304 3.63858 0.42391 
    1.23641 3.65624 0.77717 
    1.23641 3.70923 1.41304 
    1.21875 3.69157 2.43749 
    1.23641 3.69157 3.39130 
    1.36005 3.74456 4.55705 
    1.43071 3.76222 6.14672 
    1.41304 3.74456 7.91302 
    1.25408 3.74456 9.43204 
    1.21875 3.76222 11.41030 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC20')
s.location = CONST.LL
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    6.28803 4.13314 0.81250 
    6.39401 4.11548 1.13043 
    6.58830 4.00950 1.69565 
    6.67662 3.90352 2.26086 
    6.67662 3.72689 3.00271 
    6.62363 3.62091 3.95651 
    6.55298 3.55026 4.76901 
    6.30569 3.47961 5.86412 
    6.12906 3.44428 6.88857 
    6.09374 3.42662 7.66574 
    6.18205 3.44428 8.69020 
    6.30569 3.49727 9.53802 
    6.62363 3.56793 10.59780 
    6.78259 3.63858 11.83421 
    6.88857 3.69157 12.54073 
    6.88857 3.70923 13.35323 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC22')
s.location = CONST.LR
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    6.55298 3.33831 0.67119 
    6.55298 3.30299 0.88315 
    6.64129 3.21467 1.48369 
    6.67662 3.19701 1.94293 
    6.67662 3.19701 2.79075 
    6.69428 3.21467 3.81521 
    6.60597 3.17934 4.73368 
    6.58830 3.16168 5.75814 
    6.60597 3.14402 6.32335 
    6.62363 3.14402 7.24183 
    6.57064 3.14402 7.94835 
    6.53531 3.16168 8.69020 
    6.48233 3.25000 9.78530 
    6.51765 3.28532 11.05704 
    6.55298 3.26766 12.11682 
    6.55298 3.28532 12.99997 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC23')
s.location = CONST.LR
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    1.25407 4.27445 0.67119 
    1.23641 4.29212 0.95380 
    1.14809 4.22146 1.37771 
    1.04212 4.06250 1.97826 
    1.04212 3.92119 2.57880 
    1.04212 3.79755 3.24999 
    0.98913 3.63858 4.23912 
    1.04212 3.56793 5.29890 
    1.02445 3.65625 6.42933 
    1.14809 3.74456 8.08965 
    1.16576 3.77989 9.43204 
    1.05978 3.77989 10.63313 
    1.04212 3.83288 11.58693 
    0.93614 3.81521 12.71736 
    0.93614 3.83288 13.56518 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC24')
s.location = CONST.LL
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    5.81112 3.09103 0.63587 
    5.82879 3.09103 0.91848 
    5.84645 3.05570 1.37771 
    5.86411 3.09103 1.76630 
    5.81112 3.09103 2.57880 
    5.91710 3.07337 3.70923 
    5.93477 3.05570 4.83966 
    6.09373 3.12635 6.11140 
    6.27036 3.10869 7.80705 
    6.04074 3.09103 9.11411 
    5.98775 3.03804 10.17389 
    5.93477 3.03804 10.91573 
    5.91710 3.03804 11.69291 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC25')
s.location = CONST.LL
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    6.39401 3.77988 0.58288 
    6.42933 3.76221 0.81250 
    6.35868 3.70923 1.16576 
    6.32336 3.70923 1.48369 
    6.44700 3.76221 2.15489 
    6.46466 3.81520 2.93206 
    6.53531 3.86819 4.30977 
    6.60596 3.86819 5.65216 
    6.67662 3.83287 6.71194 
    6.65895 3.81520 7.80705 
    6.58830 3.79754 8.69020 
    6.55298 3.79754 9.96193 
    6.53531 3.79754 11.16302 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC27')
s.location = CONST.LR
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    5.33422 3.14401 0.95380 
    5.36955 3.12635 1.05978 
    5.42253 3.10869 1.34239 
    5.59916 3.19700 2.08423 
    5.70514 3.24999 2.61412 
    5.81112 3.33831 3.39130 
    5.95242 3.42662 4.55705 
    5.91710 3.46195 5.75814 
    5.98775 3.40896 7.34781 
    5.97009 3.30298 9.36139 
    6.09373 3.23233 10.98639 
    6.02308 3.21467 12.64671 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC28')
s.location = CONST.LR
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    5.91710 3.62092 0.75951 
    6.04075 3.62092 0.93614 
    6.25270 3.65624 1.23641 
    6.37634 3.65624 1.69565 
    6.55297 3.58559 2.57880 
    6.69428 3.51494 3.67390 
    6.69428 3.39130 5.12227 
    6.72960 3.33831 6.32335 
    6.74727 3.39130 7.70107 
    6.65895 3.44429 9.57335 
    6.48232 3.56793 11.12769 
    6.44699 3.60326 12.47008 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    
        
s = Specimen('SMC30')
s.location = CONST.LL
s.note='Single canal, no lingual canal'
s.furcation_pos_1 = 0.0 
s.furcation_pos_2 = 0.0 
s.canal_type = 0
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
    1.69565 4.08016 0.93614 
    1.66032 4.04483 1.04212 
    1.67798 4.06249 1.27174 
    1.64266 4.11548 1.62500 
    1.55434 4.15081 1.97826 
    1.51902 4.16847 2.54347 
    1.51902 4.18613 3.32064 
    1.60733 4.18613 3.99184 
    1.64266 4.18613 4.80434 
    1.90760 4.25679 5.75814 
    1.99592 4.29211 7.06520 
    1.97825 4.34510 8.61954 
    1.99592 4.32744 9.89128 
    1.94293 4.30978 11.05704 
    1.87228 4.38043 11.79888 
    1.85461 4.29211 12.89399 
'''

s.bounding_box = bounding_box_range
s.canal_pre_path = s.get_default_path(directory_name, canal_suffix)  
s.body_path = s.get_default_path(directory_name, body_suffix) 
s.set_pts1_pre( du.convert_to_points(ps1) )
s.set_pts2_pre( du.convert_to_points(ps2) )
roots.append(s)
    


