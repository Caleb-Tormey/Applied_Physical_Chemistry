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
  enumerator: 3.%s
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
# Chapter 3: Atomic Systems

:::{include} sec_1_hydrogen_atom.md
:::

:::{include} sec_2_hydrogen_wavefunction.md
:::

:::{include} sec_3_quantum_numbers.md
:::

---

:::{include} sec_4_multi_electrons.md
:::

---

:::{include} sec_5_elect_config_spect.md
:::

---


:::{code-cell} python
:tags: ["remove-input"]

from _ext.interactive_qa import QAManager
from IPython.display import display, HTML

# This renders the final control panel.
# Pass the desired title for the printed page here.
manager = QAManager(page_title="Chapter A: Mathematics Review")
display(HTML(manager.render()))
:::
## Practice Problems

You are free to do none, some, or all of these problems as you see fit. They are designed to mimic the mathematical manipulations and physical reasoning you will encounter in the rest of the book.

### 1. The Hydrogen Atom and Electrostatic Potential
*Explore the forces and energy scales that define our foundational atomic model.*
1. **Simple:** Calculate the electrostatic potential energy ($V$) in Joules for a hydrogen atom where the electron is at the Bohr radius ($r = 5.29 \times 10^{-11}\:\text{m}$). Use $V(r) = -e^2 / (4\pi\epsilon_0 r)$, where $e = 1.602 \times 10^{-19}\:\text{C}$ and $1/(4\pi\epsilon_0) = 8.988 \times 10^9\:\text{N m}^2/\text{C}^2$.
2. **Intermediate:** For a $\text{He}^+$ ion ($Z=2$), calculate the potential energy at the same distance $r$ used in the previous problem. How does the doubling of nuclear charge affect the potential energy compared to Hydrogen?
3. **Advanced:** In the Bohr model, the total energy $E$ is exactly half of the potential energy ($E = V/2$). Calculate the total energy for the hydrogen ground state in electron-volts ($1\:\text{eV} = 1.602 \times 10^{-19}\:\text{J}$). Does this match the experimental ionization energy of $13.6\:\text{eV}$?

### 2. Radial Wavefunctions and Nodes: Calculus & Analysis
*Analyze the mathematical structure of $R_{n,l}$ and solve for the physical location of nodes.*

1. **Simple (Conceptual):** The $1s$ radial wavefunction is $R_{1,0}(r) = 2(Z/a_0)^{3/2} e^{-Zr/a_0}$. As $r \to \infty$, what happens to the value of $R$? Does this function ever cross the x-axis (reach a value of zero) for any finite value of $r$? Based on this, how many radial nodes does the $1s$ orbital have?

2. **Intermediate (The $2s$ Node):** The $2s$ radial wavefunction for Hydrogen ($Z=1$) is:
   :::{math}
   R_{2s}(r) = \frac{1}{2\sqrt{2}} (a_0)^{-3/2} \left( 2 - \frac{r}{a_0} \right) e^{-r/2a_0}
   :::
   A radial node occurs where $R_{2s}(r) = 0$. Since the exponential and constant terms cannot be zero (for $r < \infty$), the node must occur at the "root" of the polynomial term. Solve for the value of $r$ in terms of $a_0$.



3. **Advanced (The $3s$ Nodes):** The $3s$ radial wavefunction involves a quadratic polynomial:
   :::{math}
   R_{3s}(r) = N \left( 6 - 6\sigma + \sigma^2 \right) e^{-\sigma/3} \quad \text{where } \sigma = \frac{Zr}{a_0}
   :::
   * (a) Set the polynomial equal to zero and use the quadratic formula to solve for the two values of $\sigma$ where nodes occur.
   * (b) Convert these $\sigma$ values back into distances $r$ (in units of $a_0$) for a Hydrogen atom ($Z=1$).
   * (c) Verify that the number of nodes you found matches the formula $\text{Nodes}_{\text{radial}} = n - l - 1$.



4. **Challenge (Node Comparison):** Sketch the $R(r)$ vs $r$ plots for $3s$, $3p$, and $3d$ on the same axes. 
   * Label every radial node. 
   * Explain why the $3d$ orbital has no radial nodes even though it is in the $n=3$ shell. 
   * How does the number of **angular nodes** (which equals $l$) compensate to keep the total node count consistent for $n=3$?

### 3. Radial Distribution Functions (RDF)
*Understand the difference between orbital amplitude ($R$) and probability ($4\pi r^2 R^2$).*

1. **Simple:** Write the expression for the Radial Distribution Function ($P(r)$) of the $1s$ orbital. 
2. **Intermediate:** For the $1s$ orbital, the maximum probability occurs at $r = a_0/Z$. Calculate this distance for $\text{H}$ ($Z=1$) and $\text{Li}^{2+}$ ($Z=3$). What does this tell you about the physical "size" of highly charged hydrogenic ions?
3. **Advanced:** Use calculus to prove that the maximum of the $1s$ RDF occurs at $r = a_0$. 
   * *Hint: Take the derivative of $P(r) = 4\pi r^2 [R_{1s}(r)]^2$ with respect to $r$, set it to zero, and solve for $r$.*


### 4. Quantum Numbers and Rules
*Master the "address" system of the electron and the hierarchy of quantum states.*
1. **Simple:** Identify the $n, l,$ and $m_l$ values for a $3d$ orbital. How many individual $3d$ orbitals exist in a $d$-subshell?
2. **Intermediate:** Determine which of the following sets of $(n, l, m_l, m_s)$ are forbidden and explain why:
    * (a) $(2, 2, 1, +1/2)$
    * (b) $(3, 1, 0, -1/2)$
    * (c) $(1, 0, 0, 0)$
    * (d) $(4, 3, -4, +1/2)$
3. **Advanced:** Calculate the total number of electrons that can be held in the $n=4$ principal shell (the **N** shell). Show how this is the sum of the capacities of the $s, p, d,$ and $f$ subshells.

### 5. Shielding, Penetration, and $Z_{\text{eff}}$
*Apply the concepts that break degeneracy in multielectron atoms.*
1. **Simple:** Calculate the effective nuclear charge ($Z_{\text{eff}}$) felt by a $2s$ electron in Lithium ($Z=3$) using the simplest approximation where core electrons ($1s^2$) provide perfect shielding ($S=2$). 
2. **Intermediate:** Experimental data shows $Z_{\text{eff}}$ for the $2s$ electron in Lithium is $\approx 1.28$, while for the $2p$ electron it is $\approx 1.02$. Use the concept of **penetration** to explain why the $2s$ electron feels a stronger pull than the $2p$ electron.

3. **Advanced:** Arrange the following orbitals in order of increasing energy for a multielectron atom: $3s, 3p, 3d, 4s, 4p, 4d, 5s$. Explain why $4s$ is placed where it is relative to $3d$.

### 6. Electron Configurations and Ions
*Predict the ground state of atoms and their behavior during ionization.*
1. **Simple:** Write the full electron configuration for Phosphorus ($Z=15$) and identify the number of unpaired electrons using Hund's Rule.
2. **Intermediate:** Write the **noble gas abbreviated** configuration for Silver ($\text{Ag}$, $Z=47$). (Note: Silver is an exception, like Copper, where a full $d$-shell is preferred).
3. **Advanced (The Transition Metal Rule):** Write the electron configuration for a neutral Iron atom ($\text{Fe}$, $Z=26$). Now, write the configuration for the $\text{Fe}^{2+}$ and $\text{Fe}^{3+}$ ions. Which electrons are removed first, and why is this counter-intuitive based on the filling order?

### 7. Term Symbols and Spectroscopy
*Describe the total state of an atom and the rules for light-matter interaction.*
1. **Simple:** What are the $L$ and $S$ values for a closed-shell noble gas like Neon? what is the resulting term symbol? (Hint: In a full shell, all angular momenta and spins cancel out).
2. **Intermediate:** For a Boron atom ($2p^1$), find $L$ and $S$. Determine the multiplicity ($2S+1$) and the possible $J$ values. Write the ground state term symbol.
3. **Advanced:** Using the selection rules ($\Delta S = 0, \Delta L = \pm 1, \Delta J = 0, \pm 1$), determine which of the following transitions are allowed:
    * (a) ${^1\text{S}_0} \rightarrow {^1\text{P}_1}$
    * (b) ${^3\text{P}_1} \rightarrow {^1\text{D}_2}$
    * (c) ${^2\text{P}_{1/2}} \rightarrow {^2\text{S}_{1/2}}$
    * (d) ${^3\text{D}_1} \rightarrow {^3\text{P}_0}$
