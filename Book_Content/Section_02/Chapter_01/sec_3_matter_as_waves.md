## Matter as Waves

### De Broglie's Hypothesis
Matter as Waves: The De Broglie HypothesisBy the 1920s, scientists had grudgingly accepted a "dual nature" for light: it behaved like a wave in interference experiments but like a particle (photon) in the photoelectric effect.1 This led a young French aristocrat and physicist, Louis de Broglie, to ask a profound question based on symmetry: If light waves can behave like particles, can matter particles behave like waves?
The Derivation De Broglie proposed his hypothesis in his 1924 PhD thesis.2 While the rigorous derivation involves complex relativity, the logic can be simplified by combining the two major energy equations of the time—Einstein's relativity and Planck's quantum theory.Einstein established the energy of a particle with mass $m$ (approximated for light as an equivalent mass):$$E = mc^2$$Planck established the energy of a quantum of frequency $\nu$:$$E = h\nu$$De Broglie equated these energies ($mc^2 = h\nu$) and used the relationship that frequency is velocity divided by wavelength ($\nu = v / \lambda$, or $c / \lambda$ for light):$$mc^2 = \frac{hc}{\lambda}$$Solving for wavelength ($\lambda$):$$\lambda = \frac{h}{mc}$$De Broglie’s leap of genius was to replace the speed of light ($c$) with the speed of any material particle ($v$). Since mass times velocity is momentum ($p$), we arrive at the famous De Broglie Equation:$$\lambda = \frac{h}{mv} = \frac{h}{p}$$This equation tells us that all matter has a wavelength. However, because Planck's constant ($h \approx 6.626 \times 10^{-34} \text{ J}\cdot\text{s}$) is incredibly small, the wavelength is only observable for objects with extremely tiny momentum—like electrons.

Experimental Proof: Davisson-GermerDe Broglie's idea was radical and initially met with skepticism.3 However, only three years later, in 1927, Clinton Davisson and Lester Germer provided the proof.4 They fired a beam of electrons at a nickel crystal.5 If electrons were purely particles, they should have bounced off randomly. Instead, they observed a diffraction pattern—a phenomenon previously thought to be exclusive to waves (like X-rays).This discovery changed everything. It meant that electrons are not just orbiting "planets" but also "standing waves" confined around the nucleus. This wave property is not just a theoretical curiosity; we use it today in Electron Microscopes. Because high-speed electrons have wavelengths thousands of times shorter than visible light, they can resolve images at the atomic scale, far beyond the limits of traditional optical lenses.
:::{code-cell} python
:tags: ["remove-input"]
# --- START: Required for every block that imports from _ext ---
import sys
import os
from IPython.display import display, HTML

# Adjust the path based on file depth
try:
    cwd = os.getcwd()
    # e.g., use ("..", "..") for a file 2 levels deep.
    project_root = os.path.abspath(os.path.join(cwd, "..", "..", ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
except Exception as e:
    print(f"Error setting project path: {e}")

from _ext.interactive_qa import QuestionBlock
# --- END: Required for every block ---
questions = QuestionBlock()
questions.add_question(
    question_id="sec-02-ch-1-q07",
    question_text="If we don't see macroscopic objects like baseballs behaving like waves in everyday life, why did De Broglie argue that they still possess a wavelength?"
)
display(HTML(questions.render()))
:::


### Applying De Broglie to Bohr
De Broglie's hypothesis provided the crucial missing puzzle piece for the Bohr model. Bohr had simply *assumed* that electrons could only exist in specific energy levels where their angular momentum was quantized ($L = n \cdot \frac{h}{2\pi}$). He didn't know why; it just made the math work to match the hydrogen spectrum.

De Broglie offered the physical reason: **stability requires a standing wave.**

Imagine a guitar string plunked down so its two ends touch to form a circle. If you pluck it, a wave travels around the loop.
* If the circumference of the loop is exactly a whole number of wavelengths ($1\lambda, 2\lambda, 3\lambda...$), the wave will meet itself perfectly in phase after one rotation. The peaks align with peaks, and troughs align with troughs. This creates a stable **standing wave** that reinforces itself.
* If the circumference is *not* a whole number (e.g., $2.5\lambda$), the wave will return out of phase. The peak of the second pass will meet the trough of the first pass, causing destructive interference. The wave quickly cancels itself out.

#### The Derivation

We can mathematically prove that de Broglie's matter waves lead directly to Bohr's assumption.

1.  **The Condition for Stability:** For an electron wave to be a stable standing wave around a nucleus, the circumference of its orbit ($2\pi r$) must equal an integer number ($n$) of wavelengths ($\lambda$).
    $$2\pi r = n\lambda \quad (\text{where } n = 1, 2, 3...)$$

2.  **Substitute de Broglie's Idea:** We replace the wavelength $\lambda$ with de Broglie's equation ($\lambda = h/mv$).
    $$2\pi r = n \left( \frac{h}{mv} \right)$$

3.  **Rearrange:** Let's move the terms to get the electron's mass ($m$), velocity ($v$), and radius ($r$) on one side.
    $$mvr \cdot 2\pi = nh$$
    $$mvr = \frac{nh}{2\pi}$$

4.  **The Result:** In classical physics, $mvr$ is the **angular momentum ($L$)** of an object orbiting in a circle.
    $$L = n \left( \frac{h}{2\pi} \right)$$

This is exactly Bohr's quantization rule! An electron orbit is only stable if its geometry allows for a standing de Broglie wave. The mysterious integer $n$ in Bohr's equations is simply counting the number of wavelengths fitted around the nucleus.


:::{code-cell} python
:tags: [remove-input]
:label: debroglie_bohr_electron
import plotly.graph_objects as go
import numpy as np

def create_offline_standing_wave():
    fig = go.Figure()
    
    # Define the steps we want the slider to show
    # Integer steps = Constructive (Stable)
    # Half steps = Destructive (Unstable)
    n_values = [3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]
    
    # Base radius of the orbit
    r0 = 10
    amplitude = 2

    # We generate traces for EACH step, but hide them initially
    for i, n in enumerate(n_values):
        # We simulate 2 full rotations (0 to 4pi) to show the overlap
        theta = np.linspace(0, 4 * np.pi, 500)
        
        # Calculate radius: R = R0 + A * sin(n * theta)
        r = r0 + amplitude * np.sin(n * theta)
        
        # Split into First Pass (0-2pi) and Second Pass (2pi-4pi)
        half = len(theta) // 2
        
        # Determine if this n is stable (integer) or unstable
        is_stable = (n % 1) == 0
        status_text = "STABLE (Constructive Interference)" if is_stable else "UNSTABLE (Destructive Interference)"
        color_status = "green" if is_stable else "red"
        
        # Trace A: First Loop (Solid Blue)
        # Visible only if this is the "active" step
        fig.add_trace(go.Scatterpolar(
            r=r[:half],
            theta=np.degrees(theta[:half]),
            mode='lines',
            line=dict(color='blue', width=3),
            name='1st Rotation',
            visible=(i==0) # Only first n is visible at start
        ))
        
        # Trace B: Second Loop (Dashed Red)
        fig.add_trace(go.Scatterpolar(
            r=r[half:],
            theta=np.degrees(theta[:half]), # Plot against 0-360 again to show overlap
            mode='lines',
            line=dict(color='red', width=3, dash='dash'),
            name='2nd Rotation',
            visible=(i==0)
        ))

    # --- Create the Slider Steps ---
    steps = []
    for i, n in enumerate(n_values):
        # Calculate which traces should be turned on for this step
        # We have 2 traces per step (First Pass, Second Pass)
        # Total traces = 2 * len(n_values)
        
        # Create a visibility list of "False" for everything
        visible_array = [False] * (len(n_values) * 2)
        
        # Turn on the two traces corresponding to this step
        idx = i * 2
        visible_array[idx] = True     # The Blue Line
        visible_array[idx+1] = True   # The Red Line
        
        is_stable = (n % 1) == 0
        status = "✅ Stable" if is_stable else "❌ Unstable"
        
        step = dict(
            method="update",
            args=[{"visible": visible_array},
                  {"title": f"Electron Orbit n={n}<br><span style='font-size:16px; color:{'green' if is_stable else 'red'}'>{status}</span>"}],
            label=str(n)
        )
        steps.append(step)

    sliders = [dict(
        active=0,
        currentvalue={"prefix": "Wavelengths (n): "},
        pad={"t": 50},
        steps=steps
    )]

    # Layout details
    fig.update_layout(
        title=f"Electron Orbit n={n_values[0]}",
        polar=dict(
            radialaxis=dict(visible=False, range=[0, r0+amplitude+1]),
            angularaxis=dict(direction="counterclockwise")
        ),
        sliders=sliders,
        showlegend=True,
        width=600, height=600,
        template="plotly_white"
    )

    return fig

fig_wave = create_offline_standing_wave()
fig_wave.show()
:::
:::{code-cell} python
:tags: ["remove-input"]
# --- START: Required for every block that imports from _ext ---
import sys
import os
from IPython.display import display, HTML

# Adjust the path based on file depth
try:
    cwd = os.getcwd()
    # e.g., use ("..", "..") for a file 2 levels deep.
    project_root = os.path.abspath(os.path.join(cwd, "..", "..", ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
except Exception as e:
    print(f"Error setting project path: {e}")

from _ext.interactive_qa import QuestionBlock
# --- END: Required for every block ---
questions = QuestionBlock()
questions.add_question(
    question_id="sec-02-ch-1-q08",
    question_text="How does the concept of a standing wave provide a physical justification for the fixed orbits found in the Bohr model of the atom?"
)
display(HTML(questions.render()))
:::