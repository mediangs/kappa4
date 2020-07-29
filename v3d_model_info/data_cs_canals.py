from __future__ import division


from constant import CONST
from class_specimen import Specimen, Canal
import os

specimens = []

bounding_box_range = [(-5, 11), (-5, 11), (-2, 14)] # [(-4, 12), (-4, 12), (-2, 14)]
directory_name = os.getenv('TOOTH_DATA') + '/v3d_cs/'
canal_suffix = '-canal-zoff.v3d'
body_suffix = '-solid-body-zoff.v3d'


"""
CS01
Sample: 18.51
C-shape
#37
"""
ml_canal = '''
8.40452 7.26697 1.91377
8.37776 7.40080 2.59630
8.47144 7.48110 3.23869
8.57850 7.46771 4.20226
8.83278 7.38742 5.16584
9.04691 7.26697 6.57105
8.88631 7.22682 8.01642
8.44467 7.21344 9.50193
8.05657 7.20005 10.70640
7.65508 7.18667 11.58968
'''

BPV = '''
4.18888 7.69523 9.07367
8.39114 4.13535 9.07367
'''

d_canal = '''
4.76435 3.90784 0.91004
4.77773 4.21565 1.43198
5.03201 4.53684 2.11451
5.20599 4.59037 2.75690
5.40673 4.46992 3.68033
5.60748 4.25579 4.72420
5.83499 4.13535 6.29001
5.94205 4.28256 7.85582
5.95544 4.59037 9.50193
5.88852 5.08554 11.26849
'''

b_canal = '''
4.69743 6.31678 0.38811
4.83126 6.54429 1.27139
4.99186 6.85210 2.31526
5.19260 7.22682 3.43943
5.21937 7.37403 4.52345
5.08554 7.64169 5.96882
5.13907 7.72199 7.65508
5.17922 7.58816 9.34133
5.39335 7.33388 11.14804
'''

s = Specimen('CS18.51')
s.tooth_position = CONST.LL
s.note=''
furcation_pos_buccal = 0.0
furcation_pos_lingual = 0.0
canal_type = 0

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)


s.canals.append(Canal(name='pre-ml',
                      pts_canal=ml_canal, pts_vector=BPV, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-d',
                      pts_canal=d_canal, pts_vector=BPV, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-b',
                      pts_canal=b_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)


"""
CS02
Sample: 18.47
#36
"""

mb_canal = '''
3.11824 5.36658 1.75317
2.77028 5.25952 2.35541
2.47586 4.97848 3.15839
2.22158 4.61714 4.28256
2.06098 4.29594 5.44688
2.03422 4.09520 6.57105
2.14128 3.96137 7.85582
2.51600 3.97475 9.46178
2.86396 4.05505 10.66625
3.31898 4.20226 11.99117
3.82754 4.25579 13.15549
'''

ml_canal = '''
2.70337 7.36065 1.33830
2.63645 7.36065 1.75317
2.58292 7.53463 2.55615
2.54277 7.73537 3.39928
2.50262 8.01642 4.60375
2.51600 8.20378 5.72792
2.62307 8.16363 6.97254
2.93088 7.97627 8.49821
3.22530 7.70861 9.78297
3.66694 7.32050 11.38893
4.10858 6.95916 13.15549
'''

d_canal = '''
10.19785 5.55395 1.29815
9.97034 5.62086 1.67288
9.68929 5.63424 2.31526
9.48855 5.67439 2.83720
9.28780 5.58071 3.76062
9.15397 5.47365 4.92494
8.95323 5.27290 6.24986
8.73910 5.15246 7.41418
8.39114 4.96509 8.89970
8.04318 4.99186 10.30491
7.72199 5.07216 11.50938
7.45433 5.09892 12.79415
'''

BPV = '''
5.16584 3.13162 12.49972
5.55395 7.77552 12.49972
'''

s = Specimen('CS18.47')
s.tooth_position = CONST.LL
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)


s.canals.append(Canal(name='pre-mb',
                      pts_canal=mb_canal, pts_opposite=ml_canal, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-ml',
                      pts_canal=ml_canal, pts_opposite=mb_canal, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-d',
                      pts_canal=d_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)


"""
CS03
Sample : 18.40 
#37
c-shape
"""

b_canal = '''
3.60003 3.17177 1.33830
3.72047 3.13162 1.83347
3.80077 3.35913 2.23496
4.25579 3.37252 2.75690
4.72420 3.34575 3.51973
5.19260 3.41267 4.44316
5.43350 3.43943 5.56733
5.51380 3.50635 6.81195
5.56733 3.61341 7.73537
'''


ml_canal = '''
3.58664 3.13162 1.31153
3.85430 3.77401 1.51228
3.84092 4.41639 1.71302
3.78739 4.75096 1.91377
3.85430 5.20599 2.43571
3.90784 5.48703 2.95764
4.04167 5.75469 3.64018
4.25579 5.91529 4.64390
4.44316 5.96882 5.88852
4.59037 5.98220 7.33388
4.65728 5.95544 7.81567
'''

BPV = '''
6.79856 2.74352 4.76435
2.60969 4.44316 4.76435
'''

s = Specimen('CS18.40')
s.tooth_position = CONST.LL
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)


s.canals.append(Canal(name='pre-b',
                      pts_canal=b_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-ml',
                      pts_canal=ml_canal, pts_vector=BPV, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))


specimens.append(s)

"""
CS04
Sample : 18.41
#16

"""


mb_canal = '''
9.79636 1.82009 2.15466
9.97034 1.87362 2.63645
10.01048 1.87362 3.11824
9.94357 1.77994 4.04167
9.78297 1.65949 5.12569
9.39487 1.63273 6.53090
9.06029 1.82009 7.97627
8.81940 2.26173 9.74282
8.72572 2.68998 10.86700
8.67218 3.05132 11.79042
'''

mb2_canal = '''
7.18667 3.15839 2.50262
7.17329 3.05132 2.99779
7.17329 3.01118 3.51973
7.26697 2.77028 4.12196
7.42757 2.58292 4.76435
7.57478 2.35541 5.48703
7.61493 2.11451 6.29001
7.42757 2.02083 7.61493
7.29374 2.27511 8.85955
7.21344 2.73013 10.18446
7.26697 3.26545 11.50938
'''

db_canal = '''
12.21868 7.33388 1.79332
12.24545 7.07961 2.07437
12.04470 6.71827 2.59630
11.56291 6.53090 3.39928
11.04098 6.38369 4.64390
10.75993 6.27663 5.52718
10.26476 6.02235 6.93239
9.54208 5.46026 8.97999
9.10044 5.08554 10.58595
8.77925 4.99186 11.58968
'''

p_canal = '''
0.89666 7.54801 1.67288
1.15094 7.49448 2.15466
1.47213 7.41418 2.87735
1.96730 7.32050 4.08182
2.51600 7.24020 5.48703
3.07809 6.93239 7.09299
3.62679 6.58444 8.41791
4.38962 6.33016 9.78297
5.59409 5.94205 11.91087
'''

BPV = '''
9.14059 4.16211 9.22089
4.09520 5.43350 9.22089
'''

s = Specimen('CS18.41')
s.tooth_position = CONST.UR
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)


s.canals.append(Canal(name='pre-mb',
                      pts_canal=mb_canal, pts_opposite=mb2_canal, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-mb2',
                      pts_canal=mb2_canal, pts_opposite=mb_canal, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-db',
                      pts_canal=db_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-p',
                      pts_canal=p_canal, pts_vector=BPV, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)


"""
CS05
Sample : 18.45
#47
"""


mb_canal = '''
2.20820 4.16211 0.76283
2.22158 4.17550 1.35168
2.20820 4.10858 1.75317
2.12790 3.81416 2.74352
2.02083 3.41267 4.05505
1.98068 3.02456 5.52718
2.06098 2.91749 6.78518
2.28849 2.89073 8.41791
2.68998 2.94426 10.02387
3.01118 3.15839 11.09451
'''

ml_canal = '''
2.20820 4.17550 0.78960
2.24834 4.16211 1.15094
2.20820 4.17550 1.59258
2.11451 4.44316 2.52939
2.14128 5.19260 3.94799
2.24834 5.82160 5.42012
2.34203 6.10265 6.59782
2.52939 6.20971 7.98965
3.01118 6.08927 9.54208
3.51973 5.91529 11.44247
'''

d_canal = '''
7.86920 3.96137 1.04387
7.64169 3.92122 1.52566
7.41418 4.00152 2.02083
7.21344 4.21565 2.73013
7.11976 4.29594 3.41267
7.03946 4.28256 4.48331
6.89225 4.28256 5.90190
6.79856 4.33609 7.58816
6.58444 4.17550 9.70268
'''

BPV = '''
2.55615 2.74352 9.54208
2.78366 6.26324 9.54208
'''

s = Specimen('CS18.45')
s.tooth_position = CONST.LR
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-mb',
                      pts_canal=mb_canal, pts_opposite=ml_canal, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-ml',
                      pts_canal=ml_canal, pts_opposite=mb_canal, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-d',
                      pts_canal=d_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

"""
CS18.01
Sample : 18.01
#14
"""

b_canal = '''
4.18888 4.32271 0.34796
3.90784 4.17550 0.70930
3.88107 3.90784 1.27139
3.86769 3.77401 2.03422
3.77401 3.65356 2.83720
3.65356 3.45281 4.08182
3.55988 3.39928 5.56733
3.54650 3.54650 6.93239
3.55988 3.74724 8.33761
3.61341 3.89445 9.62238
3.64018 4.10858 10.54580
3.66694 4.46992 11.87072
3.73386 4.67067 13.55698
'''

p_canal = '''
4.08182 9.08706 1.61934
4.08182 9.11382 2.07437
4.01490 9.08706 2.63645
3.96137 8.84616 3.72047
3.86769 8.61865 4.76435
3.77401 8.29746 6.04912
3.76062 7.76214 7.41418
3.74724 7.18667 8.97999
3.77401 6.57105 10.82685
3.66694 6.12941 12.67370
3.70709 5.78146 14.27966
'''

s = Specimen('CS18.01')
s.tooth_position = CONST.UR
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-b',
                      pts_canal=b_canal, pts_opposite=p_canal, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-p',
                      pts_canal=p_canal, pts_opposite=b_canal, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))
specimens.append(s)


"""
CS18.02
Sample : 18.02
#47
"""

mb_canal = '''
3.01118 4.26918 1.69964
2.43571 4.36286 2.71675
2.08775 4.65728 4.16211
2.07437 4.96509 5.60748
2.31526 5.59409 7.49448
2.87735 5.70116 8.97999
3.41267 5.71454 9.86327
4.30933 5.62086 11.26849
'''

ml_canal='''
2.99779 4.26918 1.69964
2.43571 4.38962 2.67660
2.08775 4.28256 4.04167
1.99407 4.12196 5.60748
2.11451 4.01490 6.81195
2.55615 3.90784 8.33761
3.15839 4.17550 9.66253
3.61341 4.21565 10.78670
4.25579 4.29594 11.66998
'''

d_canal = '''
8.31084 4.81788 1.51228
7.92274 4.80450 1.99407
7.58816 4.72420 2.55615
7.41418 4.63052 3.43943
7.30712 4.37624 5.00524
7.37403 4.42977 6.57105
7.26697 4.46992 8.41791
7.03946 4.59037 10.30491
6.86548 4.59037 11.71013
'''

BPV = '''
7.01269 8.02980 8.24393
6.94578 1.45875 8.24393
'''

s = Specimen('CS18.02')
s.tooth_position = CONST.LR
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-mb',
                      pts_canal=mb_canal, pts_opposite=ml_canal, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-ml',
                      pts_canal=ml_canal, pts_opposite=mb_canal, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-d',
                      pts_canal=d_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)


"""
CS18.03-1
Sample : 18.03
#16 MB root rest
"""

mb_canal = '''
2.35541 2.66322 10.10417
2.48924 2.58292 9.58223
2.52939 2.64983 9.10044
2.62307 2.81043 8.09671
2.48924 2.94426 6.61120
2.39556 3.05132 5.44688
2.30188 3.13162 4.24241
'''

BPV = '''
2.12790 0.82975 6.69150
2.97103 5.04539 6.69150
'''
s = Specimen('CS18.03-1')
s.tooth_position = CONST.UR
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-mb',
                      pts_canal=mb_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

"""
CS18.03-2
Sample : 18.03
#16 palatal root rest
"""

p_canal = '''
4.93833 3.06471 12.75400
4.76435 2.93088 12.11162
4.41639 2.71675 10.86700
4.04167 2.63645 8.89970
3.76062 2.70337 7.09299
3.42605 3.09147 4.64390
'''

BPV = '''
4.01490 4.93833 4.24241
2.38217 1.41860 4.24241
'''
s = Specimen('CS18.03-2')
s.tooth_position = CONST.UR
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-p',
                      pts_canal=p_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)


"""
CS18.05-1
Sample : 18.05
#46 distal root 
"""

d_canal = '''
3.80077 2.32864 0.73607
4.02828 2.43571 1.19109
4.21565 2.52939 1.79332
4.17550 2.50262 2.51600
4.14873 2.43571 3.68033
4.12196 2.43571 4.92494
4.18888 2.55615 6.53090
4.32271 2.71675 7.85582
4.55022 3.03794 9.30119
4.72420 3.34575 10.18446
'''

BPV = '''
0.76283 2.36879 6.54429
7.29374 2.34203 6.54429
'''
s = Specimen('CS18.05-1')
s.tooth_position = CONST.LR
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)

s.canals.append(Canal(name='pre-d',
                      pts_canal=d_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

"""
CS18.06
Sample : 18.06
#27  
"""


mb_canal = '''
3.21192 3.46620 2.14128
3.27884 3.14501 2.63645
3.35913 2.90411 3.27884
3.42605 2.70337 3.76062
3.55988 2.52939 5.00524
3.70709 2.59630 6.12941
3.89445 2.82381 7.93612
4.05505 3.09147 9.50193
'''

db_canal = '''
2.06098 6.94578 1.21785
2.16805 6.73165 1.87362
2.22158 6.63797 2.51600
2.31526 6.51752 3.11824
2.55615 6.61120 3.96137
2.90411 6.82533 4.88480
3.18515 6.83871 5.96882
3.54650 6.82533 7.57478
3.81416 6.66473 9.34133
'''

p_canal = '''
8.69895 5.36658 1.25800
8.89970 5.31305 1.67288
9.15397 5.25952 2.11451
9.44840 5.25952 2.95764
9.63576 5.35320 3.88107
9.72944 5.46026 4.88480
9.51531 5.48703 7.05284
9.24765 5.39335 8.93984
'''

BPV = '''
5.76807 1.24462 7.42757
5.28629 7.26697 7.42757
'''

s = Specimen('CS18.06')
s.tooth_position = CONST.UL
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)


s.canals.append(Canal(name='pre-mb',
                      pts_canal=mb_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-db',
                      pts_canal=db_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-p',
                      pts_canal=p_canal, pts_vector=BPV, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

"""
CS18.07
Sample : 18.07
#46
"""

mb_canal = '''
6.03573 2.62307 1.25800
5.99558 2.56954 1.67288
5.98220 2.36879 1.95392
5.83499 2.08775 2.19481
5.52718 1.94054 2.47586
5.19260 1.73979 2.87735
4.71082 1.57919 3.43943
4.24241 1.52566 4.28256
3.73386 1.59258 5.80822
3.51973 1.73979 6.89225
3.34575 1.94054 8.09671
3.31898 2.27511 9.46178
'''

ml_canal = '''
7.11976 2.63645 1.35168
6.98593 2.51600 1.75317
7.09299 2.19481 2.35541
7.13314 1.92715 3.03794
7.14652 1.77994 3.84092
7.09299 1.67288 4.56360
7.13314 1.64611 5.68778
7.06622 1.68626 6.93239
6.90563 1.86024 8.01642
6.70488 2.07437 9.22089
'''

db_canal = '''
3.97475 9.14059 3.58664
3.84092 8.87293 4.56360
3.82754 8.40452 5.72792
3.84092 8.12348 6.61120
3.89445 7.81567 7.61493
3.93460 7.52125 8.49821
'''

dl_canal = '''
8.80601 5.78146 1.05726
9.38148 5.96882 1.67288
9.63576 6.00897 2.59630
9.80974 6.07588 3.72047
9.84989 6.14280 4.88480
9.82312 6.19633 6.29001
9.63576 6.30339 7.53463
9.38148 6.38369 8.85955
'''

BPV = '''
0.61562 4.63052 8.51159
10.41197 4.56360 8.51159
'''

s = Specimen('CS18.07')
s.tooth_position = CONST.LR
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)


s.canals.append(Canal(name='pre-mb',
                      pts_canal=mb_canal, pts_opposite=ml_canal, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-ml',
                      pts_canal=ml_canal, pts_opposite=mb_canal, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-db',
                      pts_canal=db_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-dl',
                      pts_canal=dl_canal, pts_vector=BPV, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)



"""
CS18.08
Sample : 18.08
#27, instrumented  
"""


mb_canal = '''
1.29815 4.05505 1.03049
1.59258 4.14873 1.71302
1.91377 4.26918 2.31526
2.12790 4.25579 2.79705
2.42232 4.05505 3.31898
2.62307 3.64018 3.92122
2.75690 3.30560 4.52345
3.01118 3.03794 5.32643
3.38590 3.02456 6.65135
3.61341 3.14501 7.33388
4.01490 3.45281 8.41791
'''

db_canal = '''
1.29815 4.05505 1.03049
1.48551 4.10858 1.43198
1.77994 4.25579 2.03422
2.11451 4.42977 2.83720
2.40894 4.61714 3.47958
2.67660 4.92494 4.16211
2.94426 5.11231 4.88480
3.45281 5.13907 6.08927
3.84092 5.00524 7.33388
4.16211 4.85803 8.49821
'''

p_canal = '''
7.78891 4.13535 1.57919
7.92274 4.40301 2.31526
8.17701 4.40301 3.11824
8.28408 4.29594 3.88107
8.33761 4.10858 5.20599
8.19040 4.09520 6.61120
7.92274 4.17550 7.49448
7.48110 4.34948 8.77925
'''

BPV = '''
1.44536 2.55615 5.20599
9.32795 2.32864 5.20599
'''

s = Specimen('CS18.08')
s.tooth_position = CONST.UL
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)


s.canals.append(Canal(name='pre-mb',
                      pts_canal=mb_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-db',
                      pts_canal=db_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-p',
                      pts_canal=p_canal, pts_vector=BPV, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)



"""
CS18.09
Sample : 18.09
#26
"""


mb_canal = '''
2.85058 4.21565 1.51228
2.90411 3.94799 2.07437
2.81043 3.73386 2.71675
2.74352 3.53311 3.51973
2.83720 3.31898 4.28256
2.81043 3.26545 5.16584
2.87735 3.11824 6.33016
3.07809 3.03794 7.97627
3.51973 3.14501 8.97999
3.85430 3.47958 9.74282
3.96137 4.21565 11.10789
'''

mb2_canal = '''
5.20599 3.25207 2.63645
5.12569 3.15839 2.79705
4.89818 3.01118 3.07809
4.85803 2.87735 3.39928
4.85803 2.75690 4.12196
5.03201 2.62307 4.88480
5.11231 2.54277 5.48703
4.95171 2.55615 6.12941
4.76435 2.59630 6.97254
4.75096 2.58292 7.97627
4.81788 2.64983 8.61865
5.23275 2.93088 9.46178
5.36658 3.27884 9.94357
5.42012 3.66694 10.42536
5.27290 3.97475 10.94729
5.03201 4.30933 11.26849
4.96509 4.41639 11.42908
'''

db_canal = '''
3.09147 7.42757 0.77621
3.02456 7.20005 1.19109
2.98441 7.02608 1.63273
2.98441 6.89225 2.27511
3.10486 6.83871 2.99779
3.45281 6.70488 4.16211
3.70709 6.65135 5.16584
4.05505 6.46399 6.33016
4.10858 6.27663 7.45433
4.34948 6.06250 8.45806
4.61714 5.67439 9.42163
4.75096 5.29967 10.38521
4.65728 5.32643 11.10789
'''

p_canal = '''
9.46178 4.59037 1.01711
9.56885 4.67067 2.19481
9.48855 4.65728 3.27884
9.31457 4.71082 4.88480
9.19412 4.76435 6.04912
8.93984 4.71082 8.01642
8.41791 5.07216 10.10417
7.94950 5.35320 11.54953
'''

BPV = '''
2.43571 5.95544 7.65508
8.87293 4.36286 7.65508
'''

s = Specimen('CS18.09')
s.tooth_position = CONST.UL
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)


s.canals.append(Canal(name='pre-mb',
                      pts_canal=mb_canal, pts_opposite=mb2_canal, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-mb2',
                      pts_canal=mb2_canal, pts_opposite=mb_canal, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-db',
                      pts_canal=db_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-p',
                      pts_canal=p_canal, pts_vector=BPV, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)


"""
CS18.10
Sample : 18.10
#17, original canal  
"""


mb_canal = '''
3.60003 2.46247 2.62307
3.50635 2.40894 3.03794
3.26545 2.50262 3.51973
2.97103 2.67660 4.36286
2.73013 2.90411 5.84837
2.74352 2.98441 8.01642
3.07809 3.37252 9.54208
3.46620 3.58664 10.42536
3.90784 3.66694 11.22834
'''

db_canal = '''
8.93984 1.91377 1.61934
8.83278 1.84685 1.91377
8.51159 1.84685 2.35541
8.02980 1.96730 2.87735
7.68184 2.15466 3.43943
7.28035 2.47586 4.28256
7.05284 2.85058 5.36658
6.95916 3.14501 6.45061
6.90563 3.50635 7.57478
6.70488 3.93460 8.97999
6.42384 4.36286 10.46551
6.31678 4.56360 11.30864
'''

p_canal = '''
4.40301 8.76586 0.54870
4.42977 8.89970 0.82975
4.57699 9.12721 1.51228
4.72420 9.42163 2.51600
4.76435 9.66253 3.68033
4.73758 9.80974 5.56733
4.79111 9.63576 6.93239
5.04539 9.04691 8.57850
5.09892 8.39114 10.06402
5.08554 7.85582 11.06774
'''

BPV = '''
5.92867 2.38217 9.16736
4.80450 9.24765 9.16736
'''

s = Specimen('CS18.10')
s.tooth_position = CONST.UR
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)


s.canals.append(Canal(name='pre-mb',
                      pts_canal=mb_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-db',
                      pts_canal=db_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-p',
                      pts_canal=p_canal, pts_vector=BPV, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)


"""
CS18.11
Sample : 18.11
#37 C-shape. filled
"""

mb_canal = '''
4.48331 3.03794 1.25800
4.33609 3.14501 1.79332
4.32271 3.06471 2.35541
4.60375 2.68998 3.23869
5.12569 2.48924 4.24241
5.68778 2.48924 5.32643
6.19633 2.59630 6.65135
6.42384 2.90411 8.33761
6.31678 3.22530 9.80974
6.15618 3.57326 11.05436
6.03573 3.76062 11.62983
'''

ml_canal = '''
4.49669 3.05132 1.25800
4.32271 3.07809 1.95392
4.30933 3.05132 2.35541
4.21565 2.58292 3.10486
4.21565 2.28849 3.72047
4.12196 1.98068 4.88480
3.98813 1.82009 6.20971
3.92122 1.80671 7.32050
4.05505 1.94054 8.77925
4.21565 2.19481 9.86327
4.46992 2.58292 10.89376
4.72420 3.06471 11.97779
'''

db_canal = '''
4.10858 5.88852 1.13756
4.02828 5.62086 1.51228
4.10858 4.99186 1.98068
4.24241 4.79111 2.63645
4.42977 4.87141 3.30560
4.71082 5.00524 4.16211
5.07216 5.24614 5.12569
5.24614 5.36658 6.08927
5.28629 5.48703 7.09299
5.24614 5.60748 8.41791
5.09892 5.60748 9.90342
5.00524 5.51380 11.02759
'''

dl_canal = '''
4.12196 5.92867 1.13756
4.01490 5.60748 1.51228
4.04167 5.25952 1.91377
3.90784 5.03201 2.51600
3.73386 5.11231 3.60003
3.61341 5.33982 4.75096
3.70709 5.59409 6.08927
4.01490 5.67439 7.96289
4.29594 5.67439 10.06402
4.56360 5.62086 11.38893
'''

BPV = '''
8.29746 5.20599 9.76959
1.88700 3.50635 9.76959
'''

s = Specimen('CS18.11')
s.tooth_position = CONST.LL
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)


s.canals.append(Canal(name='pre-mb',
                      pts_canal=mb_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-ml',
                      pts_canal=ml_canal, pts_vector=BPV, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-db',
                      pts_canal=db_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

s.canals.append(Canal(name='pre-dl',
                      pts_canal=dl_canal, pts_vector=BPV, is_buccal_side=False,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

"""
CS16.04
#21, filled, post  
"""

c_canal = '''
4.88228 4.78702 0.30961
4.88228 4.60840 1.13126
4.89419 4.51313 2.16726
4.90610 4.38214 4.16780
4.94182 4.27497 6.16834
4.88228 4.25116 8.16889
4.84656 4.26306 10.52667
'''

BPV = '''
2.72693 3.58431 5.20380
7.81165 5.54913 5.20380
'''

s = Specimen('CS16.04')
s.tooth_position = CONST.UL
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)


s.canals.append(Canal(name='pre-c',
                      pts_canal=c_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)


"""
CS16.05
#22, filled  
"""

c_canal = '''
4.79111 5.04539 1.25800
4.68405 4.97848 1.79332
4.65728 4.88480 2.48924
4.44316 4.68405 3.66694
4.18888 4.53684 4.95171
3.96137 4.36286 7.03946
3.93460 4.33609 9.34133
3.93460 4.33609 10.94729
4.16211 4.41639 12.49972
'''

BPV = '''
0.84313 5.39335 18.29456
7.74876 4.32271 18.29456
'''

s = Specimen('CS16.05')
s.tooth_position = CONST.UL
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)


s.canals.append(Canal(name='pre-c',
                      pts_canal=c_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)


"""
CS16.07
#11, filled  
"""

c_canal = '''
4.62030 4.22734 20.24360
4.47741 4.33451 19.49340
4.48932 4.34642 18.20733
4.38214 4.39405 16.45686
4.32260 4.32260 13.95618
4.45359 4.26306 12.02708
4.48932 4.31070 10.27660
4.33451 4.22734 8.52613
4.38214 4.39405 6.41841
'''

BPV = '''
-0.23816 3.98918 3.89392
6.82328 3.75102 3.89392
'''

s = Specimen('CS16.07')
s.tooth_position = CONST.UR
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)


s.canals.append(Canal(name='pre-c',
                      pts_canal=c_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)


"""
CS16.08
#41, filled, file fx  
"""

c_canal = '''
2.71502 2.14344 19.89827
2.70312 2.22680 19.08852
2.66739 2.36969 17.70720
2.59594 2.45305 15.84955
2.67930 2.59594 13.61084
2.71502 2.57213 11.08635
3.00082 2.53640 9.60976
'''

BPV = '''
0.64303 2.45305 2.69121
4.88228 2.38160 2.69121
'''

s = Specimen('CS16.08')
s.tooth_position = CONST.LR
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)


s.canals.append(Canal(name='pre-c',
                      pts_canal=c_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)

"""
CS16.09
#35, filled  
"""

c_canal = '''
5.00136 3.73911 15.24224
5.03708 3.83438 14.95645
5.07281 4.19162 14.58730
5.10853 4.40596 13.81328
5.19189 4.50122 12.49149
5.26334 4.47741 11.24115
5.21570 4.37024 9.41923
5.14426 4.19162 7.13289
5.06090 4.07254 5.31097
5.04899 4.06063 4.09635
'''

BPV = '''
9.02626 3.95346 5.73966
1.27416 4.22734 5.73966
'''

s = Specimen('CS16.09')
s.tooth_position = CONST.LL
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)


s.canals.append(Canal(name='pre-c',
                      pts_canal=c_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)


"""
CS16.11
#47, filled  
"""

d_canal = '''
8.35942 3.91773 11.56267
8.04981 3.91773 11.30069
7.79974 4.02490 10.87200
7.71638 4.14398 10.31233
7.72829 4.20352 9.03817
7.53776 4.12017 7.27579
7.29960 4.07254 5.45386
7.02572 4.13208 3.70339
6.70420 4.28688 1.81002
'''

BPV = '''
5.57294 0.69066 0.01191
5.06090 6.76374 0.01191
'''

s = Specimen('CS16.11')
s.tooth_position = CONST.LR
s.note=''

s.bounding_box = bounding_box_range
s.body_path = s.get_default_path(directory_name, body_suffix)


s.canals.append(Canal(name='pre-d',
                      pts_canal=d_canal, pts_vector=BPV, is_buccal_side=True,
                      path=s.get_default_path(directory_name, canal_suffix)))

specimens.append(s)
