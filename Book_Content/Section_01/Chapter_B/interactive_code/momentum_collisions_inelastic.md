:::{code-cell} python
:tags: ["remove-input"]
:label: interactive_collision
from IPython.display import HTML, display
import uuid

def create_collision_widget():
    unique_id = f"coll_{uuid.uuid4().hex[:8]}"
    
    html_code = fr"""
    <div id="{unique_id}_container" style="font-family: 'Arial', sans-serif; max-width: 800px; margin: 20px auto; border: 1px solid #ddd; padding: 25px; border-radius: 12px; background: #fff; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        <h3 style="text-align: center; color: #2c3e50; margin-top: 0;">Inelastic Collision Simulator</h3>
        <p style="text-align: center; font-size: 0.9em; color: #666;">Observe how Momentum is conserved while Kinetic Energy is lost when the blocks stick.</p>
        
        <div style="text-align: center; background: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
            <svg id="{unique_id}_svg" width="600" height="120" viewBox="0 0 600 120">
                <line x1="0" y1="100" x2="600" y2="100" stroke="#34495e" stroke-width="2" />
                <rect id="{unique_id}_block1" x="50" y="60" width="40" height="40" fill="#e74c3c" rx="2" />
                <rect id="{unique_id}_block2" x="400" y="60" width="40" height="40" fill="#3498db" rx="2" />
                <text id="{unique_id}_v1_label" x="70" y="50" text-anchor="middle" font-size="12" font-weight="bold">v=2</text>
                <text id="{unique_id}_v2_label" x="420" y="50" text-anchor="middle" font-size="12" font-weight="bold">v=0</text>
            </svg>
        </div>

        <div style="display: flex; justify-content: space-around; gap: 20px;">
            <div style="flex: 1; text-align: center; border-right: 1px solid #eee;">
                <h4 style="margin: 0 0 10px 0; color: #2c3e50;">Momentum ($p$)</h4>
                <div style="font-size: 1.2em; font-family: monospace;" id="{unique_id}_p_val">80.0</div>
                <div style="width: 100%; background: #eee; height: 10px; border-radius: 5px; margin-top: 5px;">
                    <div id="{unique_id}_p_bar" style="width: 100%; background: #9b59b6; height: 100%; border-radius: 5px;"></div>
                </div>
            </div>
            <div style="flex: 1; text-align: center;">
                <h4 style="margin: 0 0 10px 0; color: #2c3e50;">Kinetic Energy ($KE$)</h4>
                <div style="font-size: 1.2em; font-family: monospace;" id="{unique_id}_ke_val">80.0</div>
                <div style="width: 100%; background: #eee; height: 10px; border-radius: 5px; margin-top: 5px;">
                    <div id="{unique_id}_ke_bar" style="width: 100%; background: #f1c40f; height: 100%; border-radius: 5px;"></div>
                </div>
            </div>
        </div>

        <div style="text-align: center; margin-top: 25px;">
            <button id="{unique_id}_reset" style="padding: 10px 20px; cursor: pointer; border-radius: 5px; border: none; background: #34495e; color: white; font-weight: bold;">Reset & Run Collision</button>
        </div>

        <script>
            (function() {{
                const b1 = document.getElementById('{unique_id}_block1');
                const b2 = document.getElementById('{unique_id}_block2');
                const v1L = document.getElementById('{unique_id}_v1_label');
                const v2L = document.getElementById('{unique_id}_v2_label');
                const pVal = document.getElementById('{unique_id}_p_val');
                const keVal = document.getElementById('{unique_id}_ke_val');
                const pBar = document.getElementById('{unique_id}_p_bar');
                const keBar = document.getElementById('{unique_id}_ke_bar');
                const resetBtn = document.getElementById('{unique_id}_reset');

                let pos1 = 50, pos2 = 400;
                let v1 = 1.0, v2 = 0; // Speed set to 1.0 for slower movement
                const m1 = 40, m2 = 40;
                let animationId;

                function updateDisplay(currentV1, currentV2) {{
                    const pTotal = (m1 * currentV1) + (m2 * currentV2);
                    const keTotal = (0.5 * m1 * currentV1**2) + (0.5 * m2 * currentV2**2);
                    
                    pVal.innerText = pTotal.toFixed(1);
                    keVal.innerText = keTotal.toFixed(1);
                    keBar.style.width = (keTotal / 20 * 100) + "%";
                }}

                function animate() {{
                    if (pos1 + 40 >= pos2) {{
                        const vFinal = (m1 * v1 + m2 * v2) / (m1 + m2);
                        v1 = vFinal;
                        v2 = vFinal;
                    }}
                    
                    pos1 += v1;
                    pos2 += v2;
                    
                    b1.setAttribute('x', pos1);
                    b2.setAttribute('x', pos2);
                    v1L.setAttribute('x', pos1 + 20);
                    v2L.setAttribute('x', pos2 + 20);
                    v1L.innerText = "v=" + v1.toFixed(2);
                    v2L.innerText = "v=" + v2.toFixed(2);
                    
                    updateDisplay(v1, v2);

                    if (pos2 < 550) {{
                        animationId = requestAnimationFrame(animate);
                    }}
                }}

                resetBtn.addEventListener('click', () => {{
                    cancelAnimationFrame(animationId);
                    pos1 = 50; pos2 = 400;
                    v1 = 1.0; v2 = 0;
                    animate();
                }});
                
                updateDisplay(v1, v2);
            }})();
        </script>
    </div>
    """
    return HTML(html_code)

display(create_collision_widget())
:::