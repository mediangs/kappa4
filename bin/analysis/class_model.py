# -*- coding: cp949 -*-

"""
Created on 2016. 10. 23.

@author: jongki
"""

import dist_util as du  # collection of utility function
import v3d
from constant import CONST
from geom import vector  # vector calculation


class ModelData(object):

    def __init__(self, specimen,
                 canal_ref='pre-b',
                 canals_cmp=None,
                 read_model=True,
                 wrl_export=False):

        self.specimen = specimen
        self.name = specimen.name
        self.crv_name = self.name + '-' + canal_ref  # LJKCS01-pre-b", "BLX02-pre-b" 등의 형식으로 이름을 생성
        self.tooth_position = specimen.tooth_position
        self.wrl_export = wrl_export
        self.magnification_ratio = self.specimen.magnification_ratio

        # specimen.canals[x].name 과 canal_ref 가 같은것을 cnl_ref로 설정함
        # cnl_ref는 필수, 보통 "pre-b"

        self.cnl_ref = [c for c in specimen.canals if c.name == canal_ref][0]
        assert(self.cnl_ref is not None)
        self.is_buccal_side = self.cnl_ref.is_buccal_side  # canal_ref 의 방향 buccal side or lingual side

        self.has_opposite_canal = self.cnl_ref.has_opposite_canal

        self.length = self.cnl_ref.length
        self.furcation_pos = self.cnl_ref.furcation_pos

        self.cnls_cmp = {}
        if canals_cmp:
            for c in specimen.canals:
                if c.name in canals_cmp:
                    self.cnls_cmp.update({c.name: c})
            assert(len(canals_cmp) == len(self.cnls_cmp))

        self.facets_cnl_ref = None
        self.facets_cnls_cmp = {}
        self.facets_bdy = None

        self.normals_cnl_ref = None
        self.normals_cnls_cmp = {}
        self.normals_bdy = None

        # curve1_pre = Nerve_path.create(pts)
        # pre_crv는 curve1_pre 또는 curve2_pre
        # type : Nerve_path, 3rd order B-spline curve

        self.crv_ref = None
        self.crv_opp_ref = None
        self.crvs_cmp = {}

        # CH : Curve Height
        self.apical_end_of_CH = None
        self.coronal_end_of_CH = None
        self.CH_axis_vector = None #curve_height_axis_vector

        self.read_model = read_model
        self.init_attributes()

    @property
    def crv_ref_length(self):
        return self.crv_ref.get_appr_len()

    @property
    def pts_of_crv_ref(self):
        # pre_crv를 점들의 배열로 만든것 (100 개의 점이 기본값임)
        return du.curve_to_points(self.crv_ref)

    @property
    def pts_of_crvs_cmp(self):
        if bool(self.crvs_cmp):
            pts = {}
            for k, v in self.crvs_cmp.items():
                pts.update({k: du.curve_to_points(v)})
            return pts
        else:
            return None

    def pts_of_crv(self, crv):
        return du.curve_to_points(crv)

    @property
    def pts_of_crv_opp_ref(self):
        return du.curve_to_points(self.crv_opp_ref)

    @property
    def median_major_axis_vector(self):
        """
        curve의 중간지점에서 c1과 aux_c1을 연결한 vector
        각 평면(SectionData) 분석시  타원 장축간의 거리(pt_at_pre_crv, pt_at_crv_opp_ref)가 기본값 이하일 경우 사용할 벡터
        """
        std_axis_u = 0.5  # 근관의 중간 값을 사용
        p1, t1 = vector(self.crv_ref.get_pos(std_axis_u)), vector(self.crv_ref.get_diff1(std_axis_u))
        aux_p1, _ = du.intersection_point_of_plane_and_curve(p1, t1, self.crv_opp_ref)
        return aux_p1 - p1

    def dump_curve_pts(self):
        data = dict()
        data['pts_of_crv_ref'] = du.smart_pretty(self.pts_of_crv_ref)
        return data

    def dump(self, curve_pts=True):

        data = dict()
        data['name'] = self.name
        data['crv_name'] = self.crv_name
        data['crv_ref_length'] = du.smart_pretty(self.crv_ref_length)
        data['length'] = self.length
        data['furcation_pos'] = self.furcation_pos
        data['is_buccal_side'] = self.is_buccal_side
        data['has_opposite_canal'] = self.has_opposite_canal
        data['median_major_axis_vector'] = du.smart_pretty(self.median_major_axis_vector)
        data['magnification_ratio'] = self.magnification_ratio

        # added for chart_drawer
        data['bounding_box'] = du.smart_pretty(self.specimen.bounding_box)
        data['apical_end_of_CH'] = du.smart_pretty(self.apical_end_of_CH)
        data['coronal_end_of_CH'] = du.pretty(self.coronal_end_of_CH)
        data['weine_classification'] = self.specimen.weine_classification
        # data['note'] = self.specimen.note

        if curve_pts:
            data['pts_of_crv_ref'] = du.smart_pretty(self.pts_of_crv_ref)
            data['pts_of_crvs_cmp'] = du.smart_pretty(self.pts_of_crvs_cmp)
            data['pts_of_crv_opp_ref'] = du.smart_pretty(self.pts_of_crv_opp_ref)

        return data

    def remove_facets(self):
        self.facets_cnl_ref = None
        self.facets_cnls_cmp = None
        self.facets_bdy = None

    def init_attributes(self):

        if self.read_model:
            self.read_models()
        self.allocate_curves_for_analysis()
        self.set_curve_height_axis_info()

    def read_models(self):
        """
        메모리 관리때문에 specimen class에 v3d 파일을 할당하면 안됨
        => self.facets_cnl_ref
        => self.facets_cnl_cmp
        => self.facets_bdy
        """

        files = [self.specimen.body_path, self.cnl_ref.path]
        files.extend([v.path for k, v in self.cnls_cmp.items() or {}])

        for filename in files:
            print('Loading v3d file :{name} ...'.format(name=filename))

        self.facets_bdy, self.normals_bdy = v3d.read_facets(self.specimen.body_path)
        self.facets_cnl_ref, self.normals_cnl_ref = v3d.read_facets(self.cnl_ref.path)

        if self.wrl_export:
            v3d.export_as_wrl(self.facets_bdy, self.specimen.body_path + '.wrl')
            v3d.export_as_wrl(self.facets_cnl_ref, self.cnl_ref.path + '.wrl')

        for k, v in self.cnls_cmp.items() or {}:
            facets, normals = v3d.read_facets(v.path)
            self.facets_cnls_cmp.update({v.name: facets})
            if self.wrl_export: v3d.export_as_wrl(facets, v.path + '.wrl')

            self.normals_cnls_cmp.update({v.name: normals})

    def allocate_curves_for_analysis(self):
        """
        Parameter class의
            curve1_pre, curve1_post,curve2_pre, curve2_post 를
        ModelData class의
           pre_crv, pst_crv, opp_pre_crv에 할당함
        """
        self.crv_ref = self.cnl_ref.curve_canal   # Major curve measured
        self.crv_opp_ref = self.cnl_ref.curve_opposite  # Opposite side curve

        if self.cnls_cmp:
            for k, v in self.cnls_cmp.items():
                self.crvs_cmp.update({k: v.curve_canal})  # Major curve measured

    def set_curve_height_axis_info(self):
        """
        Determine axis for measuring curve height
        => apical_end_of_CH
        => coronal_end_of_CH
        => CH_axis_vector
        """
        curve_len = self.crv_ref_length
        pos_gc_start, pos_gc_end = 0, 0
        self.apical_end_of_CH = vector(self.crv_ref.get_pos(self.crv_ref.length_to_parameter(
            pos_gc_start / curve_len)))
        # u=0.3
        # p_gc_start = vector(curve.get_pos(0.3))
        self.coronal_end_of_CH = vector(self.crv_ref.get_pos(self.crv_ref.length_to_parameter(
            (curve_len - pos_gc_end) / curve_len)))
        self.CH_axis_vector = self.coronal_end_of_CH - self.apical_end_of_CH


def export_wrls():
    import data_ljkcs_multimodel as data_set
    # import data_mx_multimodel as data_set

    for specimen in data_set.roots:
        ModelData(specimen, wrl_export=True, canal_ref='pre-b', canals_cmp=['blx-b'])

def export_canals_axis_coord():

    # import data_ljkrp1_multimodel as data_set
    import data_ljkcs_multimodel as data_set
    # import data_mx_multimodel as data_set

    specimens_data = {}
    specimen_data = dict()

    for specimen in data_set.roots:

        evaluating_canals = [CONST.BUCCAL, CONST.LINGUAL]

        for canal in evaluating_canals:
            md = ModelData(specimen, evaluating_canal=canal, canal_ref='pre', canals_cmp=['blx'])

            print(md.crv_name + '-pre')
            print(md.pts_of_crv_ref)

            print(md.crv_name + '-opp')
            print(md.pts_of_crv_opp_ref)

            for k, v in md.pts_of_crvs_cmp.items():
                print(md.crv_name + '-' + k)
                print(md.pts_of_crvs_cmp[k])



def model_data_test():
    import data_ljkrp1_canals as data_set
    md = ModelData(data_set.specimens[0], canal_ref='pre-mb', wrl_export=True, canals_cmp=['rcp-mb', 'ptu-mb', 'blx-mb'])

    print (md.name)
    print (md.crv_name)
    print (md.crv_ref_length)
    print (md.furcation_pos)
    print ()
    print (md.pts_of_crv_opp_ref)
    print (md.dump(curve_pts=False))


def model_data_gus_test():
    import data_gus18_canals as data_set
    md = ModelData(data_set.roots[0], canal_ref='pre-mb')
    # md = ModelData(data_set.roots[0], evaluating_canal=CONST.BUCCAL, canal_ref='pre', wrl_export=True)
    print (md.name)
    print (md.crv_name)
    print (md.crv_ref_length)
    print (md.furcation_pos)
    print ()
    print (md.pts_of_crv_opp_ref)
    print (md.dump(curve_pts=False))



if __name__ == '__main__':
    model_data_test()
    # model_data_gus_test()
    #export_wrls()
    #export_canals_axis_coord()
