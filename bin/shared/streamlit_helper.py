import json
import pandas as pd
from plotly import express as px
from functools import reduce
from datatable_from_modeldata import datatable_from_modeldata


class Mock():
    data_file=''
    model_data=''
    data_table=''
    coord_visible=''
    active_sections=[]


def get_section_range_info(model_data):
    md = model_data['model']
    sd = model_data['sections']
    magnification_ratio = 1 if not 'magnification_ratio' in md.keys() else md['magnification_ratio']
    section_min = sd[0]['section'] / magnification_ratio
    section_max = sd[-1]['section'] / magnification_ratio
    section_step = (sd[1]['section'] - sd[0]['section']) / magnification_ratio

    return section_min, section_max, section_step


def datatable_subset_fig(data_table, subset_str, yaxis_range, picked_sections, furcation_pos=None, ylabel=None):
    """

    :param data_table: Pandas dataframe
    :param subset_str: Column 제목,  'MinDist- CanalWidth-', 'Roundness'
    :param yaxis_range: Y축의 범위,  [0, 1]
    :param picked_sections:
    :return:
    """
    subset_tuple = tuple(subset_str.split())
    subset_cols = [col for col in data_table.columns if col.startswith(subset_tuple)]

    df_long = pd.melt(data_table, id_vars=['LengthFromApex'], value_vars=subset_cols)
    fig = px.line(df_long, x='LengthFromApex', y='value', color='variable')
    fig.layout.update(yaxis=dict(range=yaxis_range))
    fig.layout.update(legend_title_text='')
    fig.layout.update(legend_orientation="h")
    fig.layout.update(legend=dict(x=0, y=1), xaxis_title='Length from the apex(mm), Vertical line:Sections[Blue], Furcation[Green]',
                      yaxis_title=ylabel)

    for section in picked_sections:
        fig.add_shape(dict(type="line", x0=section, x1=section, y0=yaxis_range[0], y1=yaxis_range[1], opacity=0.3,
                           line=dict(color="RoyalBlue", width=2)))
    if furcation_pos:
        fig.add_shape(dict(type="line", x0=furcation_pos, x1=furcation_pos, y0=yaxis_range[0], y1=yaxis_range[1],
                           opacity=0.3, line=dict(color="Green", width=3)))

    return fig


def load_model_data(data_file):
    with open(data_file) as data_file:
        return json.load(data_file)


def string_to_valid_section_list(sections_str):
    try:
        return [float(e) for e in sections_str.split(',')]
    except:
        return None


def processed_datatable(model_data, column_def_func):

    magnification_ratio = 1 if not 'magnification_ratio' in model_data['model'].keys() else model_data['model']['magnification_ratio']

    if model_data['model']['pts_of_crvs_cmp']:
        cmp_canals = model_data['model']['pts_of_crvs_cmp'].keys()
    else:
        cmp_canals = None

    columns = column_def_func(cmp_canals=cmp_canals, ratio=magnification_ratio)
    return datatable_from_modeldata(model_data, columns)


def chart_head_label(display_name, sections):

    section_label = f'{sections[0]:.1f}' if len(sections) == 1 else reduce(lambda x, y: f'{x}, {y}',sections)
    return display_name + ': ' + str(section_label) + 'mm from apex'