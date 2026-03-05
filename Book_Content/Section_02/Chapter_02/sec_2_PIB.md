## Particle in a Box

The model we use to understand the behavior and consequences of quantum systems, specifically the Schrödinger equation, is the **Particle in a Box** (PIB). It is important to note that the PIB problem is a good starting place; however, there are aspects of it that are idealized. We will be able to apply it to some real systems, but making it match perfectly often requires work beyond the scope of this course. 

[Image of a 1D Particle in a Box potential well with infinite walls]

Here is the system. We will have a particle, say an electron, and we are going to confine it to live in a 1D "box" of length $L$. What does it mean to live in a box? We are going to create a potential energy environment in which the boundaries of the box (the walls) have infinite potential energy (not completely realistic, but a good first approximation) and the inside of the box has absolutely zero potential energy. It is inside a square potential well. 

So now we have an electron in a little energy well. Where does the quantum mechanics come in? To understand how the electron behaves, we must use the Schrödinger equation.  

Our particle must behave according to the rules of the Schrödinger equation as well as the **boundary conditions** that define our system. For our example, those rules are that the electron is physically **NOT** allowed to ever be outside the box or in the walls. How do we say that mathematically? We define our wavefunction, $\psi$, in such a way that it will be exactly zero when the position of the electron, defined by $x$, is not strictly within the boundaries of the box. 

So what about when the electron *is* in the box? When $0 \le x \le L$, we will use equation {ref}`TISE` and equation {ref}`1D_Hamiltonian` where $V(x,t) = 0$. If we write this out, we get equation {ref}`1D_PIB_SE`:

:::{math}
:label: 1D_PIB_SE
-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2} = E\psi(x)
:::

We will not solve this differential equation completely from scratch—you can find the rigorous mathematical solutions to this equation in any advanced physical chemistry text. Rather, let's look for clues about what the solution should look like conceptually. 

Equation {ref}`1D_PIB_SE` is a second-order differential equation. With differential equations, rather than solving for a single numerical value like you have in algebra, you solve it for an entire function! We want to determine what function of $x$, which we are calling $\psi$, will satisfy the equation. 

What does the equation actually say? It says that whatever function $\psi$ is, we have to be able to take the second derivative of it with respect to $x$, multiply it by $-\frac{\hbar^2}{2m}$, and get a solution that looks exactly like the original function $\psi$ multiplied by an energy constant $E$. 

What kind of functions can you take the second derivative of and get back something that resembles the original function? If we go back to section {ref}`math_derivatives`, we will see that there are two main possibilities. The first is an exponential. Recall that $\frac{d^2}{dx^2}(e^{ax}) = a^2e^{ax}$. The other possibility would be the trigonometric functions $\sin(x)$ and $\cos(x)$. Recall that $\frac{d^2}{dx^2}\sin(x) = -\sin(x)$ and $\frac{d^2}{dx^2}\cos(x) = -\cos(x)$. 

So which solution makes the most sense physically? Let's look at the other information in the problem. Recall the boundary conditions earlier required that the wavefunction be exactly zero at the walls of the box ($x=0$ and $x=L$). We cannot make the standard exponential function reach zero at these specific finite points, so that is out. Both the sine and cosine functions, however, repeatedly cross zero. 

Here is where our choice of coordinates matters. At the left wall, $x = 0$, we know that $\psi(0) = 0$. Which of the two trig functions satisfies this criterion? The answer is sine, because $\sin(0) = 0$, whereas $\cos(0) = 1$. So we know that the function's general formula will look like a sine wave, but we don't yet know the specifics of its frequency or amplitude. Let's write out our general guess in equation {ref}`sin_L_sol`:

:::{math}
:label: sin_L_sol
\psi(x) = A\sin(kx)
:::

Here, $A$ is a constant representing the amplitude of the wave, and $k$ is a constant related to the wave's frequency. 

### Applying the Second Boundary Condition

To figure out what $k$ is, we must apply our second boundary condition. At the right wall, $x = L$, the wavefunction must also be zero, meaning $\psi(L) = 0$. 

If we plug $L$ into our general equation:
$A\sin(kL) = 0$

For this to be true, either $A = 0$ or $\sin(kL) = 0$. If $A = 0$, then the entire wavefunction is zero everywhere, which means the particle doesn't exist! Since we know we have an electron in the box, $A$ cannot be zero. Therefore, $\sin(kL)$ must be zero.

When does a sine function equal zero? When the inside of the function is an integer multiple of $\pi$ (i.e., $\pi$, $2\pi$, $3\pi$, etc.). We can write this mathematically as:

:::{math}
:label: k_quantization
kL = n\pi
:::

Where $n = 1, 2, 3, \dots$ (Notice $n$ cannot be 0, because then $k=0$, and again, the whole wavefunction would vanish). 

If we rearrange equation {ref}`k_quantization` to solve for $k$, we get $k = \frac{n\pi}{L}$. We can now plug this back into our general wavefunction to get the exact, mathematical description of our electron in the box:

:::{math}
:label: PIB_wavefunction
\psi_n(x) = A\sin\left(\frac{n\pi x}{L}\right)
:::

[Image of the first three wavefunctions and probability densities for a particle in a 1D box]

*Note: The constant $A$ is simply a normalization factor to ensure total probability equals 1. For a 1D box, it turns out to be $\sqrt{2/L}$, but we will focus primarily on the sine portion here.*

### Deriving the Energy 

Now for the grand finale. We have our wavefunction, $\psi_n(x)$. How much energy does this electron have? To find out, we simply plug our new wavefunction back into the original Schrödinger equation {ref}`1D_PIB_SE` and solve for $E$.

First, let's take the first derivative of $\psi_n(x)$ with respect to $x$:
$\frac{d\psi}{dx} = A \left(\frac{n\pi}{L}\right) \cos\left(\frac{n\pi x}{L}\right)$

Now, let's take the second derivative:
$\frac{d^2\psi}{dx^2} = -A \left(\frac{n\pi}{L}\right)^2 \sin\left(\frac{n\pi x}{L}\right)$

Notice that the chunk $A\sin\left(\frac{n\pi x}{L}\right)$ is just our original wavefunction, $\psi_n(x)$! So we can simplify the second derivative to:
$\frac{d^2\psi}{dx^2} = -\left(\frac{n^2\pi^2}{L^2}\right)\psi_n(x)$

Now, let's plug this second derivative back into the full Schrödinger equation {ref}`1D_PIB_SE`:
$-\frac{\hbar^2}{2m} \left[ -\left(\frac{n^2\pi^2}{L^2}\right)\psi_n(x) \right] = E\psi_n(x)$

The negative signs cancel out. Furthermore, because $\psi_n(x)$ is on both sides of the equation, we can divide it out completely! This leaves us with an exact equation for the energy, $E$:

:::{math}
:label: PIB_Energy_hbar
E_n = \frac{n^2 \pi^2 \hbar^2}{2 m L^2}
:::

Because physical chemists often prefer working with Planck's constant ($h$) instead of the reduced Planck's constant ($\hbar = \frac{h}{2\pi}$), we can substitute that in. Squaring $\hbar$ gives $\frac{h^2}{4\pi^2}$. The $\pi^2$ terms cancel out, leaving us with the final, famous equation for the energy of a particle in a 1D box:

:::{math}
:label: PIB_Energy_Final
E_n = \frac{n^2 h^2}{8 m L^2}
:::

You might be looking ahead and wondering if we are going to perform this exact same mathematical gymnastics for every single quantum model we encounter. The short answer is: no, we are not.

The Particle in a Box is the simplest possible quantum mechanical system. We walked through its complete derivation because it is an incredibly powerful exercise. It proves, without a shadow of a doubt, that **quantization is not a magic rule we just invented; it is a natural mathematical consequence of placing a wave inside a physical boundary.** As we move forward to more complex, realistic models—like the **Harmonic Oscillator** (which models vibrating molecular bonds), the **Rigid Rotor** (which models tumbling molecules), or the **Hydrogen Atom** (which gives us our actual 3D atomic orbitals)—the math becomes significantly more intense. Solving the Schrödinger equation for those systems requires advanced differential equations, Hermite polynomials, and spherical harmonics. 

While mathematically beautiful, slogging through that level of rigorous calculus is beyond the scope of this conceptual course. Our goal is not to get lost in the mathematical weeds, but to understand the physical chemistry. From here on out, we will skip most of the grueling derivations and focus directly on the *results* of the Schrödinger equation. We will typically look at the final energy equations, the physical shapes of the resulting wavefunctions, and most importantly, how we can apply those quantum results to understand real chemical and biochemical systems.
### The Consequences: Quantization is Born

Look closely at equation {ref}`PIB_Energy_Final`. The mass of the electron ($m$) is constant. The size of the box ($L$) is constant. Planck's constant ($h$) is constant. 

The *only* thing that can change the energy of the electron is $n$, which we defined earlier as an integer ($1, 2, 3, \dots$). 

Because $n$ can only be whole numbers, **the energy of the electron can only exist at specific, discrete levels.** It cannot have an energy of $1.5$ or $2.7$. This is the very definition of **quantization**. By simply enforcing a physical boundary condition (the walls of the box), the mathematics of the wave forced the energy to become quantized. 

Furthermore, notice what happens when $n=1$ (the lowest possible state). The energy is *not zero*. Because $n$ cannot be zero, an electron confined to a space must always possess some minimum amount of kinetic energy,

:::{math}
:label: sin_L_sol
\sin\left(ax\right) = 0
:::

Recall, from the section on {ref}`trigonometric_identities` that $\sin\left(\theta\right) = 0$ when $\theta = 0,\:\pi,\:2\pi,\:3\pi,\:4\pi\ldots$, but also that the zero should come when $n\pi x = L$ to enforce the second boundary condition. Therefore, there are many but **RESTRICTED** solutions. If we solve {ref}`sin_L_sol` and the zero solutions for $\sin$ we get that $\psi\left(x\right) = N \sin\left(\frac{n\pi x}{L} \right)$. N is something called the normilzation constant and it is something we will determine in the next section.
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
question_id="sec-02-ch-2-q03",
question_text="In the Particle in a Box model, the wavefunction must go to zero at the walls ($x=0$ and $x=L$). Why does this 'clamping' of the wavefunction at the boundaries lead directly to the quantization of energy?"
)
display(HTML(questions.render()))
:::
:::{include} interactive_code/pib_solution_graphic.md
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
question_id="sec-02-ch-2-q04",
question_text="Classically, a particle can sit perfectly still at the bottom of a box with zero kinetic energy. Why does the Heisenberg Uncertainty Principle forbid this in the quantum Particle in a Box?"
)
display(HTML(questions.render()))
:::