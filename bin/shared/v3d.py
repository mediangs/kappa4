from __future__ import division
from array import array
from vector_class import vector


def read(path):
    HEADER = ' Generated by V-Works , CyberMed Lab. Inc. V3D 3-dimensional object file        '
    with open(path, 'rb') as fp:
        # header
        assert fp.read(len(HEADER)) == HEADER
        # nfaces, nvertices, nnormals
        num_items = array('I')
        num_items.fromfile(fp, 6)
        nfaces1, nvertices1, nnormals1, nfaces2, nvertices2, nnormals2 = num_items
        assert nvertices1 == nnormals1 and nvertices2 == nnormals2
        # model 1 (high)
        indices1, vertices1, normals1 = array('I'), array('f'), array('f')
        indices1.fromfile(fp, nfaces1 * 3)
        indices1 = [indices1[i * 3:(i + 1) * 3] for i in xrange(nfaces1)]
        vertices1.fromfile(fp, nvertices1 * 3)
        vertices1 = [vector(vertices1[i * 3:(i + 1) * 3]) for i in xrange(nvertices1)]
        normals1.fromfile(fp, nnormals1 * 3)
        normals1 = [vector(normals1[i * 3:(i + 1) * 3]) for i in xrange(nvertices1)]
        # model 2 (low)
        indices2, vertices2, normals2 = array('I'), array('f'), array('f')
        indices2.fromfile(fp, nfaces2 * 3)
        indices2 = [indices2[i * 3:(i + 1) * 3] for i in xrange(nfaces2)]
        vertices2.fromfile(fp, nvertices2 * 3)
        vertices2 = [vector(vertices2[i * 3:(i + 1) * 3]) for i in xrange(nvertices2)]
        normals2.fromfile(fp, nnormals2 * 3)
        normals2 = [vector(normals2[i * 3:(i + 1) * 3]) for i in xrange(nvertices2)]
        # completed.
        return (indices1, vertices1, normals1), (indices2, vertices2, normals2)


def read_facets(path):
    if path.lower().endswith('.v3d'):
        return v3d_read_facets(path)
    elif path.lower().endswith('.stl'):
        return stl_read_facets(path)
    else:
        print(f'The file extension should be either .stl or .v3d')


def stl_read_facets(path):
    from stl import mesh
    m = mesh.Mesh.from_file(path)
    facets = [vector(a) for a in zip(m.v0.tolist(), m.v1.tolist(), m.v2.tolist())]
    return facets, m.normals


def v3d_read_facets_old(path): #normal 과 facets의 수가 틀림
    HEADER = ' Generated by V-Works , CyberMed Lab. Inc. V3D 3-dimensional object file        '
    with open(path, 'rb') as fp:
        # header
        assert fp.read(len(HEADER)).decode('UTF-8') == HEADER
        # nfaces, nvertices, nnormals
        num_items = array('I')
        num_items.fromfile(fp, 6)
        nfaces1, nvertices1, nnormals1, nfaces2, nvertices2, nnormals2 = num_items
        assert nvertices1 == nnormals1 and nvertices2 == nnormals2
        # model 1 (high)
        indices, vertices, normals = array('I'), array('f'), array('f')
        indices.fromfile(fp, nfaces1 * 3)
        indices = [indices[i * 3:(i + 1) * 3] for i in range(nfaces1)]
        vertices.fromfile(fp, nvertices1 * 3)
        vertices = [vector(vertices[i * 3:(i + 1) * 3]) for i in range(nvertices1)]
        normals.fromfile(fp, nnormals1 * 3)
        normals = [vector(normals[i * 3:(i + 1) * 3]) for i in range(nvertices1)]
        facets = [list(map(vertices.__getitem__, index)) for index in indices]
        return facets, normals

def v3d_read_facets(path):
    HEADER = ' Generated by V-Works , CyberMed Lab. Inc. V3D 3-dimensional object file        '
    with open(path, 'rb') as fp:
        # header
        assert fp.read(len(HEADER)).decode('UTF-8') == HEADER
        # nfaces, nvertices, nnormals
        num_items = array('I')
        num_items.fromfile(fp, 6)
        nfaces1, nvertices1, nnormals1, nfaces2, nvertices2, nnormals2 = num_items
        assert nvertices1 == nnormals1 and nvertices2 == nnormals2
        # model 1 (high)
        indices, vertices, point_normals = array('I'), array('f'), array('f')
        indices.fromfile(fp, nfaces1 * 3)
        indices = [indices[i * 3:(i + 1) * 3] for i in range(nfaces1)]
        vertices.fromfile(fp, nvertices1 * 3)
        vertices = [vector(vertices[i * 3:(i + 1) * 3]) for i in range(nvertices1)]
        point_normals.fromfile(fp, nnormals1 * 3)
        point_normals = [vector(point_normals[i * 3:(i + 1) * 3]) for i in range(nvertices1)]
        facets = [list(map(vertices.__getitem__, index)) for index in indices]
        normals = [(vector(p[1])-vector(p[0])).cross(vector(p[2])-vector(p[1])) for p in facets]
        #normals = [(vector(p[0])-vector(p[1])).cross(vector(p[1])-vector(p[2])) for p in facets]

        return facets, normals


def export_as_wrl(facets, path):

    print ('WRL export : {name} ...'.format(name=path))
    with open(path, 'w') as fp:
        n = len(facets)
        fp.write('Shape { geometry IndexedFaceSet { coord Coordinate { \npoint [\n')
        for i in range(n):
            p1, p2, p3 = facets[i]
            fp.write('%f %f %f,\n' % tuple(p1))
            fp.write('%f %f %f,\n' % tuple(p2))
            fp.write('%f %f %f,\n' % tuple(p3))
        fp.write('] } \ncoordIndex [\n')
        for i in range(n):
            fp.write('%d %d %d -1\n' % (i * 3, i * 3 + 1, i * 3 + 2))
        fp.write(']\n}\n}\n')


def test():
    #E:\0.jongki.data\Dropbox\15.Develop\EclipseWorkspace\Kappa3-CanalChange\v3d_ljkcs\LJKCS01M
    #facets = read_facets('v3d_ljkcs/LJKCS01M/LJKCS01M-canal-pre-zoff.v3d')
    facets_v3d = read_facets('../../v3d.models/v3d_ljkrp1/rp01/RP01-canal-post-zoff-blx.v3d')
    facets_stl = read_facets('../../v3d.models/stl_ljkrp/ljkrp/ljkrp-canal.stl')


    print(facets_stl[1])
    print(facets_v3d[1])
    print('success')

def test_export_wrl():
    import os
    dir_name = os.getenv('TOOTH_DATA') + '/v3d_ljkcs/'

    facets = read_facets(dir_name+'')
    export_as_wrl(facets, 'test.wrl')

def test_export_3js_facets():
    print('reading...')
    _, (indices, vertices, _) = read('../Kappa3-CanalChange/v3d_ljkcs/LJKCS05M/LJKCS05M-solid-body-zoff.v3d')
    print(indices[:10])
    print(vertices[:10])
    print(indices[-10:])
    print(vertices[-10:])
    with open('vertices.txt', 'w') as fp:
        fp.write(',\n'.join('\t\t\t\t\tnew THREE.Vector3(%.3f, %.3f, %.3f)' % tuple(v) for v in vertices))
    with open('indices.txt', 'w') as fp:
        fp.write(',\n'.join('\t\t\t\t\tnew THREE.Face3(%d, %d, %d)' % tuple(i) for i in indices))
    print('Done!')

if __name__ == '__main__':
    test()
    #test_export_wrl()
    #test_export_3js_facets()
