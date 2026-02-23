:::{code-cell} python
:tags: ["remove-input"]
:label: interactive_pib_clean
from IPython.display import HTML, display
import uuid

def create_pib_clean_widget():
    unique_id = f"pib_{uuid.uuid4().hex[:8]}"
    
    html_code = fr"""
    <div id="{unique_id}_container" style="font-family: inherit; max-width: 800px; margin: 10px auto; padding: 10px; background: transparent;">
        <h4 style="text-align: center; color: #333; margin-bottom: 20px;">Interactive Particle in a Box: $\psi_n$ and $|\psi_n|^2$</h4>
        
        <div style="display: flex; flex-direction: column; align-items: center; gap: 20px;">
            <svg id="{unique_id}_svg" width="600" height="320" viewBox="0 0 600 320" style="background: transparent;">
                <line x1="100" y1="40" x2="100" y2="280" stroke="#333" stroke-width="3" />
                <line x1="500" y1="40" x2="500" y2="280" stroke="#333" stroke-width="3" />
                
                <line x1="100" y1="280" x2="500" y2="280" stroke="#ccc" stroke-width="1" />
                
                <text x="85" y="300" fill="#666" font-size="13">x = 0</text>
                <text x="485" y="300" fill="#666" font-size="13">x = L</text>

                <path id="{unique_id}_prob_path" d="" fill="rgba(230, 126, 34, 0.15)" stroke="#E67E22" stroke-width="2" />
                
                <path id="{unique_id}_psi_path" d="" fill="none" stroke="#4A90E2" stroke-width="2.5" />
                
                <line x1="300" y1="40" x2="300" y2="280" stroke="#e74c3c" stroke-width="1.5" stroke-dasharray="6,4" opacity="0.7" />
                <text x="305" y="55" fill="#e74c3c" font-size="11" font-style="italic">⟨x⟩ = L/2</text>
            </svg>

            <div style="display: flex; gap: 25px; align-items: center; padding: 15px; border-top: 1px solid #eee; width: 100%; justify-content: center;">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 14px; color: #555;">Quantum Number <strong>n</strong>:</span>
                    <input type="range" id="{unique_id}_n_slider" min="1" max="6" value="1" step="1" style="cursor: pointer; accent-color: #4A90E2; width: 200px;">
                    <span id="{unique_id}_n_val" style="font-weight: bold; color: #4A90E2; min-width: 20px;">1</span>
                </div>
            </div>

            <div style="display: flex; gap: 40px; font-size: 12px; color: #666;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <div style="width: 12px; height: 12px; background: #4A90E2; border-radius: 2px;"></div> <span>Wavefunction $\psi_n$</span>
                </div>
                <div style="display: flex; align-items: center; gap: 8px;">
                    <div style="width: 12px; height: 12px; background: rgba(230, 126, 34, 0.3); border: 1px solid #E67E22; border-radius: 2px;"></div> <span>Probability Density $|\psi_n|^2$</span>
                </div>
            </div>
        </div>

        <script>
            (function() {{
                const nSlider = document.getElementById('{unique_id}_n_slider');
                const nValDisplay = document.getElementById('{unique_id}_n_val');
                const psiPath = document.getElementById('{unique_id}_psi_path');
                const probPath = document.getElementById('{unique_id}_prob_path');

                const L = 400; 
                const offsetX = 100;
                const centerY = 160; 
                const amp = 90;

                function update() {{
                    const n = parseInt(nSlider.value);
                    nValDisplay.innerText = n;

                    let psiD = "";
                    let probD = "";

                    for (let x = 0; x <= L; x += 1) {{
                        const scaledX = x / L;
                        const val = Math.sin(n * Math.PI * scaledX);
                        
                        const plotX = x + offsetX;
                        const plotY_psi = centerY - (val * amp);
                        const plotY_prob = 280 - (val * val * amp * 1.6); 

                        if (x === 0) {{
                            psiD += `M ${{plotX}} ${{plotY_psi}} `;
                            probD += `M ${{plotX}} ${{plotY_prob}} `;
                        }} else {{
                            psiD += `L ${{plotX}} ${{plotY_psi}} `;
                            probD += `L ${{plotX}} ${{plotY_prob}} `;
                        }}
                    }}
                    
                    // Close the probability shaded area path
                    let probPathData = probD + `L ${{offsetX + L}} 280 L ${{offsetX}} 280 Z`;

                    psiPath.setAttribute('d', psiD);
                    probPath.setAttribute('d', probPathData);
                }}

                nSlider.addEventListener('input', update);
                update();
            }})();
        </script>
    </div>
    """
    return HTML(html_code)

display(create_pib_clean_widget())
:::