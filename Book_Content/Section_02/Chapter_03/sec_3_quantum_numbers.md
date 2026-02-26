(quantum_numbers)=
## Quantum Numbers

The solutions to the Schrödinger equation for atoms naturally produce four quantum numbers: $n$, $l$, $m_l$, and $m_s$. These are not arbitrary; they emerge from the mathematical boundary conditions required to keep the wavefunction "well-behaved." They act as the "address" of an electron and explain the underlying structure of the Periodic Table.

### 1. The Principal Quantum Number ($n$)
The number $n = 1, 2, 3, \ldots$ defines the **Principal Shell**. It primarily determines the **energy** and the average distance of the electron from the nucleus. 

* **Energy Scale:** In the Hydrogen atom, the energy depends solely on $n$: $E_n = -13.6 \text{ eV} / n^2$. This means all orbitals with the same $n$ (like $2s$ and $2p$) are **degenerate** (equal in energy).
* **Spectroscopic Shells:** Historically, these shells are also labeled with letters used in X-ray spectroscopy:
    * $n=1 \rightarrow \mathbf{K}$ shell
    * $n=2 \rightarrow \mathbf{L}$ shell
    * $n=3 \rightarrow \mathbf{M}$ shell
    * $n=4 \rightarrow \mathbf{N}$ shell

### 2. The Orbital Angular Momentum Quantum Number ($l$)
The number $l = 0, 1, \dots, (n-1)$ defines the **Subshell** and describes the **shape** of the orbital. This quantum number arises from the angular part of the Schrödinger equation (the Spherical Harmonics). 

It is important to note that the letter designations we use today ($s, p, d, f$) actually predated the quantum mechanical model. Early experimentalists observed specific patterns in the lines of atomic emission spectra and named the series based on their visual appearance. These names were later adopted to identify the specific orbitals:

* $l = 0 \rightarrow \mathbf{s}$ stands for **sharp**: Lines that were fine and well-defined.
* $l = 1 \rightarrow \mathbf{p}$ stands for **principal**: The most prominent and intense lines in the spectrum.
* $l = 2 \rightarrow \mathbf{d}$ stands for **diffuse**: Lines that appeared blurred or spread out.
* $l = 3 \rightarrow \mathbf{f}$ stands for **fundamental**: Lines that occurred at lower frequencies.



[Image of hydrogen emission spectrum with labeled series]


Beyond $l=3$, the letters simply continue alphabetically ($g, h, i \dots$), but the first four remain a tribute to the era of observational spectroscopy.



### 3. The Magnetic Quantum Number ($m_l$)
This number $m_l = -l, \dots, +l$ defines the **orientation** of the orbital in three-dimensional space. For a given subshell $l$, there are $(2l + 1)$ possible values of $m_l$. For example, a $p$-subshell ($l=1$) has three orientations ($m_l = -1, 0, 1$), which we represent as $p_x, p_y,$ and $p_z$.

### 4. The Spin Quantum Number ($m_s$)
Unlike the first three, $m_s = \pm 1/2$ does not come from the spatial Schrödinger equation but is an intrinsic property of the electron. It is an intrinsic form of angular momentum. Because an electron has charge, this "spin" creates a tiny magnetic field, which is why electrons respond to external magnetic fields.



---

### Interactive: Quantum Number Validator

Use the tool below to test different combinations of quantum numbers. It will check if your set is "Allowed" according to the rules of the Schrödinger equation and tell you which orbital it represents.

:::{include} interactive_code/qm_checker.md
:::
