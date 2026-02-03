## Energy

We define energy as what is required to do work. Well now we need to know what work is. Work is applying a force over a distance. The most obvious example would be lifting an object. If you have an object on the ground and lift it, you are performing work against the force of gravity, transferring energy into the object's position.

### Kinetic
This is the energy of motion. The most basic definition is

:::{math}
:label: kinetic_energy
KE = \frac{1}{2}mv^2
:::

It can also be defined by the momentum ($p = m v$) in equation {ref}`kinetic_energy_momentum`
:::{math}
:label: kinetic_energy_momentum
KE = \frac{p^2}{2m}
:::

### Potential
Potential energy is "stored" energy based on the configuration or position of a system. 

#### Mechanical Potential: The Spring
A classic example of potential energy is a displaced spring. According to Hooke's Law, the force required to compress or stretch a spring is proportional to the displacement $x$. As you pull the spring, you do work that is stored as potential energy:

:::{math}
:label: spring_pot
PE_{spring} = \frac{1}{2}kx^2
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
    question_id="sec-01-ch-B-q06",
    question_text="When you compress a spring, you are doing work. Where is that energy hiding before the spring is released, and what determines how much energy can be stored?"
)
display(HTML(questions.render()))
:::
#### Electromagnetism
This topic is incredibly deep. We will however, just take a brief look at properties of electric charges and magnetic fields. The first is that like charges repel, and unalike charges attract. We can actually see this if we look at the governing potential energy equation known as Coulomb's law shown in equation {ref}`coulomb_pot`.

:::{math}
:label: coulomb_pot
V\left(r\right) = \frac{q_1q_2}{4\pi\epsilon_0 r}
:::

:::{math}
:label: coulomb_force
F\left(r\right) = \frac{q_1q_2}{4\pi\epsilon_0 r^2}
:::

---

### Energy Transformation and Conservation
In an **ideal system**, energy is never lost; it only changes form. This is the Law of Conservation of Energy. If we look at a mass oscillating on a spring, we see a constant "trade" between the definitions we established in the [Kinetic](#kinetic) and [Mechanical Potential](#mechanical-potential-the-spring) sections.

* **At maximum displacement ($x = A$):** The spring is fully stretched. Velocity is zero ($KE = 0$), so the total energy is $100\%$ Potential Energy ($PE$).
* **At equilibrium ($x = 0$):** The spring is relaxed. The displacement is zero ($PE = 0$), so the total energy is now $100\%$ Kinetic Energy ($KE$).
In an ideal vacuum, the sum $E_{total} = KE + PE$ remains perfectly constant as the system cycles back and forth.
:::{include} interactive_code/KE_PE_cycle.md
:::

---
### From Simple to Complex: The Reality of Dissipation
While the ideal spring model is useful, it fails to describe the world we touch. Real systems are subject to **non-conservative forces** like friction and air resistance. 



#### The Energy "Tax"
When a real spring moves, it eventually stops. The energy hasn't disappeared—that would violate the Law of Conservation of Energy. Instead, it has been **dissipated**. The organized mechanical energy of the moving mass is transferred into the disorganized motion of atoms in the surrounding air and the spring itself. We perceive this "lost" energy as a slight increase in temperature.

* **Simple Mechanical Systems:** We track a few variables (velocity, position) of a single "large" object.
* **Complex Systems:** We deal with $10^{23}$ molecules. Because we cannot track the $KE$ and $PE$ of every single atom, we must shift our perspective from classical mechanics to **Thermodynamics**.



To handle these complex systems, we develop statistical tools. Instead of tracking a single "force," we track **Internal Energy ($U$)**, **Heat ($Q$)**, and **Entropy ($S$)**. This allows us to describe the behavior of billions of particles without needing to solve an impossible number of equations.
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
    question_id="sec-01-ch-B-q07",
    question_text="When a real-world pendulum eventually stops swinging, we say energy was dissipated. Since energy cannot be destroyed, describe the physical transition of that energy from the simple mechanical system to the complex molecular system."
)
display(HTML(questions.render()))
:::