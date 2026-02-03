(math_derivatives)=
## Derivatives

In chemistry, we are rarely interested in static pictures; we care fundamentally about change. In kinetics, we ask how the concentration of a reactant changes over time as a reaction proceeds. In thermodynamics, we need to know how the pressure of a gas responds to changes in temperature to predict engine efficiency. In quantum mechanics, we analyze how the probability density of an electron changes as we move away from the nucleus. To answer these questions quantitatively, we rely on the calculus of derivatives. Fundamentally, a derivative is a precise mathematical tool for describing a rate of change.

The most intuitive way to understand a derivative is by looking at the slope of a curve. If we plot a function—for instance, concentration versus time—the "steepness" of the line at any given moment tells us exactly how fast the reaction is occurring.



[Image of slope rise over run diagram]


We can begin by looking at the average rate of change. If we want to know the average speed of a reaction over an hour, we can pick two points on the curve ($t_1$ and $t_2$), measure the concentration at each, and divide the change in concentration by the time elapsed. Geometrically, this is equivalent to drawing a straight line that cuts through the curve at two distinct points, known as a **Secant Line**.

However, chemical phenomena often happen in the blink of an eye, and we frequently need to know the rate at a specific instant rather than an average over time. To find this instantaneous rate, we must shrink the distance between our two measurement points. As the gap between the points gets smaller and smaller—approaching zero—the Secant Line morphs into a **Tangent Line**, a line that just grazes the curve at a single point.

Mathematically, we define this "shrinking gap" using a limit. This limit allows us to calculate the slope of the tangent line at any specific point $x$, which we call the derivative, denoted as $f'(x)$ or $\frac{df}{dx}$. It is crucial to remember that the derivative is not just a single number; it is a function itself. At every point on our original curve, there is a specific slope. If we collect all these slope values and plot them, we generate a new curve: the derivative function. For example, where the original graph has a peak (a maximum) or a valley (a minimum), the tangent line is perfectly flat, meaning the derivative is zero.

:::{include} interactive_code/derivative_sec_4.md
:::
### Rules for Differentiation (One Variable)

We will not prove all of these rules here, as that is better reserved for a dedicated calculus course. Instead, we provide a summary of the essential rules for one-dimensional derivatives that you will frequently encounter in this text.



#### 1. Basic properties and Power Rule
* **Derivative of a constant:** The rate of change of a constant is zero.
    If $f(x) = c$, then:
    $$\frac{df}{dx} = 0$$
    *Example:* If $f(x) = 5$, then $f'(x) = 0$.

* **The Power Rule:** For a function of the form $f(x) = x^n$, where $n$ is any real number (positive, negative, or fractional):
    :::{math}
    :label: power_rule
    \frac{d}{dx}\left(x^n\right) = nx^{n-1}
    :::
    *Example:* If $f(x) = \frac{1}{x^2} = x^{-2}$, then $f'(x) = -2x^{-3} = -\frac{2}{x^3}$.

* **Linearity (Sum and Difference):** The derivative of a sum is the sum of the derivatives.
    $$\frac{d}{dx}\left[g(x) + f(x)\right] = g'(x) + f'(x)$$
    *Example:*
    $$\frac{d}{dx}\left(2x^2 + \frac{2}{x^3}\right) = \frac{d}{dx}(2x^2) + \frac{d}{dx}(2x^{-3}) = 4x - 6x^{-4}$$

#### 2. Exponential and Logarithmic Functions
* **The Natural Exponential:** The derivative of $e^x$ is unique because it is its own derivative. When a constant $w$ is involved in the exponent:
    $$\frac{d}{dx} e^{wx} = w e^{wx}$$
    *Example:* $\frac{d}{dx} \left( e^{-3\pi x} \right) = -3\pi e^{-3\pi x}$.

* **General Exponential (Power of $x$ base $a$):** *This covers the "Derivative of a power of x" section you requested.* If the base is a constant $a$ rather than $e$ (e.g., $2^x$ or $10^x$):
    $$\frac{d}{dx} a^x = a^x \ln(a)$$
    Note that if $a=e$, this reduces to the standard rule since $\ln(e)=1$.

* **Natural Logarithm:**
    $$\frac{d}{dx} \ln(x) = \frac{1}{x}$$

#### 3. Trigonometric Functions
Here is a reference list for the derivatives of trigonometric functions. Note the pattern regarding the "co-" functions (cosine, cotangent, cosecant), which always introduce a negative sign. We include a constant $k$ to demonstrate the chain rule application.

* $\frac{d}{dx} \sin(kx) = k\cos(kx)$
* $\frac{d}{dx} \cos(kx) = -k \sin(kx)$
* $\frac{d}{dx} \tan(kx) = k\sec^2(kx)$
* $\frac{d}{dx} \cot(kx) = -k\csc^2(kx)$
* $\frac{d}{dx} \sec(kx) = k\sec(kx) \tan(kx)$
* $\frac{d}{dx} \csc(kx) = -k\csc(kx) \cot(kx)$

#### 4. Product and Quotient Rules
When functions are multiplied or divided, we cannot simply differentiate each part separately. We must use specific rules.

* **Product Rule:**
    $$\frac{d}{dx}\left[ f(x)g(x) \right] = f'(x)g(x) + f(x)g'(x)$$
    *Example:* Let $y = x^2\sin(x)$.
    $$\frac{dy}{dx} = (2x)(\sin x) + (x^2)(\cos x) = 2x\sin x + x^2\cos x$$

* **Quotient Rule:**
    For a ratio of two functions $\frac{f(x)}{g(x)}$:
    $$\frac{d}{dx} \left[ \frac{f(x)}{g(x)} \right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}$$
    *Mnemonic:* "Low d-High minus High d-Low, over Low Low."

    *Example:* Let $y = \frac{e^x}{x^2}$.
    $$\frac{dy}{dx} = \frac{(e^x)(x^2) - (e^x)(2x)}{(x^2)^2} = \frac{x e^x (x - 2)}{x^4} = \frac{e^x(x-2)}{x^3}$$

#### 5. The Chain Rule
The chain rule allows us to differentiate **composite functions**, $f(g(x))$. It states that you differentiate the "outer" function first, leaving the inside alone, and then multiply by the derivative of the "inner" function.

$$\frac{d}{dx} f\big(g(x)\big) = f'\big(g(x)\big) \cdot g'(x)$$

*Example:* Differentiate $y = \sin(x^2)$.
1.  Identify outer function: $f(u) = \sin(u) \rightarrow f'(u) = \cos(u)$.
2.  Identify inner function: $g(x) = x^2 \rightarrow g'(x) = 2x$.
3.  Apply rule:
    $$\frac{dy}{dx} = \cos(x^2) \cdot 2x = 2x\cos(x^2)$$

#### 6. Derivatives of Even and Odd Functions
Symmetry properties are very useful in quantum mechanics and physics. The derivative operator affects the parity (symmetry) of a function:

* **Derivative of an Even Function:**
    If $f(x)$ is **even** ($f(-x) = f(x)$), its derivative $f'(x)$ is **odd**.
    * *Example:* $f(x) = x^2$ (even). $f'(x) = 2x$ (odd).
    * *Visual check:* An even function is symmetric about the y-axis. At $x=0$, the slope (derivative) must be zero (which is consistent with an odd function passing through the origin).

* **Derivative of an Odd Function:**
    If $f(x)$ is **odd** ($f(-x) = -f(x)$), its derivative $f'(x)$ is **even**.
    * *Example:* $f(x) = x^3$ (odd). $f'(x) = 3x^2$ (even).

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
    question_id="sec-01-ch-A-q08",
    question_text="Instantaneous Change If you have a plot of a chemical reaction where the y-axis is $\\textbf{Concentration of Product}$ and the x-axis is $\\textbf{Time}$, the curve will eventually flatten out as the reaction finishes. If the derivative represents the $\\textbf{slope}$ of this curve, what physical quantity does the derivative represent, and why does the derivative approach zero as the curve flattens out?"
)
display(HTML(questions.render()))
:::