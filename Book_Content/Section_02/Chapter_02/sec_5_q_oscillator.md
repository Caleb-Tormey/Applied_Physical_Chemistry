## Quantum Harmonic Oscillator

If you imagine a spring with a mass on it, we can compress the spring and then let it go. The mass will move back and forth in a harmonic motion. If there are no other forces acting on the system (like friction) it will continue forever. 

Recall that we can determine the force of the system based on the potential by the equation $F(x) = -\frac{dV(x)}{dx}$. In this case, we will look at the potential as being defined by **Hooke's Law**, where it follows a quadratic form in equation {ref}`Hooke_pot` and the restoring force, $F$, is defined by equation {ref}`Hooke_law`.

:::{math}
:label: Hooke_pot
V(x) = \frac{1}{2}kx^2
:::

:::{math}
:label: Hooke_law
F = -kx
:::

Continuing to think about our system, we imagine the harmonic motion proceeding at some rate. We define the angular frequency, $\omega$, for the system to be how many radians it goes per second. Here, $k$ is the spring constant which determines how stiff the spring is and $m$ is the mass.

:::{math}
:label: angular_freq
\omega = \sqrt{\frac{k}{m}}
:::

:::{math}
:label: HO_freq
\nu = \frac{1}{2\pi}\omega = \frac{1}{2\pi}\sqrt{\frac{k}{m}}
:::

For something like a diatomic system, we can simplify the system by thinking about the single motion having contributions of the two masses. When the two masses are identical, each mass contributes exactly half the motion. When one is **MUCH** larger than the other, all the motion is due only to the smaller mass, since the larger mass will not move very much. To say this mathematically, we use the **reduced mass**, $\mu$:

:::{math}
:label: reduced_mass
\mu = \frac{m_1m_2}{m_1+m_2}
:::

---

### Wavefunction for the Quantum Harmonic Oscillator

To find the wavefunctions for this system, we solve the Time-Independent Schrödinger Equation using the quadratic potential. Solving this involves sophisticated calculus (using power series and Hermite polynomials) that is **beyond the scope of this course**. However, we can look at the resulting wavefunctions to understand their behavior:

$$\psi_v(x) = N_v H_v(\alpha x) e^{-\frac{\alpha^2 x^2}{2}}$$

#### The Normalization Constant ($N_v$)
In the previous section on the **Postulates of Quantum Mechanics**, we learned that for a wavefunction to be physically meaningful, the total probability of finding the particle somewhere in space must be exactly 100% (or 1). Mathematically, this is expressed by the integral of the probability density:

$$\int_{-\infty}^{\infty} |\psi(x)|^2 dx = 1$$

To satisfy this requirement, we include a **normalization constant**, $N_v$. For the Harmonic Oscillator, this constant depends on the quantum number $v$ and is defined as:

$$N_v = \left( \frac{\alpha}{\pi^{1/2} 2^v v!} \right)^{1/2}$$

**Sample Calculation: $v=0$ vs $v=1$**
Let's see how this constant changes as we move up the energy ladder:

* **For $v=0$ (Ground State):**
  $N_0 = \left( \frac{\alpha}{\pi^{1/2} \cdot 2^0 \cdot 0!} \right)^{1/2} = \left( \frac{\alpha}{\pi^{1/2}} \right)^{1/2}$
  *(Note: $2^0=1$ and $0!=1$)*

* **For $v=1$ (First Excited State):**
  $N_1 = \left( \frac{\alpha}{\pi^{1/2} \cdot 2^1 \cdot 1!} \right)^{1/2} = \left( \frac{\alpha}{2\pi^{1/2}} \right)^{1/2}$

Without this constant, our "probability budget" would be incorrect, and we would not be able to accurately calculate physical properties like the average position or momentum.

---

**Conceptual Breakdown:**
* **The Gaussian ($e^{-x^2}$):** This "bell curve" ensures the wavefunction decays to zero as you move away from the center. This is vital for keeping the function **finite** and **well-behaved**, ensuring the particle remains localized near the potential well.
* **Hermite Polynomials ($H_v$):** These are mathematical functions that dictate the shape of the wave between the boundaries. Specifically, they determine the number of nodes; just like the Particle in a Box, a state with quantum number $v$ will have exactly $v$ nodes.
* **The "Leaking" Effect:** Unlike the Particle in a Box where the walls were infinite, the quadratic potential is finite. As seen in the interactive plot below, this leads to a non-zero probability that the particle exists beyond the **classical turning points**—a phenomenon where the particle "tunnels" into a region that would be classically impossible to reach.

:::{code-cell} python
:tags: ["remove-input"]
:label: interactive_qho_viz_final
# [Include the interactive QHO widget code here]
:::

:::{include} interactive_code/qho_turning_points.md
:::

### Quantum Harmonic Oscillator Energy States

The energy of a quantum harmonic oscillator is given by:

:::{math}
:label: QHO_energy
E_v = \left(v + \frac{1}{2}\right)h\nu \quad v = 0, 1, 2, \dots
:::

#### Key Features:
1.  **Zero-Point Energy:** Even at $v=0$, the energy is $E_0 = \frac{1}{2}h\nu$. A molecule **always** vibrates, even at absolute zero. This is a direct consequence of the Heisenberg Uncertainty Principle; if the vibration stopped completely, we would know both the exact position and momentum of the atoms simultaneously.
2.  **Constant Spacing:** Unlike the PIB where gaps increase with $n$, the energy difference here is constant:
    $$\Delta E = E_{v+1} - E_v = h\nu$$



#### Selection Rules: $\Delta v = \pm 1$
In order for a molecule to absorb or emit a photon and transition between vibrational states, it must follow specific "selection rules." For an ideal harmonic oscillator, the rule is:

$$\Delta v = \pm 1$$

**Why this rule?**
* **The Dipole Requirement:** First, the vibration must cause a change in the molecule's **dipole moment**. This is why homonuclear diatomics like $N_2$ or $O_2$ are "IR inactive"—their vibration doesn't shift their charge distribution.
* **The Harmonic Symmetry:** Mathematically, the $\pm 1$ restriction arises from the symmetry of the harmonic oscillator wavefunctions. Because of the way the Hermite polynomials interact in the transition moment integral (the "sandwich" integral we discussed earlier), the probability of jumping more than one level at a time (e.g., $v=0 \rightarrow v=2$) is zero for a perfect spring.

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
    question_id="sec-2-ch-2-q01",
    question_text="Given the possible quantum numbers is it possible to have zero vibrational energy in a quantum HO? Please justify and explain your answer. "
)
display(HTML(questions.render()))
#**Conceptual Question:** Given the possible quantum numbers is it possible to have zero vibrational energy in a quantum HO? Please justify and explain your answer. 
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
    question_id="sec-2-ch-2-q02",
    question_text="Given the possible quantum numbers is it possible to have zero vibrational energy in a quantum HO? Please justify and explain your answer. "
)
display(HTML(questions.render()))
#**Conceptual Question:** Given your answer to the previous
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
    question_id="sec-2-ch-2-q03",
    question_text="Let's consider running a mental experiment. What if we  "
)
display(HTML(questions.render()))
#**Conceptual Question:** Let's consider running a mental experiment. What if we 
:::
### Spectroscopy Applications

Because the energy spacing $\Delta E$ is constant, this model is the basis for **Infrared (IR) Spectroscopy**. When a molecule absorbs a photon matching $h\nu$, it jumps to the next energy level. Measuring this frequency allows us to determine the bond's "stiffness" or spring constant $k$.

Further and more detailed discussion of infra-red spectroscopy will be saved for {ref}`IR_Raman`.