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
  enumerator: B.%s
--- 
:::{code-cell} python
:tags: ["remove-input", "remove-output"]

import sys
import os

from IPython.display import display, HTML
# This block MUST be at the top of your file.
# It finds the project root and adds it to the Python path.
# Adjust the number of ".." to match how many folders deep your file is.
try:
    cwd = os.getcwd()
    # e.g., use ("..", "..") for a file 2 levels deep.
    project_root = os.path.abspath(os.path.join(cwd, "..", "..", ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    from _ext.interactive_qa import QuestionBlock
except Exception as e:
    print(f"Error setting project path: {e}")
:::
# Chapter B. Physics Introduciton and Review
While mathematics provides the vocabulary and grammar for science, physics provides the story. As we move through this book, it is crucial to remember that the equations we use are not just abstract mathematical puzzles to be solved; they are concise summaries of physical reality. Physics is fundamentally about modeling the world—observing complex, messy natural phenomena and stripping away the noise to find the simple, underlying rules that govern them. An equation like $F=ma$ or $E=h\nu$ is simply a shorthand way of describing a profound relationship between properties of the universe. Do not get lost in the algebra; instead, view these mathematical tools as the scaffolding that supports our understanding. We use them to quantify and predict the behavior of matter, ensuring that our mental models match the reality we observe in the laboratory. You should think about the physical principles and mathematics as telling the story of how the world works when you focus on one aspect or another. 

:::{include} sec_1_terminology.md
:::
:::{include} sec_2_newtons_laws.md
:::
:::{include} sec_3_vectors.md
:::
:::{include} sec_4_energy.md
:::
:::{include} sec_5_momentum.md
:::
:::{include} sec_6_conservation_laws.md
:::









:::{code-cell} python
:tags: ["remove-input"]

from _ext.interactive_qa import QAManager
from IPython.display import display, HTML

# This renders the final control panel.
# Pass the desired title for the printed page here.
manager = QAManager(page_title="Chapter B: Physics Introduction and Review")
display(HTML(manager.render()))
:::
## Practice Problems

You are free to do none, some or all these problems as you see fit. They would be very helpful to use in studying for the chapter exams. 
- Do the following unit conversions
    * $6.23\:m\:s^{-1}$ to $nm\:hr^{-1}$
    * $7.85\times 10^{12}\:\mu m^3$ to $ft^3$
    * $5.93\times 10^3\:s^{-1}$ to $min^{-1}$
- What force is required to accelerate a mass of $12.345\:g$ is by $35.7\:m\:s^{-2}$ in Newtons?
- A mass off $2.3\:g$ is raised to a height of $31.00\:m$. What is the maximum kinetic energy it can achieve? 
- Give the distance between the following pairs of points
    * $\text{A} = \left(-5.6\right)$ and $\text{B} = \left(-7.7\right)$
    * $\text{A} = \left (1.4,2.0\right)$ and $\text{B} = \left(-2.5,7.2\right)$
    * $\text{A} = \left (5.4,-8.1,-9.3\right)$ and $\text{B} = \left(12.0,27.2,0.4\right)$ 
- What force is required to hold two electrons at a distance of $1.00\:\AA$ from one another in Newtons?

