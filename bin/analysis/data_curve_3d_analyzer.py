# -*- coding: cp949 -*-

from __future__ import division

from collections import OrderedDict
import win32com.client as win32  # Excel export
from functools import reduce

import json
import os

import dist_util as du  # collection of utility function
import excel_helper
from geom import vector
import numpy


def export_curve_3d_stat_to_excel(data_directory):

    xl = win32.gencache.EnsureDispatch('Excel.Application')
    xl.Visible = True
    wb = xl.Workbooks.Add()

    results = []
    for (path, dir, files) in os.walk(data_directory):
        for filename in files:
            with open(path + '/' + filename) as data_file:
                results.append(curve_3d_stat(json.load(data_file)))

    worksheet = wb.Sheets.Add()
    worksheet.Name = 'curve_analysis'

    column_header = ','.join(results[0].keys())
    excel_helper.fill_a_row_to_sheet(worksheet, column_header, 1)

    current_row = 2
    print(column_header)
    for e in results:
        v = reduce(lambda x, y: x + ',' + y, e.values())
        print (v)
        excel_helper.fill_a_row_to_sheet(worksheet, v, current_row)
        current_row += 1


def get_torsion_zero_crossings_pos(section_pos, torsions):
    torsions_zero_crossings_index = numpy.where(numpy.diff(numpy.sign(torsions)))[0]
    torsions_zero_crossings_pos = [section_pos[x] for x in torsions_zero_crossings_index]
    torsions_zero_crossings_pos.insert(0, section_pos[0])
    torsions_zero_crossings_pos.append(section_pos[-1])
    return torsions_zero_crossings_pos


def curve_3d_stat(model_data):
    echo = False
    md = model_data['model']
    section_data = model_data['sections']

    RootName = md['name']
    CanalSide = md['crv_name'].split('-')[-1]
    curve_length = md['crv_ref_length']
    curve_axis_length = (vector(md['apical_end_of_CH']) - vector(md['coronal_end_of_CH'])).length()

    headings = ['RootName', 'CanalSide', 'CurveLength', 'CurveAxisLength', 'CurveLengthDiff', 'MeanCurvature',
                'MaxCurveHeight', 'MaxCurveHeightPos',
                'PercentilePosApex', 'PercentilePosApexOrifice',
                'TorsionZeroCrossings','TorsionZeroCrossingsPos']

    result = OrderedDict(zip(headings, ['' for _ in range(len(headings))]))
    column_header = ','.join(result.keys())
    if echo: print (column_header)

    # for torsion analysis
    section_pos, torsions, curve_heights, curvatures = [], [], [], []

    for sd in section_data:
        section_pos.append(sd['section'])
        torsions.append(sd['torsion_ref'])
        curve_heights.append(sd['CH_ref'])
        curvatures.append(sd['curvature_ref'])

    torsions_zero_crossings_pos = get_torsion_zero_crossings_pos(torsions, section_pos)
    torsions_zero_crossings_intervals = [torsions_zero_crossings_pos[n]-torsions_zero_crossings_pos[n-1]
                                         for n in range(1, len(torsions_zero_crossings_pos))]

    max_curve_height_index = numpy.argmax(curve_heights)
    max_curve_height = curve_heights[max_curve_height_index]
    max_curve_height_pos = section_pos[max_curve_height_index]
    max_curve_height_percentile_from_apex = max_curve_height_pos / (section_pos[-1] - section_pos[0])
    max_curve_height_percentile_from_orifice = (section_pos[-1]-max_curve_height_pos
                                                ) / (section_pos[-1] - section_pos[0])

    result['RootName'] = RootName
    result['CanalSide'] = CanalSide
    result['CurveLength'] = '{0}'.format(curve_length)
    result['CurveAxisLength'] = '{0}'.format(curve_axis_length)
    result['CurveLengthDiff'] = '{0}'.format(curve_length - curve_axis_length)
    result['MeanCurvature'] = '{0}'.format(sum(curvatures) / float(len(curvatures)))
    result['MaxCurveHeight'] = '{0}'.format(max_curve_height)
    result['MaxCurveHeightPos'] = '{0}'.format(max_curve_height_pos)
    result['PercentilePosApex'] = '{0}'.format(max_curve_height_percentile_from_apex)
    result['PercentilePosApexOrifice'] = '{0}'.format(max_curve_height_percentile_from_orifice)
    result['TorsionZeroCrossings'] = str(len(torsions_zero_crossings_intervals))
    result['TorsionZeroCrossingsPos'] = reduce(lambda x, y: str(x) + ',' + str(y), torsions_zero_crossings_pos)

    if echo:
        print('{0},{1}:{2}'.format(result['RootName'], result['CanalSide'],len(torsions_zero_crossings_intervals)))
        print(torsions_zero_crossings_pos)
        print(torsions_zero_crossings_intervals)
        print('max curve height: {:.2f}, position: {:.1f}, percentile pos: {:.3f}'.
              format(max_curve_height, max_curve_height_pos, max_curve_height_percentile_from_apex))

    return result
