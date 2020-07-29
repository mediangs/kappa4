from __future__ import division
from constant import CONST
from class_specimen import Specimen, Canal
import os

directory_name = os.getenv('TOOTH_DATA') + '/v3d_ljkrp1/'
roots = []
bounding_box_range = [(-2, 12), (-4, 10), (0, 14)]
canal_pre_suffix = '-canal-pre-zoff.v3d'
canal_post_suffix = '-canal-post-zoff'
body_suffix = '-solid-body-zoff.v3d'

###########
# 0 - RP01

s = Specimen('RP01')
s.tooth_position = CONST.LR
s.note = 'check all'
s.canal_type = 0
s.body_path = s.get_default_path(directory_name, body_suffix)
s.bounding_box = bounding_box_range

canal_pre_path = s.get_default_path(directory_name, canal_pre_suffix)
canal_blx_path = s.get_default_path(directory_name, canal_post_suffix) + '-blx.v3d'
canal_ptu_path = s.get_default_path(directory_name, canal_post_suffix) + '-ptu.v3d'
canal_rcp_path = s.get_default_path(directory_name, canal_post_suffix) + '-rcp.v3d'

# mesio-buccal pre-instrumentation

# buccal pre
ps1_pre = '''
    5.38080 6.51360 15.84150
    5.25690 6.60210 15.46980
    5.09760 6.77910 14.90340
    4.99140 7.04460 14.12460
    4.79670 7.11540 13.39890
    4.21260 7.11540 12.31920
    3.59310 7.38090 11.18640
    3.15060 7.85880 10.17750
    2.79660 8.26590 8.67300
    2.79660 8.51370 6.99150
    3.13290 8.76150 5.13300
    3.48690 8.70840 3.87630
    3.89400 8.42520 3.07980
    4.07100 8.19510 2.61960
    4.30110 8.01810 2.19480
    4.61970 7.91190 1.73460
'''

# lingual pre
ps2_pre = '''
    5.38080 6.51360 15.85920
    5.22150 6.65520 15.36360
    5.06220 6.90300 14.62020
    4.88520 7.08000 13.71750
    4.44270 7.00920 12.62010
    3.73470 6.40740 11.57580
    3.23910 5.68170 10.28370
    3.04440 5.32770 8.67300
    3.16830 5.31000 7.16850
    3.50460 5.09760 5.66400
    3.89400 4.86750 4.44270
    4.42500 5.00910 3.00900
    4.81440 4.77900 1.84080
    '''

# buccal, by BLX
ps1_post_blx = '''
    5.32770 6.51360 15.85920
    5.13300 6.74370 15.08040
    4.99140 6.86760 14.19540
    4.46040 7.02690 13.04490
    3.92940 7.25700 12.03600
    3.29220 7.68180 10.70850
    2.92050 8.19510 8.99160
    2.97360 8.40750 7.69950
    3.15060 8.53140 6.19500
    3.54000 8.46060 4.47810
    4.10640 8.21280 2.33640
    4.35420 8.10660 1.25670
    '''

# lingual, by BLX
ps2_post_blx = '''
    5.38080 6.51360 15.85920
    5.22150 6.65520 15.36360
    5.06220 6.90300 14.62020
    4.88520 7.08000 13.71750
    4.44270 7.00920 12.62010
    3.73470 6.40740 11.57580
    3.23910 5.68170 10.28370
    3.04440 5.32770 8.67300
    3.16830 5.31000 7.16850
    3.50460 5.09760 5.66400
    3.89400 4.86750 4.44270
    4.42500 5.00910 3.00900
    4.81440 4.77900 1.84080
    '''

ps1_post_ptu = '''
    5.38080 6.51360 15.85920
    5.18610 6.67290 15.25740
    5.09760 6.88530 14.51400
    4.47810 7.06230 12.93870
    3.66390 7.46940 11.46960
    3.04440 8.01810 10.00050
    2.92050 8.38980 8.21280
    3.25680 8.47830 5.98260
    3.62850 8.46060 4.05330
    4.03560 8.30130 2.47800
    4.28340 8.17740 1.32750
    '''
ps2_post_ptu = '''
    5.38080 6.51360 15.85920
    5.22150 6.65520 15.36360
    5.06220 6.90300 14.62020
    4.88520 7.08000 13.71750
    4.44270 7.00920 12.62010
    3.73470 6.40740 11.57580
    3.23910 5.68170 10.28370
    3.04440 5.32770 8.67300
    3.16830 5.31000 7.16850
    3.50460 5.09760 5.66400
    3.89400 4.86750 4.44270
    4.42500 5.00910 3.00900
    4.81440 4.77900 1.84080
    '''
ps1_post_rcp = '''
    5.34540 6.51360 15.85920
    5.23920 6.63750 15.52290
    5.07990 6.86760 14.72640
    4.84980 6.99150 13.78830
    4.28340 7.18620 12.47850
    3.85860 7.41630 11.68200
    3.36300 7.75260 10.56690
    3.09750 7.96500 9.78810
    2.88510 8.19510 8.77920
    2.84970 8.37210 7.55790
    2.99130 8.44290 6.31890
    3.29220 8.46060 5.02680
    4.00020 8.40750 2.70810
    4.28340 8.33670 1.69920
    '''
ps2_post_rcp = '''
    5.38080 6.51360 15.85920
    5.22150 6.65520 15.36360
    5.06220 6.90300 14.62020
    4.88520 7.08000 13.71750
    4.44270 7.00920 12.62010
    3.73470 6.40740 11.57580
    3.23910 5.68170 10.28370
    3.04440 5.32770 8.67300
    3.16830 5.31000 7.16850
    3.50460 5.09760 5.66400
    3.89400 4.86750 4.44270
    4.42500 5.00910 3.00900
    4.81440 4.77900 1.84080
    '''

canal_pre = Canal(name='pre',
                  length_buccal=15.5,
                  length_lingual=15.1,
                  furcation_pos_buccal=13.6,
                  furcation_pos_lingual=12.7,
                  pts_buccal=ps1_pre,
                  pts_lingual=ps2_pre,
                  path=canal_pre_path)
s.canals.append(canal_pre)

canal_blx = Canal(name='blx',
                  length_buccal=15.5,
                  length_lingual=15.1,
                  furcation_pos_buccal=13.6,
                  furcation_pos_lingual=12.7,
                  pts_buccal=ps1_post_blx,
                  pts_lingual=ps2_post_blx,
                  path=canal_blx_path)
s.canals.append(canal_blx)

canal_ptu = Canal(name='ptu',
                  length_buccal=15.5,
                  length_lingual=15.1,
                  furcation_pos_buccal=13.6,
                  furcation_pos_lingual=12.7,
                  pts_buccal=ps1_post_ptu,
                  pts_lingual=ps2_post_ptu,
                  path=canal_ptu_path)
s.canals.append(canal_ptu)

canal_rcp = Canal(name='rcp',
                  length_buccal=15.5,
                  length_lingual=15.1,
                  furcation_pos_buccal=13.6,
                  furcation_pos_lingual=12.7,
                  pts_buccal=ps1_post_rcp,
                  pts_lingual=ps2_post_rcp,
                  path=canal_rcp_path)
s.canals.append(canal_rcp)

roots.append(s)
