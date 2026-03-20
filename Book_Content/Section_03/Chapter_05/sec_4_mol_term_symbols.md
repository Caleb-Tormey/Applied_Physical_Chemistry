## 5.4 Molecular Term Symbols: The Very Basics

In Chapter 4, when we built the molecular orbital diagram for diatomic oxygen (O₂), we simply stated that its configuration was $(\text{core}) \dots (\sigma_{2p})^2 (\pi_{2p})^4 (\pi^*_{2p})^2$. While this tells us where the electrons are housed, it doesn't tell us the *total* angular momentum or the *total* spin of the entire molecule. 

To describe the overall electronic state of a molecule, we use a **Molecular Term Symbol**. For linear and diatomic molecules, the general format looks like this:

$^{2S+1}\Lambda$

Let's break down what these two pieces mean, and then we will actually build the term symbol for oxygen from scratch.

### 1. Spin Multiplicity ($2S+1$)
Just like in isolated atoms, electrons in molecules have spin. $S$ represents the **Total Spin Quantum Number** of the molecule. To find it, you simply add up the spins of all the unpaired electrons (each unpaired electron contributes +1/2).
* If all electrons are paired, $S = 0$. The multiplicity is $2(0)+1 = 1$. This is called a **Singlet** state.
* If there is one unpaired electron, $S = 1/2$. The multiplicity is $2(1/2)+1 = 2$. This is a **Doublet** state (common for radicals).
* If there are two unpaired electrons, $S = 1$. The multiplicity is $2(1)+1 = 3$. This is a **Triplet** state.

### 2. Total Orbital Angular Momentum ($\Lambda$)
In an isolated atom, the total orbital angular momentum is denoted by the letter $L$ (giving us atomic states like $S, P,$ and $D$). 

In a linear molecule, the strong electric field created by the two nuclei breaks the spherical symmetry. The electrons are forced to orbit around the internuclear axis (the z-axis). We use the Greek letter **$\Lambda$ (Lambda)** to represent the total orbital angular momentum along this specific axis. 

Just like atomic orbitals, we use letters to designate the value of $\Lambda$, which we calculate by adding up the individual $m_l$ values of the highest energy electrons:
* If $\Lambda = 0$, the state is **$\Sigma$ (Sigma)**.
* If $\Lambda = 1$, the state is **$\Pi$ (Pi)**.
* If $\Lambda = 2$, the state is **$\Delta$ (Delta)**.

*(Note: For homonuclear diatomics like O₂ or N₂, you will also see a $g$ or $u$ subscript added to the term symbol to indicate if the total wavefunction is symmetric (gerade) or antisymmetric (ungerade) to an inversion center, exactly like we saw in MO theory!)*

### Working Through an Example: The Oxygen Molecule (O₂)

Let's use our knowledge from Chapter 4 to derive the ground-state term symbol for O₂. The only electrons we care about are the two sitting in the highest occupied molecular orbitals (HOMO). For oxygen, these are the two degenerate $\pi^*_{2p}$ antibonding orbitals.



**Step 1: Find the Spin Multiplicity**
Following Hund's Rule, these two electrons will sit in separate $\pi^*$ orbitals with parallel spins. 
Because they are parallel, their spins add together: $S = 1/2 + 1/2 = 1$.
Multiplicity = $2(1) + 1 = 3$. 
Our term symbol starts with a **3** (it is a Triplet state).

**Step 2: Find the Total Angular Momentum ($\Lambda$)**
The two degenerate $\pi^*$ orbitals correspond to the angular momentum projections $m_l = +1$ and $m_l = -1$. 
Because our two electrons are sitting in separate orbitals, we add these projections together: $\Lambda = (+1) + (-1) = 0$. 
A $\Lambda$ value of 0 corresponds to a **$\Sigma$** state. 
So far, we have $^3\Sigma$.

**Step 3: Symmetry Labels ($g/u$ and $+/-$)**
* **Parity ($g/u$):** Antibonding $\pi^*$ orbitals are mathematically ungerade ($u$). Because we have *two* electrons in $u$ orbitals, we multiply their symmetries: $u \times u = g$. We now have $^3\Sigma_g$.
* **Reflection ($+/-$):** For $\Sigma$ states, we have to indicate if the spatial wavefunction changes sign when reflected across a mirror plane. According to the Pauli Exclusion Principle, the total wavefunction must be antisymmetric. Since our spins are parallel (symmetric), the spatial part *must* be antisymmetric (a minus sign). 

Our final, completely derived ground-state term symbol for diatomic oxygen is **$^3\Sigma_g^-$**.

### Biochemical Relevance: The Spin-Forbidden Miracle

Why do we care about these term symbols? Because they dictate the **Selection Rules** for electronic spectroscopy and chemical reactivity. One of the strictest rules in quantum mechanics is that **spin must be conserved during an electronic transition** ($\Delta S = 0$). Light and heat cannot easily flip an electron's spin. 

Let's apply this to biochemistry. The vast majority of stable organic molecules in your body (DNA, proteins, lipids) have all of their electrons perfectly paired. They exist in **Singlet** ground states. 

As we just derived, the ground state of oxygen is a **Triplet** ($^3\Sigma_g^-$). Thermodynamically, oxygen is incredibly reactive and "wants" to oxidize (burn) the organic molecules in your body to form CO₂ and H₂O. But kinetically, it can't! For a Triplet oxygen molecule to react directly with a Singlet organic molecule, an electron spin would have to flip during the collision. This is a **spin-forbidden** process, making the reaction infinitesimally slow at room temperature. 

This quantum mechanical mismatch—the fact that oxygen is a triplet and your body is made of singlets—is the reason you don't spontaneously combust in Earth's atmosphere! To actually use oxygen for cellular respiration, your body has to use transition metals (like the iron in hemoglobin and cytochrome c oxidase), which have their own unpaired $d$-electrons capable of legally bridging this spin gap.

*(Note: If O₂ absorbs energy and flips one of its electron spins, it becomes **Singlet Oxygen** ($^1\Delta_g$). Because it is now a singlet, the spin-forbidden restriction is lifted. Singlet oxygen is viciously reactive and is a major source of oxidative stress, cellular damage, and aging in biological systems!)*

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

questions_ch5 = QuestionBlock()

questions_ch5.add_question(
    question_id="sec-03-ch-5-q04",
    question_text=r"If you artificially excite an electron in a typical organic molecule so its spin flips, the molecule briefly enters a Triplet state. Why does this make the molecule incredibly reactive and dangerous to the surrounding biological tissue?"
)
display(HTML(questions_ch5.render()))
:::