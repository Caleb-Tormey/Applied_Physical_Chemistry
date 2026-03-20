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
  enumerator: 6.%s
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
# Chapter 6: Intermolecular Forces

:::{include} sec_1_introduction_molecules_materials.md
:::
:::{include} sec_2_charges_dipoles.md
:::
:::{include} sec_3_vdw_p1_dipole.md
:::
:::{include} sec_4_vdw_p2_debye_london.md
:::
:::{include} sec_5_lennard-jones.md
:::
:::{include} sec_6_hydrogen_bonding.md
:::
:::{include} sec_7_hydrophobic.md
:::



:::{code-cell} python
:tags: ["remove-input"]

from _ext.interactive_qa import QAManager
from IPython.display import display, HTML

# This renders the final control panel.
# Pass the desired title for the printed page here.
manager = QAManager(page_title="Chapter 6: Intermolecular Forces")
display(HTML(manager.render()))
:::
## Practice Problems

You are free to do none, some, or all of these problems as you see fit. They are designed to test your conceptual understanding and your ability to mathematically model the forces that govern biological architecture.

### 1. The Baseline: Charges and Dipoles
*Understand fundamental electrostatic forces and calculate their magnitudes.*

1. **Simple:** What is the fundamental difference between an intramolecular covalent bond and an intermolecular non-covalent force in terms of what happens when they are broken?
2. **Intermediate (Coulomb's Law Calculation):** A salt bridge forms between a Lysine residue ($+1$ charge) and a Glutamate residue ($-1$ charge) in a folded protein. The centers of their charged groups are separated by $3.0 \text{ \AA}$ ($3.0 \times 10^{-10} \text{ m}$). Assuming they are in a vacuum for this model, calculate the interaction energy ($E$) in Joules using Coulomb's Law: $E = \frac{q_1 q_2}{4 \pi \epsilon_0 r}$. *(Note: The elementary charge $e = 1.602 \times 10^{-19} \text{ C}$, and $\epsilon_0 = 8.854 \times 10^{-12} \text{ C}^2 \text{ N}^{-1} \text{ m}^{-2}$.)*
3. **Advanced (The Cancellation Effect):** Explain physically why the interaction energy between an ion and a permanent dipole drops off at a rate of $1/r^2$, while a pure ion-ion interaction drops off at $1/r$. Why does the presence of the dipole's opposite partial charge weaken the long-range attraction?

### 2. Van der Waals Forces: Tumbling and Squishing
*Differentiate between Keesom, Debye, and London forces, and calculate thermal effects.*

1. **Simple:** Identify the primary Van der Waals force(s) that must be overcome to boil each of the following liquids: Liquid nitrogen ($N_2$), liquid water ($H_2O$), and liquid argon ($Ar$).
2. **Intermediate (Thermal Averaging Calculation):** The Keesom interaction energy for tumbling dipoles is highly dependent on temperature: $V_{\text{Keesom}} \propto \frac{1}{T}$. Imagine two polar molecules interacting in a liquid at human body temperature ($310 \text{ K}$). If you cool that liquid down to the freezing point of water ($273 \text{ K}$) without changing the distance between the molecules, by what exact factor does the attractive interaction energy increase? Explain physically why colder temperatures result in stronger dipole-dipole attractions.
3. **Advanced (The Additive Effect):** Pentane ($C_5H_{12}$) and 2,2-dimethylpropane ($C_5H_{12}$) have the exact same chemical formula and molecular weight. However, pentane is a long, straight chain, while 2,2-dimethylpropane is a compact, spherical molecule. Which molecule will have a higher boiling point, and why? Refer specifically to London dispersion forces, surface area, and polarizability.

### 3. The Lennard-Jones Potential and Sterics
*Apply the mathematical model of molecular collision and repulsion.*

1. **Simple:** In the Lennard-Jones 12-6 potential, what specific quantum mechanical principle is physically responsible for the incredibly steep $+1/r^{12}$ term?
2. **Intermediate (Lennard-Jones Calculation):** Look at the Lennard-Jones equation: $V(r) = 4\epsilon \left[ (\frac{\sigma}{r})^{12} - (\frac{\sigma}{r})^6 \right]$. First, prove mathematically that the potential energy $V$ is exactly zero when the distance $r = \sigma$. Second, calculate the value of $V(r)$ in terms of $\epsilon$ when the molecules are pulled apart to a distance of $r = 2\sigma$. Does the energy decay quickly or slowly?
3. **Advanced (The Equilibrium Well):** Using calculus, physical chemists can find the exact distance where the molecules are happiest (the bottom of the energy well, $r_{eq}$) by taking the derivative of the Lennard-Jones potential and setting it to zero ($dV/dr = 0$). By solving this, we find that $r_{eq} = 2^{1/6}\sigma$ (or roughly $1.12\sigma$). Physically explain why the bottom of the well ($r_{eq}$) occurs at a slightly longer distance than where the energy crosses zero ($\sigma$). 

### 4. Hydrogen Bonding: The Quantum Connection
*Move beyond the dipole approximation to understand the geometric strictness of life.*

1. **Simple:** Identify the hydrogen bond donor atom and the hydrogen bond acceptor atom when a water molecule interacts with the nitrogen atom of an ammonia ($NH_3$) molecule.
2. **Intermediate (Orbital Geometry):** An introductory biology student draws a hydrogen bond between two peptide backbones with a bond angle of 110°. Using the concept of quantum orbital overlap and the $\sigma^*$ antibonding orbital, explain why this drawn interaction would be incredibly weak compared to a perfectly linear 180° interaction.
3. **Advanced (DNA Base Pair Energy Calculation):** In the DNA double helix, an Adenine-Thymine (A-T) base pair is held together by two hydrogen bonds, while a Guanine-Cytosine (G-C) pair uses three. If we estimate the average strength of a single biologically optimized hydrogen bond to be roughly $20 \text{ kJ/mol}$, calculate the total non-covalent energy required to completely "unzip" a short DNA sequence containing 4 A-T pairs and 6 G-C pairs.

### 5. The Hydrophobic Effect: Thermodynamics in Action
*Bust the "water-fearing" myth and track the flow of entropy.*

1. **Simple:** Evaluate the following statement: "Lipid molecules spontaneously form bilayers in water because the hydrophobic tails strongly repel the polar water molecules." Is this physically accurate? If not, rewrite the statement to reflect reality.
2. **Intermediate (Clathrate Cages):** What is a clathrate cage? Explain exactly how the formation of this rigid structure around a nonpolar solute molecule affects the entropy ($S$) of the surrounding water.
3. **Advanced (The Thermodynamic Bridge):** When a globular protein undergoes "hydrophobic collapse," it folds into a tight 3D sphere. The folded protein itself is highly ordered (low entropy) compared to the floppy, unfolded chain (high entropy). Since the universe demands that total entropy must increase for a process to happen spontaneously, what is the massive source of favorable, positive entropy that overcomes the protein's loss of flexibility and drives this folding process?