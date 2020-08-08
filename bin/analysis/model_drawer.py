# -*- coding: cp949 -*-

'''
Created on 2015. 7. 18.
Modified for competable with latest module : 2018.10.21
@author: jongki
'''

from __future__ import division

import numpy as np

import dist_util as du
from extract_outlines_from_vertices import sort_and_segment_vertices
from constant import CONST
from geom import vector


def draw_pre_and_post_canal_axis(model3d, cfg, colors, model_header):
    pts_of_crv_ref = model_header['pts_of_crv_ref']
    if pts_of_crv_ref:
        model3d.plot_points_detail(pts_of_crv_ref, colors.canal_axis_pre,
                                   label='' if not cfg.legend else (model_header['crv_name']))
    pts_of_crvs_cmp = model_header['pts_of_crvs_cmp']
    if pts_of_crvs_cmp:
        for i, k in enumerate(pts_of_crvs_cmp):
            model3d.plot_points_detail(pts_of_crvs_cmp[k],
                                       colors.canal_axis_post[i % len(colors.canal_axis_post)],
                                       label='' if not cfg.legend else k)
    if not ('has_opposite_canal' in model_header) or model_header['has_opposite_canal']:
        model3d.plot_points_detail(model_header['pts_of_crv_opp_ref'], colors.canal_axis_opp,
                                   label='' if not cfg.legend else 'Opposite canal axis')
    curve_name_printed = True

    return curve_name_printed


def draw_canal_centroids(model3d, colors, section):
    pt_ref = section['pt_cnl_ref_centroid']
    if pt_ref:
        model3d.plot_marker([pt_ref], colors.canal_centroid_pre)

    pts_cmp = section['pt_cnls_cmp_centroid']
    if pts_cmp:
        for i, k in enumerate(pts_cmp):
            model3d.plot_marker([pts_cmp[k]],
                                colors.canal_centroid_post[i % len(colors.canal_centroid_post)])


def draw_crossing_point_of_canal_axes(model3d, cfg, colors, model_header, section):
    pt_ref = section['pt_at_crv_ref']
    if pt_ref:
        model3d.plot_marker([pt_ref], colors.crossing_point_pre)

    if not ('has_opposite_canal' in model_header) or model_header['has_opposite_canal']:
        model3d.plot_marker([section['pt_at_crv_opp_ref']], colors.crossing_point_pre)

    pts_cmp = section['pt_at_crvs_cmp']
    if pts_cmp:
        for i, k in enumerate(pts_cmp):
            model3d.plot_marker([pts_cmp[k]],
                                colors.canal_axis_post[i % len(colors.canal_axis_post)][:1])


def draw_root_outlines(model3d, cfg, colors, model_header, section, curve_name_printed, magnification_ratio):
    # todo:  section['section']/magnification_ratio 수정
    if section['bdy_major_outline_exist']:
        if len(cfg.sections) == 1 or (
                cfg.highlight_sections and (
                section['section'] / magnification_ratio in cfg.highlight_sections)):
            contour_color_style = colors.highlighted_body_outline
        else:
            contour_color_style = colors.normal_body_outline
        label = '' if not cfg.legend else f'{"Section" if curve_name_printed else model_header["crv_name"]}{section["section"] / magnification_ratio:.2f}mm from apex'
        model3d.plot_points_detail(section['bdy_major_outline'], contour_color_style, label=label)

    else:
        label = '' if not cfg.legend else f'contour of {section["section"] / magnification_ratio:.2f}mm from apex'
        model3d.plot_points(section['bdy_major_outline'], 'yo', markersize=1, label=label)


def draw_curve_height_arrow(model3d, cfg, colors, section, magnification_ratio):
    # just for labeling
    if not None in section['cnl_straightening']:
        model3d.plot_points([[0, 0, 0], [0, 0, 0]], 'b--',
                            label='' if not cfg.legend
                            else 'curve height: %.2fmm, %.0f`' % (
                                section['cnl_straightening'][CONST.FM_DISTANCE] / magnification_ratio,
                                section['cnl_straightening'][CONST.FM_ANGLE]))

    model3d.plot_arrow(section['tangential_CH_pt_at_CH_axis'], section['pt_at_crv_ref'],
                       color=colors.ch_arrow[0], ls=colors.ch_arrow[1])


def draw_pre_canal_outlines(model3d, cfg, colors, section, magnification_ratio):
    # 모든 근관을 그림(section plane 과 근관이 교차하는 모든점을 표시)
    # 현재 version에서는 안됨
    if cfg.all_canal_outlines and section['cnl_ref_major_outline']:
        for vs in sort_and_segment_vertices([section['cnl_ref_major_outline']], inner_vertex=None,
                                            is_canal=True,magnification_ratio=magnification_ratio):
            for v in vs:
                model3d.plot_points_detail(v, colors.canal_outline_pre)

        # 평면(section plane)에 상태측 curve의 교점이 있다면
        if section['pt_at_crv_opp_ref']:
            if section['cnl_opp_ref_major_outline'] and not du.is_line_inside_outline(section['pt_at_crv_ref'],
                                                                                      section['pt_at_crv_opp_ref'],
                                                                                      section['cnl_opp_ref_major_outline'][:]):
                model3d.plot_points_detail(section['cnl_opp_ref_major_outline'], colors.canal_outline_pre)

    # 필터링한 근관의 외곽선만 표시
    elif cfg.canal_outlines:
        # pre major 근관을  표시
        label = '' if not (cfg.legend and cfg.legend_width) else 'Canal area, width: %.2fmm^2, %.2fmm' % (
            section['area_cnl_ref'], section['cnl_ref_narrow'][CONST.CD_WIDTH])
        model3d.plot_points_detail(section['cnl_ref_major_outline'], colors.pre_canal_outline, label=label)

        # 평면(section plane)에 상태측 curve의 교점이 있다면
        if section['pt_at_crv_opp_ref']:
            if section['cnl_opp_ref_major_outline'] and not du.is_line_inside_outline(section['pt_at_crv_ref'],
                                                                                      section['pt_at_crv_opp_ref'],
                                                                                      section['cnl_opp_ref_major_outline'][:]):
                model3d.plot_points_detail(section['cnl_opp_ref_major_outline'], colors.canal_outline_pre)


def draw_post_canal_outlines(model3d, cfg, colors, section, magnification_ratio):
    if cfg.canal_outlines and section['pt_at_crvs_cmp']:
        # post major 근관을  표시
        cnls_cmp_major_outline = section['cnls_cmp_major_outline']
        for i, k in enumerate(cnls_cmp_major_outline):
            model3d.plot_points_detail(cnls_cmp_major_outline[k],
                                       colors.canal_outline_post[i % len(colors.canal_outline_post)])


# def draw_ransac_ellipse(sd):
#     # major_axis_tangent_vector
#     data = (get_rotated_points(sd.pt_at_crv_ref, sd.major_axis_t_vector, sd.cnl_pst_major_outline)[:, :2]).astype(
#         np.float32)  # data type should be float32 or int32
#     '''
#     min_samples : 14개 이상, 적으면 minor한 부분으로 inliner를 설정함
#     threshold : 0.2 이상
#     '''
#     model, inliers = ransac(data, EllipseFit(), min_samples=14, threshold=.03, max_trials=500)
#     ellipse = cv2.fitEllipse(data)
#
#     from pylab import figure
#     from matplotlib.patches import Ellipse
#
#     e = Ellipse(ellipse[0], width=ellipse[1][0], height=ellipse[1][1], angle=ellipse[-1])
#     e_ransac = Ellipse(model[0], width=model[1][0], height=model[1][1], angle=model[-1])
#
#     #: plot working
#     import pylab
#
#     fig = figure()
#     ax = fig.add_subplot(111, aspect='equal')
#     ax.plot(data[:, 0], data[:, 1], '.r', label='outliers')
#     ax.plot(ellipse[0], ellipse[1], '.r')
#     ax.plot(data[inliers][:, 0], data[inliers][:, 1], '.b', label='inliers')
#
#     ax.add_artist(e)
#     e.set_alpha(0.2)
#     e.set_color('r')
#     ax.add_artist(e_ransac)
#     e_ransac.set_alpha(0.2)
#
#     pylab.gca().invert_yaxis()
#     pylab.legend(loc=4)
#     pylab.show()


def draw_mindist_iod_line(model3d, cfg, colors, section, magnification_ratio):

    # pre-canal 과 root body 사이의 최단거리를 연결한 선을 그림

    # DentinThickness(p_body, p_canal, thickness, angle)
    points = [section['mindist_ref'][CONST.DT_P_CANAL], section['mindist_ref'][CONST.DT_P_BODY]]
    label = '' if not cfg.legend else f"Thinnest(Pre-): {section['mindist_ref'][CONST.DT_THICKNESS] / magnification_ratio:.3f}mm, {section['mindist_ref'][CONST.DT_ANGLE]:.0f}`"
    model3d.plot_points_detail(points, color_style=colors.mindist_line_pre, label=label)

    for i, iod_key in enumerate(section['mindists_iod']):
        dist_info = section['mindists_iod'][iod_key]
        points = [dist_info[CONST.DT_P_CANAL], dist_info[CONST.DT_P_BODY]]
        label = '' if not cfg.legend else f'IOD.{iod_key}: {dist_info[CONST.DT_THICKNESS] / magnification_ratio:.3f}mm, {dist_info[CONST.DT_ANGLE]:.0f}'
        model3d.plot_points_detail(points, color_style=colors.mindist_line_post[i], label=label)


def draw_mindist_lines(model3d, cfg, colors, section, magnification_ratio=1):
    # pre-canal 과 root body 사이의 최단거리를 연결한 선을 그림

    # DentinThickness(p_body, p_canal, thickness, angle)
    points = [section['mindist_ref'][CONST.DT_P_CANAL], section['mindist_ref'][CONST.DT_P_BODY]]
    label = '' if not cfg.legend else 'Thinnest(Pre-): %.3fmm, %.0f`' % (
        section['mindist_ref'][CONST.DT_THICKNESS] / magnification_ratio, section['mindist_ref'][CONST.DT_ANGLE])
    model3d.plot_points_detail(points, color_style=colors.mindist_line_pre, label=label)

    for i, cmp_key in enumerate(section['mindists_cmp']):
        mindist_cmp = section['mindists_cmp'][cmp_key]
        points = [mindist_cmp[CONST.DT_P_CANAL], mindist_cmp[CONST.DT_P_BODY]]
        label = '' if not cfg.legend else f'Thinnest.{cmp_key}: {mindist_cmp[CONST.DT_THICKNESS] / magnification_ratio:.3f}mm, {mindist_cmp[CONST.DT_ANGLE]:.0f}'
        model3d.plot_points_detail(points, color_style=colors.mindist_line_post[i], label=label)


def draw_mesial_line(model3d, cfg, colors, section, magnification_ratio):
    points = [section['mesial_ref'][CONST.DT_P_CANAL], section['mesial_ref'][CONST.DT_P_BODY]]
    label = '' if not cfg.legend else f"Mesial(Pre-): {section['mesial_ref'][CONST.DT_THICKNESS] / magnification_ratio:.2f}mm"
    model3d.plot_points_detail(points, color_style=colors.mesial_line, label=label)


def draw_distal_line(model3d, cfg, colors, section, magnification_ratio):
    points = [section['distal_ref'][CONST.DT_P_CANAL], section['distal_ref'][CONST.DT_P_BODY]]
    label = '' if not cfg.legend else f"Distal(Pre-): {section['distal_ref'][CONST.DT_THICKNESS] / magnification_ratio:.2f}mm"
    model3d.plot_points_detail(points, color_style=colors.distal_line, label=label)


def draw_lateral_line(model3d, cfg, colors, section, magnification_ratio):
    points = [section['lateral_ref'][CONST.DT_P_CANAL], section['lateral_ref'][CONST.DT_P_BODY]]
    label = '' if not cfg.legend else f"Lateral(Pre-): {section['lateral_ref'][CONST.DT_THICKNESS] / magnification_ratio:.2f}mm"
    model3d.plot_points_detail(points, color_style=colors.lateral_line, label=label)


def draw_mesial_concavity(model3d, cfg, colors, section, magnification_ratio):
    concavity = section['mesial_concavity']
    if concavity:
        label = '' if not cfg.legend else f'Mesial concavity: {concavity[CONST.CV_DIST] / magnification_ratio:.2f}mm'
        model3d.plot_points_detail([concavity[CONST.CV_P_11], concavity[CONST.CV_P_12]], color_style=colors.mesial_concavity, label=label)
        model3d.plot_points_detail([concavity[CONST.CV_P_21], concavity[CONST.CV_P_22]], color_style=colors.mesial_concavity)


def draw_distal_concavity(model3d, cfg, colors, section, magnification_ratio):
    concavity = section['distal_concavity']
    if concavity:
        label = '' if not cfg.legend else f'Distal concavity: {concavity[CONST.CV_DIST] / magnification_ratio:.2f}mm'
        model3d.plot_points_detail([concavity[CONST.CV_P_11], concavity[CONST.CV_P_12]], color_style=colors.distal_concavity, label=label)
        model3d.plot_points_detail([concavity[CONST.CV_P_21], concavity[CONST.CV_P_22]], color_style=colors.distal_concavity)


def draw_mindist_pre_cwt_line(cfg, section, model3d, mindist_pre_line_style, def_label='cwt-line-Thinnest(Pre-)'):
    for k in section['mindists_cmp']:
        model3d.plot_points([section['pt_cnl_ref_cwt'], section['mindists_cmp'][k][CONST.DT_P_BODY]], mindist_pre_line_style,
                            label='' if not cfg.legend else def_label + ': %.2fmm' %
                                                            ((vector(section['mindists_cmp'][k][CONST.DT_P_BODY]) - vector(
                                                               section['pt_cnl_ref_cwt'])).length()))


def draw_mindist_post_label(cfg, section, model3d, mindist_post_arrow_color, def_label='Thinnest(Post-)'):
    for k, mindist in section['mindists_cmp'].iteritems():
        model3d.plot_points([[0, 0, 0], [0, 0, 0]], mindist_post_arrow_color,
                            label='' if not cfg.legend
                            else def_label + ': %.2fmm, %.0f`' % (mindist[CONST.DT_THICKNESS], mindist[CONST.DT_ANGLE]))


def draw_mindist_post_arrow(section, model3d, mindist_post_arrow_color, mindist_post_arrow_linestyle):
    for k, mindist in section['mindists_cmp'].iteritems():
        model3d.plot_arrow(mindist[CONST.DT_P_BODY], mindist[CONST.DT_P_CANAL],
                           color=mindist_post_arrow_color, ls=mindist_post_arrow_linestyle)


def draw_cwt_label(cfg, section, model3d, def_label='CWT'):
    return model3d.plot_points([[0, 0, 0], [0, 0, 0]], 'w',
                               label='' if not cfg.legend else def_label + ': %.3f' % (section.cwt_ratio))


def draw_mindist_post_and_cwt(cfg, section, model3d, mindist_post_arrow_color,
                              mindist_post_arrow_linestyle, def_label):
    # mindist post label
    draw_mindist_post_label(cfg, section, model3d, mindist_post_arrow_color, def_label)

    # mindist post arrow
    draw_mindist_post_arrow(section, model3d, mindist_post_arrow_color, mindist_post_arrow_linestyle)

    # CWT label
    # draw_cwt_label(pr, sd, chart3d)


def draw_mindist_pre_post_and_cwt(cfg, section, model3d, mindist_pre_line_style, mindist_post_arrow_color,
                                  mindist_post_arrow_linestyle):
    # mindist pre line and label
    draw_mindist_pre_cwt_line(cfg, section, model3d, mindist_pre_line_style)

    # mindist post label
    draw_mindist_post_label(cfg, section, model3d, mindist_post_arrow_color)

    # mindist post arrow
    draw_mindist_post_arrow(section, model3d, mindist_post_arrow_color, mindist_post_arrow_linestyle)

    # CWT label
    # draw_cwt_label(pr, sd, chart3d)


def draw_misc(cfg, section, model3d, draw_min_diameter_of_canal, draw_tangential_line, draw_plane):
    if draw_min_diameter_of_canal:
        # Min canal diameter 표시(pre)
        model3d.plot_points([section.pts_cnl_pre_dimension[0], section.pts_cnl_pre_dimension[1]], 'r:')
        # Min canal diameter 표시(post)
        if section.pt_at_crvs_cmp:
            model3d.plot_points([section.pts_cnl_pst_dimension[0], section.pts_cnl_pst_dimension[1]], 'g:')

    ################################
    # draw tangent line ==> arrow to apex
    if draw_tangential_line:
        n1 = section.t_vector_at_pre_crv / section.t_vector_at_pre_crv.length()  # normal
        if section.pt_at_crv_opp_ref:
            q1, q2 = section.pt_at_crv_opp_ref - n1 * 1, section.pt_at_crv_opp_ref
            model3d.plot_arrow(q1, q2, color="r", ls='solid')

    ################################
    # draw perpendicular plane to pre_curve at point_at_pre_curve
    if draw_plane:
        (a, b, c), (x0, y0, z0), (xl, yl, _) = section.t_vector_at_pre_crv, section.pt_at_crv_ref, cfg.specimen.bounding_box
        X, Y = np.arange(xl[0] + 1, xl[1], 1), np.arange(yl[0] + 1, yl[1], 1)
        X, Y = np.meshgrid(X, Y)
        Z = (-a * (X - x0) - b * (Y - y0)) / c + z0
        model3d.plot_surface(X, Y, Z)


def draw_canals_and_CH_axes(model3d, cfg, colors, header):
    # draw curve
    '''
    :param cfg: param for chart config
    :param header:
    :param model3d:
    :return:
    '''

    curve_name_printed = False
    if cfg.curve_axis:
        curve_name_printed = draw_pre_and_post_canal_axis(model3d, cfg, colors, header)

    # global curvature axis
    if cfg.curve_height_axis:
        model3d.plot_points_detail([header['coronal_end_of_CH'], header['apical_end_of_CH']],
                                   colors.curve_height_axis_line)

    return curve_name_printed


def model3d_drawer(cfg, model_data, axes_visible=True):
    '''
    :param cfg: param for chart configuration
    :param model_data: json formatted specimen data, all points and length info
    :return: null
    '''

    # prepare chart
    import model3d
    from class_parameter import ModelColorParameters
    import math

    colors = ModelColorParameters()
    config_chart_colors(colors)

    model_header = model_data['model']
    magnification_ratio = 1 if 'magnification_ratio' not in model_header else model_header[
        'magnification_ratio']

    model3d.init(model_header['bounding_box'])
    model3d.magnification_ratio = magnification_ratio

    # print(f' -- magnification ratio : {magnification_ratio}')
    curve_name_printed = draw_canals_and_CH_axes(model3d, cfg, colors, model_header)

    for section in model_data['sections']:

        if any(math.isclose(x, section['section'] / magnification_ratio, rel_tol=1e-3) for x in cfg.sections):
            if cfg.crossing_points:
                draw_crossing_point_of_canal_axes(model3d, cfg, colors, model_header, section)

            if cfg.centroids and 'pt_cnl_ref_centroid' in section:
                draw_canal_centroids(model3d, colors, section)

            if cfg.root_outlines:
                draw_root_outlines(model3d, cfg, colors, model_header, section, curve_name_printed, magnification_ratio)

            if cfg.curve_height and section['cnl_straightening']:
                draw_curve_height_arrow(model3d, cfg, colors, section, magnification_ratio)

            if cfg.all_canal_outlines or cfg.canal_outlines:
                draw_pre_canal_outlines(model3d, cfg, colors, section, magnification_ratio)
                draw_post_canal_outlines(model3d, cfg, colors, section, magnification_ratio)

            if cfg.mindist_pre:
                draw_mindist_lines(model3d, cfg, colors, section, magnification_ratio)

            if cfg.mindist_iod:
                draw_mindist_iod_line(model3d, cfg, colors, section, magnification_ratio)

            if cfg.orthogonal_line:
                draw_mesial_line(model3d, cfg, colors, section, magnification_ratio)
                draw_distal_line(model3d, cfg, colors, section, magnification_ratio)
                draw_lateral_line(model3d, cfg, colors, section, magnification_ratio)

            if cfg.concavity:
                draw_mesial_concavity(model3d, cfg, colors, section, magnification_ratio)
                draw_distal_concavity(model3d, cfg, colors, section, magnification_ratio)


            if cfg.mindist_post and section['pt_at_crvs_cmp']:
                # ======================================
                mindist_pre_line_color_style = ['green', '-']
                mindist_post_arrow_color = 'r'
                mindist_post_arrow_linestyle = 'solid'
                # ======================================

                # draw_mindist_pre_post_and_cwt(params, section, model3d,
                #                               mindist_pre_line_color_style,
                #                               mindist_post_arrow_color, mindist_post_arrow_linestyle)

        '''
        # ======================================
        draw_min_diameter_of_canal = False
        draw_tangential_line = False
        draw_plane = False
        # ======================================
        draw_misc(param, sd, chart3d, draw_min_diameter_of_canal, draw_tangential_line, draw_plane)
            if param.ransac_ellipse:
                draw_ransac_ellipse(section)
            '''

    if len(cfg.artificial_circles) > 0:
        for circle in cfg.artificial_circles:
            model3d.plot_points_detail(circle['points'], ['#aa0000', '-', 3], label=circle['description'])

    if len(cfg.centroids_onsite) > 0:
        model3d.plot_marker(cfg.centroids_onsite, ['magenta', 'o', 3])

    # show chart
    # print(" Finish drawing! ")
    # chart3d.show()
    return model3d.model3d_drawer_fig(axes_visible)


def config_chart_colors(colors):
    # ======================================
    #    ‘b’    blue       ‘g’    green     ‘r’    red    ‘c’    cyan
    #    ‘m’    magenta    ‘y’    yellow    ‘k’    black  ‘w’    white
    #    linestyle : ['-' | '--' | '-.' | ':' | 'None' | ' ' | '']
    # ======================================
    pre = 'indigo'
    post = ['dodgerblue', 'hotpink', 'teal', 'blue']
    dash =['-'] * len(post)

    colors.canal_axis_pre = [pre, '-', 2]  # [color, style, line width]
    colors.canal_axis_opp = [pre, ':']
    colors.canal_axis_post = list(zip(post, dash))

    colors.curve_height_axis_line = ['#0000ff', '-']

    colors.crossing_point_pre = [pre, 'o', 2]  # [color, style, marker size]
    colors.crossing_point_post = list(zip(post, ['o']*len(post), [2]*len(post)))

    colors.canal_centroid_pre = [pre, '*', 2.5]  # [color, style, marker size]
    colors.canal_centroid_post = list(zip(post, ['*']*len(post), [2.5]*len(post)))

    colors.highlighted_body_outline = ['dimgrey', '-']
    colors.normal_body_outline = ['dimgrey', '-']
    colors.ch_arrow = ['#000000', '-']

    colors.canal_outline_pre = [pre, '-']
    colors.canal_outline_post = list(zip(post, dash))

    colors.mindist_line_pre = [pre, '-']
    colors.mindist_line_post = list(zip(post, dash))
    colors.mesial_line = ['#409d26', '-']
    colors.distal_line = ['#004eeb', '-']
    colors.lateral_line = ['#989800', '-']

    colors.mesial_concavity = ['#409d26', ':']
    colors.distal_concavity = ['#004eeb', ':']


def config_chart_parameters(cfg):
    # chart_param.specimens = select_specimens(data_set.roots, ['BLX02', 'PTU01', 'RCP01'])
    cfg.sections = [5,
                    1]  # [x / 10.0 for x in range(0, 135  , 1)] #[x / 10.0 for x in range(0, 85, 1) ] # if x < 30 or x > 70 or x == 50 or x == 45]
    cfg.legend = True
    cfg.legend_width = False  # display canal width and area info
    cfg.root_outlines = True
    cfg.canal_outlines = True
    cfg.all_canal_outlines = False  # for debugging of images
    cfg.curve_axis = True
    cfg.curve_height = True
    cfg.curve_height_axis = True
    cfg.crossing_points = True
    cfg.transportation_arrow = False
    cfg.mindist_pre = True
    cfg.orthogonal_line = True
    cfg.mindist_post = False
    cfg.highlight_section_list = None  # [11.1] #None


if __name__ == '__main__':
    import json
    from class_parameter import DrawOptionParameters

    # data file to draw chart
    data_file = '../working/gus18/gus18.both.all-0.1mm.json'
    with open(data_file) as data_file:
        data = json.load(data_file)
        chart_param = DrawOptionParameters()
        config_chart_parameters(chart_param)

        cur_data = data['G18.MN011.M-B']

        model3d_drawer(chart_param, data['G18.MN011.M-B'])
