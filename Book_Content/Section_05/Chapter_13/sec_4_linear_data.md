## 13.4 Linearizing Data: The Lineweaver-Burk Plot

The Michaelis-Menten equation graphs as a rectangular hyperbola. If you plot $V_0$ against $[S]$ in a lab, the curve slowly flattens out as it asymptotically approaches $V_{max}$. 

Because it is notoriously difficult to accurately eyeball an asymptote on a curved graph, physical chemists use a mathematical trick to linearize the data. By taking the reciprocal of both sides of the Michaelis-Menten equation, we get the **Lineweaver-Burk Equation**:
$$\frac{1}{V_0} = \left(\frac{K_m}{V_{max}}\right) \frac{1}{[S]} + \frac{1}{V_{max}}$$

This beautifully matches the equation of a straight line ($y = mx + b$). 

* The **y-intercept** is $\frac{1}{V_{max}}$.
* The **x-intercept** is $-\frac{1}{K_m}$.
* The **slope** is $\frac{K_m}{V_{max}}$.

This double-reciprocal plot allows researchers to determine $V_{max}$ and $K_m$ with extreme precision using simple linear regression. 

---