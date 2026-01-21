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
- Given the following exponential and logrithmic equations, solve for x
    * $Ae^{2x} = y$
    * $-log_{10}(x) = 2.3$
    * $e^{2x}−5e^x+6=0$
- Assuming you only have the natural log function($ln$) on your calculator, calculate the value of $x$ in the following equations:
    * $x = log_{10}\left(810\right)$
    * $x = log_{10}\left(12\right) - log_{10}\left(13\right)$
    * $C = log_a\left(x\right) + log_b\left(x\right)$
- Show the following relationships are true. It may be helpful to use trigonometric identities.  
    * $\sin^2\left(\frac{\pi}{4}\right) + \tan\left(\frac{\pi}{4}\right) = \frac{3}{2}$
    * $4 \cos^2\left(x\right) - 2 = 2\cos\left(2x\right)$
    * $\sin\left(\alpha -\beta\right) + \sin\left(\alpha +\beta\right) = 2\sin\left(\alpha\right)\cos\left(\beta\right)$
- If $g(x) = a^x$ and $f(x) = a^{2x}$ solve the following problems
    * $g\left(x\right)f\left(x\right) = \:?$
    * $\frac{f\left(x\right)}{g\left(x\right)}= \:?$
    * $g(x)^2f(x)^{-1}=\:?$
- Problem 4
 