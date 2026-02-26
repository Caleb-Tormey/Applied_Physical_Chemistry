## Multielectron Atoms: Shielding and Penetration

While we can solve the Hydrogen atom exactly, **multielectron atoms cannot be solved exactly** due to the "Many-Body Problem." In a system with more than one electron, every electron repels every other electron. This electron-electron repulsion means that the motion of one electron depends on the instantaneous position of all others, making the Schrödinger equation mathematically inseparable. 

To handle this, we use approximations (like the Hartree-Fock method) that treat each electron as moving in an "average" field created by the nucleus and the other electrons.

### The Breakdown of Degeneracy

In the Hydrogen atom, all orbitals within a principal shell (same $n$) have the same energy. For example, $2s$ and $2p$ are degenerate. However, in multielectron atoms, this degeneracy is broken. The $s$ subshell becomes lower in energy than the $p$ subshell, which is lower than the $d$ subshell. This splitting is caused by two related phenomena: **Shielding** and **Penetration**.

* **Shielding:** Inner-shell electrons act as a "screen," partially canceling the positive charge of the nucleus. An outer electron does not "see" the full nuclear charge ($Z$); it feels a reduced **Effective Nuclear Charge ($Z_{eff}$)**.
* **Penetration:** This describes the ability of an orbital to have high probability density close to the nucleus. If an electron can "penetrate" the shield of inner electrons, it spends more time near the nucleus, feels a stronger $Z_{eff}$, and becomes more tightly bound (lower in energy).



### Radial Distribution Functions (RDF) and Sublevel Splitting

The reason an $s$ orbital is always lower in energy than a $p$ orbital of the same shell is visible in the **Radial Distribution Function (RDF)**. 

Even though a $2p$ electron might be "on average" closer to the nucleus than a $2s$ electron, the $2s$ orbital has a small secondary maximum (a "hump") very close to the nucleus. Because of this small region of high probability, the $2s$ electron penetrates the $1s$ core much more effectively than the $2p$ electron can.



:::{code-cell} python
:tags: ["remove-input"]
:label: rdf_plot_expanded
import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0, 20, 500)
# Radial Distribution Functions (r^2 * R^2)
rdf_2s = (r**2) * ( (2 - r) * np.exp(-r/2) )**2
rdf_2p = (r**2) * ( r * np.exp(-r/2) )**2

plt.figure(figsize=(8,4))
plt.plot(r, rdf_2s/np.max(rdf_2s), label='2s RDF', color='blue', lw=2)
plt.plot(r, rdf_2p/np.max(rdf_2p), label='2p RDF', color='red', linestyle='--', lw=2)

# Highlighting the penetration region
plt.fill_between(r, 0, rdf_2s/np.max(rdf_2s), where=(r < 2), color='blue', alpha=0.2, label='2s Penetration')

plt.title("Penetration: How s-orbitals 'get inside' the core")
plt.xlabel("Distance from Nucleus (r)")
plt.ylabel("Probability Density P(r)")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
:::

### The Order of Orbital Filling

This sublevel splitting is the reason why the energy levels of an atom don't simply follow the sequence $n=1, 2, 3...$. As $n$ increases, the splitting between subshells becomes so significant that the energy levels begin to overlap. 

For instance, the $4s$ orbital penetrates the inner electron shells so effectively that it actually drops below the $3d$ orbital in energy. This explains why the transition metals (the $d$-block) appear "delayed" on the periodic table—we fill $4s$ before $3d$.



---

### Moving to Electron Configurations

Now that we understand *why* the energies shift, we can apply this knowledge to build the electronic structure of the entire periodic table. By knowing the order of these energy levels, we can determine:

1.  **Ground State Configurations:** Using the Aufbau principle to "build up" the atom.
2.  **Spectroscopic Behavior:** Identifying "allowed" vs "forbidden" transitions. When an atom absorbs energy, an electron jumps from a lower energy subshell to a higher one. The gaps between these split subshells determine the exact frequencies of light an atom will interact with.

In the next section, we will look at the specific rules for filling these levels—**Aufbau**, **Pauli**, and **Hund**—and how they translate into the spectroscopic terms we observe in the lab.