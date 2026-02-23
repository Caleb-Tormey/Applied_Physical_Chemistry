:::{code-cell} python
:tags: ["remove-input"]
:label: interactive_rotator_spacing_final
from IPython.display import HTML, display
import uuid

def create_rotator_spectrum_widget():
    unique_id = f"rot_spec_{uuid.uuid4().hex[:8]}"
    html_code = fr"""
    <div id="{unique_id}_container" style="font-family: inherit; max-width: 800px; margin: 10px auto; padding: 15px; background: transparent;">
        <h4 style="text-align: center; color: #333;">Rigid Rotator: Transitions and Spectral Spacing</h4>
        
        <div style="display: flex; flex-direction: row; align-items: flex-end; justify-content: center; gap: 60px; height: 320px; margin-bottom: 20px;">
            <div style="text-align: center;">
                <span style="font-size: 13px; color: #444; font-weight: bold;">Energy Levels ($E \propto J^2$)</span>
                <svg width="220" height="300" viewBox="0 0 220 300">
                    <line x1="20" y1="280" x2="180" y2="280" stroke="#000" stroke-width="2"/>
                    <g id="{unique_id}_levels_group"></g>
                    <path id="{unique_id}_transition_arrow" d="" stroke="#e74c3c" stroke-width="2.5" marker-end="url(#arrowhead)" fill="none" />
                    <defs>
                        <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="0" refY="3.5" orient="auto">
                            <polygon points="0 0, 10 3.5, 0 7" fill="#e74c3c" />
                        </marker>
                    </defs>
                </svg>
            </div>
            <div style="text-align: center;">
                <span style="font-size: 13px; color: #444; font-weight: bold;">Observed Spectrum ($\Delta E$)</span>
                <svg width="300" height="180" viewBox="0 0 300 180">
                    <line x1="20" y1="150" x2="280" y2="150" stroke="#333" stroke-width="2"/>
                    <text x="120" y="170" fill="#666" font-size="11">Frequency ($\nu$)</text>
                    <g id="{unique_id}_spectrum_group"></g>
                    <rect id="{unique_id}_active_peak" x="0" y="0" width="5" height="110" fill="#e74c3c" visibility="hidden" />
                </svg>
            </div>
        </div>

        <div style="display: flex; flex-direction: column; align-items: center; gap: 10px; border-top: 1px solid #eee; padding-top: 15px;">
            <div style="display: flex; align-items: center; gap: 15px;">
                <span style="font-size: 14px;">Select Transition: <strong>J</strong> = <span id="{unique_id}_J_val">0</span> $\rightarrow$ <span id="{unique_id}_J_next">1</span></span>
                <input type="range" id="{unique_id}_J_slider" min="0" max="3" value="0" step="1" style="width: 250px; accent-color: #4A90E2;">
            </div>
        </div>

        <script>
            (function() {{
                const JSlider = document.getElementById('{unique_id}_J_slider');
                const JVal = document.getElementById('{unique_id}_J_val');
                const JNext = document.getElementById('{unique_id}_J_next');
                const levelsGroup = document.getElementById('{unique_id}_levels_group');
                const transArrow = document.getElementById('{unique_id}_transition_arrow');
                const specGroup = document.getElementById('{unique_id}_spectrum_group');
                const activePeak = document.getElementById('{unique_id}_active_peak');
                const scale = 20; 

                function update() {{
                    const J = parseInt(JSlider.value);
                    JVal.innerText = J;
                    JNext.innerText = J + 1;
                    levelsGroup.innerHTML = "";
                    for (let i = 0; i <= 4; i++) {{
                        const y = 280 - (i * i * scale);
                        const isActive = (i === J || i === J+1);
                        const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
                        line.setAttribute("x1", 20); line.setAttribute("x2", 180);
                        line.setAttribute("y1", y); line.setAttribute("y2", y);
                        line.setAttribute("stroke", isActive ? "#4A90E2" : "#555");
                        line.setAttribute("stroke-width", isActive ? "3" : "1.5");
                        levelsGroup.appendChild(line);
                        const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
                        txt.setAttribute("x", 190); txt.setAttribute("y", y + 5);
                        txt.setAttribute("fill", isActive ? "#4A90E2" : "#666");
                        txt.setAttribute("font-size", "12px");
                        txt.textContent = "J=" + i;
                        levelsGroup.appendChild(txt);
                    }}
                    const yStart = 280 - (J * J * scale);
                    const yEnd = 280 - ((J+1) * (J+1) * scale);
                    transArrow.setAttribute("d", `M 100 ${{yStart - 5}} L 100 ${{yEnd + 10}}`);
                    specGroup.innerHTML = "";
                    for (let i = 0; i <= 3; i++) {{
                        const specX = 30 + ((2*i + 1) * 28);
                        const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
                        line.setAttribute("x1", specX); line.setAttribute("x2", specX);
                        line.setAttribute("y1", 150); line.setAttribute("y2", 40);
                        line.setAttribute("stroke", "#ccc"); line.setAttribute("stroke-width", "1.5"); line.setAttribute("stroke-dasharray", "2,2");
                        specGroup.appendChild(line);
                    }}
                    const activeX = 30 + ((2*J + 1) * 28);
                    activePeak.setAttribute("x", activeX - 2.5); activePeak.setAttribute("y", 40); activePeak.setAttribute("visibility", "visible");
                }}
                JSlider.addEventListener('input', update); update();
            }})();
        </script>
    </div>
    """
    return HTML(html_code)

display(create_rotator_spectrum_widget())
:::