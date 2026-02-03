:::{code-cell} python
:tags: ["remove-input"]
:label: vector_addition_code

from IPython.display import HTML, display
import uuid

def create_vector_addition_widget():
    unique_id = f"vec_add_{uuid.uuid4().hex[:8]}"
    
    html_code = fr"""
    <div id="{unique_id}_container" style="font-family: 'Arial', sans-serif; max-width: 900px; margin: 20px auto; border: 1px solid #ddd; padding: 25px; border-radius: 12px; background: #fff; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        <h3 style="text-align: center; color: #2c3e50; margin-top: 0;">Interactive Vector Addition ($\vec{{A}} + \vec{{B}} = \vec{{R}}$)</h3>
        
        <div style="display: flex; flex-wrap: wrap; align-items: flex-start; justify-content: space-around; gap: 30px; margin-top: 20px;">
            <div style="position: relative;">
                <svg width="400" height="400" viewBox="-210 -210 420 420" style="background: #fdfdfd; border: 1px solid #eee; border-radius: 8px;">
                    <defs>
                        <pattern id="{unique_id}_grid" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M 20 0 L 0 0 0 20" fill="none" stroke="#f0f0f0" stroke-width="1"/></pattern>
                        <marker id="{unique_id}_arr_a" markerWidth="6" markerHeight="4" refX="5" refY="2" orient="auto"><polygon points="0 0, 6 2, 0 4" fill="#e74c3c" /></marker>
                        <marker id="{unique_id}_arr_b" markerWidth="6" markerHeight="4" refX="5" refY="2" orient="auto"><polygon points="0 0, 6 2, 0 4" fill="#27ae60" /></marker>
                        <marker id="{unique_id}_arr_r" markerWidth="5" markerHeight="3.5" refX="4.5" refY="1.75" orient="auto"><polygon points="0 0, 5 1.75, 0 3.5" fill="#2244b0" /></marker>
                    </defs>
                    <rect x="-210" y="-210" width="420" height="420" fill="url(#{unique_id}_grid)" />
                    <line x1="-200" y1="0" x2="200" y2="0" stroke="#ccc" stroke-width="1.5" />
                    <line x1="0" y1="-200" x2="0" y2="200" stroke="#ccc" stroke-width="1.5" />
                    <line id="{unique_id}_vec_a" x1="0" y1="0" x2="60" y2="-40" stroke="#e74c3c" stroke-width="4" marker-end="url(#{unique_id}_arr_a)" />
                    <line id="{unique_id}_vec_b" x1="60" y1="-40" x2="100" y2="-120" stroke="#27ae60" stroke-width="4" marker-end="url(#{unique_id}_arr_b)" />
                    <line id="{unique_id}_vec_r" x1="0" y1="0" x2="100" y2="-120" stroke="#2244b0" stroke-width="4" marker-end="url(#{unique_id}_arr_r)" stroke-opacity="0.6" />
                </svg>
                <div style="position: absolute; top: -10px; left: 50%; transform: translateX(-50%); font-weight: bold; color: #666;">+Y</div>
                <div style="position: absolute; top: 50%; right: -25px; transform: translateY(-50%); font-weight: bold; color: #666;">+X</div>
            </div>

            <div style="flex: 1; min-width: 300px; display: flex; flex-direction: column; gap: 15px;">
                <div style="background: #fff5f5; padding: 15px; border-radius: 8px; border: 1px solid #feb2b2;">
                    <h4 style="margin: 0 0 10px 0; color: #c53030;">Vector $\vec{{A}}$ (Red)</h4>
                    <div style="display: flex; gap: 10px; align-items: center;"><span>$A_x$:</span><input type="range" id="{unique_id}_ax" min="-100" max="100" value="60" style="flex: 1;"><span id="{unique_id}_ax_val">60</span></div>
                    <div style="display: flex; gap: 10px; align-items: center;"><span>$A_y$:</span><input type="range" id="{unique_id}_ay" min="-100" max="100" value="40" style="flex: 1;"><span id="{unique_id}_ay_val">40</span></div>
                </div>
                <div style="background: #f0fff4; padding: 15px; border-radius: 8px; border: 1px solid #9ae6b4;">
                    <h4 style="margin: 0 0 10px 0; color: #276749;">Vector $\vec{{B}}$ (Green)</h4>
                    <div style="display: flex; gap: 10px; align-items: center;"><span>$B_x$:</span><input type="range" id="{unique_id}_bx" min="-100" max="100" value="40" style="flex: 1;"><span id="{unique_id}_bx_val">40</span></div>
                    <div style="display: flex; gap: 10px; align-items: center;"><span>$B_y$:</span><input type="range" id="{unique_id}_by" min="-100" max="100" value="-80" style="flex: 1;"><span id="{unique_id}_by_val">-80</span></div>
                </div>
                <div style="background: #ebf8ff; padding: 15px; border-radius: 8px; border: 1px solid #bee3f8;">
                    <h4 style="margin: 0 0 10px 0; color: #2b6cb0;">Resultant $\vec{{R}} = \vec{{A}} + \vec{{B}}$</h4>
                    <div style="font-size: 1.1em; line-height: 1.6;">
                        $R_x = A_x + B_x = $ <b id="{unique_id}_rx">100</b><br>
                        $R_y = A_y + B_y = $ <b id="{unique_id}_ry">-40</b><br>
                        Magnitude $|\vec{{R}}| = $ <b id="{unique_id}_mag" style="color: #2244b0;">107.7</b>
                    </div>
                </div>
            </div>
        </div>

        <script>
            (function() {{
                const axS = document.getElementById('{unique_id}_ax'), ayS = document.getElementById('{unique_id}_ay');
                const bxS = document.getElementById('{unique_id}_bx'), byS = document.getElementById('{unique_id}_by');
                const axV = document.getElementById('{unique_id}_ax_val'), ayV = document.getElementById('{unique_id}_ay_val');
                const bxV = document.getElementById('{unique_id}_bx_val'), byV = document.getElementById('{unique_id}_by_val');
                const rxD = document.getElementById('{unique_id}_rx'), ryD = document.getElementById('{unique_id}_ry'), magD = document.getElementById('{unique_id}_mag');
                const vA = document.getElementById('{unique_id}_vec_a'), vB = document.getElementById('{unique_id}_vec_b'), vR = document.getElementById('{unique_id}_vec_r');

                function update() {{
                    const ax = parseFloat(axS.value), ay = parseFloat(ayS.value);
                    const bx = parseFloat(bxS.value), by = parseFloat(byS.value);
                    axV.innerText = ax; ayV.innerText = ay; bxV.innerText = bx; byV.innerText = by;
                    const rx = ax + bx, ry = ay + by, mag = Math.sqrt(rx*rx + ry*ry);
                    rxD.innerText = rx; ryD.innerText = ry; magD.innerText = mag.toFixed(1);
                    vA.setAttribute('x2', ax); vA.setAttribute('y2', -ay);
                    vB.setAttribute('x1', ax); vB.setAttribute('y1', -ay);
                    vB.setAttribute('x2', ax + bx); vB.setAttribute('y2', -(ay + by));
                    vR.setAttribute('x2', rx); vR.setAttribute('y2', -ry);
                }}
                [axS, ayS, bxS, byS].forEach(s => s.oninput = update); update();
                if (window.MathJax && window.MathJax.typesetPromise) window.MathJax.typesetPromise();
            }})();
        </script>
    </div>
    """
    return HTML(html_code)

display(create_vector_addition_widget())
:::