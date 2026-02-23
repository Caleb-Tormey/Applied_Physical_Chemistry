:::{code-cell} python
:tags: ["remove-input"]
:label: uv_catastrophe
import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 6.626e-34  # Planck's constant (J s)
c = 3.0e8      # Speed of light (m/s)
k_B = 1.38e-23 # Boltzmann constant (J/K)
T = 5000       # Temperature (K)

# Wavelength range: 100 nm to 3000 nm
wavelengths_nm = np.linspace(100, 3000, 500)
wavelengths_m = wavelengths_nm * 1e-9

# Planck's Law (The Actual Physics)
exponent = (h * c) / (wavelengths_m * k_B * T)
planck_intensity = (2 * h * c**2 / wavelengths_m**5) * (1 / (np.exp(exponent) - 1))

# Rayleigh-Jeans Law (The Classical Prediction)
rj_intensity = (2 * c * k_B * T) / wavelengths_m**4

# Create Plot
plt.figure(figsize=(10, 6))

# Plot Planck
plt.plot(wavelengths_nm, planck_intensity, label="Planck's Law (Experiment)", color='blue', linewidth=3)

# Plot Rayleigh-Jeans
plt.plot(wavelengths_nm, rj_intensity, label="Rayleigh-Jeans (Classical)", color='red', linestyle='--', linewidth=3)

# Formatting
plt.ylim(0, max(planck_intensity) * 1.5) # Cut off the infinity
plt.xlabel("Wavelength (nm)", fontsize=12)
plt.ylabel("Intensity (Spectral Radiance)", fontsize=12)
plt.title("The Ultraviolet Catastrophe", fontsize=16)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)

# Annotate the "Catastrophe"
plt.text(1000, max(planck_intensity)*1.1, "Classical Theory matches\nat long wavelengths...", fontsize=12, color='darkred')
plt.arrow(950, max(planck_intensity)*1.1, -200, -0.2e13, color='darkred', head_width=30)

plt.text(250, max(planck_intensity)*1.4, "...but diverges to\ninfinity in the UV!", fontsize=12, color='darkred', ha='left')

# Save
plt.tight_layout()
plt.savefig('uv_catastrophe.png', dpi=150)
plt.show()

:::