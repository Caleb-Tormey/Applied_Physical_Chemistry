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

You are free to do none, some or all these problems as you see fit. They would be very helpful to use in studying for the chapter exams.