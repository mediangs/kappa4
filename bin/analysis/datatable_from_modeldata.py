from collections import OrderedDict


def keyvalue_pretty_format(value, ratio):
    if value is None:
        return ''
    elif not isinstance(value, str):
        value *= ratio
        return f'{value:0.1f}' if value > 10.0 else f'{value:0.3f}'
    else:
        return value


def num(s):
    try:
        return float(s)
    except ValueError:
        return 0.0


def keyvalue_from_section(sd, key, ratio):
    # AreaChange : PostArea - PreArea
    # [f'area_cnls_cmp!{x}-area_cnl_ref' for x in cmp_canals]
    if '-' in key:
        keys = key.split('-')
        return str(num(_keyvalue(sd, keys[0], ratio)) - num(_keyvalue(sd, keys[1], ratio)))

    elif '/' in key:
        keys = key.split('/')
        try:
            return str(num(_keyvalue(sd, keys[0], ratio)) / num(_keyvalue(sd, keys[1], ratio)))
        except:
            return ''

    elif '+' in key:
        keys = key.split('+')
        return str(num(_keyvalue(sd, keys[0], ratio)) + num(_keyvalue(sd, keys[1], ratio)))

    else:
        return _keyvalue(sd, key, ratio)


def _keyvalue(sd, key, ratio):
    token = key.split('!')
    keyvalue = ''
    # 마지막이 숫자이면 interger 로 변환 --> Index임
    # [f'cnls_cmp_narrow!{x}!2' for x in cmp_canals]
    token[-1] = int(token[-1]) if token[-1].isdecimal() else token[-1]
    try:
        if len(token) == 1:
            keyvalue = keyvalue_pretty_format(sd[token[0]], ratio)

        elif len(token) == 2:
            keyvalue = keyvalue_pretty_format(sd[token[0]][token[1]], ratio)

        elif len(token) == 3:
            keyvalue = keyvalue_pretty_format(sd[token[0]][token[1]][token[2]], ratio)
    finally:
        return keyvalue


def datatable_from_modeldata(model_data, col_def):

    import pandas as pd
    from shape_analysis import outline_roundness

    echo = False

    mdata =OrderedDict(zip(col_def.names, [[] for _ in range(len(col_def.names))]))
    md = model_data['model']
    section_data = model_data['sections']
    ratio = 1 if not 'magnification_ratio' in md.keys() else 1 / md['magnification_ratio']
    # furcation_pos는 보정된 길이로 저장되어 있다고 가정함
    furcation_pos = None if not 'furcation_pos' in md else md['furcation_pos']
    orifice_pos = section_data[-1]['section'] * ratio

    for sd in section_data:
        exception = ''
        if not sd['bdy_major_outline_exist']: exception += 'BODY '
        if not sd['cnl_ref_major_outline_exist']: exception += 'CANAL-PRE '
        if sd['median_major_axis_used']:  exception += 'STD-AXIS '

        for i, name in enumerate(col_def.names):
            if name == 'RootName':
                mdata['RootName'].append(md['name'])
            elif name == 'CanalSide':
                mdata['CanalSide'].append(md['crv_name'].split('-')[-1])
            elif name =='Exception':
                mdata['Exception'].append(exception)
            elif name == 'WeineClassification':
                mdata['WeineClassification'].append('' if not 'weine_classification' in md else str(md['weine_classification']))
            elif name == 'LengthFromApex':
                mdata['LengthFromApex'].append(f'{sd["section"] * ratio:.2f}')
            elif name == 'LengthFromOrifice':
                mdata['LengthFromOrifice'].append(f'{orifice_pos - sd["section"] * ratio:.2f}')
            elif name == 'LengthFromFurcation':
                if furcation_pos:
                    pos = furcation_pos - sd['section'] * ratio
                    mdata['LengthFromFurcation'].append('' if pos < 0 else str(pos))
                else:
                    mdata['LengthFromFurcation'].append('')
            elif name == 'Roundness':
                mdata['Roundness'].append(f"{outline_roundness(sd['pt_at_crv_ref'], sd['t_vector_at_crv_ref'], sd['bdy_major_outline']):.3f}")
            else:
                mdata[col_def.names[i]].append(keyvalue_from_section(sd, col_def.keys[i], col_def.conversions[i]))

    return pd.DataFrame(mdata)