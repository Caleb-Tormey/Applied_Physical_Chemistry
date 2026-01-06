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


## Blackbody Radiation

### Stefan-Boltzman Law

### Rayleigh-Jeans Law

### UV-Catastrophe

### Planck’s solution

### Light
We need to talk about some of the basics of light before we move forward. This will not be our only discussion of this topic but it is important that we have some of the basics down before moving forward. The first is that light is an electro-magnetic wave. From the diagram (INCLUDE DIAGRAM), we see that it is an alternating electric wave in one dimension and then an alternating magnetic wave in a perpendicular plane. Because it is a wave we can define it based on the length of the wave. The length of the wave (measured from crest to crest) is called $\lambda$, pronounced lambda. We also know from other experiments that we won't discuss in this text that light all travels at the same speed in a vacuum. That is the speed of light, called $c$, and is approximately $300,000\:km\:s^{-1}$. So we know wavelengths of the light but we also know the speed. That means we can determine another property of light. Consider a wave is moving by you and you are at a certain point in space. You could see the rise and fall of the crest of the wave as it moves. You could see how many times the wave rises and falls in a given amount of time. Let's say per second. Given that all light, regardless of wavelength, moves at the same speed we can now find the frequency of the light. The relationship of these three quantities is summarized in equation {ref}`wave_freq`.

:::{math}
:label: wave_freq
\lambda\nu = c
:::


### Photo-electric Effect
The photo electric effect was a phenomena where light was shown on a metal surface. Under certain conditions electrons would be ejected from the surface of the metal. Because electrons have mass and they were moving these electrons would have a certain amount of kinetic energy (recall based on equation {ref}`kinetic_energy`). 
Recall
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
### Waves
There are some important properties and characteristics of waves we need to make sure we have down moving forward. 
### Particles (Photons)
These single photons

### Energy
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





