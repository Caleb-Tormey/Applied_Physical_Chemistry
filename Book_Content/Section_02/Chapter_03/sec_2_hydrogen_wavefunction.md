## Hydrogen Wavefunction

To find the allowed states for the electron in a hydrogen atom, we must solve the Time-Independent Schrödinger Equation (TISE) using the Coulomb potential:

:::{math}
:label: TISE_Hydrogen
\hat{H}\psi = E\psi
:::

Because the atom is spherical, it is far easier to work in **spherical coordinates** ($r, \theta, \phi$) than in standard Cartesian coordinates ($x, y, z$). In these coordinates, the Hamiltonian operator becomes quite complex, as it must account for the curvature of space:

:::{math}
:label: H_spherical
-\frac{\hbar^2}{2\mu} \nabla^2 \psi(r, \theta, \phi) - \frac{Ze^2}{4\pi\epsilon_0 r} \psi(r, \theta, \phi) = E \psi(r, \theta, \phi)
:::



### Separation of Variables
The "trick" to solving such a daunting equation is a technique called **separation of variables**. We assume the total wavefunction can be written as a product of independent functions:

:::{math}
\psi_{n,l,m_l}(r, \theta, \phi) = R_{n,l}(r) \times Y_{l,m_l}(\theta, \phi)
:::

1.  **The Radial Part ($R_{n,l}$):** This function describes how the electron density changes as you move away from the nucleus. It depends on the distance $r$ and is characterized by the quantum numbers $n$ and $l$. 
2.  **The Angular Part ($Y_{l,m_l}$):** Known as **Spherical Harmonics**, these functions describe the "surface" of the orbital. They depend on the angles $\theta$ and $\phi$ and are characterized by the quantum numbers $l$ and $m_l$.



### Solving the Radial Equation
When we separate the equation, we get a specific differential equation for the radial part. Its solutions are a combination of an exponential decay (the Gaussian-like tail) and **Associated Laguerre Polynomials**. 

This radial part is responsible for the **radial nodes** (circles of zero probability) that you see in cross-sections of $2s$ or $3p$ orbitals.

### Solving the Angular Equation (Spherical Harmonics)
The angular part of the equation is identical to the math used for the **Rigid Rotator** we studied in {ref}`rigid_rotator`. The solutions are the **Spherical Harmonics**. 

While the associated Legendre polynomials used to calculate these are mathematically advanced, you are already familiar with their physical shapes. These functions define the $s, p, d,$ and $f$ orbitals. For example:
* When $l=0$, $Y_{0,0}$ is a constant, resulting in a **spherical** s-orbital.
* When $l=1$, the $Y_{1,m_l}$ functions create the "dumbbell" shapes of p-orbitals.

### Table: Hydrogenic Radial Wavefunctions ($R_{n,l}$)

To simplify the expressions, we use the **Bohr Radius**, $a_0 = 52.9\text{ pm}$, which represents the most probable distance for an electron in the ground state of hydrogen. We also define $\sigma$ as a scaled distance: $\sigma = \frac{Zr}{a_0}$.

| Orbital | $n, l$ | Radial Wavefunction $R_{n,l}(r)$ |
| :--- | :--- | :--- |
| **1s** | $1, 0$ | $2 \left( \frac{Z}{a_0} \right)^{3/2} e^{-\sigma}$ |
| **2s** | $2, 0$ | $\frac{1}{2\sqrt{2}} \left( \frac{Z}{a_0} \right)^{3/2} (2 - \sigma) e^{-\sigma/2}$ |
| **2p** | $2, 1$ | $\frac{1}{2\sqrt{6}} \left( \frac{Z}{a_0} \right)^{3/2} \sigma e^{-\sigma/2}$ |
| **3s** | $3, 0$ | $\frac{1}{9\sqrt{3}} \left( \frac{Z}{a_0} \right)^{3/2} (6 - 6\sigma + \sigma^2) e^{-\sigma/3}$ |



---

### Connecting Math to Chemistry

When you look at these functions, you can see how the mathematical form dictates the physical behavior of the electron:

1.  **The Exponential Decay ($e^{-\sigma/n}$):** This "tail" ensures the wavefunction eventually goes to zero as $r$ increases. Notice that the denominator of the exponent is $n$; as the principal quantum number $n$ increases, the decay happens more slowly, meaning the orbital is physically larger and the electron is found further from the nucleus.
2.  **The Polynomial Term:** This is what creates **radial nodes**—spherical regions where the probability of finding the electron is zero. 
    * For the **1s** orbital, there are no roots in the polynomial (just a constant), so there are no nodes.
    * For the **2s** orbital, the term $(2 - \sigma)$ equals zero when $\sigma = 2$. This creates a single radial node.
    * **The General Rule:** The number of radial nodes is always given by $n - l - 1$.



[Image of radial nodes in 1s 2s and 3s orbitals]


### Radial Distribution Function (RDF)

While the radial wavefunction $R(r)$ tells us the amplitude, chemists are more interested in the **Radial Distribution Function**, $P(r) = 4\pi r^2 [R(r)]^2$. 

The $4\pi r^2$ term is a "volume element." Even though the wavefunction is strongest at the nucleus ($r=0$), the volume of a shell at that point is zero. Therefore, the RDF tells us the probability of finding the electron in a thin spherical shell at distance $r$.



As we will see in the next section on **Multielectron Atoms**, the small "humps" in the RDF for $s$ orbitals (representing regions where the electron is very close to the nucleus) allow them to **penetrate** inner electron shells. This penetration fundamentally changes the order of energy levels in the periodic table, making the $4s$ orbital lower in energy than the $3d$ orbital.

### Visualizing Spherical Harmonics
The applet below allows you to see the 3D shapes generated by these angular wavefunctions. Note how the quantum numbers $l$ and $m_l$ dictate the number of angular nodes and the orientation in space.

:::{include} interactive_code/spherical_harmonics.md
:::
**Note on Complex Functions:** Mathematically, the $m_l$ wavefunctions for $p$ and $d$ orbitals are complex (containing $i$). For example, $m_l = +1$ and $m_l = -1$ are not the "$\text{p}_x$" and "$\text{p}_y$" orbitals you know. To get real, observable shapes like $\text{p}_x$, we take **linear combinations** (sums and differences) of these complex wavefunctions.

By combining the spherical harmonics with linear combinations (yes literally just adding them together!) we can make the shapes of the atomic orbitals we learned all the way back in general chemistry! 

:::{include} interactive_code/orbital_visual.md
:::

### Hydrogenic Atoms
The solutions we find for Hydrogen ($Z=1$) can be generalized for any "hydrogenic" atom—any system with a nucleus and exactly one electron (e.g., $\text{He}^+$, $\text{Li}^{2+}$). The only major difference is that the energy scales by the square of the atomic number ($Z^2$) and the orbitals "contract" closer to the nucleus as $Z$ increases.

:::{math}
E_n = -\frac{Z^2 \mu e^4}{8 \epsilon_0^2 h^2 n^2} \approx -13.6 \text{ eV} \left( \frac{Z^2}{n^2} \right)
:::