import sys
import streamlit as st
sys.path.insert(1, './bin/analysis')
sys.path.insert(2, './bin/shared')

import streamlit_helper as sh
import canal_and_body_shape as cbs
from st_chart_g20_shaping_data import get_dataset_info
# from tooth_model_info import get_dataset_info


def app():
    import model_drawer as cd
    from multicolor_curvature_plot import curvature_colormap_fig
    from SessionState import SessionState

    info = get_dataset_info()
    pretty_filename =info['pretty_filename']
    get_directory_and_files = info['get_directory_and_files']
    config_chart_parameters = info['config_chart_parameters']
    chart_list = info['chart_list']
    column_definition = info['column_definition']

    param = config_chart_parameters()
    #ss = sh.Mock()
    ss = SessionState.get(data_file='', model_data='', data_table='', dataset_name='', coord_visible=False,
                          picked_sections=param.sections, furcation_pos=None)  # Pick some initial values.

    st.sidebar.subheader('Dataset')
    directory, files, dataset_name = get_directory_and_files()
    selected_file = st.sidebar.selectbox('Select model', sorted(files), format_func=pretty_filename)
    if (selected_file+dataset_name) != ss.data_file+ss.dataset_name:
        ss.model_data = sh.load_model_data(directory + selected_file)
        ss.data_table = sh.processed_datatable(ss.model_data, column_definition)
        ss.data_file = selected_file
        ss.dataset_name = dataset_name
        ss.furcation_pos = ss.model_data['model']['furcation_pos']

    # directory = './output-hero-sound-new/'
    # selected_file = 'GHero.50M-mb.sound-0.1mm.json'
    # ss.model_data = sh.load_model_data(directory + selected_file)
    # ss.data_table = sh.processed_datatable(ss.model_data, column_definition)
    # ss.data_file = selected_file
    # ss.furcation_pos = ss.model_data['model']['furcation_pos']

    st.sidebar.subheader('Model configuration')
    section_min, section_max, section_step = sh.get_section_range_info(ss.model_data)
    ss.picked_sections = [st.sidebar.slider('Section Level( Apex <--> Orifice )',
                                            section_min, section_max, param.sections[0], section_step)]

    if st.sidebar.checkbox('Stepwise navigation'):
        ss.picked_sections = [st.sidebar.number_input('Step', section_min, section_max, ss.picked_sections[0], 0.5)]

    if st.sidebar.checkbox('Multiple sections'):
        if ret := sh.string_to_valid_section_list(
                st.sidebar.text_input('Input sections(eg: 4.0, 6.5)', value='0, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11')):
            ss.picked_sections = ret

    ss.coord_visible = st.sidebar.checkbox('Coordinate axes', ss.coord_visible)
    param.legend = st.sidebar.checkbox('Legend', param.legend)
    param.curve_axis = st.sidebar.checkbox('Canal axes', param.curve_axis)
    param.concavity = st.sidebar.checkbox('Concavity', param.concavity)
    param.orthogonal_line = st.sidebar.checkbox('Dentin thicknesses', param.orthogonal_line)
    param.centroids = st.sidebar.checkbox('Center of canals(x mark)', param.centroids)

    # if st.sidebar.checkbox('Center of canal'):
    #     # Onsite centroid calculation
    #     param.centroids = cbs.canal_centroids(ss.model_data, ss.active_sections)

    if st.sidebar.checkbox('File outline'):
        file_size = st.sidebar.number_input('File size(8, 10, 15, ...', 5, 100, 30, 5)
        file_taper = st.sidebar.number_input('Taper(0.00, 0.02, ...', 0.0, 0.1, 0.04)
        param.artificial_circles = cbs.endofile_section_outlines(file_size, file_taper, ss.picked_sections, ss.model_data)

    param.sections = ss.picked_sections

    st.subheader(sh.chart_head_label(pretty_filename(ss.data_file), ss.picked_sections))
    st.plotly_chart(cd.model3d_drawer(param, ss.model_data, ss.coord_visible))

    st.sidebar.subheader('Charts')

    if st.sidebar.checkbox('Curvature chart', False):
        st.write('### Curvature, Curve height and canal width')
        st.pyplot(curvature_colormap_fig(ss.model_data, ss.picked_sections, show_torsion=True))

    for chart in chart_list:
        if st.sidebar.checkbox(*chart['checkbox_argument']):
            st.write(chart['head'])
            st.plotly_chart(sh.datatable_subset_fig(ss.data_table, chart['chart_columns'], chart['y_axis'],
                                                    ss.picked_sections, ss.furcation_pos,
                                                    ylabel=chart['ylabel']))

    # if st.sidebar.checkbox('Raw data', False):
    #     st.write('### Raw data')
    #     st.dataframe(ss.data_table)


if __name__ == '__main__':
    app()
