:::{code-cell} python
:tags: ["remove-input"]
:label: interactive_pib_solutions_fixed
from IPython.display import HTML, display
import uuid

def create_pib_solutions_widget():
    unique_id = f"pib_sol_{uuid.uuid4().hex[:8]}"
    
    html_code = fr"""
    <div id="{unique_id}_container" style="font-family: inherit; max-width: 800px; margin: 10px auto; padding: 10px; background: transparent;">
        <h4 style="text-align: center; color: #333; margin-bottom: 20px;">The Allowed States: Wavefunction Solutions ($\psi_n$)</h4>
        
        <div style="display: flex; flex-direction: column; align-items: center; gap: 20px;">
            <svg id="{unique_id}_svg" width="600" height="320" viewBox="0 0 600 320" style="background: transparent;">
                <line x1="100" y1="40" x2="100" y2="280" stroke="#333" stroke-width="3" />
                <line x1="500" y1="40" x2="500" y2="280" stroke="#333" stroke-width="3" />
                
                <line x1="100" y1="160" x2="500" y2="160" stroke="#ccc" stroke-width="1" stroke-dasharray="2,2" />
                
                <text x="85" y="300" fill="#666" font-size="13">x = 0</text>
                <text x="485" y="300" fill="#666" font-size="13">x = L</text>

                <path id="{unique_id}_psi_path" d="" fill="none" stroke="#4A90E2" stroke-width="2.5" />
                
                <g id="{unique_id}_nodes_group"></g>
            </svg>

            <div style="display: flex; flex-direction: column; gap: 10px; padding: 15px; border-top: 1px solid #eee; width: 100%; align-items: center;">
                <div style="display: flex; align-items: center; gap: 15px;">
                    <span style="font-size: 14px; color: #555;">Quantum Number <strong>n</strong>:</span>
                    <input type="range" id="{unique_id}_n_slider" min="1" max="20" value="1" step="1" style="cursor: pointer; accent-color: #4A90E2; width: 300px;">
                    <span id="{unique_id}_n_val" style="font-weight: bold; color: #4A90E2; font-size: 1.2em; min-width: 30px;">1</span>
                </div>
                <div id="{unique_id}_node_count" style="font-size: 13px; color: #7f8c8d; font-style: italic;">
                    Nodes (excluding boundaries): 0
                </div>
            </div>

            <div style="max-width: 500px; font-size: 13px; color: #666; text-align: center; line-height: 1.4;">
                Notice that for any state $n$, there are exactly $n-1$ nodes. As $n$ increases, the wavelength decreases and the kinetic energy increases.
            </div>
        </div>

        <script>
            (function() {{
                const nSlider = document.getElementById('{unique_id}_n_slider');
                const nValDisplay = document.getElementById('{unique_id}_n_val');
                const nodeDisplay = document.getElementById('{unique_id}_node_count');
                const psiPath = document.getElementById('{unique_id}_psi_path');
                const nodesGroup = document.getElementById('{unique_id}_nodes_group');

                const L = 400; 
                const offsetX = 100;
                const centerY = 160; 
                const amp = 100;

                function update() {{
                    const n = parseInt(nSlider.value);
                    nValDisplay.innerText = n;
                    nodeDisplay.innerText = `Nodes (excluding boundaries): ${{n - 1}}`;

                    // Update Wavefunction
                    let psiD = "";
                    for (let x = 0; x <= L; x += 1) {{
                        const scaledX = x / L;
                        const val = Math.sin(n * Math.PI * scaledX);
                        const plotX = x + offsetX;
                        const plotY = centerY - (val * amp);

                        if (x === 0) {{
                            psiD += `M ${{plotX}} ${{plotY}} `;
                        }} else {{
                            psiD += `L ${{plotX}} ${{plotY}} `;
                        }}
                    }}
                    psiPath.setAttribute('d', psiD);

                    // Update Node Markers
                    nodesGroup.innerHTML = "";
                    if (n > 1) {{
                        for (let i = 1; i < n; i++) {{
                            const nodeX = offsetX + (i * (L / n));
                            const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
                            circle.setAttribute("cx", nodeX);
                            circle.setAttribute("cy", centerY);
                            circle.setAttribute("r", 4);
                            circle.setAttribute("fill", "#fff");
                            circle.setAttribute("stroke", "#4A90E2");
                            circle.setAttribute("stroke-width", "1.5");
                            nodesGroup.appendChild(circle);
                        }}
                    }}
                }}

                nSlider.addEventListener('input', update);
                update();
            }})();
        </script>
    </div>
    """
    return HTML(html_code)

display(create_pib_solutions_widget())
:::