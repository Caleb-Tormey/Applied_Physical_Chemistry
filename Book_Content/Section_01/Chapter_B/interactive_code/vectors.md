:::{code-cell} python
:tags: ["remove-input"]
:label:interactive_vectors 
from IPython.display import HTML, display
import uuid

def create_vector_component_widget():
    unique_id = f"vec_{uuid.uuid4().hex[:8]}"
    
    # Using a raw f-string (fr) and double backslashes for best MathJax compatibility 
    # when injecting HTML into Jupyter.
    html_code = fr"""
    <div id="{unique_id}_container" style="font-family: 'Arial', sans-serif; max-width: 800px; margin: 20px auto; border: 1px solid #ddd; padding: 25px; border-radius: 12px; background: #fff; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        <h3 style="text-align: center; color: #2c3e50; margin-top: 0;">Interactive 2D Vector Components</h3>
        
        <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-around; gap: 30px;">
            <!-- SVG Vector Plot -->
            <div style="position: relative;">
                <svg id="{unique_id}_svg" width="320" height="320" viewBox="-110 -110 220 220" style="background: #fdfdfd; border: 1px solid #eee; border-radius: 8px;">
                    <!-- Grid Lines -->
                    <line x1="-100" y1="0" x2="100" y2="0" stroke="#ccc" stroke-width="1" />
                    <line x1="0" y1="-100" x2="0" y2="100" stroke="#ccc" stroke-width="1" />
                    
                    <!-- Angle Arc (Orange) -->
                    <path id="{unique_id}_angle_arc" d="" fill="rgba(243, 156, 18, 0.2)" stroke="#f39c12" stroke-width="2" />

                    <!-- X Component (Red) -->
                    <line id="{unique_id}_line_x" x1="0" y1="0" x2="60" y2="0" stroke="#e74c3c" stroke-width="4" marker-end="url(#{unique_id}_x_arr)" stroke-linecap="round" />
                    <!-- Y Component (Green) -->
                    <line id="{unique_id}_line_y" x1="60" y1="0" x2="60" y2="-60" stroke="#27ae60" stroke-width="4" stroke-dasharray="5,5" marker-end="url(#{unique_id}_y_arr)" stroke-linecap="round" />
                    
                    <!-- Resultant Vector (Blue) -->
                    <line id="{unique_id}_vector" x1="0" y1="0" x2="60" y2="-60" stroke="#2244b0" stroke-width="5" marker-end="url(#{unique_id}_arr)" stroke-linecap="round" />
                    
                    <!-- Arrowhead Definitions -->
                    <defs>
                        <!-- Resultant Arrow (Shrunk) -->
                        <marker id="{unique_id}_arr" markerWidth="5" markerHeight="3.5" refX="4.5" refY="1.75" orient="auto">
                            <polygon points="0 0, 5 1.75, 0 3.5" fill="#2244b0" />
                        </marker>
                        <!-- X Arrow -->
                        <marker id="{unique_id}_x_arr" markerWidth="6" markerHeight="4" refX="5" refY="2" orient="auto">
                            <polygon points="0 0, 6 2, 0 4" fill="#e74c3c" />
                        </marker>
                        <!-- Y Arrow -->
                        <marker id="{unique_id}_y_arr" markerWidth="6" markerHeight="4" refX="5" refY="2" orient="auto">
                            <polygon points="0 0, 6 2, 0 4" fill="#27ae60" />
                        </marker>
                    </defs>
                </svg>
                <div style="position: absolute; top: -20px; left: 50%; transform: translateX(-50%); font-size: 0.9em; color: #666; font-weight: bold;">
                    +Y
                </div>
                <div style="position: absolute; top: 50%; left: 102%; transform: translateY(-50%); font-size: 0.9em; color: #666; font-weight: bold;">
                    +X
                </div>
            </div>

            <!-- Controls -->
            <div style="flex: 1; min-width: 280px; background: #f8f9fa; padding: 20px; border-radius: 10px; border: 1px solid #e9ecef;">
                <div style="margin-bottom: 25px;">
                    <label style="font-weight: bold; color: #e74c3c; display: block; margin-bottom: 8px;">
                        X Component ($V_x$): <span id="{unique_id}_x_val" style="font-family: monospace;">60.0</span>
                    </label>
                    <input type="range" id="{unique_id}_x_slider" min="-100" max="100" step="1" value="60" style="width: 100%; cursor: pointer;">
                </div>
                
                <div style="margin-bottom: 25px;">
                    <label style="font-weight: bold; color: #27ae60; display: block; margin-bottom: 8px;">
                        Y Component ($V_y$): <span id="{unique_id}_y_val" style="font-family: monospace;">60.0</span>
                    </label>
                    <input type="range" id="{unique_id}_y_slider" min="-100" max="100" step="1" value="60" style="width: 100%; cursor: pointer;">
                </div>
                
                <div style="border-top: 2px solid #dee2e6; padding-top: 20px; font-size: 1.05em; line-height: 1.6;">
                    <div style="white-space: nowrap;">
                        $|\vec{{V}}| = \sqrt{{V_x^2 + V_y^2}} = $ <span id="{unique_id}_mag" style="color: #2244b0; font-weight: bold;">84.85</span>
                    </div>
                    <div style="white-space: nowrap; margin-top: 8px;">
                        $\theta = \tan^{{-1}}(V_y/V_x) = $ <span id="{unique_id}_angle" style="color: #f39c12; font-weight: bold;">45.0</span>°
                    </div>
                </div>
            </div>
        </div>
        
        <p style="font-size: 0.9em; color: #7f8c8d; margin-top: 20px; font-style: italic; text-align: center;">
            Note: In this 2D representation, $V_x$ acts as the "adjacent" side and $V_y$ as the "opposite" side of the right triangle.
        </p>

        <script>
            (function() {{
                const xSlider = document.getElementById('{unique_id}_x_slider');
                const ySlider = document.getElementById('{unique_id}_y_slider');
                const xDisp = document.getElementById('{unique_id}_x_val');
                const yDisp = document.getElementById('{unique_id}_y_val');
                const magDisp = document.getElementById('{unique_id}_mag');
                const angDisp = document.getElementById('{unique_id}_angle');
                
                const vectorLine = document.getElementById('{unique_id}_vector');
                const compXLine = document.getElementById('{unique_id}_line_x');
                const compYLine = document.getElementById('{unique_id}_line_y');
                const angleArc = document.getElementById('{unique_id}_angle_arc');

                function update() {{
                    const vx = parseFloat(xSlider.value);
                    const vy = parseFloat(ySlider.value);
                    
                    xDisp.innerText = vx.toFixed(1);
                    yDisp.innerText = vy.toFixed(1);
                    
                    const mag = Math.sqrt(vx*vx + vy*vy);
                    magDisp.innerText = mag.toFixed(2);
                    
                    let angleRad = Math.atan2(vy, vx);
                    let angleDeg = angleRad * (180 / Math.PI);
                    angDisp.innerText = angleDeg.toFixed(1);

                    // Update SVG (Y is inverted in SVG coordinate space)
                    vectorLine.setAttribute('x2', vx);
                    vectorLine.setAttribute('y2', -vy);
                    
                    compXLine.setAttribute('x2', vx);
                    
                    compYLine.setAttribute('x1', vx);
                    compYLine.setAttribute('x2', vx);
                    compYLine.setAttribute('y2', -vy);

                    // Update Angle Arc
                    const arcRadius = 25;
                    if (mag < 5) {{
                        angleArc.setAttribute('d', "");
                    }} else {{
                        // Calculate arc endpoint
                        const endX = arcRadius * Math.cos(angleRad);
                        const endY = -arcRadius * Math.sin(angleRad); // SVG inversion
                        
                        // Large arc flag is 1 if angle is > 180 degrees (but atan2 is -180 to 180)
                        const sweepFlag = vy > 0 ? 0 : 1;
                        const largeArcFlag = 0;

                        const d = `M ${{arcRadius}} 0 A ${{arcRadius}} ${{arcRadius}} 0 ${{largeArcFlag}} ${{sweepFlag}} ${{endX}} ${{endY}} L 0 0 Z`;
                        angleArc.setAttribute('d', d);
                    }}
                }}

                xSlider.addEventListener('input', update);
                ySlider.addEventListener('input', update);
                
                // Initial update and typesetting trigger
                update();
                
                // Trigger MathJax re-render for the injected content
                const triggerMath = () => {{
                    if (window.MathJax) {{
                        if (window.MathJax.typesetPromise) {{
                            window.MathJax.typesetPromise();
                        }} else if (window.MathJax.Hub && window.MathJax.Hub.Queue) {{
                            window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, '{unique_id}_container']);
                        }}
                    }}
                }};
                
                // Slight delay to ensure DOM is ready
                setTimeout(triggerMath, 100);
            }})();
        </script>
    </div>
    """
    return HTML(html_code)

display(create_vector_component_widget())
:::