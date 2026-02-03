:::{code-cell} python
:tags: [remove-input]
:label: cylindrical_coordinates
from IPython.display import HTML, display

def create_js_cylindrical_plot():
    # Unique ID to prevent collisions with other interactive widgets on the same page
    unique_id = f"cyl_{uuid.uuid4().hex[:8]}" if 'uuid' in globals() else "cyl_coord_plot"
    
    html_code = f"""
    <div id="{unique_id}_container" style="font-family: 'Arial', sans-serif; max-width: 850px; margin: auto; border: 1px solid #ddd; padding: 20px; border-radius: 8px; background: #fff;">
        <h3 style="text-align: center; color: #333; margin-top: 0;">Interactive Cylindrical Coordinates (r, φ, z)</h3>
        
        <div id="{unique_id}_plot" style="width: 100%; height: 500px; min-height: 400px;"></div>
        
        <div style="background-color: #f4f7f9; padding: 20px; border-radius: 8px; border: 1px solid #e1e8ed; margin-top: 15px; display: block;">
            <div style="display: flex; gap: 25px; flex-wrap: wrap; margin-bottom: 15px;">
                
                <div style="flex: 1; min-width: 200px;">
                    <label style="font-weight: bold; display: block; margin-bottom: 5px;">Radius (r): <span class="r_val" style="color: blue;">10.0</span></label>
                    <input type="range" class="r_slider" min="0" max="20" step="0.5" value="10" style="width: 100%;">
                    <small style="color: #666; font-style: italic;">Distance from Z-axis</small>
                </div>
                
                <div style="flex: 1; min-width: 200px;">
                    <label style="font-weight: bold; display: block; margin-bottom: 5px;">Azimuthal (φ): <span class="phi_val" style="color: #008000;">45</span>°</label>
                    <input type="range" class="phi_slider" min="0" max="360" step="1" value="45" style="width: 100%;">
                    <small style="color: #666; font-style: italic;">Rotation in XY plane</small>
                </div>

                <div style="flex: 1; min-width: 200px;">
                    <label style="font-weight: bold; display: block; margin-bottom: 5px;">Height (z): <span class="z_val" style="color: #d10000;">10.0</span></label>
                    <input type="range" class="z_slider" min="-20" max="20" step="0.5" value="10" style="width: 100%;">
                    <small style="color: #666; font-style: italic;">Vertical position</small>
                </div>
            </div>

            <div style="padding-top: 10px; border-top: 1px solid #ddd; text-align: center; font-size: 18px; color: #444;">
                <span style="margin-right: 15px;">x = <b class="x_out">0.00</b></span>
                <span style="margin-right: 15px;">y = <b class="y_out">0.00</b></span>
                <span>z = <b class="z_out">0.00</b></span>
            </div>
        </div>

        <script>
            (function() {{
                const cont = document.getElementById('{unique_id}_container');
                
                function initPlot() {{
                    const rSlider = cont.querySelector('.r_slider');
                    const phiSlider = cont.querySelector('.phi_slider');
                    const zSlider = cont.querySelector('.z_slider');
                    
                    const rDisp = cont.querySelector('.r_val');
                    const phiDisp = cont.querySelector('.phi_val');
                    const zDisp = cont.querySelector('.z_val');
                    
                    const xOut = cont.querySelector('.x_out');
                    const yOut = cont.querySelector('.y_out');
                    const zOut = cont.querySelector('.z_out');

                    function getCoords(r, pDeg, z) {{
                        const pRad = pDeg * (Math.PI / 180);
                        return {{
                            x: r * Math.cos(pRad),
                            y: r * Math.sin(pRad),
                            z: z,
                            pRad
                        }};
                    }}

                    const axisLength = 20;
                    const traceAxes = {{
                        type: 'scatter3d',
                        mode: 'lines',
                        x: [-axisLength, axisLength, null, 0, 0, null, 0, 0],
                        y: [0, 0, null, -axisLength, axisLength, null, 0, 0],
                        z: [0, 0, null, 0, 0, null, -axisLength, axisLength],
                        line: {{ color: '#bbb', width: 2 }},
                        name: 'Axes',
                        hoverinfo: 'none'
                    }};

                    function makePhiArc(r, endAngle) {{
                        const n = 30;
                        const ax = [], ay = [], az = [];
                        for(let i=0; i<=n; i++) {{
                            const ang = (endAngle) * (i/n);
                            ax.push(r * Math.cos(ang));
                            ay.push(r * Math.sin(ang));
                            az.push(0);
                        }}
                        return {{x: ax, y: ay, z: az}};
                    }}

                    function createTraces() {{
                        const r = parseFloat(rSlider.value);
                        const p = parseFloat(phiSlider.value);
                        const z = parseFloat(zSlider.value);
                        const c = getCoords(r, p, z);

                        const vector = {{
                            type: 'scatter3d', mode: 'lines+markers',
                            x: [0, c.x], y: [0, c.y], z: [0, c.z],
                            line: {{color: 'blue', width: 8}},
                            marker: {{size: 4, color: 'blue'}},
                            name: 'Position'
                        }};

                        const radialLine = {{
                            type: 'scatter3d', mode: 'lines',
                            x: [0, c.x], y: [0, c.y], z: [0, 0],
                            line: {{color: 'blue', width: 4, dash: 'dot'}},
                            name: 'r projection'
                        }};

                        const heightLine = {{
                            type: 'scatter3d', mode: 'lines',
                            x: [c.x, c.x], y: [c.y, c.y], z: [0, c.z],
                            line: {{color: '#d10000', width: 5}},
                            name: 'z'
                        }};

                        const pArc = makePhiArc(r * 0.4, c.pRad);
                        const phiTrace = {{
                            type: 'scatter3d', mode: 'lines',
                            x: pArc.x, y: pArc.y, z: pArc.z,
                            line: {{color: '#008000', width: 5}},
                            name: 'φ'
                        }};

                        return [traceAxes, vector, radialLine, heightLine, phiTrace];
                    }}

                    const layout = {{
                        scene: {{
                            xaxis: {{range: [-20, 20], title: 'X'}},
                            yaxis: {{range: [-20, 20], title: 'Y'}},
                            zaxis: {{range: [-20, 20], title: 'Z'}},
                            aspectmode: 'cube',
                            camera: {{
                                eye: {{x: 1.6, y: 1.2, z: 1.0}},
                                up: {{x: 0, y: 0, z: 1}}
                            }}
                        }},
                        margin: {{t: 0, b: 0, l: 0, r: 0}},
                        showlegend: false,
                        hovermode: false
                    }};

                    Plotly.newPlot('{unique_id}_plot', createTraces(), layout, {{responsive: true, displayModeBar: false}});

                    function update() {{
                        const r = parseFloat(rSlider.value);
                        const p = parseFloat(phiSlider.value);
                        const z = parseFloat(zSlider.value);
                        const c = getCoords(r, p, z);

                        rDisp.innerText = r.toFixed(1);
                        phiDisp.innerText = p;
                        zDisp.innerText = z.toFixed(1);
                        xOut.innerText = c.x.toFixed(2);
                        yOut.innerText = c.y.toFixed(2);
                        zOut.innerText = c.z.toFixed(2);

                        Plotly.react('{unique_id}_plot', createTraces(), layout);
                    }}

                    rSlider.addEventListener('input', update);
                    phiSlider.addEventListener('input', update);
                    zSlider.addEventListener('input', update);
                }}

                if (typeof Plotly === 'undefined') {{
                    var script = document.createElement('script');
                    script.src = 'https://cdn.plot.ly/plotly-latest.min.js';
                    document.head.appendChild(script);
                    script.onload = initPlot;
                }} else {{
                    initPlot();
                }}
            }})();
        </script>
    </div>
    """
    import uuid
    return HTML(html_code)

display(create_js_cylindrical_plot())
:::