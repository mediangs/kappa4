# -*- coding: cp949 -*-
'''
Created on 2014. 4. 9.

@author: jongki
'''

import os
from constant import CONST
from class_specimen import Specimen
from specimen_info_builder import fill_uninstrumented_specimen


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


# ondemand 에서 realign을 하고 나면 이미지가 flip되서 저장--> 좌우가 바뀜
# ===============================================================================
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
# ===============================================================================
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
# ===============================================================================



def get_meta_info():
    meta_info = {}
    meta_info['magnification_ratio'] = 1
    meta_info['directory_name'] = os.getenv('TOOTH_DATA') + '/v3d_mn/'
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

    specimen_info = {'name':'MN01', 'position': CONST.LL, 'note': '13-3-19-check all', 'weine_classification': 2, 'canals':[] }
    pre_mb = '4.96548  3.38989  1.05039  4.8859  3.31032  1.41643  4.98139  3.15117  1.98937  5.29969  3.02385  2.9761  5.64982  2.9761  3.5013  5.90446  2.88061  4.2493  6.14319  2.81695  4.99731  6.38191  2.75329  6.06361  6.50923  2.83287  7.09809  6.46149  3.05568  8.13256  6.52515  3.37398  8.99198  6.63655  3.5013  9.37393'
    pre_ml = '4.94956  3.37398  1.05039  4.8859  3.26257  1.49601  4.98139  3.11934  2.16444  4.85407  2.99202  3.23074  4.34479  2.80104  4.58352  4.18565  2.70555  5.5225  3.88326  2.62597  6.66838  3.931  2.70555  7.57554  4.2493  3.16708  8.83282  4.2493  3.54904  9.73998  4.15381  3.70819  10.10602'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':7.5, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':8.8, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN10', 'position': CONST.LR, 'note': '13-3-19-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '4.7745  4.10607  0.62068  4.85407  3.94692  1.03447  4.8859  3.72411  1.57558  4.72675  3.56496  2.1167  4.5676  3.45355  2.59414  4.64718  3.24666  3.2944  4.55169  3.05568  4.1379  4.44028  2.8647  5.01322  4.36071  2.70555  5.80897  4.29705  2.56231  6.70021  4.23339  2.48274  7.6392  4.55169  2.61006  8.89648  5.01322  2.88061  9.77181  5.5225  3.23074  10.64713'
    pre_ml = '5.37927  4.09015  0.41379  5.42701  4.01058  0.85941  5.63391  3.85143  1.55967  5.87263  3.78777  1.97346  6.01587  3.62862  2.49865  6.07953  3.34215  3.42172  6.09544  3.10342  4.23339  6.09544  2.84878  5.17237  6.23868  2.62597  6.23868  6.62064  2.48274  7.4323  6.89119  2.5464  8.2758  6.90711  2.72146  9.15112  6.74796  3.00793  10.02645  6.55698  3.37398  10.74262'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':10.2, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':10.2, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN02', 'position': CONST.LL, 'note': '13-3-19-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '6.39783  3.46947  0.65251  6.28642  3.35806  1.09813  6.22276  3.31032  1.40052  6.19093  3.10342  1.71882  6.28642  2.9761  2.19627  6.4774  2.88061  2.72146  6.7957  2.75329  3.45355  7.27315  2.46682  4.85407  7.48005  2.35542  6.55698  7.54371  2.48274  8.11665  7.38456  2.76921  9.73998  7.16175  3.15117  11.31556  7.33681  3.43764  12.54102'
    pre_ml = '2.67372  3.24666  1.46418  2.6578  3.23074  1.87797  2.6578  3.11934  2.48274  2.67372  2.91245  3.54904  2.68963  2.6578  4.5676  2.73738  2.40317  5.57025  3.08751  2.24401  6.63655  3.26257  2.27584  7.44822  3.51721  2.40317  8.43495  3.64453  2.62597  9.53308  3.94692  2.99202  10.69488  4.21747  3.2944  11.63386  4.34479  3.42172  12.50919'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':10.6, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':9.4, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN03', 'position': CONST.LL, 'note': '13-3-19-apex check, coronal crash', 'weine_classification': 3, 'canals':[] }
    pre_mb = '4.39254  2.25993  0.65251  4.42437  2.38725  1.16179  4.37662  2.51457  1.84614  4.21747  2.61006  2.78512  4.09015  2.73738  3.48538  4.09015  2.81695  4.37662  4.15381  2.80104  5.61799  4.09015  2.78512  6.65247  3.97875  2.5464  8.21214  4.20156  2.0212  9.99462  4.09015  1.32094  11.41105'
    pre_ml = '6.17502  2.16444  1.41643  6.31825  2.48274  1.79839  6.4774  2.70555  2.35542  6.52515  2.88061  3.05568  6.6843  2.8647  4.10607  6.4774  2.84878  5.93629  6.58881  2.78512  6.82753  6.66838  2.56231  7.90975  6.62064  2.27584  9.07155  6.27051  1.86205  10.42433  6.28642  1.54375  11.2519  6.60472  1.17771  11.95216'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.1, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':8.5, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN04', 'position': CONST.LL, 'note': '13-3-19-apex check, coronal crash, direction???', 'weine_classification': 2, 'canals':[] }
    pre_mb = '5.26786  2.68963  0.85941  5.37927  2.84878  1.67107  5.36335  2.92836  3.02385  5.0928  3.02385  4.15381  4.36071  3.26257  5.93629  3.88326  3.37398  7.46413  3.83551  3.40581  8.40312  3.91509  3.23074  9.69223  4.07424  2.8647  10.77446  3.94692  2.51457  11.72935'
    pre_ml = '5.28378  2.70555  0.87532  5.47476  2.89653  2.03712  5.87263  2.96019  3.26257  6.38191  3.15117  4.91773  6.7957  3.24666  5.85672  7.14583  3.31032  6.92302  7.14583  3.15117  9.27844  6.95485  2.84878  10.34475  6.90711  2.5464  11.63386'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.7, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':9.8, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN06', 'position': CONST.LL, 'note': '13-3-19-apex check, coronal spot check', 'weine_classification': 2, 'canals':[] }
    pre_mb = '6.01587  3.37398  1.09813  6.0477  3.08751  1.49601  6.09544  2.75329  2.21218  6.11136  2.45091  3.56496  6.1591  2.40317  5.10871  6.46149  2.53048  6.70021  6.60472  2.84878  8.13256  6.01587  3.05568  8.84874  5.92038  3.38989  9.62857  6.07953  3.66045  10.28109'
    pre_ml = '5.33152  3.11934  0.81166  5.47476  3.05568  1.19362  5.55433  2.83287  1.83022  5.4111  2.53048  2.83287  5.29969  2.43499  3.51721  5.01322  2.40317  5.0928  4.74267  2.51457  6.31825  4.59943  2.83287  7.71877  4.82224  3.11934  8.64185  5.14054  3.40581  9.48534  5.18829  3.85143  10.47207'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':7.7, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN11', 'position': CONST.LL, 'note': '13-3-19-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '4.5676  2.46682  0.84349  4.55169  2.78512  1.52784  4.47211  3.03976  2.05303  4.53577  3.34215  3.07159  4.5676  3.54904  4.15381  4.90182  3.59679  5.80897  4.83816  3.56496  6.90711  4.58352  3.45355  8.00524  4.74267  3.24666  9.40576  4.80633  3.05568  10.74262  4.98139  2.89653  11.33148'
    pre_ml = '6.30234  1.98937  0.84349  6.27051  2.14852  1.2732  6.28642  2.43499  1.73473  6.44557  2.84878  2.67372  6.55698  3.16708  3.75594  6.54106  3.37398  5.02914  6.4774  3.37398  6.90711  6.73204  3.23074  8.11665  6.70021  3.10342  9.08746  6.7957  2.83287  10.39249  6.97077  2.72146  10.98135'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.1, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':8.2, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN12', 'position': CONST.LL, 'note': '13-3-19-check all', 'weine_classification': 2, 'canals':[] }
    pre_mb = '6.09544  4.47211  0.57294  6.19093  4.18565  1.48009  6.81162  4.07424  2.67372  7.12992  3.97875  3.62862  7.4323  3.77185  4.7745  7.4323  3.53313  5.64982  7.51188  3.66045  6.62064  7.28907  3.83551  7.48005  7.4323  4.36071  8.46678  7.17766  4.59943  9.26253  7.19358  4.86999  10.31292'
    pre_ml = '6.09544  4.47211  0.57294  5.88855  4.12198  1.63924  5.17237  3.69228  2.81695  4.94956  3.53313  3.43764  4.75858  3.34215  4.53577  4.66309  3.27849  5.93629  4.75858  3.2944  6.92302  4.90182  3.6127  7.92567  5.22012  4.1379  8.9124  5.60208  4.93365  10.1856'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.1, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':8.9, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN15', 'position': CONST.LL, 'note': '13-3-19-check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '7.30498  5.44293  0.71617  7.33681  5.06097  1.49601  7.25724  4.71084  2.32359  7.24132  4.1379  3.69228  7.49596  3.8196  4.85407  7.44822  3.69228  5.8408  7.28907  3.62862  6.74796  6.98668  3.70819  8.3872  6.70021  3.88326  9.42168  6.35008  3.96283  10.59939'
    pre_ml = '4.86999  5.14054  0.4297  4.85407  5.04505  1.16179  4.7745  4.86999  1.87797  4.69492  4.4562  2.89653  4.71084  4.04241  4.12198  4.59943  3.85143  5.04505  4.66309  3.77185  5.79306  4.75858  3.75594  7.12992  4.85407  3.78777  8.18031  4.85407  3.99466  9.62857  4.40846  4.15381  11.01318'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.1, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':8.1, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN16', 'position': CONST.LR, 'note': 'check Buccal, lingual', 'weine_classification': 3, 'canals':[] }
    pre_mb = '5.20421  4.98139  1.05039  5.22012  4.55169  1.35277  5.36335  4.05833  2.10078  5.79306  3.8196  2.92836  6.09544  3.62862  3.91509  6.39783  3.32623  5.42701  6.60472  3.40581  7.25724  6.58881  3.64453  9.00789  6.82753  4.04241  10.8222  7.24132  4.16973  11.64978'
    pre_ml = '4.47211  4.96548  0.57294  4.4562  4.72675  0.84349  4.42437  4.42437  1.30503  4.2493  4.04241  1.95754  4.12198  3.70819  2.75329  4.18565  3.53313  3.54904  4.21747  3.16708  5.23603  4.18565  3.16708  6.77979  4.09015  3.42172  8.40312  4.02649  3.69228  9.77181  4.07424  3.931  10.85403'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.6, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':9.4, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN17', 'position': CONST.LL, 'note': 'check all, direction???', 'weine_classification': 3, 'canals':[] }
    pre_mb = '5.53842  4.99731  0.57294  5.64982  4.93365  1.12996  6.12727  4.79041  2.13261  6.54106  4.53577  3.00793  7.0026  4.10607  4.32888  7.54371  3.66045  6.58881  8.0689  3.72411  8.83282  8.19623  3.97875  10.44024  8.21214  4.31296  12.01583  8.29171  4.48803  12.90706'
    pre_ml = '4.18565  4.55169  1.49601  4.48803  4.5676  2.03712  4.58352  4.39254  2.80104  4.50394  4.10607  3.66045  4.48803  3.78777  4.82224  4.31296  3.53313  6.12727  4.34479  3.42172  7.3209  4.31296  3.42172  8.2758  4.42437  3.58087  9.69223  4.74267  3.94692  11.06092  4.93365  4.15381  12.30229  4.98139  4.31296  13.0503'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':11.2, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':9.7, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN19', 'position': CONST.LL, 'note': 'check all', 'weine_classification': 2, 'canals':[] }
    pre_mb = '5.4111  4.32888  1.19362  5.60208  3.96283  1.43235  5.95221  3.8196  1.79839  6.30234  3.69228  2.61006  6.57289  3.56496  4.32888  6.81162  3.59679  6.23868  6.84345  3.66045  7.65511  6.98668  3.86734  9.11929  6.81162  4.16973  10.40841  6.70021  4.50394  11.58612  6.7957  4.74267  12.33412'
    pre_ml = '5.4111  4.31296  1.19362  5.49067  3.96283  1.44826  5.39518  3.74002  1.83022  5.29969  3.43764  2.72146  5.23603  3.24666  4.44028  5.06097  3.24666  5.98404  5.17237  3.45355  8.24397  5.36335  3.89917  10.47207  5.28378  4.36071  11.68161'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.7, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':9.4, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN23', 'position': CONST.LL, 'note': 'check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '6.50923  3.69228  0.98673  6.54106  3.38989  1.48009  6.55698  3.03976  2.24401  6.366  2.78512  3.183  6.4774  2.68963  4.34479  6.93894  2.73738  5.96812  7.03443  2.8647  7.06626  6.77979  2.99202  7.67103  6.58881  3.31032  9.10338  6.57289  3.51721  9.91504'
    pre_ml = '5.01322  3.45355  1.14588  5.07688  3.183  1.60741  5.14054  2.91245  2.32359  5.12463  2.72146  3.183  4.91773  2.62597  4.32888  4.48803  2.64189  5.85672  4.4562  2.91245  7.28907  4.69492  3.16708  8.3872  4.48803  3.5013  9.59674  4.18565  3.62862  10.13785'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.4, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':7.6, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN24', 'position': CONST.LR, 'note': 'check all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '4.98139  3.89917  1.19362  4.94956  3.62862  1.60741  4.8859  3.35806  2.14852  4.99731  3.19891  2.64189  4.94956  2.99202  3.77185  4.69492  2.96019  5.12463  4.29705  3.183  6.66838  4.36071  3.62862  8.24397  4.64718  4.29705  10.0742'
    pre_ml = '6.12727  3.88326  1.12996  6.11136  3.62862  1.5915  6.09544  3.24666  2.45091  6.27051  3.05568  3.56496  6.73204  2.99202  4.86999  7.114  3.2944  6.92302  7.0026  3.59679  8.0689  7.05034  4.10607  9.4376  7.27315  4.37662  10.23335'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.1, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':7.6, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN25', 'position': CONST.LL, 'note': 'ck all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '7.05034  5.01322  1.00265  7.03443  4.91773  1.62333  7.09809  4.5676  2.5464  7.19358  4.07424  3.59679  7.38456  3.46947  5.01322  7.54371  3.24666  6.76387  7.38456  3.34215  8.18031  7.19358  3.64453  9.21478  7.03443  3.97875  10.24926  6.90711  4.40846  11.20416'
    pre_ml = '3.11934  4.80633  0.47745  3.183  4.90182  0.76392  3.26257  4.91773  1.43235  3.59679  4.50394  2.40317  3.931  4.16973  3.26257  4.29705  3.54904  4.63127  4.28113  3.183  6.14319  4.18565  3.24666  7.73469  4.34479  3.53313  9.13521  3.99466  4.01058  10.53573  3.58087  4.26522  11.52246'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.4, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':9.8, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN26', 'position': CONST.LL, 'note': 'check all, direction ??', 'weine_classification': 2, 'canals':[] }
    pre_mb = '7.40047  1.83022  1.75065  6.85936  2.67372  3.08751  6.366  3.26257  4.20156  5.55433  3.77185  5.18829  5.01322  4.01058  6.19093  4.69492  3.91509  7.65511  4.7745  3.66045  8.96014  4.82224  3.27849  10.28109  4.72675  2.9761  11.09275'
    pre_ml = '7.38456  1.83022  1.75065  6.97077  2.46682  2.73738  6.82753  2.99202  3.89917  7.03443  3.72411  5.26786  7.33681  4.09015  6.50923  7.70286  4.26522  8.11665  7.41639  4.05833  9.53308  7.12992  3.74002  10.55164  6.93894  3.43764  11.64978'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.3, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':9.5, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN27', 'position': CONST.LR, 'note': 'ck all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '4.72675  4.47211  0.73209  4.83816  4.32888  1.22546  4.93365  4.02649  1.87797  4.72675  3.75594  2.91245  4.48803  3.6127  3.931  4.23339  3.51721  5.36335  4.02649  3.54904  6.71613  3.97875  3.70819  7.89384  4.21747  4.10607  9.64449  4.48803  4.36071  10.36066  4.4562  4.47211  10.98135'
    pre_ml = '6.85936  4.59943  0.82758  7.0026  4.40846  1.32094  7.114  4.16973  1.73473  7.19358  3.80368  2.80104  7.38456  3.72411  4.37662  7.62328  3.74002  5.76123  7.79835  3.86734  7.16175  7.79835  4.09015  8.33946  7.54371  4.31296  9.549  7.52779  4.53577  10.297  7.67103  4.69492  11.20416'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.8, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':7.8, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN28', 'position': CONST.LR, 'note': 'check all , direction ?', 'weine_classification': 3, 'canals':[] }
    pre_mb = '4.59943  5.01322  0.81166  4.58352  4.69492  1.25729  4.40846  4.20156  2.10078  4.34479  3.88326  3.19891  4.36071  3.72411  4.20156  4.44028  3.6127  5.82489  5.06097  3.75594  8.32354  5.61799  3.91509  9.42168  5.76123  4.09015  10.36066  5.82489  4.34479  11.28373'
    pre_ml = '7.59145  5.42701  1.32094  7.54371  5.33152  1.55967  7.46413  4.99731  1.95754  7.30498  4.48803  2.59414  7.44822  4.07424  3.48538  7.48005  3.78777  4.44028  7.14583  3.62862  5.82489  7.19358  3.6127  6.98668  7.25724  3.74002  7.90975  6.92302  3.91509  9.08746  6.70021  4.21747  10.20151  6.7957  4.31296  11.04501'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.1, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':9.2, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN29', 'position': CONST.LR, 'note': 'ck all', 'weine_classification': 2, 'canals':[] }
    pre_mb = '6.30234  4.67901  0.748  6.22276  4.4562  1.2732  5.98404  4.10607  1.9098  5.90446  3.70819  2.80104  5.68165  3.31032  3.85143  5.45884  3.10342  4.96548  5.07688  2.8647  6.65247  4.59943  2.8647  8.03707  4.39254  2.89653  9.00789  4.64718  3.08751  10.1856  4.67901  3.27849  11.44288'
    pre_ml = '6.31825  4.69492  0.748  6.25459  4.50394  1.17771  6.09544  4.10607  1.9098  6.06361  3.59679  2.94427  6.28642  3.27849  4.15381  6.50923  3.02385  5.33152  6.7957  2.80104  6.90711  6.95485  2.78512  8.24397  7.08217  2.8647  9.46942  6.93894  3.02385  10.42433  6.90711  3.24666  11.57021'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.9, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':9.4, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN30', 'position': CONST.LL, 'note': 'ck all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '5.10871  2.40317  0.73209  5.12463  2.5464  0.97081  5.02914  2.78512  1.36869  4.82224  3.16708  1.89388  4.51986  3.58087  2.73738  4.34479  3.8196  3.53313  4.20156  4.01058  4.50394  4.09015  4.12198  5.4111  4.09015  4.20156  6.17502  4.04241  4.15381  7.65511  3.85143  4.09015  9.05563  3.97875  3.99466  10.04236  4.15381  3.75594  11.50654'
    pre_ml = '7.24132  2.49865  1.51193  7.19358  2.84878  1.9098  7.20949  3.26257  2.61006  7.30498  3.46947  3.15117  7.4323  3.86734  4.29705  7.46413  4.05833  5.25195  7.40047  4.1379  6.33417  7.40047  4.09015  7.38456  7.17766  3.91509  8.7055  7.01851  3.69228  9.85138  6.90711  3.48538  10.72671  6.93894  3.45355  11.42697'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':10.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':8.7, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN31', 'position': CONST.LR, 'note': 'ck all nice shape', 'weine_classification': 3, 'canals':[] }
    pre_mb = '4.16973  4.28113  0.38196  4.26522  4.1379  0.85941  4.18565  3.94692  1.44826  4.1379  3.86734  2.0212  4.09015  3.69228  2.88061  3.85143  3.40581  3.931  3.66045  3.2944  4.7745  3.40581  3.31032  5.55433  3.23074  3.24666  6.84345  3.2944  3.32623  8.21214  3.59679  3.6127  9.9787  3.99466  3.88326  11.58612'
    pre_ml = '6.73204  4.20156  0.89124  6.71613  4.05833  1.43235  6.73204  3.86734  2.08486  6.74796  3.69228  2.73738  7.0026  3.56496  3.53313  7.28907  3.35806  4.48803  7.54371  3.19891  5.36335  7.7506  3.13525  6.12727  8.02116  3.13525  7.20949  8.02116  3.27849  8.30763  7.79835  3.56496  9.6604  7.7506  4.02649  11.74527'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':10.6, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':9.4, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN33', 'position': CONST.LR, 'note': 'ck all nice shape', 'weine_classification': 3, 'canals':[] }
    pre_mb = '6.41374  3.13525  0.50928  6.58881  3.15117  0.9549  6.92302  3.16708  1.68699  7.19358  3.43764  2.64189  7.49596  3.64453  3.5013  7.70286  3.89917  5.12463  7.73469  3.931  6.50923  7.65511  3.88326  8.05299  7.40047  3.6127  9.78773  7.28907  3.13525  11.31556'
    pre_ml = '3.53313  3.13525  0.60477  3.64453  3.13525  1.11405  3.66045  3.2944  1.76656  3.74002  3.46947  2.32359  3.77185  3.59679  3.07159  3.74002  3.80368  3.99466  3.8196  4.04241  5.85672  3.94692  3.91509  7.68694  4.04241  3.46947  9.40576  4.12198  3.183  10.6153  4.15381  3.03976  11.39514'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':10.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':9.1, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN37', 'position': CONST.LR, 'note': 'ck all hypercementosis', 'weine_classification': 3, 'canals':[] }
    pre_mb = '6.46149  2.14852  1.81431  6.57289  2.37133  2.40317  6.7957  2.78512  3.16708  6.92302  3.07159  3.91509  7.14583  3.23074  4.67901  7.25724  3.42172  5.7294  7.25724  3.51721  6.82753  7.41639  3.56496  8.73733  7.27315  3.53313  9.58083  6.93894  3.5013  10.6153  6.57289  3.45355  11.71344'
    pre_ml = '4.5676  1.68699  0.9549  4.64718  1.86205  1.43235  4.55169  2.32359  2.19627  4.34479  2.76921  3.00793  4.09015  3.27849  4.40846  4.01058  3.5013  5.92038  4.05833  3.56496  7.14583  4.10607  3.56496  8.2758  4.09015  3.42172  9.81955  4.07424  3.32623  10.83811  4.01058  3.2944  11.79301'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.4, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':8.5, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN38', 'position': CONST.LL, 'note': 'ck all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '5.47476  1.51193  0.62068  5.55433  1.67107  1.03447  5.53842  1.94163  1.48009  5.50659  2.1167  1.86205  5.31561  2.27584  2.80104  4.96548  2.61006  3.72411  4.67901  3.21483  5.44293  4.26522  3.58087  7.14583  3.91509  3.53313  8.48269  3.67636  3.23074  9.93096  3.99466  2.96019  10.86995  4.16973  2.3395  12.11131'
    pre_ml = '5.80897  1.63924  0.52519  6.09544  1.76656  0.82758  6.19093  1.86205  1.0663  6.35008  2.08486  1.46418  6.50923  2.19627  2.05303  6.54106  2.24401  2.68963  6.7957  2.49865  3.67636  6.84345  2.76921  4.47211  6.97077  3.183  5.49067  7.06626  3.62862  7.12992  6.92302  3.54904  8.9124  6.81162  3.11934  10.66305  6.92302  2.70555  12.0954'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':10.7, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':10.9, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN45', 'position': CONST.LR, 'note': 'ck all direction ???', 'weine_classification': 3, 'canals':[] }
    pre_mb = '6.89119  2.67372  1.22546  6.95485  2.8647  1.65516  6.89119  3.08751  2.18035  6.71613  3.21483  2.94427  6.57289  3.26257  3.6127  6.4774  3.37398  4.12198  6.60472  3.43764  4.71084  6.60472  3.51721  5.60208  6.76387  3.56496  6.70021  6.89119  3.6127  7.54371  6.92302  3.51721  9.03972  6.71613  3.31032  9.85138  6.70021  3.07159  10.91769  6.7957  2.96019  11.64978'
    pre_ml = '3.80368  2.62597  1.25729  3.88326  2.83287  1.81431  3.99466  3.03976  2.35542  4.16973  3.08751  3.02385  4.31296  3.03976  3.85143  4.42437  3.15117  4.91773  4.42437  3.16708  6.11136  4.32888  3.19891  7.94158  4.64718  3.11934  9.45351  5.02914  2.96019  10.86995  4.93365  2.72146  12.0954'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.3, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':8.6, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN46', 'position': CONST.LL, 'note': 'ck all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '6.97077  3.99466  1.28911  6.84345  3.83551  1.71882  6.66838  3.54904  2.24401  6.66838  3.32623  2.73738  6.82753  3.10342  3.42172  7.06626  2.94427  4.21747  7.114  2.76921  5.37927  6.97077  2.62597  6.4774  6.93894  2.59414  7.09809  6.55698  2.75329  8.73733  6.50923  2.8647  9.88321  6.55698  2.94427  10.48798'
    pre_ml = '4.79041  3.31032  1.22546  4.61535  3.32623  1.63924  4.37662  3.23074  2.16444  4.28113  3.13525  2.72146  4.12198  3.03976  3.31032  4.05833  2.89653  4.02649  4.01058  2.70555  5.01322  4.1379  2.53048  6.31825  4.32888  2.5464  7.67103  4.63127  2.78512  8.9124  4.74267  3.03976  9.89913  4.74267  3.183  10.44024'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':7.9, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':8.0, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN50', 'position': CONST.LR, 'note': 'ck all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '6.98668  1.16179  0.6366  6.97077  1.32094  0.97081  7.01851  1.57558  1.5915  7.19358  1.89388  2.43499  7.27315  2.21218  3.2944  7.60737  2.53048  4.42437  7.60737  2.81695  5.18829  7.76652  2.96019  6.50923  7.83018  2.89653  7.76652  7.78243  2.72146  8.96014  7.4323  2.45091  9.9787  7.25724  2.14852  11.1405'
    pre_ml = '4.69492  0.90715  0.81166  4.66309  1.01856  1.11405  4.58352  1.28911  1.78248  4.42437  1.7029  2.67372  4.23339  2.10078  3.67636  4.12198  2.45091  4.67901  3.99466  2.78512  6.07953  4.16973  2.80104  7.38456  4.44028  2.64189  8.73733  4.67901  2.37133  9.80364  4.85407  2.0212  11.01318  4.80633  1.92571  11.55429'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':8.5, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN51', 'position': CONST.LL, 'note': 'ck all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '3.27849  2.53048  0.68434  3.38989  2.53048  1.22546  3.56496  2.61006  2.24401  3.5013  2.6578  2.64189  3.53313  2.78512  3.46947  3.75594  2.9761  4.28113  3.94692  3.02385  4.7745  3.88326  3.11934  5.55433  3.72411  3.15117  6.17502  3.6127  3.16708  6.39783  3.54904  3.15117  7.08217  3.66045  3.11934  8.22805  4.07424  2.94427  9.42168  4.48803  2.76921  10.36066  4.69492  2.61006  11.06092'
    pre_ml = '5.49067  2.18035  0.6366  5.47476  2.21218  1.00265  5.5225  2.37133  1.55967  5.7294  2.51457  2.05303  6.0477  2.59414  2.49865  6.33417  2.78512  3.37398  6.4774  2.96019  4.36071  6.7957  3.07159  5.01322  7.03443  3.13525  5.90446  7.22541  3.15117  6.70021  7.22541  3.13525  7.25724  7.17766  2.99202  8.3872  6.98668  2.72146  9.29436  6.85936  2.56231  10.01053  6.95485  2.32359  10.53573'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.1, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':8.6, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN52', 'position': CONST.LR, 'note': 'check all complex canal direction???', 'weine_classification': 3, 'canals':[] }
    pre_mb = '7.25724  2.10078  0.92307  7.14583  2.24401  1.22546  7.14583  2.32359  1.71882  7.12992  2.51457  2.57823  7.0026  2.61006  3.15117  7.16175  2.73738  3.94692  7.20949  2.8647  4.55169  7.30498  2.89653  5.17237  7.14583  3.02385  5.71348  6.76387  3.10342  6.366  6.66838  3.05568  6.74796  6.4774  3.05568  7.28907  6.60472  3.11934  7.87792  7.0026  2.8647  8.64185  7.0026  2.72146  9.2307  6.71613  2.48274  10.13785  6.55698  2.29176  10.80628'
    pre_ml = '4.28113  2.0212  1.46418  4.37662  2.24401  1.9098  4.48803  2.46682  2.49865  4.58352  2.62597  3.10342  4.79041  2.80104  3.74002  4.74267  2.96019  4.69492  4.64718  3.03976  5.55433  4.51986  3.11934  6.6843  4.31296  3.00793  7.44822  4.32888  2.94427  8.02116  4.51986  2.75329  9.00789  4.74267  2.38725  10.20151  4.86999  2.18035  10.77446'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.3, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':8.3, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN53', 'position': CONST.LR, 'note': 'ck all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '7.6392  1.35277  0.55702  7.76652  1.62333  1.01856  7.71877  1.9098  1.67107  7.59145  2.35542  2.30767  7.62328  2.62597  2.94427  7.7506  2.9761  3.75594  7.83018  3.24666  4.64718  7.68694  3.38989  5.47476  7.49596  3.56496  6.46149  7.3209  3.70819  7.70286  7.17766  3.72411  8.99198  6.87528  3.77185  10.09011  6.62064  3.66045  11.50654'
    pre_ml = '3.88326  2.19627  1.54375  3.80368  2.29176  1.87797  3.72411  2.43499  2.3395  3.62862  2.59414  2.83287  3.64453  2.80104  3.40581  3.56496  2.96019  3.86734  3.66045  3.24666  4.58352  3.74002  3.51721  5.55433  4.02649  3.72411  6.57289  4.15381  3.75594  7.28907  4.47211  3.8196  8.45086  4.82224  3.83551  9.67632  5.01322  3.77185  10.51981  4.8859  3.45355  12.04765'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':10.3, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':9.5, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN55', 'position': CONST.LR, 'note': 'ck all', 'weine_classification': 3, 'canals':[] }
    pre_mb = '7.3209  1.48009  1.00265  7.36864  1.71882  1.28911  7.4323  1.97346  1.7029  7.46413  2.3395  2.51457  7.55962  2.72146  3.72411  7.6392  2.8647  4.58352  7.6392  2.96019  5.25195  7.60737  2.99202  6.01587  7.57554  3.00793  7.4323  7.54371  2.91245  8.25988  7.33681  2.81695  9.08746  7.3209  2.51457  10.15377'
    pre_ml = '4.99731  1.86205  1.83022  4.98139  2.21218  2.21218  4.86999  2.5464  2.75329  4.69492  2.73738  3.40581  4.66309  2.8647  4.01058  4.63127  2.91245  4.58352  4.50394  3.08751  5.53842  4.4562  3.10342  6.50923  4.50394  3.08751  7.7506  4.53577  2.9761  8.80099  4.4562  2.84878  9.96279  4.29705  2.76921  10.53573'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.0, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':7.4, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN58', 'position': CONST.LL, 'note': '#check all', 'weine_classification': 2, 'canals':[] }
    pre_mb = '4.48803  3.66045  0.70026  4.80633  3.58087  1.57558  5.17237  3.67636  2.40317  5.36335  3.58087  3.03976  5.88855  3.40581  4.37662  6.19093  3.21483  5.36335  6.50923  3.05568  6.31825  6.63655  3.03976  8.00524  6.76387  3.03976  9.18295  6.90711  3.19891  10.72671  6.44557  3.38989  11.8885  6.366  3.51721  12.76383'
    pre_ml = '4.48803  3.62862  0.70026  4.64718  3.56496  1.52784  4.74267  3.67636  2.45091  4.58352  3.32623  4.2493  4.61535  3.15117  5.20421  4.42437  2.99202  6.09544  4.26522  2.89653  7.06626  4.31296  2.92836  9.03972  4.39254  3.05568  10.12194  4.40846  3.24666  11.0291  4.50394  3.46947  12.30229  4.48803  3.59679  12.92298'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':11.2, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':10.5, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN63', 'position': CONST.LR, 'note': '-', 'weine_classification': 2, 'canals':[] }
    pre_mb = '5.90446  4.55169  0.70026  5.88855  4.2493  1.41643  5.7294  3.88326  2.1167  5.58616  3.58087  2.75329  5.07688  3.34215  3.46947  4.74267  3.15117  4.48803  4.71084  3.05568  5.87263  4.47211  3.15117  7.24132  4.51986  3.27849  8.11665  4.72675  3.43764  9.37393  5.4111  3.51721  10.31292  5.74531  3.6127  10.90177'
    pre_ml = '5.90446  4.53577  0.70026  5.92038  4.31296  1.2732  5.92038  3.70819  2.5464  6.06361  3.37398  3.53313  6.62064  3.183  4.51986  7.03443  3.07159  5.42701  7.22541  3.02385  6.54106  7.28907  3.16708  8.02116  7.38456  3.27849  9.46942  7.7506  3.5013  10.48798'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':8.7, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':8.1, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN64', 'position': CONST.LL, 'note': '', 'weine_classification': 2, 'canals':[] }
    pre_mb = '6.58881  1.95754  0.85941  6.46149  2.03712  1.14588  6.03178  2.24401  1.68699  5.69757  2.32359  2.0212  5.04505  2.56231  3.05568  4.50394  2.76921  4.40846  4.1379  3.00793  6.25459  4.05833  3.03976  7.62328  4.12198  3.02385  8.67367  4.32888  2.73738  9.85138  4.21747  2.5464  10.75854'
    pre_ml = '6.57289  1.95754  0.85941  6.65247  2.16444  1.49601  6.98668  2.38725  2.38725  7.17766  2.75329  3.51721  7.12992  3.15117  4.90182  7.09809  3.35806  6.33417  6.93894  3.2944  7.81426  6.76387  3.15117  9.0238  6.70021  2.78512  10.15377  6.76387  2.62597  10.66305'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.6, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':9.2, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN66', 'position': CONST.LL, 'note': '#check all', 'weine_classification': 2, 'canals':[] }
    pre_mb = '5.68165  1.86205  1.75065  5.76123  1.78248  2.10078  5.79306  1.81431  2.45091  5.79306  2.14852  3.00793  5.69757  2.72146  3.99466  5.37927  3.05568  4.79041  4.79041  3.23074  5.74531  4.48803  3.27849  6.54106  4.05833  3.21483  7.6392  4.02649  2.89653  9.18295  4.07424  2.51457  10.58347  3.86734  2.16444  11.71344'
    pre_ml = '5.68165  1.84614  1.75065  5.79306  1.78248  2.16444  5.85672  1.86205  2.59414  5.93629  2.24401  3.32623  5.96812  2.88061  4.40846  6.17502  3.11934  5.12463  6.39783  3.24666  6.01587  6.93894  3.34215  7.46413  6.82753  3.19891  8.46678  6.44557  2.84878  9.70815  6.09544  2.49865  10.83811  6.0477  2.25993  11.44288'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.2, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':8.7, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
    infos.append(specimen_info)


    specimen_info = {'name':'MN67', 'position': CONST.LR, 'note': '', 'weine_classification': 2, 'canals':[] }
    pre_mb = '7.06626  2.21218  0.82758  6.92302  2.37133  1.51193  6.85936  2.68963  2.59414  7.0026  2.78512  3.64453  7.20949  2.88061  5.0928  6.60472  2.91245  6.65247  6.74796  2.73738  7.79835  7.05034  2.56231  8.51452  7.05034  2.29176  10.05828  7.114  1.98937  11.1405'
    pre_ml = '7.05034  2.21218  0.82758  6.82753  2.41908  1.75065  6.66838  2.62597  2.76921  6.27051  2.73738  3.69228  5.34744  2.8647  5.17237  5.58616  2.88061  6.58881  5.26786  2.75329  7.79835  5.06097  2.5464  9.00789  4.8859  2.32359  10.21743  4.66309  2.10078  11.29965'

    specimen_info['canals'].append({'name':'pre-mb', 'furcation_pos':9.2, 'is_buccal_side':True, 'pts_canal': pre_mb, 'pts_opposite': pre_ml})
    specimen_info['canals'].append({'name':'pre-ml', 'furcation_pos':8.7, 'is_buccal_side':False, 'pts_canal': pre_ml, 'pts_opposite': pre_mb})
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

