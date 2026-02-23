(hydrogen_atom)=
## Hydrogen Atom

In previous chapters, we looked at idealized model systems like the particle in a box and the harmonic oscillator. As mentioned in {ref}`rigid_rotator`, the model that bridges us to the real world of chemistry is the rotation of a particle in three dimensions. 

A hydrogen atom is the simplest atom and, as far as a chemist is concerned, the simplest form of matter. To build a mathematical model of this system, we must first establish our coordinates and physical assumptions.

### Setting Up the Model: The Central Field Approximation

To solve the Schrödinger equation for an atom, we apply a few key simplifications:

1.  **The Fixed Nucleus:** Because the proton is nearly 2,000 times more massive than the electron, we assume the nucleus is stationary at the origin $(0,0,0)$. This is similar to how we treat the Sun as fixed when calculating the orbit of the Earth.
2.  **Spherical Symmetry:** The interaction between the nucleus and the electron is purely electrostatic. The potential energy, $V(r)$, depends only on the distance $r$ between the two particles, not the angle.



### From Bohr to Waves

You may recall the **Bohr Model** from general chemistry, which used the **de Broglie relation** to suggest that electrons exist as "stationary waves" circularizing the nucleus. Bohr proposed that only orbits where the circumference was an integer multiple of the wavelength ($n\lambda = 2\pi r$) were allowed. 

While Bohr's model correctly predicted the energy levels of hydrogen, it failed for larger atoms because it still treated the electron as a particle on a flat, circular track. In the true quantum model, we extend this "circular" wave idea into three-dimensional space. The electron is no longer a point on a ring; it is a three-dimensional wave-function "cloud" that exists in a spherical volume.

### The Electrostatic Potential

The "walls" that confine our electron aren't physical barriers like the Particle in a Box. Instead, the electron is trapped by the **Coulombic Potential**:

:::{math}
:label: Coulomb_potential
V(r) = -\frac{Ze^2}{4\pi\epsilon_0 r}
:::

* **$Z$**: The atomic number (1 for Hydrogen).
* **$e$**: The elementary charge.
* **$r$**: The distance from the nucleus.

As $r$ approaches infinity, the potential energy goes to zero (the electron is free). As $r$ gets closer to the nucleus, the potential energy becomes increasingly negative, "locking" the electron into a bound state.



This sets the stage for the **Hydrogen Wavefunction**. Just as the Particle in a Box gave us energy levels based on $n$, solving the Schrödinger equation with this $1/r$ potential will give us the three-dimensional shapes we know as **orbitals**.