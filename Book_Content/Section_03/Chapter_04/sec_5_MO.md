## 4.5 Molecular Orbital (MO) Theory: Diatomics

Up to this point, every theory we have discussed—Lewis, VSEPR, Valence Bond, and Hybrid Orbital—has shared one massive, fundamental assumption: **electrons are localized**. They assume that a bond is a static bridge built directly between two specific atoms, and the electrons in that bond belong exclusively to that specific pair of atoms.

This localized assumption is fantastic for predicting molecular geometry and basic connectivity. However, it completely fails to explain many observable physical and chemical properties of molecules, such as the colors they absorb, their magnetic properties, and how they conduct electricity.

To explain these phenomena, we must abandon the localized model entirely. We must transition to **Molecular Orbital (MO) Theory**.

### Breaking the Localized Assumption

The core premise of MO theory is profound but simple: **electrons do not belong to individual atoms or specific bonds; they belong to the entire molecule.**

When atoms come together to form a molecule, their atomic orbitals completely lose their individual identities. Instead of just overlapping a little bit at the edges (like in Valence Bond theory), the atomic wavefunctions of all the atoms combine to form entirely new, delocalized wavefunctions that stretch across the entire molecule. We call these new wavefunctions **molecular orbitals**.

### Constructing MOs: LCAO-MO

To mathematically construct these molecular orbitals, we use the exact same trick we used for hybrid orbitals: the **Linear Combination of Atomic Orbitals (LCAO)**. 

However, there is a critical difference. In hybridization, we mixed orbitals on the *same* atom. In MO theory, we mix wavefunctions from *different* atoms. 

Let's look at the simplest possible molecule: diatomic hydrogen (H₂). We have two hydrogen atoms, each with a 1*s* atomic orbital wavefunction. Because these are waves, they can interact in two distinct ways:

1.  **Constructive Interference (In-Phase):** The two wavefunctions add together. This builds up a massive amount of electron density directly between the two positively charged nuclei. The nuclei are highly attracted to this dense negative cloud, which acts as a strong glue, dropping the system into a deep potential energy well. This creates a **bonding molecular orbital**, which is *lower* in energy than the original atomic orbitals.
2.  **Destructive Interference (Out-of-Phase):** One wavefunction is mathematically subtracted from the other. They cancel each other out exactly halfway between the nuclei, creating a **node** (a region of zero electron density). With no electron "glue" between them, the two positively charged nuclei fiercely repel each other. This creates an **antibonding molecular orbital**, denoted with an asterisk (*). It is significantly *higher* in energy than the original atomic orbitals.



Just like with hybridization, we must obey the **law of conservation of orbitals**. We put two atomic orbitals in (one 1*s* from each hydrogen), so we get exactly two molecular orbitals out: one bonding and one antibonding.

### Filling the Orbitals

Once we have mapped out the energy levels of these new molecular orbitals, we fill them with the available valence electrons using the exact same quantum mechanical rules we used for single atoms:
* **Aufbau Principle:** Fill the lowest energy orbitals first (the bonding orbitals).
* **Pauli Exclusion Principle:** A maximum of two electrons per orbital, and they must have opposite spins.
* **Hund's Rule:** If you have multiple orbitals at the exact same energy level (degenerate orbitals), place one electron in each before pairing them up.

### Symmetry and Nomenclature: $\sigma$, $\pi$, $g$, and $u$

To keep track of all these new MOs, physical chemists classify them by their spatial symmetry:

* **$\sigma$ (Sigma) Symmetry:** If you look straight down the bond axis, the orbital looks like a cylinder. There is no node along the internuclear axis itself. Head-on overlap of *s* or *p* orbitals creates $\sigma$ MOs.
* **$\pi$ (Pi) Symmetry:** The electron density sits above and below the bond axis, with a nodal plane cutting straight through the nuclei. Side-by-side overlap of parallel *p* orbitals creates $\pi$ MOs.

We also classify MOs by how they behave if you invert them through the exact center of the molecule:
* ***Gerade* ($g$):** German for "even." If you start at any point in the orbital, draw a straight line through the center of the molecule, and come out the exact same distance on the other side, the wavefunction has the *exact same sign* (phase).
* ***Ungerade* ($u$):** German for "odd." If you do the same inversion trick, the wavefunction changes sign (from positive phase to negative phase). 

*(Note for biochemistry students: While $g$ and $u$ symmetry might seem like unnecessary physics jargon right now, these inversion symmetries strictly govern whether a molecule can absorb certain wavelengths of light—the very foundation of spectroscopy and fluorescence!)*

### The Triumph of MO Theory: The Oxygen Problem

To truly appreciate why we need MO theory despite its complexity, we have to look at its greatest triumph: explaining diatomic oxygen (O₂).

If you draw the Lewis structure for O₂, you get a double bond between the two oxygen atoms, with two lone pairs on each atom ($O=O$). Every single electron is perfectly paired up. According to Lewis, Valence Bond, and Hybrid theories, oxygen is **diamagnetic** (meaning it should be weakly repelled by a magnetic field). 

However, if you pour liquid oxygen between the poles of a strong magnet, it sticks. It bridges the gap between the magnets. Experimental reality proves that O₂ is **paramagnetic**, meaning it contains unpaired electrons. The localized models are completely, unequivocally wrong.

Let's look at the Molecular Orbital diagram for O₂. 



When the 2*p* orbitals of the two oxygen atoms combine, they form a $\sigma$ bonding orbital, two degenerate $\pi$ bonding orbitals, two degenerate $\pi^*$ antibonding orbitals, and a $\sigma^*$ antibonding orbital. 

When we fill these newly created molecular orbitals with oxygen's 12 valence electrons, we follow Aufbau and Pauli to fill the lower energy $\sigma$ and $\pi$ bonding orbitals. But when we reach the highest occupied energy level, we have two electrons left and *two* equal-energy $\pi_{2p}^*$ antibonding orbitals. 

According to **Hund's Rule**, those two electrons must go into separate orbitals with parallel spins. MO theory perfectly predicts that O₂ has exactly two unpaired electrons, beautifully explaining its magnetic properties where every other theory failed.