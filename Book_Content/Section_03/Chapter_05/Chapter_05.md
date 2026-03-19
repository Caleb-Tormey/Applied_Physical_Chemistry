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
  enumerator: 5.%s
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
# Chapter 5: Molecular Symmetry and Spectroscopy
:::{include} sec_1_introduction_mol_symmetry.md 
:::
:::{include} sec_2_point_groups.md
:::
:::{include} sec_3_energy_scales.md
:::
:::{include} sec_4_mol_term_symbols.md
:::
:::{include} sec_5_IR_raman.md
:::
:::{include} sec_6_UV_vis_beers.md
:::
:::{include} sec_7_chromophores.md
:::
%## Introduction to Molecular Symmetry Elements
%```markdown
%```{include} /Book_Content/Section_03/Chapter_05/part1-intro_mol_sym.md
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

You are free to do none, some, or all of these problems as you see fit. They are designed to test both your conceptual understanding and your ability to apply physical laws to calculate real biochemical values.

### 1. Molecular Symmetry and Point Groups
*Distinguish physical actions from mathematical frameworks and read the symmetry "cheat codes."*

1. **Simple:** Explain the physical difference between a "symmetry element" and a "symmetry operation." Why must every molecule possess the Identity ($E$) element?
2. **Intermediate:** Look at the $C_{2v}$ character table. If a specific molecular orbital is assigned the Mulliken symbol $B_1$, what does the "B" tell you about how that orbital behaves when rotated around the molecule's principal axis?
3. **Advanced (The Limits of Symmetry):** A single water molecule belongs to the $C_{2v}$ point group, possessing a principal rotation axis and mirror planes. However, an entire folded protein like myoglobin belongs to the $C_1$ point group (possessing only the Identity element). Explain why massive biological polymers completely lose global symmetry, and why physical chemists might still use high-symmetry point groups (like $D_{4h}$) to model the local active site of that same protein.

### 2. Energy Scales and Term Symbols
*Connect the energy of a photon to the physical motion of the molecule and its quantum state.*

1. **Simple:** Match the region of the electromagnetic spectrum (Microwave, Infrared, UV-Visible) to the physical molecular transition it excites (Valence Electron Transition, Bond Vibration, Molecular Rotation). 
2. **Intermediate (Energy Calculation):** A peptide bond absorbs UV light at 214 nm, while a carbon-oxygen double bond stretches at an IR wavenumber of 1700 cm⁻¹. Using the Planck-Einstein relation ($E = hc/\lambda$), calculate the energy of *one mole* of photons for both of these transitions in kJ/mol. *(Note: $h = 6.626 \times 10^{-34} \text{ J s}$, $c = 3.0 \times 10^8 \text{ m/s}$, $N_A = 6.022 \times 10^{23} \text{ mol}^{-1}$)*.
3. **Advanced (The Oxygen Paradox):** The ground state of molecular oxygen is a Triplet ($^3\Sigma_g^-$). The organic molecules comprising the human body are almost exclusively Singlets. Using the quantum mechanical selection rules for electronic transitions, explain why this spin mismatch prevents humans from spontaneously combusting in the atmosphere. 

### 3. Vibrational Spectroscopy: IR and Raman
*Apply the rules of dipoles, polarizability, and mutual exclusion to vibrating bonds.*

1. **Simple:** State the fundamental selection rule required for a normal mode of vibration to be Infrared (IR) active, and the selection rule required for it to be Raman active.
2. **Intermediate:** Carbon dioxide (CO₂) is a linear molecule with a center of inversion ($i$). It has a symmetric stretching mode and an asymmetric stretching mode. Predict which mode will appear on an IR spectrum and which will appear on a Raman spectrum. What elegant physical chemistry rule does this demonstrate?
3. **Advanced (The Water Problem):** You are tasked with determining the secondary structure (alpha-helices vs. beta-sheets) of a newly discovered enzyme. Because it is a functional protein, it must be analyzed in a liquid water buffer. Explain why you would choose Raman spectroscopy over IR spectroscopy for this experiment, referencing the specific physical properties of the H₂O molecule's electron cloud and dipole.

### 4. Electronic Spectroscopy and Beer's Law
*Understand the probabilities of absorption and calculate concentrations from light.*

1. **Simple:** In the Beer-Lambert Law ($A = \varepsilon l c$), what does the molar absorptivity constant ($\varepsilon$) physically represent at the quantum mechanical level?
2. **Intermediate (Beer's Law Calculation):** You are measuring the concentration of the amino acid Tryptophan ($\varepsilon_{280} = 5500 \text{ M}^{-1}\text{cm}^{-1}$) in a standard 1.0 cm path-length cuvette. The spectrophotometer reads an absorbance of $A = 0.85$. Calculate the molar concentration of the Tryptophan. As a bonus, knowing that $A = -\log_{10}(T)$, calculate the percent transmittance ($\%T$) of the sample.
3. **Advanced (The Limits of Linearity):** A student prepares a highly concentrated (2.5 M) solution of a protein and measures its absorbance, expecting a massive signal. However, the absorbance is much lower than the Beer-Lambert law predicts. Explain the physical intermolecular interactions that cause this linear law to fail at high concentrations. 

### 5. Chromophores, Auxochromes, and Fluorescence
*Track the flow of energy and calculate the thermodynamics of glowing molecules.*

1. **Simple:** What is an auxochrome? How does attaching an auxochrome with a lone pair of electrons to a chromophore affect the wavelength of light it absorbs?
2. **Intermediate (The Particle in a Box):** Ethylene (one C=C bond) absorbs high-energy UV light, making it colorless. Beta-carotene (eleven conjugated C=C bonds) absorbs lower-energy blue light, making it appear orange. Using the "Particle in a 1D Box" model from Chapter 4, explain how the length of the conjugated $\pi$ system dictates the energy of light the molecule absorbs.
3. **Advanced (Stokes Shift Energy Calculation):** Wild-type Green Fluorescent Protein (GFP) maximally absorbs high-energy blue light at an excitation wavelength of 395 nm, and it emits lower-energy green light at 509 nm. Calculate the exact amount of energy (in kJ/mol) that is lost as heat to the surrounding water via internal conversion during a single fluorescent cycle.