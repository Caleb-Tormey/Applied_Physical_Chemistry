:::{code-cell} python
:label: Derivative_Interactive
:tags: [remove-input]
from IPython.display import HTML, display
import random

def create_split_derivative_plot():
    # Unique ID to prevent conflicts in Jupyter
    plot_id = f"deriv_split_{random.randint(1000, 9999)}"
    
    html_code = f"""
    <div style="font-family: 'Arial', sans-serif; max-width: 800px; margin: auto; border: 1px solid #ddd; padding: 20px; border-radius: 8px;">
        <h3 style="text-align: center;">Derivative: Slope Mapper</h3>
        
        <div id="{plot_id}" style="width: 100%; height: 750px; background-color: #ffffff;"></div>
        
        <div style="background-color: #f4f4f4; padding: 15px; border-radius: 5px; margin-top: 10px;">
            <div style="margin-bottom: 10px;">
                <label style="font-weight: bold;">x value: <span id="x_val_{plot_id}" style="color: blue;">1.00</span></label>
                <input type="range" id="slider_{plot_id}" min="-3" max="3" step="0.1" value="1.0" style="width: 100%;">
            </div>
            <div style="display: flex; justify-content: space-around; text-align: center;">
                <div>Function Value f(x): <b><span id="fx_val_{plot_id}">...</span></b></div>
                <div>Slope Value f'(x): <b><span id="slope_val_{plot_id}" style="color: #d62728;">...</span></b></div>
            </div>
        </div>

        <script>
        (function() {{
            var divID = "{plot_id}";
            var sliderID = "slider_{plot_id}";
            var xTxtID = "x_val_{plot_id}";
            var fTxtID = "fx_val_{plot_id}";
            var slopeTxtID = "slope_val_{plot_id}";

            function init() {{
                // 1. Define Math Functions
                // f(x) = 2x^2
                function f(x) {{ return 2 * Math.pow(x, 2); }}
                
                // f'(x) = 4x
                function df(x) {{ return 4 * x; }}

                // 2. Generate Static Curves (Range -4 to 4)
                var xArr = [], yArr = [], dyArr = [];
                for(var i=-4.0; i<=4.0; i+=0.1) {{
                    xArr.push(i);
                    yArr.push(f(i));
                    dyArr.push(df(i));
                }}

                // 3. Initial State
                var startX = 1.0;
                var startY = f(startX);
                var startM = df(startX);

                // Helper: Get Tangent Line Data
                function getTan(cx, cy, m) {{
                    var length = 1.0; // How long the tangent line looks
                    return {{
                        x: [cx - length, cx + length],
                        y: [cy - (m*length), cy + (m*length)]
                    }};
                }}
                var tan = getTan(startX, startY, startM);

                // 4. Setup Traces
                
                // --- TOP PLOT (Function) ---
                var traceFx = {{
                    x: xArr, y: yArr, 
                    mode: 'lines', name: 'f(x) = 2x²',
                    line: {{color: '#1f77b4', width: 3}},
                    xaxis: 'x', yaxis: 'y'
                }};
                
                var tracePointTop = {{
                    x: [startX], y: [startY], 
                    mode: 'markers', name: 'Current Point',
                    marker: {{color: '#1f77b4', size: 10, line: {{color: 'white', width: 2}}}},
                    xaxis: 'x', yaxis: 'y', showlegend: false
                }};

                var traceTangent = {{
                    x: tan.x, y: tan.y, 
                    mode: 'lines', name: 'Tangent Slope',
                    line: {{color: '#d62728', width: 3}}, // RED TANGENT
                    xaxis: 'x', yaxis: 'y'
                }};

                // --- BOTTOM PLOT (Derivative) ---
                var traceDeriv = {{
                    x: xArr, y: dyArr, 
                    mode: 'lines', name: "f '(x) = 4x",
                    line: {{color: 'grey', width: 2, dash: 'dot'}},
                    xaxis: 'x', yaxis: 'y2'
                }};

                var tracePointBot = {{
                    x: [startX], y: [startM], 
                    mode: 'markers', name: 'Slope Value',
                    marker: {{color: '#d62728', size: 12}}, // RED DOT
                    xaxis: 'x', yaxis: 'y2', showlegend: false
                }};

                // 5. Layout with Explicit Subplots
                var layout = {{
                    height: 750,
                    margin: {{t: 50, b: 50, l: 60, r: 20}},
                    hovermode: 'closest',
                    showlegend: true,
                    legend: {{x: 0, y: 1.05, orientation: 'h'}},
                    
                    // --- TOP AXIS Definition ---
                    xaxis: {{
                        anchor: 'y', range: [-4, 4], zeroline: false
                    }},
                    yaxis: {{
                        domain: [0.55, 1], // Occupies top 45%
                        title: '<b>f(x) = 2x²</b>',
                        range: [-5, 35] // Fixed range so graph doesn't jump
                    }},
                    
                    // --- BOTTOM AXIS Definition ---
                    xaxis2: {{
                        anchor: 'y2', range: [-4, 4], title: 'x'
                    }},
                    yaxis2: {{
                        domain: [0, 0.40], // Occupies bottom 40%
                        title: "<b>f '(x) = 4x</b>",
                        range: [-16, 16] // Fixed range for derivative
                    }},
                    
                    annotations: [
                        {{
                            x: 0.5, y: 1.02, xref: 'paper', yref: 'paper',
                            text: 'Original Function (Parabola)', showarrow: false, font: {{size: 14}}
                        }},
                        {{
                            x: 0.5, y: 0.42, xref: 'paper', yref: 'paper',
                            text: 'Derivative Function (Linear)', showarrow: false, font: {{size: 14}}
                        }}
                    ]
                }};
                
                var config = {{responsive: true, displayModeBar: false}};

                // 6. Draw Plot
                Plotly.newPlot(divID, [traceFx, tracePointTop, traceTangent, traceDeriv, tracePointBot], layout, config)
                .then(function() {{
                     document.getElementById(xTxtID).innerText = startX.toFixed(2);
                     document.getElementById(fTxtID).innerText = startY.toFixed(2);
                     document.getElementById(slopeTxtID).innerText = startM.toFixed(2);
                }});

                // 7. Update Loop
                var slider = document.getElementById(sliderID);
                slider.oninput = function() {{
                    var val = parseFloat(this.value);
                    
                    var y = f(val);
                    var m = df(val);
                    var t = getTan(val, y, m);
                    
                    // Text Updates
                    document.getElementById(xTxtID).innerText = val.toFixed(2);
                    document.getElementById(fTxtID).innerText = y.toFixed(2);
                    document.getElementById(slopeTxtID).innerText = m.toFixed(2);
                    
                    // Plotly React (Efficient Update)
                    Plotly.react(divID, [
                        traceFx, // 0 (Static)
                        {{x: [val], y: [y], mode:'markers', marker: tracePointTop.marker, xaxis:'x', yaxis:'y'}}, // 1 Point Top
                        {{x: t.x, y: t.y, mode:'lines', line: traceTangent.line, xaxis:'x', yaxis:'y'}}, // 2 Tangent
                        traceDeriv, // 3 (Static)
                        {{x: [val], y: [m], mode:'markers', marker: tracePointBot.marker, xaxis:'x', yaxis:'y2'}} // 4 Point Bot
                    ], layout, config);
                }};
            }}

            // Load Lib
            if(typeof Plotly === 'undefined') {{
                var s = document.createElement('script');
                s.src = 'https://cdn.plot.ly/plotly-2.24.1.min.js';
                s.onload = init;
                document.head.appendChild(s);
            }} else {{
                init();
            }}
        }})();
        </script>
    </div>
    """
    return HTML(html_code)

create_split_derivative_plot()
:::