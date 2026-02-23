---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
numbering:
  enumerator: 2.%s
--- 
:::{code-cell} python
:tags: ["remove-input", "remove-output"]

import sys
import os

# This block MUST be at the top of your file.
# It finds the project root and adds it to the Python path.
# Adjust the number of ".." to match how many folders deep your file is.
try:
    cwd = os.getcwd()
    # e.g., use ("..", "..") for a file 2 levels deep.
    project_root = os.path.abspath(os.path.join(cwd, "..", "..", ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
except Exception as e:
    print(f"Error setting project path: {e}")
:::
# Chapter 2: Foundations of Quantum Mechanics
Welcome to the frontier of modern chemistry. To understand how atoms bond and how molecules vibrate, we have to abandon our "common sense" intuition derived from the macroscopic world and embrace a framework that is as elegant as it is counterintuitive: Quantum Mechanics.
Think of Quantum Mechanics not as a collection of random rules, but as a rigorous logical architecture. We begin with a set of Postulates—fundamental assumptions that act like the "axioms" of a geometry book. These provide the "rules of the game" for the subatomic world.

While the math behind these rules can get incredibly dense, our goal here isn't to get lost in formal proofs. For example, we won't spend our time proving the linear algebra behind Hermitian operators; instead, we will focus on why they matter to a chemist—specifically, how they allow us to extract real-world, measurable values (like energy or momentum) from wavefunctions that are often mathematically complex.

From Concepts to Consequences
By focusing on the "why" rather than the "proof," we can quickly move to the "how." Once we establish these conceptual underpinnings, we will explore their physical consequences through classic models:

Particle-in-a-Box (PIB): Discovering why energy is "quantized" and how confinement dictates electronic behavior.

Quantum Harmonic Oscillator (q-HO): Visualizing the physics of a vibrating chemical bond.

Rigid Rotator: Deciphering the mathematics of molecular "tumbling" and rotation as well as model the hydrogen atom. 

Mastering these postulates isn't about becoming a mathematician; it’s about learning the grammar of the universe. Once you understand the conceptual framework, the behavior of every electron and atom becomes a story you can actually read. 
:::{include} sec_1.0_postulates.md
:::
:::{include} sec_1.1_schrodinger_eqn.md
:::
:::{include} sec_4_operators.md
:::
:::{include} sec_2_PIB.md
:::
:::{include} sec_3_probability_density.md
:::
:::{include} sec_5_q_oscillator.md
:::
:::{include} sec_6_q_rr.md
:::












:::{code-cell} python
:tags: ["remove-input"]

from _ext.interactive_qa import QAManager
from IPython.display import display, HTML

# This renders the final control panel.
# Pass the desired title for the printed page here.
manager = QAManager(page_title="Chapter 2: Foundations of Quantum Mechanics")
display(HTML(manager.render()))
:::
%:::{code-cell} python
%:tags: ["remove-input", "remove-output"]

%import sys
%import os

%# This block MUST be at the top of your file.
%# It finds the project root and adds it to the Python path.
%# Adjust the number of ".." to match how many folders deep your file is.
%try:
%    cwd = os.getcwd()
%    # e.g., use ("..", "..") for a file 2 levels deep.
%    project_root = os.path.abspath(os.path.join(cwd, "..", "..", ".."))
%    if project_root not in sys.path:
%        sys.path.insert(0, project_root)
%except Exception as e:
%    print(f"Error setting project path: {e}")
%:::
## Practice Problems

You are free to do none, some, or all of these problems as you see fit. They are designed to mimic the mathematical manipulations and physical reasoning you will encounter in the rest of the book.

### 1. The Wavefunction and Probability
*Apply the Born Interpretation of the wavefunction $|\psi|^2$.*
1.  **Simple:** A wavefunction for a particle is given by $\psi$. If the value of the wavefunction at a specific point $x$ is $0.4 + 0.3i$, calculate the probability density $|\psi|^2$ at that point.
2.  **Intermediate:** For a particle in a 1D box of length $L$, the ground state wavefunction is $\psi_1 = \sqrt{\frac{2}{L}}\sin(\frac{\pi x}{L})$. Calculate the probability density at the exact center of the box ($x = L/2$).
3.  **Advanced:** Explain why a wavefunction that "blows up" (goes to infinity) as $x \to \infty$ is not physically acceptable. Which specific postulate or property of wavefunctions does this violate, and what would happen to the "probability budget" if we tried to use it?



### 2. Operators and Eigenvalues
*Connect physical observables to mathematical operations using $\hat{A}\psi = a\psi$.*
1.  **Simple:** The operator for position is simply "multiply by $x$." If our wavefunction is $\psi = e^{-ax^2}$, write the mathematical expression for $\hat{x}\psi$.
2.  **Intermediate:** The momentum operator is $\hat{p}_x = -i\hbar \frac{d}{dx}$. Show that the function $\psi = e^{ikx}$ is an eigenfunction of the momentum operator and determine the eigenvalue (the momentum $p$).
3.  **Advanced:** A "Hermitian" operator is required to have real eigenvalues. Why is this a fundamental requirement for any operator representing a physical observable (like energy or position) in a laboratory setting?

### 3. Particle in a Box (PIB)
*Explore energy quantization and nodes in a confined system.*
1.  **Simple:** Calculate the energy (in Joules) of an electron in the $n=1$ state of a 1D box that is $1.0\:\text{nm}$ long. 
2.  **Intermediate:** For a particle in a box, how many **internal nodes** (points where the probability of finding the particle is zero) are present in the $n=4$ state? Draw a rough sketch of $\psi_4$ to verify your answer.
3.  **Advanced:** If you decrease the length of the box by half, what happens to the energy of the ground state? Provide the ratio of $E_{\text{new}}/E_{\text{old}}$ and explain why "confinement" leads to higher kinetic energy.



### 4. Quantum Harmonic Oscillator (QHO)
*Analyze vibrational energy states and the zero-point energy.*
1.  **Simple:** A HCl molecule has a vibrational frequency of $\nu = 8.66 \times 10^{13}\:s^{-1}$. Calculate the "Zero-Point Energy" ($E_0$) for this bond in Joules.
2.  **Intermediate:** Calculate the energy required ($\Delta E$) to excite a molecule from the $v=1$ state to the $v=2$ state. How does this compare to the energy required to go from $v=10 \to v=11$ for an ideal harmonic oscillator?
3.  **Advanced:** Using the selection rule $\Delta v = \pm 1$, explain why we observe a single dominant absorption peak in the IR spectrum of a simple diatomic molecule, even though many different energy levels exist.

### 5. Rigid Rotator
*Examine rotational energy and the "picket fence" spectrum.*
1.  **Simple:** Calculate the rotational energy for a system in the $J=0$ state. Compare this to the zero-point energy of the Harmonic Oscillator. What does this imply about molecular rotation at absolute zero?
2.  **Intermediate:** A molecule has a moment of inertia $I = 1.45 \times 10^{-46}\:\text{kg m}^2$. Calculate the energy of the $J=1$ rotational state.
3.  **Advanced:** The energy spacing between levels $J$ and $J+1$ is $\Delta E = E_{J+1} - E_J = \frac{\hbar^2}{I}(J+1)$. Show that the energy difference between the $J=0 \to 1$ transition and the $J=1 \to 2$ transition is exactly $\frac{\hbar^2}{I}$. What does this tell us about the spacing of lines in a microwave spectrum?



### 6. Comparing the Models
*Synthesize the conceptual differences between translation, vibration, and rotation.*
1.  **Simple:** Which of the three models (PIB, QHO, or Rigid Rotator) has energy levels that are **equally spaced**? 
2.  **Intermediate:** You are looking at two different diatomic molecules. Molecule A has a very stiff bond (high $k$), and Molecule B has a very loose bond (low $k$). Which one will have a higher frequency absorption in its IR spectrum? (Assume masses are the same).
3.  **Advanced:** Imagine an electron in a conjugated dye molecule (PIB) and a vibrating CO molecule (QHO). If you "shrink" the system (decrease the box length $L$ for the PIB, or increase the stiffness $k$ for the QHO), what happens to the energy gap between the ground state and the first excited state in each case?