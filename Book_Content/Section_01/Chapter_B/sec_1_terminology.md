## Terminology, Definitions and Units

### Powers of Ten

We will be using scientific notation, however, it is often better to use powers of ten to make the numbers more reasonable. To that end there are prefixes that we can use to account for this. They typically come in bundles of 3 powers of 10 (so $1000$ or $0.001$)

:::{csv-table} Powers of Ten Prefixes
:header: "Prefix", "Exponent", "Number","Scientific Notation", "Name"
:label: tbl_prefix

"Giga (G)", "9", "1,000,000,000",$10^9$,"billion"
"Mega (M)", "6", "1,000,000",$10^6$,"million"
"kilo (k)", "3", "1,000",$10^3$,"thousand"
"hecto (h)", "2", "100",$10^2$,"hundred"
"deca (da)", "1", "10",$10$,"ten"
"deci (d)", "-1", "0.1",$10^{-1}$,"tenth"
"centi (c)", "-2", "0.01",$10^{-2}$,"hundreth"
"milli (m)", "-3", "0.001",$10^{-3}$,"thousandth"
"micro ($\mu$)", "-6", "0.000001",$10^{-6}$,"millionth"
"nano (n)", "-9", "0.00000001",$10^{-9}$,"billionth"

:::

### Basie SI Units

In order to do science in an organized and more easily reproducible way, we need to have standards upon which to compare results or to set up experiments. To that end standardized units are vital to physical science. While there are many systems of units, we will primarily be using SI units (short for Internation System of Units well technically it is short for the French Système International d'unités). Here are the units we will be primarily using. 


:::{csv-table} Base SI Units
:header: "Quantity", "Name", "Abbreviation"
:label: tbl_base_units

"Length", "Meter", "m"
"Mass", "Kilogram", "kg"
"Time", "Second", "s"
"Electric Current", "Ampere", "A"
"Thermodynamic Temperature", "Kelvin", "K"
"Amount of Substance", "Mole", "mol"
"Luminous Intensity", "Candela", "cd"
:::

### Derived Units

We cannot just use the base units as the world has more complicated characteristics. We can therefore combine base units to create derived units. For example, we use meter, m, as the unit of length. If we would like to describe an area we would multiply the length ($l$) times the width ($w$). The length and the width both have units of meters. So when we multiply them together we get meters times meters which should be a unit of area as shown below,



:::{math}
:enumerated: false

l(m) \times w(m) = lw(m^2)= a (m^2)

:::

We can also mix unit types for other derived units. For example, we could find the density of water by finding the mass that occupies a certain volume. What we would find is that $1\:g$ of water would occupy $1\:mL$
Look in {ref}`tbl_derived_units` for some of the derived units we will be using. 
:::{csv-table} Examples of Derived SI Units
:header: "Quantity", "Unit Name", "Symbol", "Expression in Base Units"
:label: tbl_derived_units

"Frequency", "Hertz", "Hz", "s⁻¹"
"Force", "Newton", "N", "kg⋅m/s²"
"Pressure", "Pascal", "Pa", "N/m² or kg/(m⋅s²)"
"Energy, Work, Heat", "Joule", "J", "N⋅m or kg⋅m²/s²"
"Power", "Watt", "W", "J/s or kg⋅m²/s³"
"Electric Charge", "Coulomb", "C", "A⋅s"
"Electric Potential", "Volt", "V", "J/C"
"Electric Resistance", "Ohm", "Ω", "V/A"
"Capacitance", "Farad", "F", "C/V"
"Magnetic Flux Density", "Tesla", "T", "N/(A⋅m)"
:::


### Unit Conversion

It will often be required to convert from one set of units to another based on experimental procedures or previous studies. It is vital you be able to confidently change units, and especially derived units, accurately. The key to making the conversions is to pay attention to whether the unit is in the numerator or denominator. Most errors come from converting with inverted relationships. Key to doing this correctly is writing out **ALL** units and not taking shortcuts. Let's show a couple of examples. 

we will start with a straight forward one where we will convert $1.23\:m$ to kilometers,

:::{math}
:enumerated: false
\begin{align}
1.23\:m =\:?\:km\\
\text{Use the fact that}\: 1000\:m = 1\:km\\
1.23\:m\times \frac{1\:km}{1000\:m}\\
1.23\:\cancel{m}\times \frac{1\:km}{1000\:\cancel{m}}\\
\frac{1.23\:km}{1000}=0.00123\:km=\boxed{1.23\times 10^{-3}\:km}
\end{align}
:::

We can do a trickier one if we look at derived units and units with exponents. Let's next convert $4.56\:kg\:L^{-1}$ to units of grams per cubic meter ($g\:m^{-3}$). To do this let's first write out some of the conversion ratios that might be helpful. $1\:kg = 1000\:g$, $1\:L = 1\:dm^3$, and $1\:dm = 0.1\:m$.

::::{dropdown} Click here for solution
:::{math}
:enumerated: false
\begin{align}
\frac{4.56\:\cancel{kg}}{1\:L}\times\frac{1000\:g}{1\:\cancel{kg}}=\frac{4.56\times10^3\:g}{1\:L}\\
\frac{4.56\times10^3\:g}{1\:\cancel{L}}\times\frac{1\:\cancel{L}}{1\:dm^3}=\frac{4.56\times10^3\:g}{1\:dm^3}\\
\frac{4.56\times10^3\:g}{1\:dm^3}\times\left(\frac{0.1\:dm}{1\:m}\right)^3=\frac{4.56\times10^3\:g}{1\:\cancel{dm^3}}\times\frac{0.001\:\cancel{dm^3}}{1\:m^3}=\frac{4.56\:g}{1\:m^3}\\
\boxed{4.56\:g\:m^{-3}}
\end{align}
:::
::::

Lastly let's look at using and converting to non-SI units (typically imperial units). You may see some familiar or unfamiliar unit comparisons that may be necessary. For example, there are $2.54\:cm$ per $1\:in$. There are also $12\:inch$ per $1\:ft$ and $5280\:ft$ per $1\:mi$. Using these facts let's convert $1\:km$ to miles.

::::{dropdown} Click here for solution
:::{math}
:enumerated: false
\begin{align}
1\:\cancel{km}\times \frac{1000\:m}{1\:\cancel{km}}=1000\:m\\
1000\:\cancel{m}\times\frac{100\:cm}{1\:\cancel{m}}=100000\:cm\\
100000\:\cancel{cm}\times\frac{1\:inch}{2.54\:\cancel{cm}}=39370\:in\\
39370\:\cancel{in}\times\frac{1\:\cancel{ft}}{12\:\cancel{in}}\times\frac{1\:mi}{5280\:\cancel{ft}} =\boxed{0.621\:mi}
\end{align}
:::
::::
### Coordinate Systems

Coordinate systems are used to help define a system in space. By creating a coordinate system every point in the space can be uniquely identified. If we want to determine thing like speed, or concentration we need some notion as

#### Two-Dimensional Space (2D)

This is the system you have used since algebra class. A point $P$ is defined by its horizontal distance ($x$) and vertical distance ($y$) from the origin.
* **Coordinates:** $(x, y)$
* **Best for:** Flat planes, blocks, projectile motion without air resistance.

Instead of "over and up," we describe a point by "how far" and "which direction." This is perfect for central forces, like a planet orbiting a star or an electron in a 2D ring.
* **Coordinates:** $(r, \theta)$
    * $r$: Radial distance from the origin ($0 \le r < \infty$).
    * $\theta$ (theta): The angle measured counter-clockwise from the positive x-axis ($0 \le \theta < 2\pi$).

We relate the two using basic trigonometry (SOH CAH TOA) and the Pythagorean theorem.

**Polar $\to$ Cartesian:**
$$x = r \cos \theta$$
$$y = r \sin \theta$$

**Cartesian $\to$ Polar:**
$$r = \sqrt{x^2 + y^2}$$
$$\theta = \arctan\left(\frac{y}{x}\right)$$

:::{code-cell} python
:tags: [remove-input]
:label: polar_cartesian_convert
from IPython.display import HTML, display
import json

def create_js_polar_plot():
    # We define the HTML and JS structure as a multi-line string.
    # We use Plotly.js (loaded from CDN) to handle the rendering.
    
    html_code = """
    <div style="font-family: 'Arial', sans-serif; max-width: 600px; margin: auto; border: 1px solid #ddd; padding: 20px; border-radius: 8px;">
        <h3 style="text-align: center;">Interactive Polar Coordinates</h3>
        
        <div id="polar_plot" style="width: 100%; height: 500px;"></div>
        
        <div style="background-color: #f9f9f9; padding: 15px; border-radius: 5px;">
            
            <div style="margin-bottom: 15px;">
                <label for="r_slider" style="font-weight: bold;">Radius (r): <span id="r_val" style="color: blue;">5.0</span></label>
                <input type="range" id="r_slider" min="1" max="10" step="0.1" value="5" style="width: 100%;">
            </div>
            
            <div>
                <label for="theta_slider" style="font-weight: bold;">Angle (θ): <span id="theta_val" style="color: magenta;">45</span>°</label>
                <input type="range" id="theta_slider" min="0" max="360" step="1" value="45" style="width: 100%;">
            </div>

            <div style="margin-top: 15px; text-align: center; font-size: 16px;">
                Cartesian: <b>x = <span id="x_out">3.54</span></b>, <b>y = <span id="y_out">3.54</span></b>
            </div>
        </div>

        <script>
            // Check if Plotly is loaded, if not, load it
            if (typeof Plotly === 'undefined') {
                var script = document.createElement('script');
                script.src = 'https://cdn.plot.ly/plotly-latest.min.js';
                document.head.appendChild(script);
                script.onload = initPolarPlot;
            } else {
                initPolarPlot();
            }

            function initPolarPlot() {
                var rSlider = document.getElementById('r_slider');
                var thetaSlider = document.getElementById('theta_slider');
                var rValDisp = document.getElementById('r_val');
                var thetaValDisp = document.getElementById('theta_val');
                var xOut = document.getElementById('x_out');
                var yOut = document.getElementById('y_out');

                function getCoords(r, deg) {
                    var rad = deg * (Math.PI / 180);
                    return {
                        x: r * Math.cos(rad),
                        y: r * Math.sin(rad),
                        rad: rad
                    };
                }

                // Initial Data
                var r0 = parseFloat(rSlider.value);
                var t0 = parseFloat(thetaSlider.value);
                var c0 = getCoords(r0, t0);

                // --- Trace Definitions ---
                // 1. Vector (Black Line)
                var traceVector = {
                    x: [0, c0.x], y: [0, c0.y],
                    mode: 'lines+markers',
                    line: {color: 'black', width: 4},
                    marker: {size: 8, color: 'black'},
                    name: 'Vector'
                };

                // 2. X-Component (Blue Dashed)
                var traceX = {
                    x: [0, c0.x], y: [c0.y, c0.y],
                    mode: 'lines',
                    line: {color: 'blue', width: 2, dash: 'dot'},
                    name: 'x-comp'
                };

                // 3. Y-Component (Red Dashed)
                var traceY = {
                    x: [c0.x, c0.x], y: [0, c0.y],
                    mode: 'lines',
                    line: {color: 'red', width: 2, dash: 'dot'},
                    name: 'y-comp'
                };
                
                // 4. Arc (Green)
                function makeArc(r, rad) {
                    var n = 20;
                    var arcX = [];
                    var arcY = [];
                    var arcR = r * 0.25; // Arc is 25% of radius
                    for (var i = 0; i <= n; i++) {
                        var a = (rad / n) * i;
                        arcX.push(arcR * Math.cos(a));
                        arcY.push(arcR * Math.sin(a));
                    }
                    return {x: arcX, y: arcY};
                }
                var arcDat = makeArc(r0, c0.rad);
                var traceArc = {
                    x: arcDat.x, y: arcDat.y,
                    mode: 'lines',
                    line: {color: 'magenta', width: 3},
                    name: 'Angle'
                };

                var layout = {
                    xaxis: {range: [-10, 10], title: 'x', zeroline: true},
                    yaxis: {range: [-10, 10], title: 'y', scaleanchor: 'x', zeroline: true},
                    showlegend: false,
                    margin: {t: 20, b: 40, l: 40, r: 40},
                    height: 500
                };

                var config = {responsive: true, displayModeBar: false};

                Plotly.newPlot('polar_plot', [traceVector, traceX, traceY, traceArc], layout, config);

                // --- Update Function ---
                function updatePlot() {
                    var r = parseFloat(rSlider.value);
                    var t = parseFloat(thetaSlider.value);
                    
                    // Update Text Displays
                    rValDisp.innerText = r.toFixed(1);
                    thetaValDisp.innerText = t.toFixed(0);
                    
                    var c = getCoords(r, t);
                    xOut.innerText = c.x.toFixed(2);
                    yOut.innerText = c.y.toFixed(2);
                    
                    // Recalculate Arc
                    var arc = makeArc(r, c.rad);

                    // Animate/React
                    // We construct new data arrays for the 4 traces
                    Plotly.react('polar_plot', [
                        {x: [0, c.x], y: [0, c.y]},           // Vector
                        {x: [0, c.x], y: [c.y, c.y]},         // X-comp (Horizontal from Y-axis) ... wait geometry
                        // Correct geometry: X-comp is projection on X axis? 
                        // Usually shown as line along bottom or top.
                        // Let's do: Line from (0,0) to (x,0) is x-comp.
                        // Line from (x,0) to (x,y) is y-comp.
                        // Visual style chosen: Box style (Project to axes)
                        {x: [0, c.x], y: [c.y, c.y]},         // Top Line (Blue)
                        {x: [c.x, c.x], y: [0, c.y]},         // Side Line (Red)
                        {x: arc.x, y: arc.y}                  // Arc
                    ], layout);
                }

                // Attach Listeners
                rSlider.addEventListener('input', updatePlot);
                thetaSlider.addEventListener('input', updatePlot);
            }
        </script>
    </div>
    """
    
    return HTML(html_code)

# Run the function to display the widget
create_js_polar_plot()
:::

#### Three-Dimensional Space (3D) 

Cartesian
We simply add a vertical $z$-axis perpendicular to the $xy$ plane.
* **Coordinates:** $(x, y, z)$
* **Best for:** Boxes, cubes, standard infinite potential wells.

Cyclindrical Coordinates
magine taking the 2D Polar system and just extruding it upwards. This creates a system defined by a circular base and a height.
* **Coordinates:** $(r, \theta, z)$
    * $r$: Distance from the Z-axis (radius of the cylinder).
    * $\theta$: Angle in the $xy$ plane (azimuthal).
    * $z$: Height above the $xy$ plane.
* **Best for:** Wires, pipes, magnetic fields around a current.
:::{code-cell} python
:tags: [remove-input]
:label: cylindrical_coordinates
import numpy as np
import plotly.graph_objects as go

def create_cylindrical_diagram_fixed():
    fig = go.Figure()

    # --- Parameters for the Example Point P ---
    r_p = 4        
    theta_deg = 60 
    z_p = 5        
    
    theta_rad = np.deg2rad(theta_deg)

    # Convert P to Cartesian coordinates
    x_p = r_p * np.cos(theta_rad)
    y_p = r_p * np.sin(theta_rad)

    # --- 1. Contextual Cylinder Outlines ---
    phi_cyl = np.linspace(0, 2*np.pi, 100)
    cyl_x = r_p * np.cos(phi_cyl)
    cyl_y = r_p * np.sin(phi_cyl)

    # Base Circle
    fig.add_trace(go.Scatter3d(
        x=cyl_x, y=cyl_y, z=np.zeros_like(cyl_x),
        mode='lines', line=dict(color='lightblue', dash='dot', width=2), 
        opacity=0.4, hoverinfo='skip'
    ))
    # Top Circle
    fig.add_trace(go.Scatter3d(
        x=cyl_x, y=cyl_y, z=np.full_like(cyl_x, z_p),
        mode='lines', line=dict(color='lightblue', dash='dot', width=2), 
        opacity=0.4, hoverinfo='skip'
    ))

    # --- 2. Geometry Lines ---
    # Projection Drop
    fig.add_trace(go.Scatter3d(
        x=[x_p, x_p], y=[y_p, y_p], z=[z_p, 0],
        mode='lines', line=dict(color='grey', dash='dash'), hoverinfo='skip'
    ))

    # Radial Line 'r'
    fig.add_trace(go.Scatter3d(
        x=[0, x_p], y=[0, y_p], z=[0, 0],
        mode='lines+text', line=dict(color='blue', width=5),
        text=["", "<b>r</b>"], textposition="middle center", 
        textfont=dict(size=16, color='blue')
    ))
    
    # Height Line 'z'
    fig.add_trace(go.Scatter3d(
        x=[0, 0], y=[0, 0], z=[0, z_p],
        mode='lines+text', line=dict(color='green', width=5),
        text=["", "<b>z</b>"], textposition="middle left", 
        textfont=dict(size=16, color='green')
    ))
    
    # Connector top
    fig.add_trace(go.Scatter3d(
        x=[0, x_p], y=[0, y_p], z=[z_p, z_p],
        mode='lines', line=dict(color='grey', dash='dash'), hoverinfo='skip'
    ))

    # Angle 'theta'
    arc_angles = np.linspace(0, theta_rad, 30)
    arc_dist = r_p * 0.3
    arc_x = arc_dist * np.cos(arc_angles)
    arc_y = arc_dist * np.sin(arc_angles)
    
    fig.add_trace(go.Scatter3d(
        x=arc_x, y=arc_y, z=np.zeros_like(arc_x),
        mode='lines', line=dict(color='magenta', width=4), hoverinfo='skip'
    ))
    
    fig.add_trace(go.Scatter3d(
        x=[arc_x[15]], y=[arc_y[15]], z=[0],
        mode='text', text=["<b>θ</b>"], textposition="bottom right", 
        textfont=dict(size=16, color='magenta')
    ))

    # --- 3. Points ---
    # Origin
    fig.add_trace(go.Scatter3d(
        x=[0], y=[0], z=[0], mode='markers', marker=dict(size=5, color='black'), hoverinfo='skip'
    ))
    # Projection
    fig.add_trace(go.Scatter3d(
        x=[x_p], y=[y_p], z=[0], mode='markers', marker=dict(size=5, color='grey'), hoverinfo='skip'
    ))
    # Point P
    fig.add_trace(go.Scatter3d(
        x=[x_p], y=[y_p], z=[z_p],
        mode='markers+text', marker=dict(size=10, color='red'),
        text=["<b>P(r, θ, z)</b>"], textposition="top center", textfont=dict(size=16)
    ))

    # --- Layout ---
    # Simplified axis config (removed titlefont)
    axis_config = dict(showgrid=False, zeroline=True, showline=True, showticklabels=False)
    
    fig.update_layout(
        title="<b>Cylindrical Coordinate System (r, θ, z)</b>",
        width=800, height=800,
        showlegend=False,
        template="plotly_white",
        scene=dict(
            # Define Title and Font structure explicitly here
            xaxis=dict(**axis_config, title=dict(text="X", font=dict(size=20)), range=[-1, 6]),
            yaxis=dict(**axis_config, title=dict(text="Y", font=dict(size=20)), range=[-1, 6]),
            zaxis=dict(**axis_config, title=dict(text="Z", font=dict(size=20)), range=[0, 7]),
            aspectmode='cube',
            camera=dict(
                eye=dict(x=1.6, y=1.6, z=1.2),
                center=dict(x=0, y=0, z=-0.2)
            )
        )
    )

    return fig

fig_cyl = create_cylindrical_diagram_fixed()
fig_cyl.show()
:::
Spherical Coordinates

This is the most important system for quantum chemistry. Atoms are spherical. To locate an electron, we specify its distance from the nucleus and two angles (like latitude and longitude).

* **Coordinates:** $(r, \theta, \phi)$
    * $r$: Distance from the origin (radius).
    * $\theta$ (theta): The **Polar Angle** (angle down from the top z-axis). Ranges from $0$ to $\pi$.
    * $\phi$ (phi): The **Azimuthal Angle** (angle around the z-axis in the xy plane). Ranges from $0$ to $2\pi$.

*Warning:* Math textbooks often swap the symbols for $\theta$ and $\phi$. In Physics and Chemistry, $\theta$ is almost always the angle from the Z-axis.

**Conversions (Spherical $\to$ Cartesian):**
$$x = r \sin \theta \cos \phi$$
$$y = r \sin \theta \sin \phi$$
$$z = r \cos \theta$$
:::{code-cell}
:tags: ["remove-input"]
questions = QuestionBlock()
questions.add_question(
    question_id="sec-2-ch-2-q01",
    question_text="Given the possible quantum numbers is it possible to have zero vibrational energy in a quantum HO? Please justify and explain your answer. "
)
display(HTML(questions.render()))
:::
:::{code-cell} python
:tags: ["remove-input"]
:label: spherical_cartesian_convert
from IPython.display import HTML, display

def create_js_spherical_plot():
    html_code = """
    <div style="font-family: 'Arial', sans-serif; max-width: 800px; margin: auto; border: 1px solid #ddd; padding: 20px; border-radius: 8px;">
        <h3 style="text-align: center;">Interactive Spherical Coordinates (r, θ, φ)</h3>
        
        <div id="spherical_plot" style="width: 100%; height: 600px;"></div>
        
        <div style="background-color: #f9f9f9; padding: 15px; border-radius: 5px;">
            <div style="display: flex; gap: 20px; flex-wrap: wrap;">
                
                <div style="flex: 1; min-width: 200px;">
                    <label for="r_s_slider" style="font-weight: bold;">Radius (r): <span id="r_s_val" style="color: blue;">10.0</span></label>
                    <input type="range" id="r_s_slider" min="1" max="20" step="0.5" value="10" style="width: 100%;">
                </div>
                
                <div style="flex: 1; min-width: 200px;">
                    <label for="theta_s_slider" style="font-weight: bold;">Polar Angle (θ): <span id="theta_s_val" style="color: magenta;">45</span>°</label>
                    <input type="range" id="theta_s_slider" min="0" max="180" step="1" value="45" style="width: 100%;">
                    <small style="color: grey;">Angle from top Z-axis</small>
                </div>

                <div style="flex: 1; min-width: 200px;">
                    <label for="phi_s_slider" style="font-weight: bold;">Azimuthal (φ): <span id="phi_s_val" style="color: green;">45</span>°</label>
                    <input type="range" id="phi_s_slider" min="0" max="360" step="1" value="45" style="width: 100%;">
                    <small style="color: grey;">Rotation in XY plane</small>
                </div>
            </div>

            <div style="margin-top: 15px; text-align: center; font-size: 16px;">
                Cartesian: 
                <b>x = <span id="x_s_out">0.00</span></b>, 
                <b>y = <span id="y_s_out">0.00</span></b>, 
                <b>z = <span id="z_s_out">0.00</span></b>
            </div>
        </div>

        <script>
            if (typeof Plotly === 'undefined') {
                var script = document.createElement('script');
                script.src = 'https://cdn.plot.ly/plotly-latest.min.js';
                document.head.appendChild(script);
                script.onload = initSphericalPlot;
            } else {
                initSphericalPlot();
            }

            function initSphericalPlot() {
                var rSlider = document.getElementById('r_s_slider');
                var thetaSlider = document.getElementById('theta_s_slider');
                var phiSlider = document.getElementById('phi_s_slider');
                
                var rDisp = document.getElementById('r_s_val');
                var thetaDisp = document.getElementById('theta_s_val');
                var phiDisp = document.getElementById('phi_s_val');
                
                var xOut = document.getElementById('x_s_out');
                var yOut = document.getElementById('y_s_out');
                var zOut = document.getElementById('z_s_out');

                function getSphericalCoords(r, thetaDeg, phiDeg) {
                    var tRad = thetaDeg * (Math.PI / 180);
                    var pRad = phiDeg * (Math.PI / 180);
                    
                    var x = r * Math.sin(tRad) * Math.cos(pRad);
                    var y = r * Math.sin(tRad) * Math.sin(pRad);
                    var z = r * Math.cos(tRad);
                    
                    return {x: x, y: y, z: z, tRad: tRad, pRad: pRad};
                }

                // Initial Data
                var r0 = parseFloat(rSlider.value);
                var t0 = parseFloat(thetaSlider.value);
                var p0 = parseFloat(phiSlider.value);
                var c0 = getSphericalCoords(r0, t0, p0);

                // --- Traces ---
                
                // 1. Main Vector (Blue)
                var traceVec = {
                    type: 'scatter3d',
                    x: [0, c0.x], y: [0, c0.y], z: [0, c0.z],
                    mode: 'lines+markers',
                    line: {color: 'blue', width: 6},
                    marker: {size: 4, color: 'blue'},
                    name: 'r Vector'
                };

                // 2. The Shadow on Floor (Grey Dashed) - Shows Phi projection
                var traceShadow = {
                    type: 'scatter3d',
                    x: [0, c0.x], y: [0, c0.y], z: [0, 0],
                    mode: 'lines',
                    line: {color: 'grey', width: 4, dash: 'dash'},
                    name: 'XY Projection'
                };

                // 3. The Height Drop (Red) - Shows Z height
                var traceHeight = {
                    type: 'scatter3d',
                    x: [c0.x, c0.x], y: [c0.y, c0.y], z: [c0.z, 0],
                    mode: 'lines',
                    line: {color: 'red', width: 4},
                    name: 'z Height'
                };

                // 4. Theta Arc (Magenta) - Arc from Z-axis down to vector
                function makeThetaArc(r, tRad, pRad) {
                    var n = 15;
                    var ax = [], ay = [], az = [];
                    var arcR = r * 0.4; // 40% of length
                    for(var i=0; i<=n; i++){
                        var ang = (tRad/n)*i;
                        // For a fixed Phi, vary Theta from 0 to current
                        ax.push(arcR * Math.sin(ang) * Math.cos(pRad));
                        ay.push(arcR * Math.sin(ang) * Math.sin(pRad));
                        az.push(arcR * Math.cos(ang));
                    }
                    return {x: ax, y: ay, z: az};
                }
                var tArc = makeThetaArc(r0, c0.tRad, c0.pRad);
                var traceTheta = {
                    type: 'scatter3d',
                    x: tArc.x, y: tArc.y, z: tArc.z,
                    mode: 'lines',
                    line: {color: 'magenta', width: 4},
                    name: 'Theta'
                };

                var layout = {
                    scene: {
                        xaxis: {range: [-20, 20], title: 'X'},
                        yaxis: {range: [-20, 20], title: 'Y'},
                        zaxis: {range: [-20, 20], title: 'Z'},
                        aspectmode: 'cube',
                        camera: {
                            eye: {x: 1.5, y: 1.5, z: 1.2}
                        }
                    },
                    margin: {t: 0, b: 0, l: 0, r: 0},
                    showlegend: false
                };
                
                var config = {responsive: true, displayModeBar: false};

                Plotly.newPlot('spherical_plot', [traceVec, traceShadow, traceHeight, traceTheta], layout, config);

                // --- Update Loop ---
                function updateSphere() {
                    var r = parseFloat(rSlider.value);
                    var t = parseFloat(thetaSlider.value);
                    var p = parseFloat(phiSlider.value);
                    
                    rDisp.innerText = r.toFixed(1);
                    thetaDisp.innerText = t.toFixed(0);
                    phiDisp.innerText = p.toFixed(0);
                    
                    var c = getSphericalCoords(r, t, p);
                    xOut.innerText = c.x.toFixed(2);
                    yOut.innerText = c.y.toFixed(2);
                    zOut.innerText = c.z.toFixed(2);
                    
                    var newTArc = makeThetaArc(r, c.tRad, c.pRad);
                    
                    // Efficiently restyle the data
                    Plotly.react('spherical_plot', [
                        {x: [0, c.x], y: [0, c.y], z: [0, c.z]},     // Vector
                        {x: [0, c.x], y: [0, c.y], z: [0, 0]},       // Shadow
                        {x: [c.x, c.x], y: [c.y, c.y], z: [c.z, 0]}, // Height
                        {x: newTArc.x, y: newTArc.y, z: newTArc.z}   // Theta Arc
                    ], layout);
                }

                rSlider.addEventListener('input', updateSphere);
                thetaSlider.addEventListener('input', updateSphere);
                phiSlider.addEventListener('input', updateSphere);
            }
        </script>
    </div>
    """
    return HTML(html_code)

create_js_spherical_plot()
:::