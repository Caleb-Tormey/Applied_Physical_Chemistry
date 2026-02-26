## Rigid Rotator

The rigorous rigid rotator will be used to model the hydrogen atom, and so further discussion of the wavefunction solutions to this system will be discussed in section {ref}`hydrogen_atom`. Rather, we are just going to use a simplified model called the "particle-on-a-ring" to look at quantized rotational motion. 

Before we look at the quantum analog, let's start by looking at classical angular momentum. Recall we defined some basic principles of angular motion in the physics review chapter on {ref}`linear_angular_momentum`. If we have a particle with mass $m$ and it is constrained to move on a circular ring of radius $r$, the magnitude of its angular momentum in the axis perpendicular to the ring (the $z$-axis) is defined in equation {ref}`J_z`, where $p$ is the instantaneous linear momentum of the particle:

:::{math}
:label: J_z
J_z = pr
:::

The total energy of our system is due completely to the motion of the particle and so is kinetic in origin. We can express the energy of the system by relating the kinetic energy to the angular momentum:

:::{math}
:enumerated: false
E = \frac{1}{2}mv^2 = \frac{p^2}{2m} = \frac{(J_z/r)^2}{2m} = \frac{J_z^2}{2mr^2}
:::

We notice that the denominator looks like the **moment of inertia** ($I = mr^2$). By including this definition, we find the energy of our particle on a loop:

:::{math}
:label: classical_energy_rotation
E = \frac{J_z^2}{2I}
:::

:::{code-cell} python
:tags: ["remove-input"]
# --- Interactive Question Block ---
from IPython.display import display, HTML
import sys, os

# Simplified for this block
from _ext.interactive_qa import QuestionBlock
questions = QuestionBlock()
questions.add_question(
    question_id="sec-2-ch-2-q04",
    question_text="Does it make sense that the energy of the rotating system is inversely proportional to the moment of inertia? Explain why it is or isn't."
)
display(HTML(questions.render()))
:::

### The Quantum Condition

Where does the quantum part come in? We define the wavelike character of our particle using the de Broglie relation ($p = h/\lambda$). Combining this with our expression for $J_z$:

:::{math}
J_z = pr = \frac{hr}{\lambda}
:::

For the wavefunction to be physically realistic (well-behaved), it must meet back up with itself exactly as it circles the ring. It must be **continuous** and **single-valued**. This requires the circumference of the ring to be an integer multiple of the wavelength:

:::{math}
:enumerated: false
J \lambda = 2\pi r \implies \lambda = \frac{2\pi r}{J} \quad J = 0, 1, 2, \dots
:::



Substituting this quantized wavelength back into our expression for $J_z$:

:::{math}
:label: quantum_J_z
J_z = J \hbar
:::

And the quantized energy states:

:::{math}
:label: quantum_energy_angular
E_{J} = \frac{J^2 \hbar^2}{2I}
:::

---

### Spectroscopy Applications: The Microwave Region

Just as vibrations are mapped to the Infrared region, pure rotations of molecules are typically observed in the **Microwave region**. Because it takes significantly less energy to make a molecule tumble than it does to stretch its bonds, rotational transitions occur at much lower frequencies.

#### Selection Rules and Energy Spacing
To observe a rotational transition, a molecule must possess a permanent dipole moment. The selection rule for this system is $\Delta J = \pm 1$. 

In the Harmonic Oscillator, the energy levels were equally spaced, resulting in a single spectral line. In the Rigid Rotator, however, the energy depends on $J^2$. This has two major consequences:
1. **Increasing Gaps:** As $J$ increases, the energy levels spread further apart.
2. **Multiple Spectral Lines:** Because the difference between adjacent levels ($E_{J+1} - E_{J}$) increases as $J$ goes up, the spectrum consists of a series of lines rather than just one.


:::{include} interactive_code/rot_spectrum.md
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
question_id="sec-02-ch-2-q08",
question_text="In the Rigid Rotator model, we assume the bond length $r$ is fixed. If the angular momentum is quantized, why must the energy levels become increasingly spaced further apart as the quantum number $J$ increases, unlike the evenly spaced levels of the Harmonic Oscillator?"
)
display(HTML(questions.render()))
:::
---

## Tying it All Together: From Postulates to Models

Over the course of this chapter, we have moved from the abstract to the applied. We began with a set of mathematical "rules"—the **Postulates of Quantum Mechanics**—and used them as a blueprint to build three fundamental models of motion. 

These models are not just mathematical exercises; they are the "standard rulers" we use to measure and understand real physical systems:

* **The Particle in a Box (PIB):** Represents **confinement**. We use this to model electrons "trapped" in a conjugated system (like the $\pi$ electrons in beta-carotene).
* **The Harmonic Oscillator (QHO):** Represents **vibration**. This is our primary tool for modeling the rhythmic stretching and bending of chemical bonds in diatomic molecules.
* **The Rigid Rotator:** Represents **rotation**. This allows us to understand how molecules tumble through space and how they interact with microwave radiation.

---

### Summary of Fundamental Quantum Models

| Feature | Particle in a Box (1D) | Harmonic Oscillator | Rigid Rotator (Ring) |
| :--- | :--- | :--- | :--- |
| **Physical Motion** | Translation / Confinement | Vibration | Rotation |
| **Potential Energy $V$** | $0$ (inside), $\infty$ (outside) | $\frac{1}{2}kx^2$ (Quadratic) | $0$ (on the ring) |
| **Quantum Number** | $n = 1, 2, 3, \dots$ | $v = 0, 1, 2, \dots$ | $J = 0, 1, 2, \dots$ |
| **Energy $E$** | $E_n = \frac{n^2 h^2}{8mL^2}$ | $E_v = (v + \frac{1}{2})h\nu$ | $E_{J} = \frac{J^2 \hbar^2}{2I}$ |
| **Energy Spacing** | Increases with $n$ | **Constant** ($\Delta E = h\nu$) | Increases with $J$ |
| **Zero-Point Energy?** | Yes ($E_1 > 0$) | Yes ($E_0 = \frac{1}{2}h\nu$) | **No** ($E_0 = 0$) |
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
question_id="sec-02-ch-2-q09",
question_text="Why must a molecule possess a permanent dipole moment to be 'active' in microwave (rotational) spectroscopy? What is the role of the oscillating electric field of the photon in this process?"
)
display(HTML(questions.render()))
:::
### What’s Next?

We have successfully used the postulates to solve for "ideal" model systems. However, chemistry is ultimately the study of atoms. In the next chapter, we will take the lessons learned from the **Rigid Rotator** and apply them to the first "real" physical system: the **Hydrogen Atom**. By placing a single electron in a three-dimensional spherical potential, we will finally see where the $s, p, d,$ and $f$ orbitals—the fundamental shapes of chemistry—actually come from.