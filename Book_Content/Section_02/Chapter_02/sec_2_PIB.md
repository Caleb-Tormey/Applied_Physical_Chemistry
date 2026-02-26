## Particle in a Box

The model we use to play understand behavior and consequences of quantum systems and specifically Schrödinger's equation is the **Particle in a Box** (PIB). It is important to note that the PIB problem is a good starting place, however, there are aspects of it that are idealized. We will be able to apply it to some real systems but in order to have it match correctly will require work beyond the scope of this course. 

Here is the system. We will have a particle, we could use an electron, and we are going to confine it to live in a box. What does it mean to live in a box? What we are going to do is create a potential energy in which the boundaries of the box are infinite energy (not realistic but a good first approximation) and the inside of the box has no energy. So it is inside a square potential and therefore a particle. 

Ok so now we have an electron in a little energy well. Where does the quantum mechanics come in? Well do understand how the electron behaves we must use Schrödinger's equation.  

Our particle must behave according to the rules of the Schrödinger's equation as well as the boundary conditions that define our system. For our example, those rules are that the electron is **NOT** allowed to ever be outside the box. How do we say that mathematically? We will define our wavefunction, $\psi$, in such a way that it will be equal to zero when the position of the electron, defined by $x$ is not within the boundary of the box. 

So what about when the electron is in the box? When $0\ge x \le L$ we will use equation {ref}`TISE` and equation {ref}`1D_Hamiltonian` where, $V \left (x,t\right) = 0. If we write this out we get equation {ref}`1D_PIB_SE` 

:::{math}
:label: 1D_PIB_SE
-\frac{\hbar^2}{2m}\frac{d^2\psi \left(x\right)}{d x^2} = E\psi\left(x\right)
:::

We will not solve this problem explicit, however, you can find solutions to this equation in any physical chemistry text. Rather let's look for clues about what the solution should look like. Equation {ref}`1D_PIB_SE` is a second order differential equation. With differential equations rather than solving for a value like you have in the past you solve it for an entire function! So we want to determine what function of $x$, that we are calling $\psi$ will satisfy the equation. Well what does the equation say? It says that whatever function $\psi$ is we have to be able to take the second derivative of it with respect to $x$, multiply it by $-\frac{\hbar^2}{2m}$, and get a solution that looks like the original function, $\psi$ multiplied by an energy term. Well what kind of functions can you take second derivatives of and get back out something that resembles the original function? If we go back to section {ref}`math_derivatives` we will see that there are two possibilities. The first is an exponential. Recall that $\frac{d^2 e^{ax}}{dx^2} = a^2e^{ax}$. The other possibility would be $\sin x$ and $\cos x$. Recall that $\frac{d^2\sin x}{dx^2}= -\sin x$ and $\frac{d^2\cos x}{dx^2}= -\cos x$. So which solution makes the most sense? Let's look at other information in the problem. Recall, the boundary conditions earlier required that the wavefunction be zero at the wall of the box ($0$ and $L$). We cannot make the exponential function zero at any point, so that will be out. Both the $\sin$ and $\cos$ functions can be zero at certain points. Here is where our choice of coordinates matters. When $x = 0$ we know that $\psi(x) = 0$, so which of the two trig functions satisfies these criteria? The answer is $\sin$ as $\cos\left(0\right)= 1$. So we know that the function's general formula will look like $\sin\left(x\right)$ but we don't know any details. Here we require the other boundary condition. In this case that boundary condition is that the When $x = L$,that is also $\psi(x) = 0$. Here is where we will start to see where quantum mechanics solutions look different from the classical analog. If we want to solve for this problem we can set it up in equation {ref}`sin_L_sol`.

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