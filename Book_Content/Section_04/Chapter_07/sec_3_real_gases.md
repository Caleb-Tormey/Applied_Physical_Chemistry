## 7.3 Real Gases: The Chapter 6 Payoff

The Ideal Gas Law works perfectly when gas molecules are hot and far apart. But what happens when we push a system to its physical limits? 

If we compress a gas to extremely high pressures (forcing the molecules incredibly close together) or cool it to extremely low temperatures (slowing the molecules down so they linger next to each other), the Ideal Gas Law spectacularly fails. The calculated pressure and the actual measured pressure no longer match. 

Reality sets in. To accurately model a real system, we have to fix the two massive assumptions of the ideal model. We do this using the **Van der Waals Equation of State**:

$$\left(P + a\frac{n^2}{V^2}\right)(V - nb) = nRT$$

Notice that this is just the Ideal Gas Law ($P_{ideal}V_{ideal} = nRT$) with two specific correction factors bolted onto the pressure and volume terms. Let's look at exactly how these corrections tie directly back to the intermolecular forces we learned in Chapter 6.

### The $b$ Parameter: Excluded Volume and Sterics

In the ideal model, we assumed molecules take up zero space. The volume ($V$) in the ideal gas law is supposed to be the *free, empty space* available for molecules to fly around in.

However, real molecules have physical size. As you compress a gas, the physical volume of the molecules themselves starts to take up a significant fraction of the container. 

To fix this, we must subtract the volume actually occupied by the molecules from the total volume of the container. This is the $(V - nb)$ term.
* $n$ is the number of moles.
* $b$ is a measured constant specific to each molecule that represents its physical size. A massive protein has a huge $b$ value; a tiny helium atom has a microscopic $b$ value. 

**The Physics Tie-In:** The $b$ parameter is the macroscopic manifestation of the **Pauli Exclusion Principle** and the incredibly steep $+1/r^{12}$ repulsive wall of the Lennard-Jones potential. Because electron clouds cannot overlap, each molecule claims a specific sphere of "excluded volume" that no other molecule can enter.

### The $a$ Parameter: Intermolecular Attractions

In the ideal model, we assumed molecules don't pull on each other. 

In reality, gas molecules experience London dispersion forces, and if they are polar, Keesom and Debye forces. Imagine a gas molecule flying toward the wall of a container, about to collide and register a unit of Pressure. As it approaches the wall, the other gas molecules behind it exert a $1/r^6$ attractive pull on it. 

This collective backward pull acts like a parachute, slowing the molecule down just a fraction of a second before it hits the wall. Because it hits the wall with less force, the **measured pressure of a real gas is always lower than the ideal pressure.**

To use the ideal $nRT$ math, we have to artificially add that "lost" pressure back in. This is the $+ a\frac{n^2}{V^2}$ term.
* $(n/V)^2$ represents the density of the gas (how close the molecules are).
* $a$ is a measured constant specific to each molecule that represents the strength of its intermolecular forces. Water has a massive $a$ value due to hydrogen bonding; nonpolar methane has a much smaller $a$ value.

### Biochemical Relevance: Macromolecular Crowding

You might still be thinking, "This is great for engines, but I study cells." 

The concept of the $b$ parameter (excluded volume) is currently one of the hottest topics in biophysics! Introductory biology often depicts the inside of a cell (the cytosol) as a watery soup with a few proteins floating around. 

In reality, the cytosol is crammed full of ribosomes, cytoskeleton filaments, mRNA, and millions of folded proteins. Up to 40% of the physical volume of a cell is solid biomatter. This is called **macromolecular crowding**. 

Because of this massive excluded volume ($nb$), the *actual* free water volume available for a substrate to find an enzyme is much smaller than the total volume of the cell. This physical crowding drastically alters the thermodynamics of protein folding and chemical equilibrium, proving that you cannot treat the inside of a cell like a dilute, ideal solution!