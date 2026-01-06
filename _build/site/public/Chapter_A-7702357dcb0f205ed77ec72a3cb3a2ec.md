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
  enumerator: A.%s
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
# Chapter A. Mathematics Review

The emphasis of this book is not in-depth, abstract and rigorous mathematical derivations. Still some mathematics will be required to fully understand concepts as well as calculate useful information. To that end we will review some basic mathematics involving the most important and useful mathematical concepts and techniques. By far, the most common mathematics you will use in this course will be solving equations. We will review rewriting and solving algebraic equations for certain variables using standard multiplication, division, addition and subtraction. We will then move on to manipulating and solving polynomial equations, review techniques using logarithms and exponents, review basic and useful trigonometry and then how to solve systems of equations. As we will be studying the physics of chemistry in this textbook it is important for us to have use of basic analysis tools. We will review basic calculus focusing on single variable derivatives and integrals while introducing the concept of partial derivatives. This chapter is not meant as a complete and exhaustive review of all the Mathematics you have taken to this point. Rather it is hopefully a quick and helpful reminder of mathematics you have learned in the past. It is important to review even some basic algebraic operations because even strong students can sometimes subtract when they mean to divide or forget to distribute mathematical operations to all the terms in the equation. However, if you find there are certain topics you are still struggling with even after this review, it is vital that you address those early as this book moves very quickly through topics. 

## Solving Equations
We will typically have equations of more than one variable in which we want to isolate one variable from the others. Often this is done to either show a relationship between two variables or to ultimately perform a calculation given a set of conditions. There are different invaluable methods and tools used in solving these equations. We will review some of the more important and relevant ones for this textbook. 

## Solving With Addition and Subtraction

Given equation {eq}`add_subtract`, we can solve for y by adding and subtracting terms. The general idea is that whatever we **do** to one side of the equation we do the exact same thing to the other side. In this sense, the equation is perfectly balanced and for all intents and purposes unchanged. 

:::{math}
:label: add_subtract

y - 4 + x = 4x - 10

:::

::::{dropdown} Click here for solution
:::{math}
:enumerated: false
\begin{align}

y - 4 + x \textcolor{red}{+ 4} = 4x - 10 \textcolor{red}{+ 4} \\
y -\cancel{ 4 \textcolor{red}{+ 4}} + x = 4x \boxed{- 10 \textcolor{red}{+ 4}} \\
y + x = 4x - 6 \\
y + x \textcolor{red}{-x} = 4x - 6 \textcolor{red}{-x} \\
y + \cancel{x \textcolor{red}{-x}} = \boxed{4x  \textcolor{red}{-x}}- 6 \\
y = 3x-6
\end{align}
:::
::::
## Solving With Multiplication and Division
Given equation {eq}`multi_divide`, we can solve for y by multiplying and dividing terms. Just as before, whatever we **do** to one side of the equation we do the exact same thing to the other side. 

:::{math}
:label: multi_divide

\frac{x}{ay}=\frac{2a}{x^2}

:::

::::{dropdown} Click here for solution
:::{math}
:enumerated: false
\begin{align}
\frac{x}{ay}\textcolor{red}{y}=\frac{2a}{x^2}\textcolor{red}{y}\\
\frac{x}{a\cancel{y}}\cancel{\textcolor{red}{y}}=\frac{2a\textcolor{red}{y}}{x^2}\\
\frac{x}{a} = \frac{2ay}{x^2}\\
\frac{x}{a}\textcolor{red}{x^2}= \frac{2ay}{x^2}\textcolor{red}{x^2}\\
\frac{\boxed{x}}{a}\boxed{\textcolor{red}{x^2}}= \frac{2ay}{\cancel{x^2}}\cancel{\textcolor{red}{x^2}}\\
\frac{x^3}{a} = 2ay\\
\frac{x^3}{a}\textcolor{red}{\frac{1}{2a}} = 2ay\textcolor{red}{\frac{1}{2a}}\\
\frac{x^3}{\boxed{a}}\textcolor{red}{\frac{1}{\textcolor{black}{\boxed{\textcolor{red}{2a}}}}} = \cancel{2a}y\textcolor{red}{\frac{1}{\textcolor{black}{\cancel{\textcolor{red}{2a}}}}}\\
\frac{x^3}{2a^2}=y\\
y = \frac{x^3}{2a^2}
\end{align}

:::
::::

### Solving Using A Combination

We have seen some examples using addition/subtraction or multiplication/division. Often when both types of processes must be done to solve an equation some confusion can occur. There are several helpful things to considered when dealing with situations like this. The first is when adding/subtracting elements you must ensure they have the same denominator. For example, you can't add $\frac{2a}{x}$ and $3a$ directly because the respective denominators of $x$ and $1$ do not match. The second thing is that when multiply/dividing you must apply this process to each term. For example, if my equation is $a + b + c = 2x$ and I divide both sides by x the result will be $\frac{a + b + c}{x}=\frac{a}{x} + \frac{b}{x} + \frac{c}{x} = 2$. Let's look at the solution to equation {eq}`asmd_example` and again solve for $y$.

:::{math} 
:label: asmd_example
xy + x -16 = 40 + z
:::

::::{dropdown} Click here for solution
:::{math}
:enumerated: false
\begin{align}
xy + x -16 = 40 + z \\
xy + x - 16 \textcolor{red}{+ 16} = 40 + z \textcolor{red}{+ 16}\\
xy + x -\cancel{ 16 \textcolor{red}{+ 16}} = \boxed{40 \textcolor{red}{+ 16}} + z\\
xy + x = 56 + z\\
\textcolor{red}{\frac{1}{x}}\left (xy + x\right) = \textcolor{red}{\frac{1}{x}}\left(56 + z\right)\\
\frac{xy}{x} + \frac{x}{x} = \frac{56 + z}{x}\\
\frac{\cancel{x}y}{\cancel{x}} + \frac{\cancel{x}}{\cancel{x}}= \frac{56 + z}{x}\\
y + 1 = \frac{56 + z}{x}\\
y + 1 \textcolor{red}{-1} = \frac{56 + z}{x}\textcolor{red}{-1} \\
y + \cancel{1 \textcolor{red}{-1}} = \frac{56 + z}{x} - 1 \\
y = \frac{56 + z}{x} - 1

\end{align}
:::
::::

### Polynomials
In physical sciences, we often use polynomials as a versatile mathematical tool to model and understand physical behavior and experiment. A polynomial is defined as an expression that consists of sums of variables raised to non-negative integer powers and multiplied by coefficients that can be positive or negatively signed. The general form of a polynomial is described in equation {ref}`gen_poly` where x is our variable, $n$ is the degree of the polynomial. It's the highest exponent of $x$ and must be a non-negative integer. Each $a$ term like $a_n$ is a coefficient. Coefficients are just constant numbers that multiply its corresponding variable term. These can be positive, negative, or zero. You can think of it as a scaling factor that determines the magnitude and sign of its associated $x$ power. Notice that for the final term $x^0=1$ so it just becomes a constant $a_0$.
:::{math}
:label: gen_poly
y = a_n x^n + a_{n-1} x^{n-1}\cdots a_2 x^2 + a_1 x^1 + a_0 x^0
:::

Here are some examples of polynomials you may have already encountered or will encounter in this text. 
- $y = mx + b$ is the equation for a line.
- $y = ax^2 + bx + c$ is the equation for a parabola.
- $V^3 - \left ( b + \frac{RT}{P}\right)V^2 + \frac{a}{P}V -\frac{ab}{P} = 0$ is the van der Waals equation.

 We use them for three primary reasons. First, you have likely done a ``line of best fit'' on some data in your laboratory or class. Behind the scenes, the computer program is doing a linear regression on a polynomial of degree one ($y = a_1x + a_0$), we can fit polynomials of even higher degrees in the same way to experimental data points to create a mathematical model of the system we're studying. Second, polynomials are incredibly easy to work with because their derivatives and integrals can be found using the simple power rule you learned in calculus, making calculations straightforward. Finally, and most powerfully, many complex functions that describe real-world phenomena, such as the potential energy of a chemical bond, can be accurately approximated by a polynomial via a Taylor series expansion. While we will not do this explicitly, you will however see what the expansion is and how it works. This allows us to simplify complicated problems into a manageable form without losing essential physical insight.

 Recall that we on occasion must find the roots of an equation. That is where the equation is equal to zero. When solving quadratic equations, polynomials of $n = 2$, you have probably learned how to factor the equation into the product of two linear parts. For example, 
 :::{math}
 :enumerated: false
\begin{align}
x^2 + 3x + 2 = 0\\
\left(x+1\right)\left(x+2\right) = 0\\
\end{align}
:::
and so the solution is $x = -1,x = -2$. 

Or for more challenging problems you might have learned how to complete the square or use the quadratic formula (equation {ref}`quadratic_formula`). 
:::{math}
:label: quadratic_formula
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
:::
In this class we will encounter higher order polynomials. There are methods for solving these, however, we will not learn how to do them explicitly. Rather we will use computational tools like _Mathematica_ or Python. 
 
  
### Exponentials and Logarithms 
We will start by looking at $e$ and $\ln$. These are called the exponential (sometimes referred to as the Natural number or Euler's number) and the natural logarithm respectively. They are ubiquitous in natural science due to the fact many physical processes are well modeled by first order differential equations. Another point of these two operations is that they are the inverse of one another. For example,
:::{math}
:enumerated: false
\begin{align}
y = e^x\\
\ln{y} = \ln{e^x}\\
\ln{y} = x
\end{align}
:::

(properties-of-exponentials-and-logarithms)=
#### Properties of Exponentials and Logarithms

Here we will review the properties of exponents and logarithms. The first is to recognize that an exponent is just repeated multiplication of the base. For example,
:::{math}
:enumerated:false
2^3 = 2 \times 2 \times 2
:::

So in general we say that for a base, $b$ and exponent $m$ the exponent can be defined as

:::{math}
b^m = \prod_{i = 1}^m b_i
:::

So we can multiply exponents of the same base in the following way,

:::{math}
:label: product_of_powers
b^m\times b^n = b^{m+n}
:::

Likewise, we can look at dividing exponents of the same base but accounting for the negative in the exponent of the denominator

:::{math}
:label: quotient_of_powers
\frac{b^m}{b^n} = b^{m-n}
:::

#### Changing Bases
In the equation $y = ae^x$, $e$ is called the base and x is the exponent. The base of the Log operation must match the base of the exponent. So in our case $\ln$ is the natural log since it is in base $e$ which is the natural number. If instead you had the number $10^x$ this would be base ten, and you would need to use a base-10 logarithm, $Log_{10}$. You can change bases by using the following relationship. 
:::{math}
:label: log_convert
log_b\left ( a\right) = \frac{log_x\left(a\right)}{log_x\left(b\right)}
:::

For Example,

If we are curious to solve for the value of $x$ in equation {ref}`log_problem`we could attempt to solve it by taking the $Log_2$ of both sides, however, often a calculator will only have a $Log_{10}$ or natural log ($\ln$) button. 

:::{math}
:label: log_problem
2^x = 100
:::
We can see where equation {ref}`log_convert` comes from and we can solve our problem in the following way. 
::::{dropdown} Click here for solution
:::{math}
:enumerated: false
\begin{align}
2^x = 100\\
\textcolor{red}{\ln{\textcolor{black}{2^x}}} = \textcolor{red}{\ln{\textcolor{black}{100}}}\\
x\ln{2} = \ln{100}\\
x = \frac{\ln{100}}{\ln{2}}\\
x \approx  \frac{4.60517}{0.69315}\\
x \approx  6.6386\\
\end{align}
:::
::::


#### Performing Algebra with Exponentials and Logarithms
 
Here is the first part of my chapter. Now for a question.

Often the place students get the most screwed up is when attempting to do algebraic manipulation with these two operations. The biggest issue is misapplying the rules from section {ref}`properties-of-exponentials-and-logarithms`
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



(trigonometric_identities)=
### Trigonometric Functions and Identities
While trigonometry is the branch of mathematics concerned with the relationships between angles and sides of triangles. While we won't be reviewing all the details of triangles there are a few important things to review. The first are the basic 

The relationship between these functions can be seen most explicitly using the unit circle. 


### Simultaneous Equations
a + b = c
2a -3b = 2c
-3a + 8b = 10c

## Functions

In another example, if we look at the ideal gas law $PV = nRT$ we can ask how the pressure will vary with changing volume at constant moles (n) and constant temperature (T). To solve this we must manipulate the equation to get pressure (P) and volume (V) on separate sides of the equation. Because we are looking at how pressure is changing with volume we will want to have pressure on the left-hand side, abbreviated LHS, and then have volume on the right-hand side, abbreviated RHS. This will be done by dividing 
One thing we will note which we manipulate an equation to put one variable on the LHS and one variable on the RHS is we are creating a function. Plainly speaking, a function is a little mathematical machine that takes an input, what we call the **independent** variable, and spits out another variable, what we call the **dependent** variable. Sometimes functions will be clearly spelled out. For example, we will see when we get to wave-functions where we declare them as $\psi\left ( x \right)$. In this case $\psi$ is the dependent variable and is a function of $x$ which is the independent variable. Sometimes, the relationship, dependent and independent variables, is not explicitly stated, and we must make that inference. This is the case for our ideal gas law example above. For that example, we could say that the pressure is a function of the volume. Stated more directly $P\left(V\right) = \frac{nRT}{V}$. From this example you can also see that we could additionally make functions of the pressure as it relates to varying the temperature (T) or the number of moles (n). 

Testing Question Asking Scheme

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
    question_id="sec1-chA-q2",
    question_text="This is the second question about this section."
)
display(HTML(questions.render()))
:::


(math_derivatives)=
## Derivatives

In chemistry, we are often concerned about how certain quantities change with space or time. For example, as a chemical reaction proceeds we might be interested in how much starting material is left after a certain amount of time. Or perhaps we want to understand how pressure of a vessel may alter with changes in temperature. Here is where the mathematics of calculus are indispensable. One of the foundational ideas in calculus is the concept of the derivative. The derivative of a line or curve will give us information about the behavior of that function. More specifically details about how the line or curve changes.

For example, if we coul what we are looking at is its slope. The slope is defined as the rise (or fall) of a curve over the ``run'' of the curve. 

The average amount that it changes we can take two points a certain distance apart and see what the average slope of the curve is over those two points. However, we might become interested in knowing more and more specifically what the slope is over a very small distance. We can take this to the extreme and ask what happens when the distance between the x values is zero. 

Our curves will be defined as functions and we can mathematically do things...


### Rules for differentiating (one variable)
We will not prove all of these rules as that is better done in an actual calculus class, rather we will remind of you of the rules for these one dimensional derivatives.
- Derivative of a constant $f\left(x\right) = a$, $f'\left(x\right) =\frac{d f\left(x\right)}{d x} = 0$. An example of this would be $f\left(x\right) = 5$ where $\frac{d 5 }{dx} = 0$.
- Derivative using power rule where something has the form $f\left(x\right) = a x^n$ where $n$ can be any number positive or negative. (we will often see $n$ be integer value but it isn't required) 
 

- Derivative of a sum 

- Derivative of a product

- Derivative of trig functions

- Derivative of an exponential

- Derivative of composite function and the chain rule

- Derivative of a power of x

- Derivative of a quotient



## Integrals
Integral x^x
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
    question_id="sec1-chA-q3",
    question_text="This is the third question about this section."
)
display(HTML(questions.render()))
:::
## Summary of stuff 

here is a summary...probably not using it

:::{code-cell} python
:tags: ["remove-input"]

from _ext.interactive_qa import QAManager
from IPython.display import display, HTML

# This renders the final control panel.
# Pass the desired title for the printed page here.
manager = QAManager(page_title="Chapter 2: Foundations of Quantum Mechanics")
display(HTML(manager.render()))
:::
## Practice Problems

You are free to do none, some or all these problems as you see fit. They would be very helpful to use in studying for the chapter exams. 
- Solve the following problems for $x$
    * $2 + x = 34 + 2y$
    * $\frac{3y}{17x} = 15$
    * $\frac{3y^2 + x}{10y} = 15y + y^2$
- Given the following polynomials find the values of x 
    * $x^2 + 4x + 3= 0$  
    * $2x^2 + 16x - 4 = 0$
- If $g(x) = a^x$ and $f(x) = a^{2x}$ solve the following problems
    * $g\left(x\right)f\left(x\right) = \:?$
    * $\frac{f\left(x\right)}{g\left(x\right)}= \:?$
    * $g(x)^2f(x)^{-1}=\:?$
- Problem 4
 