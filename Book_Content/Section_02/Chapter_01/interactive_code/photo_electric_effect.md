:::{code-cell} python
:tags: ["remove-input"]
:label: photo_electric
import plotly.graph_objects as go
import numpy as np

def plot_photoelectric():
    # Constants
    h = 6.626e-34 # Planck's constant
    eV_to_J = 1.602e-19
    
    # Frequency range (0 to 3 PetaHertz)
    freq = np.linspace(0, 3.0e15, 100) 
    
    # Metal: Sodium (Work function approx 2.28 eV)
    phi_eV = 2.28
    phi_J = phi_eV * eV_to_J
    
    # Calculate KE (KE = h*nu - Phi)
    # If KE < 0, it means no emission (set to 0 for plotting)
    ke_joules = (h * freq) - phi_J
    ke_ev = ke_joules / eV_to_J
    ke_plot = np.where(ke_ev > 0, ke_ev, 0) # Only show positive KE

    # Threshold Frequency location
    threshold_freq = phi_J / h
    
    fig = go.Figure()

    # The Kinetic Energy Line
    fig.add_trace(go.Scatter(
        x=freq, y=ke_plot,
        mode='lines',
        name='Kinetic Energy of Electron',
        line=dict(color='blue', width=3)
    ))

    # The Threshold Marker
    fig.add_trace(go.Scatter(
        x=[threshold_freq], y=[0],
        mode='markers+text',
        name='Threshold Frequency',
        text=['Threshold<br>(No ejection below this)'],
        textposition='bottom right',
        marker=dict(size=12, color='red')
    ))

    fig.update_layout(
        title="Photoelectric Effect: KE vs Frequency",
        xaxis_title="Frequency of Light (Hz)",
        yaxis_title="Electron Kinetic Energy (eV)",
        template="simple_white",
        annotations=[
            dict(
                x=2.5e15, y=6,
                xref="x", yref="y",
                text="Slope = Planck's Constant (h)",
                showarrow=True,
                arrowhead=1
            )
        ]
    )
    
    return fig

plot_photoelectric()
:::