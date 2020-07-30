# -*- coding: cp949 -*-

'''
Created on 2014. 4. 9.
changed on 2017.4.2.

@author: jongki

data from jongki(Mx6)
안동 장갑수 원장님의 치아
'''

import os
from constant import CONST
from class_specimen import Specimen
from specimen_info_builder import fill_uninstrumented_specimen



# ===============================================================================
#
# LEFT                              Cornal
#      .....                          ^
#     . DB  .                         |
#      .....         ...              |
#                  .     .            |
#                  .  P  .            |
#      ....          ...              |
#    .  MB  .                         |
#      ....                         Apical
#
# ===============================================================================

# ===============================================================================
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
# ===============================================================================

# =====================================================


def get_meta_info():
    meta_info = {}
    meta_info['magnification_ratio'] = 1
    meta_info['directory_name'] = os.getenv('TOOTH_DATA') + '/v3d_mx/'
    meta_info['bounding_box_range'] = [(-10, 20), (-10, 20), (-2, 28)]
    meta_info['canal_suffix'] = '-canal-zoff.v3d'
    meta_info['body_suffix'] = '-solid-body-zoff.v3d'
    return meta_info

    # directory_name = os.getenv('TOOTH_DATA') + '/v3d_mx/'
    # bounding_box_range = [(-10, 20), (-10, 20), (-2, 28)]
    # canal_suffix = '-canal-zoff.v3d'
    # body_suffix = '-solid-body-zoff.v3d'


def get_specimen_infos():
    infos=[]

    specimen_info = {'name':'MX01', 'position': CONST.UL, 'note': '13-4-14-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '2.07018  8.26119  18.1629  2.24595  8.30025  17.7723  2.42172  8.47602  17.30358  2.5389  8.61273  16.71768  2.49984  8.74944  15.58494  2.55843  8.84709  14.53032  2.65608  8.84709  13.59288  2.77326  8.76897  12.14766  2.94903  8.26119  9.80406  3.33963  7.89012  8.74944  3.57399  7.51905  8.0073  3.82788  7.24563  7.2261'
    pre_mb2 = '5.33169  8.7885  16.6005  5.2731  8.86662  16.0146  5.0778  9.04239  15.2334  5.01921  9.12051  14.60844  4.99968  9.1791  13.78818  5.0778  9.14004  12.6945  5.40981  9.10098  11.09304  5.87853  9.04239  10.1556  6.21054  8.76897  9.29628  6.32772  8.28072  8.63226  6.21054  7.6167  7.92918  5.76135  7.26516  7.06986'
    pre_p = '13.12416  4.53096  18.61209  13.14369  4.70673  18.04572  13.00698  4.72626  17.26452  12.67497  4.62861  15.85836  12.3039  4.78485  13.94442  11.79612  4.98015  12.26484  10.87821  5.09733  10.3509  9.68688  5.17545  8.5932  8.76897  5.03874  7.30422'
    pre_db = '4.14036  3.73023  18.31914  4.04271  3.80835  17.69418  3.86694  3.82788  17.10828  3.88647  3.82788  16.05366  3.906  3.69117  14.72562  3.98412  3.61305  13.31946  4.21848  3.74976  11.87424  4.66767  4.08177  10.58526  4.99968  4.55049  9.3744  5.01921  5.15592  7.96824'
    bl_vector = '3.59352 5.21451 10.11654 10.66338 5.21451 10.11654'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':7.9, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':10.4, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':8.8, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX02', 'position': CONST.UR, 'note': '13-4-14-check all', 'weine_classification': 4, 'canals':[] }
    pre_mb = '2.81232  3.88647  18.20196  2.96856  3.80835  17.88948  3.1248  3.57399  17.14734  3.18339  3.39822  16.32708  3.16386  3.30057  15.4287  3.00762  3.16386  14.41314  2.96856  3.1248  13.39758  3.20292  3.30057  12.38202  3.7107  3.73023  11.21022  4.15989  4.08177  10.38996  4.41378  4.60908  9.29628'
    pre_mb2 = '4.51143  4.12083  18.02619  4.43331  3.92553  17.577  4.39425  3.78882  17.26452  4.37472  3.61305  16.6005  4.27707  3.47634  15.31152  4.31613  3.39822  14.6475  4.51143  3.35916  13.98348  4.6872  3.37869  13.20228  4.70673  3.43728  12.18672  4.6872  3.84741  10.9368  4.4919  4.33566  9.88218  4.47237  4.62861  9.33534'
    pre_p = '9.45252  7.98777  17.34264  9.41346  7.87059  16.95204  9.25722  7.71435  16.2099  9.08145  7.57764  15.2334  8.80803  7.47999  13.94442  8.53461  7.46046  13.0851  7.98777  7.24563  11.87424  7.47999  7.01127  10.46808  7.14798  6.75738  9.1791'
    pre_db = '2.05065  8.49555  17.01063  2.08971  8.35884  16.63956  2.12877  8.2026  16.09272  2.3436  8.06589  15.2334  2.59749  7.89012  14.17878  3.06621  7.51905  12.85074  3.43728  7.26516  12.14766  4.02318  6.93315  11.21022  4.66767  6.60114  10.27278  5.03874  6.26913  9.33534'
    bl_vector = '3.63258 7.12845 11.79612 7.90965 7.34328 11.79612'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':7.1, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':6.8, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':7, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX03', 'position': CONST.UL, 'note': '13-4-21-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '2.10924  8.37837  16.30755  2.46078  8.3979  15.74118  2.77326  8.51508  15.27246  2.90997  8.65179  13.98348  3.33963  8.63226  12.96792  3.47634  8.53461  11.44458  3.82788  8.14401  9.92124  4.12083  7.77294  8.94474  4.45284  7.20657  8.24166'
    pre_mb2 = '3.78882  7.94871  16.56144  3.7107  8.22213  15.8193  3.7107  8.35884  15.19434  4.08177  8.33931  14.41314  4.04271  8.57367  13.2804  4.64814  8.49555  12.22578  5.37075  8.35884  11.3274  5.70276  8.08542  10.46808  5.50746  7.51905  9.33534  5.52699  7.0308  8.3979'
    pre_p = '10.87821  3.14433  18.53397  10.78056  3.37869  17.7723  10.60479  3.67164  16.75674  10.1556  4.04271  15.07716  9.70641  4.33566  13.39758  9.14004  4.57002  11.75706  8.53461  4.90203  10.11654  7.85106  5.21451  8.7885'
    pre_db = '1.52334  3.7107  16.05366  1.48428  3.82788  15.66306  1.67958  3.80835  15.15528  2.01159  3.73023  14.21784  2.24595  3.76929  13.2804  2.79279  4.02318  11.9133  3.26151  4.31613  10.85868  3.98412  4.99968  9.49158  4.6872  5.60511  8.55414'
    bl_vector = '3.32010 4.41378 10.60479 8.49555 4.45284 10.60479'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':6.8, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':7.7, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':9.6, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':6.8, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX04', 'position': CONST.UR, 'note': 'type 1 ?, 13-4-21-check all', 'weine_classification': 2, 'canals':[] }
    pre_mb = '3.53493  3.3201  14.68656  3.59352  3.3201  13.78818  3.53493  3.39822  12.92886  3.33963  3.5154  11.60082  3.20292  3.59352  10.31184  3.3201  3.74976  8.67132  3.57399  4.06224  7.4214  4.02318  4.4919  6.0543  4.14036  4.6872  5.2731'
    pre_mb2 = '3.53493  3.30057  14.66703  3.63258  3.33963  13.59288  3.5154  3.39822  12.61638  3.53493  3.37869  10.97586  3.88647  3.3201  9.25722  4.37472  3.28104  8.0073  4.51143  3.78882  6.67926  4.70673  4.2966  5.54652  5.21451  4.70673  4.72626'
    pre_db = '5.74182  9.04239  14.13972  5.76135  8.94474  13.63194  5.91759  8.86662  13.0851  5.95665  8.82756  12.18672  6.01524  8.65179  10.78056  5.95665  8.22213  9.1791  5.99571  7.79247  7.96824  6.13242  6.85503  6.2496  6.11289  6.23007  4.92156'
    pre_p = '13.90536  3.76929  14.99904  13.71006  3.84741  14.70609  13.37805  4.00365  13.8663  12.8898  4.04271  12.1086  12.32343  4.15989  10.19466  11.46411  4.33566  8.08542  10.40949  4.64814  6.17148  9.31581  5.09733  4.60908'
    bl_vector = '5.99571 6.77691 6.05430 10.09701 5.07780 6.05430'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.6, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':8.3, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':8.4, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':10.4, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX05', 'position': CONST.UR, 'note': '13-4-21-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '2.9295  7.49952  18.00666  2.87091  7.20657  17.42076  2.71467  6.91362  16.32708  2.7342  6.73785  15.07716  2.81232  6.58161  13.43664  2.87091  6.6402  12.03048  3.00762  6.75738  10.42902  3.80835  6.65973  8.90568  4.27707  6.67926  7.92918  4.6872  6.73785  7.06986'
    pre_mb2 = '3.73023  5.859  17.10828  3.80835  6.03477  16.52238  3.84741  5.72229  15.8193  3.7107  5.56605  14.29596  3.80835  5.39028  12.96792  4.14036  5.05827  11.95236  4.23801  5.11686  10.85868  4.55049  5.31216  9.80406  4.82391  5.60511  9.02286  5.13639  5.89806  8.28072  5.91759  6.23007  7.18704'
    pre_db = '6.40584  12.65544  17.65512  6.4449  12.22578  17.06922  6.30819  11.93283  16.24896  6.13242  11.5227  14.80374  6.21054  11.11257  12.96792  6.48396  10.50714  11.40552  6.46443  9.60876  9.765  6.48396  8.57367  8.35884  6.42537  7.59717  7.10892'
    pre_p = '13.33899  4.04271  17.98713  13.0851  3.86694  17.34264  12.77262  3.82788  16.4052  12.4992  3.92553  14.92092  12.06954  4.12083  12.96792  11.42505  4.41378  11.17116  10.60479  4.99968  9.45252  9.99936  5.17545  8.12448  9.45252  5.52699  7.0308'
    bl_vector = '6.15195 8.61273 8.90568 10.48761 5.68323 8.90568'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':10.6, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':9.1, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':10.5, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':10.6, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX06', 'position': CONST.UL, 'note': '', 'weine_classification': 1, 'canals':[] }
    pre_mb = '4.33566  9.10098  18.72927  4.58955  9.10098  18.39726  4.99968  9.31581  17.65512  5.48793  9.72594  16.6005  5.72229  9.99936  15.54588  5.80041  10.17513  14.0616  5.62464  10.25325  12.1086  5.42934  10.17513  10.46808  5.17545  9.82359  9.1791  5.09733  9.60876  8.16354'
    pre_db = '1.83582  4.8825  18.04572  1.93347  5.09733  17.65512  2.08971  5.21451  16.7958  2.49984  5.23404  15.624  2.98809  5.39028  14.10066  3.33963  5.6637  12.61638  3.78882  6.03477  11.05398  4.64814  6.65973  9.14004  5.03874  7.01127  8.31978'
    pre_p = '12.57732  1.5624  18.08478  12.6945  1.89441  17.577  12.40155  2.24595  16.48332  11.34693  2.85138  14.88186  10.50714  3.47634  12.8898  9.80406  4.06224  11.21022  8.9838  4.74579  9.3744  8.2026  5.35122  8.31978'
    bl_vector = '4.49190 6.58161 9.23769 8.78850 4.66767 9.23769'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.4, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':9.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':10.6, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX07', 'position': CONST.UR, 'note': '13-4-21-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '4.6872  4.8825  18.20196  4.70673  4.84344  17.61606  4.47237  4.78485  16.7958  4.17942  4.86297  15.97554  3.96459  4.90203  15.07716  3.63258  5.13639  13.82724  3.69117  5.40981  12.18672  4.04271  5.76135  10.50714  4.62861  6.03477  9.25722  5.05827  6.21054  8.16354'
    pre_mb2 = '6.21054  3.76929  16.07319  5.95665  3.78882  15.72165  5.70276  3.80835  15.21387  5.58558  3.76929  14.62797  5.56605  3.7107  13.92489  5.37075  3.86694  13.06557  5.17545  3.98412  12.42108  5.11686  4.25754  11.28834  5.13639  4.39425  10.50714  5.56605  4.99968  9.02286  5.78088  5.29263  8.3979'
    pre_db = '7.69482  8.63226  17.85042  7.30422  8.45649  17.03016  7.14798  8.33931  16.36614  7.06986  8.3979  15.38964  7.10892  8.49555  14.02254  7.2261  8.37837  12.6945  7.24563  8.0073  11.36646  7.20657  7.46046  10.03842  6.91362  6.97221  8.67132'
    pre_p = '16.03413  1.79676  18.61209  15.56541  1.64052  17.7723  14.82327  1.77723  16.6005  13.78818  2.26548  14.80374  12.92886  2.90997  12.8898  11.99142  3.59352  10.97586  11.21022  4.1013  9.5697  10.17513  5.03874  8.04636'
    bl_vector = '6.89409  7.44093  10.05795 11.52270  3.94506  10.05795'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.6, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':7.3, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':8.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':11.8, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX08', 'position': CONST.UL, 'note': '13-4-21-check all', 'weine_classification': 2, 'canals':[] }
    pre_mb = '2.85138  6.69879  17.65512  2.83185  6.99174  17.1864  3.02715  7.44093  16.36614  2.96856  7.73388  15.46776  2.59749  8.0073  14.4522  2.81232  8.04636  13.39758  3.00762  7.94871  11.79612  3.41775  7.51905  10.38996  3.7107  7.20657  9.25722  3.94506  6.91362  8.51508'
    pre_mb2 = '3.88647  7.16751  16.11225  4.35519  7.30422  15.50682  4.58955  7.40187  15.13575  4.76532  7.59717  14.35455  4.80438  7.71435  13.88583  4.90203  7.83153  13.14369  5.13639  7.87059  12.18672  5.09733  7.69482  10.85868  5.42934  7.28469  9.9603  5.76135  6.85503  9.21816  5.6637  6.19101  8.47602'
    pre_db = '2.69514  2.46078  16.77627  2.75373  2.69514  15.89742  2.90997  2.87091  14.92092  3.18339  3.10527  13.78818  3.61305  3.5154  12.38202  4.15989  3.96459  11.21022  4.94109  4.51143  9.84312  5.40981  4.76532  9.21816'
    pre_p = '11.36646  2.16783  18.49491  11.5227  2.46078  17.7723  11.48364  2.69514  16.9911  11.15163  3.06621  15.66306  10.46808  3.5154  13.78818  9.90171  3.84741  12.46014  8.88615  4.25754  10.1556  8.28072  4.35519  8.86662'
    bl_vector = '3.65211 4.21848 12.20625 9.19863 3.73023 12.20625'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':7.8, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':5.8, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':7.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':9.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX09', 'position': CONST.UL, 'note': '13-4-21-check all', 'weine_classification': 2, 'canals':[] }
    pre_mb = '5.44887  7.08939  17.26452  5.62464  7.36281  16.83486  5.54652  7.59717  16.28802  5.56605  7.73388  15.70212  5.64417  7.85106  14.72562  5.48793  7.94871  13.4757  5.25357  7.94871  12.65544  4.92156  7.83153  11.83518  4.92156  7.65576  11.05398  5.01921  7.38234  10.11654  4.86297  6.93315  8.94474'
    pre_mb2 = '7.0308  7.4214  17.06922  6.99174  7.53858  16.71768  6.8355  7.6167  16.30755  6.77691  7.67529  15.85836  6.48396  7.79247  15.27246  6.0543  7.87059  14.41314  5.97618  7.98777  13.39758  6.21054  8.04636  12.38202  6.32772  7.98777  11.40552  6.11289  7.79247  10.50714  6.09336  7.51905  9.5697  6.30819  7.28469  9.06192  6.48396  7.14798  8.74944'
    pre_db = '5.76135  2.67561  17.55747  5.83947  2.96856  16.87392  5.97618  3.16386  15.97554  5.95665  3.28104  15.19434  5.87853  3.41775  14.10066  5.83947  3.65211  13.04604  5.91759  3.98412  11.75706  5.97618  4.33566  10.70244  5.99571  4.72626  9.765  5.72229  5.31216  8.63226'
    pre_p = '15.99507  4.14036  18.78786  15.54588  4.53096  17.73324  14.99904  4.78485  16.36614  14.02254  4.90203  14.6475  12.83121  5.13639  12.61638  12.05001  5.2731  11.44458  10.83915  5.35122  9.765  9.78453  5.40981  8.3979'
    bl_vector = '6.24960 5.31216 9.64782 10.35090 5.39028 9.64782'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':7.6, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':6.8, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':7.8, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':11.6, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX10', 'position': CONST.UR, 'note': '13-4-21-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '2.87091  3.43728  17.59653  2.87091  3.37869  17.1864  2.9295  3.24198  16.75674  2.94903  3.22245  16.13178  2.96856  3.24198  15.35058  3.02715  3.30057  14.6475  3.35916  3.35916  13.43664  3.53493  3.5154  12.38202  3.69117  3.73023  11.28834  4.06224  4.06224  9.99936  4.33566  4.27707  9.14004'
    pre_mb2 = '2.87091  3.43728  17.59653  2.87091  3.37869  17.1864  2.9295  3.24198  16.75674  2.94903  3.22245  16.13178  2.96856  3.24198  15.35058  3.02715  3.30057  14.6475  3.35916  3.35916  13.43664  3.53493  3.5154  12.38202  3.69117  3.73023  11.28834  4.06224  4.06224  9.99936  4.33566  4.27707  9.14004'
    pre_db = '4.66767  8.51508  16.83486  4.47237  8.43696  16.52238  4.39425  8.35884  15.97554  4.57002  8.10495  15.19434  4.86297  7.77294  13.8663  5.09733  7.24563  12.26484  5.42934  6.85503  11.3274  5.68323  6.52302  10.46808  5.72229  6.23007  9.5697'
    pre_p = '12.51873  4.43331  18.26055  12.40155  4.57002  17.69418  12.14766  4.57002  17.10828  11.79612  4.6872  15.97554  11.40552  4.90203  14.60844  10.83915  5.09733  13.04604  9.97983  5.23404  11.17116  9.00333  5.33169  9.53064'
    bl_vector = '5.48793 6.23007 10.72197 10.01889 5.33169 10.72197'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':6.8, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':4.9, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':6.8, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':8.4, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX11', 'position': CONST.UL, 'note': '13-4-28-check all', 'weine_classification': 2, 'canals':[] }
    pre_mb = '2.18736  6.32772  17.86995  2.44125  6.42537  16.9911  2.79279  6.52302  16.0146  2.98809  6.58161  14.72562  3.06621  6.60114  13.2804  3.08574  6.48396  12.03048  3.59352  6.15195  10.66338  4.04271  5.83947  9.88218  4.31613  5.48793  9.10098'
    pre_mb2 = '3.35916  6.52302  17.92854  3.20292  6.50349  17.42076  3.02715  6.6402  16.44426  3.18339  6.67926  15.46776  3.74976  6.8355  14.2569  4.53096  7.01127  13.59288  5.17545  7.14798  12.6945  5.52699  7.06986  11.87424  5.78088  6.69879  10.9368  5.97618  6.13242  9.9603  6.23007  5.76135  9.49158'
    pre_db = '2.10924  1.38663  17.42076  2.46078  1.66005  16.56144  2.9295  1.89441  15.4287  3.43728  2.18736  14.0616  4.14036  2.59749  12.57732  4.57002  3.18339  11.17116  5.01921  3.69117  9.72594'
    pre_p = '11.22975  4.39425  16.52238  11.05398  4.57002  15.0381  10.60479  4.78485  13.16322  9.82359  4.76532  11.21022  8.84709  4.80438  9.49158'
    bl_vector = '4.17942 4.23801 10.83915 8.88615 4.55049 10.83915'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.2, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':7.7, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':7.6, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':6.3, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX12', 'position': CONST.UR, 'note': '1-2-1 type, 13-4-28-check all', 'weine_classification': 2, 'canals':[] }
    pre_mb = '5.2731  4.27707  18.41679  5.13639  4.12083  18.00666  5.01921  3.84741  17.65512  4.66767  3.53493  16.83486  4.47237  3.55446  16.05366  4.41378  3.59352  14.99904  4.25754  3.74976  13.98348  4.1013  3.88647  13.59288  4.02318  4.00365  13.00698  3.84741  4.27707  12.18672  3.73023  4.51143  11.36646  3.96459  4.58955  10.42902  4.41378  4.62861  9.72594  4.98015  4.64814  8.94474  5.39028  4.76532  8.28072  5.52699  4.94109  7.6167'
    pre_mb2 = '5.25357  4.25754  18.39726  5.11686  4.1013  17.9676  4.99968  3.74976  17.577  4.82391  3.35916  16.87392  4.99968  2.98809  16.0146  5.09733  2.89044  14.99904  4.96062  3.08574  14.2569  4.84344  3.24198  13.55382  5.0778  3.28104  12.1086  5.19498  3.37869  11.09304  5.21451  4.06224  9.60876  5.33169  4.66767  8.51508  5.37075  4.76532  8.24166'
    pre_db = '7.2261  8.47602  16.85439  7.16751  8.31978  16.4052  7.06986  8.0073  15.93648  6.93315  7.67529  15.0381  6.87456  7.46046  14.02254  6.81597  7.2261  12.96792  6.79644  6.95268  11.75706  6.91362  6.67926  10.78056  6.77691  6.15195  9.765  6.81597  5.29263  8.43696'
    pre_p = '13.41711  2.28501  17.7723  13.26087  1.99206  17.1864  13.0851  1.953  16.6005  12.96792  2.10924  15.93648  12.59685  2.22642  14.76468  12.03048  2.48031  13.31946  11.42505  2.79279  11.99142  10.42902  3.22245  10.3509  9.43299  3.86694  8.7885  8.72991  4.23801  7.77294'
    bl_vector = '6.34725 5.52699 9.17910 9.78453 3.86694 9.17910'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':10.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':9.2, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':7.8, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':10.2, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX13', 'position': CONST.UL, 'note': '13-4-28-check all', 'weine_classification': 2, 'canals':[] }
    pre_mb = '3.96459  8.43696  18.31914  4.02318  8.61273  17.7723  4.27707  8.74944  17.26452  4.4919  8.71038  16.71768  4.4919  8.86662  15.97554  4.45284  9.04239  15.11622  4.51143  9.21816  14.02254  4.60908  9.39393  12.65544  4.58955  9.43299  11.718  4.58955  9.27675  10.38996  4.66767  8.9838  9.3744  4.74579  8.45649  8.24166  4.6872  8.14401  7.46046'
    pre_mb2 = '3.96459  8.43696  18.29961  4.21848  8.74944  17.34264  4.57002  8.67132  16.75674  5.15592  8.69085  16.17084  5.54652  8.74944  15.54588  5.80041  8.76897  15.11622  5.89806  8.90568  14.2569  5.76135  9.06192  13.31946  5.70276  9.12051  12.26484  6.01524  9.00333  11.3274  6.23007  8.7885  10.3509  6.23007  8.31978  9.21816  5.72229  8.18307  8.55414  5.39028  7.77294  7.73388'
    pre_db = '2.94903  4.6872  17.83089  2.98809  4.80438  17.22546  3.10527  4.96062  16.52238  3.20292  5.0778  15.85836  3.3201  5.0778  14.76468  3.43728  4.94109  13.35852  3.69117  4.90203  12.06954  4.02318  5.03874  10.7415  4.55049  5.25357  9.49158  5.05827  5.58558  7.96824'
    pre_p = '11.93283  2.44125  18.53397  11.97189  2.46078  17.65512  11.85471  2.51937  16.32708  11.50317  2.67561  15.2334  11.17116  3.06621  13.74912  10.64385  3.43728  12.22578  9.53064  4.12083  9.92124  8.24166  4.64814  7.65576'
    bl_vector = '4.68720 6.32772 8.51508 8.59320 4.47237 8.51508'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.8, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':9.7, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':8.6, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':11.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX14', 'position': CONST.UL, 'note': '13-4-28-check all', 'weine_classification': 4, 'canals':[] }
    pre_mb = '9.5697  3.84741  18.45585  9.49158  3.94506  18.08478  9.53064  4.25754  17.49888  9.62829  4.45284  16.71768  9.62829  4.45284  15.78024  9.66735  4.57002  14.8428  9.72594  4.74579  13.78818  9.60876  4.92156  13.04604  8.82756  5.25357  11.75706  7.6167  5.54652  10.38996'
    pre_mb2 = '7.85106  2.89044  18.51444  7.85106  3.02715  18.22149  7.812  3.20292  17.83089  7.79247  3.30057  17.22546  7.812  3.35916  16.28802  7.92918  3.49587  15.4287  7.812  3.55446  14.56938  7.67529  3.57399  13.671  7.57764  3.74976  12.85074  7.57764  4.15989  12.22578  7.92918  4.84344  11.48364  7.89012  5.6637  10.58526'
    pre_db = '7.94871  10.33137  18.04572  7.71435  9.88218  17.3817  7.63623  9.1791  16.24896  7.67529  8.63226  14.68656  7.75341  8.06589  13.39758  7.75341  7.38234  12.42108  7.812  6.54255  11.56176  7.71435  5.64417  10.3509'
    pre_p = '2.28501  3.5154  18.5535  2.3436  3.67164  17.88948  2.59749  3.94506  16.71768  2.89044  4.12083  15.2334  3.35916  4.31613  13.35852  3.86694  4.4919  11.9133  5.03874  4.92156  10.31184'
    bl_vector = '8.33931 6.38631 12.88980 4.23801 5.07780 12.88980'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':6.7, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':6.3, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':7.4, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':7.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX15', 'position': CONST.UL, 'note': '', 'weine_classification': 1, 'canals':[] }
    pre_mb = '6.38631  5.6637  17.45982  6.09336  6.15195  16.75674  5.93712  6.6402  15.66306  5.70276  7.16751  13.82724  5.56605  7.34328  12.65544  5.33169  7.26516  10.62432  5.09733  7.01127  9.5697'
    pre_db = '4.33566  4.19895  17.577  4.15989  4.25754  16.87392  4.19895  4.41378  15.66306  4.21848  4.37472  14.8428  4.33566  4.41378  13.39758  4.43331  4.58955  12.53826  4.82391  5.01921  10.85868  4.98015  5.78088  9.68688'
    pre_p = '13.92489  2.65608  18.39726  13.53429  2.87091  17.49888  12.92886  3.10527  16.32708  12.12813  3.35916  14.76468  11.09304  3.5154  13.04604  9.99936  3.76929  11.75706  9.35487  3.96459  10.78056  8.88615  4.15989  9.72594  8.18307  4.62861  8.86662'
    bl_vector = '4.99968 5.83947 9.90171 8.80803 4.99968 9.90171'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':7.2, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':9.8, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX16', 'position': CONST.UR, 'note': '13-4-28-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '4.70673  5.19498  17.98713  4.58955  5.15592  17.55747  4.51143  4.94109  17.12781  4.47237  4.62861  16.65909  4.2966  4.47237  15.95601  4.06224  4.4919  15.01857  3.98412  4.55049  13.92489  3.96459  4.80438  12.63591  4.17942  5.01921  11.34693  4.41378  5.17545  10.33137  4.74579  5.48793  9.27675  4.82391  5.83947  8.61273'
    pre_mb2 = '6.21054  3.78882  16.63956  5.87853  3.67164  15.97554  5.58558  3.55446  15.25293  5.52699  3.45681  14.51079  5.39028  3.47634  13.45617  5.48793  3.45681  12.20625  5.6637  3.47634  11.38599  5.80041  3.47634  10.95633  5.81994  3.53493  10.5462  5.87853  3.65211  10.17513  5.95665  3.96459  9.66735  6.15195  4.25754  9.23769  6.46443  4.80438  8.33931'
    pre_db = '7.14798  8.37837  17.88948  7.18704  8.06589  17.30358  7.12845  7.94871  16.48332  7.01127  7.96824  15.31152  6.97221  7.90965  14.0616  6.97221  7.55811  12.6945  7.0308  7.16751  11.44458  6.81597  6.71832  10.1556  6.52302  6.52302  9.14004'
    pre_p = '13.90536  1.93347  18.43632  13.74912  1.97253  17.61606  13.43664  1.93347  16.63956  13.0851  2.22642  15.35058  12.46014  2.65608  13.78818  11.36646  3.18339  11.75706  10.68291  3.63258  10.50714  9.5697  4.58955  8.67132'
    bl_vector = '6.91362 6.30819 10.37043 10.44855 4.25754 10.37043'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.3, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':6.8, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':8.2, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':10.2, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX17', 'position': CONST.UL, 'note': '13-4-28-check all', 'weine_classification': 2, 'canals':[] }
    pre_mb = '5.78088  7.85106  17.40123  5.70276  8.45649  16.56144  5.60511  8.96427  15.31152  5.50746  9.1791  13.94442  5.48793  9.06192  12.42108  5.58558  8.67132  11.01492  5.68323  7.89012  9.68688  5.6637  7.55811  8.7885'
    pre_mb2 = '5.76135  7.83153  17.3817  5.859  8.16354  16.87392  6.19101  8.57367  15.78024  6.28866  8.74944  14.88186  6.38631  8.7885  13.90536  6.77691  8.65179  12.92886  6.95268  8.51508  11.87424  7.0308  8.18307  10.81962  6.71832  7.69482  9.80406  6.50349  7.40187  9.29628  6.30819  7.36281  8.63226  6.38631  7.6167  8.12448'
    pre_db = '3.96459  4.90203  17.69418  3.96459  5.15592  17.26452  3.906  5.33169  16.71768  3.906  5.44887  16.09272  3.84741  5.50746  15.2334  3.78882  5.39028  14.2569  3.96459  5.31216  12.81168  4.51143  5.54652  11.28834  5.03874  5.93712  10.23372  5.54652  6.42537  9.41346'
    pre_p = '11.69847  2.40219  18.3582  11.67894  2.49984  17.81136  11.50317  2.71467  16.75674  11.17116  2.85138  15.4287  10.68291  3.08574  13.78818  10.05795  3.49587  12.1086  9.27675  4.12083  10.19466  8.3979  4.72626  8.63226'
    bl_vector = '4.98015 6.01524 10.99539 9.33534 4.41378 10.99539'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.2, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':7.4, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':7.8, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':9.4, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX18', 'position': CONST.UR, 'note': '13-4-28-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '4.78485  4.84344  17.7723  4.72626  4.84344  17.1864  4.58955  4.82391  16.36614  4.2966  4.8825  15.50682  3.69117  5.17545  14.02254  3.49587  5.44887  12.53826  3.74976  5.64417  11.40552  4.39425  5.95665  10.19466  4.84344  6.07383  9.53064'
    pre_mb2 = '5.60511  4.1013  17.08875  5.44887  4.21848  16.32708  5.0778  4.31613  15.8193  4.62861  4.4919  14.95998  4.55049  4.35519  13.39758  5.19498  3.74976  11.67894  5.50746  3.86694  10.70244  5.48793  4.94109  9.41346  5.56605  5.44887  8.7885'
    pre_db = '6.13242  9.21816  17.24499  6.11289  9.15957  16.71768  6.17148  9.08145  15.97554  6.26913  9.00333  14.80374  6.26913  8.86662  13.4757  6.32772  8.47602  12.3039  6.32772  8.08542  11.48364  6.19101  7.57764  10.42902  6.13242  7.20657  9.60876'
    pre_p = '12.18672  2.85138  18.37773  12.06954  2.81232  17.7723  11.87424  2.90997  17.06922  11.60082  3.20292  15.85836  11.28834  3.5154  14.41314  10.83915  3.88647  12.4992  10.27278  4.31613  10.85868  9.06192  5.01921  8.82756'
    bl_vector = '5.91759 7.26516 10.38996 9.84312 4.90203 10.38996'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.6, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':7.3, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':7.6, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':9.8, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX19', 'position': CONST.UL, 'note': '13-4-28-check all', 'weine_classification': 2, 'canals':[] }
    pre_mb = '4.55049  8.49555  18.3582  4.66767  8.65179  17.73324  4.76532  8.74944  16.9911  4.86297  8.92521  16.2099  4.84344  9.3744  15.35058  4.99968  9.64782  14.33502  5.17545  9.9603  13.20228  5.15592  10.19466  12.34296  5.09733  10.37043  10.78056  5.19498  10.03842  9.92124  5.29263  9.60876  9.21816  5.37075  9.10098  8.28072  5.37075  9.00333  7.812'
    pre_mb2 = '4.55049  8.49555  18.33867  4.62861  8.65179  17.85042  4.82391  8.74944  16.7958  5.42934  8.57367  15.78024  5.93712  8.30025  15.2334  6.11289  8.43696  14.76468  6.23007  8.53461  14.17878  6.19101  8.90568  13.4757  6.48396  8.94474  12.77262  7.12845  8.74944  11.718  7.46046  8.51508  10.66338  7.47999  8.28072  9.765  7.16751  7.98777  8.94474  6.73785  7.77294  8.16354  6.46443  7.6167  7.69482'
    pre_db = '1.52334  6.46443  16.71768  1.79676  6.6402  15.93648  2.03112  6.54255  14.88186  2.32407  6.40584  13.71006  2.77326  6.26913  12.38202  3.45681  6.40584  10.58526  4.45284  6.87456  8.82756  4.96062  7.12845  7.92918'
    pre_p = '10.40949  1.5624  16.9911  10.37043  1.79676  16.28802  10.19466  2.16783  15.35058  9.78453  2.40219  14.10066  9.1791  2.69514  12.61638  8.67132  3.28104  10.58526  8.04636  3.65211  9.02286  7.71435  4.12083  7.69482'
    bl_vector = '4.58955 6.85503 8.41743 8.06589 3.80835 8.41743'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.6, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':9.9, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':7.6, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':8.8, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX20', 'position': CONST.UR, 'note': '13-4-28-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '4.57002  5.15592  18.12384  4.21848  4.8825  17.53794  4.02318  4.76532  17.06922  3.84741  4.80438  16.28802  3.69117  4.90203  15.35058  3.55446  5.0778  14.10066  3.86694  5.37075  12.06954  4.6872  5.6637  10.11654  4.99968  5.80041  9.45252'
    pre_mb2 = '5.81994  3.26151  17.10828  5.76135  3.22245  16.71768  5.48793  3.30057  16.4052  5.2731  3.3201  15.54588  5.2731  3.37869  14.76468  5.44887  3.3201  13.82724  5.35122  3.55446  13.00698  5.48793  3.84741  11.99142  5.70276  4.4919  10.66338  6.21054  4.99968  9.29628'
    pre_db = '7.79247  9.19863  18.20196  7.55811  9.21816  17.69418  7.2261  9.06192  16.7958  7.08939  9.02286  15.70212  7.05033  8.88615  14.41314  6.95268  8.61273  13.00698  6.8355  8.04636  11.48364  6.65973  7.24563  10.23372  6.48396  6.71832  9.33534'
    pre_p = '13.92489  2.01159  18.14337  13.53429  1.99206  17.3817  12.92886  2.16783  16.52238  12.57732  2.36313  15.2334  12.01095  2.77326  13.59288  11.40552  3.22245  12.3039  10.60479  3.7107  11.09304  9.82359  4.15989  9.92124  9.19863  4.35519  9.10098'
    bl_vector = '6.28866 6.79644 10.50714 10.09701 4.27707 10.50714'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.6, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':6.8, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':8.4, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':9.8, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX21', 'position': CONST.UR, 'note': '13-4-28-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '2.69514  5.17545  17.26452  3.02715  5.03874  16.44426  3.00762  5.15592  15.78024  2.7342  5.35122  14.53032  2.5389  5.56605  13.00698  2.7342  5.74182  11.63988  3.20292  5.81994  10.42902  3.80835  5.93712  9.1791  4.00365  6.0543  8.74944'
    pre_mb2 = '3.74976  4.47237  16.56144  3.67164  4.60908  16.13178  3.63258  4.6872  15.70212  3.92553  4.51143  15.0381  4.21848  4.27707  14.29596  4.2966  4.14036  13.12416  4.27707  4.17942  12.14766  4.53096  4.04271  11.24928  4.92156  4.04271  10.23372  5.25357  4.33566  9.60876  5.2731  5.09733  8.82756  5.21451  5.4684  8.47602'
    pre_db = '4.96062  8.63226  17.28405  5.05827  8.55414  16.36614  5.31216  8.51508  15.35058  5.62464  8.41743  14.0616  5.89806  8.12448  12.4992  5.74182  7.53858  10.62432  5.80041  6.71832  8.82756'
    pre_p = '10.89774  2.05065  17.94807  10.81962  2.42172  16.48332  10.60479  3.08574  14.80374  10.23372  3.63258  12.65544  9.72594  4.17942  10.9368  9.31581  4.57002  9.84312  8.82756  4.96062  8.63226'
    bl_vector = '5.62464 7.34328 10.19466 9.27675 5.07780 10.19466'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':7.6, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':7.3, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':7.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':9.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX22', 'position': CONST.UR, 'note': '', 'weine_classification': 1, 'canals':[] }
    pre_mb = '2.26548  4.15989  17.53794  2.49984  4.00365  16.9911  2.57796  3.84741  16.13178  2.69514  3.61305  14.53032  2.94903  3.30057  12.92886  3.20292  3.3201  10.66338  3.88647  3.98412  8.3979  4.25754  4.45284  7.49952'
    pre_db = '3.08574  8.26119  17.53794  3.24198  8.24166  16.95204  3.5154  8.30025  16.28802  3.82788  8.2026  15.19434  4.15989  8.06589  13.94442  4.41378  7.83153  12.73356  4.66767  7.40187  11.28834  4.86297  6.95268  10.19466  5.11686  6.40584  9.02286  5.29263  5.72229  7.77294'
    pre_p = '10.58526  3.35916  18.67068  10.7415  3.47634  17.81136  10.83915  3.65211  16.87392  10.85868  3.96459  15.54588  10.68291  4.19895  14.13972  10.37043  4.2966  12.6945  9.64782  4.47237  10.62432  8.84709  4.72626  9.06192  8.31978  4.8825  8.12448'
    bl_vector = '5.48793 6.13242 8.63226 8.63226 5.07780 8.63226'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':8.8, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':10.4, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX23', 'position': CONST.UL, 'note': '13-4-28-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '4.62861  10.31184  17.81136  4.62861  10.46808  17.59653  4.64814  10.72197  17.36217  4.80438  10.76103  17.01063  5.0778  10.66338  16.38567  5.11686  10.62432  15.40917  4.94109  10.70244  14.27643  4.70673  10.72197  12.79215  4.58955  10.60479  11.42505  4.58955  10.25325  9.94077  4.74579  9.765  8.7885  4.76532  9.5697  8.28072  4.72626  9.23769  7.6167'
    pre_mb2 = '6.69879  9.90171  16.7958  6.67926  10.01889  16.58097  6.58161  10.17513  16.17084  6.50349  10.23372  15.87789  6.30819  10.23372  15.25293  6.21054  10.19466  14.66703  6.52302  9.94077  13.10463  6.91362  9.66735  12.08907  7.01127  9.39393  10.80009  7.0308  9.04239  9.62829  6.89409  8.7885  8.96427  6.56208  8.5932  8.37837  6.34725  8.41743  7.87059  6.34725  8.16354  7.44093'
    pre_db = '0.89838  5.31216  16.89345  1.23039  5.44887  16.44426  1.71864  5.72229  15.54588  2.20689  5.83947  14.29596  2.51937  5.859  12.81168  3.08574  5.89806  11.1321  3.5154  6.07383  9.99936  4.06224  6.26913  8.82756  4.4919  6.56208  7.69482'
    pre_p = '11.62035  2.98809  16.67862  11.40552  3.06621  15.93648  11.17116  3.26151  14.72562  10.91727  3.41775  13.43664  10.66338  3.63258  12.1086  10.38996  3.94506  11.01492  9.90171  4.27707  9.88218  9.23769  4.57002  8.55414  8.45649  5.23404  7.10892'
    bl_vector = '4.23801 6.69879 8.10495 8.04636 4.62861 8.10495'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.6, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':8.1, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':9.4, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':9.8, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX24', 'position': CONST.UL, 'note': '13-4-28-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '4.31613  7.87059  17.65512  4.33566  8.18307  16.83486  4.35519  8.5932  15.78024  4.41378  8.96427  14.10066  4.51143  9.06192  12.61638  4.55049  9.02286  10.97586  4.58955  8.84709  9.41346  4.6872  8.65179  8.63226  4.82391  8.24166  7.812  4.64814  7.69482  6.77691'
    pre_mb2 = '6.21054  6.77691  16.38567  6.52302  7.14798  15.66306  6.8355  7.47999  14.80374  6.81597  7.79247  13.63194  6.69879  7.98777  12.42108  6.71832  8.02683  10.9368  6.81597  7.85106  9.64782  6.85503  7.49952  8.67132  6.62067  7.05033  7.6167  6.38631  6.48396  6.56208'
    pre_db = '2.7342  4.1013  16.91298  2.79279  4.47237  16.44426  2.69514  4.6872  15.8193  2.69514  4.74579  14.95998  2.81232  4.6872  13.24134  3.02715  4.66767  11.79612  3.35916  4.90203  10.50714  3.80835  5.15592  9.33534  4.27707  5.50746  8.2026  4.55049  6.15195  6.87456'
    pre_p = '10.05795  3.10527  18.98316  10.21419  3.10527  17.88948  10.31184  2.83185  16.83486  10.48761  2.77326  15.70212  10.48761  2.7342  14.49126  10.17513  3.00762  12.65544  9.62829  3.37869  10.97586  9.06192  3.74976  9.41346  8.55414  4.06224  8.0073  8.12448  4.45284  6.87456'
    bl_vector = '5.05827 6.15195 7.24563 8.10495 4.31613 7.24563'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.4, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':8.4, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':9.4, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':11.6, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX25', 'position': CONST.UL, 'note': '', 'weine_classification': 2, 'canals':[] }
    pre_mb = '4.25754  8.88615  17.42076  4.15989  8.67132  17.06922  4.1013  8.53461  16.4052  4.19895  8.53461  15.4287  4.19895  8.57367  14.37408  4.33566  8.61273  13.35852  4.84344  8.71038  12.03048  5.29263  8.67132  10.5462  5.11686  8.3979  9.3744  5.19498  7.85106  8.31978  5.19498  6.95268  6.79644'
    pre_mb2 = '6.21054  6.77691  16.38567  6.52302  7.14798  15.66306  6.8355  7.47999  14.80374  6.81597  7.79247  13.63194  6.69879  7.98777  12.42108  6.71832  8.02683  10.9368  6.81597  7.85106  9.64782  6.85503  7.49952  8.67132  6.62067  7.05033  7.6167  6.38631  6.48396  6.56208'
    pre_db = '2.96856  3.53493  17.22546  3.08574  3.61305  16.36614  3.37869  3.57399  15.54588  3.76929  3.55446  14.21784  4.00365  3.76929  12.85074  4.31613  4.1013  11.56176  4.86297  4.84344  9.64782  5.11686  5.64417  7.89012'
    pre_p = '12.57732  4.08177  18.47538  12.36249  4.15989  17.577  12.16719  4.19895  16.2099  11.77659  4.41378  14.60844  11.3274  4.58955  12.96792  10.66338  4.8825  11.17116  9.60876  5.23404  9.3744  8.76897  5.4684  7.77294'
    bl_vector = '4.02318 6.21054 9.64782 9.55017 6.28866 9.64782'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.2, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':8.9, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':10.8, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX26', 'position': CONST.UL, 'note': '13-4-28-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '2.36313  7.14798  17.83089  2.36313  7.34328  17.1864  2.42172  7.51905  16.56144  2.59749  7.77294  15.85836  3.04668  7.85106  14.72562  3.20292  7.92918  13.671  3.24198  7.90965  12.14766  3.41775  7.75341  10.89774  3.57399  7.4214  9.72594  3.73023  7.2261  9.1791  4.1013  6.93315  8.47602'
    pre_mb2 = '4.41378  7.4214  17.71371  4.39425  7.59717  16.95204  4.43331  7.75341  16.09272  4.51143  7.83153  15.31152  4.21848  7.87059  14.72562  4.04271  7.90965  13.4757  4.31613  7.90965  12.38202  4.78485  7.73388  11.1321  5.2731  7.40187  10.46808  5.58558  6.75738  9.72594  5.6637  6.4449  8.90568  5.62464  6.34725  8.49555'
    pre_db = '1.73817  1.7577  17.65512  1.7577  2.07018  17.03016  2.01159  2.46078  16.17084  2.30454  2.65608  15.19434  2.65608  3.02715  13.90536  3.08574  3.45681  12.4992  3.65211  3.906  11.3274  4.04271  4.14036  10.81962  4.62861  4.72626  10.03842  4.78485  5.03874  9.41346'
    pre_p = '11.95236  2.79279  18.24102  11.60082  3.06621  17.1864  11.01492  3.24198  15.93648  10.46808  3.49587  14.13972  9.72594  3.78882  12.61638  8.71038  4.1013  10.97586  7.90965  4.53096  9.3744'
    bl_vector = '3.24198 5.58558 10.25325 8.51508 4.70673 10.25325'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':8.8, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':9.2, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':9.8, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX27', 'position': CONST.UR, 'note': 'mb root: 3 canals, 13-4-28-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '1.38663  5.44887  17.71371  1.19133  5.33169  17.30358  1.15227  5.21451  16.75674  1.19133  5.01921  15.89742  1.46475  4.82391  14.95998  1.83582  4.57002  14.21784  2.01159  4.55049  13.43664  2.3436  4.62861  12.4992  2.49984  4.55049  11.67894  3.28104  4.6872  10.58526  3.78882  4.82391  10.13607  4.17942  4.94109  9.53064'
    pre_mb2 = '3.61305  3.76929  16.62003  3.7107  3.67164  16.17084  3.82788  3.5154  15.54588  4.04271  3.37869  14.8428  4.27707  3.28104  13.94442  4.72626  3.20292  12.8898  4.98015  3.47634  11.79612  5.44887  3.94506  10.85868  5.83947  4.4919  10.07748  5.97618  4.60908  9.78453'
    pre_db = '3.7107  8.74944  17.65512  3.7107  8.55414  16.7958  3.74976  8.53461  15.66306  3.94506  8.31978  14.41314  4.23801  7.77294  13.12416  4.51143  7.44093  12.03048  5.01921  6.87456  10.89774  5.35122  6.4449  9.72594'
    pre_p = '10.87821  3.53493  18.12384  10.83915  3.906  17.03016  10.66338  4.2966  15.66306  10.33137  4.64814  14.0616  9.70641  4.92156  12.1086  9.04239  5.03874  10.07748'
    bl_vector = '3.69117 4.27707 10.52667 8.63226 2.67561 10.52667'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':7.2, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':6.4, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':7.2, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':7.6, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX28', 'position': CONST.UR, 'note': '13-4-28-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '2.55843  2.71467  17.83089  2.40219  2.67561  17.34264  2.30454  2.57796  16.56144  2.30454  2.51937  15.58494  2.30454  2.63655  14.60844  2.38266  2.87091  13.31946  2.51937  3.20292  11.67894  2.85138  3.55446  10.3509  3.5154  3.98412  9.14004  4.14036  4.39425  8.0073'
    pre_mb2 = '3.78882  2.48031  16.69815  3.63258  2.49984  16.0146  3.61305  2.5389  15.66306  3.76929  2.57796  15.2334  4.06224  2.61702  14.49126  4.23801  2.69514  13.671  4.39425  2.89044  12.34296  4.90203  2.98809  11.3274  5.35122  3.16386  10.27278  5.76135  3.45681  9.3744  5.87853  3.92553  8.71038  5.83947  4.17942  8.30025  5.83947  4.41378  7.94871'
    pre_db = '2.63655  7.69482  16.54191  2.79279  7.67529  16.09272  3.06621  7.63623  15.50682  3.33963  7.6167  14.8428  3.57399  7.57764  14.17878  3.84741  7.49952  13.12416  4.15989  7.32375  11.9133  4.37472  7.0308  10.89774  4.76532  6.4449  9.5697  5.13639  5.70276  8.24166'
    pre_p = '13.39758  5.54652  18.12384  13.41711  5.31216  17.577  13.16322  5.23404  16.9911  12.87027  5.23404  16.36614  12.38202  5.25357  15.27246  11.63988  5.15592  13.51476  11.01492  5.17545  12.03048  10.07748  5.11686  10.19466  9.41346  5.0778  8.74944  9.00333  5.09733  7.812'
    bl_vector = '4.58955 5.33169 9.12051 9.33534 5.09733 9.12051'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.4, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':7.0, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':6.8, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':9.8, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX29', 'position': CONST.UR, 'note': '13-4-28-check all', 'weine_classification': 2, 'canals':[] }
    pre_mb = '4.78485  5.76135  17.24499  4.60908  5.37075  16.67862  4.04271  4.6872  15.70212  3.78882  4.23801  14.33502  3.55446  4.1013  13.20228  3.24198  4.17942  12.06954  3.14433  4.31613  10.97586  3.39822  4.4919  9.60876  3.80835  4.82391  8.08542  4.00365  5.11686  7.34328'
    pre_mb2 = '4.76532  5.74182  17.22546  4.80438  5.44887  16.75674  4.96062  5.01921  16.32708  4.92156  4.37472  15.58494  4.80438  3.92553  14.6475  4.94109  3.59352  13.71006  5.2731  3.28104  12.81168  5.56605  3.06621  11.83518  5.58558  3.08574  10.85868  5.60511  3.26151  9.88218  5.95665  3.78882  8.67132  6.07383  4.23801  7.92918  6.32772  4.57002  7.36281  6.48396  4.66767  7.14798'
    pre_db = '6.11289  9.51111  17.22546  6.07383  9.43299  16.91298  6.03477  9.29628  16.44426  5.99571  9.15957  15.85836  5.93712  9.04239  14.92092  6.01524  8.94474  13.39758  6.03477  8.76897  12.22578  6.01524  8.30025  10.7415  6.13242  7.69482  9.60876  6.01524  7.06986  8.28072  5.81994  6.79644  7.65576'
    pre_p = '15.35058  5.39028  18.5535  14.97951  4.99968  17.69418  14.70609  4.76532  16.7958  14.2569  4.62861  15.35058  13.51476  4.55049  13.39758  12.57732  4.78485  11.67894  11.65941  4.90203  10.19466  10.85868  5.0778  9.02286  9.39393  5.19498  7.30422'
    bl_vector = '5.21451 7.34328 9.45252 11.50317 4.88250 9.45252'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.2, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':9.6, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':8.8, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':12.6, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX30', 'position': CONST.UR, 'note': '13-4-28-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '4.25754  5.6637  17.61606  4.04271  5.48793  17.06922  3.98412  4.99968  16.2099  3.78882  4.6872  15.27246  3.73023  4.4919  14.10066  3.53493  4.4919  12.65544  3.55446  4.53096  11.60082  3.69117  4.78485  10.5462  3.84741  5.09733  9.25722'
    pre_mb2 = '4.99968  5.23404  17.44029  4.78485  5.03874  16.83486  4.55049  4.58955  15.74118  4.76532  4.21848  14.60844  5.01921  3.96459  13.63194  5.05827  3.84741  12.42108  5.05827  3.92553  11.17116  5.42934  4.17942  9.9603  5.62464  4.35519  9.47205  5.81994  4.45284  9.06192'
    pre_db = '4.64814  9.04239  17.3817  4.6872  8.86662  17.06922  4.6872  8.76897  16.67862  4.82391  8.72991  15.89742  5.03874  8.63226  14.8428  5.21451  8.47602  13.671  5.40981  8.10495  12.22578  5.60511  7.6167  10.97586  5.70276  7.2261  10.03842  5.76135  7.0308  9.21816'
    pre_p = '12.61638  5.4684  18.57303  12.51873  5.39028  17.73324  12.12813  5.19498  16.48332  11.85471  5.29263  15.15528  11.30787  5.44887  13.35852  10.52667  5.6637  11.63988  9.55017  5.81994  9.92124  8.86662  5.72229  8.90568'
    bl_vector = '4.98015 6.71832 10.19466 9.72594 6.05430 10.19466'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':7.2, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':7.0, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':7, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':9.4, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX31', 'position': CONST.UR, 'note': '', 'weine_classification': 1, 'canals':[] }
    pre_mb = '5.37075  5.40981  17.81136  5.19498  5.23404  17.42076  4.99968  4.98015  16.7958  4.72626  4.86297  15.66306  4.45284  4.86297  14.37408  4.43331  4.92156  12.65544  4.74579  5.09733  11.21022  5.29263  5.39028  9.92124'
    pre_db = '8.90568  8.10495  17.7723  8.88615  8.04636  17.26452  8.82756  7.90965  16.56144  8.71038  7.71435  15.74118  8.41743  7.46046  14.68656  7.96824  7.18704  13.35852  7.63623  6.79644  12.06954  7.28469  6.26913  10.9368  7.05033  5.81994  9.88218'
    pre_p = '12.14766  1.11321  18.39726  11.79612  1.13274  17.73324  11.58129  1.23039  16.95204  11.30787  1.46475  15.8193  10.89774  1.73817  14.56938  10.46808  2.1483  13.2804  9.82359  2.75373  11.79612  9.23769  3.33963  10.62432  8.45649  4.04271  9.5697'
    bl_vector = '6.67926 6.24960 10.85868 9.37440 3.14433 10.85868'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':7.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':7.2, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':9.6, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX32', 'position': CONST.UR, 'note': '13-4-28-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '3.04668  6.91362  17.55747  2.90997  6.89409  17.20593  2.65608  7.05033  16.69815  2.46078  7.24563  16.09272  2.30454  7.4214  15.64353  2.20689  7.53858  14.99904  2.30454  7.63623  13.63194  2.59749  7.6167  12.42108  2.94903  7.75341  11.3274  3.22245  7.77294  10.5462  3.69117  7.75341  9.5697  3.7107  7.87059  8.63226'
    pre_mb2 = '3.80835  5.78088  16.75674  3.61305  5.81994  16.44426  3.49587  5.95665  16.03413  3.55446  5.93712  15.56541  3.7107  5.76135  14.80374  3.74976  5.72229  14.02254  3.86694  5.54652  13.16322  3.94506  5.56605  12.14766  4.25754  5.60511  11.1321  4.57002  5.83947  10.31184  4.72626  6.56208  9.25722  5.11686  6.77691  8.47602'
    pre_db = '6.99174  11.17116  18.1629  6.85503  10.95633  17.577  6.77691  10.78056  16.63956  6.73785  10.64385  15.4287  6.79644  10.5462  14.29596  6.87456  10.13607  12.92886  6.79644  9.39393  11.44458  6.52302  8.65179  9.99936  6.23007  8.26119  8.90568'
    pre_p = '11.87424  1.32804  18.06525  11.60082  1.73817  16.9911  11.07351  2.24595  15.8193  10.3509  2.81232  14.02254  9.66735  3.57399  11.99142  9.14004  4.23801  10.3509  8.43696  4.82391  8.86662'
    bl_vector = '6.30819 8.72991 10.85868 9.53064 4.39425 10.85868'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':6.4, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':8.2, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':9.6, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX33', 'position': CONST.UL, 'note': '13-4-28-check all', 'weine_classification': 2, 'canals':[] }
    pre_mb = '5.72229  9.27675  17.79183  5.859  9.39393  17.59653  6.01524  9.55017  17.08875  6.11289  9.66735  16.05366  6.19101  9.82359  15.11622  6.15195  9.97983  13.78818  6.03477  10.11654  12.46014  5.72229  10.13607  11.01492  5.58558  9.97983  10.11654  5.6637  9.60876  9.14004  5.56605  9.3744  8.57367  5.35122  9.14004  7.6167'
    pre_mb2 = '5.72229  9.27675  17.7723  5.87853  9.39393  17.53794  6.03477  9.45252  17.32311  6.13242  9.53064  16.77627  6.23007  9.64782  15.8193  6.28866  9.80406  14.41314  6.4449  9.74547  13.55382  6.50349  9.68688  12.61638  6.60114  9.5697  11.79612  6.91362  9.14004  10.66338  6.99174  8.86662  9.94077  6.99174  8.49555  9.27675  6.85503  7.98777  8.65179  6.77691  7.85106  8.22213  6.69879  7.75341  7.92918  6.6402  7.51905  7.59717'
    pre_db = '1.69911  6.8355  17.88948  1.99206  7.05033  17.26452  2.30454  6.87456  16.0146  2.51937  6.60114  14.6475  2.79279  6.36678  13.0851  3.22245  6.40584  11.75706  3.74976  6.48396  10.50714  4.43331  6.75738  9.33534  4.78485  6.99174  8.0073'
    pre_p = '10.60479  0.68355  18.43632  10.3509  0.99603  17.577  10.19466  1.32804  16.75674  9.9603  1.91394  15.4287  9.55017  2.55843  13.55382  8.96427  3.26151  11.40552  8.28072  3.98412  9.64782  7.44093  4.94109  7.77294'
    bl_vector = '4.47237 6.95268 8.90568 8.20260 4.00365 8.90568'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.4, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':8.4, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':9.2, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':11.2, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX34', 'position': CONST.UR, 'note': '', 'weine_classification': 1, 'canals':[] }
    pre_mb = '4.33566  6.8355  17.90901  4.17942  6.93315  17.26452  4.04271  6.91362  16.6005  3.906  6.77691  15.4287  4.00365  6.67926  14.41314  4.2966  6.8355  12.57732  4.62861  7.0308  11.44458  5.19498  7.28469  9.9603'
    pre_db = '7.40187  10.07748  18.65115  7.2261  9.94077  18.1629  7.12845  9.84312  17.42076  7.14798  9.66735  16.2099  7.30422  9.45252  15.0381  7.34328  9.23769  13.94442  7.18704  8.80803  12.61638  6.95268  8.28072  11.56176  6.69879  7.94871  10.78056  6.38631  7.53858  9.99936'
    pre_p = '11.79612  2.03112  18.72927  11.50317  2.1483  18.08478  11.30787  2.28501  17.1864  11.05398  2.46078  16.09272  10.70244  2.71467  14.92092  10.31184  3.10527  13.59288  9.66735  3.73023  11.95236  9.02286  4.27707  10.85868  8.55414  4.80438  9.80406'
    bl_vector = '5.83947 7.89012 11.40552 9.39393 4.21848 11.40552'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':6.4, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':7.6, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':9.4, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX35', 'position': CONST.UL, 'note': '13-4-28-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '4.57002  9.9603  16.63956  4.76532  9.99936  16.42473  5.25357  10.25325  15.99507  5.78088  10.52667  15.15528  5.91759  10.56573  14.17878  5.93712  10.50714  13.00698  5.68323  10.52667  11.9133  5.60511  10.31184  11.05398  5.50746  9.9603  10.1556  5.25357  9.68688  9.1791  5.15592  9.53064  8.69085'
    pre_mb2 = '7.16751  9.04239  15.78024  7.30422  9.19863  15.44823  7.34328  9.43299  14.99904  7.28469  9.53064  14.4522  7.2261  9.55017  13.78818  7.26516  9.49158  13.16322  7.4214  9.1791  12.34296  7.49952  8.94474  11.56176  7.47999  8.84709  11.17116  7.0308  8.55414  10.19466  6.54255  8.22213  9.49158  6.21054  7.90965  8.7885'
    pre_db = '2.90997  6.21054  18.04572  2.9295  6.4449  17.34264  3.16386  6.58161  16.17084  3.28104  6.73785  15.07716  3.65211  6.89409  13.59288  4.00365  6.93315  12.26484  4.55049  6.99174  11.01492  4.92156  7.18704  10.27278  5.17545  7.26516  9.45252'
    pre_p = '10.78056  1.23039  18.1629  10.5462  1.50381  17.1864  10.13607  1.99206  16.17084  9.66735  2.49984  14.92092  9.1791  2.9295  13.20228  8.5932  3.65211  11.48364  7.67529  4.37472  10.07748  6.95268  5.29263  8.74944'
    bl_vector = '4.47237 8.71038 10.27278 7.75341 5.01921 10.27278'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':6.7, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':5.8, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':8.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':10.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX36', 'position': CONST.UL, 'note': '13-4-28-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '6.28866  9.60876  17.08875  6.28866  9.92124  16.67862  6.26913  10.19466  16.17084  6.15195  10.50714  15.66306  5.97618  10.78056  14.92092  5.99571  10.9368  13.98348  6.07383  10.91727  12.92886  6.2496  10.62432  11.60082  6.26913  10.17513  10.27278  6.15195  9.45252  8.86662  5.87853  8.88615  7.6167'
    pre_mb2 = '7.75341  8.51508  16.67862  7.812  8.63226  16.24896  7.92918  8.88615  15.46776  8.04636  8.90568  14.95998  8.14401  8.92521  14.51079  8.08542  9.06192  13.80771  8.08542  9.15957  12.92886  7.812  9.3744  12.08907  7.6167  9.39393  11.09304  7.53858  9.33534  10.46808  7.24563  9.23769  9.66735  6.93315  9.12051  9.08145  6.85503  8.94474  8.65179  6.77691  8.55414  8.10495'
    pre_db = '2.32407  6.81597  17.20593  2.36313  6.99174  16.71768  2.42172  6.95268  15.58494  2.5389  6.77691  14.17878  2.77326  6.56208  12.77262  3.35916  6.56208  11.28834  4.08177  6.6402  9.9603  4.96062  7.01127  8.3979  5.31216  7.2261  7.69482'
    pre_p = '12.16719  1.5624  17.73324  11.9133  1.60146  17.34264  11.60082  1.7577  16.48332  11.15163  1.7577  15.27246  10.80009  2.12877  13.78818  10.17513  2.44125  11.99142  9.49158  3.02715  10.46808  8.67132  3.98412  9.02286  8.37837  4.53096  7.49952'
    bl_vector = '5.17545 9.76500 9.33534 10.83915 3.47634 9.33534'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.5, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':7.6, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX37', 'position': CONST.UL, 'note': '13-4-28-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '5.56605  9.19863  16.09272  5.4684  9.33534  15.97554  5.2731  9.62829  15.68259  5.25357  9.765  15.21387  5.37075  9.99936  14.49126  5.37075  10.21419  13.82724  5.23404  10.52667  12.85074  5.05827  10.7415  11.75706  4.96062  10.7415  10.50714  5.05827  10.52667  9.3744  4.90203  10.19466  7.96824  4.72626  10.11654  7.34328'
    pre_mb2 = '6.07383  8.9838  16.05366  6.13242  9.08145  15.79977  6.23007  9.25722  15.21387  6.28866  9.47205  14.54985  6.40584  9.58923  13.94442  6.62067  9.72594  13.20228  6.81597  9.80406  12.38202  7.01127  9.92124  11.24928  7.06986  9.92124  10.03842  6.97221  9.64782  8.94474  6.91362  9.33534  8.22213  6.67926  9.12051  7.71435  6.56208  8.88615  7.28469  6.46443  8.41743  6.62067'
    pre_db = '2.42172  5.23404  18.63162  2.42172  5.33169  18.20196  2.48031  5.39028  17.61606  2.59749  5.48793  16.63956  2.69514  5.64417  15.624  2.94903  5.87853  13.98348  3.18339  6.30819  12.18672  3.7107  6.79644  10.19466  4.23801  7.55811  8.35884  4.45284  8.10495  7.38234'
    pre_p = '10.87821  1.73817  18.43632  10.99539  2.01159  17.9676  11.05398  2.18736  17.42076  11.1321  2.32407  15.74118  11.03445  2.59749  14.21784  10.68291  2.77326  13.0851  10.3509  3.14433  11.75706  9.86265  3.78882  10.3509  9.06192  4.78485  8.71038  7.96824  6.0543  6.56208'
    bl_vector = '3.63258  9.76500  8.18307 10.78056  5.58558  8.18307'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':7.7, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':7.3, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX38', 'position': CONST.UL, 'note': '', 'weine_classification': 3, 'canals':[] }
    pre_mb = '2.85138  7.67529  17.55747  3.02715  7.87059  17.1864  3.06621  8.22213  16.83486  3.20292  8.69085  16.28802  3.39822  9.02286  15.66306  3.61305  9.15957  14.8428  3.82788  9.1791  13.90536  3.80835  9.15957  12.96792  3.80835  9.04239  12.1086  4.1013  8.41743  10.78056  4.45284  7.96824  9.88218  4.55049  7.73388  9.1791'
    pre_mb2 = '4.78485  7.69482  16.65909  4.98015  7.85106  16.38567  5.23404  8.30025  15.89742  5.37075  8.57367  15.4287  5.37075  8.72991  14.95998  5.56605  8.82756  14.10066  5.78088  8.84709  13.43664  6.09336  8.80803  12.73356  6.19101  8.76897  12.38202  5.80041  7.77294  10.11654  5.68323  7.40187  9.5697'
    pre_db = '2.42172  3.55446  18.28008  2.5389  3.86694  17.85042  2.69514  4.25754  17.10828  2.85138  4.51143  16.05366  3.14433  4.60908  14.60844  3.45681  4.72626  13.12416  4.04271  4.98015  11.79612  4.51143  5.4684  10.38996  4.8825  5.68323  9.60876'
    pre_p = '10.58526  1.71864  18.5535  10.50714  1.91394  18.00666  10.31184  2.22642  17.03016  10.13607  2.44125  15.89742  9.86265  2.75373  14.6475  9.64782  3.10527  13.51476  9.06192  3.5154  12.03048  8.33931  3.88647  10.7415  7.67529  4.47237  9.1791'
    bl_vector = '3.04668  8.18307  11.09304 9.90171  5.40981  11.09304'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.1, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':6.5, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX39', 'position': CONST.UL, 'note': '', 'weine_classification': 2, 'canals':[] }
    pre_mb = '3.7107  6.4449  17.10828  3.98412  5.95665  16.44426  3.96459  5.23404  15.624  3.94506  4.6872  14.72562  3.86694  4.35519  13.00698  3.61305  4.60908  11.01492  3.63258  4.78485  9.5697  3.84741  4.8825  8.55414  3.906  5.0778  7.57764'
    pre_mb2 = '3.7107  6.42537  17.08875  3.88647  5.859  16.28802  4.00365  5.03874  15.46776  3.96459  4.41378  14.10066  3.92553  4.14036  12.06954  4.39425  3.80835  10.81962  4.64814  3.76929  9.64782  4.66767  4.31613  7.6167  4.92156  4.45284  6.8355'
    pre_db = '5.42934  7.36281  17.65512  5.29263  7.57764  17.03016  5.29263  7.53858  16.44426  5.50746  7.49952  15.54588  5.64417  7.65576  14.13972  5.93712  7.65576  12.57732  6.0543  7.51905  11.36646  6.15195  7.20657  9.88218  6.17148  6.85503  9.02286  6.17148  6.23007  7.96824  6.03477  6.32772  7.30422'
    pre_p = '12.34296  2.77326  18.90504  12.34296  2.7342  18.5535  12.38202  2.57796  17.85042  12.26484  2.49984  16.9911  12.03048  2.5389  15.85836  11.93283  2.59749  14.53032  11.69847  2.79279  13.0851  11.28834  3.10527  11.63988  10.5462  3.61305  9.84312  9.99936  4.08177  8.55414  9.39393  4.39425  7.34328  8.84709  4.45284  6.52302'
    bl_vector = '2.89044  6.17148  7.96824 9.64782  3.20292  7.96824'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX40', 'position': CONST.UL, 'note': '', 'weine_classification': 4, 'canals':[] }
    pre_mb = '4.17942  8.69085  18.28008  4.23801  8.69085  18.00666  4.35519  8.72991  17.69418  4.55049  8.76897  17.06922  4.64814  8.84709  16.44426  4.62861  8.82756  15.46776  4.66767  8.7885  14.49126  4.70673  8.80803  13.671  4.78485  8.80803  12.61638  5.09733  8.65179  11.17116  5.21451  8.43696  10.03842  5.29263  7.69482  8.2026  5.15592  7.40187  7.46046'
    pre_mb2 = '6.50349  7.73388  17.34264  6.56208  7.79247  17.03016  6.65973  7.90965  16.63956  6.81597  7.96824  16.09272  6.91362  8.0073  15.35058  7.01127  7.90965  14.4522  7.08939  7.85106  13.78818  7.16751  7.75341  13.0851  7.14798  7.75341  12.3039  7.10892  7.75341  11.36646  6.95268  7.69482  10.31184  6.21054  7.51905  8.71038  6.01524  7.30422  8.08542'
    pre_db = '2.59749  4.31613  18.31914  2.36313  4.33566  17.88948  2.32407  4.35519  17.53794  2.32407  4.39425  16.71768  2.42172  4.58955  15.74118  2.7342  4.6872  14.53032  2.96856  4.84344  13.12416  3.28104  4.96062  11.83518  3.76929  4.92156  10.62432  4.37472  5.0778  9.49158  4.84344  5.37075  8.3979  5.17545  5.60511  7.46046'
    pre_p = '9.90171  3.24198  17.81136  10.07748  3.16386  17.30358  10.17513  2.96856  16.4052  10.37043  2.83185  15.4287  10.33137  2.71467  14.17878  10.03842  2.69514  12.42108  9.60876  2.77326  10.97586  8.86662  3.06621  9.49158  8.0073  3.67164  7.96824  7.38234  4.23801  6.95268'
    bl_vector = '3.80835  8.37837  8.35884 9.70641  4.51143  8.35884'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.8, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':8.7, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX41', 'position': CONST.UL, 'note': '', 'weine_classification': 1, 'canals':[] }
    pre_mb = '4.17942  10.31184  18.24102  4.23801  10.48761  17.61606  4.21848  10.52667  16.75674  4.08177  10.58526  16.0146  3.73023  10.76103  14.6475  4.12083  10.29231  12.6945  4.19895  10.17513  11.95236  4.15989  9.80406  10.3509  4.43331  8.92521  8.3979  4.4919  8.06589  7.18704'
    pre_db = '1.21086  7.51905  16.7958  1.26945  7.49952  16.09272  1.30851  7.28469  15.0381  1.46475  6.85503  13.671  1.89441  6.56208  12.14766  2.61702  6.52302  10.46808  3.18339  6.52302  9.45252  3.82788  6.62067  8.28072  4.02318  6.69879  7.69482'
    pre_p = '10.56573  3.59352  18.59256  10.60479  3.78882  18.12384  10.46808  4.04271  17.06922  10.05795  4.06224  15.624  9.49158  4.31613  13.71006  8.69085  4.62861  11.87424  8.16354  4.86297  10.27278  7.34328  4.96062  7.65576'
    bl_vector = '3.20292  9.94077  9.64782 9.90171  5.68323  9.64782'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX42', 'position': CONST.UL, 'note': '', 'weine_classification': 1, 'canals':[] }
    pre_mb = '4.4919  7.40187  17.55747  4.4919  7.73388  16.91298  4.57002  8.22213  15.85836  4.78485  8.53461  14.68656  4.84344  8.7885  13.31946  4.92156  8.76897  12.06954  4.92156  8.2026  10.38996  4.80438  7.65576  9.06192'
    pre_db = '1.79676  5.15592  17.44029  1.79676  5.31216  16.95204  1.99206  5.33169  16.09272  2.10924  5.15592  14.88186  2.3436  5.09733  13.90536  2.81232  5.09733  12.6945  3.47634  5.31216  11.24928  4.08177  5.6637  10.03842  4.35519  5.87853  9.02286'
    pre_p = '10.05795  1.40616  18.39726  10.03842  1.64052  17.81136  10.07748  1.953  16.9911  10.05795  2.22642  16.05366  9.92124  2.49984  14.8428  9.53064  2.75373  13.16322  8.96427  3.30057  11.40552  8.22213  3.84741  9.41346  7.75341  4.33566  8.35884'
    bl_vector = '4.00365  8.43696  9.53064 10.07748  4.68720  9.53064'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX43', 'position': CONST.UR, 'note': '', 'weine_classification': 3, 'canals':[] }
    pre_mb = '5.37075  5.87853  18.33867  5.2731  5.56605  17.73324  5.05827  5.35122  16.9911  4.82391  4.98015  15.85836  4.74579  4.6872  14.56938  4.51143  4.94109  12.92886  4.62861  5.09733  12.03048  4.78485  5.29263  11.28834  5.01921  5.44887  10.5462  5.35122  5.58558  9.99936'
    pre_mb2 = '7.0308  4.25754  16.95204  6.81597  3.906  16.48332  6.48396  3.74976  15.89742  6.11289  3.74976  15.15528  5.78088  3.78882  14.13972  5.97618  3.57399  13.43664  6.07383  3.57399  12.46014  6.03477  3.78882  11.79612  6.15195  4.21848  10.7415  6.21054  4.41378  10.23372  6.4449  4.60908  9.80406'
    pre_db = '7.92918  8.84709  18.04572  7.6167  8.5932  16.91298  7.32375  8.61273  15.15528  7.16751  8.37837  13.51476  7.05033  7.6167  11.718  6.65973  6.52302  9.765'
    pre_p = '14.49126  2.48031  17.92854  14.0616  2.63655  16.44426  13.2804  3.06621  14.4522  12.55779  3.43728  13.04604  11.46411  3.86694  11.44458  10.52667  4.39425  10.3509  9.25722  4.86297  9.1791'
    bl_vector = '4.12083  6.30819  10.95633 9.72594  2.89044  10.95633'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':7.2, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':6.3, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX44', 'position': CONST.UL, 'note': '', 'weine_classification': 1, 'canals':[] }
    pre_mb = '4.4919  10.50714  17.90901  4.66767  10.60479  17.42076  5.01921  10.7415  16.44426  5.05827  10.7415  15.4287  5.13639  10.64385  13.94442  5.2731  10.3509  12.65544  5.15592  9.99936  11.44458  5.05827  9.3744  10.11654  5.03874  8.74944  9.02286  5.03874  7.89012  7.96824'
    pre_db = '3.55446  3.80835  17.61606  3.37869  4.2966  17.1864  3.57399  4.47237  16.63956  3.76929  4.57002  16.09272  3.98412  4.74579  15.2334  4.1013  4.98015  14.13972  4.2966  5.15592  12.77262  4.4919  5.44887  11.44458  4.78485  5.91759  9.92124  5.13639  6.4449  8.08542'
    pre_p = '12.81168  4.53096  18.1629  12.59685  4.80438  17.69418  12.32343  4.96062  16.83486  11.95236  4.99968  15.8193  11.30787  5.13639  14.33502  10.42902  5.21451  12.34296  9.41346  5.39028  10.27278  7.94871  5.78088  8.0073'
    bl_vector = '3.24198  8.96427  8.35884 9.72594  6.44490  8.35884'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX45', 'position': CONST.UL, 'note': '', 'weine_classification': 3, 'canals':[] }
    pre_mb = '3.92553  5.2731  17.03016  4.06224  5.56605  16.48332  4.04271  5.74182  15.93648  4.12083  5.89806  15.0381  4.25754  6.07383  13.8663  4.1013  6.28866  12.92886  3.98412  6.38631  12.06954  4.14036  6.50349  10.81962  4.37472  6.40584  9.53064  4.58955  6.0543  8.24166  4.60908  5.78088  7.4214  4.4919  5.62464  6.87456'
    pre_mb2 = '5.56605  5.60511  17.30358  5.4684  5.70276  16.83486  5.50746  5.87853  16.32708  5.60511  5.93712  15.8193  5.68323  5.93712  15.15528  5.40981  6.03477  14.29596  5.21451  6.15195  13.63194  5.35122  6.30819  12.6945  5.60511  6.34725  11.95236  5.78088  6.40584  11.05398  5.91759  6.40584  9.92124  6.2496  6.03477  8.5932  6.4449  5.56605  7.812  6.48396  5.19498  6.99174  6.56208  5.13639  6.40584'
    pre_db = '4.19895  3.39822  17.40123  4.14036  3.63258  16.95204  4.19895  3.73023  16.52238  4.37472  3.80835  15.97554  4.57002  3.67164  15.38964  4.80438  3.5154  14.60844  4.99968  3.39822  13.671  5.03874  3.39822  12.65544  5.05827  3.26151  11.40552  5.17545  3.22245  10.19466  5.35122  3.45681  8.90568  5.4684  3.65211  8.28072  5.48793  3.86694  7.49952'
    pre_p = '10.1556  3.28104  18.63162  10.23372  3.24198  18.1629  10.40949  3.22245  17.65512  10.58526  3.20292  16.87392  10.56573  3.24198  15.85836  10.50714  3.47634  14.68656  10.40949  3.55446  13.43664  10.29231  3.65211  12.1086  9.94077  3.49587  9.9603  9.23769  3.43728  7.89012  8.69085  3.5154  6.56208'
    bl_vector = '3.08574  5.81994  7.63623 9.10098  4.74579  7.63623'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':6.5, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':6.5, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX46', 'position': CONST.UR, 'note': '', 'weine_classification': 3, 'canals':[] }
    pre_mb = '1.32804  4.60908  16.52238  1.40616  4.62861  16.17084  1.52334  4.62861  15.70212  1.64052  4.58955  15.07716  1.7577  4.58955  14.2569  2.03112  4.4919  13.16322  2.20689  4.62861  12.18672  2.36313  4.8825  11.3274  2.98809  4.99968  10.07748  3.73023  5.09733  8.94474  3.98412  5.17545  8.47602'
    pre_mb2 = '3.06621  3.18339  16.63956  3.02715  3.26151  16.42473  2.98809  3.35916  16.09272  2.94903  3.39822  15.8193  2.87091  3.49587  15.46776  2.87091  3.5154  15.19434  2.89044  3.5154  14.76468  2.94903  3.43728  14.02254  2.98809  3.43728  13.2804  3.08574  3.47634  12.53826  3.37869  3.35916  11.87424  3.76929  3.41775  11.01492  4.08177  3.76929  10.07748  4.43331  4.06224  9.1791  4.78485  4.15989  8.71038'
    pre_db = '5.50746  9.86265  16.75674  5.52699  9.74547  16.2099  5.54652  9.55017  15.50682  5.74182  9.23769  14.76468  5.93712  8.90568  13.82724  6.0543  8.3979  12.4992  6.15195  7.79247  11.21022  6.13242  6.6402  9.60876  6.07383  6.11289  8.63226'
    pre_p = '11.38599  2.48031  17.73324  11.22975  2.3436  17.1864  10.99539  2.30454  16.2099  10.81962  2.36313  15.19434  10.7415  2.5389  14.21784  10.33137  3.02715  12.6945  9.74547  3.61305  11.17116  9.02286  4.08177  9.80406  8.41743  4.23801  8.74944'
    bl_vector = '3.10527  6.01524  9.97983 7.65576  2.40219  9.97983'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':7.5, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':6.4, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX47', 'position': CONST.UL, 'note': '', 'weine_classification': 2, 'canals':[] }
    pre_mb = '4.62861  9.29628  16.15131  4.72626  9.53064  15.50682  4.80438  9.80406  14.21784  4.57002  9.84312  12.81168  4.60908  9.5697  11.75706  4.70673  9.23769  10.85868  4.60908  9.02286  9.765  4.66767  8.57367  8.67132  4.64814  8.31978  8.0073'
    pre_mb2 = '4.62861  9.31581  16.13178  4.74579  9.58923  15.35058  5.01921  9.66735  14.0616  4.98015  9.60876  12.96792  5.05827  9.35487  11.99142  5.50746  8.67132  10.3509  5.52699  8.0073  9.02286  5.2731  7.28469  8.12448'
    pre_db = '1.13274  5.859  16.11225  1.15227  5.95665  15.624  1.23039  5.97618  14.88186  1.62099  5.81994  14.02254  2.03112  5.76135  13.00698  2.61702  5.72229  11.79612  3.10527  5.68323  10.85868  3.76929  5.87853  9.45252  4.4919  6.2496  8.08542'
    pre_p = '10.3509  3.24198  18.43632  10.25325  3.35916  17.65512  10.17513  3.37869  16.36614  9.94077  3.3201  15.0381  9.49158  3.30057  13.90536  8.86662  3.33963  12.46014  8.26119  3.5154  11.1321  7.89012  3.82788  9.84312  7.57764  4.23801  8.63226  7.4214  4.39425  7.92918'
    bl_vector = '3.76929  8.22213  9.06192 8.02683  4.62861  9.06192'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX48', 'position': CONST.UL, 'note': '', 'weine_classification': 3, 'canals':[] }
    pre_mb = '2.98809  9.88218  16.83486  3.24198  10.03842  16.4052  3.61305  10.09701  15.624  3.82788  10.13607  14.92092  4.17942  10.11654  14.0616  4.41378  9.97983  13.16322  4.14036  9.86265  11.9133  4.04271  9.62829  10.9368  4.41378  9.06192  9.80406  4.58955  8.43696  8.63226  4.4919  8.24166  7.57764'
    pre_mb2 = '4.94109  9.3744  16.07319  5.05827  9.49158  15.8193  5.15592  9.58923  15.50682  5.33169  9.68688  14.49126  5.2731  9.72594  13.78818  5.15592  9.68688  13.00698  5.37075  9.43299  12.1086  5.68323  9.10098  11.05398  5.91759  8.67132  10.07748  5.859  8.2026  9.10098  5.95665  7.71435  8.51508  5.87853  7.59717  8.2026  5.6637  7.46046  7.812  5.31216  7.36281  7.53858'
    pre_db = '1.15227  5.54652  16.7958  1.28898  5.48793  16.28802  1.40616  5.4684  15.50682  1.62099  5.44887  14.68656  1.87488  5.35122  13.8663  2.10924  5.25357  12.96792  2.57796  5.44887  11.75706  3.26151  5.54652  10.58526  4.17942  5.60511  9.41346  4.57002  5.76135  8.5932  4.76532  5.87853  7.96824'
    pre_p = '10.23372  2.36313  18.90504  10.37043  2.48031  18.51444  10.52667  2.55843  18.12384  10.68291  2.59749  17.73324  10.62432  2.7342  17.22546  10.42902  2.77326  16.13178  10.09701  2.83185  14.8428  9.74547  2.98809  13.31946  9.15957  3.39822  11.63988  8.82756  3.61305  10.23372  8.12448  4.04271  8.28072'
    bl_vector = '4.53096  7.89012  8.28072 8.76897  4.66767  8.28072'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX49', 'position': CONST.UR, 'note': '', 'weine_classification': 4, 'canals':[] }
    pre_mb = '3.74976  4.15989  18.24102  3.73023  4.12083  17.83089  3.82788  4.04271  17.1864  3.78882  4.02318  16.6005  3.74976  4.17942  15.66306  3.78882  4.41378  14.2569  3.96459  4.4919  12.8898  4.31613  4.78485  11.87424  4.72626  5.05827  10.58526'
    pre_mb2 = '4.98015  3.41775  16.65909  4.78485  3.39822  16.32708  4.92156  3.28104  15.85836  4.96062  3.20292  15.31152  4.92156  3.28104  14.56938  4.76532  3.45681  13.55382  4.6872  3.86694  12.42108  4.92156  4.25754  11.3274  5.35122  4.57002  10.46808'
    pre_db = '6.2496  8.04636  17.7723  6.23007  7.85106  17.10828  6.46443  7.73388  16.56144  6.52302  7.67529  15.66306  6.48396  7.49952  14.72562  6.4449  7.18704  13.39758  6.32772  6.71832  12.18672  6.23007  6.2496  11.1321  6.03477  5.87853  10.46808'
    pre_p = '14.02254  1.69911  17.42076  13.37805  1.81629  16.77627  12.67497  2.07018  15.97554  12.20625  2.24595  15.15528  11.63988  2.55843  14.13972  10.97586  2.94903  12.77262  10.33137  3.35916  11.5227  9.72594  3.82788  10.58526  9.19863  4.08177  9.765'
    bl_vector = '4.53096  5.97618  10.56573 9.29628  3.78882  10.56573'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX50', 'position': CONST.UR, 'note': '2 DB canals', 'weine_classification': 3, 'canals':[] }
    pre_mb = '4.27707  4.80438  17.69418  4.17942  4.76532  17.30358  4.1013  4.6872  16.6005  4.02318  4.57002  15.8193  3.88647  4.55049  14.95998  3.7107  4.64814  13.59288  3.59352  4.8825  12.81168  3.76929  5.19498  11.56176  4.14036  5.50746  10.42902  4.25754  5.68323  9.10098'
    pre_mb2 = '5.93712  3.39822  15.70212  5.83947  3.43728  15.4287  5.64417  3.47634  15.0381  5.42934  3.45681  14.56938  5.23404  3.5154  13.98348  5.35122  3.47634  13.35852  5.4684  3.39822  12.81168  5.64417  3.3201  12.1086  5.76135  3.43728  11.36646  6.03477  3.76929  10.46808  6.19101  4.27707  9.92124  6.46443  4.99968  9.02286'
    pre_db = '6.19101  7.65576  17.32311  6.19101  7.57764  16.7958  6.30819  7.63623  16.28802  6.40584  7.73388  15.66306  6.40584  7.77294  14.76468  6.48396  7.77294  13.78818  6.4449  7.79247  12.73356  6.50349  7.63623  11.95236  6.42537  7.26516  10.97586  6.17148  6.93315  10.11654'
    pre_p = '12.08907  2.87091  16.91298  11.85471  3.10527  16.05366  11.50317  3.22245  14.60844  11.07351  3.3201  13.16322  10.64385  3.61305  11.95236  10.1556  3.96459  10.89774  9.62829  4.47237  9.5697'
    bl_vector = '3.88647  6.69879  10.17513 10.37043  3.59352  10.17513'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':5.8, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX51', 'position': CONST.UR, 'note': '', 'weine_classification': 3, 'canals':[] }
    pre_mb = '4.06224  4.90203  16.95204  3.98412  4.76532  16.81533  3.86694  4.66767  16.62003  3.78882  4.51143  16.09272  3.78882  4.2966  15.56541  3.69117  4.12083  14.70609  3.69117  4.00365  13.63194  3.7107  4.00365  12.42108  3.69117  4.12083  11.40552  3.80835  4.37472  10.42902  3.96459  4.64814  9.72594  4.12083  4.96062  8.7885'
    pre_mb2 = '5.03874  4.02318  15.97554  4.78485  3.78882  15.46776  4.58955  3.7107  14.92092  4.35519  3.69117  14.17878  4.08177  3.78882  13.31946  4.19895  3.7107  12.22578  4.41378  3.7107  11.28834  4.80438  3.906  10.07748  4.86297  4.25754  9.25722  4.8825  4.6872  8.47602'
    pre_db = '4.51143  8.57367  17.26452  4.55049  8.53461  16.87392  4.66767  8.3979  16.28802  4.82391  8.31978  15.46776  4.99968  8.18307  14.60844  5.0778  7.92918  13.35852  5.19498  7.6167  12.14766  5.19498  7.24563  11.09304  5.17545  6.91362  10.3509  4.94109  6.38631  9.41346  4.90203  6.11289  8.51508'
    pre_p = '10.97586  2.16783  17.65512  10.85868  2.26548  16.9911  10.83915  2.38266  16.24896  10.56573  2.71467  14.80374  10.40949  3.00762  13.43664  9.92124  3.43728  11.67894  9.29628  3.74976  10.27278  8.55414  4.00365  8.9838  8.12448  4.17942  7.96824'
    bl_vector = '3.39822  5.62464  9.53064 9.41346  3.30057  9.53064'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)


    specimen_info = {'name':'MX52', 'position': CONST.UL, 'note': '', 'weine_classification': 2, 'canals':[] }
    pre_mb = '5.19498  4.70673  18.26055  5.19498  4.51143  17.69418  5.42934  4.21848  16.83486  5.72229  3.76929  15.58494  5.859  3.43728  14.2569  5.99571  3.22245  12.81168  6.30819  3.08574  10.9368  6.60114  3.20292  9.14004  6.81597  3.73023  6.99174'
    pre_mb2 = '5.15592  4.6872  18.24102  5.23404  4.47237  17.61606  5.31216  4.25754  16.95204  4.99968  4.41378  16.0146  4.62861  4.62861  14.99904  4.27707  4.8825  13.51476  4.1013  5.21451  11.718  4.17942  5.56605  10.11654  4.60908  5.81994  8.43696  4.62861  5.97618  7.69482  4.58955  6.13242  6.79644'
    pre_db = '10.9368  7.38234  17.9676  11.03445  7.20657  17.42076  11.11257  7.01127  16.91298  10.97586  6.89409  16.09272  10.83915  6.91362  15.11622  10.56573  6.95268  13.55382  10.05795  6.97221  11.79612  9.5697  6.87456  9.9603  8.96427  6.89409  8.55414  8.67132  6.91362  7.57764'
    pre_p = '5.11686  11.81565  16.24896  5.0778  11.58129  15.70212  4.92156  11.56176  15.4287  4.76532  11.62035  15.17481  4.6872  11.60082  14.78421  4.76532  11.67894  14.29596  4.76532  11.62035  13.4757  4.92156  11.36646  12.38202  5.2731  10.83915  11.1321  5.58558  10.19466  10.03842  5.91759  9.66735  9.10098  6.48396  8.88615  7.6167'
    bl_vector = '9.15957  3.18339  10.37043 3.55446  9.55017  10.37043'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_mb2})
    specimen_info['canals'].append({'name':'pre-mb2', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_mb2, 'pts_opposite': pre_mb})
    specimen_info['canals'].append({'name':'pre-db', 'furcation_pos':0.0, 'is_buccal_side':True, 'pts_canal': pre_db, 'pts_vector': bl_vector})
    specimen_info['canals'].append({'name':'pre-p', 'furcation_pos':0.0, 'is_buccal_side':False, 'pts_canal': pre_p, 'pts_vector': bl_vector})
    infos.append(specimen_info)

    return infos


def _get_specimen_infos():
    infos=[]

    specimen_info = {'name': 'MX01', 'position': CONST.UL, 'note': '13-4-14-check all', 'weine_classification': 3, 'canals':[]}
    mbc = '2.07018 8.26119 18.16290  2.24595 8.30025 17.77230  2.42172 8.47602 17.30358  2.53890 8.61273 16.71768  2.49984 8.74944 15.58494  2.55843 8.84709 14.53032  2.65608 8.84709 13.59288  2.77326 8.76897 12.14766  2.94903 8.26119 9.80406  3.33963 7.89012 8.74944  3.57399 7.51905 8.00730  3.82788 7.24563 7.22610'
    mb2c = '5.33169 8.78850 16.60050  5.27310 8.86662 16.01460  5.07780 9.04239 15.23340  5.01921 9.12051 14.60844  4.99968 9.17910 13.78818  5.07780 9.14004 12.69450  5.40981 9.10098 11.09304  5.87853 9.04239 10.15560  6.21054 8.76897 9.29628  6.32772 8.28072 8.63226  6.21054 7.61670 7.92918  5.76135 7.26516 7.06986'
    pc = '13.12416 4.53096 18.61209 13.14369 4.70673 18.04572 13.00698 4.72626 17.26452 12.67497 4.62861 15.85836 12.30390 4.78485 13.94442 11.79612 4.98015 12.26484 10.87821 5.09733 10.35090 9.68688 5.17545 8.59320 8.76897 5.03874 7.30422'
    dbc = '4.14036 3.73023 18.31914 4.04271 3.80835 17.69418 3.86694 3.82788 17.10828 3.88647 3.82788 16.05366 3.90600 3.69117 14.72562 3.98412 3.61305 13.31946 4.21848 3.74976 11.87424 4.66767 4.08177 10.58526 4.99968 4.55049 9.37440 5.01921 5.15592 7.96824'
    blv = ' 3.59352 5.21451 10.11654 10.66338 5.21451 10.11654'

    # specimen_info['canals'] = [{'name':'mb', 'furcation_pos': 9.0, 'is_buccal_side': True, 'pts_canal': mbc, 'pts_opposite': mb2c},
    #                            {'name':'mb2', 'furcation_pos': 7.9, 'is_buccal_side': False, 'pts_canal': mb2c, 'pts_opposite': mbc},
    #                            {'name':'db', 'furcation_pos': 8.8, 'is_buccal_side': True, 'pts_canal': dbc, 'pts_vector': blv},
    #                            {'name':'p', 'furcation_pos': 10.4, 'is_buccal_side': False, 'pts_canal': pc, 'pts_vector': blv}]

    specimen_info['canals'].append({'name':'mb', 'furcation_pos': 9.0, 'is_buccal_side': True, 'pts_canal': mbc, 'pts_opposite': mb2c})
    specimen_info['canals'].append({'name':'mb2', 'furcation_pos': 7.9, 'is_buccal_side': False, 'pts_canal': mb2c, 'pts_opposite': mbc})
    specimen_info['canals'].append({'name':'db', 'furcation_pos': 8.8, 'is_buccal_side': True, 'pts_canal': dbc, 'pts_vector': blv})
    specimen_info['canals'].append({'name':'p', 'furcation_pos': 10.4, 'is_buccal_side': False, 'pts_canal': pc, 'pts_vector': blv})
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

