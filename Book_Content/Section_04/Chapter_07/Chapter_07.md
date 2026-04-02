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
  enumerator: 7.%s
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
# Chapter 7: Introduction to Thermodynamics
:::{include} sec_1_introduction_thermo.md
:::
:::{include} sec_2_ideal_gas_law.md
:::
:::{include} sec_3_real_gases.md
:::
:::{include} sec_4_mixtures_pressures.md
:::
:::{include} sec_5_reversible_irreversible.md
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

:::{code-cell} python
:tags: ["remove-input"]

from _ext.interactive_qa import QAManager
from IPython.display import display, HTML

# This renders the final control panel.
# Pass the desired title for the printed page here.
manager = QAManager(page_title="Chapter 7: Introduction to Thermodynamics")
display(HTML(manager.render()))
:::
## Practice Problems

You are free to do none, some, or all of these problems as you see fit. They are designed to mimic the mathematical manipulations and physical reasoning you will encounter in the rest of the book.

### 7.1 The Macroscopic World: Defining the Sandbox
*Identify the boundaries of your thermodynamic system and distinguish between the state of the system and the path taken to get there.*

1. **Simple:** Classify the following biological systems as Open, Closed, or Isolated: 
    * (a) A sealed, rigid bomb calorimeter containing a metabolizing cell culture.
    * (b) A perfectly insulated thermos of hot soup.
    * (c) A living human being.
    * Identify which of the following are state functions and which are path functions: Temperature ($T$), Heat ($q$), Volume ($V$), Work ($w$), Internal Energy ($U$).

2. **Intermediate:** Imagine you are analyzing the internal energy of a system. The system starts at State A ($P_1, V_1, T_1$) and undergoes a complex series of expansions and compressions, eventually returning exactly to State A. What is the total change in Volume ($\Delta V$) and the total change in Internal Energy ($\Delta U$) for this entire cyclic process? Explain why this is true based on the definition of a state function.

3. **Advanced:** Prove mathematically why work ($w$) is a path function by considering a gas that expands from $V_1 = 1.0\:\text{L}$ to $V_2 = 5.0\:\text{L}$ under two different pathways: 
    * Pathway A: The external pressure is kept constant at $1.0\:\text{atm}$.
    * Pathway B: The external pressure is kept constant at $5.0\:\text{atm}$ for the first $2.0\:\text{L}$ of expansion, and then drops to $1.0\:\text{atm}$ for the remainder. 
    * Calculate the total work done in L·atm for both pathways. Does $\Delta V$ change? Does $w$ change?

### 7.2 The Ideal Gas Law: A Perfect (But Fake) Baseline
*Apply the fundamental equation of state and understand the physical assumptions required to use it.*

1. **Simple:** Calculate the number of moles of oxygen gas ($\text{O}_2$) present in a human lung with a volume of $2.5\:\text{L}$ at standard atmospheric pressure ($1.0\:\text{atm}$) and normal body temperature ($37^\circ\text{C}$). Use $R = 0.08206\:\text{L atm / mol K}$.

2. **Intermediate:** What are the "Two Massive Assumptions" of the Ideal Gas Law? Explain physically why an ideal gas can never be condensed into a liquid, no matter how much you drop the temperature or increase the pressure.

3. **Advanced (The Solute Analogy):** Physical chemists use the ideal gas law to model dilute biological solutions. In a dilute solution, the solute molecules act like a "gas" expanding to fill the "vacuum" of the liquid solvent. This creates Osmotic Pressure ($\Pi$). By substituting $\Pi$ for $P$ and concentration ($c = n/V$) into the ideal gas law, calculate the osmotic pressure (in atm) of a $0.15\:\text{M}$ saline solution ($\text{NaCl}$) at $37^\circ\text{C}$. *(Hint: Remember that NaCl dissociates into two ions, so the effective concentration of particles is doubled!)*

### 7.3 Real Gases: The Chapter 6 Payoff
*Correct the flaws of the ideal gas law using the van der Waals parameters for sterics and intermolecular forces.*

1. **Simple:** Look at the van der Waals equation: $(P + a(n/V)^2)(V - nb) = nRT$. Which parameter ($a$ or $b$) corrects for the fact that molecules have physical size (excluded volume)? Which parameter corrects for the intermolecular attractions we learned about in Chapter 6? 

2. **Intermediate:** Compare the van der Waals parameters for Helium gas ($\text{He}$) and Water vapor ($\text{H}_2\text{O}$). 
    * Which gas will have a larger $b$ value, and why?
    * Which gas will have a massively larger $a$ value, and what specific intermolecular force is responsible for this?

3. **Advanced (Macromolecular Crowding):** Calculate the pressure exerted by $1.0\:\text{mole}$ of $\text{CO}_2$ confined to a highly compressed volume of $0.5\:\text{L}$ at $300\:\text{K}$. 
    * (a) Use the Ideal Gas Law.
    * (b) Use the van der Waals equation. For $\text{CO}_2$, $a = 3.59\:\text{L}^2\text{atm/mol}^2$ and $b = 0.0427\:\text{L/mol}$.
    * (c) Is the real pressure lower or higher than the ideal pressure? Explain how the attractive forces between $\text{CO}_2$ molecules alter the physical force exerted on the walls of the container. 

### 7.4 Mixtures and Partial Pressures
*Calculate the independent driving forces of molecules in complex mixtures using Dalton's Law.*

1. **Simple:** Dry atmospheric air is roughly $78\%\:\text{N}_2$, $21\%\:\text{O}_2$, and $1\%\:\text{Ar}$ by mole fraction. If the total barometric pressure at sea level is $760\:\text{mmHg}$, calculate the partial pressure of oxygen ($P_{\text{O}_2}$) in mmHg. 

2. **Intermediate (The Thermodynamics of Breathing):** When you inhale, the dry air from the environment is immediately saturated with water vapor in your warm lungs. At $37^\circ\text{C}$, the vapor pressure of water is exactly $47\:\text{mmHg}$. If the total pressure in your lungs is $760\:\text{mmHg}$, what is the *new* total pressure available for the dry gases? Calculate the actual $P_{\text{O}_2}$ inside the alveolar space. 

3. **Advanced:** A scuba diver breathes a customized gas mixture called Heliox ($20\%\:\text{O}_2$ and $80\%\:\text{He}$) to avoid nitrogen narcosis. If the diver is at a depth where the total pressure is $5.0\:\text{atm}$, calculate the partial pressure of $\text{O}_2$ in atm. Based on Henry's Law, how does this high partial pressure affect the concentration of dissolved oxygen in the diver's bloodstream compared to standing at sea level?

### 7.5 Heat, Work, and Pathways: Moving the Energy
*Quantify the transfer of energy through random thermal motion ($q$) and directed physical expansion ($w$).*

1. **Simple:** Calculate the physical work ($w$) in Joules done by your chest cavity when you take a deep breath, expanding your lungs by $0.50\:\text{L}$ against a constant atmospheric pressure of $1.0\:\text{atm}$. Is the work positive or negative with respect to your body (the system)? *(Note: $1\:\text{L atm} = 101.325\:\text{J}$)*.

2. **Intermediate:** Calculate the heat ($q$) required to raise the temperature of a $250\:\text{g}$ cup of liquid water from $20^\circ\text{C}$ to $37^\circ\text{C}$ (body temperature). The specific heat capacity of water is $4.18\:\text{J/(g K)}$. If the water does absolutely no expansion work during this heating process ($w=0$), what is the total change in Internal Energy ($\Delta U$) of the water?

3. **Advanced (The Efficiency of Life):** A biochemical system generates $1.0\:\text{mole}$ of gas at $310.15\:\text{K}$. The gas expands from $1.0\:\text{L}$ to $10.0\:\text{L}$.
    * (a) Calculate the work done if the expansion is perfectly **irreversible** against a constant external pressure of $1.0\:\text{atm}$. 
    * (b) Calculate the work done if the expansion is perfectly **reversible** (isothermal). Use $w = -nRT \ln(V_2/V_1)$ with $R = 8.314\:\text{J/(mol K)}$.
    * (c) Which pathway extracts the *maximum* possible work from the system? Explain why living cells use enzymes to break massive metabolic reactions into dozens of tiny, near-reversible steps rather than burning fuel in one massive, irreversible explosion.