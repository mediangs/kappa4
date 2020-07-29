import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import os
import json
from geom import vector
import gc


def get_curve_info(model_data):

    info = {}
    md = model_data['model']
    section_data = model_data['sections']
    magnification_ratio = 1 if not 'magnification_ratio' in md.keys() else md['magnification_ratio']

    ref_key = md['name']
    info[ref_key] = {'ref': True, 'section_pos': [], 'torsions': [], 'curve_heights': [], 'curvatures': [], 'canal_width': []}
    if md['pts_of_crvs_cmp']:
        for key in md['pts_of_crvs_cmp']:
            info[key] = {'ref': False, 'section_pos': [], 'torsions': [], 'curve_heights': [], 'curvatures': [], 'canal_width': []}

    for sd in section_data:
        width = (vector(sd['cnl_ref_narrow'][0]) - vector(sd['cnl_ref_narrow'][1])).length()
        info[ref_key]['section_pos'].append(sd['section'] / magnification_ratio)
        info[ref_key]['torsions'].append(sd['torsion_ref'])
        info[ref_key]['curve_heights'].append(sd['CH_ref'] / magnification_ratio)
        info[ref_key]['curvatures'].append(sd['curvature_ref'] * magnification_ratio)
        info[ref_key]['canal_width'].append(width / magnification_ratio)

        if md['pts_of_crvs_cmp']:

            for key in md['pts_of_crvs_cmp']:
                try:
                    width = (vector(sd['cnls_cmp_narrow'][key][0]) - vector(sd['cnls_cmp_narrow'][key][1])).length()
                except:
                    width = 0
                info[key]['section_pos'].append(sd['section'] /magnification_ratio)

                try:
                    info[key]['torsions'].append(sd['torsions_cmp'][key])
                except:
                    info[key]['torsions'].append(0)

                info[key]['curve_heights'].append(sd['CHs_cmp'][key] / magnification_ratio)

                try:
                    info[key]['curvatures'].append(sd['curvatures_cmp'][key] * magnification_ratio)
                except:
                    info[key]['curvatures'].append(0)
                info[key]['canal_width'].append(width / magnification_ratio)

    return info


def get_torsion_crossings_coord(sections, torsions, curve_heights):
    #todo None 처리
    torsions = [0 if v is None else v for v in torsions]
    index = np.where(np.diff(np.sign(torsions)))[0]
    x = [sections[a] for a in index]
    y = [curve_heights[a] for a in index]
    return x, y


def curvature_colormap_fig(model_data, vlines=[], show_torsion=True):
    curves_info = get_curve_info(model_data)
    names, x_axes, y_gcs, y_lcs, canal_widths, x_torsions, y_torsions = [], [], [], [], [], [], []
    for k, v in curves_info.items():
        names.append(k)
        sections = v['section_pos']
        GCs = v['curve_heights']
        LCs = v['curvatures']

        x_axes.append(np.array(sections))
        y_gcs.append(np.array(GCs))
        y_lcs.append(np.array(LCs))
        canal_widths.append(np.array(v['canal_width']))

        if show_torsion:
            TRs = v['torsions']
            _tx, _ty = get_torsion_crossings_coord(sections, TRs, GCs)
            x_torsions.append(_tx)
            y_torsions.append(_ty)

    ylim = max(2, max(y_gcs[0]) + 0.1) # range of y-axis
    xlim = max(13, max(x_axes[0]) + 0.2) #range of x-axis

    fig, axs = plt.subplots(nrows=len(x_axes), ncols=1, figsize=(15, 4 * len(x_axes) - len(x_axes) + 1), sharex='all', sharey='all')

    for i, _ in enumerate(x_axes):
        ax = axs if len(x_axes) == 1 else axs[i]
        ax.set_title(names[i])
        ax.set_xlabel('Apex <---     Distance from apex (mm)     ---> Orifice')
        ax.set_ylabel('Curve height, Canal width (mm)')
        ax.set_xlim(0, xlim)
        ax.set_ylim(0, ylim)
        ax.grid(axis='y', which='major', linewidth=0.5)
        ax.plot(x_axes[i], canal_widths[i], label='Canal width')
        if len(vlines) > 0:
            for ln in vlines:
                ax.axvline(x=ln, linewidth=0.5)
        if show_torsion:
            ax.scatter(x_torsions[i], y_torsions[i], label='Twisting point')

        ax.legend()

        # Create a continuous norm to map from data points to colors
        norm = plt.Normalize(0, 1.0)
        points = np.array([x_axes[i], y_gcs[i]]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        line_collection = LineCollection(segments, cmap='Reds', norm=norm)
        # Set the values used for colormapping
        line_collection.set_array(y_lcs[i])
        line_collection.set_linewidth(3)
        line = ax.add_collection(line_collection)
        cbar =fig.colorbar(line, ax=ax)
        cbar.ax.set_ylabel('Curvature (1/mm)')

    return fig


def curve_plot(model_data, data_directory=None):
    fig = curvature_colormap_fig(model_data)
    md = model_data['model']

    if md['crv_name']:
        name = md['crv_name'].split('.')[1]
        if not ('mb' in name or 'ml' in name):
            name = md['crv_name'].split('.')[1] + '.' + md['crv_name'].split('.')[2]

    if data_directory:
        data_directory = data_directory+'/figs'
        if not os.path.exists(data_directory):
            os.mkdir(data_directory)

        plt.savefig(data_directory+'/'+name+'.png', dpi=300)
        print('Saving '+data_directory+'/'+name+'.png')

        fig.clf()
        plt.close()
        gc.collect()
    else:
        plt.show()


def canal_curve_plot(data_file):
    with open(data_file) as data_file:
        curve_plot(json.load(data_file))


def multiple_canal_curve_plot_export(data_directory):
    for (path, _, files) in os.walk(data_directory):
        for filename in (f for f in files if f.lower().endswith('.json')):
            with open(path + '/' + filename) as data_file:
                curve_plot(get_curve_info(json.load(data_file)), data_directory)




