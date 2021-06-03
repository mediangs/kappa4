from datatable_column_definition import column_definition_single_canal as column_definition


_dataset = [{'name': 'Maxillary Molar:mx', 'dir': './rendered_json/mx6/mx/'},
            {'name': 'Maxillary Molar:mxk', 'dir': './rendered_json/mx6/mxk/'},
            {'name': 'Maxillary Molar:mxl', 'dir': './rendered_json/mx6/mxl/'},
            {'name': 'Mandibular Molar', 'dir': './rendered_json/mn6/output/'},
            # {'name': 'Shaper', 'dir': './rendered_json/g20.shaping/output-shaper-sound-new/'},
            # {'name': 'Shaper-centroid', 'dir': './rendered_json/g20.shaping/output-shaper-sound-cog/'},
            ]

chart_list = [{'checkbox_argument': ['Mindist chart', True],
               'head':'### Mindist(mm)',
               'chart_columns':'MinDist-', 'y_axis':[0, 2], 'ylabel':'Thinnest dentin thickness(mm)'},

              {'checkbox_argument': ['Canal area chart', True],
               'head': '### Canal area (mm^2)',
               'chart_columns': 'Area-', 'y_axis': [0, 2], 'ylabel': 'Canal area(mm^2)'},

              {'checkbox_argument': ['Mindist angle chart', True],
               'head': '### Mindist angle',
               'chart_columns': 'MinDistAngle-', 'y_axis': [0, 360], 'ylabel': 'Direction of thinnest dentin'},

              {'checkbox_argument': ['Roundness chart', True],
               'head': '### Roundness(1: circle, 0: line)',
               'chart_columns': 'Roundness', 'y_axis': [0.5, 1.1], 'ylabel': 'Roundness'},
              ]


def pretty_filename(name):
    name = name.replace('-pre-', ' : ').split('-')[0]
    return name


def config_chart_parameters():
    from class_parameter import DrawOptionParameters
    param = DrawOptionParameters()
    param.use_matplot = False
    param.legend = True
    param.legend_width = True  # display canal width and area info
    param.root_outlines = True
    param.canal_outlines = True
    param.all_canal_outlines = True  # for debugging of images
    param.curve_axis = True
    param.curve_height = False
    param.curve_height_axis = False
    param.crossing_points = True
    param.mindist_pre = True
    param.orthogonal_line = False
    param.concavity = False
    param.centroids = True
    param.artificial_circles = []
    param.centroids_onsite = []
    param.sections = [6.0]
    return param


def get_directory_and_files():
    from os import listdir
    from os.path import isfile, join
    import streamlit as st

    dataset_name = st.sidebar.selectbox('', [x['name'] for x in _dataset])
    directory = next((item['dir'] for item in _dataset if item["name"] == dataset_name), None)
    return directory, [f for f in listdir(directory) if isfile(join(directory, f))], dataset_name


def get_dataset_info():
    return {'pretty_filename': pretty_filename,
            'get_directory_and_files': get_directory_and_files,
            'config_chart_parameters': config_chart_parameters,
            'column_definition': column_definition,
            'chart_list': chart_list, }


