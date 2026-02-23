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
  enumerator: 1.%s
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
# Chapter 1: History of Quantum Mechanics

We will begin by looking at the origins of quantum mechanics. This history is long and deep, but it is enough to say that using Newton's notions for how the physics of the world worked scientists were able to work out most problems. We call the physics of this era classical mechanics. In classical mechanics all physical observables like position, momentum and energy can, in principle, take on any value within a continuous range. Also, fundamentally classical physics is deterministic. If we know precise information about the system (position, momentum) we can predict the future exactly. We will find that quantum theory does not have this feature. Rather 


:::{include} sec_a_all_about_waves.md
:::
:::{include} sec_1_classical_physics_breakdown.md 
:::
:::{include} sec_2_early_atomic_models.md
:::
:::{include} sec_3_matter_as_waves.md
:::
:::{include} sec_4_formalism_of_QM.md
:::
:::{include} sec_5_the_uncertainty_principle.md
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
manager = QAManager(page_title="Chapter A: Mathematics Review")
display(HTML(manager.render()))
:::
## Practice Problems

You are free to do none, some, or all of these problems as you see fit. They are designed to mimic the mathematical manipulations and physical reasoning you will encounter in the rest of the book.

### 1. Nature of Waves and Light
*Apply the fundamental relationship $\lambda\nu = c$ to electromagnetic radiation.*
1.  **Simple:** A radio station broadcasts at a frequency of $101.5\:\text{MHz}$ ($1.015 \times 10^8\:s^{-1}$). What is the wavelength of this signal in meters?
2.  **Intermediate:** A laser pointer emits green light with a wavelength of $532\:\text{nm}$. Calculate the frequency of this light. *(Hint: Remember to convert nanometers to meters first: $1\:\text{nm} = 10^{-9}\:\text{m}$).*
3.  **Advanced:** Compare the time it takes for a radio wave ($\lambda = 3.0\:\text{m}$) vs. an X-ray ($\lambda = 1.0\:\text{Å}$) to travel from the Sun to the Earth (Distance $\approx 1.5 \times 10^{11}\:\text{m}$). What does this imply about the speed of light for different wavelengths in a vacuum?

### 2. Quantized Energy (Planck)
*Use $E = h\nu$ to determine the energy of individual photons. Constants: $h = 6.626 \times 10^{-34}\:\text{J s}$.*
1.  **Simple:** Calculate the energy (in Joules) of a single photon of UV light with a frequency of $3.0 \times 10^{15}\:\text{Hz}$.
2.  **Intermediate:** Calculate the energy of a photon of red light with a wavelength of $700\:\text{nm}$. *(Hint: You must combine $E=h\nu$ and $c=\lambda\nu$).*
3.  **Advanced (Molar Energy):** In chemistry, we often work with moles. Calculate the total energy contained in **one mole** of photons with a wavelength of $254\:\text{nm}$ (UV-C light). Compare this to the energy required to break a C-C bond ($\approx 347\:\text{kJ/mol}$).

### 3. The Photoelectric Effect
*Analyze the ejection of electrons using $KE_{electron} = h\nu - \Phi$.*
1.  **Simple:** A metal has a work function ($\Phi$) of $3.5 \times 10^{-19}\:\text{J}$. What is the minimum "threshold" frequency of light required to eject an electron?
2.  **Intermediate:** Light with a frequency of $1.0 \times 10^{15}\:\text{Hz}$ strikes the metal from the previous problem. Calculate the kinetic energy of the ejected electron.
3.  **Advanced (Velocity):** Using the kinetic energy calculated in the Intermediate problem, determine the **velocity** of the ejected electron. *(Mass of an electron $m_e = 9.109 \times 10^{-31}\:\text{kg}$).*

### 4. The Bohr Model
*Calculate energy transitions in the Hydrogen atom using the Rydberg formula.*
1.  **Simple:** Calculate the energy of an electron in the ground state ($n=1$) of a Hydrogen atom. (Recall $E_n = -2.178 \times 10^{-18}\:\text{J} \left(\frac{1}{n^2}\right)$).
2.  **Intermediate:** An electron falls from the $n=3$ energy level to the $n=2$ energy level (part of the Balmer series). Calculate the change in energy ($\Delta E$) and determine if energy is absorbed or emitted.
3.  **Advanced:** Calculate the wavelength (in nm) of the photon emitted during the transition in the previous problem. Does this correspond to visible light?

### 5. Matter as Waves (De Broglie)
*Apply the concept of wave-particle duality using $\lambda = \frac{h}{p} = \frac{h}{mv}$.*
1.  **Simple:** Calculate the De Broglie wavelength of an electron ($mass = 9.11 \times 10^{-31}\:\text{kg}$) moving at $2.0 \times 10^6\:\text{m/s}$.
2.  **Intermediate (Macroscopic):** Calculate the De Broglie wavelength of a $0.145\:\text{kg}$ baseball thrown at $40.0\:\text{m/s}$. Compare this length to the size of a proton ($\approx 10^{-15}\:\text{m}$) to explain why we don't observe wave behavior in baseballs.
3.  **Advanced (Acceleration):** An electron is accelerated from rest through a potential difference of $100\:\text{Volts}$, giving it a Kinetic Energy of $100\:\text{eV}$ ($1.602 \times 10^{-17}\:\text{J}$). First, find the velocity, then calculate the wavelength.

### 6. The Uncertainty Principle
*Explore the limits of measurement using $\Delta x \Delta p \ge \frac{h}{4\pi}$.*
1.  **Simple:** If the uncertainty in the position of a particle is $\Delta x = 1.0 \times 10^{-10}\:\text{m}$ (approximate size of an atom), what is the minimum uncertainty in its momentum ($\Delta p$)?
2.  **Intermediate:** An electron is confined to a box of length $1.0\:\text{nm}$. Assuming the uncertainty in position is the size of the box, calculate the minimum uncertainty in its **velocity**.
3.  **Advanced (Mass Dependence):** Repeat the intermediate calculation for a helium atom ($mass \approx 6.64 \times 10^{-27}\:\text{kg}$) confined to the same $1.0\:\text{nm}$ box. How does the mass of the particle affect the uncertainty in its velocity?





