## Multielectron Atoms: Shielding and Penetration

While we can solve the Hydrogen atom exactly, **multielectron atoms cannot be solved exactly** due to electron-electron repulsion. We must use approximations (like the Hartree-Fock method), which are beyond this text.

However, we can understand their behavior conceptually. In multielectron atoms, the $n$-degeneracy is broken ($2s$ is lower than $2p$). This is due to:

* **Shielding:** Inner electrons "block" the nuclear charge from outer electrons.
* **Penetration:** Some orbitals (like $s$) have a small probability of being very close to the nucleus. An electron that "penetrates" the inner shells feels a higher effective nuclear charge ($Z_{eff}$) and is therefore lower in energy.

### Radial Distribution Functions (RDF)
The RDF represents the probability of finding an electron at a distance $r$. Note how the $2s$ orbital has a small "hump" closer to the nucleus than the $2p$ orbital—this is penetration!

:::{code-cell} python
:tags: ["remove-input"]
:label: rdf_plot
import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0, 20, 500)
# Simple RDF approximations for 2s and 2p
rdf_2s = (r**2) * ( (2 - r)*np.exp(-r/2) )**2
rdf_2p = (r**2) * ( r*np.exp(-r/2) )**2

plt.figure(figsize=(8,4))
plt.plot(r, rdf_2s/np.max(rdf_2s), label='2s RDF', color='blue')
plt.plot(r, rdf_2p/np.max(rdf_2p), label='2p RDF', color='red', linestyle='--')
plt.title("Penetration: 2s vs 2p Radial Distribution")
plt.xlabel("Radius (r)")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
:::