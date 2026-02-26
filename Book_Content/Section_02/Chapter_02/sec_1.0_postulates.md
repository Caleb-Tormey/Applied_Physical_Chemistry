## Postulates of Quantum Mechanics

In classical mechanics, defining a "system" is intuitive. If you want to describe a ball flying through the air, you list its **mass ($m$)**, its **position ($x$)**, and its **velocity ($v$)**. With those variables and Newton’s Second Law ($F=ma$), you can predict exactly where that ball will be at any moment in the future.

In the subatomic world, this approach breaks down. We can no longer point to a specific "coordinate" for an electron with 100% certainty. Instead, we swap classical variables for **Postulates**—fundamental axioms that define the "rules of the quantum game."

---

### 1. The State of the System (The Wavefunction)
In Classical Mechanics, the "state" is a list of physical properties. In Quantum Mechanics, the state of the system is entirely contained within the **wavefunction**, $\psi(x, t)$.

* **The Concept:** Everything that *can* be known about a particle—its energy, its position, its momentum—is "baked into" the math of $\psi$. 
* **The Reality Check:** $\psi$ is often a **complex function** (containing $i = \sqrt{-1}$), meaning it isn't a directly measurable "physical" wave like a string vibrating.
* **Probability Density:** To connect back to reality, we look at the square of the magnitude, $|\psi|^2$. According to the **Born Interpretation**, this represents the **probability density** of finding the particle at a specific point.
#### Important Wavefunction Properties: 

In quantum mechanics, not just any mathematical function can serve as a valid wavefunction. Because $\psi$ must represent a physical reality, it must satisfy a set of criteria often referred to as being "well-behaved." If a function fails any of these tests, the postulates we discussed earlier (like calculating expectation values or solving the Schrödinger Equation) simply won't work.

For a wavefunction to be physically acceptable, it must meet the following four criteria:

1. **Finite** The wavefunction must not "blow up" to infinity at any point. If $\psi$ were infinite at a certain location, the probability of finding the particle there ($|\psi|^2$) would also be infinite, which is physically impossible.
2. **Single-Valued** At any specific point in space, there can only be one value for $\psi$. If a function had two different values for the same $x$-coordinate, it would imply the particle has two different probability densities at the exact same spot simultaneously.
3. **Continuous** There should be no "breaks" or "jumps" in the function. Mathematically, this means $\psi(x)$ must be continuous. Physically, a jump would imply an instantaneous change in probability, which violates the wave-like nature of the particle.
4. **Continuous First Derivative (Smooth)** Not only must the function be connected (continuous), but it must also be "smooth"—meaning its slope ($\frac{d\psi}{dx}$) must also be continuous.
- The "Kink" Problem: If there is a sharp "kink" or "corner" in the wavefunction, the second derivative (which is required to calculate Kinetic Energy in the Schrödinger Equation) becomes undefined at that point.
- The Exception: The only time a wavefunction is allowed to have a "kink" is at a point where the potential energy ($V$) is infinite (like the walls of our Particle in a Box).

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
question_id="sec-02-ch-2-q01",
question_text="The wavefunction $\psi$ is often a complex-valued function (containing $i$). Why is it physically necessary to use the product $\psi^*\psi$ to describe probability density, and what property must the resulting integral over all space satisfy?"
)
display(HTML(questions.render()))
:::

---

### 2. The Correspondence Principle (Operators)
In the macroscopic world, if you want to know the momentum ($p$), you just measure it. In QM, physical variables are replaced by **mathematical operators**.

* **The Concept:** Think of an operator ($\hat{A}$) as a mathematical "instruction" (like a derivative or a multiplier) that acts on the wavefunction to extract information.
* **The Translation:** Every classical observable has a quantum counterpart. For example, the classical kinetic energy $T = \frac{p^2}{2m}$ is replaced by a specific Kinetic Energy Operator that involves a second derivative.

---

### 3. Observables and Eigenvalues
In the "large" world, a car can drive at any speed—20 mph, 20.1 mph, or 20.0001 mph. Values are continuous. In the quantum world, when we apply an operator to a wavefunction, the only results we can actually measure are the **eigenvalues** ($a$).

$$\hat{A}\psi = a\psi$$

* **The Concept:** This equation explains **quantization**. The math only allows for specific, discrete solutions. This is why an electron in an atom exists in specific energy levels rather than a continuous smear.
* **The "Real" Factor:** We use **Hermitian operators** because they are mathematically guaranteed to yield **real-numbered eigenvalues**. Even if our wavefunction is complex, the energy or momentum we measure in the lab must be a real number; you'll never measure an "imaginary" amount of Joules.

---

### 4. Expectation Values (The "Sandwich" Integral)
Since QM is built on probability, we can't always predict a single result for one measurement. Instead, we calculate the **Expectation Value** $\langle a \rangle$, which is the statistical average of many measurements.

$$\langle a \rangle = \int \psi^* \hat{A} \psi \, dx$$

* **The "Sandwich":** We place the operator between the wavefunction and its complex conjugate ($\psi^*$). 
* **Normalization:** For this average to make sense, the total probability of finding the particle *somewhere* in the universe must be exactly **1 (100%)**. We **normalize** our wavefunctions to ensure our "probability budget" is mathematically sound.

---

### 5. Time Evolution (The TDSE)
The most famous equation in classical mechanics is $F=ma$, which tells us how a system changes over time. In Quantum Mechanics, that role is filled by the **Time-Dependent Schrödinger Equation (TDSE)**:

$$\hat{H}\psi = i\hbar \frac{\partial \psi}{\partial t}$$

* **The Concept:** If you have the wavefunction ($\psi$) and you know the total energy operator (the **Hamiltonian**, $\hat{H}$), the TDSE tells you exactly how that wavefunction will evolve. 
* **Our Focus:** While the TDSE handles the "motion," we will spend most of this course on the **Time-Independent** version to find "stationary states"—the specific energy levels of atoms and molecules that define their chemical identity. We will discuss the time independent version in the next section. 