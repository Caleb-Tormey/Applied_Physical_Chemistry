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

:::{code-cell} python
:tags: ["remove-input"]
# --- START: Required for every block that imports from _ext ---
import sys
import os
from IPython.display import display, HTML

# Adjust the path based on file depth
try:
    cwd = os.getcwd()
    # e.g., use ("..", "..") for a file 2 levels deep.
    project_root = os.path.abspath(os.path.join(cwd, "..", "..", ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
except Exception as e:
    print(f"Error setting project path: {e}")

from _ext.interactive_qa import QuestionBlock
# --- END: Required for every block ---
questions = QuestionBlock()
questions.add_question(
    question_id="sec-01-ch-B-q01",
    question_text="If you are measuring the distance between two molecules in a crystal lattice, why might you choose a derived unit or a specific power-of-ten prefix (like nano- or pico-) rather than the standard SI unit of meters?"
)
display(HTML(questions.render()))
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
:::{code-cell} python
:tags: ["remove-input"]
# --- START: Required for every block that imports from _ext ---
import sys
import os
from IPython.display import display, HTML

# Adjust the path based on file depth
try:
    cwd = os.getcwd()
    # e.g., use ("..", "..") for a file 2 levels deep.
    project_root = os.path.abspath(os.path.join(cwd, "..", "..", ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
except Exception as e:
    print(f"Error setting project path: {e}")

from _ext.interactive_qa import QuestionBlock
# --- END: Required for every block ---
questions = QuestionBlock()
questions.add_question(
    question_id="sec-01-ch-B-q02",
    question_text="In a 3D coordinate system, if you move an object only along the $z$-axis, what happens to its $x$ and $y$ coordinates? How does this simplify the calculation of the distance from the origin?"
)
display(HTML(questions.render()))
:::
Cyclindrical Coordinates
magine taking the 2D Polar system and just extruding it upwards. This creates a system defined by a circular base and a height.
* **Coordinates:** $(r, \theta, z)$
    * $r$: Distance from the Z-axis (radius of the cylinder).
    * $\theta$: Angle in the $xy$ plane (azimuthal).
    * $z$: Height above the $xy$ plane.
* **Best for:** Wires, pipes, magnetic fields around a current.
:::{include} interactive_code/cylindrical_coordinates.md
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
:::{include} interactive_code/spherical_coordinates.md
:::
:::{code-cell} python
:tags: ["remove-input"]
# --- START: Required for every block that imports from _ext ---
import sys
import os
from IPython.display import display, HTML

# Adjust the path based on file depth
try:
    cwd = os.getcwd()
    # e.g., use ("..", "..") for a file 2 levels deep.
    project_root = os.path.abspath(os.path.join(cwd, "..", "..", ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
except Exception as e:
    print(f"Error setting project path: {e}")

from _ext.interactive_qa import QuestionBlock
# --- END: Required for every block ---
questions = QuestionBlock()
questions.add_question(
    question_id="sec-01-ch-B-q03",
    question_text="Explain it is helpful to have different coordinate systems. As part of your explanation give examples of when you might want one system over another. "
)
display(HTML(questions.render()))
:::