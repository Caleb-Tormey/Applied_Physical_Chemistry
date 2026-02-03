:::{code-cell} python
:tags: ["remove-input"]
:label: spherical_cartesian_convert
from IPython.display import HTML, display

def create_js_spherical_plot():
    html_code = """
    <div style="font-family: 'Arial', sans-serif; max-width: 850px; margin: auto; border: 1px solid #ddd; padding: 20px; border-radius: 8px; background: #fff;">
        <h3 style="text-align: center; color: #333;">Interactive Spherical Coordinates (r, θ, φ)</h3>
        
        <div id="spherical_plot" style="width: 100%; height: 600px;"></div>
        
        <div style="background-color: #f4f7f9; padding: 20px; border-radius: 8px; border: 1px solid #e1e8ed;">
            <div style="display: flex; gap: 25px; flex-wrap: wrap; margin-bottom: 15px;">
                
                <div style="flex: 1; min-width: 220px;">
                    <label for="r_s_slider" style="font-weight: bold; display: block; margin-bottom: 5px;">Radius (r): <span id="r_s_val" style="color: blue;">10.0</span></label>
                    <input type="range" id="r_s_slider" min="0" max="20" step="0.5" value="10" style="width: 100%;">
                </div>
                
                <div style="flex: 1; min-width: 220px;">
                    <label for="theta_s_slider" style="font-weight: bold; display: block; margin-bottom: 5px;">Polar Angle (θ): <span id="theta_s_val" style="color: #d100d1;">45</span>°</label>
                    <input type="range" id="theta_s_slider" min="0" max="180" step="1" value="45" style="width: 100%;">
                    <small style="color: #666; font-style: italic;">Angle from Z-axis</small>
                </div>

                <div style="flex: 1; min-width: 220px;">
                    <label for="phi_s_slider" style="font-weight: bold; display: block; margin-bottom: 5px;">Azimuthal (φ): <span id="phi_s_val" style="color: #008000;">45</span>°</label>
                    <input type="range" id="phi_s_slider" min="0" max="360" step="1" value="45" style="width: 100%;">
                    <small style="color: #666; font-style: italic;">Rotation from X-axis</small>
                </div>
            </div>

            <div style="padding-top: 10px; border-top: 1px solid #ddd; text-align: center; font-size: 18px; color: #444;">
                <span style="margin-right: 15px;">x = <b id="x_s_out">0.00</b></span>
                <span style="margin-right: 15px;">y = <b id="y_s_out">0.00</b></span>
                <span>z = <b id="z_s_out">0.00</b></span>
            </div>
        </div>

        <script>
            if (typeof Plotly === 'undefined') {
                var script = document.createElement('script');
                script.src = 'https://cdn.plot.ly/plotly-latest.min.js';
                document.head.appendChild(script);
                script.onload = initSphericalPlot;
            } else {
                initSphericalPlot();
            }

            function initSphericalPlot() {
                const rSlider = document.getElementById('r_s_slider');
                const thetaSlider = document.getElementById('theta_s_slider');
                const phiSlider = document.getElementById('phi_s_slider');
                
                const rDisp = document.getElementById('r_s_val');
                const thetaDisp = document.getElementById('theta_s_val');
                const phiDisp = document.getElementById('phi_s_val');
                
                const xOut = document.getElementById('x_s_out');
                const yOut = document.getElementById('y_s_out');
                const zOut = document.getElementById('z_s_out');

                function getCoords(r, tDeg, pDeg) {
                    const tRad = tDeg * (Math.PI / 180);
                    const pRad = pDeg * (Math.PI / 180);
                    return {
                        x: r * Math.sin(tRad) * Math.cos(pRad),
                        y: r * Math.sin(tRad) * Math.sin(pRad),
                        z: r * Math.cos(tRad),
                        tRad, pRad
                    };
                }

                // --- Static Reference Frame (The Axes) ---
                const axisLength = 20;
                const traceAxes = {
                    type: 'scatter3d',
                    mode: 'lines',
                    x: [0, axisLength, null, 0, 0, null, 0, 0],
                    y: [0, 0, null, 0, axisLength, null, 0, 0],
                    z: [0, 0, null, 0, 0, null, 0, axisLength],
                    line: { color: '#bbb', width: 2 },
                    name: 'Axes',
                    hoverinfo: 'none'
                };

                // Helper for arcs
                function makeArc(r, startAngle, endAngle, plane, constantAngle) {
                    const n = 30;
                    const ax = [], ay = [], az = [];
                    for(let i=0; i<=n; i++) {
                        const ang = startAngle + (endAngle - startAngle) * (i/n);
                        if (plane === 'theta') {
                            // t varies, p is constant
                            ax.push(r * Math.sin(ang) * Math.cos(constantAngle));
                            ay.push(r * Math.sin(ang) * Math.sin(constantAngle));
                            az.push(r * Math.cos(ang));
                        } else {
                            // p varies, t is constant (90 deg for floor arc)
                            ax.push(r * Math.sin(constantAngle) * Math.cos(ang));
                            ay.push(r * Math.sin(constantAngle) * Math.sin(ang));
                            az.push(r * Math.cos(constantAngle));
                        }
                    }
                    return {x: ax, y: ay, z: az};
                }

                function createTraces() {
                    const r = parseFloat(rSlider.value);
                    const t = parseFloat(thetaSlider.value);
                    const p = parseFloat(phiSlider.value);
                    const c = getCoords(r, t, p);

                    // 1. Vector
                    const vector = {
                        type: 'scatter3d', mode: 'lines+markers',
                        x: [0, c.x], y: [0, c.y], z: [0, c.z],
                        line: {color: 'blue', width: 8},
                        marker: {size: 4, color: 'blue'},
                        name: 'r'
                    };

                    // 2. Projections
                    const shadow = {
                        type: 'scatter3d', mode: 'lines',
                        x: [0, c.x, c.x], y: [0, c.y, c.y], z: [0, 0, c.z],
                        line: {color: '#888', width: 3, dash: 'dash'},
                        name: 'Projection'
                    };

                    // 3. Theta Arc (Polar)
                    const tArc = makeArc(r * 0.4, 0, c.tRad, 'theta', c.pRad);
                    const thetaTrace = {
                        type: 'scatter3d', mode: 'lines',
                        x: tArc.x, y: tArc.y, z: tArc.z,
                        line: {color: '#d100d1', width: 5},
                        name: 'θ'
                    };

                    // 4. Phi Arc (Azimuthal)
                    const pArc = makeArc(r * 0.4, 0, c.pRad, 'phi', Math.PI/2);
                    const phiTrace = {
                        type: 'scatter3d', mode: 'lines',
                        x: pArc.x, y: pArc.y, z: pArc.z,
                        line: {color: '#008000', width: 5},
                        name: 'φ'
                    };

                    return [traceAxes, vector, shadow, thetaTrace, phiTrace];
                }

                const layout = {
                    scene: {
                        xaxis: {range: [-20, 20], showgrid: true, zeroline: true, title: 'X'},
                        yaxis: {range: [-20, 20], showgrid: true, zeroline: true, title: 'Y'},
                        zaxis: {range: [-20, 20], showgrid: true, zeroline: true, title: 'Z'},
                        aspectmode: 'cube',
                        camera: {
                            eye: {x: 1.6, y: 1.2, z: 1.0}, // Fixed angle for depth
                            up: {x: 0, y: 0, z: 1}
                        }
                    },
                    margin: {t: 0, b: 0, l: 0, r: 0},
                    showlegend: false,
                    hovermode: false
                };

                const config = {responsive: true, displayModeBar: false};

                Plotly.newPlot('spherical_plot', createTraces(), layout, config);

                function update() {
                    const r = parseFloat(rSlider.value);
                    const t = parseFloat(thetaSlider.value);
                    const p = parseFloat(phiSlider.value);
                    const c = getCoords(r, t, p);

                    rDisp.innerText = r.toFixed(1);
                    thetaDisp.innerText = t;
                    phiDisp.innerText = p;
                    xOut.innerText = c.x.toFixed(2);
                    yOut.innerText = c.y.toFixed(2);
                    zOut.innerText = c.z.toFixed(2);

                    Plotly.react('spherical_plot', createTraces(), layout);
                }

                [rSlider, thetaSlider, phiSlider].forEach(s => s.addEventListener('input', update));
            }
        </script>
    </div>
    """
    return HTML(html_code)

create_js_spherical_plot()
:::