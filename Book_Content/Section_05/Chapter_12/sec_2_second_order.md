## 12.2 Second-Order Reactions and the "Pseudo" Trick

A classic second-order reaction relies on the collision of two different molecules: $\text{Rate} = k[\text{A}][\text{B}]$. 

Integrating this equation as written is a mathematical nightmare because both $[\text{A}]$ and $[\text{B}]$ are changing simultaneously at different rates depending on their stoichiometry. 

To avoid solving monstrous multivariable differential equations, physical chemists and biochemists use a brilliant experimental hack called **Pseudo-First-Order Kinetics**. 

Imagine you are studying the hydrolysis of a specific ester ($\text{A}$) by reacting it with water ($\text{B}$). You set up your beaker with 0.001 M of the ester. Since it is an aqueous solution, the concentration of water is roughly 55.5 M. 

As the reaction proceeds to 100% completion, the ester concentration drops from 0.001 M to 0 M. The water concentration drops from 55.5 M to 55.499 M. Mathematically, the concentration of water did not change. It is essentially a constant. 

We can bundle this massive, unchanging concentration of $[\text{B}]$ into our rate constant to create a new, "fake" rate constant called $k_{obs}$ (the observed rate constant):
$$k_{obs} = k[\text{B}]$$
$$\text{Rate} = k_{obs}[\text{A}]$$

By flooding the system with a massive excess of one reactant, we have mathematically forced a complex second-order reaction to behave exactly like a simple first-order reaction! You can now use all the easy math from Section 12.1 to analyze your data.