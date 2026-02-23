:::{code-cell} python
:tags: ["remove-input"]
:label: double_slit
from IPython.display import HTML, display
import uuid

def create_double_slit_widget():
    # Generate a unique ID to prevent conflicts with other widgets on the page
    uid = f"ds_{uuid.uuid4().hex[:8]}"
    
    html_code = fr"""
    <div id="{uid}_cont" style="border: 1px solid #ddd; padding: 25px; border-radius: 12px; background: #fff; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; box-shadow: 0 4px 6px rgba(0,0,0,0.05); max-width: 900px; margin: auto;">
        <div style="display: flex; flex-direction: column; gap: 25px;">
            <!-- Simulation Canvas (Now on top and larger) -->
            <div style="width: 100%; position: relative;">
                <canvas id="{uid}_canvas" width="800" height="400" style="background: #000; border-radius: 8px; width: 100%; height: auto;"></canvas>
                <div style="position: absolute; top: 10px; left: 50%; transform: translateX(-50%); font-weight: bold; color: rgba(255,255,255,0.5); font-size: 0.8em; letter-spacing: 1px;">DOUBLE SLIT SIMULATION</div>
            </div>
            
            <!-- UI Controls (Now below and in a grid) -->
            <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; border: 1px solid #eee;">
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 25px;">
                    
                    <!-- Wave Properties -->
                    <div>
                        <h4 style="margin: 0 0 12px 0; color: #333; border-bottom: 1px solid #ddd; padding-bottom: 5px;">Wave Properties</h4>
                        <label style="display: block; font-weight: bold; margin-bottom: 5px; color: #555;">Wavelength (λ): <span id="{uid}_lam_val" style="color: #2244b0;">25</span></label>
                        <input type="range" id="{uid}_lam" min="15" max="60" value="25" style="width: 100%; margin-bottom: 15px; cursor: pointer;">
                        
                        <label style="display: block; font-weight: bold; margin-bottom: 5px; color: #555;">Slit Separation (d): <span id="{uid}_d_val" style="color: #2244b0;">40</span></label>
                        <input type="range" id="{uid}_d" min="20" max="120" value="40" style="width: 100%; cursor: pointer;">
                    </div>

                    <!-- Animation Settings -->
                    <div>
                        <h4 style="margin: 0 0 12px 0; color: #333; border-bottom: 1px solid #ddd; padding-bottom: 5px;">Animation Settings</h4>
                        <label style="display: block; font-weight: bold; margin-bottom: 5px; color: #555;">Animation Speed: <span id="{uid}_speed_val" style="color: #2244b0;">0.30</span></label>
                        <input type="range" id="{uid}_speed" min="0.05" max="1.0" step="0.05" value="0.30" style="width: 100%; margin-bottom: 15px; cursor: pointer;">
                        
                        <div style="display: flex; flex-direction: column; gap: 8px;">
                            <button id="{uid}_obs" style="width: 100%; padding: 10px; font-weight: bold; cursor: pointer; background: #2244b0; color: white; border: none; border-radius: 6px; transition: all 0.2s ease;">
                                Observe Slits: OFF
                            </button>
                            <button id="{uid}_reset" style="width: 100%; padding: 10px; font-weight: bold; cursor: pointer; background: #666; color: white; border: none; border-radius: 6px; transition: all 0.2s ease;">
                                Reset Animation
                            </button>
                        </div>
                    </div>
                </div>

                <div style="margin-top: 20px; padding: 12px; border-left: 4px solid #2244b0; background: #fff; font-size: 0.9em; color: #444; line-height: 1.5; border-radius: 0 4px 4px 0;">
                    <strong>Conceptual Insight:</strong> Use the <b>Observe</b> button to see the "collapse" into particle behavior. This simulation demonstrates how "which-way" information destroys the spatial coherence required for wave interference.
                </div>
            </div>
        </div>
        
        <script>
        (function() {{
            const canvas = document.getElementById('{uid}_canvas');
            const ctx = canvas.getContext('2d');
            const lamSl = document.getElementById('{uid}_lam');
            const dSl = document.getElementById('{uid}_d');
            const speedSl = document.getElementById('{uid}_speed');
            const obsBtn = document.getElementById('{uid}_obs');
            const resetBtn = document.getElementById('{uid}_reset');
            
            const lamVal = document.getElementById('{uid}_lam_val');
            const dVal = document.getElementById('{uid}_d_val');
            const speedVal = document.getElementById('{uid}_speed_val');
            
            let observing = false;
            let time = 0;
            const wavePropSpeed = 4.5; 
            
            obsBtn.onclick = () => {{
                observing = !observing;
                obsBtn.innerText = observing ? "Observe Slits: ON" : "Observe Slits: OFF";
                obsBtn.style.background = observing ? "#c53030" : "#2244b0";
            }};

            resetBtn.onclick = () => {{
                time = 0;
            }};

            // Deterministic pseudo-random function for stable trajectories based on particle index
            function pseudoRandom(i) {{
                const x = Math.sin(i * 123.456) * 10000;
                return x - Math.floor(x);
            }}

            function draw() {{
                const w = canvas.width;
                const h = canvas.height;
                const lam = parseInt(lamSl.value);
                const d = parseInt(dSl.value);
                const animSpeed = parseFloat(speedSl.value);
                
                lamVal.innerText = lam;
                dVal.innerText = d;
                speedVal.innerText = animSpeed.toFixed(2);
                
                ctx.clearRect(0, 0, w, h);
                
                const slitX = 220; 
                const screenX = w - 80;
                const slitY1 = h/2 - d/2;
                const slitY2 = h/2 + d/2;
                const currentFrontX = time * wavePropSpeed;
                
                // 1. Incoming Source
                if (!observing) {{
                    for (let x = 0; x < slitX; x += 3) {{
                        if (x < currentFrontX) {{
                            const phase = (x - currentFrontX) % lam;
                            const normPhase = (phase + lam) % lam;
                            const alpha = Math.pow(Math.cos(Math.PI * (normPhase / (lam/2) - 1)), 4);
                            
                            ctx.strokeStyle = `rgba(0, 255, 255, ${{alpha * 0.45}})`;
                            ctx.beginPath();
                            ctx.moveTo(x, 0); ctx.lineTo(x, h);
                            ctx.stroke();
                        }}
                    }}
                }} else {{
                    // Increased density for source side
                    for (let i = 0; i < 150; i++) {{
                        const px = (currentFrontX + i * 4) % slitX;
                        const yBase = h/2;
                        // Use pseudo-random for stable spread
                        const rnd = pseudoRandom(i);
                        const yVar = (rnd - 0.5) * h * 0.95;
                        ctx.fillStyle = "rgba(0, 255, 255, 0.6)";
                        ctx.beginPath(); ctx.arc(px, yBase + yVar, 2, 0, 2*Math.PI); ctx.fill();
                    }}
                }}
                
                // 2. Barrier Wall
                ctx.strokeStyle = "#ffffff";
                ctx.lineWidth = 8;
                ctx.beginPath();
                ctx.moveTo(slitX, 0); ctx.lineTo(slitX, slitY1 - 12);
                ctx.moveTo(slitX, slitY1 + 12); ctx.lineTo(slitX, slitY2 - 12);
                ctx.moveTo(slitX, slitY2 + 12); ctx.lineTo(slitX, h);
                ctx.stroke();
                
                // 3. Region after Slits
                if (!observing) {{
                    const maxRadius = Math.max(0, currentFrontX - slitX);
                    for (let r = 0; r < Math.min(w - slitX + 100, maxRadius); r += 4) {{
                        const phase = (r + slitX - currentFrontX) % lam;
                        const normPhase = (phase + lam) % lam;
                        const alpha = Math.pow(Math.cos(Math.PI * (normPhase / (lam/2) - 1)), 4);
                        
                        ctx.strokeStyle = `rgba(0, 255, 255, ${{alpha * 0.3}})`;
                        ctx.beginPath(); ctx.arc(slitX, slitY1, r, -Math.PI/2, Math.PI/2); ctx.stroke();
                        ctx.beginPath(); ctx.arc(slitX, slitY2, r, -Math.PI/2, Math.PI/2); ctx.stroke();
                    }}
                }} else {{
                    // "Observation" sensors
                    ctx.fillStyle = "rgba(255, 255, 0, 0.95)";
                    ctx.beginPath(); ctx.arc(slitX, slitY1, 9, 0, 2*Math.PI); ctx.fill();
                    ctx.beginPath(); ctx.arc(slitX, slitY2, 9, 0, 2*Math.PI); ctx.fill();

                    // Particles emerging with collimated, pseudo-random trajectories
                    const distPastSlits = currentFrontX - slitX;
                    if (distPastSlits > 0) {{
                        for (let i = 0; i < 40; i++) {{
                            const progress = (distPastSlits + i * 20) % (screenX - slitX);
                            
                            // Slit 1 Stream
                            const rnd1 = pseudoRandom(i + 500);
                            const spread1 = (rnd1 - 0.5) * 0.25 * progress;
                            ctx.fillStyle = "rgba(0, 255, 255, 0.6)";
                            ctx.beginPath(); 
                            ctx.arc(slitX + progress, slitY1 + spread1, 2, 0, 2*Math.PI); 
                            ctx.fill();

                            // Slit 2 Stream
                            const rnd2 = pseudoRandom(i + 1000);
                            const spread2 = (rnd2 - 0.5) * 0.25 * progress;
                            ctx.beginPath(); 
                            ctx.arc(slitX + progress, slitY2 + spread2, 2, 0, 2*Math.PI); 
                            ctx.fill();
                        }}
                    }}
                }}

                // 4. Detector Screen & Intensity Pattern
                ctx.lineWidth = 3;
                ctx.strokeStyle = "#444";
                ctx.beginPath(); ctx.moveTo(screenX, 0); ctx.lineTo(screenX, h); ctx.stroke();

                const patternAmplitude = 60;
                const patternFade = Math.min(1, Math.max(0, (currentFrontX - screenX) / 80 + 0.1));
                
                if (patternFade > 0) {{
                    ctx.beginPath();
                    ctx.strokeStyle = `rgba(255, 255, 255, ${{patternFade * 0.9}})`;
                    ctx.lineWidth = 2;
                    for (let y = 0; y < h; y++) {{
                        const dy = y - h/2;
                        let intensity;
                        
                        if (!observing) {{
                            const L = screenX - slitX;
                            const val = Math.PI * d * dy / (lam * L);
                            const envelope = Math.pow(Math.sin(8*dy/L)/(8*dy/L) || 1, 2);
                            intensity = Math.pow(Math.cos(val), 2) * envelope;
                        }} else {{
                            const spread = 700;
                            const g1 = Math.exp(-Math.pow(dy - d/2, 2) / spread);
                            const g2 = Math.exp(-Math.pow(dy + d/2, 2) / spread);
                            intensity = (g1 + g2) * 0.45;
                        }}
                        
                        const plotX = screenX + intensity * patternAmplitude * patternFade;
                        if (y === 0) ctx.moveTo(plotX, y);
                        else ctx.lineTo(plotX, y);
                        
                        ctx.fillStyle = `rgba(0, 255, 255, ${{intensity * patternFade * 0.8}})`;
                        ctx.fillRect(screenX, y, 6, 1);
                    }}
                    ctx.stroke();
                }}

                time += animSpeed; 
                requestAnimationFrame(draw);
            }}
            draw();
        }})();
        </script>
    </div>
    """
    return HTML(html_code)

# Run the widget
display(create_double_slit_widget())
:::