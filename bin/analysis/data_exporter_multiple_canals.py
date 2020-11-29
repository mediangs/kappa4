# -*- coding: cp949 -*-

from __future__ import division
from functools import reduce
import win32com.client as win32  # Excel export
import json
import os

import excel_helper
from datatable_from_modeldata import datatable_from_modeldata
from geom import vector


def get_indices_of_subheadings(headings, subheadings):
    idxs = [i for i, x in enumerate(headings) if x.startswith(subheadings)]
    idxs = sorted(idxs)
    return idxs[0], idxs[-1]


def draw_chart_on_sheet(sheet, num_rows, headings, subheadings):
    x_axis, _ = get_indices_of_subheadings(headings, 'LengthFromApex')
    x_axis = index_to_excel_column_string(x_axis + 1)

    CONST = win32.constants

    CH_LINE_THICKNESS = 1.27
    CHART_START_COL = (len(headings) + 1) * 53
    CHART_WIDTH, CHART_HEIGHT = 450, 180
    CHART_START_ROW = 40
    rows = num_rows + 2

    for i, elem in enumerate(subheadings):
        subheading, min_scale, max_scale = elem
        start, end = get_indices_of_subheadings(headings, subheading)
        start = index_to_excel_column_string(start + 1)
        end = index_to_excel_column_string(end + 1)
        CHART_ROW = CHART_START_ROW + (CHART_HEIGHT+10) * i

        ###########################
        # Curvature & Torsion chart
        chart = sheet.ChartObjects().Add(CHART_START_COL, CHART_ROW, CHART_WIDTH, CHART_HEIGHT).Chart
        chart.ChartType = CONST.xlXYScatterSmoothNoMarkers

        #Titles - NOT WORKING
        chart.HasTitle = True
        chart.ChartTitle.Characters.Text = "Scatter Chart"
        chart.Axes(CONST.xlCategory, CONST.xlPrimary).HasTitle = True
        chart.Axes(CONST.xlCategory, CONST.xlPrimary).AxisTitle.Characters.Text = "X values"
        chart.Axes(CONST.xlValue, CONST.xlPrimary).HasTitle = True
        chart.Axes(CONST.xlValue, CONST.xlPrimary).AxisTitle.Characters.Text = "Y values"
        chart.Axes(CONST.xlCategory).HasMajorGridlines = True

        ranges = f'{x_axis}2:{x_axis}{rows}, {start}2:{end}{rows}'

        chart.SetSourceData(sheet.Range(ranges), CONST.xlColumns)

        chart.ApplyLayout(4)
        chart.Axes(CONST.xlValue).MinimumScale = min_scale
        chart.Axes(CONST.xlValue).MaximumScale = max_scale
        chart.Axes(CONST.xlValue).TickLabels.NumberFormatLocal = "#,##0.0_ "
        chart.Axes(CONST.xlValue).HasMajorGridlines = True


def index_to_excel_column_string(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string


def get_tooth_info(md, short=False):
    ratio = 1 if not 'magnification_ratio' in md.keys() else 1 / md['magnification_ratio']
    tooth_info = ',' if md['crv_name'] is None else md['crv_name'] + ', length: %.2f' % (md['crv_ref_length'] * ratio)
    if not short:
        tooth_info += ',,CURVE,%2f,FURCATION,%2f' % (md['length'], md['furcation_pos'])
        tooth_info += ',straight length from apex to orifice,%2f' % ((vector(md['apical_end_of_CH']).distance(vector(md['coronal_end_of_CH']))) * ratio)
        # tooth_info += '' if md.specimen.note is None else ',,, NOTE: ' + md.specimen.note
    return tooth_info


# def get_column_dict(cmp_canals):
#     column_definition = column_definition(cmp_canals, 1)
#     return OrderedDict(zip(column_definition.names, ['' for _ in range(len(column_definition.names))]))


def model_data_export_to_excel_sheet(model_data, column_definition,
                                     excel_workbook=None, name_converter=None,
                                     charts_on_sheet=None):

    echo = False
    model_header = model_data['model']
    section_data = model_data['sections']
    magnification_ratio = 1 if not 'magnification_ratio' in model_header.keys() else model_header['magnification_ratio']

    #Get name of comparison canals
    cmp_canals = None if not 'pts_of_crvs_cmp' in model_header else model_header['pts_of_crvs_cmp'].keys()

    tooth_info = get_tooth_info(model_header, short=True)
    columns = column_definition(cmp_canals, magnification_ratio)
    column_header = ','.join(columns.names)
    rows = datatable_from_modeldata(model_data, columns)

    if echo:
        print(tooth_info)
        print(column_header)

    # Add sheet & change sheet name
    if excel_workbook:
        worksheet = excel_workbook.Sheets.Add()

        if name_converter:
            name = name_converter(model_header['crv_name'])
        else:
            name = model_header['crv_name']

        worksheet.Name = name
        # Fill column header
        excel_helper.fill_a_row_to_sheet(worksheet, tooth_info, 1)
        excel_helper.fill_a_row_to_sheet(worksheet, column_header, 2)
        cur_row_of_sheet = 3

        for index, row in rows.iterrows():
            r = reduce(lambda x, y: x + ',' + y, row)
            excel_helper.fill_a_row_to_sheet(worksheet, r, cur_row_of_sheet)
            cur_row_of_sheet += 1

        if charts_on_sheet:
            draw_chart_on_sheet(worksheet, len(section_data), columns.names, charts_on_sheet)

        # draw_chart_on_sheet(worksheet, len(section_data), columns.names,
        #                     [['MinDist-', 0, 2], ['MinDistAngle-', 0, 360], ['Concavity-', 0, 2]])

        # draw_chart_on_sheet(worksheet, len(section_data), columns.names,
        #                     [['Transportation', 0, 1], ['MinDist-', 0, 2], ['IOD-', 0, 1],
        #                      ['MinDistAngle-', 0, 360], ['TranspAngle-', 0, 360],
        #                      ['Concavity-', 0, 2]])

        # draw_chart_on_sheet(worksheet, len(section_data), ce,
        #            [['Transportation', 0, 1], ['MinDist-', 0, 2], ['IOD-', 0, 1],
        #             ['GC-', 0, 2.5], ['MinDistAngle-', 0, 360], ['TranspAngle-', 0, 360],
        #             ['Concavity-', 0, 2], ['CanalWidth', 0, 2],
        #             ['Distal-', 0, 2.5], ['Mesial-', 0, 2.5],
        #             ['Curvature', 0, 1], ['Area-', 0, 2]])


def export_single_specimen_stat_to_excel_sheet(data_file, column_definition, name_converter=None, charts_on_sheet=None):

    xl = win32.gencache.EnsureDispatch('Excel.Application')
    #xl = win32.Dispatch("Excel.Application")
    xl.Visible = True
    wb = xl.Workbooks.Add()

    with open(data_file) as data_file:
        print('  Exporting [{}] ...'.format(data_file))
        data = json.load(data_file)
        model_data_export_to_excel_sheet(data, column_definition=column_definition,
                                         excel_workbook=wb, name_converter=name_converter,
                                         charts_on_sheet=charts_on_sheet)


def export_multiple_specimens_to_corresponding_excel_sheets(data_directory, column_definition,
                                                            name_converter=None, charts_on_sheet=None):

    xl = win32.gencache.EnsureDispatch('Excel.Application')
    xl.Visible = True
    wb = xl.Workbooks.Add()

    for (path, dir, files) in os.walk(data_directory):
        for filename in files:
            with open(path + '/' + filename) as data_file:
                print('  Exporting [{}] ...'.format(filename))
                data = json.load(data_file)
                model_data_export_to_excel_sheet(data, column_definition=column_definition,
                                                 excel_workbook=wb, name_converter=name_converter,
                                                 charts_on_sheet=charts_on_sheet)


def export_multiple_specimens_to_single_excel_sheet(data_directory, column_definition):

    xl = win32.gencache.EnsureDispatch('Excel.Application')
    xl.Visible = True
    wb = xl.Workbooks.Add()
    worksheet = wb.Sheets.Add()
    worksheet.Name = 'all data'

    is_first_file = True
    cur_row_of_sheet = 1

    for (path, dir, files) in os.walk(data_directory):
        for filename in files:
            with open(path + '/' + filename) as data_file:
                model_data = json.load(data_file)
                if is_first_file:
                    # Get name of comparison canals
                    model_header = model_data['model']
                    magnification_ratio = 1 if not 'magnification_ratio' in model_header.keys() else model_header['magnification_ratio']
                    cmp_canals = model_header['pts_of_crvs_cmp'].keys()
                    columns = column_definition(cmp_canals, magnification_ratio)
                    column_header = ','.join(columns.names)
                    excel_helper.fill_a_row_to_sheet(worksheet, column_header, 1)
                    cur_row_of_sheet = 2
                    is_first_file = False

                rows = datatable_from_modeldata(model_data, columns)

                print('  Exporting [{}] ...'.format(filename))

                for index, row in rows.iterrows():
                    r = reduce(lambda x, y: x + ',' + y, row)
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
            model_data_export_to_excel_sheet(model, pst='blx', excel_workbook=wb)

if __name__ == '__main__':
    main()
