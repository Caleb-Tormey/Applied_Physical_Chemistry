## Integrals
In physical science, we often encounter quantities that are not constant. A force might change as an object moves, or the density of an object might vary from its center to its edge. When dealing with such changing quantities, simple multiplication (like $\text{Distance} = \text{Velocity} \times \text{Time}$) fails. Instead, we must break the problem into infinitely small pieces where the quantity is roughly constant, and then add them all up. This process is called Integration.

The Conceptual MeaningGeometrically, the integral of a function $f(x)$ represents the area under the curve of that function. Physically, it represents an accumulation.If you integrate velocity over time, you accumulate displacement.If you integrate power over time, you accumulate energy.If you integrate density over volume, you accumulate mass.The notation $\int f(x) \, dx$ tells us to sum up the value of $f(x)$ multiplied by a tiny width $dx$.

In this course I will not ask you to do anything beyond a simple integral by hand. However, you may be asked to solve problems by using computational tools like \textit{Mathematica} or tables of integrals. Here are a couple of examples...
:::{code-cell} python
:label: Integral_Area_under_curve
:tags: [remove-input]
import matplotlib.pyplot as plt
import numpy as np

# Define a "generic" looking function
def f(x):
    return np.sin(x) + 0.1*x**2 + 2

# Set up the domain
x = np.linspace(0, 6, 100)
y = f(x)

# Define the integration limits (a and b)
a = 1.5
b = 4.5

# Create the plot
plt.figure(figsize=(8, 5))

# Plot the function line
plt.plot(x, y, color='blue', linewidth=2, label='$f(x)$')

# Shade the area under the curve between a and b
ix = np.linspace(a, b, 100)
iy = f(ix)
plt.fill_between(ix, iy, color='skyblue', alpha=0.4)

# Add vertical dashed lines for limits
plt.vlines([a, b], 0, [f(a), f(b)], color='gray', linestyle='--')

# Add Labels
plt.text(a, -0.3, '$a$', horizontalalignment='center', fontsize=14)
plt.text(b, -0.3, '$b$', horizontalalignment='center', fontsize=14)
plt.text((a+b)/2, 1.5, r'Area = $\int_a^b f(x)dx$', horizontalalignment='center', fontsize=14)

plt.xlabel('$x$', fontsize=12)
plt.ylabel('$f(x)$', fontsize=12)

# Clean up the axes (remove numbers for a "textbook" look)
plt.xticks([])
plt.yticks([])
plt.ylim(0, 5)
plt.xlim(0, 6)

# Draw the main axes
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Remove top and right borders
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.title('The Integral as Area Under the Curve', fontsize=14)
plt.show()
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
    question_id="sec1-chA-q3",
    question_text="This is the third question about this section."
)
display(HTML(questions.render()))
:::