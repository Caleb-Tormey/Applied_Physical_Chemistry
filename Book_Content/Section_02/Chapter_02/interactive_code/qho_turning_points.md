:::{code-cell} python
:tags: ["remove-input"]
:label: interactive_qho_viz_refined
from IPython.display import HTML, display
import uuid

def create_qho_widget():
    unique_id = f"qho_{uuid.uuid4().hex[:8]}"
    html_code = fr"""
    <div id="{unique_id}_container" style="font-family: inherit; max-width: 800px; margin: 10px auto; padding: 10px; background: transparent;">
        <h4 style="text-align: center; color: #333;">QHO: Wavefunctions and Classical Turning Points</h4>
        <div style="display: flex; flex-direction: column; align-items: center; gap: 15px;">
            <svg id="{unique_id}_svg" width="600" height="350" viewBox="0 0 600 350" style="background: transparent;">
                <path id="{unique_id}_pot" d="" fill="none" stroke="#999" stroke-width="2" />
                
                <path id="{unique_id}_psi" d="" fill="rgba(74, 144, 226, 0.25)" stroke="#4A90E2" stroke-width="2.5" />
                
                <line id="{unique_id}_tp_left" x1="0" y1="0" x2="0" y2="300" stroke="#e74c3c" stroke-width="1.5" stroke-dasharray="4" />
                <line id="{unique_id}_tp_right" x1="0" y1="0" x2="0" y2="300" stroke="#e74c3c" stroke-width="1.5" stroke-dasharray="4" />
                
                <line x1="50" y1="300" x2="550" y2="300" stroke="#333" stroke-width="1.5" />
                <text x="270" y="325" fill="#666" font-size="12">Displacement (x)</text>
                <text id="{unique_id}_tp_label" x="215" y="345" fill="#e74c3c" font-size="11" font-weight="bold">Red Lines: Classical Turning Points</text>
            </svg>

            <div style="display: flex; gap: 20px; align-items: center; border-top: 1px solid #eee; padding-top: 15px; width: 100%; justify-content: center;">
                <span style="font-size: 14px;">Quantum Number <strong>v</strong>:</span>
                <input type="range" id="{unique_id}_v_slider" min="0" max="4" value="0" step="1" style="width: 250px; accent-color: #4A90E2;">
                <span id="{unique_id}_v_val" style="font-weight: bold; color: #4A90E2; font-size: 1.2em; min-width: 20px;">0</span>
            </div>
        </div>
        <script>
            (function() {{
                const vSlider = document.getElementById('{unique_id}_v_slider');
                const vVal = document.getElementById('{unique_id}_v_val');
                const psiPath = document.getElementById('{unique_id}_psi');
                const potPath = document.getElementById('{unique_id}_pot');
                const tpL = document.getElementById('{unique_id}_tp_left');
                const tpR = document.getElementById('{unique_id}_tp_right');

                const centerX = 300; 
                const baselineY = 300; 
                const k = 0.015; // Increased k for a narrower, steeper potential
                
                // Hermite Polynomials
                const hermite = [
                    (z) => 1,
                    (z) => 2 * z,
                    (z) => 4 * z * z - 2,
                    (z) => 8 * Math.pow(z, 3) - 12 * z,
                    (z) => 16 * Math.pow(z, 4) - 48 * z * z + 12
                ];

                function draw() {{
                    const v = parseInt(vSlider.value);
                    vVal.innerText = v;

                    // Calculate Energy Level
                    const energy = (v + 0.5) * 45; 
                    const tpX = Math.sqrt(energy / k);

                    // Draw Potential Curve
                    let pD = "";
                    for(let x=-200; x<=200; x+=2) {{
                        let y = baselineY - (k * x * x);
                        if (y < 20) y = 20; // Cap height
                        pD += (x === -200 ? "M" : "L") + (centerX + x) + " " + y;
                    }}
                    potPath.setAttribute('d', pD);

                    // Draw Wavefunction
                    let psiD = "";
                    const xRange = 180;
                    const spread = 25; // Controls the width of the Gaussian relative to the potential
                    
                    for(let x = -xRange; x <= xRange; x += 1) {{
                        const z = x / spread;
                        const hVal = hermite[v](z);
                        const gauss = Math.exp(-(z * z) / 2);
                        
                        // Scale amplitude for visibility per level
                        const norm = Math.sqrt(Math.pow(2, v) * 1); 
                        const amp = (hVal * gauss * 25) / norm;
                        
                        const plotX = centerX + x;
                        const plotY = (baselineY - energy) - amp;
                        
                        psiD += (x === -xRange ? "M" : "L") + plotX + " " + plotY;
                    }}
                    
                    // Close path to create a filled "ribbon" effect
                    psiD += ` L ${{centerX + xRange}} ${{baselineY - energy}} L ${{centerX - xRange}} ${{baselineY - energy}} Z`;
                    psiPath.setAttribute('d', psiD);

                    // Update Turning Point Indicators
                    tpL.setAttribute('x1', centerX - tpX); tpL.setAttribute('x2', centerX - tpX);
                    tpL.setAttribute('y1', baselineY - energy - 40); tpL.setAttribute('y2', baselineY);
                    
                    tpR.setAttribute('x1', centerX + tpX); tpR.setAttribute('x2', centerX + tpX);
                    tpR.setAttribute('y1', baselineY - energy - 40); tpR.setAttribute('y2', baselineY);
                }}

                vSlider.addEventListener('input', draw);
                draw();
            }})();
        </script>
    </div>
    """
    return HTML(html_code)

display(create_qho_widget())
:::