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

(hydrogen_atom)=
## Hydrogen Atom
While we have looked at model systems and 

As mentioned in {ref}`rigid_rotator` we will that model for the hydrogen atom. It may not be exactly clear why we would use this model so let's discuss the details. A hydrogen atom is the simplest atom and as far as a chemist is concerned the simplest form of matter. When we are first introduced to atoms we are typically given the Bohr model where there is a dense nucleus where the majority of the matter of the atom is contained with the lighter electrons ``orbiting'' around far from the nucleus. This is a reasonable first step to the model based Rutherford's gold foil experiment and the experiments working on electron characteristics (Thompson's cathode ray tube and Millikan's oil drop). However, there are some fundamental problems with treating this atomic system like this.

## Hydrogen Wavefunction

We will treat the hydrogen system as a rigid rotator model 

### Hydrogen Energy States

(quantum_numbers)=
### Quantum Numbers

The four quantum numbers are $n$, $l$, $m_l$ and $m_s$. Here is a summary of what the quantum numbers do and what values are allowed.

The principal quantum number, $n$, can have values of $n = 1,2,3,\ldots$. The primary physical meaning of this quantity is that it determines what the energy of the orbital will be. For hydrogen, orbitals with the same $n$ value will have the same energy, or often said to be degenerate. 

The angular momentum quantum number is $l$. The values that $l$ can have is based on the principal quantum number $n$. The allowable states are $l = 0,1,2,\ldots,(n-1)$. The primary physical meaning of this are that it tells you the shape of the of orbital. Additionally, the $l$ numbers have a letter designation that are given below. (see diagram for pictures of examples of the shapes of these orbitals)
- $l = 0 \rightarrow\:\text{s orbital}$
- $l = 1 \rightarrow\:\text{p orbital}$
- $l = 2 \rightarrow\:\text{d orbital}$
- $l = 3 \rightarrow\:\text{f orbital}$

The magnetic quantum number, $m_l$, defines the orientation of the orbital in three-dimensional space. The $m_l$ values are determined by the respective angular quantum number, $l$. The allowable values are $m_l = -l, -(l-1),\ldots,-1,0,1,\ldots,l-1,l$. For example, if $l = 2$, then $m_l = -2,-1,0,1,2$.  

Finally, there is the spin quantum number $m_s$. This quantum number is only two valued and does not depend on the other quantum numbers. It can be $m_s = \frac{1}{2}$ or $m_s=-\frac{1}{2}. It is an intrinsic angular momentum of the electron, separate from the angular momentum of the electron orbital around the nucleus this is why it is called spin. 

## Multielectron Atoms
Recall from {ref}`quantum_numbers`

There are several fundamental rules for multielectron atoms that inform us on how to identify electrons. The first is that no two electrons in the same atom may share all four quantum numbers with any other electron. This is known as the Pauli exclusion principle. Another rule is that all electrons will fill from the lowest energy and move up systematicaly. This is known as Aufbau. Last, when filling orbitals with degenerate states, electrons will enter singly and only after all degenerate orbitals have a single electron will they begin to pair up. This is known as Hund's rule. 

**Conceptual question** "A substance that is paramagnetic is attracted to magnetic fields, while a substance that is diamagnetic is repelled by magnetic fields. How does this relate to paired and unpaired electrons?"
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
The order of 

Why do 

### Adsorption and Emission
Hydrogen and hydrogenic atoms
Selection rules
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

You are free to do none, some or all these problems as you see fit. They would be very helpful to use in studying for the chapter exams.