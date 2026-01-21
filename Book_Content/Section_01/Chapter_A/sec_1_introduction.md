

## Solving Basic Equations
We will typically have equations of more than one variable in which we want to isolate one variable from the others. Often this is done to either show a relationship between two variables or to ultimately perform a calculation given a set of conditions. There are different invaluable methods and tools used in solving these equations. We will review some of the more important and relevant ones for this textbook. 

### Solving With Addition and Subtraction

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
### Solving With Multiplication and Division
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