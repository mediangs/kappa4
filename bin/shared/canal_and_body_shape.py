import math


def endofile_radius(file_size, taper, distance):
    """
    :param file_size: 8, 10, 15, 20 ...
    :param taper: 0.02, 0.04, 0.06
    :param distance: the distance from a file tip, 확대 전의 길이
    :return:
    """
    return (file_size / 100 + taper * distance)/2


def endofile_section_outlines(file_size, taper, picked_sections, model_data):
    """

    :param file_size:
    :param taper:
    :param picked_sections:
    :param model_data:
    :return:[{'':, '':} ]
    """
    from extract_outlines_from_vertices import get_circle_around_point, sort_and_segment_vertices
    from geom import vector

    magnification_ratio = 1 if 'magnification_ratio' not in model_data['model'] else model_data['model'][
        'magnification_ratio']
    endofile_sections = []

    for section in model_data['sections']:
        if any(math.isclose(x, section['section'] / magnification_ratio, rel_tol=1e-3) for x in picked_sections):

            #확대전의 파일 반지름을 구함
            radius = endofile_radius(file_size, taper, section['section'] / magnification_ratio)

            #확대된 상태의 원을 구함, 파일을 확대한 값으로 전달해야함
            circle = get_circle_around_point(center=vector(section['pt_at_crv_ref']),
                                             tangent_vector=vector(section['t_vector_at_crv_ref']),
                                             radius=radius * magnification_ratio, magnification_ratio=magnification_ratio)

            sorted_circle = sort_and_segment_vertices(circle, vector(section['pt_at_crv_ref']),
                                                      magnification_ratio=magnification_ratio)

            endofile_sections.append({'description': f'#{file_size}, {taper:.2f} Taper, Diameter {radius*2:.2f}mm', 'points': sorted_circle[0]})

    return endofile_sections


def canal_centroids(model_data, picked_sections):
    import math
    from shape_analysis import outline_centroid

    magnification_ratio = 1 if 'magnification_ratio' not in model_data['model'] else model_data['model'][
        'magnification_ratio']
    centroids = []

    for section in model_data['sections']:
        if any(math.isclose(x, section['section'] / magnification_ratio, rel_tol=1e-3) for x in picked_sections):
            centroid = outline_centroid(section['pt_at_crv_ref'], section['t_vector_at_crv_ref'], section['cnl_ref_major_outline'])
            centroids.append(centroid)

    return centroids
