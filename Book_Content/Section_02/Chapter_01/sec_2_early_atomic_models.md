## The Early Atomic Models

Building upon the fundamental discoveries encountered in General Chemistry—such as J.J. Thomson’s identification of the electron via cathode rays and Rutherford’s realization that the atom’s mass is concentrated in a tiny, positive nucleus—we now shift our focus to how these subatomic particles are actually arranged. While we know the "building blocks" (protons, neutrons, and electrons), the early 20th century was defined by the struggle to explain the atom's stability and its interaction with light. These early models weren't just theoretical guesses; they were direct responses to spectroscopic evidence, specifically the discrete line spectra of elements that classical physics simply could not explain. Understanding these initial attempts is crucial, as they bridge the gap between simple particle physics and the complex wave-mechanics that define modern chemistry.

### The Thomson ``Plum Pudding'' Model

The "Plum Pudding" Solution to Neutrality By the early 20th century, experimental evidence had firmly established two contradictory facts: atoms contained discrete, negatively charged particles (electrons), yet bulk matter—like a block of metal—was electrically neutral. This created a structural puzzle: if negative charges are present, an equal amount of positive charge must exist to cancel them out, but where was it? Without evidence of a dense core, J.J. Thomson proposed that the positive charge was not a distinct particle, but rather a diffuse, continuous cloud that made up the bulk of the atom's volume. In this Plum Pudding Model, the tiny negative electrons were embedded within this positive sphere like raisins in a pudding or seeds in a watermelon. This arrangement successfully explained how atoms could be electrically neutral while allowing for electrons to be easily removed (ionization), assuming the positive mass was soft and spread thin rather than concentrated in a hard nucleus.

:::{code-cell}python
:tags: [remove-input]
:label: plum_pudding
import matplotlib.pyplot as plt
import numpy as np

def create_plum_pudding_spaced():
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Parameters
    main_radius = 4
    num_electrons = 15
    electron_radius = 0.3
    
    # Calculate spacing constraint
    electron_diameter = 2 * electron_radius
    # "Within 2 diameters" means we want the center-to-center distance 
    # to be AT LEAST 2 diameters.
    min_distance = 2 * electron_diameter
    
    # 1. Create the Diffuse Positive Charge Cloud (Large Red Circle)
    positive_cloud = plt.Circle((0, 0), main_radius, color='salmon', alpha=0.4)
    ax.add_patch(positive_cloud)
    
    # 2. Generate Non-Overlapping Positions
    electron_positions = []
    max_attempts = 5000  # Safety break to prevent infinite loops
    attempts = 0
    
    while len(electron_positions) < num_electrons and attempts < max_attempts:
        attempts += 1
        
        # Generate random position
        # r = R * sqrt(random()) ensures uniform distribution over the area
        r = (main_radius - electron_radius) * np.sqrt(np.random.rand())
        theta = 2 * np.pi * np.random.rand()
        
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        
        # Check distance against ALL existing electrons
        too_close = False
        for (ex, ey) in electron_positions:
            dist = np.sqrt((x - ex)**2 + (y - ey)**2)
            if dist < min_distance:
                too_close = True
                break
        
        # Only add if it passed the distance check
        if not too_close:
            electron_positions.append((x, y))
            
    if len(electron_positions) < num_electrons:
        print(f"Note: Only fit {len(electron_positions)} electrons with this spacing.")

    # 3. Draw the Electrons
    for x, y in electron_positions:
        electron = plt.Circle((x, y), electron_radius, color='gray', alpha=0.9, zorder=2)
        ax.add_patch(electron)
        ax.text(x, y, "-", color='white', ha='center', va='center', 
                fontsize=20, fontweight='bold', zorder=3)

    # 4. Add Text Annotations
    if electron_positions:
        # Find a suitable electron to point to (top-right looks best)
        # We sort by x+y to find the one closest to the top-right corner
        best_idx = np.argmax([x + y for x, y in electron_positions])
        target_x, target_y = electron_positions[best_idx]
        
        ax.annotate('Electrons (negative charge)', 
                    xy=(target_x, target_y), 
                    xytext=(main_radius + 1, main_radius),
                    arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle="arc3,rad=.2"),
                    fontsize=12, fontweight='bold')
                
    # Point to the cloud
    ax.annotate('Diffuse Positive Charge Cloud', 
                xy=(-main_radius/2, main_radius/2), 
                xytext=(-main_radius - 2, main_radius),
                arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle="arc3,rad=.2"),
                fontsize=12, fontweight='bold', ha='right')

    # Formatting
    ax.set_xlim(-main_radius - 3, main_radius + 3)
    ax.set_ylim(-main_radius - 1, main_radius + 2)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.title("Thomson's Plum Pudding Model", fontsize=16)
    
    plt.savefig('plum_pudding_spaced.png', bbox_inches='tight', dpi=300)

create_plum_pudding_spaced()
:::
### Rutherford's Gold Foil Experiment

If Thomson's "Plum Pudding" model were correct, the atom would be a soft, diffuse sphere of charge. When Ernest Rutherford fired heavy, positively charged alpha particles at a thin sheet of gold foil, he expected them to punch through the atoms like bullets through a fog, with only minor deflections. Instead, he observed something shocking: while most particles passed straight through, a small fraction were deflected at sharp angles, and some even bounced straight back toward the source. This result was impossible for a diffuse cloud to achieve. Rutherford was forced to conclude that the positive charge and nearly all the mass were not spread out, but concentrated in an incredibly small, dense center: the nucleus. The atom was not a pudding, but mostly empty space, with electrons orbiting a tiny, massive core.
### The Bohr Model
Rutherford’s nuclear model, while supported by the scattering data, faced a catastrophic problem. According to classical physics, a negatively charged electron orbiting a positive nucleus is accelerating; it should continuously radiate energy, lose speed, and spiral into the nucleus, causing the atom to collapse in a fraction of a second. Furthermore, this collapsing model suggests atoms should emit a continuous rainbow of light as they spiral, but experiments showed that hydrogen atoms emit light only at specific, discrete colors (the hydrogen line spectrum). Niels Bohr saved the nuclear model by applying the new idea of "quantization." He proposed that electrons are locked into specific, fixed orbits (energy levels) where they are stable and do not radiate energy. Light is emitted only when an electron "jumps" from a higher orbit to a lower one, releasing a photon with an energy that exactly matches the gap between the levels. This quantization perfectly explained the sharp lines in the hydrogen spectrum, proving that the laws of classical physics did not apply on the atomic scale.

:::{code-cell} python
:tags: [remove-input]
:label: bohr_model_light
import plotly.graph_objects as go
import numpy as np

def create_bohr_model():
    # Constants
    R_H = 1.097373e7  # Rydberg constant in m^-1
    
    # Define the visible transitions (Balmer Series: n_high -> n=2)
    # We map these to their approximate observable colors
    transitions = [
        {"ni": 3, "nf": 2, "color": "#FF0000", "name": "Red (H-alpha)", "wavelength": 656},
        {"ni": 4, "nf": 2, "color": "#00FFFF", "name": "Cyan (H-beta)", "wavelength": 486},
        {"ni": 5, "nf": 2, "color": "#0000FF", "name": "Blue (H-gamma)", "wavelength": 434},
        {"ni": 6, "nf": 2, "color": "#7F00FF", "name": "Violet (H-delta)", "wavelength": 410},
    ]

    fig = go.Figure()

    # --- 1. Draw the Orbits (Static Background) ---
    # Orbits radius scales with n^2
    max_n = 6
    radii = [n**2 for n in range(1, max_n + 1)]
    
    for i, r in enumerate(radii):
        n = i + 1
        fig.add_shape(type="circle",
                      xref="x", yref="y",
                      x0=-r, y0=-r, x1=r, y1=r,
                      line_color="lightgrey", line_dash="dot")
        # Label the orbit
        fig.add_annotation(x=r, y=0, text=f"n={n}", showarrow=False, xanchor="left", font=dict(color="gray"))

    # Nucleus
    fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(size=15, color='orange'), name='Nucleus'))

    # --- 2. Create Traces for Each Transition ---
    # We will toggle the visibility of these using the slider
    
    for t in transitions:
        ni, nf = t['ni'], t['nf']
        ri = ni**2
        rf = nf**2
        wl = t['wavelength']
        color = t['color']
        
        # A. The Electron starting position (at top of orbit)
        # We'll visualize the "jump" with an arrow
        
        # Arrow Trace (Scatter with arrow marker or just an annotation? 
        # Annotations are easier for arrows in Plotly layout, but hard to toggle with sliders.
        # We will use a Scatter line that looks like a path)
        
        fig.add_trace(go.Scatter(
            x=[0, 0], 
            y=[ri, rf],
            mode='lines+markers',
            line=dict(color=color, width=4, dash='dash'),
            marker=dict(size=10, symbol="arrow-down", angleref="previous"),
            name=f"Transition n={ni}->{nf}",
            visible=False,  # Hidden by default
            hoverinfo='text',
            text=f"Photon Emitted: {wl} nm"
        ))
        
        # B. The Spectrum Marker (The tick mark on the bottom bar)
        # We map 400-700nm to an x-axis range for the spectrum bar
        # Let's place the spectrum bar visually at y = -50 roughly
        spectrum_x = np.interp(wl, [380, 750], [-30, 30])
        
        fig.add_trace(go.Scatter(
            x=[spectrum_x], 
            y=[-45], # Position below the atom
            mode='markers+text',
            marker=dict(symbol="triangle-up", size=15, color=color, line=dict(width=2, color='white')),
            text=[f"{wl} nm"],
            textposition="bottom center",
            visible=False,
            showlegend=False
        ))

    # --- 3. The Spectrum Background (Static) ---
    # Draw a colored rectangle at the bottom to represent visible light
    # We cheat a bit and just draw colored bands
    colors = ['#7F00FF', '#0000FF', '#00FFFF', '#00FF00', '#FFFF00', '#FFA500', '#FF0000']
    x_positions = np.linspace(-30, 30, len(colors))
    
    for i in range(len(colors)-1):
        fig.add_shape(type="rect",
            xref="x", yref="y",
            x0=x_positions[i], y0=-50,
            x1=x_positions[i+1], y1=-40,
            fillcolor=colors[i], opacity=0.8, line_width=0,
            layer="below"
        )
    
    fig.add_annotation(x=0, y=-52, text="Visible Spectrum", showarrow=False, yanchor="top")

    # --- 4. Interactivity: Sliders ---
    steps = []
    # Trace 0 is Nucleus (always visible)
    # Traces 1,2 are Transition 1
    # Traces 3,4 are Transition 2, etc.
    
    # Pre-calculate which traces belong to which step
    # 0 is Nucleus. Pairs start at 1.
    num_transitions = len(transitions)
    
    for i in range(num_transitions):
        step = {
            "method": "update",
            "args": [{"visible": [False] * len(fig.data)},
                     {"title": f"Transition: n={transitions[i]['ni']} → n={transitions[i]['nf']} ({transitions[i]['name']})"}],
            "label": f"n={transitions[i]['ni']} -> 2"
        }
        # Set Nucleus (0) to True
        step["args"][0]["visible"][0] = True
        
        # Set the specific transition pair to True
        # Pair 1 is at index 1 and 2. Pair 2 is at 3 and 4...
        idx_start = 1 + (i * 2)
        step["args"][0]["visible"][idx_start] = True     # The Arrow
        step["args"][0]["visible"][idx_start+1] = True   # The Spectrum Marker
        
        steps.append(step)

    sliders = [dict(
        active=0,
        currentvalue={"prefix": "Select Jump: "},
        pad={"t": 50},
        steps=steps
    )]
    
    # Initialize with the first transition visible
    fig.data[0].visible = True
    fig.data[1].visible = True
    fig.data[2].visible = True

    fig.update_layout(
        sliders=sliders,
        title="Bohr Model: The Hydrogen Balmer Series",
        xaxis=dict(range=[-40, 40], visible=False),
        yaxis=dict(range=[-60, 45], visible=False, scaleanchor="x", scaleratio=1),
        plot_bgcolor="white",
        width=700, height=700,
        showlegend=False
    )

    return fig

fig = create_bohr_model()
fig.show()
:::