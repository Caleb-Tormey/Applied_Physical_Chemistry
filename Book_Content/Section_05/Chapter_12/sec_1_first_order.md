## 12.1 First-Order Reactions: The Biological Standard

The vast majority of biochemical processes—from radioactive decay to pharmaceutical clearance—follow first-order kinetics. In a first-order reaction, the rate is directly and linearly proportional to the concentration of a single reactant.

### The Calculus of Time

Let's derive the equation that allows us to predict the future. We start by setting our two definitions of the rate equal to each other for a first-order process:
$$-\frac{d[\text{A}]}{dt} = k[\text{A}]$$

To solve this differential equation, we need to separate our variables, putting all the $[\text{A}]$ terms on the left and all the $t$ terms on the right:
$$\frac{d[\text{A}]}{[\text{A}]} = -k dt$$

Now, we integrate both sides. We will integrate time from $t = 0$ to some future time $t$. We will integrate the concentration from our starting concentration $[\text{A}]_0$ to our future concentration $[\text{A}]_t$:
$$\int_{[\text{A}]_0}^{[\text{A}]_t} \frac{1}{[\text{A}]} d[\text{A}] = -k \int_{0}^{t} dt$$

The integral of $1/x$ is the natural logarithm ($\ln x$). Evaluating these integrals gives us:
$$\ln[\text{A}]_t - \ln[\text{A}]_0 = -kt$$

Rearranging this into the standard format of a straight line ($y = mx + b$), we arrive at the **Integrated First-Order Rate Law**:
$$\ln[\text{A}]_t = -kt + \ln[\text{A}]_0$$

**Laboratory Relevance:** This equation is an experimental goldmine. If you measure the concentration of a reactant over time in the lab and plot $\ln[\text{A}]$ on the y-axis against time $t$ on the x-axis, and the result is a perfectly straight line, you have definitively proven the reaction is first-order! The slope of that line instantly gives you $-k$. *(We will leave the calculus derivations for second-order and zeroth-order laws as an exercise in the practice problems at the end of the chapter).*

### The Independence of Half-Life ($t_{1/2}$)

The half-life ($t_{1/2}$) is the exact amount of time it takes for the concentration of a reactant to drop to exactly half of its current value. Let's plug this definition into our newly integrated equation. 

At $t = t_{1/2}$, the future concentration $[\text{A}]_t$ is exactly $\frac{1}{2}[\text{A}]_0$. 
$$\ln\left(\frac{1}{2}[\text{A}]_0\right) - \ln[\text{A}]_0 = -k t_{1/2}$$

Using the rules of logarithms ($\ln A - \ln B = \ln(A/B)$), the initial concentrations completely cancel out:
$$\ln\left(\frac{1}{2}\right) = -k t_{1/2}$$
$$-0.693 = -k t_{1/2}$$

Rearranging this gives us the fundamental equation for a first-order half-life:
$$t_{1/2} = \frac{0.693}{k}$$

Notice what is completely missing from this equation: **Concentration**. The half-life of a first-order reaction is a constant. If a drug has a half-life of 4 hours, it takes 4 hours for 100 mg to drop to 50 mg. It *also* takes 4 hours for 10 mg to drop to 5 mg. The clearance rate physically slows down as the concentration drops, keeping the half-life perfectly rigid.