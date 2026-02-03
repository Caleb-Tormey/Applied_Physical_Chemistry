## Integrals

In physical science, we often encounter quantities that are not constant. A force might change as an object moves, or the density of an object might vary from its center to its edge. When dealing with such changing quantities, simple multiplication (like $\text{Distance} = \text{Velocity} \times \text{Time}$) fails. Instead, we must break the problem into infinitely small pieces where the quantity is roughly constant, and then add them all up. This process is called **Integration**.

### The Conceptual Meaning
Geometrically, the integral of a function $f(x)$ represents the **area under the curve** of that function. Physically, it represents an **accumulation**.

* If you integrate **velocity** over time, you accumulate **displacement**.
* If you integrate **power** over time, you accumulate **energy**.
* If you integrate **density** over volume, you accumulate **mass**.

The notation $\int f(x) \, dx$ tells us to sum up the value of $f(x)$ multiplied by a tiny width $dx$.

## Calculating Definite Integrals

While an *indefinite* integral gives you a general formula, a **definite** integral gives you a specific number. It answers the question: "How much changed between point A and point B?"

To calculate a definite integral $\int_{a}^{b} f(x) \, dx$, we use the **Fundamental Theorem of Calculus**. The procedure is:
1.  Find the anti-derivative function, $F(x)$.
2.  Evaluate it at the upper limit ($b$).
3.  Evaluate it at the lower limit ($a$).
4.  Subtract the lower result from the upper result: $F(b) - F(a)$.

### The Logic: Why do we subtract?
Why is the formula $F(b) - F(a)$? Why subtraction?

Think of the anti-derivative $F(x)$ as a running total—an "odometer" that measures the total area accumulated from some arbitrary starting point (let's call it $0$) up to $x$.



* **$F(b)$** represents the total area from the start up to the finish line ($b$).
* **$F(a)$** represents the total area from the start up to the starting line ($a$).

If we want the area *strictly* between $a$ and $b$, we take the total area up to $b$ and **cut off** (subtract) the area that happened before $a$.

$$\text{Area}(a \to b) = \text{Total Area}(0 \to b) - \text{Total Area}(0 \to a)$$

### Notation and Steps
We often use a square bracket notation to keep track of our work:
$$\int_{a}^{b} f(x) \, dx = \left[ F(x) \right]_{a}^{b} = F(b) - F(a)$$

### Example
Calculate the integral of $f(x) = 2x$ from $x=1$ to $x=3$.

1.  **Find the Anti-derivative:**
    The integral of $2x$ is $x^2$.
2.  **Set up the bracket:**
    $$\left[ x^2 \right]_{1}^{3}$$
3.  **Plug in Upper Limit ($3$):**
    $$3^2 = 9$$
4.  **Plug in Lower Limit ($1$):**
    $$1^2 = 1$$
5.  **Subtract (Upper - Lower):**
    $$9 - 1 = 8$$

The area under the curve between 1 and 3 is exactly 8 units.

In this course, I will not ask you to do anything beyond a simple integral by hand. However, you may be asked to solve problems by using computational tools like *Mathematica* or tables of integrals. Here are a few examples.

### Example 1: The Simple "Anti-Derivative"
Integration is often just differentiation in reverse. If you know the Power Rule for derivatives ($\frac{d}{dx}x^n = nx^{n-1}$), you can run it backward for integrals.

**Rule:**
$$\int x^n \, dx = \frac{x^{n+1}}{n+1}$$

**Problem:** Calculate $\int (3x^2 + 4x) \, dx$.

**Solution:**
We handle each term separately:
1.  For $3x^2$: Raise the power to 3, then divide by 3 $\rightarrow \frac{3x^3}{3} = x^3$.
2.  For $4x$: Raise the power to 2, then divide by 2 $\rightarrow \frac{4x^2}{2} = 2x^2$.

**Result:**
$$\int (3x^2 + 4x) \, dx = x^3 + 2x^2 + C$$
*(Note: We add $+C$ for indefinite integrals because the starting point is unknown.)*

### Example 2: Technique (U-Substitution)
Sometimes a function looks messy, but it is actually just a composite function (Chain Rule) in disguise. We can simplify it by changing the variable from $x$ to $u$.

**Problem:** Calculate $\int 2x \cos(x^2) \, dx$.

**Strategy:**
Notice that we have an $x^2$ inside the cosine, and a $2x$ outside. Since the derivative of $x^2$ is $2x$, this is a perfect candidate for substitution.

1.  **Set $u$:** Let $u = x^2$.
2.  **Find $du$:** Take the derivative. $du = 2x \, dx$.
3.  **Substitute:** Replace $x^2$ with $u$ and replace $2x \, dx$ with $du$.
    $$\int \cos(u) \, du$$
4.  **Solve:** The integral of $\cos(u)$ is $\sin(u)$.
    $$\sin(u) + C$$
5.  **Sub back:** Replace $u$ with $x^2$.

**Result:**
$$\sin(x^2) + C$$

### Example 3: The "Setup and Lookup"
In advanced thermodynamics and quantum mechanics, you will often face difficult integrals that have already been solved by mathematicians. Your job is not to re-invent the wheel, but to **match the pattern**.

**Problem:** Calculate the total probability of finding a particle if its distribution is given by a Gaussian function:
$$\int_{-\infty}^{\infty} e^{-3x^2} \, dx$$

**Strategy:**
1.  **Identify the Form:** This is a "Gaussian Integral." We look this up in a Table of Integrals (or ask Mathematica).
2.  **The General Solution:** The table says:
    $$\int_{-\infty}^{\infty} e^{-ax^2} \, dx = \sqrt{\frac{\pi}{a}}$$
3.  **Map the Variables:** Compare our problem to the table's solution.
    * Our problem has $e^{-3x^2}$.
    * The table has $e^{-ax^2}$.
    * Therefore, we identify that **$a = 3$**.

**Solution:**
We simply plug $a=3$ into the general result.

**Result:**
$$\sqrt{\frac{\pi}{3}}$$
### Example 4: Definite Integral with Limit Adjustment
In Quantum Mechanics, we often need to "normalize" a wavefunction. This frequently results in a definite integral where the variable inside the function is complex (like $\frac{\pi x}{L}$). When we use substitution on a **definite** integral, we must remember to transform the **boundaries ($a$ and $b$)** to match the new variable.

**Problem:** Calculate the integral from $0$ to $L$ for the square of a sine wave:
$$\int_{0}^{L} \sin^2\left(\frac{\pi x}{L}\right) \, dx$$

**Strategy:**
1.  **Lookup:** We find the general solution in a table:
    $$\int \sin^2(u) \, du = \frac{u}{2} - \frac{1}{4}\sin(2u)$$
2.  **Substitution:** Our integral has $\frac{\pi x}{L}$ instead of just $u$.
    * Let $u = \frac{\pi x}{L}$
    * Find $dx$: $du = \frac{\pi}{L} dx \rightarrow dx = \frac{L}{\pi} du$
3.  **Change the Limits:** This is the critical step. We must convert the $x$ boundaries into $u$ boundaries.
    * **Lower Limit:** When $x = 0$, $u = \frac{\pi (0)}{L} = 0$.
    * **Upper Limit:** When $x = L$, $u = \frac{\pi (L)}{L} = \pi$.

**New Setup:**
We rewrite the integral entirely in terms of $u$, pulling the constants out to the front:
$$\frac{L}{\pi} \int_{0}^{\pi} \sin^2(u) \, du$$

**Solution:**
Now we apply the table's result to our new limits ($0$ to $\pi$):
$$\frac{L}{\pi} \left[ \frac{u}{2} - \frac{1}{4}\sin(2u) \right]_{0}^{\pi}$$

Evaluate at the upper limit ($\pi$) minus the lower limit ($0$):
* At $\pi$: $\left(\frac{\pi}{2} - \frac{\sin(2\pi)}{4}\right) = \frac{\pi}{2} - 0 = \frac{\pi}{2}$
* At $0$: $\left(\frac{0}{2} - \frac{\sin(0)}{4}\right) = 0$

**Result:**
$$\frac{L}{\pi} \left( \frac{\pi}{2} \right) = \frac{L}{2}$$

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
    question_id="sec-01-ch-A-q09",
    question_text="Imagine you have a sensor measuring the flow rate of water into a beaker (in mL/second), but the flow rate is constantly changing (speeding up and slowing down). If you plot this Flow Rate vs. Time, why does the area under that curve (the integral) give you the total Volume of water in the beaker, even though you never measured volume directly?"
)
display(HTML(questions.render()))
:::