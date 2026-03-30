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
  enumerator: 10.%s
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
# Chapter 10: Chemical Equilibrium

:::{include} sec_1_deltag_keq.md
:::
:::{include} sec_2_rxn_quotient.md
:::
:::{include} sec_3_vanthoff.md
:::
:::{include} sec_4_standardstate.md
:::
:::{include} sec_5_coupled_rxn.md
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
## Le Chatelier's Principle

## Coupled Reactions
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

### 10.1 The State of Gridlock: $\Delta G = 0$ and $K_{eq}$
*Connect macroscopic standard free energy to the precise microscopic ratios of equilibrium.*

1. **Simple:** A generic isomerization reaction ($\text{A} \rightleftharpoons \text{B}$) has a standard Gibbs Free Energy of $\Delta G^\circ = -11.4\:\text{kJ/mol}$ at $25^\circ\text{C}$ ($298.15\:\text{K}$). Calculate the equilibrium constant ($K_{eq}$) for this reaction. At equilibrium, are there more products or reactants in the beaker? *(Note: $R = 8.314\:\text{J/(mol K)}$).*
2. **Intermediate (The Calculation Pipeline):** Using standard thermodynamic tables, calculate the absolute equilibrium constant ($K_{eq}$) for the synthesis of ammonia gas at $298.15\:\text{K}$: $\text{N}_2(g) + 3\text{H}_2(g) \rightleftharpoons 2\text{NH}_3(g)$. 
    * First, find $\Delta H_{rxn}^\circ$ using $\Delta H_f^\circ$ values ($\text{NH}_3 = -46.1\:\text{kJ/mol}$).
    * Second, find $\Delta S_{rxn}^\circ$ using absolute $S^\circ$ values ($\text{N}_2 = 191.6$, $\text{H}_2 = 130.7$, $\text{NH}_3 = 192.5\:\text{J/(mol K)}$).
    * Finally, calculate $\Delta G^\circ$ and solve for $K_{eq}$. 
3. **Advanced (Activities vs. Concentrations):** A physical chemistry student calculates a $K_{eq}$ of $4.5 \times 10^3$ for a reaction using pure Molarity ($[C]$) measured in a dilute buffer. When a biochemist runs the exact same reaction inside a dense, crowded living cell, the apparent $K_{eq}$ drops to $1.2 \times 10^3$. Explain this discrepancy using the concept of the activity coefficient ($\gamma$). Why does the crowded environment of the cell lower the *effective* concentration ($a$) of the reacting molecules?

### 10.2 The Reaction Quotient ($Q$) vs. $K$: The Driving Force
*Use real-time concentrations to calculate the exact thermodynamic push of a reaction.*

1. **Simple:** Write the master equation for real-time Free Energy in terms of $Q$ and $K_{eq}$. If $Q$ is mathematically larger than $K_{eq}$, what is the sign of $\Delta G$? Does the reaction spontaneously move forward to create more products, or backward to consume them?
2. **Intermediate:** The conversion of Dihydroxyacetone phosphate (DHAP) to Glyceraldehyde 3-phosphate (GAP) has a highly unfavorable standard free energy: $\Delta G^{\circ\prime} = +7.5\:\text{kJ/mol}$. However, in a working red blood cell at $37^\circ\text{C}$ ($310.15\:\text{K}$), the concentration of DHAP is $140\:\mu\text{M}$ and the concentration of GAP is only $3\:\mu\text{M}$. 
    * (a) Calculate the Reaction Quotient ($Q$).
    * (b) Calculate the actual, real-time Free Energy ($\Delta G$) of the reaction. 
    * (c) Is the reaction spontaneous in the forward direction inside this specific cell?
3. **Advanced (Metabolic Survival):** An enzyme catalyzes the reaction $\text{X} \rightleftharpoons \text{Y}$ with a standard free energy of $\Delta G^{\circ\prime} = +15.0\:\text{kJ/mol}$ at $310.15\:\text{K}$. To keep the organism alive, the cell must force this reaction to run in the forward direction ($\Delta G < 0$). If the cell clamps the concentration of reactant $\text{X}$ at a constant $5.0\:\text{mM}$, what is the *maximum* possible concentration of product $\text{Y}$ (in $\mu\text{M}$) that the next enzyme in the pathway can allow to accumulate before the reaction stalls out and reaches equilibrium?

### 10.3 Temperature Dependence: The van 't Hoff Equation
*Quantify how the balance of heat and chaos shifts when the thermal environment changes.*

1. **Simple:** A physical chemist measures the equilibrium constant of a novel enzyme at five different temperatures. They plot $\ln(K_{eq})$ on the y-axis versus $1/T$ on the x-axis and get a perfectly straight line with a slope of $+5200\:\text{K}$ and a y-intercept of $+12.5$. Using the linear van 't Hoff equation, calculate the Standard Enthalpy ($\Delta H^\circ$) in kJ/mol and the Standard Entropy ($\Delta S^\circ$) in J/(mol K) for this reaction.
2. **Intermediate:** The binding of a regulatory drug to its target protein is exothermic ($\Delta H^\circ = -42.0\:\text{kJ/mol}$). At a normal body temperature of $37^\circ\text{C}$ ($310.15\:\text{K}$), the binding constant is $K_1 = 3.5 \times 10^5$. A patient is put into induced therapeutic hypothermia, dropping their body temperature to $32^\circ\text{C}$ ($305.15\:\text{K}$). Use the two-point van 't Hoff equation to calculate the new binding constant ($K_2$). Does the drug bind more tightly or less tightly in the cold?
3. **Advanced (The Calculus of van 't Hoff):** Starting from the Gibbs-Helmholtz derivative $\frac{d(\ln K_{eq})}{dT} = \frac{\Delta H^\circ}{RT^2}$, integrate both sides from $T_1$ to $T_2$ to mathematically derive the two-point van 't Hoff equation. What physical assumption must you make about $\Delta H^\circ$ in order to legally pull it out of the integral? Is this assumption valid over a $100^\circ\text{C}$ temperature span?

### 10.4 The Biochemical Standard State ($\Delta G^{\circ\prime}$)
*Adjust the impossible baseline of physical chemistry to the physical reality of aqueous life.*

1. **Simple:** Define the three specific rules that differentiate the Biochemical Standard State ($^\prime$) from the strict Physical Chemistry Standard State ($^\circ$). Why is it physically impossible for a living cell to survive at the strict physical chemistry baseline?
2. **Intermediate:** The hydrolysis of a specific ester releases exactly one proton ($\text{H}^+$) as a product. The physical chemistry standard free energy for this reaction is $\Delta G^\circ = +12.5\:\text{kJ/mol}$ at $37^\circ\text{C}$ ($310.15\:\text{K}$). Calculate the Biochemical Standard Free Energy ($\Delta G^{\circ\prime}$) by accounting for the fact that the baseline proton concentration is $1.0 \times 10^{-7}\:\text{M}$ instead of $1.0\:\text{M}$. 
3. **Advanced (The Water Problem):** In physical chemistry, pure liquids are assigned an activity of exactly $1$, which removes them from the equilibrium constant ($K_{eq}$) equation. If a biochemist decided to be hyper-pedantic and actually included the concentration of bulk water ($55.5\:\text{M}$) in the denominator of the $K_{eq}$ expression for a condensation reaction at $298.15\:\text{K}$, how much would this mathematical choice artificially alter the calculated $\Delta G^\circ$ value (in kJ/mol)? 

### 10.5 Coupled Reactions and the Steady State
*Evaluate the thermodynamic reality of ATP and the distinction between equilibrium and life.*

1. **Simple:** A cell needs to synthesize a complex lipid. The condensation reaction is heavily unfavored ($\Delta G^{\circ\prime} = +22.0\:\text{kJ/mol}$). The cell couples this synthesis to the hydrolysis of one molecule of ATP ($\Delta G^{\circ\prime} = -30.5\:\text{kJ/mol}$). Using thermodynamic addition, calculate the net $\Delta G^{\circ\prime}$ for the coupled reaction. Is the net process spontaneous?
2. **Intermediate:** A high school textbook claims that ATP provides energy by "exploding" next to an enzyme, releasing a spark of heat that forces an unfavorable bond together. Correct this gross misconception. Using the example of glutamine synthetase, explain the physical mechanism of reaction coupling. How does the covalent attachment of a phosphate group fundamentally change the equilibrium constant of the chemical intermediate?
3. **Advanced (Equilibrium vs. Steady State):** Explain the mathematical and physiological difference between Chemical Equilibrium and a Steady State. If the concentration of ATP in a human cell is completely stable at $5.0\:\text{mM}$ for three straight hours, does this mean the ATP synthesis/hydrolysis cycle has reached equilibrium? Why is reaching true thermodynamic equilibrium ($\Delta G = 0$) the physical definition of biological death?