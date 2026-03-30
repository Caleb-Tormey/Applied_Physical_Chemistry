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
  enumerator: 8.%s
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
# Chapter 8: First Law of Thermodynamics

:::{include} sec_1_first_law_internal.md
:::
:::{include} sec_2_enthalpy.md
:::
:::{include} sec_3_heat_capacity.md
:::
:::{include} sec_4_Hess_Law.md
:::
:::{include} sec_5_bond_enthalpies.md
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
    question_id="sec-2-ch-2-q01",
    question_text="Given the possible quantum numbers is it possible to have zero vibrational energy in a quantum HO? Please justify and explain your answer. "
)
display(HTML(questions.render()))
#**Conceptual Question:** Given the possible quantum numbers is it possible to have zero vibrational energy in a quantum HO? Please justify and explain your answer. 
:::
## ATP and Energy Coupling

## Calorimetry
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

### 8.1 Internal Energy ($U$) and the First Law
*Apply the conservation of energy to biological systems and distinguish between heat and work.*

1. **Simple:** A muscle cell is doing heavy physical work. It expends $450\:\text{J}$ of work ($w$) to contract its fibers and simultaneously releases $120\:\text{J}$ of heat ($q$) into the surrounding tissue. Using the First Law of Thermodynamics ($\Delta U = q + w$), calculate the total change in Internal Energy ($\Delta U$) of the muscle cell.
2. **Intermediate:** An extremophile archaeon is placed in a rigid, sealed bomb calorimeter. It ferments a nutrient, releasing $850\:\text{J}$ of heat. Because the calorimeter is perfectly rigid, what is the value of physical work ($w$)? Therefore, the heat measured by the calorimeter ($q_v$) is exactly equal to the change in which state function?
3. **Advanced:** The internal energy ($U$) of an ideal monatomic gas is defined purely by its kinetic energy: $U = \frac{3}{2} nRT$. Calculate the internal energy of $1.0\:\text{mole}$ of helium gas at body temperature ($310.15\:\text{K}$). If the gas is heated at a constant volume to $320.15\:\text{K}$, calculate the exact amount of heat ($q$) required. *(Note: $R = 8.314\:\text{J/(mol K)}$)*.

### 8.2 Enthalpy ($H$): The Heat at Constant Pressure
*Understand why biochemists invented Enthalpy and how it corrects for expansion work.*

1. **Simple:** Write the mathematical definition of Enthalpy ($H$) in terms of Internal Energy ($U$), Pressure ($P$), and Volume ($V$). Explain physically why $\Delta H$ is almost exactly equal to $\Delta U$ for biochemical reactions involving only liquids and solids, but differs significantly for reactions that produce a gas.
2. **Intermediate:** The complete combustion of $1.0\:\text{mole}$ of solid glucose produces $6.0\:\text{moles}$ of $\text{CO}_2$ gas and consumes $6.0\:\text{moles}$ of $\text{O}_2$ gas. Since the number of moles of gas does not change ($\Delta n_{gas} = 0$), the expansion work ($P\Delta V$) at constant pressure is zero. If the change in internal energy ($\Delta U$) for this reaction is $-2808\:\text{kJ/mol}$, what is the exact value of $\Delta H$? 
3. **Advanced:** A yeast cell ferments glucose into ethanol and $\text{CO}_2$ gas at a constant pressure of $1.0\:\text{atm}$ and a temperature of $298.15\:\text{K}$. The reaction produces $2.0\:\text{moles}$ of $\text{CO}_2$ gas, pushing back the atmosphere and doing expansion work. If the heat released by the cell into the open beaker is measured as $q_p = -68.0\:\text{kJ}$, calculate the total change in Internal Energy ($\Delta U$) for this fermentation process. *(Hint: Use $\Delta H = \Delta U + P\Delta V$, and substitute the Ideal Gas Law for the $P\Delta V$ term).*

### 8.3 Calorimetry and Heat Capacity
*Measure biological heat mathematically and explore the temperature dependence of Enthalpy.*

1. **Simple:** You are designing a fluid to cool a high-powered biological incubator. Fluid A has a specific heat capacity of $2.0\:\text{J/(g K)}$ and Fluid B has a specific heat capacity of $4.5\:\text{J/(g K)}$. Which fluid will absorb more heat energy before its temperature rises by $1^\circ\text{C}$? Which is a better thermal buffer?
2. **Intermediate (Differential Scanning Calorimetry):** A physical chemist uses DSC to slowly heat a $0.05\:\text{M}$ solution of a folded protein. At exactly $55^\circ\text{C}$, the protein denatures (unfolds). The instrument detects a sudden, massive spike in the heat capacity ($C_p$) of the solution. Is the unfolding of this protein an endothermic or exothermic process? Explain your reasoning.
3. **Advanced (Kirchhoff's Law):** The standard enthalpy of a biological reaction is $\Delta H^\circ_{298} = -50.0\:\text{kJ/mol}$ at $25^\circ\text{C}$ ($298.15\:\text{K}$). The total heat capacity of the products is $150\:\text{J/(K mol)}$, and the total heat capacity of the reactants is $100\:\text{J/(K mol)}$. Using Kirchhoff's Law ($\Delta H_{T_2} = \Delta H_{T_1} + \Delta C_p \Delta T$), calculate the exact enthalpy of this reaction at $37^\circ\text{C}$ ($310.15\:\text{K}$). 

### 8.4 Standard States and Enthalpies of Formation
*Establish the thermodynamic baseline and calculate energy changes from scratch.*

1. **Simple:** Write the balanced chemical equation for the standard formation of liquid water ($\text{H}_2\text{O}$) from its elements in their standard states. What is the assigned standard enthalpy of formation ($\Delta H_f^\circ$) for pure $\text{O}_2(g)$ and pure $\text{H}_2(g)$?
2. **Intermediate:** Using the following standard enthalpies of formation ($\Delta H_f^\circ$), calculate the overall standard enthalpy of reaction ($\Delta H_{rxn}^\circ$) for the conversion of Pyruvate to Lactate (a key step in anaerobic glycolysis):
    * Pyruvate(aq): $-474.0\:\text{kJ/mol}$
    * Lactate(aq): $-517.0\:\text{kJ/mol}$
    * Is this specific metabolic step endothermic or exothermic?
3. **Advanced (The Baseline Problem):** Calculate the standard enthalpy of reaction ($\Delta H_{rxn}^\circ$) for the combustion of methane: $\text{CH}_4(g) + 2\text{O}_2(g) \rightarrow \text{CO}_2(g) + 2\text{H}_2\text{O}(l)$. 
    * $\text{CH}_4(g): -74.8\:\text{kJ/mol}$
    * $\text{CO}_2(g): -393.5\:\text{kJ/mol}$
    * $\text{H}_2\text{O}(l): -285.8\:\text{kJ/mol}$
    * Once you find the total $\Delta H_{rxn}^\circ$, explain why a biochemist cannot easily use this exact number to predict the heat released by methane-producing bacteria living at the bottom of the ocean ($4^\circ\text{C}$ and $300\:\text{atm}$). 

### 8.5 Hess's Law and Biochemical Pathways
*Treat Enthalpy as a state function to solve complex metabolic puzzles.*

1. **Simple:** A biological pathway consists of two steps. Step 1 has an enthalpy of $\Delta H = +25\:\text{kJ/mol}$. Step 2 has an enthalpy of $\Delta H = -60\:\text{kJ/mol}$. According to Hess's Law, what is the net enthalpy change of the overall pathway? 
2. **Intermediate:** Determine the net enthalpy for the overall reaction: $\text{A} + 2\text{B} \rightarrow \text{C} + \text{D}$, using the following measured laboratory steps:
    * Reaction 1: $\text{A} + \text{B} \rightarrow \text{X} \quad (\Delta H = -40\:\text{kJ/mol})$
    * Reaction 2: $\text{C} + \text{D} \rightarrow \text{X} + \text{B} \quad (\Delta H = +15\:\text{kJ/mol})$
    * *(Hint: You may need to reverse one of the reactions!)*
3. **Advanced (The Hydration Cycle):** When solid sodium chloride ($\text{NaCl}$) dissolves in water, the beaker actually feels slightly cold ($\Delta H_{soln} = +3.9\:\text{kJ/mol}$). Explain this endothermic reality by using a Hess's Law cycle (a Born-Haber style cycle). Break the dissolution process into two theoretical steps: 
    * (1) Breaking the ionic lattice into gaseous ions (Lattice Enthalpy, $\Delta H \approx +788\:\text{kJ/mol}$).
    * (2) The surrounding of those gaseous ions by water molecules (Hydration Enthalpy, $\Delta H \approx -784\:\text{kJ/mol}$).
    * Which force ultimately "wins" the enthalpy tug-of-war, and what drives the salt to spontaneously dissolve if the enthalpy is unfavorable?