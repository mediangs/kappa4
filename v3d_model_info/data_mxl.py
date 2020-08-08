'''
Created on 2014. 4. 9.

@author: jongki

total number of teeth : 8
Data from KUM2-11-07-20

'''
# -*- coding: cp949 -*-
import os
from constant import CONST
from class_specimen import Specimen
from specimen_info_builder import fill_uninstrumented_specimen


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

def get_meta_info():
    meta_info = {}
    meta_info['magnification_ratio'] = 1
    meta_info['directory_name'] = os.getenv('TOOTH_DATA') + '/v3d_mxl/'
    meta_info['bounding_box_range'] = [(-10, 20), (-10, 20), (-2, 28)]
    meta_info['canal_suffix'] = '-canal-zoff.v3d'
    meta_info['body_suffix'] = '-solid-body-zoff.v3d'
    return meta_info

def get_specimen_infos():
    infos=[]
    specimen_info = {'name':'MXL02', 'position': CONST.UR, 'note': '', 'weine_classification': None, 'canals':[] }
    pre_mb = '4.47211  3.15117  0.55702  4.44028  2.9761  0.97081  4.53577  2.89653  1.68699  4.58352  3.03976  2.78512  4.55169  3.13525  3.72411  4.50394  3.26257  5.02914  4.53577  3.24666  6.38191  4.50394  3.24666  7.4323  4.7745  3.07159  8.48269  4.94956  2.78512  9.51717  5.33152  2.14852  10.94952'
    pre_mb2 = '4.4562  3.13525  0.55702  4.4562  2.96019  1.12996  4.66309  2.92836  2.19627  4.99731  3.00793  3.32623  5.23603  3.13525  4.51986  5.69757  3.15117  5.61799  6.22276  3.15117  6.82753  6.19093  3.08751  7.92567  5.93629  2.92836  8.92831  5.7294  2.72146  9.70815  5.76123  2.40317  10.36066'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MXL03', 'position': CONST.UL, 'note': '', 'weine_classification': None, 'canals':[] }
    pre_mb = '3.43764  4.01058  1.30503  3.53313  3.74002  1.71882  3.66045  3.56496  2.24401  3.86734  3.45355  3.02385  4.09015  3.31032  4.09015  4.16973  3.24666  4.91773  4.20156  3.23074  5.88855  4.32888  3.32623  6.89119  4.39254  3.53313  7.86201  4.82224  3.931  8.78508  5.10871  4.29705  9.50125'
    pre_mb2 = '5.20421  4.20156  1.3846  5.07688  3.96283  1.67107  5.01322  3.72411  1.9098  4.93365  3.59679  2.40317  4.86999  3.5013  3.05568  4.96548  3.38989  3.77185  5.22012  3.31032  4.44028  5.49067  3.23074  5.17237  5.66574  3.19891  5.93629  5.74531  3.2944  6.77979  5.71348  3.45355  7.54371  5.68165  3.80368  8.3872  5.79306  4.28113  9.08746'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MXL04', 'position': CONST.UR, 'note': '', 'weine_classification': None, 'canals':[] }
    pre_mb = '5.15646  3.24666  1.05039  5.12463  3.42172  1.52784  5.10871  3.48538  2.24401  5.07688  3.56496  3.02385  4.98139  3.59679  3.80368  4.85407  3.58087  4.75858  4.90182  3.48538  5.66574  5.02914  3.34215  6.73204  5.0928  3.19891  7.86201  5.29969  3.03976  8.86465  5.53842  2.67372  10.05828  5.66574  2.64189  10.8222'
    pre_mb2 = '7.05034  3.42172  1.67107  6.98668  3.56496  2.10078  6.81162  3.64453  2.81695  6.65247  3.66045  3.54904  6.57289  3.64453  4.20156  6.366  3.62862  4.90182  6.30234  3.6127  5.57025  6.17502  3.58087  6.50923  6.60472  3.56496  7.48005  7.08217  3.54904  8.57818  7.27315  3.37398  9.37393  7.46413  3.16708  10.31292  8.08482  2.78512  11.1405'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MXL05', 'position': CONST.UL, 'note': '', 'weine_classification': None, 'canals':[] }
    pre_mb = '5.88855  2.81695  0.92307  6.01587  3.00793  1.55967  6.20685  2.94427  2.59414  6.33417  2.91245  3.45355  6.41374  2.88061  4.21747  6.55698  2.91245  4.8859  6.7957  2.8647  5.47476  6.82753  2.80104  6.14319  6.74796  2.73738  6.93894  6.57289  2.62597  7.73469  6.28642  2.45091  8.57818  5.93629  2.25993  9.40576  5.87263  1.83022  10.16968'
    pre_mb2 = '5.88855  2.81695  0.92307  5.87263  2.99202  1.79839  5.92038  2.92836  2.45091  5.88855  2.88061  3.32623  5.66574  2.91245  4.39254  5.34744  2.92836  5.0928  5.07688  2.9761  5.76123  4.85407  2.9761  6.76387  4.83816  2.84878  7.6392  4.58352  2.57823  8.3872  4.61535  2.19627  9.21478  4.71084  1.67107  10.32884'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MXL06', 'position': CONST.UR, 'note': '', 'weine_classification': None, 'canals':[] }
    pre_mb = '5.79306  3.51721  0.60477  5.76123  3.48538  0.81166  5.79306  3.43764  1.11405  5.95221  3.34215  1.79839  6.12727  3.183  2.35542  6.28642  3.03976  3.00793  6.42966  2.96019  3.70819  6.38191  2.94427  4.4562  6.28642  3.02385  5.07688  6.12727  3.15117  5.71348  5.85672  3.32623  6.46149  5.58616  3.54904  7.19358  5.33152  3.80368  7.87792  5.12463  4.28113  8.72142  5.14054  4.64718  9.35802'
    pre_mb2 = '4.31296  3.5013  1.35277  4.39254  3.43764  1.60741  4.47211  3.37398  1.94163  4.63127  3.26257  2.46682  4.71084  3.10342  3.10342  4.69492  3.00793  3.72411  4.66309  2.94427  4.36071  4.61535  3.00793  4.82224  4.48803  3.08751  5.69757  4.47211  3.26257  6.58881  4.44028  3.58087  7.44822  4.40846  3.94692  8.16439  4.47211  4.39254  8.86465  4.63127  4.71084  9.48534'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MXL07', 'position': CONST.UR, 'note': '', 'weine_classification': None, 'canals':[] }
    pre_mb = '2.48274  2.51457  0.748  2.56231  2.57823  0.89124  2.6578  2.72146  1.19362  2.83287  2.8647  1.54375  3.02385  2.94427  1.86205  3.2944  3.08751  2.2281  3.56496  3.21483  2.56231  3.77185  3.35806  3.00793  4.04241  3.5013  3.46947  4.28113  3.58087  3.97875  4.39254  3.6127  4.71084  4.23339  3.53313  5.50659  4.15381  3.46947  6.22276  4.23339  3.32623  6.98668  4.40846  3.11934  7.86201  4.55169  2.92836  8.48269  4.69492  2.76921  8.94423'
    pre_mb2 = '4.39254  2.43499  1.3846  4.4562  2.5464  1.57558  4.63127  2.70555  1.81431  4.82224  2.88061  2.08486  5.01322  3.11934  2.46682  5.02914  3.35806  2.91245  5.04505  3.51721  3.37398  5.15646  3.64453  3.80368  5.26786  3.69228  4.37662  5.45884  3.74002  4.98139  5.71348  3.74002  5.42701  5.90446  3.74002  5.8408  6.27051  3.70819  6.44557  6.52515  3.58087  6.89119  6.77979  3.34215  7.36864  7.03443  3.03976  7.83018  7.20949  2.72146  8.25988  7.3209  2.45091  8.73733'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MXL0A', 'position': CONST.UL, 'note': '', 'weine_classification': None, 'canals':[] }
    pre_mb = '5.10871  3.59679  0.89124  5.20421  3.43764  1.35277  5.31561  3.13525  1.94163  5.18829  2.92836  2.72146  5.29969  2.8647  3.85143  5.26786  2.83287  5.29969  5.29969  2.9761  6.31825  5.55433  3.2944  7.49596  5.80897  3.67636  8.37129  6.03178  4.07424  9.27844'
    pre_mb2 = '6.39783  3.48538  0.79575  6.28642  3.37398  1.16179  6.12727  3.15117  1.75065  6.0477  3.00793  2.43499  5.98404  2.94427  2.9761  5.69757  2.88061  3.89917  5.90446  2.84878  4.66309  6.17502  2.83287  5.44293  6.31825  2.91245  6.14319  6.58881  3.02385  6.76387  6.95485  3.23074  7.38456  7.12992  3.5013  8.00524  7.16175  3.72411  8.43495  7.0026  3.96283  9.00789'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MXL0B', 'position': CONST.UR, 'note': '', 'weine_classification': None, 'canals':[] }
    pre_mb = '4.59943  1.84614  1.0663  4.61535  2.1167  1.63924  4.64718  2.29176  2.18035  4.72675  2.53048  2.8647  4.83816  2.75329  3.94692  4.8859  2.89653  5.34744  4.80633  2.78512  6.30234  5.04505  2.53048  7.3209  5.33152  2.00529  8.2758  5.42701  1.67107  8.88057'
    pre_mb2 = '6.7957  2.56231  0.82758  6.71613  2.67372  1.2732  6.7957  2.80104  1.89388  6.85936  2.84878  2.53048  6.77979  2.92836  3.43764  7.0026  3.05568  4.66309  7.20949  3.03976  5.68165  7.14583  2.96019  6.38191  7.05034  2.72146  7.16175  6.77979  2.32359  8.00524  6.09544  1.7029  8.81691'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    infos.append(specimen_info)

    return infos


specimens = []

# 각 specimen의  데이터를 읽음
specimen_infos = get_specimen_infos()

# specimen전체에 적용되는 공통 정보들
meta_info = get_meta_info()

for sp_info in specimen_infos:
    s = Specimen(sp_info['name'])
    s.tooth_position = sp_info['position']
    s.note = sp_info['note']
    s.canal_type = sp_info['weine_classification']
    s.weine_classification = sp_info['weine_classification']
    s = fill_uninstrumented_specimen(meta_info, s, sp_info['canals'])
    specimens.append(s)

