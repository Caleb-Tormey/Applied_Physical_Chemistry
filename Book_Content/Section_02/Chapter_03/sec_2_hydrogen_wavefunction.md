## Hydrogen Wavefunction

To find the allowed states for the electron in a hydrogen atom, we must solve the Time-Independent Schrödinger Equation (TISE) using the Coulomb potential:

:::{math}
:label: TISE_Hydrogen
\hat{H}\psi = E\psi
:::

Because the atom is spherical, it is far easier to work in **spherical coordinates** ($r, \theta, \phi$) than in standard Cartesian coordinates ($x, y, z$). In these coordinates, the Hamiltonian operator becomes quite complex, as it must account for the curvature of space:

:::{math}
:label: H_spherical
-\frac{\hbar^2}{2\mu} \nabla^2 \psi(r, \theta, \phi) - \frac{Ze^2}{4\pi\epsilon_0 r} \psi(r, \theta, \phi) = E \psi(r, \theta, \phi)
:::

### Separation of Variables
The "trick" to solving such a daunting equation is a technique called **separation of variables**. We assume the total wavefunction can be written as a product of independent functions:

:::{math}
\psi_{n,l,m_l}(r, \theta, \phi) = R_{n,l}(r) \times Y_{l,m_l}(\theta, \phi)
:::

1.  **The Radial Part ($R_{n,l}$):** This function describes how the electron density changes as you move away from the nucleus. It depends on the distance $r$ and is characterized by the quantum numbers $n$ and $l$. 
2.  **The Angular Part ($Y_{l,m_l}$):** Known as **Spherical Harmonics**, these functions describe the "surface" of the orbital. They depend on the angles $\theta$ and $\phi$ and are characterized by the quantum numbers $l$ and $m_l$.

### Solving the Radial Equation
When we separate the equation, we get a specific differential equation for the radial part. Its solutions are a combination of an exponential decay (the Gaussian-like tail) and **Associated Laguerre Polynomials**. 

This radial part is responsible for the **radial nodes** (spherical shells of zero probability) that you see in cross-sections of $2s$ or $3p$ orbitals.

### Solving the Angular Equation (Spherical Harmonics)
The angular part of the equation is identical to the math used for the **Rigid Rotator**. The solutions are the **Spherical Harmonics**, $Y_{l,m_l}(\theta, \phi)$. 



These functions are products of **Associated Legendre Polynomials** (in $\theta$) and an exponential term $e^{im_l\phi}$. While the math is rigorous, the physical result is what gives orbitals their characteristic symmetry:
* **Angular Nodes:** These are planes or cones where the probability of finding an electron is zero. The number of angular nodes is always equal to the orbital angular momentum quantum number, $l$.
* **Shape:** $l=0$ (s-orbitals) has 0 angular nodes (spherical). $l=1$ (p-orbitals) has 1 angular node (a planar node), creating the dumbbell shape. $l=2$ (d-orbitals) has 2 angular nodes.

### Table: Hydrogenic Radial Wavefunctions ($R_{n,l}$)

To simplify the expressions, we use the **Bohr Radius**, $a_0 = 52.9\text{ pm}$, and define $\sigma = \frac{Zr}{a_0}$.

| Orbital | $n, l$ | Radial Wavefunction $R_{n,l}(r)$ |
| :--- | :--- | :--- |
| **1s** | $1, 0$ | $2 \left( \frac{Z}{a_0} \right)^{3/2} e^{-\sigma}$ |
| **2s** | $2, 0$ | $\frac{1}{2\sqrt{2}} \left( \frac{Z}{a_0} \right)^{3/2} (2 - \sigma) e^{-\sigma/2}$ |
| **2p** | $2, 1$ | $\frac{1}{2\sqrt{6}} \left( \frac{Z}{a_0} \right)^{3/2} \sigma e^{-\sigma/2}$ |
| **3s** | $3, 0$ | $\frac{1}{9\sqrt{3}} \left( \frac{Z}{a_0} \right)^{3/2} (6 - 6\sigma + \sigma^2) e^{-\sigma/3}$ |
### The Angular Wavefunctions ($Y_{l,m_l}$)

The angular part of the equation is identical to the math used for the **Rigid Rotator** we studied in {ref}`rigid_rotator`. The solutions are the **Spherical Harmonics**.

While the associated Legendre polynomials used to calculate these are mathematically advanced, you are already familiar with their physical shapes—they define the $s, p, d,$ and $f$ orbitals.



| Orbital Type | $l, m_l$ | Spherical Harmonic $Y_{l,m_l}(\theta, \phi)$ | Shape Description |
| :--- | :--- | :--- | :--- |
| **s** | $0, 0$ | $\left( \frac{1}{4\pi} \right)^{1/2}$ | A constant; perfectly spherical. |
| **p** ($m_l=0$) | $1, 0$ | $\left( \frac{3}{4\pi} \right)^{1/2} \cos\theta$ | Oriented along the z-axis ($p_z$). |
| **p** ($m_l=\pm 1$) | $1, \pm 1$ | $\mp \left( \frac{3}{8\pi} \right)^{1/2} \sin\theta e^{\pm i\phi}$ | Complex functions in the xy-plane. |
| **d** ($m_l=0$) | $2, 0$ | $\left( \frac{5}{16\pi} \right)^{1/2} (3\cos^2\theta - 1)$ | Oriented along the z-axis ($d_{z^2}$). |

### Constructing the Total Wavefunction

To get the complete picture of an electron, we simply multiply the radial and angular parts together. For example, the full wavefunction for the hydrogen 1s ground state ($n=1, l=0, m_l=0$) is:

:::{math}
\psi_{1s} = R_{1,0} \times Y_{0,0} = \frac{1}{\sqrt{\pi}} \left(\frac{Z}{a_0}\right)^{3/2} e^{-Zr/a_0}
:::
---

### Connecting Math to Chemistry: Nodes and Energy

In quantum mechanics, there is a fundamental correlation between **curvature**, **nodes**, and **energy**. 

#### 1. The Total Node Count
The total number of nodes in a wavefunction is a direct measure of its energy. For a hydrogenic orbital, the total number of nodes is always $n-1$. These are split between the two components:
* **Radial Nodes:** $n - l - 1$
* **Angular Nodes:** $l$
* **Total Nodes:** $(n - l - 1) + l = n - 1$


The following table summarizes how the quantum numbers $n$ and $l$ determine the nodal structure and relative energy of hydrogenic orbitals. Notice that as the total number of nodes ($n-1$) increases, the energy of the orbital increases (becomes less negative).

| Orbital | $n$ | $l$ | Radial Nodes ($n-l-1$) | Angular Nodes ($l$) | Total Nodes ($n-1$) | Relative Energy |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1s** | 1 | 0 | 0 | 0 | 0 | Lowest ($E_1$) |
| **2s** | 2 | 0 | 1 | 0 | 1 | Higher ($E_2$) |
| **2p** | 2 | 1 | 0 | 1 | 1 | Higher ($E_2$) |
| **3s** | 3 | 0 | 2 | 0 | 2 | Higher ($E_3$) |
| **3p** | 3 | 1 | 1 | 1 | 2 | Higher ($E_3$) |
| **3d** | 3 | 2 | 0 | 2 | 2 | Higher ($E_3$) |



---

### Why Nodes Matter for Energy
In physical chemistry, a "node" represents a change in the algebraic sign (phase) of the wavefunction. Mathematically, this creates a steeper gradient (slope) in the wavefunction. According to the kinetic energy operator in the Schrödinger Equation:

:::{math}
\hat{T} = -\frac{\hbar^2}{2\mu} \nabla^2
:::

The $\nabla^2$ term (the Laplacian) measures the **curvature** of the wavefunction. More nodes mean more "wiggles," higher curvature, and therefore higher kinetic energy. 
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
question_id="sec-02-ch-3-q01",
question_text="Both the $3s$ and the $3d$ orbitals exist in the $n=3$ principal shell and therefore have the exact same total number of nodes. However, their physical shapes are entirely different. Compare the types of nodes (radial vs. angular) in these two orbitals, and explain how their specific geometries compensate to keep the total node count equal."
)
display(HTML(questions.render()))
:::
1. **In Hydrogen:** All orbitals with the same $n$ (like $3s, 3p, 3d$) have the same total number of nodes ($n-1 = 2$) and are **degenerate** (have the same energy).
2. **In Multielectron Atoms:** The *type* of node matters. Because radial nodes allow an electron to spend time closer to the nucleus (penetration), a $3s$ electron (2 radial nodes) feels a stronger nuclear pull than a $3d$ electron (0 radial nodes, 2 angular nodes), breaking the degeneracy.

As $n$ increases, the number of nodes increases. Mathematically, more nodes mean the wavefunction must "wiggle" more (higher kinetic energy). Physically, this corresponds to the electron having higher energy and being, on average, further from the nucleus.

#### 2. Increasing Orbital Energy
In a one-electron system like Hydrogen, the energy depends **only** on the principal quantum number $n$:
:::{math}
E_n = - \frac{hcR_H Z^2}{n^2}
:::
As $n$ increases ($1 \to 2 \to 3$), the energy $E_n$ becomes less negative (closer to zero), meaning the electron is less tightly bound to the nucleus. 

#### 3. The Exponential Decay ($e^{-\sigma/n}$)
This "tail" ensures the wavefunction goes to zero as $r \to \infty$. Notice the $n$ in the denominator: as $n$ increases, the decay happens more slowly. This is why a $3s$ orbital is much larger than a $1s$ orbital.

### Radial Distribution Function (RDF)
While $R(r)$ tells us the amplitude, we use the **Radial Distribution Function**, $P(r) = 4\pi r^2 [R(r)]^2$, to find the probability of finding the electron at a distance $r$.



The "humps" in the RDF for $s$ orbitals allow them to **penetrate** inner electron shells. In multielectron atoms, this penetration breaks the energy degeneracy of the $l$ states, making $E_{2s} < E_{2p}$.
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
question_id="sec-02-ch-3-q03",
question_text="For an electron in a $1s$ orbital, the radial wavefunction $R(r)$ is at its absolute maximum precisely at the nucleus ($r=0$). However, the Radial Distribution Function $P(r)$ is exactly zero at the nucleus. Explain this apparent contradiction. Where is the electron actually most likely to be found, and why?"
)
display(HTML(questions.render()))
:::
### Visualizing Spherical Harmonics
The applet below allows you to see the 3D shapes generated by these angular wavefunctions. Note how $l$ and $m_l$ dictate the orientation and nodal planes.

:::{include} interactive_code/spherical_harmonics.md
:::

**Note on Complex Functions:** Mathematically, the $m_l$ wavefunctions for $p$ and $d$ orbitals are complex (containing $i$). To get real, observable shapes like $\text{p}_x$ or $\text{d}_{x^2-y^2}$, we take **linear combinations** (sums and differences) of these complex wavefunctions.

:::{include} interactive_code/orbital_visual.md
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
question_id="sec-02-ch-3-q04",
question_text="When solving the angular part of the Schrödinger equation, the spherical harmonics for $m_l = +1$ and $m_l = -1$ are mathematically complex (they contain $i$). Explain conceptually what mathematical operation we must perform on these complex functions to generate the familiar, observable $p_x$ and $p_y$ orbital shapes, and why this is allowed in quantum mechanics."
)
display(HTML(questions.render()))
:::
### Hydrogenic Atoms
The solutions for Hydrogen ($Z=1$) generalize to any one-electron system (e.g., $\text{He}^+$, $\text{Li}^{2+}$). The energy scales by $Z^2$, and the orbitals "contract" toward the nucleus as $Z$ increases.

:::{math}
E_n \approx -13.6 \text{ eV} \left( \frac{Z^2}{n^2} \right)
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
question_id="sec-02-ch-3-q05",
question_text="Consider the $1s$ orbital for a neutral Hydrogen atom ($Z=1$) and a $Li^{2+}$ ion ($Z=3$). Without doing any calculations, explain how the physical size of the $1s$ orbital and the energy of the electron will differ between these two systems. What drives this physical change?"
)
display(HTML(questions.render()))
:::