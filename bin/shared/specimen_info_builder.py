
'''
2020.4.26
'''
from class_specimen import Canal


def fill_uninstrumented_specimen(meta_info, specimen, canals):
    """
    Uninstrumented canal 처리용
    :param meta_info:
    :param specimen:
    :param canals:
    :return:
    """

    specimen.body_path = specimen.get_default_path(meta_info['directory_name'], meta_info['body_suffix'])
    specimen.bounding_box = meta_info['bounding_box_range']
    specimen.magnification_ratio = meta_info['magnification_ratio']
    canal_path = specimen.get_default_path(meta_info['directory_name'], meta_info['canal_suffix'])

    for c in canals:
        specimen.canals.append(
            Canal(name=c['name'], furcation_pos=0.0 if not 'furcation_pos' in c.keys() else c['furcation_pos'],
                  cnls_cmp_name=None if not 'cnls_cmp_name' in c.keys() else c['cnls_cmp_name'],
                  pts_canal=c['pts_canal'],
                  pts_opposite=None if not 'pts_opposite' in c.keys() else c['pts_opposite'],
                  pts_vector=None if not 'pts_vector' in c.keys() else c['pts_vector'],
                  is_buccal_side=c['is_buccal_side'], path=canal_path)
        )

    return specimen


def fill_specimen(meta_info, specimen, canals):
    """
    Canal shaping data 처리용(Brazil)
    :param meta_info:
    :param specimen:
    :param canals:
    :return:
    """

    specimen.body_path = specimen.get_default_path(meta_info['directory_name'], meta_info['body_suffix'])
    specimen.bounding_box = meta_info['bounding_box_range']
    specimen.magnification_ratio = meta_info['magnification_ratio']
    canal_sound_file = specimen.get_default_path(meta_info['directory_name'], meta_info['canal_sound_suffix'])
    canal_first_file = specimen.get_default_path(meta_info['directory_name'], meta_info['canal_first_suffix'])
    canal_second_file = specimen.get_default_path(meta_info['directory_name'], meta_info['canal_second_suffix'])

    canal_list = meta_info['canal_list'] # sound, t04(reg), t06(S45)
    canal_file_list = [canal_sound_file, canal_first_file, canal_second_file]

    for c in canals:
        # sound, t04(reg), t06(S45) 인지 판별
        # canal name이 mb.sound, mb.t04, ml.reg 의 형식이라 가정
        canal_index = [i for i, canal_name in enumerate(canal_list) if c['name'].split('.')[-1] in canal_name][0]
        canal_path = canal_file_list[canal_index]
        specimen.canals.append(
            Canal(name=c['name'], furcation_pos=0.0 if not 'furcation_pos' in c.keys() else c['furcation_pos'],
                  cnls_cmp_name=None if not 'cnls_cmp_name' in c.keys() else c['cnls_cmp_name'],
                  pts_canal=c['pts_canal'],
                  pts_opposite=None if not 'pts_opposite' in c.keys() else c['pts_opposite'],
                  pts_vector=None if not 'pts_vector' in c.keys() else c['pts_vector'],
                  is_buccal_side=c['is_buccal_side'], path=canal_path)
        )

    return specimen


def fill_canals_for_sound(pts_canals, canal_list, is_buccal):

    SOUND, FIRST, SECOND = 0, 1, 2
    pts_mains = pts_canals['buccal'] if is_buccal else pts_canals['lingual']
    pts_subs = pts_canals['lingual'] if is_buccal else pts_canals['buccal']

    is_furcation_exist = (is_buccal and 'buccal_furcation' in pts_canals) or (not is_buccal and 'lingual_furcation' in pts_canals)
    furcation_main = 0.0 if not is_furcation_exist else pts_canals['buccal_furcation'] if is_buccal else pts_canals['lingual_furcation']

    is_buccal_side = True if is_buccal else False
    prefix_main = 'mb.' if is_buccal else 'ml.'
    prefix_sub = 'ml.' if is_buccal else 'mb.'
    # suffix(canal list)가 세개라고 가정하고
    canal_sound, canal_first, canal_second = canal_list

    canals = []

    # Canal(name='pre-mb', length=15.5, furcation_pos=13.6, cnls_cmp_name=['blx-mb', 'ptu-mb', 'rcp-mb'],
    #       pts_canal=buccal_pre, pts_opposite=lingual_pre,
    #       is_buccal_side=True, path=canal_pre_path))

    # canals.append({'name': 'mb.sound', 'cnls_cmp_name': ['mb.t04', 'mb.t06'],
    #                'pts_canal': mb_sound, 'pts_opposite': ml_sound, 'is_buccal_side': True})
    canals.append({'name': prefix_main+canal_sound, 'furcation_pos': furcation_main,
                   'cnls_cmp_name': [prefix_main+canal_first, prefix_main+canal_second],
                   'pts_canal': pts_mains[SOUND], 'pts_opposite': pts_subs[SOUND], 'is_buccal_side': is_buccal_side})

    # canals.append({'name': 'ml.sound',
    #                'pts_canal': ml_sound, 'pts_opposite': mb_sound, 'is_buccal_side': False})
    canals.append({'name': prefix_sub+canal_sound,
                   'pts_canal': pts_subs[SOUND], 'pts_opposite': pts_mains[SOUND], 'is_buccal_side': not is_buccal_side})

    # canals.append({'name': 'mb.t04',
    #                'pts_canal': mb_t04, 'pts_opposite': ml_sound, 'is_buccal_side': True})
    canals.append({'name': prefix_main+canal_first,
                   'pts_canal': pts_mains[FIRST], 'pts_opposite': pts_subs[SOUND], 'is_buccal_side': is_buccal_side})

    # canals.append({'name': 'mb.t06',
    #                'pts_canal': mb_t06, 'pts_opposite': ml_sound, 'is_buccal_side': True})
    canals.append({'name': prefix_main+canal_second,
                   'pts_canal': pts_mains[SECOND], 'pts_opposite': pts_subs[SOUND], 'is_buccal_side': is_buccal_side})

    return canals


def fill_canals_for_first_prep(pts_canals, canal_list, is_buccal):

    SOUND, FIRST, SECOND = 0, 1, 2
    pts_mains = pts_canals['buccal'] if is_buccal else pts_canals['lingual']
    pts_subs = pts_canals['lingual'] if is_buccal else pts_canals['buccal']
    is_buccal_side = True if is_buccal else False
    prefix_main = 'mb.' if is_buccal else 'ml.'
    prefix_sub = 'ml.' if is_buccal else 'mb.'
    canal_sound, canal_first, canal_second = canal_list

    is_furcation_exist = (is_buccal and 'buccal_furcation' in pts_canals) or (not is_buccal and 'lingual_furcation' in pts_canals)
    furcation_main = 0.0 if not is_furcation_exist else pts_canals['buccal_furcation'] if is_buccal else pts_canals['lingual_furcation']

    canals = []
    # canals.append({'name': 'mb.t04', 'cnls_cmp_name': ['mb.t06'],
    #               'pts_canal': mb_t04, 'pts_opposite': ml_sound, 'is_buccal_side': True})
    canals.append({'name': prefix_main+canal_first, 'furcation_pos': furcation_main,
                   'cnls_cmp_name': [prefix_main+canal_second],
                   'pts_canal': pts_mains[FIRST], 'pts_opposite': pts_subs[SOUND], 'is_buccal_side': is_buccal_side})

    # canals.append({'name': 'mb.t06',
    #                'pts_canal': mb_t06, 'pts_opposite': ml_sound, 'is_buccal_side': True})
    canals.append({'name': prefix_main+canal_second,
                   'pts_canal': pts_mains[SECOND], 'pts_opposite': pts_subs[SOUND], 'is_buccal_side': is_buccal_side})

    # canals.append({'name': 'ml.sound',
    #               'pts_canal': ml_sound, 'pts_opposite': mb_sound, 'is_buccal_side': False})
    canals.append({'name': prefix_sub+canal_sound,
                   'pts_canal': pts_subs[SOUND], 'pts_opposite': pts_mains[SOUND], 'is_buccal_side': not is_buccal_side})
    return canals

