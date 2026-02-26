(electron_configurations)=
## Electronic Configurations and Spectroscopy

Building a multi-electron atom requires us to organize electrons into the "neighborhoods" defined by our quantum numbers. While the Schrödinger equation provides the allowed states, three fundamental rules dictate how electrons inhabit them.

### Rules for Filling Orbitals

1.  **Pauli Exclusion Principle:** No two electrons in an atom can have the same four quantum numbers $(n, l, m_l, m_s)$. Since an orbital is defined by the first three numbers, this implies that a single orbital can hold a maximum of two electrons, which must have opposite spins.
2.  **Aufbau Principle:** Fill from lowest energy to highest. Due to the penetration and shielding effects, the energy order is not strictly numerical by $n$.
3.  **Hund's Rule:** For degenerate orbitals (same energy), electrons occupy them singly with parallel spins before pairing. This minimizes electron-electron repulsion.

### Determining the Filling Order: The Diagonal Rule

To remember the sequence of orbital energies, we use the **Madelung Rule** (the $n+l$ rule). A common visual aid is the "Diagonal Tower." By writing out the subshells and drawing diagonal arrows from the top-right to the bottom-left, the correct order emerges:

[Image of the Aufbau principle diagonal rule for electron filling]

**The resulting sequence is:**
$$1s < 2s < 2p < 3s < 3p < 4s < 3d < 4p < 5s < 4d \dots$$

### Scaling Up: Noble Gas Notation

As atoms get larger, writing out the full electron configuration becomes cumbersome and obscures the most important part of the atom: the **valence electrons**. Consider the element **Bromine (Br)**, which has 35 electrons. Using the filling order above, its full configuration is:

$$1s^2 2s^2 2p^6 3s^2 3p^6 4s^2 3d^{10} 4p^5$$

Notice that the first 18 electrons are identical to the configuration of **Argon**, the preceding noble gas. Because these "core electrons" are tightly bound and generally do not participate in chemical reactions, we can abbreviate them using the noble gas symbol in brackets:

$$\text{Br: [Ar]} 4s^2 3d^{10} 4p^5$$

This notation immediately highlights that Bromine has 7 valence electrons in its fourth shell, explaining its high reactivity as a halogen.

---

### Ion Formation: The Transition Metal Exception

When atoms lose electrons to form cations, they generally remove electrons from the highest energy level first. However, there is a critical distinction between main-group elements and transition metals.

* **Main-Group Elements:** Electrons are removed in the exact reverse order of filling. For Magnesium ([Ne] 3s²), the 3s electrons are the last in and the first out to form Mg²⁺.
* **Transition Metals ($ns$ vs $(n-1)d$):** Even though the 4s orbital fills before the 3d orbital, **transition metals always lose their s electrons first.** For example, Iron (Fe) has the configuration: [Ar] 4s² 3d⁶. 
When it forms Fe²⁺, it does **not** lose 3d electrons; it loses the 4s electrons: 
$$\text{Fe}^{2+} = \text{[Ar]} 3d^6$$

This happens because once the 3d subshell begins to fill, the effective nuclear charge increases and the relative energies of the 3d and 4s orbitals shift, making the 4s electrons more peripheral and easier to remove.

---

### Atomic Term Symbols: Why Do We Care?

While electron configurations tell us which "bins" the electrons occupy, they don't account for the **magnetic and angular momentum interactions** between those electrons. Just saying an atom is "$p^2$" is like saying two magnets are in a drawer; their overall energy depends heavily on whether their poles are aligned or opposed. We use Term Symbols to predict real physical and chemical behavior:

1.  **Energy Fine Structure:** Electrons create magnetic fields that interact through **Spin-Orbit Coupling**. This splits single energy levels into multiple "fine structure" levels. For example, this splitting is exactly why the iconic yellow glow of streetlights (the Sodium D-line) is actually a *doublet* of two very closely spaced wavelengths, not a single line.

[Image of energy level splitting showing spin-orbit coupling for the Sodium D-line doublet]

2.  **Exchange Energy (Singlet vs. Triplet):** Term symbols reveal the total spin ($S$). Consider an excited Helium atom with a $1s^1 2s^1$ configuration. The two electrons can either have paired spins (a **Singlet** state, $S=0$) or parallel spins (a **Triplet** state, $S=1$). Because parallel spins force electrons to stay further apart spatially (a quantum effect called *exchange energy*), the Triplet state is significantly lower in energy than the Singlet state. 

[Image of Helium energy level diagram showing orthohelium and parahelium]

Because transitions between Singlet and Triplet states are strictly forbidden (see below), these two forms of helium do not easily interconvert. They have entirely different emission spectra! In fact, late 19th-century astronomers observing these distinct spectra thought they were looking at two completely different elements, naming them *parahelium* (singlet) and *orthohelium* (triplet).
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
question_id="sec-02-ch-3-q06",
question_text="Consider the electron configurations of Helium. Why is it physically possible for the excited state ($1s^1 2s^1$) to exist as either a Singlet ($S=0$) or a Triplet ($S=1$), while the ground state ($1s^2$) can only exist as a Singlet?"
)
display(HTML(questions.render()))
:::
#### Calculating Term Symbols
The general form is ${^{2S+1}L_J}$. To determine $L$, we use the following spectroscopic letter mapping:

| Total $L$ Value | 0 | 1 | 2 | 3 | 4 | 5 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Term Letter** | **S** | **P** | **D** | **F** | **G** | **H** |

**Example Walkthrough: Carbon ($2p^2$)**
* **Step 1 ($L$):** Two electrons in p orbitals ($l=1$) with $m_l = +1, 0$. Sum $L = 1$, which corresponds to a **P** state.
* **Step 2 ($S$):** Two parallel spins $1/2 + 1/2 = 1$. Multiplicity $2S+1 = 3$ (**Triplet**).
* **Step 3 ($J$):** Range from $|L-S|$ to $|L+S|$, giving 0, 1, 2. By Hund's Rules, the ground state for a less-than-half-filled shell is the lowest $J$: ${^3\text{P}_0}$.
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
question_id="sec-02-ch-3-q07",
question_text="In late 19th-century astronomy, the triplet excited state of helium (orthohelium) and the singlet excited state (parahelium) were thought to be completely different elements because their emission spectra were so distinct. Explain the physical concept of exchange energy. Why does forcing two electrons to have parallel spins (triplet) lower the energy of the atom compared to paired spins (singlet)?"
)
display(HTML(questions.render()))
:::
---

### Selection Rules and Spectroscopy

Transitions between these states are governed by conservation laws. A photon carries an intrinsic angular momentum of 1. To conserve this, the atom must change its state accordingly. The three main selection rules are:

1.  **$\Delta S = 0$:** Spin multiplicity must not change (Singlet $\to$ Triplet is "forbidden").
2.  **$\Delta L = \pm 1$:** The orbital shape must change (e.g., $s \to p$).
3.  **$\Delta J = 0, \pm 1$:** (But $J=0 \to J=0$ is forbidden).

#### The Meaning of "Forbidden"
In quantum mechanics, a "forbidden" transition does not mean *impossible*—it just means *highly improbable* or *very slow*. 

This is the entire mechanism behind glow-in-the-dark materials! Atoms or ions trapped in a solid matrix absorb light and enter an excited singlet state. They then undergo a non-radiative process to drop into a lower-energy triplet state. Because the transition back down to the singlet ground state violates the $\Delta S = 0$ rule, the electron gets "stuck." The light slowly leaks out over hours as **phosphorescence** rather than instantly flashing as **fluorescence**.

:::{code-cell}
:tags: ["remove-input"]

# --- START: Required for every block ---
import sys
import os
from IPython.display import display, HTML

try:
    cwd = os.getcwd()
    project_root = os.path.abspath(os.path.join(cwd, "..", "..", ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
except Exception as e:
    print(f"Error setting project path: {e}")

from _ext.interactive_qa import QuestionBlock
# --- END: Required for every block ---

questions = QuestionBlock()
questions.add_question(
    question_id="sec-2-ch-2-q11",
    question_text="In the context of quantum mechanical selection rules, what does it mean for a transition to be forbidden? Does this mean the transition can never, ever happen? Explain what this means from the fundamental notion of probability density in quantum mechanics."
)
display(HTML(questions.render()))
:::

[Image of Jablonski diagram comparing fluorescence and phosphorescence with singlet and triplet states]

---


:::{code-cell}
:tags: ["remove-input"]

# --- START: Required for every block ---
import sys
import os
from IPython.display import display, HTML

try:
    cwd = os.getcwd()
    project_root = os.path.abspath(os.path.join(cwd, "..", "..", ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
except Exception as e:
    print(f"Error setting project path: {e}")

from _ext.interactive_qa import QuestionBlock
# --- END: Required for every block ---

questions = QuestionBlock()
questions.add_question(
    question_id="sec-2-ch-2-q08",
    question_text="A substance that is paramagnetic is attracted to magnetic fields, while a substance that is diamagnetic is repelled by magnetic fields. How does this relate to paired and unpaired electrons?"
)
display(HTML(questions.render()))
:::


:::{code-cell}
:tags: ["remove-input"]

# --- START: Required for every block ---
import sys
import os
from IPython.display import display, HTML

try:
    cwd = os.getcwd()
    project_root = os.path.abspath(os.path.join(cwd, "..", "..", ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
except Exception as e:
    print(f"Error setting project path: {e}")

from _ext.interactive_qa import QuestionBlock
# --- END: Required for every block ---

questions = QuestionBlock()
questions.add_question(
    question_id="sec-2-ch-2-q12",
    question_text="Glow-in-the-dark materials rely on a bottleneck in electron relaxation. Using your knowledge of spin multiplicity and selection rules, explain why a material will emit light instantaneously (fluorescence) when the electron remains in a singlet state, but will emit light slowly over hours (phosphorescence) if the excited electron crosses over into a triplet state. Again, how does this relate to statistics and probability densities rather than strictly enforced rules."
)
display(HTML(questions.render()))
:::