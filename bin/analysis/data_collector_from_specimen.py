import json
import os

from class_model import ModelData
from class_section import SectionData


def curves_data_collector(specimens, output_dir):

    specimen_curves_data = dict()

    for specimen in specimens:
        for canal in specimen.canals:
            md = ModelData(specimen, canal_ref=canal.name)
            specimen_curves_data.update({md.crv_name: md.dump_curve_pts()})

        with open('{}/output/{}-curves.json'.format(output_dir, specimen.name), 'w') as f:
            print('==> Writing to {}'.format(f.name))
            f.write(json.dumps(specimen_curves_data))

        specimen_curves_data = {}


def specimens_with_multiple_canals_data_collector(specimens, section_interval, output_dir,
                                                  output_file, export_to_separate_files,
                                                  evaluating_canals=['all'],
                                                  concavity=True):
    specimen_data = dict()

    for specimen in specimens:
        for canal in specimen.canals:
            if canal.cnls_cmp_name and 'all' in evaluating_canals or canal.name in evaluating_canals:
                md = ModelData(specimen, canal_ref=canal.name, canals_cmp=canal.cnls_cmp_name)
                specimen_data['model'] = md.dump(curve_pts=True)
                specimen_data['sections'] = [
                    SectionData(md, (x * md.magnification_ratio) / 10.0, concavity).dump(outline=True) for x in
                    range(0, int(md.crv_ref_length * 10 / md.magnification_ratio), int(section_interval * 10))]

                if export_to_separate_files:
                    if not os.path.exists(output_dir):
                        os.mkdir(output_dir)

                    with open(f'{output_dir}/{md.name}-{section_interval}mm.json', 'w') as f:
                        print(f'==> Writing to {f.name}')
                        f.write(json.dumps(specimen_data))

                specimen_data = {}


def specimens_with_single_canal_data_collector(specimens, section_interval, output_dir,
                                               output_file, export_to_separate_files,
                                               evaluating_canals=['all'],
                                               concavity=True, sections=None):
    specimen_data = dict()

    for specimen in specimens:
        for canal in specimen.canals:
            if 'all' in evaluating_canals or canal.name in evaluating_canals:
                md = ModelData(specimen, canal_ref=canal.name)
                specimen_data['model'] = md.dump(curve_pts=True)
                if section_interval:
                    specimen_data['sections'] = [
                        SectionData(md, x * md.magnification_ratio / 10.0, concavity).dump(outline=True) for x in
                        range(0, int(md.crv_ref_length * 10 / md.magnification_ratio), int(section_interval * 10))]
                elif sections:
                    specimen_data['sections'] = [
                        SectionData(md, x * md.magnification_ratio, concavity).dump(outline=True) for x in sections]

                if export_to_separate_files:
                    if not os.path.exists(output_dir):
                        os.mkdir(output_dir)

                    with open(f'{output_dir}/{md.crv_name}-{section_interval}mm.json', 'w') as f:
                        print('==> Writing to {}'.format(f.name))
                        f.write(json.dumps(specimen_data))

                specimen_data = {}
            else:
                print(f'No matching canal! {canal.name}')


if __name__ == '__main__':
    import os
    import data_mx_canals as data_set

    specimens = data_set.specimens[0:5]
    section_interval = 7  # unit - mm
    output_dir = os.getcwd()
    output_file = 'mx6.1-2-{}mm.json'.format(section_interval)

    export_to_separate_files = False
    evaluating_canals = ['all']

    print(os.getcwd())

    # data_collector(specimens, section_interval, output_dir, output_file, export_to_separate_files, evaluating_canals)
    curves_data_collector(specimens, output_dir)
