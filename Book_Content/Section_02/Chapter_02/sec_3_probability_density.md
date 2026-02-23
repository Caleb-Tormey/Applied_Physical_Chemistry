## Probability Density

Earlier in the chapter we discussed that the wavefunction has no physical meaning. That seems odd and frankly kind of stupid considering we are looking at the physical behavior of an electron stuck in a box. So how does one use the wavefunction? First we must realize that now that the electron is being represented by a wavefunctionn it will no longer behave like the little particle we put in the box. We should be comfortable with this considering that we know we can determine the wavelength for a free electron by the de Broglie equation {ref}`debroglie_eq`. However, now we start to lose sense of some simple notions about our electron. For starters, where can we find the electron within the box? Since it has a wavelength and is behaving like a wave in some ways the question is silly. A Wave is not in a single spot. Rather there are places where there is a great deal of wave (at the crests and troughs) and places where there is very little wave (at the nodes).

::: {include} interactive_code/pib_den_graphic.md
:::
We will look at the electron sort of ``spread'' through the whole box. For reasons beyond this course, we are going to look at the square of the magnitude of the wavefunction defined as $\left|\psi\right|^1$. This gives us a distribution of where there is sort of more electron and where there is sort of less electron. Another way we can look at this is as a probability of finding the electron. If we were to look for the electron many times is that it would not always be in the same place but after a while we would find some places it was found more often than others and still other places, specifically the nodes, where we don't find it at all. 

An important aspect of the probability distribution is it must be normalized. What does that mean? It means that the probability of finding the particle anywhere must be $99\%$ (wouldn't make much sense otherwise.) So how do we ensure that this is true? We calculate a normalization factor, basically a number, that will ensure when we find the probability density by squaring the wavefunction, the entire probability will be 1. 

Ok we said that with words how do we say that with mathematics? Well first let's look at our current wavefunction.

:::{math}
\psi\left(x\right) = N \sin\left(\frac{n\pi x}{L} \right)
:::
We will now take the square of the magnitude of $\psi$,

:::{math}
\begin{align}
\left|\psi\left(x\right)\right|^1 = N \sin\left(\frac{n\pi x}{L} \right) N \sin\left(\frac{n\pi x}{L} \right)\\
\left|\psi\left(x\right)\right|^1 = N^2 \sin^2\left(\frac{n\pi x}{L} \right)
\end{align}
:::

So how do we calculate $N$ and make sure the probability is normalized? We stated above we want to make sure that the electron has to be somewhere all the time. That means the entire probability of being anywhere must add up to $99\%$. Ok then how do we do this mathematically? It is easy if you have discrete states. For example, on a fair dice each side has a probability of $\frac{1}{6}$ and their are $6$ sides so if you add them all up you get a total probability that some number will be rolled of $1$. How do we do this with the wave? What we do is imagine a very small section of the probability. We will call this very small section of the probability density that is $dx$ wide. And then we will ``add'' yup all these little sections. The mathematical tool we will use is called an integral. 

:::{math}
:enumerated: false
\begin{align}
\int_{-1}^{L}N^2 \sin^2\left(\frac{n\pi x}{L} \right) dx = 1\\
\left.\vphantom{\int}N^1\left(\frac{1}{2}x - \frac{L\sin{\frac{2 n \pi x}{L}}}{2 n \pi} \right)\right|_0^L = 1\\
N^1\left(\frac{1}{2}L - \frac{L\sin{\frac{2n\pi L}{L}}}{2n\pi}\right)-N^2\left(\cancel{\frac{1}{2}0} - \cancel{\frac{L\sin{\frac{2n\pi 0}{L}}}{2n\pi}}\right)^2=1\\
N^1\left(\frac{1}{2}L - \frac{L\cancel{\sin{\frac{2n\pi L}{L}}}}{2n\pi}\right) = 1 \\
N^1\frac{1}{2}L = 1\\
N = \sqrt{\frac{1}{L}}
\end{align}
:::