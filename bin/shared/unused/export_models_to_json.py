from __future__ import division

import json


class json_data(object):

    def __init__(self, position, up, lookAt, sensitivity):
        self.jo = {'camera': {'position': position, 'up': up, 'lookAt': lookAt},
                   'controls': {'sensitivity': sensitivity},
                   'objects': []}

    def add_line(self, points, color):
        P = [(p[0], p[1], p[2]) for p in points]
        self.jo['objects'].append({'type': 'Line', 'points': P, 'color': color})

    def add_mesh(self, vertices, faces, color):
        V = [(v[0], v[1], v[2]) for v in vertices]
        F = [(f[0], f[1], f[2]) for f in faces]
        self.jo['objects'].append({'type': 'Mesh', 'vertices': V, 'faces': F, 'color': color})
        
    def add(self, key, value):
        self.jo['objects'].append({key:value})
        
    def export(self, path):
        with open(path, 'w') as fp:
            fp.write(json.dumps(self.jo))


def test0():
    jd = json_data((0, 0, 20), (0, 1, 0), (4, 4, 10), 10)
    sub_value = {'aaa' : [1,2,3,4]}
    value = {'sub1': sub_value}
    print(value)
    jd.add('section1', value)
    # lines
    # export
    jd.export('../json_test/data0.json')


def test1():
    jd = json_data((0, 0, 20), (0, 1, 0), (4, 4, 10), 10)
    # lines
    jd.add_line([[6.11, 6.51, 17.88], [5.97, 6.42, 17.61], [4.00, 5.45, 13.61], [2.81, 4.15, 9.38], [3.72, 4.23, 5.09], [4.39, 4.41, 3.88]],
                0x66ffff)
    jd.add_line([[6.09, 6.51, 17.88], [4.30, 6.27, 14.12], [3.18, 7.47, 10.18], [3.93, 7.49, 5.89], [4.42, 7.50, 3.98]],
                0x9999ff)
    # meshes
    V = [(0, 0, 0), (5, 0, 0), (0, 5, 0)]
    F = [(0, 1, 2)]
    jd.add_mesh(V, F, 0xffff00)
    # export
    jd.export('../json_test/data1.json')

def test2():
    jd = json_data((0, 0, 20), (0, 1, 0), (4, 4, 10), 10)
    # lines
    jd.add_line([[6.11, 6.51, 17.88], [5.97, 6.42, 17.61], [4.00, 5.45, 13.61], [2.81, 4.15, 9.38], [3.72, 4.23, 5.09], [4.39, 4.41, 3.88]],
                0x66ffff)
    jd.add_line([[6.09, 6.51, 17.88], [4.30, 6.27, 14.12], [3.18, 7.47, 10.18], [3.93, 7.49, 5.89], [4.42, 7.50, 3.98]],
                0x9999ff)
    # mesh 1
    V = [(0, 0, 0), (5, 0, 0), (0, 5, 0)]
    F = [(0, 1, 2)]
    jd.add_mesh(V, F, 0xffff00)
    # mesh 2
    import v3d
    path = 'LJKCS01M-canal-pre-zoff.v3d'
    _, (indices, vertices, _) = v3d.read(path)
    jd.add_mesh(vertices, indices, 0x333300)
    # export
    jd.export('../cases/data2.json')

def test3():
    jd = json_data((0, 0, 20), (0, 1, 0), (4, 4, 10), 10)
    import v3d
    path = '../Kappa3-CanalChange/v3d_ljkcs/LJKCS05M/LJKCS05M-solid-body-zoff.v3d' 
    _, (indices, vertices, _) = v3d.read(path)
    #jd.add_mesh(vertices, indices, 0x333300)
    
    path = '../Kappa3-CanalChange/v3d_ljkcs/LJKCS05M/LJKCS05M-canal-pre-zoff.v3d' 
    _, (indices, vertices, _) = v3d.read(path)
    #jd.add_mesh(vertices, indices, 0x333300)

    path = '../Kappa3-CanalChange/v3d_ljkcs/LJKCS05M/LJKCS05M-canal-post-zoff.v3d' 
    _, (indices, vertices, _) = v3d.read(path)
    jd.add_mesh(vertices, indices, 0x333300)

    # export
    jd.export('../Kappa3-CanalChange/json/LJKCS05M.json')


if __name__ == '__main__':
    test0()
    #test3()
    print("done")
