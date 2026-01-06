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
  enumerator: 2.%s
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
# Chapter 2: Foundations of Quantum Mechanics

## Wave Behavior

### de Broglie equation

:::{math}
:label: deBroglie_eq

\lambda = \frac{h}{p} = \frac{h}{mv}
:::

### Diffraction and Interference

### Double Slit Experiment

## Heisenberg's Uncertainty Principles

### Connecting Waves and Particles

## Schrödinger's Equation 
When we reviewed Newton's laws one thing that wasn't mentioned was that his formulation of the definition of force is something, that while well reasoned, is not derived but rather proposed and then all other classical laws are derived from that starting point. In fact, other laws had proposed that the force was rather proportional to the velocity rather than acceleration. We of course have found that momentum is true for this case. Schrödinger proposed his equation in much the same matter. There are two forms of Schrödinger equation we will discuss but only one that we will use in any meaningful sense. The first is called the **Time Dependent Schrödinger Equation** that we will refer to from now on as TDSE and can be seen in equation {ref}`TDSE`. The second and more useful form of this equation that we will use is called the **Time Independent Schrödinger Equation** that will be referred to as TISE and can be seen in equation {ref}`TISE`. 

:::{math}
:label: TDSE

i\frac{\partial}{\partial t}\Psi\left(x,t\right) = \hat{H}\Psi\left(x,t\right)
:::

$\hat{H}$ is known as the Hamiltonian operator. We will talk about operators later but suffice to say it is something that tells us about the energy of our system. The Hamiltonian is divided into two parts, the kinetic energy, $-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}$, and the potential energy $V\left(x,t\right)$. Together they combine to become the Hamiltonian, $\hat{H}$, defined in one-dimension in equation {ref}`1D_Hamiltonian`. $\Psi \left(x,t\right) and $\Psi \left(x\right)$ are what is known as the **wavefunction**. The wavefunction is a very important part as it encapsulates all possible information about a quantum system. The wavefunction is also a purely mathematical object. What that means is that the wavefunction itself is not directly observable or experimentally measured. We will discuss how the wavefunction is physically relevant and measurable in section {ref}`operators_and_expectation_values`.

:::{math}
:label: 1D_Hamiltonian
-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V\left(x,t\right)
:::
:::{math}
:label: TISE
\hat{H}\Psi\left(x\right) = E\Psi\left(x\right)
:::

We will almost exclusively be looking at TISE because the systems we are going to be looking at are stable over reasonably long time frames. There are places where the TDSE is important becuase the system changes with time. For example, looking at things like photon absorption probabilities, processes like fluoresce and some kinetics questions about things like bond formation all require seeing how the wave function changes with time. 
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




## Probability Density

Earlier in the chapter we discussed that the wavefunction has no physical meaning. That seems odd and frankly kind of stupid considering we are looking at the physical behavior of an electron stuck in a box. So how does one use the wavefunction? First we must realize that now that the electron is being represented by a wavefunctionn it will no longer behave like the little particle we put in the box. We should be comfortable with this considering that we know we can determine the wavelength for a free electron by the de Broglie equation {ref}`debroglie_eq`. However, now we start to lose sense of some simple notions about our electron. For starters, where can we find the electron within the box? Since it has a wavelength and is behaving like a wave in some ways the question is silly. A Wave is not in a single spot. Rather there are places where there is a great deal of wave (at the crests and troughs) and places where there is very little wave (at the nodes).

:::{code-cell} python
:label: PIB_prob_density 
:tags: [remove-input]
import numpy as np
import matplotlib.pyplot as plt

def plot_particle_in_box_dual_axis():
    """
    Calculates and plots the wavefunction and probability density for a
    particle in a 1-D box for n=3, using two separate y-axes for clarity.

    The left y-axis shows the wavefunction amplitude, and the right y-axis
    shows the probability density. Axis labels are color-coded to match
    their respective plots.

    This script uses atomic units where h-bar = 1, m_e = 1, and length
    is in Bohr radii (a_0).
    
    Returns:
        matplotlib.figure.Figure: The figure object containing the plot.
    """

    # --- Parameters (in atomic units) ---
    L = 10.0  # Box length in Bohr radii (a_0)
    n = 3     # Principal quantum number
    # Mass of the electron (m_e) is 1 in atomic units.
    # Planck's constant (hbar) is 1 in atomic units.

    # --- Setup the spatial grid ---
    x = np.linspace(0, L, 1000)

    # --- Calculations ---
    normalization_constant = np.sqrt(2 / L)
    psi = normalization_constant * np.sin(n * np.pi * x / L)
    psi_squared = psi**2

    # --- Plotting Setup ---
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Create a second y-axis that shares the same x-axis
    ax2 = ax1.twinx()

    # --- Plot Wavefunction on the left axis (ax1) ---
    color1 = 'cornflowerblue'
    line1 = ax1.plot(x, psi, color=color1, label=r'$\psi_3(x)$ (Wavefunction)')[0]
    ax1.set_xlabel('Position, x (Bohr radii, $a_0$)', fontsize=12)
    ax1.set_ylabel('Wavefunction Amplitude', color=color1, fontsize=12)
    ax1.tick_params(axis='y', labelcolor=color1)
    # Add a horizontal line at y=0 for reference
    ax1.axhline(0, color='gray', linestyle='--', linewidth=1)


    # --- Plot Probability Density on the right axis (ax2) ---
    color2 = 'orangered'
    line2 = ax2.plot(x, psi_squared, color=color2, label=r'$|\psi_3(x)|^2$ (Probability Density)')[0]
    ax2.set_ylabel('Probability Density', color=color2, fontsize=12)
    ax2.tick_params(axis='y', labelcolor=color2)

    # --- Final Touches ---
    fig.suptitle(f'Particle in a 1-D Box (n={n})', fontsize=16, fontweight='bold')
    
    # Set plot limits to the box boundaries
    ax1.set_xlim(0, L)

    # Create a unified legend for both lines
    lines = [line1, line2]
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper right')

    # Ensure the layout is tight to prevent labels from overlapping
    fig.tight_layout()
    # Adjust title position after tight_layout
    plt.subplots_adjust(top=0.92)


    # --- Return the figure object for Jupyter Book to display ---
    #return fig

# Call the function as the final line of the cell.
# Jupyter Book will capture the returned figure object and display it.
plot_particle_in_box_dual_axis()
:::
We will look at the electron sort of ``spread'' through the whole box. For reasons beyond this course, we are going to look at the square of the magnitude of the wavefunction defined as $\left|\psi\right|^2$. This gives us a distribution of where there is sort of more electron and where there is sort of less electron. Another way we can look at this is as a probability of finding the electron. If we were to look for the electron many times is that it would not always be in the same place but after a while we would find some places it was found more often than others and still other places, specifically the nodes, where we don't find it at all. 

An important aspect of the probability distribution is it must be normalized. What does that mean? It means that the probability of finding the particle anywhere must be $100\%$ (wouldn't make much sense otherwise.) So how do we ensure that this is true? We calculate a normalization factor, basically a number, that will ensure when we find the probability density by squaring the wavefunction, the entire probability will be 1. 

Ok we said that with words how do we say that with mathematics? Well first let's look at our current wavefunction.

:::{math}
\psi\left(x\right) = N \sin\left(\frac{n\pi x}{L} \right)
:::
We will now take the square of the magnitude of $\psi$,

:::{math}
\begin{align}
\left|\psi\left(x\right)\right|^2 = N \sin\left(\frac{n\pi x}{L} \right) N \sin\left(\frac{n\pi x}{L} \right)\\
\left|\psi\left(x\right)\right|^2 = N^2 \sin^2\left(\frac{n\pi x}{L} \right)
\end{align}
:::

So how do we calculate $N$ and make sure the probability is normalized? We stated above we want to make sure that the electron has to be somewhere all the time. That means the entire probability of being anywhere must add up to $100\%$. Ok then how do we do this mathematically? It is easy if you have discrete states. For example, on a fair dice each side has a probability of $\frac{1}{6}$ and their are $6$ sides so if you add them all up you get a total probability that some number will be rolled of $1$. How do we do this with the wave? What we do is imagine a very small section of the probability. We will call this very small section of the probability density that is $dx$ wide. And then we will ``add'' yup all these little sections. The mathematical tool we will use is called an integral. 

:::{math}
:enumerated: false
\begin{align}
\int_{0}^{L}N^2 \sin^2\left(\frac{n\pi x}{L} \right) dx = 1\\
\left.\vphantom{\int}N^2\left(\frac{1}{2}x - \frac{L\sin{\frac{2 n \pi x}{L}}}{2 n \pi} \right)\right|_0^L = 1\\
N^2\left(\frac{1}{2}L - \frac{L\sin{\frac{2n\pi L}{L}}}{2n\pi}\right)-N^2\left(\cancel{\frac{1}{2}0} - \cancel{\frac{L\sin{\frac{2n\pi 0}{L}}}{2n\pi}}\right)^2=1\\
N^2\left(\frac{1}{2}L - \frac{L\cancel{\sin{\frac{2n\pi L}{L}}}}{2n\pi}\right) = 1 \\
N^2\frac{1}{2}L = 1\\
N = \sqrt{\frac{2}{L}}
\end{align}
:::
(operators_and_expectation_values)=
## Operators and Expectation Values


## Quantum Harmonic Oscillator

If you imagine a spring with a mass on it, we can compress the spring and then let it go. The mass will move back and forth in a harmonic motion. If there are no other forces acting on the system (like friction) it will continue forever. 

Recall, that we can determine the force of the system based on the potential by the equation $V\left(r\right) = -\frac{d V\left(r\right)}{dr}$. In this case we will look at the potential as being defined **Hooke's law** where it follows a quadratic form in equation {ref}`Hooke_pot` and the restoring force, $F$, is defined by equation {ref}`Hooke_law`.

:::{math}
:label: Hooke_pot
V\left(x\right) = \frac{1}{2}kx^2
:::

:::{math}
:label: Hooke_law
F = -kx
:::

Continuing to think about our system we imagine the harmonic motion proceeding at some rate. We define the angular frequency, $\omega$, for the system to be how many radians it goes per second
$k$ is the spring constant which determines how stiff the spring is and $m$ is the mass.

:::{math}
:label: angular_freq
\omega = \sqrt{\frac{k}{m}}
:::

:::{math}
:label: HO_freq
\nu = \frac{1}{2\pi}\omega=\frac{1}{2\pi}\sqrt{\frac{k}{m}}
:::
 For something like a diatomic system we can simplify the system by thinking about the single motion having contributions of the two masses. Let's look at the two limits. When the two masses are identical we would think of each mass contributing exactly half the motion. When one is **MUCH** larger than the other we would think that all the motion is due only to the smaller mass since the larger mass will not move very much. Again, how do we say this mathematically? We use the reduced mass $\mu$. It is defined in equation {ref}`reduced_mass`.

 :::{math}
 :label: reduced_mass
 \mu=\frac{m_1m_2}{m_1+m_2}
 :::

### Wavefunction for Quantum Harmonic Oscillator

Looking at the classical turning points of the classical harmonic oscillator we notice that the wavefunction extends beyond the potential very slightly. {diagram of quadratic potential and HO wavefunctions}. The non-zero wavefunction outside the potential results in a  non-zero probability that the particle could exist 

### Quantum Harmonic Oscillator Energy States
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
    question_id="sec-2-ch-2-q02",
    question_text="Given the possible quantum numbers is it possible to have zero vibrational energy in a quantum HO? Please justify and explain your answer. "
)
display(HTML(questions.render()))
#**Conceptual Question:** Given your answer to the previous
:::
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
    question_id="sec-2-ch-2-q03",
    question_text="Let's consider running a mental experiment. What if we  "
)
display(HTML(questions.render()))
#**Conceptual Question:** Let's consider running a mental experiment. What if we 
:::
### Spectroscopy Applications

Further and more detailed discussion of infra-red spectroscopy will be saved for {ref}`IR_Raman`
(rigid_rotator)=
## Rigid Rotator

The rigorous rigid rotator will be used to model the hydrogen atom and so further discussion of the wavefunction solutions to this system will be discussed in section {ref}`hydrogen_atom` rather we are just going to use a simplified model called the ``particle-on-a-ring'' to look at quantized rotational motion. 

Before we look at the quantum analog let's start by just looking at classical angular momentum. Recall we defined some basic principles of angular motion in the physics review chapter on {ref}`linear_angular_momentum` . If we have a particle with mass $m$ and it is constrained to move on a circular ring of radius $r$ the magnitude of its angular momentum in the axis perpendicular to the ring (that we will call the $z$ axis) is defined in equation {ref}`J_z`, where p is the instantaneous linear momentum of the particle confined to the ring and is defined as $p = mv$. 

:::{math}
:label: J_z
J_z = pr
:::
The total energy of our system is due completely to the motion of the particle and so is kinetic in origin. We can express the energy of the system by relating the kinetic energy (equation {ref}`kinetic_energy`) to the angular momentum by using instantaneous linear momentum $p$ (equation {ref}`linear_momentum`) in equation {ref}`J_z`.

:::{math}
:enumerated:false
\begin{align}
E = \frac{1}{2}mv^2 = \frac{p^2}{2m}=\frac{\left(\frac{J_z}{r}\right)^2}{2m} = \frac{J_z^2}{2mr^2}
\end{align}
:::

We might notice that the bottom of the equation derived above looks like the moment of inertia defined in equation ({ref}`moment_of_inertia`). By including this defintion we find that the enrgy of our particle on a loop is defined in equation {ref}`classical_energy_rotation`

:::{math}
:label: classical_energy_rotation
E = \frac{J_z^2}{2I}
:::

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
# --- END: Required for every block --- import QuestionBlock
from IPython.display import display, HTML

# This block is now very clean!
questions = QuestionBlock()
questions.add_question(
    question_id="sec-2-ch-2-q04",
    question_text="Does it make sense that the energy of the rotating system is inversely proportional to the moment of inertia? Explain why it is or isn't."
)
display(HTML(questions.render()))
#**Conceptual Question:** Does it make sense that the energy of the rotating system is inversely proportional to the moment of inertia? Explain why it is or isn't. 
:::

Up to this point we have just been defining a classical system. So where does the quantum part come in? Well we know that particles can behave like waves so how could we define the wavelike character of our particle moving in a circle? We know from the de Broglie equation ({ref}`debroglie_eq`) that the wavelength is inversely proportional to the linear momentum ($p = \frac{h}{\lambda}$). We also know that the magnitude of the angluar momentum along the $z$ axis is proportional to the instantaneous linear momentum. Combining these two concepts we can derive an expression for $J_z$ in terms of the wavelength $\lambda$.

:::{math}
\begin{align}
J_z = p r = \frac{h r}{\lambda}
\end{align}
:::
One condition for the particle's wavefunction to be physically realistic is that as it goes around in a circular path it must meet back up with itself exactly. Mathematically that is stated as it must be continuous and single-valued. If this condition is not satisfied, the resulting wave would destructively interfere and cancel itself out.

This requirement imposes a critical boundary condition that wavelength must be an integer multiple, that we will call $m_l$, of the circumference of the ring (2πr)

:::{math}
:enumerated: false
\begin{align}
m_l\lambda = 2 \pi r\\
\lambda = \frac{2\pi r}{m_l}\\
 m_l= 0,\pm 1,\pm 2,\pm3,\ldots\\
\end{align}
:::

If you notice we are not restricted to only positive integer values. The next conceptual question will have you reason why this is the case. 

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
    question_id="sec-2-ch-2-q05",
    question_text="Does it make sense that the energy of the rotating system is inversely proportional to the moment of inertia? Explain why it is or isn't."
)
display(HTML(questions.render()))
#**Conceptual Question:** Consider your quantum particle moving around on your ring. What property of the rotating system is described by the need for positive and negative values of the same magnitude?
:::

We can then substitute our now necessarily quantized wavelength definition back into our expression for the angular momentum $J_z$ to derive the following equation

:::{math}
:enumerated:false
J_z = \frac{h r}{\lambda} = \frac{h r}{{2\pi r}{m_l}} = m_l\frac{h}{2\pi} = m_l\hbar
:::

And so we see that our values for angular momentum of our quantum particle traveling on a ring are restricted to values defined in equation {ref}`quantum_J_z`. $\hbar=\frac{h}{2\pi}$ is pronounced h-bar and is also known as reduced Planck's constant.
:::{math}
:label: quantum_J_z
J_z = m_l\hbar
:::
We can then determine the quantized energy states by using equation {ref}`quantum_J_z` and equation {ref}`classical_energy_rotation` to find
:::{math}
:label: quantum_energy_angular
E_{m_l}=\frac{m_l^2\hbar^2}{2I}
:::
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
    question_id="sec-2-ch-2-q06",
    question_text="If I were to double the quantum number of a rotating system how would that change the energy? How does that compare with doubling the quantum number of the quantum harmonic oscillator?"
)
display(HTML(questions.render()))
#**Conceptual Question:** If I were to double the quantum number of a rotating system how would that change the energy? How does that compare with doubling the quantum number of the quantum harmonic oscillator?
:::
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
    question_id="sec-2-ch-2-q07",
    question_text="Is it possible to have zero rotational energy for a quantum particle? Again, how does that compare with the quantum harmonic oscillator?"
)
display(HTML(questions.render()))

#**Conceptual Question:** Is it possible to have zero rotational energy for a quantum particle? Again, how does that compare with the quantum harmonic oscillator?
::: 
### Rigid Rotator Energy States

### Spectroscopy Applications

### Rotational Vibrational Coupling

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
    question_id="sec-2-ch-2-q08",
    question_text="If you look closely you will notice that the rotational gaps are not exactly the same as is predicted by basic theory. What could be a possible reason?"
)
display(HTML(questions.render()))
#**Conceptual idea:** If you look closely you will notice that the rotational gaps are not exactly the same as is predicted by basic theory. What could be a possible reason. 
:::

:::{code-cell} python
:tags: ["remove-input"]

from _ext.interactive_qa import QAManager
from IPython.display import display, HTML

# This renders the final control panel.
# Pass the desired title for the printed page here.
manager = QAManager(page_title="Chapter 2: Foundations of Quantum Mechanics")
display(HTML(manager.render()))
:::
%:::{code-cell} python
%:tags: ["remove-input", "remove-output"]

%import sys
%import os

%# This block MUST be at the top of your file.
%# It finds the project root and adds it to the Python path.
%# Adjust the number of ".." to match how many folders deep your file is.
%try:
%    cwd = os.getcwd()
%    # e.g., use ("..", "..") for a file 2 levels deep.
%    project_root = os.path.abspath(os.path.join(cwd, "..", "..", ".."))
%    if project_root not in sys.path:
%        sys.path.insert(0, project_root)
%except Exception as e:
%    print(f"Error setting project path: {e}")
%:::
## Practice Problems

You are free to do none, some or all these problems as you see fit. They would be very helpful to use in studying for the chapter exams.