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
  enumerator: 9.%s
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
# Chapter 9: Second and Third Laws of Thermodynamics

:::{include} sec_1_second_law.md
:::
:::{include} sec_2_third_law.md
:::
:::{include} sec_3_system_surroundings.md
:::
:::{include} sec_4_free_energy.md
:::
:::{include} sec_5_chemical_pot.md
:::
:::{include} sec_6_ATP.md
:::
## Free Energy
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
## Standard States

## Temperature and pH Effects
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

### 9.1 The Arrow of Time and the Concept of Entropy ($S$)
*Connect the time-reversibility of classical mechanics to the statistical drive toward maximum microstates.*

1. **Simple:** A physical chemist creates a tiny model system with just 4 particles and 2 units of energy. They determine that there are exactly 6 distinct microscopic ways to arrange the energy among the particles without changing the macroscopic appearance of the system. Calculate the thermodynamic entropy ($S$) of this system in J/K using Boltzmann's equation. *(Note: $k_B = 1.38 \times 10^{-23}$ J/K).*
2. **Intermediate:** Explain the "Arrow of Time" using the concept of microstates ($W$). If you film a drop of ink diffusing into a beaker of water and then play the video in reverse, it looks impossible. Why does classical Newtonian mechanics fail to explain this impossibility, and how does Boltzmann's definition of entropy mathematically prove the video is playing backward?
3. **Advanced (The Hydrophobic Effect):** When a nonpolar amino acid is dropped into water, the water molecules form rigid clathrate cages around it. During protein folding, these nonpolar amino acids clump together in the core of the protein. 
    * (a) Does the clumping of the amino acids increase or decrease the microstates of the protein chain itself? 
    * (b) Explain physically why the surrounding water molecules "drive" this folding process by demanding an increase in their own microstates. 

### 9.2 The Third Law: The Absolute Baseline
*Define the absolute zero of entropy and use standard molar entropies ($S^\circ$) to calculate system changes.*

1. **Simple:** State the Third Law of Thermodynamics. Explain physically what happens to the translational, rotational, and vibrational energy of molecules at 0 K, and why this results in exactly one microstate ($W=1$). 
2. **Intermediate:** We can look up the absolute standard entropy ($S^\circ$) of a molecule in a textbook table, but the enthalpy table only lists the *change* in formation enthalpy ($\Delta H_f^\circ$). Explain why we have a mathematical baseline for absolute entropy but lack a universal baseline for absolute energy. 
3. **Advanced:** Using standard thermodynamic tables, calculate the standard entropy of reaction ($\Delta S_{rxn}^\circ$) for the synthesis of urea from ammonia and carbon dioxide: 
    $2\text{NH}_3(g) + \text{CO}_2(g) \rightarrow \text{CO}(\text{NH}_2)_2(aq) + \text{H}_2\text{O}(l)$
    * $\text{NH}_3(g): 192.5$ J/(mol K)
    * $\text{CO}_2(g): 213.8$ J/(mol K)
    * Urea$(aq): 173.8$ J/(mol K)
    * $\text{H}_2\text{O}(l): 69.9$ J/(mol K)
    * Does the sign of your calculated $\Delta S^\circ$ make physical sense based on the phases of the reactants and products?

### 9.3 The Universe Ledger: System vs. Surroundings
*Use the First Law heat bridge and Clausius’s definition to calculate the entropy change of the universe.*

1. **Simple:** Rudolf Clausius defined the macroscopic change in entropy as $\Delta S = q/T$. If an exothermic biological reaction releases 4500 J of heat into the surrounding cellular fluid at a constant body temperature of 310 K, calculate the exact change in entropy of the surroundings ($\Delta S_{surr}$). 
2. **Intermediate:** The folding of a specific enzyme represents a localized decrease in chaos ($\Delta S_{sys} = -200$ J/(mol K)). However, the formation of its internal bonds is highly exothermic, releasing 100 kJ/mol of heat ($\Delta H_{sys} = -100$ kJ/mol) at 298 K. 
    * (a) Calculate $\Delta S_{surr}$. 
    * (b) Calculate the total $\Delta S_{univ}$. 
    * (c) Does this enzyme fold spontaneously according to the Second Law?
3. **Advanced (The Entropy Tax):** Synthesizing a complex DNA double helix from individual nucleotides massively decreases the entropy of the system. A biology student claims that living cells must have a special mechanism to bypass the Second Law of Thermodynamics to build such ordered structures. Use the "Universe Ledger" and the concept of the "Entropy Tax" to correct their misconception. 

### 9.4 Free Energy: Helmholtz ($A$) vs. Gibbs ($G$)
*Unify system enthalpy and entropy into the ultimate judge of spontaneity.*

1. **Simple:** Calculate the Standard Gibbs Free Energy ($\Delta G^\circ$) for a reaction at 298 K where $\Delta H^\circ = -45.0$ kJ/mol and $\Delta S^\circ = -125$ J/(mol K). Is this reaction spontaneous under standard conditions? *(Hint: Make sure your energy units match before subtracting!)*
2. **Intermediate:** Why do biochemists exclusively use Gibbs Free Energy ($G$) instead of Helmholtz Free Energy ($A$)? In your explanation, define the difference between the constant volume constraints of a bomb calorimeter and the physical environment of a living cell. 
3. **Advanced (The Thermodynamic Quadrants):** The thermal denaturation (melting) of a protein costs heat ($\Delta H^\circ = +300$ kJ/mol) but creates massive structural chaos ($\Delta S^\circ = +900$ J/(mol K)). 
    * (a) Which of the four thermodynamic quadrants does this reaction belong to? 
    * (b) Write the Gibbs Free Energy equation and set $\Delta G = 0$ to calculate the exact temperature (in Celsius) at which this protein spontaneously melts. 

### 9.5 Chemical Potential ($\mu$): The Thermodynamic Force
*Translate macroscopic Free Energy into the microscopic driving forces of concentration gradients.*

1. **Simple:** Write the equation for the chemical potential of a solute: $\mu = \mu^\circ + RT \ln([C])$. If a cell actively pumps sodium ions out of the cytoplasm, lowering the internal concentration from 15 mM to 1.5 mM, what happens to the mathematical value of the natural log term? Does the chemical potential of internal sodium increase or decrease?
2. **Intermediate:** Use the "boulder on a hill" analogy to explain the physical process of osmosis. If a red blood cell is placed in pure distilled water, describe the chemical potential of water inside the cell versus outside the cell. In which direction does the thermodynamic force drive the water molecules?
3. **Advanced:** A neuron needs to push a potassium ion ($K^+$) into the cell, moving it from a region of low chemical potential (outside) to a region of high chemical potential (inside). Since the ion will never spontaneously roll "up" the thermodynamic hill, explain thermodynamically how the cell can force this process to happen. 

### 9.6 The ATP Payoff: Bringing It All Together
*Apply the full thermodynamic ledger to the universal energy currency of life.*

1. **Simple:** The hydrolysis of ATP to ADP and $\text{P}_i$ has a positive entropy change ($\Delta S > 0$). Detail the two physical reasons for this increase in chaos (translational freedom and the hydration shell). 
2. **Intermediate:** ATP hydrolysis is located in "The Dream" thermodynamic quadrant. Explain how the Enthalpy term ($\Delta H$) and the Entropy term ($-T\Delta S$) work together to ensure that the cell does not have to pay an entropy tax to the universe during this reaction. 
3. **Advanced (The Real Cell):** The standard free energy of ATP hydrolysis is $\Delta G^{\circ\prime} = -30.5$ kJ/mol. However, in a healthy human cell at 310 K, the concentrations are kept far from standard: $[\text{ATP}] = 5.0$ mM, $[\text{ADP}] = 0.5$ mM, and $[\text{P}_i] = 5.0$ mM. 
    * (a) Calculate the Reaction Quotient ($Q$).
    * (b) Calculate the *actual* Free Energy ($\Delta G$) of ATP hydrolysis in