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
:::{include} sec_1_introduction.md
:::
:::{include} sec_2_other_equations.md
:::
:::{include} sec_3_functions.md
:::
:::{include} sec_4_derivatives.md
:::
:::{include} sec_5_integrals.md
:::









## Summary of stuff 

**Tools of the Trade: Algebra and Functions** Mathematics provides the grammar for describing the physical world. At the foundation, we rely on algebra and the concept of dimensional consistency; unlike abstract math, physical variables carry units, and equations must balance both numerically and dimensionally. We frequently model reality using specific types of functions. Polynomials help us find equilibrium points through their roots, though we must always interpret which mathematical solutions are physically possible. Exponentials and logarithms are particularly vital in chemistry, allowing us to handle vast scales (like pH) and model natural decay or probability distributions. Furthermore, trigonometric functions and the symmetry of even and odd functions provide the framework for understanding periodic motion and simplifying the complex equations found in quantum mechanics.

**The Calculus of Change: Derivatives and Integrals** Beyond static relationships, physical science is fundamentally about change and accumulation. The derivative serves as our tool for measuring instantaneous rates of change, geometrically represented as the slope of a curve. It allows us to determine how sensitive a system is to fluctuations and to identify stable states by locating where the slope is zero (minima and maxima). Conversely, integration allows us to calculate accumulation—summing up varying rates to find total quantities, like calculating total energy from power or probability from a wavefunction. Whether finding the area under a curve geometrically or solving definite integrals using substitution and tables, calculus provides the bridge between theoretical models and measurable physical quantities.

:::{code-cell} python
:tags: ["remove-input"]

from _ext.interactive_qa import QAManager
from IPython.display import display, HTML

# This renders the final control panel.
# Pass the desired title for the printed page here.
manager = QAManager(page_title="Chapter A: Mathematics Review ")
display(HTML(manager.render()))
:::
## Practice Problems

You are free to do none, some, or all of these problems as you see fit. They are designed to mimic the mathematical manipulations you will encounter in the rest of the book.

### 1. Algebra and Rearrangement
*Solve the following equations for $x$ in terms of the other variables.*
1.  **Simple:** $2 + x = 34 + 2y$
2.  **Intermediate:** $\frac{3y}{17x} = 15$
3.  **Advanced:** $\frac{3y^2 + x}{10y} = 15y + y^2$

### 2. Roots of Polynomials
*Find the values of $x$ that satisfy these equations.*
1.  **Simple (Factorable):** $x^2 + 4x + 3= 0$
2.  **Intermediate (Quadratic Formula):** $2x^2 + 16x - 4 = 0$
3.  **Advanced (Cubic/Substitution):** $x^4 - 5x^2 + 4 = 0$ *(Hint: Treat $x^2$ as the variable first)*

### 3. Exponentials and Logarithms
*Solve for $x$.*
1.  **Simple:** $Ae^{2x} = y$
2.  **Intermediate:** $-\log_{10}(x) = 2.3$ *(Important for pH calculations)*
3.  **Advanced:** $e^{2x} - 5e^x + 6 = 0$ *(Hint: This is a quadratic in disguise. Let $u = e^x$)*

### 4. Logarithm Rules
*Assume you only have the natural log function ($\ln$) on your calculator. Use the change-of-base formula or log properties to express $x$ in terms of values you could type into a calculator.*
1.  **Simple:** $x = \log_{10}(810)$
2.  **Intermediate:** $x = \log_{10}(12) - \log_{10}(13)$
3.  **Advanced:** Solve for $x$ in terms of $C, a, b$: $C = \log_a(x) + \log_b(x)$

### 5. Trigonometric Identities
*Prove that the LHS (Left Hand Side) equals the RHS (Right Hand Side). Construction of the unit circle may be helpful.*
1.  **Simple:** $\sin^2\left(\frac{\pi}{4}\right) + \tan\left(\frac{\pi}{4}\right) = \frac{3}{2}$
2.  **Intermediate:** $4 \cos^2(x) - 2 = 2\cos(2x)$
3.  **Advanced:** $\sin(\alpha -\beta) + \sin(\alpha +\beta) = 2\sin(\alpha)\cos(\beta)$

### 6. Exponent Rules
*Given $g(x) = a^x$ and $f(x) = a^{2x}$, simplify the following expressions into a single term like $a^{(\dots)}$.*
1.  **Simple:** $g(x)f(x)$
2.  **Intermediate:** $\frac{f(x)}{g(x)}$
3.  **Advanced:** $g(x)^2 f(x)^{-1}$

### 7. Even and Odd Functions
*Determine if the following functions are Even ($f(x)=f(-x)$), Odd ($f(-x)=-f(x)$), or Neither. These symmetries are crucial for simplifying quantum mechanical integrals.*
1.  **Simple:** $f(x) = 3x^4 - 2x^2 + 1$
2.  **Intermediate:** $f(x) = x \sin(x)$
3.  **Advanced:** Without calculating the value, evaluate the integral $\int_{-5}^{5} (x^3 - 3x) \, dx$ based on symmetry arguments.

### 8. Derivatives
*Calculate the first derivative, $f'(x)$, for the following functions.*
1.  **Simple (Power Rule):** $f(x) = 4x^3 - \frac{2}{x^2} + 5$
2.  **Intermediate (Product Rule + Exponential):** $f(x) = x^2 e^{-3x}$ *(Common in radial probability distributions)*
3.  **Advanced (Chain Rule + Trig):** $f(x) = \ln(\cos(x^2))$

### 9. Integrals
*Calculate the following integrals.*
1.  **Simple (Indefinite):** $\int (3x^2 + e^{2x}) \, dx$
2.  **Intermediate (Definite):** $\int_{1}^{3} \frac{1}{x} \, dx$
3.  **Advanced (Technique):** $\int_{0}^{\infty} x e^{-x^2} \, dx$ *(Hint: Use U-substitution where $u = -x^2$. Watch your limits!)*
 