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

You are free to do none, some, or all of these problems as you see fit. They are designed to mimic the mathematical manipulations and physical reasoning you will encounter in the rest of the book.

### 1. Units and Conversions
*Perform the following unit conversions, paying close attention to compound units and powers.*
1.  **Simple:** $5.93 \times 10^3\:s^{-1}$ to $min^{-1}$
2.  **Intermediate:** $6.23\:m\:s^{-1}$ to $nm\:hr^{-1}$
3.  **Advanced:** $7.85 \times 10^{12}\:\mu m^3$ to $ft^3$ *(Hint: $(1\:\mu m)^3$ involves a different factor than $1\:\mu m$)*

### 2. Coordinate Systems and Distance
*Calculate the distance between the following pairs of points in space.*
1.  **1D Space:** $\text{A} = (-5.6)$ and $\text{B} = (-7.7)$
2.  **2D Space:** $\text{A} = (1.4, 2.0)$ and $\text{B} = (-2.5, 7.2)$
3.  **3D Space:** $\text{A} = (5.4, -8.1, -9.3)$ and $\text{B} = (12.0, 27.2, 0.4)$

### 3. Newton’s Laws and Basic Forces
*Apply $F=ma$ and basic force definitions.*
1.  **Simple:** What force is required to accelerate a mass of $12.345\:g$ by $35.7\:m\:s^{-2}$ in Newtons?
2.  **Intermediate:** A mass of $2.3\:g$ is raised to a height of $31.00\:m$. What is the maximum kinetic energy it can achieve if dropped?
3.  **Advanced (Electromagnetism):** What force is required to hold two electrons at a distance of $1.00\:\text{Å}$ from one another in Newtons?

### 4. Vectors and Magnitude
*Vectors are essential for describing molecular dipole moments and electric fields.*
1.  **Simple:** Determine the magnitude of a 2D displacement vector $\vec{r} = (12.0, -5.0)\:m$.
2.  **Intermediate:** A force vector $\vec{F}$ has components $F_x = 3.5\:N, F_y = -2.1\:N,$ and $F_z = 6.0\:N$. Calculate the total magnitude of the force.
3.  **Advanced:** A particle moves from position $\text{A} = (1, 2, 3)$ to $\text{B} = (4, 6, 15)$ in meters. Find the displacement vector $\vec{\Delta r}$ and its total length.

### 5. Vector Operations
*Practice adding and subtracting vectors.*
1.  **Simple:** Given $\vec{A} = (3, 4)$ and $\vec{B} = (1, -2)$, find $\vec{C} = \vec{A} + \vec{B}$.
2.  **Intermediate:** A molecule has two bond dipoles represented by vectors $\vec{\mu}_1 = (0, 1.5)$ and $\vec{\mu}_2 = (1.2, -0.5)$. Find the net dipole vector.
3.  **Advanced:** Subtract vector $\vec{V}_2 = (5, -2, 4)$ from $\vec{V}_1 = (2, 8, -1)$ and find the magnitude of the resulting vector.

### 6. Work and Mechanical Potential Energy
*Potential energy governs how atoms interact within a lattice or molecule.*
1.  **Simple:** A spring with a force constant $k = 150\:N\:m^{-1}$ is compressed by $0.05\:m$. How much potential energy is stored in the spring?
2.  **Intermediate:** How much work is required to stretch that same spring from its equilibrium position to a displacement of $0.20\:m$?
3.  **Advanced:** If a $0.50\:kg$ mass is attached to the spring in the previous problem and released from $0.20\:m$, what is its maximum velocity as it passes through the equilibrium point?

### 7. Angular Motion and Torque
*Rotational energy is a key component of the total energy in gas-phase molecules.*
1.  **Simple:** A point mass of $0.15\:kg$ is rotating at a radius of $0.50\:m$. What is its moment of inertia ($I$)?
2.  **Intermediate:** Calculate the torque produced if a force of $50\:N$ is applied perpendicularly to the end of a $0.25\:m$ long wrench.
3.  **Advanced:** A flywheel ($I = 2.5\:kg\:m^2$) is spinning at an angular velocity of $10\:rad\:s^{-1}$. What is its angular momentum ($L$)? If the radius of the mass distribution were doubled while maintaining the same speed, how would the angular momentum change?

### 8. Collisions and Conservation
*Collisions between molecules are how energy and momentum are exchanged in a chemical system.*
1.  **Simple (Linear Momentum):** A $2.0\:kg$ cart moving at $3.0\:m\:s^{-1}$ hits a stationary $1.0\:kg$ cart. If they stick together (perfectly inelastic), what is their final velocity?
2.  **Intermediate (Energy Loss):** In the collision above, calculate the total kinetic energy of the system before and after the crash. How much energy was "lost" to the environment?
3.  **Advanced (Elastic Exchange):** If the same two carts undergo a perfectly elastic collision (they bounce), and the $2.0\:kg$ cart slows to $1.0\:m\:s^{-1}$, use the conservation of momentum to find the final velocity of the $1.0\:kg$ cart.

### 9. Conceptual Conservation
*Conservation laws allow us to predict the outcomes of reactions without knowing every detail.*
1.  **Simple:** In a chemical reaction, $10.0\:g$ of Calcium Carbonate is heated in a sealed container to produce Calcium Oxide and Carbon Dioxide gas. According to the Law of Conservation of Mass, what must be the total mass of the products?
2.  **Advanced:** An electron and a positron (same mass, opposite charge) collide and annihilate, turning their mass entirely into light energy ($E=mc^2$). Identify at least three properties (Mass-Energy, Charge, Momentum, etc.) that must be conserved in this event.