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

## Terminology, Definitions and Units

### Powers of Ten

We will be using scientific notation, however, it is often better to use powers of ten to make the numbers more reasonable. To that end there are prefixes that we can use to account for this. They typically come in bundles of 3 powers of 10 (so $1000$ or $0.001$)

:::{csv-table} Powers of Ten Prefixes
:header: "Prefix", "Exponent", "Number","Scientific Notation", "Name"
:label: tbl_prefix

"Giga (G)", "9", "1,000,000,000",$10^9$,"billion"
"Mega (M)", "6", "1,000,000",$10^6$,"million"
"kilo (k)", "3", "1,000",$10^3$,"thousand"
"hecto (h)", "2", "100",$10^2$,"hundred"
"deca (da)", "1", "10",$10$,"ten"
"deci (d)", "-1", "0.1",$10^{-1}$,"tenth"
"centi (c)", "-2", "0.01",$10^{-2}$,"hundreth"
"milli (m)", "-3", "0.001",$10^{-3}$,"thousandth"
"micro ($\mu$)", "-6", "0.000001",$10^{-6}$,"millionth"
"nano (n)", "-9", "0.00000001",$10^{-9}$,"billionth"

:::

### Basie SI Units

In order to do science in an organized and more easily reproducible way, we need to have standards upon which to compare results or to set up experiments. To that end standardized units are vital to physical science. While there are many systems of units, we will primarily be using SI units (short for Internation System of Units well technically it is short for the French Système International d'unités). Here are the units we will be primarily using. 


:::{csv-table} Base SI Units
:header: "Quantity", "Name", "Abbreviation"
:label: tbl_base_units

"Length", "Meter", "m"
"Mass", "Kilogram", "kg"
"Time", "Second", "s"
"Electric Current", "Ampere", "A"
"Thermodynamic Temperature", "Kelvin", "K"
"Amount of Substance", "Mole", "mol"
"Luminous Intensity", "Candela", "cd"
:::

### Derived Units

We cannot just use the base units as the world has more complicated characteristics. We can therefore combine base units to create derived units. For example, we use meter, m, as the unit of length. If we would like to describe an area we would multiply the length ($l$) times the width ($w$). The length and the width both have units of meters. So when we multiply them together we get meters times meters which should be a unit of area as shown below,



:::{math}
:enumerated: false

l(m) \times w(m) = lw(m^2)= a (m^2)

:::

We can also mix unit types for other derived units. For example, we could find the density of water by finding the mass that occupies a certain volume. What we would find is that $1\:g$ of water would occupy $1\:mL$
Look in {ref}`tbl_derived_units` for some of the derived units we will be using. 
:::{csv-table} Examples of Derived SI Units
:header: "Quantity", "Unit Name", "Symbol", "Expression in Base Units"
:label: tbl_derived_units

"Frequency", "Hertz", "Hz", "s⁻¹"
"Force", "Newton", "N", "kg⋅m/s²"
"Pressure", "Pascal", "Pa", "N/m² or kg/(m⋅s²)"
"Energy, Work, Heat", "Joule", "J", "N⋅m or kg⋅m²/s²"
"Power", "Watt", "W", "J/s or kg⋅m²/s³"
"Electric Charge", "Coulomb", "C", "A⋅s"
"Electric Potential", "Volt", "V", "J/C"
"Electric Resistance", "Ohm", "Ω", "V/A"
"Capacitance", "Farad", "F", "C/V"
"Magnetic Flux Density", "Tesla", "T", "N/(A⋅m)"
:::


### Unit Conversion

It will often be required to convert from one set of units to another based on experimental procedures or previous studies. It is vital you be able to confidently change units, and especially derived units, accurately. The key to making the conversions is to pay attention to whether the unit is in the numerator or denominator. Most errors come from converting with inverted relationships. Key to doing this correctly is writing out **ALL** units and not taking shortcuts. Let's show a couple of examples. 

we will start with a straight forward one where we will convert $1.23\:m$ to kilometers,

:::{math}
:enumerated: false
\begin{align}
1.23\:m =\:?\:km\\
\text{Use the fact that}\: 1000\:m = 1\:km\\
1.23\:m\times \frac{1\:km}{1000\:m}\\
1.23\:\cancel{m}\times \frac{1\:km}{1000\:\cancel{m}}\\
\frac{1.23\:km}{1000}=0.00123\:km=\boxed{1.23\times 10^{-3}\:km}
\end{align}
:::

We can do a trickier one if we look at derived units and units with exponents. Let's next convert $4.56\:kg\:L^{-1}$ to units of grams per cubic meter ($g\:m^{-3}$). To do this let's first write out some of the conversion ratios that might be helpful. $1\:kg = 1000\:g$, $1\:L = 1\:dm^3$, and $1\:dm = 0.1\:m$.

::::{dropdown} Click here for solution
:::{math}
:enumerated: false
\begin{align}
\frac{4.56\:\cancel{kg}}{1\:L}\times\frac{1000\:g}{1\:\cancel{kg}}=\frac{4.56\times10^3\:g}{1\:L}\\
\frac{4.56\times10^3\:g}{1\:\cancel{L}}\times\frac{1\:\cancel{L}}{1\:dm^3}=\frac{4.56\times10^3\:g}{1\:dm^3}\\
\frac{4.56\times10^3\:g}{1\:dm^3}\times\left(\frac{0.1\:dm}{1\:m}\right)^3=\frac{4.56\times10^3\:g}{1\:\cancel{dm^3}}\times\frac{0.001\:\cancel{dm^3}}{1\:m^3}=\frac{4.56\:g}{1\:m^3}\\
\boxed{4.56\:g\:m^{-3}}
\end{align}
:::
::::

Lastly let's look at using and converting to non-SI units (typically imperial units). You may see some familiar or unfamiliar unit comparisons that may be necessary. For example, there are $2.54\:cm$ per $1\:in$. There are also $12\:inch$ per $1\:ft$ and $5280\:ft$ per $1\:mi$. Using these facts let's convert $1\:km$ to miles.

::::{dropdown} Click here for solution
:::{math}
:enumerated: false
\begin{align}
1\:\cancel{km}\times \frac{1000\:m}{1\:\cancel{km}}=1000\:m\\
1000\:\cancel{m}\times\frac{100\:cm}{1\:\cancel{m}}=100000\:cm\\
100000\:\cancel{cm}\times\frac{1\:inch}{2.54\:\cancel{cm}}=39370\:in\\
39370\:\cancel{in}\times\frac{1\:\cancel{ft}}{12\:\cancel{in}}\times\frac{1\:mi}{5280\:\cancel{ft}} =\boxed{0.621\:mi}
\end{align}
:::
::::
### Coordinate Systems

Coordinate systems are used to help define a system in space. By creating a coordinate system every point in the space can be uniquely identified. If we want to determine thing like speed, or concentration we need some notion as

#### Cartesian

This is the coordinate system you are most familiar with using. The 

We can find the distance between these points using...

#### Spherical

Sometimes the mathematics is easier if you change the coordinate system. For 

:::{code-cell}
:tags: ["remove-input"]
questions = QuestionBlock()
questions.add_question(
    question_id="sec-2-ch-2-q01",
    question_text="Given the possible quantum numbers is it possible to have zero vibrational energy in a quantum HO? Please justify and explain your answer. "
)
display(HTML(questions.render()))
:::

#### Cylindrical 



## Newton's Laws

For our review we will just worry about the basics of Newton's Laws. These have been a very successful model and are good at explaining many physical phenomena. We will find later in this text that for some problems we will require the use of a new type of theory (Spoiler Quantum Theory). We will review Newton's laws but I will also give for you some information about why these laws are important for you to internalize and how they come up in every chemical system one way or another. 

Newton's Three Laws
- The first law is the law of inertia. An object will remain at rest or in uniform, straight-line motion unless acted upon by and external force. 
    * In general chemistry we learn about the Kinetic Molecular Theory of Gases (KMT), which models gas particles traveling in straight lines until they encounter either the wall or another gas particle. 
    * We will also find that additional and small attractive forces of real gases will require us to modify the ideal gas law due to the change in momentum of the gas particles. 
- The second law is the law that defines the force. The force ($F$) acting on an object is equal to its mass ($m$) times its acceleration ($a$). You can think of it also being the rate of change of the momentum ($p$) also (and in some ways maybe more fundamental). 
    * $F = ma$ and $F = \frac{dp}{dt}$
    * When looking at the origin of pressure what we are finding is the force exerted by the gas particle as it collides with the wall. 
    * Another way we can determine the force is by analyzing the potential energy. Interestingly the force of the system is related to how the potential changes with distance and is defined as $V\left(r\right) = -\frac{d V\left(r\right)}{dr}$. 
    * A very relevant example for studying chemistry is that the behavior of bonded atoms for small displacements will mimic the behavior of two masses connected by a spring. 
- The third law is the action-reaction law. For every action, there is an equal and opposite reaction. 
    * Again with two collisions of gas molecules we will conserve the momentum in the closed system (and energy if it is an elastic collision) due to the equal and opposite forces. 
## Vectors
It isn't just enough to say something is moving at a certain rate, we must also talk about in what direction. Given a coordinate system we can define things like velocity and acceleration based on these principles. This is the point of a vector. It not only has a value it contains in it information about the direction it is going. 

The magnitude of the vector is given by the length of the vector. 


**You will notice the magnitude of the vector equation is similar to how we found distances between two points. How are they related?**

## Energy

We define energy as what is required to do work. Well now we need to know what work is. Work is applying a force over a distance. The most obvious example would be lifting an object. If you have an object on the ground

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
(linear_angular_momentum)=
## Momentum
### Linear
We discussed this earlier where momentum is defined in equation {ref}`linear_momentum` 
:::{math}
:label: linear_momentum
p =mv
:::
### Angular

The moment of inertia $I$ plainly speaking is how difficult it is to start spinning something or how hard it is to slow/stop it from spinning. So a little object with not much mass is easy to stop whereas a large object with a big radius is more difficult. 

:::{math}
:label: moment_of_inertia
I = mr^2
:::

### Torque

Just as we need to apply a force to change linear momentum. We must apply a torque to change angular momentum. 

:::{note}
***Conceptual Question:*** In the moment of inertia question, does changing the mass or changing the radius have a greater impact on the moment of inertia? Explain your reasoning. 
:::
## Conservation Laws

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

