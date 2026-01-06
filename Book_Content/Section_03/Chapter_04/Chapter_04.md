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


It is important to mention here that when we are discussing different types of theories about chemical bonds that many parts of the different theories will overlap or share words or pictures. This can lead to some confusion about conclusions that each theory will draw or assumptions that are made. Please pay special attention to the assumptions each theory is making. 

In general what is bonding? In the most simplistic case bonding is 

Ionic bonding
## Lewis Theory and VSEPR
Covalent bonding
## Valence Bond Theory
Like Lewis theory we will have localized electrons. W
You are likely already familiar with valence bond 

**question. explain why water and methane are difficult to make fit in the valence bond theory framework. 


## Hybrid Orbital Theory

As we saw at the end of the last section there are limitations to valence bond theory. Most importantly that we often do not have the correct number of half filled orbitals to account for the number of bonds. Also, using just the $s$ and $p$ orbitals we cannot account for shapes that don't have $90\degree$ or $180\degree$ angles. 

From general chemistry we have been told to look at the VSPER group and then determine the extent of hybridization. For example, in something with four electron groups (bonds or lone pairs) around a central atom in a Lewis structure, for example water or methane (see image....) you would hybridize one $2s$ orbital with three $2p$ orbitals to make four $sp^3$ hybridized orbitals. These will have, as a consequence, the correct tetrahedral shape and the correct bond angles (though they may be larger or smaller depending on lone pairs). We haven't discussed where this comes from though. 

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

You are free to do none, some or all these problems as you see fit. They would be very helpful to use in studying for the chapter exams.