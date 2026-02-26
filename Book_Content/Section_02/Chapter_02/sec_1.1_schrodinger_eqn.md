## Schrödinger's Equation 

When we reviewed Newton's laws, one thing that wasn't mentioned was that his formulation of the definition of force is something that, while well-reasoned, is not derived but rather proposed. It serves as a postulate; all other classical laws are derived from that starting point. Historically, other thinkers had proposed that force was proportional to velocity rather than acceleration, but experimental reality confirmed Newton's $F=ma$. 

Erwin Schrödinger proposed his equation in much the same manner. It is the fundamental postulate of motion for the quantum world. There are two forms of the Schrödinger equation we will discuss, though we will primarily focus on the version that describes stable, stationary states. 

The first is the **Time-Dependent Schrödinger Equation (TDSE)**, shown in equation {ref}`TDSE`. The second and more common form used in chemistry is the **Time-Independent Schrödinger Equation (TISE)**, shown in equation {ref}`TISE`.

:::{math}
:label: TDSE
i\hbar\frac{\partial}{\partial t}\Psi(x,t) = \hat{H}\Psi(x,t)
:::



$\hat{H}$ is known as the **Hamiltonian operator**. As we will see, an operator is a mathematical instruction that tells us how to extract information from a system—in this case, information about the total energy. The Hamiltonian is composed of two parts: the kinetic energy, $-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}$, and the potential energy, $V(x,t)$. Combined, they form the Hamiltonian defined in one dimension in equation {ref}`1D_Hamiltonian`:

:::{math}
:label: 1D_Hamiltonian
\hat{H} = -\frac{\hbar^2}{2m}\frac{d^2}{d x^2} + V(x)
:::

$\Psi(x,t)$ and $\psi(x)$ are the **wavefunctions**. The wavefunction is the most critical object in quantum mechanics because it encapsulates all possible information about a system. It is important to remember that the wavefunction is a purely mathematical object; it is not directly observable. We will discuss how to extract measurable values from it in section {ref}`operators_and_expectation_values`.

:::{math}
:label: TISE
\hat{H}\psi(x) = E\psi(x)
:::

We will almost exclusively look at the TISE because the chemical systems we study—atoms and molecules—are typically stable over long time frames. The TDSE becomes vital when the system changes with time, such as during photon absorption, fluorescence, or the kinetics of bond formation.

---

### The Eigenvalue Problem

You may notice that the TISE has a very specific mathematical structure: 

$$\text{(Operator)} \times \text{(Function)} = \text{(Constant)} \times \text{(Same Function)}$$

This is known as an **Eigenvalue Problem (EVP)**. In linear algebra and calculus, an operator $\hat{A}$ has an **eigenfunction** $f(x)$ if operating on that function returns the original function multiplied by a scalar constant $a$, called the **eigenvalue**.

$$\hat{A}f(x) = af(x)$$

In the context of the TISE, the Hamiltonian is the operator, the wavefunction is the eigenfunction, and the **Total Energy ($E$)** is the eigenvalue. This means that if you know the wavefunction, you can "measure" the energy of the system by simply applying the Hamiltonian operator to it.



#### Examples: Is it an Eigenfunction?

To determine if a function is an eigenfunction of an operator, we simply perform the math and see if we get the original function back (multiplied only by a constant).

**Example 1: A Successful Match**
Is $f(x) = e^{5x}$ an eigenfunction of the derivative operator $\frac{d}{dx}$?
1. Apply the operator: $\frac{d}{dx}(e^{5x}) = 5e^{5x}$
2. Analyze the result: We have the original function ($e^{5x}$) multiplied by a constant ($5$).
3. **Conclusion:** Yes, $e^{5x}$ is an eigenfunction with an eigenvalue of 5.

**Example 2: A Failure to Match**
Is $f(x) = x^2$ an eigenfunction of the derivative operator $\frac{d}{dx}$?
1. Apply the operator: $\frac{d}{dx}(x^2) = 2x$
2. Analyze the result: We do **not** have the original function ($x^2$). The function has changed its form entirely.
3. **Conclusion:** No, $x^2$ is not an eigenfunction of this operator.

In chemistry, we are constantly hunting for wavefunctions that are eigenfunctions of the Hamiltonian, because those functions represent the stable energy states (orbitals) of atoms and molecules.

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
question_id="sec-02-ch-2-q02",
question_text="If a wavefunction is an eigenfunction of an operator (like the Hamiltonian), a single measurement will always return the same eigenvalue. However, if it is NOT an eigenfunction, we must use an expectation value. Conceptually, what does the expectation value represent in terms of multiple measurements?"
)
display(HTML(questions.render()))
:::