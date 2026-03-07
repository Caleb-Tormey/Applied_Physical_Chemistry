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
  enumerator: 4.%s
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
# Chapter 4: Chemical Bonding and Molecular Orbitals

:::{include} sec_1_introduction_to_bonding.md
:::
:::{include} sec_2_lewis_vsepr.md
:::
:::{include} sec_3_vb_theory.md
:::
:::{include} sec_4_hybrid.md
:::
:::{include} sec_5_MO.md
:::
:::{include} sec_6_MO_poly.md
:::






The **Conceptual Question** comment is left in to make it easier to find in the markdown. 
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
    question_text="Why is it reasonable to promote the electrons from lower energy level unhybridized orbitals to hybrid orbitals?  "
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

You are free to do none, some, or all of these problems as you see fit. They are designed to mimic the conceptual reasoning and physical applications you will encounter in the rest of the book and in your future biochemistry courses.

### 1. The Nature of the Chemical Bond and Energy
*Challenge the common misconceptions about bond energy and thermodynamic stability.*

1. **Simple:** A biology textbook states, "The breaking of the high-energy phosphate bond in ATP releases energy to power cellular processes." Based on Section 4.1, explain why this statement is physically incorrect. Where does the released energy actually come from?
2. **Intermediate:** Look at a standard potential energy curve for a diatomic molecule. What physical forces dictate the steep repulsive curve at very short internuclear distances, and what forces define the attractive curve at longer distances? 
3. **Advanced:** The average kinetic (thermal) energy of molecules in a human cell at 37°C is relatively low. If a specific drug-receptor interaction relies solely on a very shallow potential energy well (weak bonding), what will happen to that drug-receptor complex in the chaotic, warm environment of the cell?

### 2. VSEPR, 3D Geometry, and Polarity
*Translate 2D bookkeeping into 3D shapes and predict macroscopic intermolecular forces.*

1. **Simple:** Using AXE notation, determine the electron geometry and molecular geometry for Carbon Dioxide (CO₂) and Sulfur Dioxide (SO₂). Why do they have different bond angles despite both having two oxygen atoms bonded to a central atom?
2. **Intermediate:** Look at the structure of a lipid molecule in a cell membrane. The hydrocarbon tail is entirely composed of tetrahedral (AX₄) carbon atoms. Why is this tail considered nonpolar and hydrophobic, even though the individual C-H bonds have a slight dipole?
3. **Advanced (Formal Charge & Stability):** The thiocyanate ion (SCN⁻) can be drawn using three different resonance structures. Draw them, assign formal charges to each atom in all three structures, and use those charges to predict which structure contributes most to the actual localized physical state of the ion.

### 3. Valence Bond Theory and Hybridization
*Apply the LCAO mathematical workaround to solve the geometry problem of localized bonds.*

1. **Simple:** If a carbon atom attempted to bond with hydrogen using only its native, unhybridized ground-state atomic orbitals ($2s$ and $2p$), what molecule would it form, and what would the bond angles be? 
2. **Intermediate:** Identify the hybridization state ($sp$, $sp^2$, or $sp^3$) of every carbon, nitrogen, and oxygen atom in the amino acid Glycine (NH₂-CH₂-COOH). 
3. **Advanced:** In Section 4.4, we established that the peptide bond linking amino acids is $sp^2$ hybridized. 
    * (a) Explain how the unhybridized $p$ orbitals on the carbon and nitrogen interact.
    * (b) Why does this specific quantum mechanical interaction completely restrict rotation around the peptide bond, and why is this vital for protein folding?

### 4. Molecular Orbital Theory: Diatomics
*Abandon the localized assumption to explain the electronic and magnetic reality of molecules.*

1. **Simple:** What is the physical difference between constructive interference and destructive interference when combining two 1s atomic wavefunctions? How does this relate to the concept of a node in an antibonding orbital?
2. **Intermediate:** Draw the Lewis structure for diatomic oxygen (O₂). Does this localized model predict that oxygen is diamagnetic or paramagnetic? Now, look at the MO diagram for O₂. How does Hund's rule applied to the degenerate $\pi^*$ orbitals correctly predict the experimental magnetic behavior of the molecule?
3. **Advanced (Superoxide):** In biochemistry, oxidative stress is often caused by the "superoxide" radical, O₂⁻. 
    * (a) Using the MO diagram for neutral O₂, add one extra electron to create the O₂⁻ diagram. 
    * (b) Calculate the bond order for neutral O₂ and the superoxide O₂⁻. (Bond Order = [Bonding Electrons - Antibonding Electrons] / 2). 
    * (c) Based on your calculation, is the bond in superoxide stronger or weaker than in neutral oxygen?

### 5. Polyatomics and Biochemical Applications
*Connect frontier molecular orbitals to the colors of life and molecular toxicity.*

1. **Simple:** Define the terms HOMO and LUMO. Why are these specific molecular orbitals considered the "frontier" of chemical reactivity?
2. **Intermediate:** Ethanol (drinking alcohol) and beta-carotene (the pigment in carrots) are both organic molecules. Ethanol absorbs high-energy UV light and is colorless, while beta-carotene absorbs lower-energy visible light and appears orange. Use the concept of delocalized conjugated $\pi$ systems and the HOMO-LUMO gap to explain this difference.
3. **Advanced:** Carbon monoxide (CO) is a lethal poison because it binds to the iron (Fe) in hemoglobin much tighter than O₂ does. Describe the "push-pull" orbital interaction that causes this. Specifically, identify which orbital on CO acts as the electron donor ($\sigma$ donation) and which empty orbital acts as the electron acceptor ($\pi$ backbonding).