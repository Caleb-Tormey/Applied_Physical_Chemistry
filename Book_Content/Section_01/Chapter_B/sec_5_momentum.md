(linear_angular_momentum)=
## Momentum

Momentum is a measure of an object's "quantity of motion." It depends on both how much stuff is moving and how fast it is moving. In physics, we distinguish between motion in a straight line and motion around a pivot.

### Linear Momentum
We defined linear momentum ($p$) in equation {ref}`linear_momentum` as the product of mass and velocity. It is a vector quantity, meaning the direction of travel is as important as the speed.

:::{math}
:label: linear_momentum
p = mv
:::



One of the most powerful principles in physics is the **Law of Conservation of Momentum**: in an isolated system (where no external forces act), the total momentum before an interaction is equal to the total momentum after.

### Angular Momentum
When objects rotate, we use angular momentum ($L$). Just as linear momentum is the product of mass and velocity, angular momentum is the product of the "rotational mass" (Moment of Inertia) and the rotational velocity ($\omega$).

#### Moment of Inertia
The moment of inertia $I$ plainly speaking is how difficult it is to start spinning something or how hard it is to stop it. As shown in equation {ref}`moment_of_inertia`, a small object with little mass is easy to stop, whereas a large object with a big radius is more difficult because the mass is distributed further from the axis of rotation.

:::{math}
:label: moment_of_inertia
I = mr^2
:::
:::{code-cell} python
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
    question_id="sec-01-ch-B-q08",
    question_text="Does changing the mass of a spinning object or changing its radius have a greater impact on its resistance to changes in motion (Moment of Inertia)? Explain your reasoning based on the definition of $I$."
)
display(HTML(questions.render()))
:::


### Torque
Just as we need to apply a force to change linear momentum, we must apply a **Torque** ($\tau$) to change angular momentum. Torque is the rotational equivalent of force, often thought of as a "twisting" force. It depends not just on how much force you apply, but where you apply it (the lever arm $r$).

:::{math}
:label: torque_def
\tau = r \times F
:::
:::{code-cell} python
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
    question_id="sec-01-ch-B-q09",
    question_text="Imagine you are trying to open a very heavy revolving door. Why is it easier to push on the edge furthest from the hinge rather than close to the center? Relate this to the concept of torque."
)
display(HTML(questions.render()))
:::
---

## Collisions: Energy vs. Momentum
In any collision, **momentum is always conserved**. However, **kinetic energy** is not always conserved. We generally categorize collisions into two types:

1. **Elastic Collisions:** Both momentum and kinetic energy are conserved. The objects "bounce" perfectly.
2. **Inelastic Collisions:** Momentum is conserved, but some kinetic energy is converted into heat, sound, or deformation (internal energy). If the objects stick together, it is "perfectly inelastic."

This is the bridge between simple systems and complex ones: in an inelastic collision, the "missing" energy has simply moved from the macroscopic motion of the blocks to the microscopic motion of the molecules (heat).

:::{include} interactive_code/momentum_collisions_elastic_vs_inelastic.md
:::
:::{code-cell} python
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
    question_id="sec-01-ch-B-q10",
    question_text="In a perfectly inelastic collision, two objects stick together and kinetic energy is lost, yet momentum is conserved. What is happening physically at the molecular level to absorb that kinetic energy?"
)
display(HTML(questions.render()))
:::
### Looking Ahead: Material Properties and Elasticity
The distinction between an elastic "bounce" and an inelastic "thud" might seem like a simple physics puzzle, but these questions are of central importance to chemists and materials scientists. 

Why does a rubber ball bounce while a clump of clay sticks? The answer lies in the microscopic internal structure of the material. In future sections, we will discuss how these basic mechanical ideas expand into **Material Properties**. We will explore how molecular bonds act like tiny springs and how the efficiency of energy transfer within those bonds determines if a material is brittle, elastic, or plastic. Understanding how energy is "stored" or "lost" at the atomic level is the key to designing everything from high-impact sports gear to heat-resistant aerospace alloys.
:::{code-cell} python
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
    question_id="sec-01-ch-B-q11",
    question_text="Based on the <b>Looking Ahead </b> section, if a material is described as highly elastic, what does that tell you about how its internal molecular springs handle energy during a collision compared to a material that is brittle?"
)
display(HTML(questions.render()))
:::