## 14.2 Approximating Complex Mechanisms

When physical chemists attempt to derive the overall rate law for a multi-step mechanism, they often run into intermediates—highly unstable molecules that exist temporarily between steps. Because you cannot easily measure the concentration of a fleeting intermediate in a lab, we have to substitute it out of our rate law equations using mathematical approximations.

### The Steady-State Approximation (General)
We applied this concept specifically to enzymes in Chapter 13, but it applies to any sequential reaction:
$$A \xrightarrow{k_1} I \xrightarrow{k_2} P$$

If the intermediate ($I$) is highly reactive (meaning $k_2 \gg k_1$), it will be consumed the split-second it is created. Therefore, its concentration remains incredibly low and effectively constant. We set the rate of change of the intermediate to zero:
$$\frac{d[I]}{dt} = k_1[A] - k_2[I] \approx 0$$
Solving for $[I]$ allows us to replace the unmeasurable intermediate with measurable reactants:
$$[I] = \frac{k_1}{k_2}[A]$$

### The Pre-Equilibrium Approximation
Sometimes, a mechanism features a fast, reversible step followed by a slow, rate-determining step:
$$A + B \rightleftharpoons I \quad \text{(Fast, equilibrium)}$$
$$I \xrightarrow{k_{slow}} P \quad \text{(Slow, RDS)}$$

Because the first step is zooming back and forth infinitely faster than the second step can drain $I$ away, the first step is essentially at equilibrium. We can use the equilibrium constant ($K_{eq}$) to express the intermediate in terms of reactants:
$$K_{eq} = \frac{[I]}{[A][B]} \implies [I] = K_{eq}[A][B]$$
Substituting this into the rate law for the slow step ($\text{Rate} = k_{slow}[I]$) gives us a perfectly solvable overall rate law based only on things we can measure.

---