:::{code-cell} python
:tags: ["remove-input"]
:label: interactive_spring_energy
from IPython.display import HTML, display
import uuid

def create_spring_energy_widget():
    unique_id = f"spring_{uuid.uuid4().hex[:8]}"
    
    html_code = fr"""
    <div id="{unique_id}_container" style="font-family: 'Arial', sans-serif; max-width: 800px; margin: 20px auto; border: 1px solid #ddd; padding: 25px; border-radius: 12px; background: #fff; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        <h3 style="text-align: center; color: #2c3e50; margin-top: 0;">Energy Exchange: Ideal Spring Oscillator</h3>
        
        <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-around; gap: 20px;">
            <div style="text-align: center;">
                <svg id="{unique_id}_svg" width="300" height="200" viewBox="0 0 300 200" style="background: #fdfdfd; border: 1px solid #eee; border-radius: 8px;">
                    <rect x="0" y="50" width="10" height="100" fill="#95a5a6" />
                    <line x1="0" y1="150" x2="300" y2="150" stroke="#34495e" stroke-width="2" />
                    <path id="{unique_id}_spring" d="" fill="none" stroke="#7f8c8d" stroke-width="2" />
                    <rect id="{unique_id}_block" x="150" y="110" width="40" height="40" fill="#3498db" rx="4" />
                </svg>
                <div style="margin-top: 10px;">
                    <button id="{unique_id}_play" style="padding: 8px 16px; cursor: pointer; border-radius: 5px; border: none; background: #2ecc71; color: white;">Play/Pause Animation</button>
                </div>
            </div>

            <div style="width: 250px; background: #f8f9fa; padding: 15px; border-radius: 10px;">
                <div style="margin-bottom: 15px;">
                    <label style="font-weight: bold; color: #e74c3c;">Kinetic Energy ($KE$)</label>
                    <div style="width: 100%; background: #eee; height: 20px; border-radius: 10px; margin-top: 5px;">
                        <div id="{unique_id}_ke_bar" style="width: 50%; background: #e74c3c; height: 100%; border-radius: 10px; transition: width 0.05s;"></div>
                    </div>
                </div>
                <div style="margin-bottom: 15px;">
                    <label style="font-weight: bold; color: #27ae60;">Potential Energy ($PE$)</label>
                    <div style="width: 100%; background: #eee; height: 20px; border-radius: 10px; margin-top: 5px;">
                        <div id="{unique_id}_pe_bar" style="width: 50%; background: #27ae60; height: 100%; border-radius: 10px; transition: width 0.05s;"></div>
                    </div>
                </div>
                <div style="border-top: 2px solid #ddd; padding-top: 10px; font-weight: bold; text-align: center;">
                    Total Energy: <span style="color: #2c3e50;">Constant</span>
                </div>
            </div>
        </div>

        <script>
            (function() {{
                const block = document.getElementById('{unique_id}_block');
                const spring = document.getElementById('{unique_id}_spring');
                const keBar = document.getElementById('{unique_id}_ke_bar');
                const peBar = document.getElementById('{unique_id}_pe_bar');
                const playBtn = document.getElementById('{unique_id}_play');

                let t = 0;
                let running = true;
                const amplitude = 80;
                const centerX = 130;

                function drawSpring(xEnd) {{
                    let d = "M 10 130 ";
                    const coils = 10;
                    const step = (xEnd - 10) / coils;
                    for (let i = 1; i <= coils; i++) {{
                        const x = 10 + i * step;
                        const y = 130 + (i % 2 === 0 ? -15 : 15);
                        d += `L ${{x - step/2}} ${{y}} L ${{x}} 130 `;
                    }}
                    spring.setAttribute('d', d);
                }}

                function animate() {{
                    if (running) {{
                        t += 0.0125;
                        const xOffset = amplitude * Math.sin(t);
                        const posX = centerX + xOffset;
                        
                        // Physics Calculations
                        const velocity = amplitude * Math.cos(t);
                        const pe = 0.5 * Math.pow(xOffset, 2);
                        const ke = 0.5 * Math.pow(velocity, 2);
                        const total = pe + ke;

                        // Update Visuals
                        block.setAttribute('x', posX);
                        drawSpring(posX);
                        
                        keBar.style.width = (ke/total * 100) + "%";
                        peBar.style.width = (pe/total * 100) + "%";
                    }}
                    requestAnimationFrame(animate);
                }}

                playBtn.addEventListener('click', () => running = !running);
                animate();
            }})();
        </script>
    </div>
    """
    return HTML(html_code)

display(create_spring_energy_widget())
:::