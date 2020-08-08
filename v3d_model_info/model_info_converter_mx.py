import data_mxl_canals as data_set


def pos_str(pos):
    return 'CONST.UR CONST.UL CONST.LR CONST.LL'.split()[pos]

    # specimen_info['canals'] = [{'name':'mb', 'furcation_pos': 9.0, 'is_buccal_side': True, 'pts_canal': mbc, 'pts_opposite': mb2c},
    #                            {'name':'mb2', 'furcation_pos': 7.9, 'is_buccal_side': False, 'pts_canal': mb2c, 'pts_opposite': mbc},
    #                            {'name':'db', 'furcation_pos': 8.8, 'is_buccal_side': True, 'pts_canal': dbc, 'pts_vector': blv},
    #                            {'name':'p', 'furcation_pos': 10.4, 'is_buccal_side': False, 'pts_canal': pc, 'pts_vector': blv}]

def canal_tail(name):
    ret =''
    if name =='pre-mb':
        ret = "'pts_canal': pre_mb, 'pts_opposite': pre_mb2"
    elif name == 'pre-mb2':
        ret = "'pts_canal': pre_mb2, 'pts_opposite': pre_mb"
    elif name == 'pre-db':
        ret = "'pts_canal': pre_db, 'pts_vector': bl_vector"
    elif name == 'pre-p':
        ret = "'pts_canal': pre_p, 'pts_vector': bl_vector"
    else:
        'ERROR'
    return ret



specimens = data_set.specimens[:]

print()
print('get_specimen_infos():')
print('    infos=[]')

for s in specimens:
    print(f"    specimen_info = {{'name':'{s.name}', 'position': {pos_str(s.tooth_position)}, 'note': '{s.note}', 'weine_classification': {s.weine_classification}, 'canals':[] }}")
    pts_vector = None
    for canal in s.canals:
        pts_str = f'{sum(canal.pts_canal,[])}'.replace('[',"'").replace(']',"'").replace(',', ' ')
        print(f'    {canal.name.replace("-","_")} = {pts_str}')

        if canal.pts_vector:
            pts_vector = f'    {canal.pts_vector}'.lstrip().rstrip().replace('\n', " ")
    if pts_vector:
        print(f"    bl_vector = '{pts_vector}'")

    print()
    for canal in s.canals:
        print(f"    specimen_info['canals'].append({{'name':'{canal.name}', 'furcation_pos':{canal.furcation_pos}, 'is_buccal_side':{canal.is_buccal_side}, {canal_tail(canal.name)}}})")

    print(f'    infos.append(specimen_info)')

    print()
    print()

print('    return infos')


