from dataclasses import dataclass


@dataclass
class ColumnDefinition:
    names: []
    keys: []
    conversions: []


def column_definition_multicanal_small(cmp_canals, ratio):

    column_names = 'LengthFromApex LengthFromOrifice LengthFromFurcation'.split()
    column_keys = 'section - -'.split()
    conversions = [1/ratio, None, None]

    # Concavity(cv_dist, cv_p_1, cv_p12, cv_p3, cv_p4)
    column_names.extend('Concavity-Mesial Concavity-Distal'.split())
    column_keys.extend('mesial_concavity!0 distal_concavity!0'.split())
    conversions.extend([1/ratio, 1/ratio])

    # DentinThickness(p_body, p_canal, thickness, angle)
    column_names.append('MinDist-Pre')
    column_keys.append('mindist_ref!2')
    conversions.append(1/ratio)

    column_names.extend([f'MinDist-{x}' for x in cmp_canals])
    column_keys.extend([f'mindists_cmp!{x}!2' for x in cmp_canals])
    conversions.extend([1/ratio for x in cmp_canals])

    # DentinThickness(p_body, p_canal, thickness, angle)
    column_names.append('MinDistAngle-Pre')
    column_keys.append('mindist_ref!3')
    conversions.append(1)

    column_names.extend([f'MinDistAngle-{x}' for x in cmp_canals])
    column_keys.extend([f'mindists_cmp!{x}!3' for x in cmp_canals])
    conversions.extend([1 for x in cmp_canals])

    column_names.extend([f'MinDistIOD-{x}' for x in cmp_canals])
    column_keys.extend([f'mindists_iod!{x}!2' for x in cmp_canals])
    conversions.extend([1/ratio for x in cmp_canals])

    column_names.extend([f'IOD-{x}' for x in cmp_canals])
    column_keys.extend([f'cwt_ratios!{x}' for x in cmp_canals])
    conversions.extend([1 for x in cmp_canals])

    assert (len(column_names) == len(column_keys))
    assert (len(conversions) == len(column_keys))

    return ColumnDefinition(column_names, column_keys, conversions)


def column_definition_single_canal(cmp_canals, ratio):

    column_names = 'RootName CanalSide WeineClassification Exception LengthFromApex LengthFromOrifice LengthFromFurcation GC-Pre'.split()
    column_keys = 'name crv_name weine_classification - section - - CH_ref'.split()
    conversions = [None, None, None, None, 1/ratio, None, None, 1/ratio]

    column_names.append('Curvature-Pre')
    column_keys.append('curvature_ref')
    conversions.append(ratio)

    column_names.append('Torsion-Pre')
    column_keys.append('torsion_ref')
    conversions.append(1)

    # Concavity(cv_dist, cv_p_1, cv_p12, cv_p3, cv_p4)
    column_names.extend('Concavity-Mesial Concavity-Distal'.split())
    column_keys.extend('mesial_concavity!0 distal_concavity!0'.split())
    conversions.extend([1/ratio, 1/ratio])

    # DentinThickness(p_body, p_canal, thickness, angle)
    column_names.append('MinDist-Pre')
    column_keys.append('mindist_ref!2')
    conversions.append(1/ratio)

    column_names.append('Area-Pre')
    column_keys.append('area_cnl_ref')
    conversions.append(1/ratio ** 2)

    column_names.append('CanalWidth-Pre')
    column_keys.append('cnl_ref_narrow!2')
    conversions.append(1/ratio)

    # FileMovement(vector angle distance)
    column_names.append('GCAngle-Pre')
    column_keys.append('cnl_straightening!1')
    conversions.append(1)

    # DentinThickness(p_body, p_canal, thickness, angle)
    column_names.append('MinDistAngle-Pre')
    column_keys.append('mindist_ref!3')
    conversions.append(1)

    # DentinThickness(p_body, p_canal, thickness, angle)
    column_names.extend('Mesial-Pre Distal-Pre Lateral-Pre'.split())
    column_keys.extend('mesial_ref!2 distal_ref!2 lateral_ref!2'.split())
    conversions.extend([1/ratio, 1/ratio, 1/ratio])

    column_names.append('Roundness')
    column_keys.append('-')
    conversions.append(1)


    assert (len(column_names) == len(column_keys))
    assert (len(conversions) == len(column_keys))

    return ColumnDefinition(column_names, column_keys, conversions)


def column_definition_multicanal_extended(cmp_canals, ratio):

    column_names = 'RootName CanalSide WeineClassification Exception LengthFromApex LengthFromOrifice LengthFromFurcation GC-Pre'.split()
    column_keys = 'name crv_name weine_classification - section - - CH_ref'.split()
    conversions = [None, None, None, None, 1/ratio, None, None, 1/ratio]

    column_names.extend([f'GC-{x}' for x in cmp_canals])
    column_keys.extend([f'CHs_cmp!{x}' for x in cmp_canals])
    conversions.extend([1/ratio for x in cmp_canals])

    column_names.append('Curvature-Pre')
    column_keys.append('curvature_ref')
    conversions.append(ratio)

    column_names.extend([f'Curvature-{x}' for x in cmp_canals])
    column_keys.extend([f'curvatures_cmp!{x}' for x in cmp_canals])
    conversions.extend([ratio for x in cmp_canals])

    column_names.append('Torsion-Pre')
    column_keys.append('torsion_ref')
    conversions.append(1)

    column_names.extend([f'Torsion-{x}' for x in cmp_canals])
    column_keys.extend([f'torsions_cmp!{x}' for x in cmp_canals])
    conversions.extend([1 for x in cmp_canals])

    # Concavity(cv_dist, cv_p_1, cv_p12, cv_p3, cv_p4)
    column_names.extend('Concavity-Mesial Concavity-Distal'.split())
    column_keys.extend('mesial_concavity!0 distal_concavity!0'.split())
    conversions.extend([1/ratio, 1/ratio])

    # FileMovement(vector angle distance)
    column_names.extend([f'Transportation-{x}' for x in cmp_canals])
    column_keys.extend([f'cnls_transportation!{x}!2' for x in cmp_canals])
    conversions.extend([1/ratio for x in cmp_canals])

    # FileMovement(vector angle distance)
    column_names.extend([f'TransportationCentroid-{x}' for x in cmp_canals])
    column_keys.extend([f'cnls_centroid_transportation!{x}!2' for x in cmp_canals])
    conversions.extend([1/ratio for x in cmp_canals])

    # DentinThickness(p_body, p_canal, thickness, angle)
    column_names.append('MinDist-Pre')
    column_keys.append('mindist_ref!2')
    conversions.append(1/ratio)

    column_names.extend([f'MinDist-{x}' for x in cmp_canals])
    column_keys.extend([f'mindists_cmp!{x}!2' for x in cmp_canals])
    conversions.extend([1/ratio for x in cmp_canals])

    column_names.extend([f'MinDistIOD-{x}' for x in cmp_canals])
    column_keys.extend([f'mindists_iod!{x}!2' for x in cmp_canals])
    conversions.extend([1/ratio for x in cmp_canals])

    column_names.append('Area-Pre')
    column_keys.append('area_cnl_ref')
    conversions.append(1/ratio ** 2)

    column_names.extend([f'Area-{x}' for x in cmp_canals])
    column_keys.extend([f'area_cnls_cmp!{x}' for x in cmp_canals])
    conversions.extend([1/ratio ** 2 for x in cmp_canals])

    column_names.extend([f'AreaChange-{x}' for x in cmp_canals])
    column_keys.extend([f'area_cnls_cmp!{x}-area_cnl_ref' for x in cmp_canals])
    conversions.extend([1/ratio ** 2 for x in cmp_canals])

    column_names.extend([f'AreaChangeRatio-{x}' for x in cmp_canals])
    column_keys.extend([f'area_cnls_cmp!{x}/area_cnl_ref' for x in cmp_canals])
    conversions.extend([1 for _ in cmp_canals])

    column_names.append('CanalWidth-Pre')
    column_keys.append('cnl_ref_narrow!2')
    conversions.append(1/ratio)

    # CanalDimension(p1, p2, width)
    column_names.extend([f'CanalWidth-{x}' for x in cmp_canals])
    column_keys.extend([f'cnls_cmp_narrow!{x}!2' for x in cmp_canals])
    conversions.extend([1/ratio for x in cmp_canals])

    # FileMovement(vector angle distance)
    column_names.append('GCAngle-Pre')
    column_keys.append('cnl_straightening!1')
    conversions.append(1)

    column_names.extend([f'GCAngle-{x}' for x in cmp_canals])
    column_keys.extend([f'cnls_straightened!{x}!1' for x in cmp_canals])
    conversions.extend([1 for x in cmp_canals])

    column_names.extend([f'TranspAngle-{x}' for x in cmp_canals])
    column_keys.extend([f'cnls_transportation!{x}!1' for x in cmp_canals])
    conversions.extend([1 for x in cmp_canals])

    # DentinThickness(p_body, p_canal, thickness, angle)
    column_names.append('MinDistAngle-Pre')
    column_keys.append('mindist_ref!3')
    conversions.append(1)

    column_names.extend([f'MinDistAngle-{x}' for x in cmp_canals])
    column_keys.extend([f'mindists_cmp!{x}!3' for x in cmp_canals])
    conversions.extend([1 for x in cmp_canals])

    column_names.extend([f'IOD-{x}' for x in cmp_canals])
    column_keys.extend([f'cwt_ratios!{x}' for x in cmp_canals])
    conversions.extend([1 for x in cmp_canals])

    # DentinThickness(p_body, p_canal, thickness, angle)
    column_names.append('Mesial-Pre')
    column_keys.append('mesial_ref!2')
    conversions.append(1/ratio)

    column_names.extend([f'Mesial-{x}' for x in cmp_canals])
    column_keys.extend([f'mesials_cmp!{x}!2' for x in cmp_canals])
    conversions.extend([1/ratio for x in cmp_canals])

    column_names.append('Distal-Pre')
    column_keys.append('distal_ref!2')
    conversions.append(1/ratio)

    column_names.extend([f'Distal-{x}' for x in cmp_canals])
    column_keys.extend([f'distals_cmp!{x}!2' for x in cmp_canals])
    conversions.extend([1/ratio for x in cmp_canals])

    column_names.append('Lateral-Pre')
    column_keys.append('lateral_ref!2')
    conversions.append(1/ratio)

    column_names.extend([f'Lateral-{x}' for x in cmp_canals])
    column_keys.extend([f'laterals_cmp!{x}!2' for x in cmp_canals])
    conversions.extend([1/ratio for x in cmp_canals])

    column_names.append('Roundness')
    column_keys.append('-')
    conversions.append(1)

    assert (len(column_names) == len(column_keys))
    assert (len(conversions) == len(column_keys))

    return ColumnDefinition(column_names, column_keys, conversions)