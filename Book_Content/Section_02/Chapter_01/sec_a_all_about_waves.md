## The Nature of Waves

Before we can understand anything about quantum mechanics, we must first establish the language of waves. Whether it is sound, light, or an electron, all waves are described by three fundamental properties.

### 1. Fundamental Properties

* **Wavelength ($\lambda$, lambda):**
    This is the distance between two consecutive peaks (or troughs) of a wave.
    * *Physical Meaning:* In light, wavelength determines **color**. In sound, it determines **pitch**. In quantum mechanics, it determines **momentum**.
* **Frequency ($\nu$, nu):**
    This is the number of wave cycles that pass a fixed point in one second. Measured in Hertz (Hz).
    * *Physical Meaning:* Frequency is directly proportional to energy ($E = h\nu$). High frequency means high energy.
* **Amplitude ($A$):**
    This is the height of the wave from its center line to its peak.
    * *Physical Meaning:* Amplitude determines **intensity** or brightness. In quantum mechanics, the square of the amplitude ($\Psi^2$) determines the **probability** of finding a particle.

### Interactive Demonstration
Use the slider below to change the **Wavelength**.
* Observe how the **Frequency** (the number of waves that fit on the screen) changes automatically.
* Note that the **Amplitude** (the vertical height) stays constant, as it is independent of the other two.
:::{code-cell} python
:tags: [remove-input]
:label: wave_diagram
import numpy as np
import plotly.graph_objects as go

def create_wave_properties_plot():
    fig = go.Figure()

    # X-axis range
    x_max = 10
    x = np.linspace(0, x_max, 500)
    
    # We will slide through different Wavelengths (lambda)
    # Range: Short waves (0.5) to Long waves (5.0)
    wavelengths = np.linspace(1.0, 5.0, 20)
    amplitude = 1.0  # Kept constant to show independence
    
    # Pre-calculate traces for every slider step
    for i, wl in enumerate(wavelengths):
        
        # Calculate Wave Number (k) based on wavelength
        # y = A * sin( (2pi / lambda) * x )
        k = (2 * np.pi) / wl
        y = amplitude * np.sin(k * x)
        
        # --- Visual Calculation of Peaks ---
        # Peak 1 is at 1/4 of a wavelength (pi/2 phase)
        # Peak 2 is at 1/4 + 1 full wavelength
        peak1_x = wl / 4.0
        peak2_x = peak1_x + wl
        
        # Frequency (nu) is proportional to 1/lambda
        freq = 1.0 / wl

        # --- Trace 0: The Sine Wave ---
        fig.add_trace(go.Scatter(
            x=x, y=y,
            mode='lines',
            line=dict(color='#0074D9', width=3),
            name='The Wave',
            visible=(i==10) # Start with a middle value visible
        ))

        # --- Trace 1: Wavelength Marker (Crest to Crest) ---
        # A horizontal line connecting two peaks
        fig.add_trace(go.Scatter(
            x=[peak1_x, peak2_x], 
            y=[amplitude + 0.2, amplitude + 0.2], # Slightly above the wave
            mode='lines+markers+text',
            marker=dict(symbol='arrow-bar-up', size=10, angleref="previous"),
            line=dict(color='#FF4136', width=2),
            text=[f"", f"<b>λ = {wl:.2f}</b>"],
            textposition="top center",
            name='Wavelength',
            visible=(i==10)
        ))
        
        # --- Trace 2: Amplitude Marker (Center to Crest) ---
        # A vertical line at the first peak
        fig.add_trace(go.Scatter(
            x=[peak1_x, peak1_x], 
            y=[0, amplitude], 
            mode='lines+markers+text',
            marker=dict(symbol='line-ns', size=10),
            line=dict(color='#2ECC40', width=2, dash='dot'),
            text=["", "<b>Amp</b>"],
            textposition="middle right",
            name='Amplitude',
            visible=(i==10)
        ))

    # --- Create Sliders ---
    steps = []
    traces_per_step = 3 # Wave, Wavelength Marker, Amplitude Marker
    
    for i, wl in enumerate(wavelengths):
        freq = 1.0 / wl
        
        # Visibility Logic
        visible = [False] * (len(wavelengths) * traces_per_step)
        base = i * traces_per_step
        visible[base] = True     # Wave
        visible[base+1] = True   # Wavelength Marker
        visible[base+2] = True   # Amplitude Marker
        
        step = dict(
            method="update",
            args=[{"visible": visible},
                  {"title": f"<b>Wavelength (λ): {wl:.2f} units</b>  |  Frequency (ν): {freq:.2f} Hz"}],
            label=f"{wl:.1f}"
        )
        steps.append(step)

    sliders = [dict(
        active=10,
        currentvalue={"prefix": "Adjust Wavelength: "},
        pad={"t": 50},
        steps=steps
    )]

    fig.update_layout(
        sliders=sliders,
        title="Wave Properties: Wavelength vs Frequency",
        xaxis=dict(range=[0, x_max], title="Distance (x)"),
        yaxis=dict(range=[-1.8, 2.0], title="Amplitude (y)", showticklabels=False),
        height=500,
        showlegend=False,
        template="plotly_white",
        margin=dict(t=80)
    )
    
    # Static Annotation for "Amplitude" meaning
    fig.add_annotation(
        text="Amplitude = Intensity (Brightness)",
        xref="paper", yref="paper",
        x=0.02, y=0.05, showarrow=False,
        font=dict(size=12, color="#2ECC40")
    )

    return fig

fig_props = create_wave_properties_plot()
fig_props.show()
:::
### 2. Wave Interactions

Waves do not bounce off each other like billiard balls. When they meet, they pass through one another, their effects adding together. This is called the **Principle of Superposition**.

#### Interference
Interference occurs when two or more waves overlap. The result depends entirely on how the peaks and troughs align.

* **Constructive Interference:**
    When the peak of one wave aligns with the peak of another, they add together to form a wave with double the amplitude.
    * *Example:* Two speakers playing the same note perfectly in sync create a louder sound.
* **Destructive Interference:**
    When the peak of one wave aligns with the trough of another, they cancel each other out. If the amplitudes are equal, the result is zero—complete silence or darkness.
    * *Example:* Noise-canceling headphones work by generating a sound wave that is exactly "opposite" to the outside noise, canceling it out.



:::{code-cell} python
:tags: [remove-input]
:label: wave_interference
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_opacity_interference_plot():
    # Layout: 70% Wave Graph, 30% Intensity Meter
    fig = make_subplots(
        rows=1, cols=2,
        column_widths=[0.7, 0.3],
        subplot_titles=("<b>Wave Superposition</b>", "<b>Resultant Intensity (A²)</b>"),
        horizontal_spacing=0.1
    )

    # X-axis for the wave
    x = np.linspace(0, 4*np.pi, 500)
    
    # Phase shifts
    phi_values = np.linspace(0, 2*np.pi, 41) 

    # Pre-calculate traces
    for i, phi in enumerate(phi_values):
        
        # --- Physics Math ---
        y1 = np.sin(x)            
        y2 = np.sin(x + phi)      
        y_sum = y1 + y2           
        
        # Intensity Calculation
        # Max Amplitude = 2.0 -> Max Intensity = 4.0
        current_max_amp = np.max(np.abs(y_sum))
        intensity = current_max_amp**2
        
        # Calculate Opacity (Alpha)
        # 4.0 Intensity = 1.0 Opacity (Fully Opaque)
        # 0.0 Intensity = 0.0 Opacity (Fully Transparent/White)
        opacity_val = intensity / 4.0
        
        # Determine Status Text
        if np.isclose(phi, np.pi, atol=0.15):
            status_title = f"Phase: {phi:.2f} rad <br><span style='color:red; font-size:16px'><b>COMPLETE DESTRUCTIVE INTERFERENCE</b></span>"
        elif np.isclose(phi, 0, atol=0.15) or np.isclose(phi, 2*np.pi, atol=0.15):
            status_title = f"Phase: {phi:.2f} rad <br><span style='color:green; font-size:16px'><b>CONSTRUCTIVE INTERFERENCE</b></span>"
        else:
            status_title = f"Phase: {phi:.2f} rad"

        # --- LEFT PLOT: Waves ---
        
        # 0. Wave 1
        fig.add_trace(go.Scatter(
            x=x, y=y1, mode='lines',
            line=dict(color='blue', width=2, dash='dot'),
            name='Wave 1', visible=(i==0)
        ), row=1, col=1)

        # 1. Wave 2
        fig.add_trace(go.Scatter(
            x=x, y=y2, mode='lines',
            line=dict(color='red', width=2, dash='dot'),
            name='Wave 2', visible=(i==0)
        ), row=1, col=1)

        # 2. Resultant
        fig.add_trace(go.Scatter(
            x=x, y=y_sum, mode='lines',
            line=dict(color='purple', width=5),
            name='Resultant', visible=(i==0)
        ), row=1, col=1)

        # --- RIGHT PLOT: Intensity Meter ---
        
        # 3. The Static Reference Ring (Outline)
        fig.add_trace(go.Scatter(
            x=[0], y=[0],
            mode='markers',
            marker=dict(size=80, color='white', line=dict(color='black', width=2)),
            hoverinfo='skip',
            name='Max Possible', visible=(i==0), showlegend=False
        ), row=1, col=2)
        
        # 4. The Active Intensity Bulb (Variable Opacity)
        fig.add_trace(go.Scatter(
            x=[0], y=[0],
            mode='markers',
            marker=dict(
                size=78,            # Slightly smaller than ring to fit inside
                color='purple',     # Color stays purple
                opacity=opacity_val, # Opacity changes!
                line=dict(width=0)
            ),
            hoverinfo='text',
            hovertext=f"Intensity: {intensity:.2f}",
            name='Current Intensity', visible=(i==0), showlegend=False
        ), row=1, col=2)
        
        # 5. The Value Text (Smaller and positioned better)
        fig.add_trace(go.Scatter(
            x=[0], y=[-0.65], # Position inside/near bottom of ring
            mode='text',
            text=[f"<b>Intensity: {intensity:.1f}</b>"],
            textfont=dict(size=14, color="black"), # Smaller font
            visible=(i==0), showlegend=False
        ), row=1, col=2)

    # --- Sliders ---
    steps = []
    traces_per_step = 6 
    
    for i, phi in enumerate(phi_values):
        visible = [False] * (len(phi_values) * traces_per_step)
        base_idx = i * traces_per_step
        for offset in range(6):
            visible[base_idx + offset] = True
            
        # Title Logic
        if np.isclose(phi, np.pi, atol=0.15):
            title = f"Phase: {phi:.2f} rad <br><span style='color:red; font-size:16px'><b>COMPLETE DESTRUCTIVE INTERFERENCE</b></span>"
        elif np.isclose(phi, 0, atol=0.15) or np.isclose(phi, 2*np.pi, atol=0.15):
            title = f"Phase: {phi:.2f} rad <br><span style='color:green; font-size:16px'><b>COMPLETE CONSTRUCTIVE INTERFERENCE</b></span>"
        else:
            title = f"Phase: {phi:.2f} rad"

        steps.append(dict(
            method="update",
            args=[{"visible": visible}, {"title": title}],
            label=f"{phi:.1f}"
        ))

    sliders = [dict(
        active=0,
        currentvalue={"prefix": "Phase Shift: "},
        pad={"t": 60},
        steps=steps
    )]

    fig.update_layout(
        sliders=sliders,
        height=500,
        template="plotly_white",
        yaxis=dict(range=[-2.5, 2.5], title="Amplitude"),
        xaxis2=dict(visible=False, range=[-1, 1]),
        yaxis2=dict(visible=False, range=[-1, 1])
    )

    return fig

fig_opacity = create_opacity_interference_plot()
fig_opacity.show()
:::

#### Diffraction
Diffraction is the bending of waves around an obstacle or through a slit.

* **Particles:** If you throw baseballs at a wall with a hole in it, they either go straight through or bounce back. They do not bend.
* **Waves:** If you send a water wave through a narrow opening, the wave spreads out (diffracts) on the other side.

This property was the "smoking gun" in the Davisson-Germer experiment. Since electrons created a diffraction pattern when passing through a crystal, they *had* to be waves.