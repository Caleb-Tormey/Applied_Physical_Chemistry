## 14.3 Transition State Theory

In Chapter 11, we used the empirical Arrhenius equation ($k = A e^{-E_a/RT}$) to describe how temperature affects rate. However, Arrhenius leaves us with a highly unsatisfying "fudge factor"—the pre-exponential $A$. 

In 1935, Henry Eyring developed **Transition State Theory (TST)**, replacing the empirical guesswork of Arrhenius with the rigorous laws of thermodynamics. 

Eyring hypothesized that the transition state ($\ddagger$) is actually in a quasi-equilibrium with the reactants. This allows us to apply Gibbs Free Energy to the top of the kinetic mountain. The resulting **Eyring Equation** is one of the most powerful formulas in physical chemistry:
$$k = \frac{k_B T}{h} e^{-\frac{\Delta G^\ddagger}{RT}}$$
*(where $k_B$ is the Boltzmann constant and $h$ is Planck's constant).*

### Dissecting the Activation Free Energy ($\Delta G^\ddagger$)
Just like standard free energy, we can break the activation free energy into its enthalpy and entropy components ($\Delta G^\ddagger = \Delta H^\ddagger - T\Delta S^\ddagger$):

* **Activation Enthalpy ($\Delta H^\ddagger$):** The raw energetic cost of stretching and breaking the reactant bonds. It is almost always a large positive number (unfavorable).
* **Activation Entropy ($\Delta S^\ddagger$):** The change in chaos required to reach the transition state. If two molecules must collide in a highly specific, restricted geometry to react, they are losing rotational and translational freedom. Therefore, $\Delta S^\ddagger$ is often negative (unfavorable). 

---