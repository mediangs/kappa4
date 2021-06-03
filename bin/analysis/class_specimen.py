# -*- coding: cp949 -*-
'''
Created on 2014. 4. 3.

@author: jongki
'''

from nerve_path import Nerve_path
import helpers_contours as du


class Canal:
    """
    Canal 정보를 담은 class
    buccal과 lingual canal path 정보를 포함
    """
    name = None                     # pre, pst, blx, rcp ...
    length = None            # lenght of canal
    furcation_pos = None
    pts_canal = None               # curve points of the canal(exported from v-works)
    pts_opposite = None              # curve points of the canal(exported from v-works)
    has_opposite_canal = False      # pair 를 이루는 canal 인지,
    path = None                     # file path
    cnls_cmp_name = None
    # facets =  None                   # facets

    def __init__(self, name, is_buccal_side, length=0.0, furcation_pos=0.0, pts_canal=None,
                 pts_opposite=None, pts_vector=None, path=None, cnls_cmp_name=None):
        """
        :param name:
        :param length:
        :param furcation_pos:
        :param pts_canal:
        :param pts_opposite:
        :param pts_vector: buccal to lingual(palatal) vector
        :param is_buccal_side: current canal is buccal side?
        :param path:
        """

        assert (pts_opposite or pts_vector)

        self.name = name
        self.length = length
        self.furcation_pos = furcation_pos
        self.pts_vector = pts_vector
        self.pts_canal = du.convert_to_points(pts_canal)
        self.is_buccal_side = is_buccal_side
        if pts_opposite:
            self.has_opposite_canal = True
            self.pts_opposite = du.convert_to_points(pts_opposite)
        elif pts_vector:
            self.has_opposite_canal = False
            self.pts_opposite = du.shift_points(self.pts_canal, self.pts_vector, self.is_buccal_side)
        else:
            print('opposite canal info should be provided')
            exit()
        self.path = path
        self.cnls_cmp_name = cnls_cmp_name

    @property
    def curve_canal(self):
        return Nerve_path.create(self.pts_canal)

    @property
    def curve_opposite(self):
        return Nerve_path.create(self.pts_opposite)


class Specimen:
    """
        분석할 시편(치아)에 대한 정보를 담은 class
    """

    def __init__(self, name):
        # BLX01 , LJKCS01M 등의 이름
        self.name = name
        self.tooth_position = None
        self.note = None
        self.canal_type = None
        self.canals = []  # list of Curve instances
        self.body_path = None
        self.bounding_box = None
        self.weine_classification = None
        self.magnification_ratio = 1
        self.central_fossa = None
        self.chamber_roof = None
        self.long_axis = None

    def get_default_path(self, directory, suffix):
        '''
        :param directory:
        :param suffix:
        :return:

        Specimen name이 GHero.57M-mb.sound
        GHero.57M subfold name
        '''

        if '-' in self.name:
            subfold_name = self.name.split('-')[0]
        else:
            subfold_name = self.name.strip()

        return directory+subfold_name+'/'+subfold_name+suffix

def test2():

    from constant import CONST
    import os

    specimens = []

    bounding_box_range = [(-10, 20), (-10, 20), (-10, 20)]
    directory_name = os.getenv('TOOTH_DATA') + '/v3d_smc/'
    canal_pre_suffix = '-canal-zoff.v3d'
    body_suffix = '-solid-body-zoff.v3d'

    ###########
    # 0 - SMC01

    s = Specimen('SMC01')
    s.location = CONST.LR
    s.note = 'Single canal, no lingual canal'
    s.bounding_box = bounding_box_range
    s.body_path = s.get_default_path(directory_name, body_suffix)
    canal_pre_path = s.get_default_path(directory_name, canal_pre_suffix)

    ps_buccal = '''
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

    ps_vector = '''
    2.93206 3.67390 8.60188
    5.98776 3.65624 8.60188
        '''

    canal_pre = Canal(name='pre-b',
                      pts_canal=ps_buccal,
                      pts_vector=ps_vector,
                      is_buccal_side=True,
                      path=canal_pre_path)
    s.canals.append(canal_pre)

    specimens.append(s)

    for s in specimens:
        print('name : ' + s.name)
        for canal in s.canals:
            print(' canal name : ' + canal.name)
            print(' canal path : ' + canal.path)
            print(canal.pts_canal)
            print(canal.pts_vector)
            print(canal.pts_opposite)

    print('pre-b : ')
    print([c.pts_canal for c in s.canals if c.name == 'pre-b'][0])


def test():
    from constant import CONST
    import os

    directory_name = os.getenv('TOOTH_DATA') + '/v3d_ljkrp1/'
    specimens = []
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
    buccal_pre = '''
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
    lingual_pre = '''
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
    buccal_post_blx = '''
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
    lingual_post_blx = '''
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

    buccal_post_ptu = '''
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
    lingual_post_ptu = '''
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
    buccal_post_rcp = '''
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
    lingual_post_rcp = '''
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

    s.canals.append(
        Canal(name='pre-b', length=15.5, furcation_pos=13.6,
              pts_canal=buccal_pre, pts_opposite=lingual_pre,
              is_buccal_side=True, path=canal_pre_path))

    s.canals.append(
        Canal(name='pre-l', length=15.1, furcation_pos=12.7,
              pts_canal=lingual_pre, pts_opposite=buccal_pre,
              is_buccal_side=False, path=canal_pre_path))

    s.canals.append(
        Canal(name='blx-b', length=15.5, furcation_pos=13.6,
              pts_canal=buccal_post_blx, pts_opposite=lingual_post_blx,
              is_buccal_side=True, path=canal_blx_path))

    s.canals.append(
        Canal(name='blx-l', length=15.1, furcation_pos=12.7,
              pts_canal=lingual_post_blx, pts_opposite=buccal_post_blx,
              is_buccal_side=True, path=canal_blx_path))

    s.canals.append(
        Canal(name='ptu-b', length=15.5, furcation_pos=13.6,
              pts_canal=buccal_post_ptu, pts_opposite=lingual_post_ptu,
              is_buccal_side=True, path=canal_ptu_path))

    s.canals.append(
        Canal(name='ptu-l', length=15.1, furcation_pos=12.7,
              pts_canal=lingual_post_ptu, pts_opposite=buccal_post_ptu,
              is_buccal_side=False, path=canal_ptu_path))

    s.canals.append(
        Canal(name='rcp-b', length=15.5, furcation_pos=13.6,
              pts_canal=buccal_post_rcp, pts_opposite=lingual_post_rcp,
              is_buccal_side=True, path=canal_rcp_path))

    s.canals.append(
        Canal(name='rcp-l', length=15.1, furcation_pos=12.7,
              pts_canal=lingual_post_rcp, pts_opposite=buccal_post_rcp,
              is_buccal_side=False, path=canal_rcp_path))

    specimens.append(s)

    for s in specimens:
        print('name : ' + s.name)
        for canal in s.canals:
            print(' canal name : ' + canal.name)
            print(' canal path : ' + canal.path)
            print(canal.pts_canal)

    print('pre : ')
    print([c.pts_canal for c in s.canals if c.name == 'pre-b'][0])

    print('rcp : ')
    print([c.pts_canal for c in s.canals if c.name == 'rcp-b'][0])
    

if __name__ == '__main__':
    #test()
    test2()
        


