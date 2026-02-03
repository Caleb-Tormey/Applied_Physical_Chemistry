## Solving More ``Complicated'' Equations
n the previous section, we refreshed the "Golden Rule" of algebra: whatever you do to one side of the equation, you must do to the other. When solving simple linear equations like $3x + 4 = 10$, you isolate $x$ by peeling away the layers using simple inverse operations: you subtract the addition and divide the multiplication.However, nature rarely moves in straight lines. In chemistry, you will encounter reaction rates that change exponentially, pH scales based on logarithms, and electron wavefunctions defined by trigonometry. While the equations look scarier, the strategy remains exactly the same: Identify the operation acting on your variable, and apply its inverse to both sides.
### Polynomials
In physical sciences, we often use polynomials as a versatile mathematical tool to model and understand physical behavior and experiment. A polynomial is defined as an expression that consists of sums of variables raised to non-negative integer powers and multiplied by coefficients that can be positive or negatively signed. The general form of a polynomial is described in equation {ref}`gen_poly` where x is our variable, $n$ is the degree of the polynomial. It's the highest exponent of $x$ and must be a non-negative integer. Each $a$ term like $a_n$ is a coefficient. Coefficients are just constant numbers that multiply its corresponding variable term. These can be positive, negative, or zero. You can think of it as a scaling factor that determines the magnitude and sign of its associated $x$ power. Notice that for the final term $x^0=1$ so it just becomes a constant $a_0$.
:::{math}
:label: gen_poly
y = a_n x^n + a_{n-1} x^{n-1}\cdots a_2 x^2 + a_1 x^1 + a_0 x^0
:::

Here are some examples of polynomials you may have already encountered or will encounter in this text. 
- $y = mx + b$ is the equation for a line.
- $y = ax^2 + bx + c$ is the equation for a parabola.
- $V^3 - \left ( b + \frac{RT}{P}\right)V^2 + \frac{a}{P}V -\frac{ab}{P} = 0$ is the van der Waals equation.

 We use them for three primary reasons. First, you have likely done a ``line of best fit'' on some data in your laboratory or class. Behind the scenes, the computer program is doing a linear regression on a polynomial of degree one ($y = a_1x + a_0$), we can fit polynomials of even higher degrees in the same way to experimental data points to create a mathematical model of the system we're studying. Second, polynomials are incredibly easy to work with because their derivatives and integrals can be found using the simple power rule you learned in calculus, making calculations straightforward. Finally, and most powerfully, many complex functions that describe real-world phenomena, such as the potential energy of a chemical bond, can be accurately approximated by a polynomial via a Taylor series expansion. While we will not do this explicitly, you will however see what the expansion is and how it works. This allows us to simplify complicated problems into a manageable form without losing essential physical insight.

 Recall that we on occasion must find the roots of an equation. That is where the equation is equal to zero. When solving quadratic equations, polynomials of $n = 2$, you have probably learned how to factor the equation into the product of two linear parts. For example, 
 :::{math}
 :enumerated: false
\begin{align}
x^2 + 3x + 2 = 0\\
\left(x+1\right)\left(x+2\right) = 0\\
\end{align}
:::
and so the solution is $x = -1,x = -2$. 

Or for more challenging problems you might have learned how to complete the square or use the quadratic formula (equation {ref}`quadratic_formula`). 
:::{math}
:label: quadratic_formula
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
:::
In this class we will encounter higher order polynomials. There are methods for solving these, however, we will not learn how to do them explicitly. Rather we will use computational tools like _Mathematica_ or Python. 
:::{code-cell}
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
    question_id="sec-01-ch-A-q02",
    question_text="Physical Validity of Roots When you solve a quadratic equation describing a physical event (like the time it takes for a ball to hit the ground), you often get two mathematical solutions (e.g., $t = 5$ seconds and $t = -2$ seconds). Mathematically both are correct, but physically we usually discard one. How do you decide which mathematical root represents the real world and which is an artifact of the equation? "
)
display(HTML(questions.render()))
#**Conceptual Question:** Given the possible quantum numbers is it possible to have zero vibrational energy in a quantum HO? Please justify and explain your answer. 
:::
### Exponentials and Logarithms 
We will start by looking at $e$ and $\ln$. These are called the exponential (sometimes referred to as the Natural number or Euler's number) and the natural logarithm respectively. They are ubiquitous in natural science due to the fact many physical processes are well modeled by first order differential equations. Another point of these two operations is that they are the inverse of one another. For example,
:::{math}
:enumerated: false
\begin{align}
y = e^x\\
\ln{y} = \ln{e^x}\\
\ln{y} = x
\end{align}
:::

(properties-of-exponentials-and-logarithms)=
#### Properties of Exponentials and Logarithms

Here we will review the properties of exponents and logarithms. The first is to recognize that an exponent is just repeated multiplication of the base. For example,
:::{math}
:enumerated:false
2^3 = 2 \times 2 \times 2
:::

So in general we say that for a base, $b$ and exponent $m$ the exponent can be defined as

:::{math}
b^m = \prod_{i = 1}^m b_i
:::

So we can multiply exponents of the same base in the following way,

:::{math}
:label: product_of_powers
b^m\times b^n = b^{m+n}
:::

Likewise, we can look at dividing exponents of the same base but accounting for the negative in the exponent of the denominator

:::{math}
:label: quotient_of_powers
\frac{b^m}{b^n} = b^{m-n}
:::

#### Changing Bases
In the equation $y = ae^x$, $e$ is called the base and x is the exponent. The base of the Log operation must match the base of the exponent. So in our case $\ln$ is the natural log since it is in base $e$ which is the natural number. If instead you had the number $10^x$ this would be base ten, and you would need to use a base-10 logarithm, $Log_{10}$. You can change bases by using the following relationship. 
:::{math}
:label: log_convert
log_b\left ( a\right) = \frac{log_x\left(a\right)}{log_x\left(b\right)}
:::

For Example,

If we are curious to solve for the value of $x$ in equation {ref}`log_problem`we could attempt to solve it by taking the $Log_2$ of both sides, however, often a calculator will only have a $Log_{10}$ or natural log ($\ln$) button. 

:::{math}
:label: log_problem
2^x = 100
:::
We can see where equation {ref}`log_convert` comes from and we can solve our problem in the following way. 
::::{dropdown} Click here for solution
:::{math}
:enumerated: false
\begin{align}
2^x = 100\\
\textcolor{red}{\ln{\textcolor{black}{2^x}}} = \textcolor{red}{\ln{\textcolor{black}{100}}}\\
x\ln{2} = \ln{100}\\
x = \frac{\ln{100}}{\ln{2}}\\
x \approx  \frac{4.60517}{0.69315}\\
x \approx  6.6386\\
\end{align}
:::
::::


#### Performing Algebra with Exponentials and Logarithms
 
Here is the first part of my chapter. Now for a question.

Often the place students get the most screwed up is when attempting to do algebraic manipulation with these two operations. The biggest issue is misapplying the rules from section {ref}`properties-of-exponentials-and-logarithms`

:::{code-cell}
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
    question_id="sec-01-ch-A-q03",
    question_text="Scaling and Compression In chemistry, we often measure quantities that vary over huge ranges, such as proton concentration $[H^+]$ which can range from $10^{-1}$ to $10^{-14}$. Why do we use a logarithmic scale (like pH) to represent these numbers? What does a <b> linear</b> change in pH (going from 1 to 2) represent in terms of the actual physical change in concentration?"
)
display(HTML(questions.render()))
#**Conceptual Question:** Given the possible quantum numbers is it possible to have zero vibrational energy in a quantum HO? Please justify and explain your answer. 
:::




(trigonometric_identities)=
### Trigonometric Functions and Identities
While trigonometry is the branch of mathematics concerned with the relationships between angles and sides of triangles. While we won't be reviewing all the details of triangles there are a few important things to review. The first are the basic 

The relationship between these functions can be seen most explicitly using the unit circle. 
% Unit Circle stuff
:::{code-cell} python
:label: Unit_circle 
:tags: [remove-input]
# Necessary imports for plotting and interactivity
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# 1. Setup Data
# ----------------
# We will use 5-degree steps for smooth animation
steps = 73 # 0 to 360
theta_deg = np.linspace(0, 360, steps)
theta_rad = np.radians(theta_deg)

# Full wave data (for the gray background tracks)
full_x = theta_deg
full_sin = np.sin(theta_rad)
full_cos = np.cos(theta_rad)

# Circle background
circle_bg_x = np.cos(np.linspace(0, 2*np.pi, 100))
circle_bg_y = np.sin(np.linspace(0, 2*np.pi, 100))

# 2. Initialize the Figure with Subplots
# --------------------------------------
# Row 1, Col 1: Unit Circle (We will make it span 2 rows via specs)
# Row 1, Col 2: Sine Wave
# Row 2, Col 2: Cosine Wave
fig = make_subplots(
    rows=2, cols=2,
    specs=[[{"rowspan": 2}, {}],
           [None, {}]],
    column_widths=[0.4, 0.6],
    subplot_titles=("Unit Circle", "Sine Wave (y-value)", "Cosine Wave (x-value)"),
    horizontal_spacing=0.1, vertical_spacing=0.15
)

# --- Add STATIC Background Traces ---
# 1. Circle Background
fig.add_trace(go.Scatter(x=circle_bg_x, y=circle_bg_y, mode='lines', line=dict(color='lightgray', dash='dash'), showlegend=False), row=1, col=1)
# 2. Sine Background
fig.add_trace(go.Scatter(x=full_x, y=full_sin, mode='lines', line=dict(color='lightgray', dash='dash'), showlegend=False), row=1, col=2)
# 3. Cosine Background
fig.add_trace(go.Scatter(x=full_x, y=full_cos, mode='lines', line=dict(color='lightgray', dash='dash'), showlegend=False), row=2, col=2)

# --- Add DYNAMIC Initial Traces (Theta = 0) ---
# We define these empty or at start pos so the animation has something to update.

# CIRCLE: Three separate lines for the triangle so they can be different colors
# Trace 3: Hypotenuse (Black)
fig.add_trace(go.Scatter(x=[0, 1], y=[0, 0], mode='lines', line=dict(color='black', width=2), name='Radius'), row=1, col=1)
# Trace 4: Adjacent/Cos (Blue)
fig.add_trace(go.Scatter(x=[0, 1], y=[0, 0], mode='lines', line=dict(color='blue', width=3), name='Cos(θ)'), row=1, col=1)
# Trace 5: Opposite/Sin (Red)
fig.add_trace(go.Scatter(x=[1, 1], y=[0, 0], mode='lines', line=dict(color='red', width=3), name='Sin(θ)'), row=1, col=1)
# Trace 6: Point P
fig.add_trace(go.Scatter(x=[1], y=[0], mode='markers', marker=dict(color='black', size=10), showlegend=False), row=1, col=1)

# SINE WAVE
# Trace 7: The "traced" path so far (Red)
fig.add_trace(go.Scatter(x=[0], y=[0], mode='lines', line=dict(color='red', width=3), showlegend=False), row=1, col=2)
# Trace 8: The leading point
fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='red', size=8), showlegend=False), row=1, col=2)

# COSINE WAVE
# Trace 9: The "traced" path so far (Blue)
fig.add_trace(go.Scatter(x=[0], y=[1], mode='lines', line=dict(color='blue', width=3), showlegend=False), row=2, col=2)
# Trace 10: The leading point
fig.add_trace(go.Scatter(x=[0], y=[1], mode='markers', marker=dict(color='blue', size=8), showlegend=False), row=2, col=2)

# 3. Create Frames
# ----------------
frames = []
for k in range(steps):
    t_rad = theta_rad[k]
    t_deg = theta_deg[k]
    
    # Calc current coords
    curr_cos = np.cos(t_rad)
    curr_sin = np.sin(t_rad)
    
    # Data for the "Traced" lines (slicing arrays up to current step)
    x_so_far = theta_deg[:k+1]
    sin_so_far = full_sin[:k+1]
    cos_so_far = full_cos[:k+1]

    frames.append(go.Frame(
        data=[
            # Update Circle components (Traces 3, 4, 5, 6 in global list, but indices 3-10 roughly)
            # Note: Plotly updates traces in order of addition after the static ones.
            # Hypotenuse: (0,0) to (cos, sin)
            go.Scatter(x=[0, curr_cos], y=[0, curr_sin]), 
            # Cosine Leg (Blue): (0,0) to (cos, 0)
            go.Scatter(x=[0, curr_cos], y=[0, 0]),       
            # Sine Leg (Red): (cos, 0) to (cos, sin)
            go.Scatter(x=[curr_cos, curr_cos], y=[0, curr_sin]), 
            # Point P
            go.Scatter(x=[curr_cos], y=[curr_sin]),      

            # Update Sine Wave
            # Path
            go.Scatter(x=x_so_far, y=sin_so_far),
            # Point
            go.Scatter(x=[t_deg], y=[curr_sin]),

            # Update Cosine Wave
            # Path
            go.Scatter(x=x_so_far, y=cos_so_far),
            # Point
            go.Scatter(x=[t_deg], y=[curr_cos]),
        ],
        name=str(int(t_deg)),
        traces=[3, 4, 5, 6, 7, 8, 9, 10] # Explicitly tell Plotly which traces to update
    ))

fig.frames = frames

# 4. Layout and Sliders
# ---------------------
sliders = [dict(
    active=0,
    currentvalue={"prefix": "Angle (θ): "},
    pad={"t": 50},
    steps=[dict(method='animate', 
                args=[[f.name], dict(mode='immediate', frame=dict(duration=0, redraw=True), transition=dict(duration=0))],
                label=f"{f.name}°") for f in frames]
)]

fig.update_layout(
    height=700, width=900,
    title_text="Visualizing Sine and Cosine",
    sliders=sliders,
    # Fix axes ranges so they don't jump around
    xaxis1=dict(range=[-1.5, 1.5], title="x (Cos)"), yaxis1=dict(range=[-1.5, 1.5], title="y (Sin)", scaleanchor="x", scaleratio=1),
    xaxis2=dict(range=[0, 360]), yaxis2=dict(range=[-1.5, 1.5]),
    xaxis3=dict(range=[0, 360], title="Angle (Degrees)"), yaxis3=dict(range=[-1.5, 1.5]),
    showlegend=True
)

fig.show()
:::
| **Category** | **Identity** | **Variations / Notes** |
| :--- | :--- | :--- |
| **Reciprocal** | $\csc \theta = \frac{1}{\sin \theta}$ | $\sec \theta = \frac{1}{\cos \theta}$ |
| **Quotient** | $\tan \theta = \frac{\sin \theta}{\cos \theta}$ | $\cot \theta = \frac{\cos \theta}{\sin \theta}$ |
| **Pythagorean** | $\sin^2 \theta + \cos^2 \theta = 1$ | $1 + \tan^2 \theta = \sec^2 \theta$ |
| **Even/Odd** | $\sin(-\theta) = -\sin \theta$ | $\cos(-\theta) = \cos \theta$ |
| **Sum/Diff** | $\sin(\alpha \pm \beta) = \sin \alpha \cos \beta \pm \cos \alpha \sin \beta$ | $\cos(\alpha \pm \beta) = \cos \alpha \cos \beta \mp \sin \alpha \sin \beta$ |
| **Double Angle** | $\sin(2\theta) = 2\sin \theta \cos \theta$ | $\cos(2\theta) = \cos^2 \theta - \sin^2 \theta$ |

:::{code-cell}
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
    question_id="sec-01-ch-A-q04",
    question_text="Periodicity and Waves Trigonometric functions like $\\sin(x)$  and $\\cos(x)$ repeat their values in a cycle. If a physical system (like a vibrating bond in a molecule) is modeled using a sine wave, what physical property does the period of the function represent? If you increase the frequency of vibration, how does that change the shape of the sine function?"
)
display(HTML(questions.render()))
#**Conceptual Question:** Given the possible quantum numbers is it possible to have zero vibrational energy in a quantum HO? Please justify and explain your answer. 
:::
### Simultaneous Equations
In physical science, you often encounter situations where multiple conditions must be satisfied at the same time. Mathematically, this leads to simultaneous equations—a set of equations containing multiple variables that must be solved together. The solution to a system of simultaneous equations is the specific set of values for the variables that makes all the equations true. Geometrically, if you have a system of two equations with two variables ($x$ and $y$), the solution corresponds to the point(s) where their graphs intersect. Here would be a simple example of two simultaneous equations. Recall, from algebra class there are several ways to solve these problems. In one method you can scale equations by multiplying all the terms by the same value and you can add and subtract equations to cancel certain variables. 

Let's consider the simple example here where we will solve by scaling and adding equations. Try on your own. 
::: {math}
:label:simultaneous_example
\begin{align}
2x + 3y &= 10 \\
x - y &= -3
\end{align}
:::
::::{dropdown} Click here for solution
:::{math}
:enumerated: false
\begin{align}
\text{First, multiply the second equation by 3}\\
\textcolor{red}{3}x - \textcolor{red}{3}y = \textcolor{red}{3}\left(-3\right)\\
3x - 3y = -9 \\
\text{now add the first equation to the scaled second equation from above}\\
2x + 3y = 10 \\
3x - 3y = -9 \\
2x + 3x + 3y - 3y = 1\\
5x = 1 \\
x = \frac{1}{5} \\
\text{Now subsititue our now known value of x into the original second equation!}\\
\frac{1}{5} - y = -3\\
-y = -3 -\frac{1}{5}\\
-y = -3\textcolor{red}{\frac{5}{5}} - \frac{1}{5}\\
-y = -\frac{15}{5} - \frac{1}{5}\\
-y = -\frac{16}{5}\\
y = \frac{16}{5}
\end{align}
:::
::::
#### Example, Spectroscopic analysis of a mixture
A classic application is determining the concentration of two different compounds (let's call them Compound X and Compound Y) in a single solution using UV-Vis spectroscopy. According to Beer’s Law, the total absorbance ($A$) of a mixture is the sum of the absorbances of the individual components.If we measure the absorbance at two different wavelengths (1$\lambda_1$ and 2$\lambda_2$), we can set up a system of two linear equations. Let's consider that concentration of compound X (M) is $x$ and the concentration of compound Y (M) is $y$. For our purposes at $450\:nm$ compound X absorbs strongly ($\epsilon = 100$) and compound Y absorbs weakly ($\epsilon = 20$) and the total absorbance is $0.80$. However, at $600\:nm$ compound Y absorbs weakly ($\epsilon = 10$) and compound Y absorbs strongly (\epsilon = 80). The total absorbance is $0.60$

Try writing out the system of equations. You can check your answer below. 
::::{dropdown} Click here for solution
:::{math}
:enumerated: false
\begin{align}
100x + 20 y = 0.80\\
10x + 80y = 0.60
\end{align}
:::
::::

Try solving this system of equations and see what you get for the concentrations of compound X and compound Y respectively. 

::::{dropdown} Click here for solution
:::{math}
:enumerated: false
\begin{align}
x = y \approx 0.0067\:M
\end{align}
:::
::::

The plot in {ref}`Beers_simultaneous` shows the above solution visually. We show a section of each line of all possible concentration combinations that would satisfy one of the wavelength measurements. The intersection is the only composition that explains both measurements.

:::{code-cell} python
:label: Beers_simultaneous 
:tags: [remove-input]
import matplotlib.pyplot as plt
import numpy as np

# Define a range of possible concentrations for Compound X
c_x = np.linspace(0, 0.012, 100)

# Equation 1 (450 nm): 100x + 20y = 0.80  =>  y = (0.80 - 100x) / 20
c_y_450 = (0.80 - 100 * c_x) / 20

# Equation 2 (600 nm): 10x + 80y = 0.60   =>  y = (0.60 - 10x) / 80
c_y_600 = (0.60 - 10 * c_x) / 80

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the lines
plt.plot(c_x, c_y_450, label='Absorbance at 450nm\n($100x + 20y = 0.80$)', color='#d62728', linewidth=2)
plt.plot(c_x, c_y_600, label='Absorbance at 600nm\n($10x + 80y = 0.60$)', color='#1f77b4', linewidth=2)

# Mark the intersection
plt.plot(0.00666, 0.00666, 'ko', markersize=10, zorder=5, label='Solution (Mix Composition)')
plt.text(0.007, 0.007, '  Intersection:\n  $C_X \\approx 0.0067$ M\n  $C_Y \\approx 0.0067$ M', fontsize=11)

# Formatting
plt.title('Determining Mixture Composition via Simultaneous Equations')
plt.xlabel('Concentration of Compound X (M)')
plt.ylabel('Concentration of Compound Y (M)')
plt.xlim(0, 0.01)
plt.ylim(0, 0.01)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.show()

:::
:::{code-cell}
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
    question_id="sec-01-ch-A-q05",
    question_text="Degrees of Freedom Imagine you have a mixture containing two unknown compounds, A and B. If you measure the total light absorbance of the mixture at just one wavelength, you have one equation with two unknown concentrations ($C_A$ and $C_B$). Why is this physically insufficient to determine the composition of the mixture, and why does adding a second measurement at a different wavelength allow you to solve it?"
)
display(HTML(questions.render()))
#**Conceptual Question:** Given the possible quantum numbers is it possible to have zero vibrational energy in a quantum HO? Please justify and explain your answer. 
:::