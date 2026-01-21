(math_derivatives)=
## Derivatives

In chemistry, we are often concerned about how certain quantities change with space or time. For example, as a chemical reaction proceeds we might be interested in how much starting material is left after a certain amount of time. Or perhaps we want to understand how pressure of a vessel may alter with changes in temperature. Here is where the mathematics of calculus are indispensable. One of the foundational ideas in calculus is the concept of the derivative. The derivative of a line or curve will give us information about the behavior of that function. More specifically details about how the line or curve changes.

For example, if we coul what we are looking at is its slope. The slope is defined as the rise (or fall) of a curve over the ``run'' of the curve. 

The average amount that it changes we can take two points a certain distance apart and see what the average slope of the curve is over those two points. However, we might become interested in knowing more and more specifically what the slope is over a very small distance. We can take this to the extreme and ask what happens when the distance between the x values is zero. 

Our curves will be defined as functions and we can mathematically do things...


### Rules for differentiating (one variable)
We will not prove all of these rules as that is better done in an actual calculus class, rather we will remind of you of the rules for these one dimensional derivatives.
- Derivative of a constant $f\left(x\right) = a$, $f'\left(x\right) =\frac{d f\left(x\right)}{d x} = 0$. An example of this would be $f\left(x\right) = 5$ where $f'\left(x\right) = \frac{d 5 }{dx} = 0$.
- Derivative using power rule where something has the form $f\left(x\right) =  x^n$ where $n$ can be any number positive or negative. (we will often see $n$ be integer value, however,  isn't required) The power rule is defined in equation {eq}`power_rule`
:::{math}
:label: power_rule
\frac{df}{dx}=\frac{d}{dx}x^n =  nx^{n-1} 
:::
 
- Derivative of trig function. Here is a list of the trig functions and their derivatives. 
  * $\frac{d}{dx} \sin kx = k\cos kx$
  * $\frac{d}{dx} \cos kx = -k \sin kx$
  * $\frac{d}{dx} \tan kx = k\sec^2 kx$
  * $\frac{d}{dx} \cot kx = -k\csc^2 kx$
  * $\frac{d}{dx} \sec kx = k\sec kx \tan kx$
  * $\frac{d}{dx} \csc kx = -k\csc kx \cot kx$


- Derivative of an exponential, $\frac{d}{dx} e^{wx} = w e^{wx}$. For example, the first derivative of $e^{-3\pi x}$ is $-3\pi e^{-3\pi x}$

- Derivative of a sum $\frac{d}{dx}\left(g\left(x\right) + f\left(x\right)\right)$ is just the sum of the derivatives, $g'\left(x\right) + f'\left(x\right)$. For example, the first derivative of $2x^2 + \frac{2}{x^3}$ is equal to $4x - \frac{6}{x^4}$.

- Derivative of a product is defined as $\frac{d}{dx}f\left(x\right)g\left(x\right) = f'\left(x\right)g\left(x\right) + f\left(x\right)g'\left(x\right)$. For example, $\frac{d}{dx}\left(x^2\sin x\right) = 2x\sin x + x^2\cos x$

- Derivative of composite function and the chain rule. In order to take the derivative of a composite function we will use the chain rule which is defined as $\frac{d}{dx}f\left(g\left(x\right)\right) = \frac{df}{dg}\frac{dg}{dx}$. Let's make this more concrete with an example. Let's take the first derivative of $\sin{x^2}$. We can define $f\left(x\right) = \sin x$ and $g\left(x\right) = x^2$. So first let's calculate $\frac{d f\left(g\left(x\right)\right)}{dg\left(x\right)} =\frac{d \sin g\left(x\right)}{d g\left(x\right)}= \cos g\left(x\right)$. And then we can calculate $\frac{d g\left(x\right)}{dx} = \frac{d x^2}{dx} = 2x$. We can then substitute in the definition of $g\left(x\right)$ and then multiply these two solutions as shown in the definition of the chain rule to get $\frac{d \sin x^2}{d x} = 2x \cos x^2 $

- Derivative of a power of x

- Derivative of a quotient

- Derivatives of even and odd functions