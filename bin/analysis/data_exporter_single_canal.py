# -*- coding: cp949 -*-

from __future__ import division
from collections import OrderedDict
import win32com.client as win32  # Excel export
from functools import reduce

import dist_util as du  # collection of utility function
import excel_helper
from constant import CONST
from geom import vector


def draw_chart(sheet, num_rows):
    CONST = win32.constants
    CH_LINE_THICKNESS = 1.27
    CHART_WIDTH, CHART_HEIGHT = 450, 250
    CHART_START_COL, CHART_START_ROW = 1800, 40
    rows = num_rows + 2

    ###########################
    # Curvature & Torsion chart
    ch1 = sheet.ChartObjects().Add(CHART_START_COL, CHART_START_ROW, CHART_WIDTH, CHART_HEIGHT).Chart
    ch1.ChartType = CONST.xlXYScatterSmoothNoMarkers

    ranges = 'D2:D{0}, G2:G{0}, I2:I{0}, K2:K{0}'.format(rows)
    ch1.SetSourceData(sheet.Range(ranges), CONST.xlColumns)
    s_gc_pre, s_lc_pre, s_lt_pre = ch1.SeriesCollection()

    s_lt_pre.AxisGroup = CONST.xlSecondary
    s_gc_pre.Format.Line.Weight = CH_LINE_THICKNESS
    s_lc_pre.Format.Line.Weight = CH_LINE_THICKNESS
    s_lt_pre.Format.Line.Weight = CH_LINE_THICKNESS
    s_gc_pre.Format.Line.ForeColor.RGB = excel_helper.rgb_to_hex((23, 173, 166))
    s_lc_pre.Format.Line.ForeColor.RGB = excel_helper.rgb_to_hex((152, 24, 146))
    s_lt_pre.Format.Line.ForeColor.RGB = excel_helper.rgb_to_hex((178, 18, 18))

    ch1.ApplyLayout(4)
    ch1.Axes(CONST.xlValue, CONST.xlSecondary).MinimumScale = -20
    ch1.Axes(CONST.xlValue, CONST.xlSecondary).MaximumScale = 20
    ch1.Axes(CONST.xlValue, CONST.xlSecondary).MajorUnit = 5
    ch1.Axes(CONST.xlValue).MinimumScale = -2
    ch1.Axes(CONST.xlValue).MaximumScale = 2
    ch1.Axes(CONST.xlValue).TickLabels.NumberFormatLocal = "#,##0.0_ "
    ch1.Axes(CONST.xlValue).HasMajorGridlines = True

    ###########################
    # Dentin thickness chart
    ch2 = sheet.ChartObjects().Add(CHART_START_COL, CHART_START_ROW + CHART_HEIGHT * 1 + 10, CHART_WIDTH,
                                   CHART_HEIGHT).Chart
    ch2.ChartType = CONST.xlXYScatterSmoothNoMarkers

    #         x-axis,  s_min,   s_mesial,  s_distal,  s_lateral, s_canal
    ranges = 'D2:D{0}, P2:P{0}, AC2:AC{0}, AD2:AD{0}, AE2:AE{0}, T2:T{0}'.format(rows)

    ch2.SetSourceData(sheet.Range(ranges), CONST.xlColumns)
    s_min, s_mesial, s_distal, s_lateral, s_canal = ch2.SeriesCollection()

    ch2.ApplyLayout(4)
    ch2.Axes(CONST.xlValue).MinimumScale = 0
    ch2.Axes(CONST.xlValue).MaximumScale = 4
    ch2.Axes(CONST.xlValue).TickLabels.NumberFormatLocal = "#,##0.0_ "
    ch2.Axes(CONST.xlValue).HasMajorGridlines = True

    s_min.Format.Line.Weight = CH_LINE_THICKNESS + 0.3
    s_mesial.Format.Line.Weight = CH_LINE_THICKNESS
    s_distal.Format.Line.Weight = CH_LINE_THICKNESS
    s_lateral.Format.Line.Weight = CH_LINE_THICKNESS
    s_canal.Format.Line.Weight = CH_LINE_THICKNESS

    s_min.Format.Line.ForeColor.RGB = excel_helper.rgb_to_hex((0, 0, 0))
    s_mesial.Format.Line.ForeColor.RGB = excel_helper.rgb_to_hex((106, 175, 5))
    s_distal.Format.Line.ForeColor.RGB = excel_helper.rgb_to_hex((152, 24, 146))
    s_lateral.Format.Line.ForeColor.RGB = excel_helper.rgb_to_hex((23, 173, 166))
    s_canal.Format.Line.ForeColor.RGB = excel_helper.rgb_to_hex((255, 13, 13))

    ###########################
    # Direction chart
    ch3 = sheet.ChartObjects().Add(CHART_START_COL, CHART_START_ROW + CHART_HEIGHT * 2 + 10 * 2, CHART_WIDTH,
                                   CHART_HEIGHT).Chart
    ch3.ChartType = CONST.xlXYScatterSmoothNoMarkers


    #         x-axis,  s_angle_min, s_angle_gc
    ranges = 'D2:D{0}, Y2:Y{0}, V2:V{0}'.format(rows)
    ch3.SetSourceData(sheet.Range(ranges), CONST.xlColumns)

    s_angle_min, s_angle_gc = ch3.SeriesCollection()

    ch3.ApplyLayout(4)
    ch3.Axes(CONST.xlValue).MinimumScale = 0
    ch3.Axes(CONST.xlValue).MaximumScale = 360
    ch3.Axes(CONST.xlValue).MajorUnit = 90

    ch3.Axes(CONST.xlValue).TickLabels.NumberFormatLocal = "#,##0.0_ "
    ch3.Axes(CONST.xlValue).HasMajorGridlines = True

    s_angle_min.Format.Line.Weight = CH_LINE_THICKNESS
    s_angle_gc.Format.Line.Weight = CH_LINE_THICKNESS

    s_angle_min.Format.Line.ForeColor.RGB = excel_helper.rgb_to_hex((178, 18, 18))
    s_angle_gc.Format.Line.ForeColor.RGB = excel_helper.rgb_to_hex((246, 88, 107))

    '''
    s_angle.ChartType = CONST.xlXYScatter
    s_angle.ForeColor.ObjectThemeColor = 
    s_angle.LineFormat.DashStyle = CONST.msoLineSysDash
    s_angle.MarkerStyle = 8
    s_angle.MarkerSize = 1
    '''


def summary_table(sheet, curve_len, interval):
    DATA_START_ROW = 3
    BASE_ROW, BASE_COL = 40, 17
    num_rows = int(curve_len / interval)
    num_sets = 1 / interval

    row_data = 'GC max from coronal,,GC precentile,,GC max value'
    excel_helper.fill_a_row_to_sheet(sheet, row_data, 1, 8)
    # expression for GC max from coronal
    row_data = '=B%d - CELL("contents",INDEX(B%d:B%d,MATCH(MAX(C%d:C%d),C%d:C%d,0)))' % (
    DATA_START_ROW + num_rows, DATA_START_ROW, DATA_START_ROW + num_rows, DATA_START_ROW, DATA_START_ROW + num_rows,
    DATA_START_ROW, DATA_START_ROW + num_rows)
    excel_helper.fill_a_cell_to_sheet(sheet, row_data, 1, 9)

    # expression for GC percentile
    row_data = '=I1/B%d * 100' % (DATA_START_ROW + num_rows)
    excel_helper.fill_a_row_to_sheet(sheet, row_data, 1, 11)

    row_data = '=MAX(C%d:C%d)' % (DATA_START_ROW, DATA_START_ROW + num_rows)
    excel_helper.fill_a_row_to_sheet(sheet, row_data, 1, 13)

    row_data = ',Min. dist.,Mesial,Distal,Lateral, Min. dia. canal'
    excel_helper.fill_a_row_to_sheet(sheet, row_data, BASE_ROW, BASE_COL);
    BASE_ROW += 1
    for i in range(int(num_rows / num_sets) + 1):
        row_data = '%.1f,' % ((i * 2 + 1) / 2.0)
        row_data += '=AVERAGE(F%d:F%d),' % (
        int(i * num_sets + DATA_START_ROW), int((i + 1) * num_sets + DATA_START_ROW - 1))
        row_data += '=AVERAGE(G%d:G%d),' % (
        int(i * num_sets + DATA_START_ROW), int((i + 1) * num_sets + DATA_START_ROW - 1))
        row_data += '=AVERAGE(H%d:H%d),' % (
        int(i * num_sets + DATA_START_ROW), int((i + 1) * num_sets + DATA_START_ROW - 1))
        row_data += '=AVERAGE(I%d:I%d),' % (
        int(i * num_sets + DATA_START_ROW), int((i + 1) * num_sets + DATA_START_ROW - 1))
        row_data += '=AVERAGE(J%d:J%d)' % (
        int(i * num_sets + DATA_START_ROW), int((i + 1) * num_sets + DATA_START_ROW - 1))

        excel_helper.fill_a_row_to_sheet(sheet, row_data, BASE_ROW, BASE_COL);
        BASE_ROW += 1


def get_rows(model_data, pst=None):
    echo = False

    md = model_data['model']
    section_data = model_data['sections']

    column_dict = get_column_dict()
    furcation_pos = None if not 'furcation_pos' in md else md['furcation_pos']
    orifice_pos = section_data[-1]['section']

    rows = []

    for sd in section_data:

        exception = ''
        if not sd['bdy_major_outline_exist']: exception += 'BODY '
        if not sd['cnl_ref_major_outline_exist']: exception += 'CANAL-PRE '
        if pst and not sd['cnls_cmp_major_outline_exist'][pst]:  exception += 'CANAL-POST '
        if sd['median_major_axis_used']:  exception += 'STD-AXIS '
        pst_exist = False if not pst else sd['pt_at_crvs_cmp'][pst]

        column_dict['RootName'] = md['name']
        column_dict['CanalSide'] = md['crv_name'].split('-')[-1]
        column_dict['WeineClassification'] = '' if not 'weine_classification' in md else str(md['weine_classification'])

        column_dict['LengthFromApex'] = '{:.2f}'.format(sd['section'])
        column_dict['LengthFromOrifice'] = '{:.2f}'.format(orifice_pos - sd['section'])
        if furcation_pos:
            pos = furcation_pos - sd['section']
            column_dict['LengthFromFurcation'] = '' if pos < 0 else str(pos)
        else:
            column_dict['LengthFromFurcation'] = ''

        column_dict['GCPre'] = '{:.3f}'.format(sd['CH_ref'])
        column_dict['GCPost'] = '' if not pst_exist else '{:.3f}'.format(sd['CHs_cmp'][pst])

        column_dict['CurvaturePre'] = '{:.3f}'.format(sd['curvature_ref'])
        column_dict['CurvaturePost'] = '' if not pst_exist else '{:.3f}'.format(sd['curvatures_cmp'][pst])

        column_dict['TorsionPre'] = '{:.3f}'.format(sd['torsion_ref'])
        column_dict['TorsionPost'] = '' if not pst_exist else '{:.3f}'.format(sd['torsions_cmp'][pst])
        column_dict['MesialConcavity'] = '' if not sd['mesial_concavity'] else '{:.2f}'.format(sd['mesial_concavity'][CONST.CV_DIST])
        column_dict['DistalConcavity'] = '' if not sd['distal_concavity'] else '{:.2f}'.format(sd['distal_concavity'][CONST.CV_DIST])

        # FileMovement(vector angle distance)
        column_dict['Transportation'] = '' if not pst_exist else '{:.3f}'.format(sd['cnls_transportation'][pst][CONST.FM_DISTANCE])

        # MinDistPre 가 좀 이상, pst 가 필요?
        # DentinThickness(p_body, p_canal, thickness, angle)
        column_dict['MinDistPre'] = '{:.3f}'.format(sd['mindist_ref'][CONST.DT_THICKNESS])
        column_dict['MinDistPost'] = '' if not pst_exist else '{:.3f}'.format(sd['mindists_cmp'][pst][CONST.DT_THICKNESS])

        column_dict['AreaPre'] = '{:.3f}'.format(sd['area_cnl_ref'])  # poly_area(vs_canal_pre_major)
        column_dict['AreaPost'] = '' if not pst_exist else '{:.3f}'.format(sd['area_cnls_cmp'][pst])  # poly_area(vs_canal_post_major)

        # CanalDimension(p1, p2, width)
        column_dict['CanalWidthPre'] = '{:.3f}'.format(sd['cnl_ref_narrow'][CONST.CD_WIDTH])
        column_dict['CanalWidthPost'] = '' if not pst_exist else '{:.3f}'.format(sd['cnls_cmp_narrow'][pst][CONST.CD_WIDTH])

        # FileMovement(vector angle distance)
        column_dict['GCAnglePre'] = '' if not sd['cnl_straightening'][CONST.FM_ANGLE] else '{:.1f}'.format(sd['cnl_straightening'][CONST.FM_ANGLE])
        column_dict['GCAnglePost'] = '' if not pst_exist or not sd['cnls_straightened'][pst][CONST.FM_ANGLE] else '{:.1f}'.format(sd['cnls_straightened'][pst][CONST.FM_ANGLE])
        column_dict['TranspAngle'] = '' if not pst_exist else '{:.1f}'.format(sd['cnls_transportation'][pst][CONST.FM_ANGLE])

        # DentinThickness(p_body, p_canal, thickness, angle)
        DT_ANGLE = 3
        column_dict['MinDistAnglePre'] = '{:.1f}'.format(sd['mindist_ref'][CONST.DT_ANGLE])
        column_dict['MinDistAnglePost'] = '' if not pst_exist else '{:.1f}'.format(sd['mindists_cmp'][pst][CONST.DT_ANGLE])
        column_dict['IOD'] = '' if not pst_exist else '{:.3f}'.format(sd['cwt_ratios'][pst])
        column_dict['Exception'] = exception

        column_dict['MesialPre'] = '{:.3f}'.format(sd['mesial_ref'][CONST.DT_THICKNESS])
        column_dict['DistalPre'] = '{:.3f}'.format(sd['distal_ref'][CONST.DT_THICKNESS])
        column_dict['LateralPre'] = '{:.3f}'.format(sd['lateral_ref'][CONST.DT_THICKNESS])
        column_dict['CounterLateralPre'] = '{:.3f}'.format(sd['counter_lateral_ref'][CONST.DT_THICKNESS])

        current_row = reduce(lambda x, y: x + ',' + y, column_dict.values())
        rows.append(current_row)
        if echo: print(current_row)

    return rows


def get_tooth_info(md):
    tooth_info = ',' if md['crv_name'] is None else md['crv_name'] + ', length: %.2f' % md['crv_ref_length']
    tooth_info += ',,CURVE,%2f,FURCATION,%2f' % (md['length'], md['furcation_pos'])
    tooth_info += ',straight length from apex to orifice,%2f' % (vector(md['apical_end_of_CH']).distance(vector(md['coronal_end_of_CH'])))
    # tooth_info += '' if md.specimen.note is None else ',,, NOTE: ' + md.specimen.note
    return tooth_info


def get_column_element():
    column_element = ['RootName', 'CanalSide', 'WeineClassification', 'LengthFromApex', 'LengthFromOrifice',
                      'LengthFromFurcation', 'GCPre', 'GCPost', 'CurvaturePre',
                      'CurvaturePost', 'TorsionPre', 'TorsionPost', 'MesialConcavity', 'DistalConcavity',
                      'Transportation','MinDistPre', 'MinDistPost', 'AreaPre', 'AreaPost', 'CanalWidthPre',
                      'CanalWidthPost','GCAnglePre', 'GCAnglePost', 'TranspAngle', 'MinDistAnglePre', 'MinDistAnglePost',
                      'IOD', 'Exception', 'MesialPre', 'DistalPre', 'LateralPre', 'CounterLateralPre']
    return column_element


def get_column_dict():
    return OrderedDict(zip(get_column_element(), ['' for _ in range(len(get_column_element()))]))


def get_column_header():
    return ','.join(get_column_dict().keys())


def export_overall_stat(model_data, pst=None, excel_workbook=None):

    echo = False

    md = model_data['model']
    section_data = model_data['sections']

    tooth_info = get_tooth_info(md)
    column_header = get_column_header()
    rows = get_rows(model_data, pst)

    if echo:
        print (tooth_info)
        print (column_header)

    # Add sheet & change sheet name
    if excel_workbook:
        worksheet = excel_workbook.Sheets.Add()
        if md['crv_name']:
            worksheet.Name = md['crv_name']
        # Fill column header
        excel_helper.fill_a_row_to_sheet(worksheet, tooth_info, 1)
        excel_helper.fill_a_row_to_sheet(worksheet, column_header, 2)
        cur_row_of_sheet = 3

        for r in rows:
            excel_helper.fill_a_row_to_sheet(worksheet, r, cur_row_of_sheet)
            cur_row_of_sheet += 1

        draw_chart(worksheet, len(section_data))


def export_overall_stat_to_excel(data_directory):
    import json
    import os
    import win32com.client as win32  # Excel export

    xl = win32.gencache.EnsureDispatch('Excel.Application')
    xl.Visible = True
    wb = xl.Workbooks.Add()

    for (path, dir, files) in os.walk(data_directory):
        for filename in files:
            with open(path + '/' + filename) as data_file:
                print('  Exporting [{}] ...'.format(filename))
                data = json.load(data_file)
                export_overall_stat(data, excel_workbook=wb)


def export_overall_stat_to_single_sheet(data_directory):
    import json
    import os
    import win32com.client as win32  # Excel export

    xl = win32.gencache.EnsureDispatch('Excel.Application')
    xl.Visible = True
    wb = xl.Workbooks.Add()
    worksheet = wb.Sheets.Add()
    worksheet.Name = 'all data'
    excel_helper.fill_a_row_to_sheet(worksheet, get_column_header(), 1)
    cur_row_of_sheet = 2

    for (path, dir, files) in os.walk(data_directory):
        for filename in files:
            with open(path + '/' + filename) as data_file:
                model_data = json.load(data_file)
                rows = get_rows(model_data)
                print('  Exporting [{}] ...'.format(filename))

                for r in rows:
                    excel_helper.fill_a_row_to_sheet(worksheet, r, cur_row_of_sheet)
                    cur_row_of_sheet += 1

def main():
    import json
    import os

    import win32com.client as win32  # Excel export

    import data_exporter_single_canal as da

    xl = win32.gencache.EnsureDispatch('Excel.Application')
    xl.Visible = True
    wb = xl.Workbooks.Add()

    for (path, dir, files) in os.walk(os.getcwd()+'/output'):
        for filename in files:
            with open(path+'/'+filename) as data_file:
                data = json.load(data_file)
                da.export_overall_stat(data, excel_workbook=wb)
                print('{0} has processed'.format(filename))


def main2():

    import json
    import win32com.client as win32  # Excel export

    data_file = '../working/ljkcs.both.all-0.1mm.json'
    xl = win32.gencache.EnsureDispatch('Excel.Application')
    xl.Visible = True
    wb = xl.Workbooks.Add()

    with open(data_file) as data_file:
        data = json.load(data_file)
        for k, model in data.items():
            # print k, model
            export_overall_stat(model, pst='blx', excel_workbook=wb)

if __name__ == '__main__':
    main()
