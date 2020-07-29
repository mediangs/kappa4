# -*- coding: cp949 -*-

"""
Created on 2015. 7. 13.

@author: jongki
"""
import concavity_analysis
import dist_util as du  # collection of utility function
import extract_outlines_from_vertices as eo
from shape_analysis import outline_area, outline_centroid
from constant import CONST
from geom import vector  # vector calculation
from named_tuples import DentinThickness, FileMovement
from rotate import get_rotated_points


class SectionData(object):
    """
    class docs
    """

    def __init__(self, model, section, concavity=True, fixed_long_axis_vector=None, MIN_DIST_BTN_AXIS=2):
        """
        :param model: instance of "ModelData" class
        :param section:
        :param fixed_long_axis_vector:
        :param MIN_DIST_BTN_AXIS:
        """

        self.model = model
        self.fixed_long_axis_vector = fixed_long_axis_vector
        self.concavity = concavity
        self.MIN_DIST_BTN_AXIS = MIN_DIST_BTN_AXIS  # (MIN_DIST_BTN_AXIS)mm 이하이면 std_axis_vector 사용

        # Serial No. 0,1,2,3,... from apex
        # self.index = ndx
        
        # distance from apex(mm)
        self.section = section

        # curve length 를 1로 봤을때 현재 section위치의 비율, 만일 0.5라면 중간
        self.crv_ref_length_ratio = None
        self.crvs_cmp_length_ratio = {}     # {'pst1' : 0.45, 'pst2' : '0.42'}

        # 현재 section면과 교점들
        self.pt_at_crv_ref = None
        self.pt_at_crv_opp_ref = None
        self.pt_at_crvs_cmp = {}

        self.pt_cnl_ref_centroid = None
        self.pt_cnls_cmp_centroid ={}

        #CH(Curve Height)
        self.CH_pt_at_crvs_cmp = {}
        # gc_axis_vector와 직교하는 점
        self.CH_pt_at_CH_axis = None
        # t1 와 직교하는 점, 평면상에서 
        self.tangential_CH_pt_at_crvs_cmp = {}
        # t1 와 직교하는 점
        self.tangential_CH_pt_at_CH_axis = None

        self.t_vector_at_crv_ref = None
        self.major_axis_vector = None
        self.major_axis_t_vector = None
        self.median_major_axis_used = None
    
        self.bdy_major_outline = None
        self.bdy_major_outline_exist = None

        self.cnl_ref_outlines = None
        self.cnl_ref_major_outline = None
        self.cnl_ref_major_outline_exist = None

        self.cnls_cmp_outlines = {}
        self.cnls_cmp_major_outline = {}
        self.cnls_cmp_major_outline_exist = {}

        self.cnls_cmp_p2_outlines = {}
        self.cnls_cmp_major_p2_outline = {}

        self.cnl_opp_ref_major_outline = None
        self.cnls_opp_cmp_major_outline = {}

        # FileMovement(vector angle distance normal_angle)
        self.cnl_straightening = None
        self.cnls_straightened = {}
        self.cnls_transportation = {}   # cnls_transportation['pst'].distance
        self.cnls_centroid_transportation = {}   # cnls_transportation['pst'].distance

        # CanalDimension(p1, p2, width)
        self.cnl_ref_narrow = None      # cnl_ref_narrow.width
        self.cnl_ref_wide = None

        self.cnls_cmp_narrow = {}
        self.cnls_cmp_wide = {}

        # DentinThickness(p_body, p_canal, thickness, angle)
        self.mindist_ref = None         # mindist_ref.thickness,    mindist_ref.angle
        self.mindists_cmp = {}          # mindists_cmp['pst'].thickness
        self.mindists_iod = {}          # mindists_cmp['pst'].thickness

        self.lateral_ref = None
        self.laterals_cmp ={}

        self.counter_lateral_ref = None
        self.counter_laterals_cmp = {}

        self.mesial_ref = None
        self.mesials_cmp = {}

        self.distal_ref = None
        self.distals_cmp = {}

        self.mesial_concavity = None
        self.distal_concavity = None

        self.pt_cnl_ref_cwt = None
        self.cwt_ratios = {}
        
        self.area_cnl_ref = None
        self.area_cnls_cmp = {}

        # Calculated parameters
        self.CH_ref = None          # curve height
        self.CHs_cmp = {}

        self.curvature_ref = None
        self.curvatures_cmp = {}

        self.torsion_ref = None
        self.torsions_cmp = {}

        self.init_attributes()

    def rotate(self, points):
        return get_rotated_points(self.pt_at_crv_ref, self.t_vector_at_crv_ref, points)

    def dump(self, outline=True):

        data = dict()

        data['section'] = self.section
        data['pt_at_crv_ref'] = du.smart_pretty(self.pt_at_crv_ref)
        data['pt_at_crvs_cmp'] = du.smart_pretty(self.pt_at_crvs_cmp)
        data['pt_at_crv_opp_ref'] = du.smart_pretty(self.pt_at_crv_opp_ref)

        data['pt_cnl_ref_centroid'] = du.smart_pretty(self.pt_cnl_ref_centroid)
        data['pt_cnls_cmp_centroid'] = du.smart_pretty(self.pt_cnls_cmp_centroid)

        data['CH_pt_at_crvs_cmp'] = du.smart_pretty(self.CH_pt_at_crvs_cmp)
        data['CH_pt_at_CH_axis'] = du.smart_pretty(self.CH_pt_at_CH_axis)
        data['tangential_CH_pt_at_crvs_cmp'] = du.smart_pretty(self.tangential_CH_pt_at_crvs_cmp)
        data['tangential_CH_pt_at_CH_axis'] = du.smart_pretty(self.tangential_CH_pt_at_CH_axis)

        data['t_vector_at_crv_ref'] = du.smart_pretty(self.t_vector_at_crv_ref)
        data['major_axis_vector'] = du.smart_pretty(self.major_axis_vector)
        data['major_axis_t_vector'] = du.smart_pretty(self.major_axis_t_vector)
        data['median_major_axis_used'] = self.median_major_axis_used

        data['bdy_major_outline_exist'] = self.bdy_major_outline_exist
        data['cnl_ref_major_outline_exist'] = self.cnl_ref_major_outline_exist
        data['cnls_cmp_major_outline_exist'] = self.cnls_cmp_major_outline_exist

        if outline:
            data['bdy_major_outline'] = du.smart_pretty(self.bdy_major_outline, 3)

            # data['cnl_ref_outlines'] = du.pretty(self.cnl_ref_outlines)
            data['cnl_ref_major_outline'] = du.smart_pretty(self.cnl_ref_major_outline, 3)

            # data['cnls_cmp_outlines'] = du.pretty(self.cnls_cmp_outlines)
            data['cnls_cmp_major_outline'] = du.smart_pretty(self.cnls_cmp_major_outline, 3)

            # data['cnls_cmp_p2_outlines'] = du.pretty(self.cnls_cmp_p2_outlines)
            data['cnls_cmp_major_p2_outline'] = du.smart_pretty(self.cnls_cmp_major_p2_outline, 3)

            data['cnl_opp_ref_major_outline'] = du.smart_pretty(self.cnl_opp_ref_major_outline, 3)
            data['cnls_opp_cmp_major_outline'] = du.smart_pretty(self.cnls_opp_cmp_major_outline, 3)

        data['mesial_concavity'] = self.mesial_concavity
        data['distal_concavity'] = self.distal_concavity
        # FileMovement(vector, angle, distance)
        data['cnl_straightening'] = self.cnl_straightening
        data['cnls_straightened'] = self.cnls_straightened
        data['cnls_transportation'] = self.cnls_transportation
        data['cnls_centroid_transportation'] = self.cnls_centroid_transportation

        # CanalDimension(p1, p2, width)
        data['cnl_ref_narrow'] = self.cnl_ref_narrow
        data['cnl_ref_wide'] = self.cnl_ref_wide

        data['cnls_cmp_narrow'] = self.cnls_cmp_narrow
        data['cnls_cmp_wide'] = self.cnls_cmp_wide

        # DentinThickness(p_body, p_canal, thickness, angle)
        data['mindist_ref'] = self.mindist_ref
        data['mindists_cmp'] = self.mindists_cmp
        data['mindists_iod'] = self.mindists_iod

        data['lateral_ref'] = self.lateral_ref
        data['laterals_cmp'] = self.laterals_cmp

        data['counter_lateral_ref'] = self.counter_lateral_ref
        data['counter_laterals_cmp'] = self.counter_laterals_cmp

        data['mesial_ref'] = self.mesial_ref
        data['mesials_cmp'] = self.mesials_cmp

        data['distal_ref'] = self.distal_ref
        data['distals_cmp'] = self.distals_cmp

        data['pt_cnl_ref_cwt'] = du.smart_pretty(self.pt_cnl_ref_cwt)
        data['cwt_ratios'] = du.smart_pretty(self.cwt_ratios)

        data['area_cnl_ref'] = du.smart_pretty(self.area_cnl_ref)
        data['area_cnls_cmp'] = du.smart_pretty(self.area_cnls_cmp)

        data['CH_ref'] = du.smart_pretty(self.CH_ref)
        data['CHs_cmp'] = du.smart_pretty(self.CHs_cmp)

        data['curvature_ref'] = du.smart_pretty(self.curvature_ref)
        data['curvatures_cmp'] = du.smart_pretty(self.curvatures_cmp)

        data['torsion_ref'] = du.smart_pretty(self.torsion_ref)
        data['torsions_cmp'] = du.smart_pretty(self.torsions_cmp)

        return data

    def init_attributes(self):

        if self.section > self.model.crv_ref_length:
            print('requested section %.2f exceed length of canal %.2f' % (self.section, self.model.crv_ref_length))
            return

        print(f' -> [{self.model.crv_name}] {self.section:.2f} --> {self.section/self.model.magnification_ratio:.2f}mm section analysis ...')

        self.set_current_section_info()
        self.set_curve_height_intersection_info()
        self.set_body_outline_info()
        self.set_canal_ref_outline_info()
        self.set_canals_cmp_outline_info()

        if self.model.has_opposite_canal and self.pt_at_crv_opp_ref:
            self.set_opposite_canal_major_outline()

        self.set_canals_cmp_outline_including_point_at_curve_cmp()
        self.set_canals_shaping_vectors_and_angles()
        self.set_canals_centroid_info()
        self.set_canals_dimension_info()
        self.set_dist_info()
        self.set_mindist_and_iod_info()
        self.set_canals_area_info()
        if self.concavity and self.model.has_opposite_canal:
            self.set_concavity_info()
        self.set_rest_parameters()

    def set_rest_parameters(self):

        # curve height
        self.CH_ref = 0.0 if not self.CH_pt_at_CH_axis else (self.pt_at_crv_ref - self.CH_pt_at_CH_axis).length()

        for k, CH_pt_at_crv_cmp in self.CH_pt_at_crvs_cmp.items():
            CH_cmp = 0.0 if not (CH_pt_at_crv_cmp and self.CH_pt_at_CH_axis
                                 ) else (CH_pt_at_crv_cmp - self.CH_pt_at_CH_axis).length()

            self.CHs_cmp.update({k: CH_cmp})

        self.curvature_ref = self.model.crv_ref.get_curvature(self.crv_ref_length_ratio)
        self.torsion_ref = self.model.crv_ref.get_torsion(self.crv_ref_length_ratio)

        for k, pt_at_crv_cmp in self.pt_at_crvs_cmp.items():
            curvature_cmp = None if not pt_at_crv_cmp else self.model.crvs_cmp[k].get_curvature(self.crvs_cmp_length_ratio[k])
            torsion_cmp = None if not pt_at_crv_cmp else self.model.crvs_cmp[k].get_torsion(self.crvs_cmp_length_ratio[k])

            self.curvatures_cmp.update({k: curvature_cmp})
            self.torsions_cmp.update({k: torsion_cmp})

    def set_current_section_info(self):
        """
        => pt_at_crv_ref          : pre-curve와 절단면(current section)의 교차점
        => t_vector_at_crv_ref    : pre-curve교차점의 tangent vector
        => pt_at_crvs_cmp         : post-curve와 절단면(current section)의 교차점
        => pt_at_crv_opp_ref      : post-curve교차점의 tangent vector
        => pre_crv_length_ratio   : pre-curve의 길이에서 현재 교차점까지 길이의 비율(u value)
        => pst_crv_length_ratio   : post-curve의 길이에서 현재 교차점까지 길이의 비율(u value)
        => major_axis_vector      : 현 단면의 장축(sd.pt_at_crv_opp_ref - sd.pt_at_crv_ref)
        => major_axis_t_vector
        => median_major_axis_used
        """
        self.crv_ref_length_ratio = self.section / self.model.crv_ref_length
        u = self.model.crv_ref.length_to_parameter(self.crv_ref_length_ratio)  # 길이값을 u값으로 변환
        self.pt_at_crv_ref = vector(self.model.crv_ref.get_pos(u))

        self.t_vector_at_crv_ref = vector(self.model.crv_ref.get_diff1(u)) if not self.fixed_long_axis_vector else (
            self.fixed_long_axis_vector)  # point and tangent

        for k, crv_cmp in self.model.crvs_cmp.items() or {}:
            pt_at_crv_cmp, u2 = du.intersection_point_of_plane_and_curve(self.pt_at_crv_ref,
                                                                         self.t_vector_at_crv_ref, crv_cmp)
            self.pt_at_crvs_cmp.update({k: pt_at_crv_cmp})
            self.crvs_cmp_length_ratio.update({k: None if not pt_at_crv_cmp else crv_cmp.parameter_to_length(u2)})

        if self.model.crv_opp_ref:
            self.pt_at_crv_opp_ref, _ = du.intersection_point_of_plane_and_curve(self.pt_at_crv_ref,
                                                                                 self.t_vector_at_crv_ref,
                                                                                 self.model.crv_opp_ref)

        if not self.pt_at_crv_opp_ref or (
                self.pt_at_crv_opp_ref - self.pt_at_crv_ref).length() < self.MIN_DIST_BTN_AXIS * self.model.magnification_ratio:
            print('      ---> using std_axis_vector for current section')
            # median_major_axis_vector를 현재 section의 평면에 투영한것
            self.major_axis_vector = self.model.median_major_axis_vector - self.t_vector_at_crv_ref * (
                self.model.median_major_axis_vector.dot(
                    self.t_vector_at_crv_ref) / (self.t_vector_at_crv_ref.length()) ** 2)

            self.major_axis_t_vector = self.t_vector_at_crv_ref
            self.median_major_axis_used = True
        else:
            self.major_axis_vector = self.pt_at_crv_opp_ref - self.pt_at_crv_ref
            self.major_axis_t_vector = self.t_vector_at_crv_ref
            self.median_major_axis_used = False

    def set_curve_height_intersection_info(self):
        """
        => CH_pt_at_crvs_cmp
        => CH_pt_at_CH_axis
        => tangential_CH_pt_at_crvs_cmp
        => tangential_CH_pt_at_CH_axis
        """
        # ===============================================================================
        # 다음에서 Global curvature를 구함
        #
        #                   coronal_end_of_curve_height
        #     CH_axis_vector  |.
        #             ^       |  .
        #             |       | .   .   굚t1
        #             |       |  .    .   굚
        #       pt_at_CH_axis +---.-----.   굚  point_at_pre_curve
        #                     |    .  /   .
        #                     |    /      .
        #                     | /  .     .
        #     t_pt_at_CH_axis +    .    .
        #                     |   .   .
        #                     |
        #                   apical_end_of_curve_height
        #
        # pt_at_CH_axis_of_curve_height : CurveHeight에 해당, global curve에서 gc_axis_vector에 수선의 발을 내렸을때 만나는 점,
        # tangential_point_at_long_axis_of_curve_height : p1과 t1이 이루는 평면과 gc_axis_vector와 만나는 점(canal straightening vector 에 사용)
        # MinDist의 방향과 curve의 방향을 비교할때는 p3t_gc를 사용해야함
        #
        #    => sd.CH_pt_at_crvs_cmp
        #    => sd.CH_pt_at_CH_axis
        #    => sd.tangential_CH_pt_at_crvs_cmp
        #    => sd.tangential_CH_pt_at_CH_axis
        # ===============================================================================

        for k, crv_cmp in self.model.crvs_cmp.items() or {}:
            CH_pt_at_crv_cmp, _ = du.intersection_point_of_plane_and_curve(
                self.pt_at_crv_ref, self.model.CH_axis_vector, crv_cmp)
            self.CH_pt_at_crvs_cmp.update({k: CH_pt_at_crv_cmp})

            # t1 와 직교하는 점, 평면상에서
            tangential_CH_pt_at_crv_cmp, _ = du.intersection_point_of_plane_and_curve(
                self.pt_at_crv_ref, self.major_axis_t_vector, crv_cmp)
            self.tangential_CH_pt_at_crvs_cmp.update({k: tangential_CH_pt_at_crv_cmp})

        # gc_axis_vector와 직교하는 점
        self.CH_pt_at_CH_axis = du.intersection_point_of_plane_and_line(
            self.pt_at_crv_ref, self.model.CH_axis_vector,
            self.model.apical_end_of_CH, self.model.CH_axis_vector)

        # t1 와 직교하는 점
        self.tangential_CH_pt_at_CH_axis = du.intersection_point_of_plane_and_line(
            self.pt_at_crv_ref, self.major_axis_t_vector,
            self.model.apical_end_of_CH, self.model.CH_axis_vector)

    def set_body_outline_info(self):
        """
        bdy_major_outline
        bdy_major_outline_exist
        """
        _, self.bdy_major_outline, self.bdy_major_outline_exist = eo.section_outlines_from_vertices(
            self.pt_at_crv_ref, self.major_axis_t_vector, self.model.facets_bdy, self.model.normals_bdy,
            is_canal=False, magnification_ratio=self.model.magnification_ratio)

    def set_concavity_info(self):
        is_distal = concavity_analysis.is_distal_concavity(self.model.is_buccal_side, self.model.tooth_position)

        self.mesial_concavity = concavity_analysis.concavity_analysis(self.bdy_major_outline, self.pt_at_crv_ref,
                                                                      self.pt_at_crv_opp_ref, self.t_vector_at_crv_ref,
                                                                      self.model.magnification_ratio, not is_distal)
        self.distal_concavity = concavity_analysis.concavity_analysis(self.bdy_major_outline, self.pt_at_crv_ref,
                                                                      self.pt_at_crv_opp_ref, self.t_vector_at_crv_ref,
                                                                      self.model.magnification_ratio, is_distal)

    def set_canal_ref_outline_info(self):
        """
        cnl_ref_outlines
        cnl_ref_major_outline
        cnl_ref_major_outline_exist
        """
        self.cnl_ref_outlines, self.cnl_ref_major_outline, self.cnl_ref_major_outline_exist = eo.section_outlines_from_vertices(
            self.pt_at_crv_ref, self.major_axis_t_vector,
            self.model.facets_cnl_ref, self.model.normals_cnl_ref,
            is_canal=True, magnification_ratio=self.model.magnification_ratio)

    def set_canals_cmp_outline_info(self):
        """
        cnls_cmp_outlines
        cnls_cmp_major_outline
        cnls_cmp_major_outline_exist
        """
        for k, facets_cnl_cmp in self.model.facets_cnls_cmp.items() or {}:
            cnl_cmp_outlines, cnl_cmp_major_outline, cnl_cmp_major_outline_exist = eo.section_outlines_from_vertices(
                self.pt_at_crv_ref,
                self.major_axis_t_vector,
                facets_cnl_cmp, self.model.normals_cnls_cmp[k], is_canal=True,
                magnification_ratio=self.model.magnification_ratio)

            self.cnls_cmp_outlines.update({k: cnl_cmp_outlines})
            self.cnls_cmp_major_outline.update({k: cnl_cmp_major_outline})
            self.cnls_cmp_major_outline_exist.update({k: cnl_cmp_major_outline_exist})

    def set_canals_cmp_outline_including_point_at_curve_cmp(self):
        """
        sd.cnls_cmp_p2_outlines
        sd.cnls_cmp_major_p2_outline
        """
        for k, pt_at_crv_cmp in self.pt_at_crvs_cmp.items() or {}:
            if pt_at_crv_cmp:
                cnl_cmp_p2_outlines, cnl_cmp_major_p2_outline, _ = eo.section_outlines_from_vertices(
                    pt_at_crv_cmp,
                    self.major_axis_t_vector,
                    self.model.facets_cnls_cmp[k], self.model.normals_cnls_cmp[k], is_canal=True,
                    magnification_ratio=self.model.magnification_ratio)

                self.cnls_cmp_p2_outlines.update({k: cnl_cmp_p2_outlines})
                self.cnls_cmp_major_p2_outline.update({k: cnl_cmp_major_p2_outline})

            else:
                # self.cnls_cmp_major_p2_outline = self.cnls_cmp_major_outline[:]
                self.cnls_cmp_major_p2_outline.update({k: self.cnls_cmp_major_outline[k][:]})

    def set_opposite_canal_major_outline(self):
        """
        sd.cnl_opp_ref_major_outline
        sd.cnls_opp_cmp_major_outline
        """
        _, self.cnl_opp_ref_major_outline, _ = eo.section_outlines_from_vertices(
            self.pt_at_crv_opp_ref, self.major_axis_t_vector,
            self.model.facets_cnl_ref, self.model.normals_cnl_ref,
            is_canal=True, magnification_ratio=self.model.magnification_ratio)

        for k, facets_cnl_cmp in self.model.facets_cnls_cmp.items() or {}:
            _, cnl_opp_cmp_major_outline, _ = eo.section_outlines_from_vertices(
                self.pt_at_crv_opp_ref, self.major_axis_t_vector,
                facets_cnl_cmp, self.model.normals_cnls_cmp[k],
                is_canal=True, magnification_ratio=self.model.magnification_ratio)
            self.cnls_opp_cmp_major_outline.update({k: cnl_opp_cmp_major_outline})

    def set_canals_centroid_info(self):
        """
        sd.pt_cnl_ref_centroid
        sd.pt_cnls_cmp_centroid
        """

        #결과값을 vector로 변환해야 None type check 시 문제가 없음
        self.pt_cnl_ref_centroid = vector(outline_centroid(self.pt_at_crv_ref, self.t_vector_at_crv_ref,
                                                           self.cnl_ref_major_outline))

        for k, pt_at_crv_cmp in self.pt_at_crvs_cmp.items() or {}:
            if pt_at_crv_cmp:
                pt_cnl_cmp_centroid = vector(outline_centroid(
                    pt_at_crv_cmp, self.t_vector_at_crv_ref,
                    self.cnls_cmp_major_outline[k]))  # poly_area(vs_canal_post_major)
            else:
                pt_cnl_cmp_centroid = None

            self.pt_cnls_cmp_centroid.update({k:pt_cnl_cmp_centroid})

        self.cnls_centroid_transportation = self.movement_vector_and_angle(self.pt_cnl_ref_centroid,
                                                                           self.pt_cnls_cmp_centroid)

    def lenth_of_vector(self, a, b):
        try:
            return vector(a - b)
        except:
            return None

    def movement_vector_and_angle(self, pt_ref, pt_cmps):

        transportation = {}
        # pt_cmps = {} if not pt_cmps else pt_cmps
        for k, pt_cmp in pt_cmps.items():
            transportation_vector = None if not (pt_ref and pt_cmp) else pt_cmp - pt_ref
            #transportation_vector = self.lenth_of_vector(pt_cmp, pt_ref)
            transportation_angle = None if not transportation_vector else du.normalize_angle(
                du.angle_btn_vectors(self.major_axis_vector, transportation_vector, self.major_axis_t_vector),
                self.model.is_buccal_side, self.model.specimen.tooth_position)

            transportation.update(
                {k: FileMovement(transportation_vector, transportation_angle,
                                 None if not transportation_vector else transportation_vector.length())})
        return transportation

    def set_canals_shaping_vectors_and_angles(self):
        """
        ADDED - 13.10.16
        canal straightening vector, 현재 section면에서 p1과
        tangential_point_at_long_axis_of_curve_height(gc_axis와 면의 교차점)가 만나는 점의 벡터
        FileMovement = namedtuple('FileMovement', 'vector angle distance')
        """

        straightening_vector = None if ((self.tangential_CH_pt_at_CH_axis - self.pt_at_crv_ref).length() == 0
                                        ) else self.tangential_CH_pt_at_CH_axis - self.pt_at_crv_ref

        straightening_angle = None if not (
            straightening_vector) else du.normalize_angle(du.angle_btn_vectors(
            self.major_axis_vector, straightening_vector, self.major_axis_t_vector),
            self.model.is_buccal_side, self.model.specimen.tooth_position)

        self.cnl_straightening = FileMovement(straightening_vector, straightening_angle,
                                              None if not straightening_vector else straightening_vector.length())

        for k, tangential_CH_pt_at_crv_cmp in self.tangential_CH_pt_at_crvs_cmp.items() or {}:
            straightened_vector = None if not tangential_CH_pt_at_crv_cmp or (
                (self.tangential_CH_pt_at_CH_axis - tangential_CH_pt_at_crv_cmp
                 ).length() == 0) else self.tangential_CH_pt_at_CH_axis - tangential_CH_pt_at_crv_cmp

            straightened_angle = None if not straightened_vector else du.normalize_angle(
                du.angle_btn_vectors(self.major_axis_vector, straightened_vector, self.major_axis_t_vector),
                self.model.is_buccal_side, self.model.specimen.tooth_position)

            self.cnls_straightened.update(
                {k: FileMovement(straightened_vector, straightened_angle,
                                 None if not straightened_vector else straightened_vector.length())})

        self.cnls_transportation = self.movement_vector_and_angle(self.pt_at_crv_ref, self.pt_at_crvs_cmp)


    def set_canals_dimension_info(self):

        self.cnl_ref_narrow, self.cnl_ref_wide = du.shortest_and_longest_diameter_of_canal(
            self.pt_at_crv_ref, self.major_axis_vector,
            self.major_axis_t_vector, self.cnl_ref_major_outline, step_angle=1)

        for k, pt_at_crv_cmp in self.pt_at_crvs_cmp.items() or {}:
            if pt_at_crv_cmp:
                cnl_cmp_narrow, cnl_cmp_wide = du.shortest_and_longest_diameter_of_canal(
                    pt_at_crv_cmp, self.major_axis_vector,
                    self.major_axis_t_vector, self.cnls_cmp_major_p2_outline[k], step_angle=1)

                self.cnls_cmp_narrow.update({k: cnl_cmp_narrow})
                self.cnls_cmp_wide.update({k: cnl_cmp_wide})

    def determine_min_dist_iod_info(self, vs_canal_major, canal_center,
                                    major_axis_vector, major_axis_tangent_vector):
        """

        :param vs_body_major:
        :param vs_canal_major:
        :param canal_center: canal center
        :param major_axis_vector:
        :param major_axis_tangent_vector:
        :return:
        """
        iod_angle = self.mindist_ref.angle
        iod_angle = du.normalize_angle(iod_angle, self.model.is_buccal_side, self.model.specimen.tooth_position)
        vs_body_mindist = self.mindist_ref.p_body

        try:
            vs_canal_mindist = du.angled_point_from_vertices(canal_center, major_axis_vector,
                                                             major_axis_tangent_vector, vs_canal_major, iod_angle,
                                                             self.model.magnification_ratio)

        except TypeError:
            print("   --> can not calculate mindist info")
            return DentinThickness(vector([0, 0, 0]), vector([0, 0, 0]), 0, 0)

        return DentinThickness(vs_body_mindist, vs_canal_mindist,
                               (vector(vs_body_mindist)-vector(vs_canal_mindist)).length(), self.mindist_ref.angle)

    def determine_min_dist_info(self, vs_body_major, vs_canal_major, canal_center,
                                major_axis_vector, major_axis_tangent_vector):
        """

        :param vs_body_major:
        :param vs_canal_major:
        :param canal_center: canal center
        :param major_axis_vector:
        :param major_axis_tangent_vector:
        :return:
        """
        #todo: 길이 측정 알고리즘 수정요, ==> mindist between two contour

        try:

            # _, vs_body_mindist = du.mindist_btn_contour_and_point(vs_body_major, p1)
            #
            # # 근관의 장축(p2-p1)과 치근최단거리의 축(vs_body_mindist - p1)의 각을 구함
            # mindist_angle = du.angle_btn_vectors(major_axis_vector, vs_body_mindist - p1, major_axis_tangent_vector)
            # vs_canal_mindist = du.angled_point_from_vertices(p1, major_axis_vector, major_axis_tangent_vector,
            #                                                      vs_canal_major, mindist_angle,
            #                                                      self.model.magnification_ratio)

            vs_body_mindist, vs_canal_mindist, mindist, mindist_angle = du.mindist_btn_contours_crossing_point(
                vs_body_major, vs_canal_major, canal_center, major_axis_vector, major_axis_tangent_vector,
                self.model.magnification_ratio)

        except TypeError:
            print("   --> can not calculate mindist info")
            return DentinThickness(vector([0, 0, 0]), vector([0, 0, 0]), 0, 0)

        return DentinThickness(vs_body_mindist, vs_canal_mindist, mindist,
                               du.normalize_angle(mindist_angle, self.model.is_buccal_side, self.model.specimen.tooth_position))

    def determine_dist_intersection_vertexes(self, direction, pt_at_crv, vs_canal_major):

        vs_body = du.angled_point_from_vertices(pt_at_crv, self.major_axis_vector, self.major_axis_t_vector,
                                                self.bdy_major_outline, direction,
                                                self.model.magnification_ratio, self.bdy_major_outline_exist)
        vs_canal = du.angled_point_from_vertices(pt_at_crv, self.major_axis_vector, self.major_axis_t_vector,
                                                 vs_canal_major, direction, self.model.magnification_ratio)

        # 만일 direction에 해달되는 점이 없는 경우(None이 반환된 경우 dentinthickness를 모두 0,0,0 으로 설정
        return DentinThickness(vs_body, vs_canal, (vs_body - vs_canal).length(),
                               direction) if vs_canal and vs_body else DentinThickness(vector([0, 0, 0]),
                                                                                       vector([0, 0, 0]), 0, direction)

    def set_dist_info(self):

        self.lateral_ref = self.determine_dist_intersection_vertexes(
            180, self.pt_at_crv_ref, self.cnl_ref_major_outline)

        self.counter_lateral_ref = self.determine_dist_intersection_vertexes(
            0, self.pt_at_crv_ref, self.cnl_ref_major_outline)

        self.mesial_ref = self.determine_dist_intersection_vertexes(
            du.convert_tooth_surface_to_angle(CONST.MESIAL, self.model.is_buccal_side, self.model.tooth_position),
            self.pt_at_crv_ref, self.cnl_ref_major_outline)

        self.distal_ref = self.determine_dist_intersection_vertexes(
            du.convert_tooth_surface_to_angle(CONST.DISTAL, self.model.is_buccal_side, self.model.tooth_position),
            self.pt_at_crv_ref, self.cnl_ref_major_outline)

        for k, pt_at_crv_cmp in self.pt_at_crvs_cmp.items() or {}:
            if pt_at_crv_cmp:
                lateral_cmp = self.determine_dist_intersection_vertexes(
                    180, pt_at_crv_cmp, self.cnls_cmp_major_outline[k])

                counter_lateral_cmp = self.determine_dist_intersection_vertexes(
                    0, pt_at_crv_cmp, self.cnls_cmp_major_outline[k])

                mesial_cmp = self.determine_dist_intersection_vertexes(
                    du.convert_tooth_surface_to_angle(
                        CONST.MESIAL, self.model.is_buccal_side, self.model.tooth_position),
                    pt_at_crv_cmp, self.cnls_cmp_major_outline[k])

                distal_cmp = self.determine_dist_intersection_vertexes(
                    du.convert_tooth_surface_to_angle(
                        CONST.DISTAL, self.model.is_buccal_side, self.model.tooth_position),
                    pt_at_crv_cmp, self.cnls_cmp_major_outline[k])

                self.laterals_cmp.update({k: lateral_cmp})
                self.counter_laterals_cmp.update({k: counter_lateral_cmp})
                self.mesials_cmp.update({k: mesial_cmp})
                self.distals_cmp.update({k: distal_cmp})

    def set_mindist_and_iod_info(self):
        """
        pt_pre_mindist_at_bdy, ==>  mindist_ref.ptb, mindist_ref.ptc, mindist_ref.angle
        pt_pre_mindist_at_cnl,
        angle_pre_mindist

        pt_pst_mindist_at_bdy, ==> mindists_cmp.p1, mindists_cmp.p2, length, mindists_cmp.angle
        pt_pst_mindist_at_cnl,
        angle_pst_mindist

        pt_cnl_ref_cwt
        cwt_ratios
        """

        # mindist_ref should be ==> ? (sd.pst_mindist.p_body - sd.pt_cnl_pre_cwt).length()

        self.mindist_ref = self.determine_min_dist_info(
            self.bdy_major_outline, self.cnl_ref_major_outline,
            self.pt_at_crv_ref, self.major_axis_vector, self.major_axis_t_vector)

        for k, pt_at_crv_cmp in self.pt_at_crvs_cmp.items() or {}:
            if pt_at_crv_cmp:
                mindist_cmp = self.determine_min_dist_info(
                    self.bdy_major_outline, self.cnls_cmp_major_outline[k],
                    pt_at_crv_cmp, self.major_axis_vector, self.major_axis_t_vector)

                # mindist_cmp = self.determine_min_dist_info(
                #     self.bdy_major_outline, self.cnls_cmp_major_outline[k],
                #     self.pt_at_crv_ref, self.major_axis_vector, self.major_axis_t_vector)

                self.mindists_cmp.update({k: mindist_cmp})

                mindist_iod = self.determine_min_dist_iod_info(
                    self.cnls_cmp_major_outline[k], self.pt_at_crv_ref,
                    self.major_axis_vector, self.major_axis_t_vector)

                assert(mindist_iod.p_body == self.mindist_ref.p_body)
                assert(mindist_iod.angle == self.mindist_ref.angle)

                self.mindists_iod.update({k: mindist_iod})

                dist_body_to_canal_ref = (mindist_iod.p_body - self.mindist_ref.p_canal).length()
                dist_body_to_canal_iod = (mindist_iod.p_body - mindist_iod.p_canal).length()

                cwt_ratio = (dist_body_to_canal_ref - dist_body_to_canal_iod) / dist_body_to_canal_ref

                self.cwt_ratios.update({k: 0 if cwt_ratio < 0 else cwt_ratio})

                # self.pt_cnl_ref_cwt = du.angled_point_from_vertices(
                #     self.pt_at_crv_ref, self.major_axis_vector,
                #     self.major_axis_t_vector, self.cnl_ref_major_outline, mindist_cmp.angle,
                #     self.model.magnification_ratio)
                #
                # cwt_ratio = ((mindist_cmp.p_body - self.pt_cnl_ref_cwt).length() - (
                #     mindist_cmp.p_body - mindist_cmp.p_canal).length()) / (
                #     mindist_cmp.p_body - self.pt_cnl_ref_cwt).length()
                #
                # self.cwt_ratios.update({k: 0 if cwt_ratio < 0 else cwt_ratio})

    def set_canals_area_info(self):
        """
        sd.area_cnl_ref
        sd.area_cnls_cmp
        """

        self.area_cnl_ref = outline_area(self.pt_at_crv_ref,
                                         self.t_vector_at_crv_ref,
                                         self.cnl_ref_major_outline)  # poly_area(vs_canal_pre_major)

        for k, pt_at_crv_cmp in self.pt_at_crvs_cmp.items() or {}:
            if pt_at_crv_cmp:
                area_cnl_cmp = outline_area(
                    pt_at_crv_cmp,
                    self.t_vector_at_crv_ref,
                    self.cnls_cmp_major_outline[k])  # poly_area(vs_canal_post_major)
            else:
                area_cnl_cmp = None

            self.area_cnls_cmp.update({k:area_cnl_cmp})


def gus18_model_analysis():
    from class_model import ModelData
    import data_g18_canals as data_set

    specimen_data = dict()

    md = ModelData(data_set.specimens[2], canal_ref='pre-ml')
    specimen_data['model'] = md.dump(curve_pts=True)
    sd = SectionData(md, 13.2).dump(outline=True)




def ljkcs_model_analysis():
    import json
    from class_model import ModelData
    import data_ljkcs_multimodel as data_set

    specimen_data = dict()

    for specimen in data_set.roots:
        evaluating_canals = [CONST.BUCCAL, CONST.LINGUAL]
        for canal in evaluating_canals:
            md = ModelData(specimen, evaluating_canal=canal, canal_ref='pre', canals_cmp=['blx'])
            specimen_data['model'] = md.dump(curve_pts=True)
            specimen_data['sections'] = [SectionData(md, x / 10.0).dump(outline=True) for x in
                                         range(0, int(md.crv_ref_length * 10), 2)]

            filename = '../working/ljkcs/'+md.crv_name+'.02mm.json'
            with open(filename, 'w') as f:
                f.write(json.dumps(specimen_data))

            specimen_data = {}


def test():
    import json
    from class_model import ModelData

    # import data_ljkrp1_multimodel as data_set
    import data_ljkcs_canals as data_set
    # import data_mx_multimodel as data_set

    specimens_data = {}
    specimen_data = dict()


    # md = ModelData(data_set.roots[0], evaluating_canal=CONST.BUCCAL,
    #               canal_ref='pre', canals_cmp=['blx', 'ptu', 'rcp'])

    # md = ModelData(data_set.roots[0], evaluating_canal=CONST.BUCCAL, canal_ref='pre', canals_cmp=['blx'])
    # specimen_data['model'] = md.dump(curve_pts=False)
    # specimen_data['sections'] = [SectionData(md, x/10.0).dump(outline=False) for x in range(0, int(md.crv_ref_length * 10), 20)]

    for specimen in data_set.roots:

        evaluating_canals = [CONST.BUCCAL, CONST.LINGUAL]

        for canal in evaluating_canals:
            md = ModelData(specimen, is_buccal_side=canal, canal_ref='pre', canals_cmp=['blx'])
            specimen_data['model'] = md.dump(curve_pts=False)
            specimen_data['sections'] = [SectionData(md, x / 10.0).dump(outline=False) for x in
                                         range(0, int(md.crv_ref_length * 10), 10)]
            specimens_data.update({md.crv_name: specimen_data})
            specimen_data = {}

            md = None

    filename = '../ljkcs.both.all.1mm.json'

    with open(filename, 'w') as f:
        f.write(json.dumps(specimens_data))


if __name__ == '__main__':
    #test()
    # ljkcs_model_analysis()
    gus18_model_analysis()
