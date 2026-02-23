:::{code-cell} python
:tags: ["remove-input"]
:label: spherical_harmonics_3d_fixed_v3
from IPython.display import HTML, display
import uuid

def create_spherical_harmonics_widget():
    # Use a standard string instead of an f-string to avoid {l} being interpreted as a Python variable
    unique_id = "sh_" + uuid.uuid4().hex[:8]
    
    html_template = """
    <div id="{uid}_container" style="font-family: inherit; max-width: 800px; margin: 10px auto; padding: 15px; border: 1px solid #eee; border-radius: 10px; text-align: center; background: #fff;">
        <h4 style="color: #333;">3D Orbital Shape Generator (Angular Part)</h4>
        <div style="margin-bottom: 15px; display: flex; justify-content: center; gap: 20px; align-items: center;">
            <div>
                <label style="font-size: 14px; font-weight: bold;">l (Angular): </label>
                <select id="{uid}_l_select" style="padding: 5px; border-radius: 4px;">
                    <option value="0">0 (s-orbital)</option>
                    <option value="1">1 (p-orbital)</option>
                    <option value="2">2 (d-orbital)</option>
                </select>
            </div>
            <div>
                <label style="font-size: 14px; font-weight: bold;">mₗ (Orientation): </label>
                <select id="{uid}_ml_select" style="padding: 5px; border-radius: 4px; min-width: 50px;"></select>
            </div>
        </div>
        <canvas id="{uid}_canvas" width="400" height="300" style="background: #111; border-radius: 8px; cursor: move;"></canvas>
        <p style="font-size: 12px; color: #666; margin-top: 10px; line-height: 1.4;">
            These 3D plots represent the angular part ($Y_{l,m_l}$) of the wavefunction.<br>
            The distance from the center represents the <b>magnitude</b> of the Spherical Harmonic.
        </p>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script>
            (function() {
                const canvas = document.getElementById('{uid}_canvas');
                const lSelect = document.getElementById('{uid}_l_select');
                const mlSelect = document.getElementById('{uid}_ml_select');
                
                let scene, camera, renderer, mesh;

                function getY(l_val, m_val, theta, phi) {
                    if (l_val === 0) return 1.0;
                    if (l_val === 1) {
                        if (m_val === 0) return Math.abs(Math.cos(theta));
                        return Math.abs(Math.sin(theta)); 
                    }
                    if (l_val === 2) {
                        if (m_val === 0) return Math.abs(0.5 * (3 * Math.pow(Math.cos(theta), 2) - 1));
                        if (Math.abs(m_val) === 1) return Math.abs(Math.sin(theta) * Math.cos(theta));
                        return Math.abs(Math.pow(Math.sin(theta), 2));
                    }
                    return 1.0;
                }

                function updateMLOptions() {
                    const currentL = parseInt(lSelect.value);
                    mlSelect.innerHTML = "";
                    for(let i = -currentL; i <= currentL; i++) {
                        let opt = document.createElement('option');
                        opt.value = i;
                        opt.text = i;
                        if(i === 0) opt.selected = true;
                        mlSelect.appendChild(opt);
                    }
                }

                function createGeometry() {
                    if(mesh) scene.remove(mesh);
                    
                    const l_active = parseInt(lSelect.value);
                    const m_active = parseInt(mlSelect.value) || 0;
                    
                    const geometry = new THREE.SphereGeometry(1, 128, 128);
                    const positions = geometry.attributes.position;
                    const vector = new THREE.Vector3();

                    for (let i = 0; i < positions.count; i++) {
                        vector.fromBufferAttribute(positions, i);
                        
                        let r_orig = vector.length();
                        let theta = Math.acos(vector.z / r_orig);
                        let phi = Math.atan2(vector.y, vector.x);
                        
                        let r_new = getY(l_active, m_active, theta, phi);
                        vector.multiplyScalar(r_new * 1.8 + 0.1); 
                        
                        positions.setXYZ(i, vector.x, vector.y, vector.z);
                    }
                    
                    positions.needsUpdate = true;
                    geometry.computeVertexNormals();
                    
                    const material = new THREE.MeshNormalMaterial({ 
                        wireframe: true,
                        transparent: true,
                        opacity: 0.8
                    });
                    mesh = new THREE.Mesh(geometry, material);
                    scene.add(mesh);
                }

                function init() {
                    scene = new THREE.Scene();
                    camera = new THREE.PerspectiveCamera(50, 400/300, 0.1, 1000);
                    camera.position.z = 5;
                    camera.position.y = 1;
                    camera.lookAt(0,0,0);

                    renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
                    renderer.setSize(400, 300);
                    renderer.setPixelRatio(window.devicePixelRatio);

                    updateMLOptions();
                    createGeometry();
                    animate();
                }

                lSelect.addEventListener('change', () => { 
                    updateMLOptions(); 
                    createGeometry(); 
                });
                
                mlSelect.addEventListener('change', createGeometry);
                
                function animate() {
                    requestAnimationFrame(animate);
                    if(mesh) {
                        mesh.rotation.y += 0.005;
                        mesh.rotation.x += 0.002;
                    }
                    renderer.render(scene, camera);
                }

                if (typeof THREE !== 'undefined') {
                    init();
                } else {
                    setTimeout(init, 500);
                }
            })();
        </script>
    </div>
    """
    return HTML(html_template.replace("{uid}", unique_id))

display(create_spherical_harmonics_widget())
:::