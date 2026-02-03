## Functions

In another example, if we look at the ideal gas law $PV = nRT$ we can ask how the pressure will vary with changing volume at constant moles (n) and constant temperature (T). To solve this we must manipulate the equation to get pressure (P) and volume (V) on separate sides of the equation. Because we are looking at how pressure is changing with volume we will want to have pressure on the left-hand side, abbreviated LHS, and then have volume on the right-hand side, abbreviated RHS. This will be done by dividing 
One thing we will note which we manipulate an equation to put one variable on the LHS and one variable on the RHS is we are creating a function. Plainly speaking, a function is a little mathematical machine that takes an input, what we call the **independent** variable, and spits out another variable, what we call the **dependent** variable. Sometimes functions will be clearly spelled out. For example, we will see when we get to wave-functions where we declare them as $\psi\left ( x \right)$. In this case $\psi$ is the dependent variable and is a function of $x$ which is the independent variable. Sometimes, the relationship, dependent and independent variables, is not explicitly stated, and we must make that inference. This is the case for our ideal gas law example above. For that example, we could say that the pressure is a function of the volume. Stated more directly $P\left(V\right) = \frac{nRT}{V}$. From this example you can also see that we could additionally make functions of the pressure as it relates to varying the temperature (T) or the number of moles (n). 

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
    question_id="sec-01-ch-A-q06",
    question_text="In thermodynamics, we say that Pressure is a $\\textbf{function}$ of Temperature and Volume, written as $P(T, V)$. In terms of physical experiments, what does this functional notation imply about the reproducibility of your results if you set $T$ and $V$ to the exact same values in two different experiments?"
)
display(HTML(questions.render()))
#**Conceptual Question:** Given the possible quantum numbers is it possible to have zero vibrational energy in a quantum HO? Please justify and explain your answer. 
:::
### Even and Odd Functions

Even and odd functions are characterized by their symmetry properties. An even function is symmetric with respect to the y-axis, meaning its graph remains unchanged if reflected across the y-axis. Mathematically, a function $f(x)$ is even if $f(-x) = f(x)$ for all $x$ in its domain. An odd function has rotational symmetry about the origin, meaning if you rotate the graph 180 degrees around $(0,0)$, it looks the same. A function $f(x)$ is odd if $f(-x) = -f(x)$. However, these are special cases; most functions are neither even nor odd, meaning they satisfy neither of these specific symmetry conditions (e.g., $f(-x) \neq f(x)$ and $f(-x) \neq -f(x)$). Here is a visual representation of these three types of functions:Even: $f(x) = x^2$ (Symmetric across the y-axis)Odd: $f(x) = x^3$ (Symmetric about the origin) and Neither: $f(x) = x^2 + 3x$ (Lacks both symmetries)

:::{code-cell} python
:label: Even_odd_neither_functions 
:tags: [remove-input]
import matplotlib.pyplot as plt
import numpy as np

# Define the x-axis values
# Zooming in (e.g. -5 to 5) makes the local asymmetry of the 'neither' function more obvious
x = np.linspace(-5, 5, 400)

# Define the functions
y_even = x**2
y_odd = x**3
y_neither = x**2 + 3*x  # Increased the linear coefficient to make asymmetry clear

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the even function (Symmetric across y-axis)
plt.plot(x, y_even, label='Even: $f(x) = x^2$', color='#1f77b4', linewidth=2)

# Plot the odd function (Symmetric about origin)
plt.plot(x, y_odd, label='Odd: $f(x) = x^3$', color='#ff7f0e', linewidth=2)

# Plot the neither function (No symmetry)
plt.plot(x, y_neither, label='Neither: $f(x) = x^2 + 3x$', color='#2ca02c', linewidth=2, linestyle='--')

# Add visual aids (axes, grid, etc)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.title('Comparison of Even, Odd, and Neither Functions')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

# Set limits for clear visualization
plt.xlim(-5, 5)
plt.ylim(-30, 30)

plt.show()

:::

% Concept question

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
    question_id="sec-01-ch-A-q07",
    question_text="In quantum mechanics, particles often exist in symmetric boxes or potentials centered at $x=0$. If the wave function describing a particle is an Odd function (meaning $f(-x) = -f(x)$), what is the value of the function exactly at the center ($x=0$)? What might this imply about the probability of finding the particle exactly in the center of the box?"
)
display(HTML(questions.render()))
:::