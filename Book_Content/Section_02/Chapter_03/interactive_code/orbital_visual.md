:::{code-cell} python
:tags: ["remove-input"]
:label: orbital_combination_final_fix
from IPython.display import HTML, display
import uuid

def create_static_math_orbital_widget():
    uid = "orb_fix_" + uuid.uuid4().hex[:8]
    
    html_template = r"""
    <div id="ID_container" style="font-family: sans-serif; max-width: 800px; margin: 10px auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px; text-align: center; background-color: #ffffff; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
        <h4 style="color: #333; margin-bottom: 5px;">Constructing Real Orbitals from Complex Pairs</h4>
        <p style="font-size: 13px; color: #666; margin-bottom: 20px;">
            Linear combinations transform imaginary "donut" solutions into directional lobes.
        </p>
        
        <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 20px; flex-wrap: nowrap;">
            <div style="border: 1px solid #e1e4e8; padding: 10px; border-radius: 8px; background-color: #f8f9fa; flex: 1; min-width: 180px;">
                <span style="font-weight: bold; display: block; margin-bottom: 8px; font-size: 0.85em;">p-orbitals ($|m_l|=1$)</span>
                <div style="display: flex; gap: 5px; justify-content: center;">
                    <button id="ID_btn_p_comp" style="cursor: pointer; padding: 6px 10px; border-radius: 4px; border: 1px solid #ccc; font-size: 0.85em; white-space: nowrap;">Complex</button>
                    <button id="ID_btn_px" style="cursor: pointer; padding: 6px 10px; border-radius: 4px; background-color: #4A90E2; color: white; border: 1px solid #2e6da4; font-size: 0.85em; white-space: nowrap;">Real $p_x$</button>
                </div>
            </div>
            <div style="border: 1px solid #e1e4e8; padding: 10px; border-radius: 8px; background-color: #f8f9fa; flex: 1.2; min-width: 220px;">
                <span style="font-weight: bold; display: block; margin-bottom: 8px; font-size: 0.85em;">d-orbitals ($|m_l|=2$)</span>
                <div style="display: flex; gap: 5px; justify-content: center;">
                    <button id="ID_btn_d_comp" style="cursor: pointer; padding: 6px 10px; border-radius: 4px; border: 1px solid #ccc; font-size: 0.85em; white-space: nowrap;">Complex</button>
                    <button id="ID_btn_dx2" style="cursor: pointer; padding: 6px 10px; border-radius: 4px; border: 1px solid #ccc; font-size: 0.85em; white-space: nowrap;">Real $d_{x^2-y^2}$</button>
                </div>
            </div>
        </div>

        <div id="ID_math_area" style="background-color: #fdfdfd; border: 1px dashed #ccc; border-radius: 6px; padding: 10px; margin-bottom: 15px; min-height: 80px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div id="ID_math_p_comp" class="ID_math_item" style="display:none; font-size: 1.2em;">$|Y_{1,\pm 1}| \text{ (Complex Donuts)}$</div>
            <div id="ID_math_px" class="ID_math_item" style="display:block; font-size: 1.2em;">$p_x = \frac{1}{\sqrt{2}} (Y_{1,1} + Y_{1,-1})$</div>
            <div id="ID_math_d_comp" class="ID_math_item" style="display:none; font-size: 1.2em;">$|Y_{2,\pm 2}| \text{ (Complex Donuts)}$</div>
            <div id="ID_math_dx2" class="ID_math_item" style="display:none; font-size: 1.2em;">$d_{x^2-y^2} = \frac{1}{\sqrt{2}} (Y_{2,2} + Y_{2,-2})$</div>
        </div>

        <canvas id="ID_canvas" width="500" height="350" style="background-color: #000; border-radius: 8px;"></canvas>
        
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script>
            (function() {
                const canvas = document.getElementById('ID_canvas');
                const btnPComp = document.getElementById('ID_btn_p_comp');
                const btnPx = document.getElementById('ID_btn_px');
                const btnDComp = document.getElementById('ID_btn_d_comp');
                const btnDx2 = document.getElementById('ID_btn_dx2');
                
                let scene, camera, renderer, mesh, mode = 'px';

                function getR(theta, phi) {
                    if (mode === 'p_comp') return Math.abs(Math.sin(theta));
                    if (mode === 'px') return Math.abs(Math.sin(theta) * Math.cos(phi));
                    if (mode === 'd_comp') return Math.abs(Math.pow(Math.sin(theta), 2));
                    if (mode === 'dx2') return Math.abs(Math.pow(Math.sin(theta), 2) * Math.cos(2*phi));
                    return 1;
                }

                function createMesh() {
                    if(mesh) scene.remove(mesh);
                    const geometry = new THREE.SphereGeometry(1, 100, 100);
                    const pos = geometry.attributes.position;
                    const v = new THREE.Vector3();
                    for (let i = 0; i < pos.count; i++) {
                        v.fromBufferAttribute(pos, i);
                        let r_orig = v.length();
                        let theta = Math.acos(v.z / r_orig);
                        let phi = Math.atan2(v.y, v.x);
                        let r = getR(theta, phi);
                        v.multiplyScalar(r * 2.5 + 0.1); 
                        pos.setXYZ(i, v.x, v.y, v.z);
                    }
                    pos.needsUpdate = true;
                    geometry.computeVertexNormals();
                    mesh = new THREE.Mesh(geometry, new THREE.MeshNormalMaterial({ wireframe: true }));
                    scene.add(mesh);
                }

                function init() {
                    scene = new THREE.Scene();
                    camera = new THREE.PerspectiveCamera(50, 500/350, 0.1, 1000);
                    camera.position.set(4, 3, 5);
                    camera.lookAt(0,0,0);
                    renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
                    renderer.setSize(500, 350);
                    createMesh();
                    animate();
                }

                function update(m, activeMathId, btn) {
                    mode = m;
                    document.querySelectorAll('#ID_math_area .ID_math_item').forEach(el => el.style.display = 'none');
                    document.getElementById(activeMathId).style.display = 'block';

                    [btnPComp, btnPx, btnDComp, btnDx2].forEach(b => {
                        b.style.backgroundColor = '#efefef';
                        b.style.color = '#333';
                        b.style.border = '1px solid #ccc';
                    });
                    btn.style.backgroundColor = '#4A90E2';
                    btn.style.color = 'white';
                    btn.style.border = '1px solid #2e6da4';
                    
                    createMesh();
                }

                btnPComp.onclick = () => update('p_comp', 'ID_math_p_comp', btnPComp);
                btnPx.onclick = () => update('px', 'ID_math_px', btnPx);
                btnDComp.onclick = () => update('d_comp', 'ID_math_d_comp', btnDComp);
                btnDx2.onclick = () => update('dx2', 'ID_math_dx2', btnDx2);

                function animate() {
                    requestAnimationFrame(animate);
                    if(mesh) { mesh.rotation.y += 0.008; mesh.rotation.x += 0.003; }
                    renderer.render(scene, camera);
                }
                
                if (typeof THREE !== 'undefined') { init(); } 
                else { setTimeout(init, 800); }
            })();
        </script>
    </div>
    """
    return HTML(html_template.replace("ID_", uid + "_"))

display(create_static_math_orbital_widget())
:::