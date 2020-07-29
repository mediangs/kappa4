'''
Created on 2014. 4. 4.

@author: jongki
'''

def java_scrip_header(fi):
    
    
    header = '''
<html>
    <head>
        <title>My first Three.js app</title>
        <style>canvas { width: 100%; height: 100% }</style>
    </head>
    <body>
        <script src="http://threejs.org/build/three.min.js"></script>
        <script src="http://threejs.org/examples/js/controls/OrbitControls.js"></script>
        <script>
            var scene = new THREE.Scene();
            var camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
    
            var renderer = new THREE.WebGLRenderer();
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.body.appendChild(renderer.domElement);

        '''
    with open(fi,'w') as f:
        f.write(header)
    print('  === Java scrip export header')
    
def java_scrip_footer(fi):
    footer = ''' 
            camera.position.z = 100;

            function render() {
                //requestAnimationFrame(render);
                //line.rotation.x += 0.1;
                //line.rotation.y += 0.1;
                renderer.render(scene, camera);
            };

            controls = new THREE.OrbitControls( camera, renderer.domElement );
            controls.center.set( 0, 0, 0);
            controls.addEventListener( 'change', render );
            animate();
            function animate() {
                requestAnimationFrame( animate );
                controls.update();
                render();
            }
        </script>
    </body>
</html>

    '''
    with open(fi,'a') as f:
        f.write(footer)

    print('  === Java scrip export footer')
                
def java_scrip_export(fi, var_name, color, vs):
    
    with open(fi,'a') as f:
        f.write('\n')
        f.write( 'var %s = new THREE.Geometry(); \n' % var_name )
        for v in vs :
            f.write( '%s.vertices.push( new THREE.Vector3( %f, %f, %f ) ); \n' % (var_name, v[0], v[1], v[2] ) )
        f.write( 'scene.add(new THREE.Line( %s, new THREE.LineBasicMaterial(%s) )); \n' % (var_name, color) )
    print('  === Java scrip export body %s') % var_name
    '''    
    with open(fi,'a') as f:
        f.write('\n')
        f.write( '%s\n' % var_name )
        for v in vs :
            f.write( '[%f, %f, %f] ' % (v[0], v[1], v[2] ) )
    print '  === Java scrip export body %s' % var_name
    '''
        