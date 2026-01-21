## The Uncertainty Principle

In Classical Physics, there is no limit to how precisely we can know the world. If we had perfect measuring tools, we could theoretically know the exact position and exact momentum of every particle in the universe simultaneously.

Quantum Mechanics shatters this idea. In 1927, Werner Heisenberg formulated the **Uncertainty Principle**, which states that there is a fundamental limit to the precision with which certain pairs of physical properties, such as position ($x$) and momentum ($p$), can be known.

$$\sigma_x \sigma_p \ge \frac{h}{4\pi}$$

Where $\sigma_x$ is the standard deviation (uncertainty) in position and $\sigma_p$ is the uncertainty in momentum.

#### It is Not a Measurement Problem
It is crucial to understand that this is **not** a limitation of our technology. It is not caused by "clumsy" microscopes bumping into the particle. Even if you had a magical, perfect measuring device, this uncertainty would still exist. It is a fundamental property of nature itself.

Mathematically, this arises because the operators for position and momentum **do not commute**. In linear algebra, $A \times B$ is usually equal to $B \times A$. In Quantum Mechanics, the order matters: $\hat{x}\hat{p} \neq \hat{p}\hat{x}$. This mathematical quirk dictates that these two properties cannot share a simultaneous "eigenstate" (a state of definite reality).

#### The Wave Explanation: Position vs. Momentum
We can understand this intuitively by looking at the wave nature of matter.
* **Momentum** is defined by wavelength ($p = h/\lambda$). To know a particle's momentum perfectly, it must have a single, perfect wavelength. A perfect sine wave, however, extends infinitely in both directions. If the wave is everywhere, the **position is completely unknown**.
* **Position** is defined by localization. To make a wave "localized" (so we know where the particle is), we must construct a **Wave Packet**. We do this by adding together many different waves with slightly different wavelengths.
    * Where the peaks align, they add up (constructive interference).
    * Everywhere else, they cancel out (destructive interference).

**The Trade-off:**
To make the position very narrow (a sharp spike), you must stack up a **huge range** of different wavelengths (momentums).
* Narrow Position $\rightarrow$ Wide range of Momentums.
* Precise Momentum $\rightarrow$ Wide range of Positions.

There are other "Conjugate Pairs" that behave this way, such as **Energy and Time** ($\Delta E \Delta t \ge h/4\pi$), but position and momentum remain the most famous example.

:::{code-cell} python
:tags: [remove-input]
:label: uncertainty_principle
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_uncertainty_visualizer_v2():
    # Create subplots
    fig = make_subplots(rows=2, cols=1, 
                        subplot_titles=("<b>Momentum Space</b><br>(Ingredients: Range of Wavelengths Used)", 
                                        "<b>Position Space</b><br>(Result: The Wave Packet)"),
                        vertical_spacing=0.2)

    # X-axis for Position Space
    x = np.linspace(-20, 20, 1000)
    
    # Sigma K values (Spread of Momentum)
    # Small = Precise Momentum, Large = Uncertain Momentum
    sigma_k_values = [0.5, 1.0, 2.0, 3.0, 5.0]
    
    # Pre-calculate traces
    for i, sigma_k in enumerate(sigma_k_values):
        
        # --- 1. Momentum Distribution (Gaussian) ---
        k_axis = np.linspace(-10, 10, 500)
        momentum_dist = np.exp(-k_axis**2 / (2 * sigma_k**2))
        
        fig.add_trace(go.Scatter(
            x=k_axis, y=momentum_dist,
            mode='lines', fill='tozeroy',
            line=dict(color='orange', width=2),
            name='Momentum Range (Delta p)',
            visible=(i==2) 
        ), row=1, col=1)

        # --- 2. Position Wave Packet ---
        sigma_x = 1.0 / sigma_k # Heisenberg relationship
        
        # Envelope and Wave
        envelope = np.exp(-x**2 / (2 * sigma_x**2))
        psi = envelope * np.cos(5 * x)
        
        fig.add_trace(go.Scatter(
            x=x, y=psi,
            mode='lines',
            line=dict(color='teal', width=2),
            name='Wave Packet',
            visible=(i==2)
        ), row=2, col=1)
        
        # --- 3. The Red "Uncertainty" Line ---
        # We place this slightly below the wave
        fig.add_trace(go.Scatter(
            x=[-sigma_x, sigma_x], y=[-0.4, -0.4],
            mode='lines+markers+text',
            marker=dict(symbol='line-ns', size=12),
            line=dict(color='red', width=3),
            text=["", f"<b>Δx = {sigma_x:.2f}</b>"], # Label the uncertainty value
            textposition="bottom center",
            name='Position Uncertainty (Delta x)',
            visible=(i==2)
        ), row=2, col=1)

    # --- Sliders ---
    steps = []
    traces_per_step = 3
    
    for i, sigma_k in enumerate(sigma_k_values):
        visible = [False] * (len(sigma_k_values) * traces_per_step)
        base_idx = i * traces_per_step
        visible[base_idx] = True
        visible[base_idx+1] = True
        visible[base_idx+2] = True
        
        step = dict(
            method="update",
            args=[{"visible": visible}],
            label=f"{sigma_k}"
        )
        steps.append(step)

    sliders = [dict(
        active=2,
        currentvalue={"prefix": "Momentum Spread (Delta p): "},
        pad={"t": 50},
        steps=steps
    )]

    fig.update_layout(
        sliders=sliders,
        title="<b>Heisenberg Uncertainty Principle</b><br>Narrow Position requires Wide Momentum",
        height=700,
        showlegend=False,
        template="plotly_white",
        margin=dict(t=100)
    )
    
    # Axis labels and range fixing
    fig.update_yaxes(showticklabels=False, row=1, col=1)
    fig.update_yaxes(range=[-1.0, 1.2], showticklabels=False, row=2, col=1)
    
    # Add a static annotation explaining the Red Line if needed
    fig.add_annotation(
        text="The Red Line is the standard deviation (Δx).<br>This is the region where the particle is likely found.",
        xref="paper", yref="paper",
        x=0.5, y=-0.1, showarrow=False,
        font=dict(size=12, color="gray")
    )

    return fig

fig_v2 = create_uncertainty_visualizer_v2()
fig_v2.show()
:::