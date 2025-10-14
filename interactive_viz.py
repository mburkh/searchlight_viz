import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# === Data Setup ===
xtab = {
    'Trump': [37, 24, 16, 23],
    'Harris': [23, 35, 17, 25]
}
index = ['Increase housing costs', 'Decrease housing costs', 'Have no impact on housing cost', 'Not sure']
df = pd.DataFrame(xtab, index=index)

# === Streamlit UI ===
st.set_page_config(page_title="Inclusionary Zoning Dashboard", layout="centered")
st.title("🗳️ How do Voters View Inclusionary Zoning?")
st.markdown("Interact with the visualization below to discover the perceived effect of inclusionary zoning on housing costs, based on 2024 presidential preferences.")

# === Build the Chart ===
fig = go.Figure()

# Common properties for bar style
common_bar_style = dict(
    orientation='h',
    textposition='auto',
    marker_line_color='#DDDDDD',  # Light gray edge
    marker_line_width=1.5,
)

# Add Trump data
fig.add_trace(go.Bar(
    y=df.index.tolist(),
    x=df['Trump'],
    name='Trump',
    marker_color='#BB4021',
    hovertemplate='%{x}% of Trump voters: <br>%{y}<extra></extra>',
    text=df['Trump'],
    offsetgroup=0,
    **common_bar_style
))

# Add Harris data
fig.add_trace(go.Bar(
    y=df.index.tolist(),
    x=df['Harris'],
    name='Harris',
    marker_color='#3A6FA1',
    hovertemplate='%{x}% of Harris voters: <br>%{y}<extra></extra>',
    text=df['Harris'],
    offsetgroup=1,
    **common_bar_style
))

# === Layout and Styling ===
fig.update_layout(
    barmode='group',
    bargap=0.15,         # Smaller gap between groups
    bargroupgap=0.0,     # No extra spacing between bars in a group
    height=400,
    plot_bgcolor='#f0f2f6',
    paper_bgcolor='#ffffff',
    title={
        'text': 'Inclusionary Zoning (IZ) and Housing Cost Perceptions',
        'y': 0.95,
        'x': 0.5,  # Center title
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(size=20, color='black', family='Arial')
    },
    legend=dict(
        title='2024 Presidential Vote',
        title_font=dict(size=13, color='black'),
        font=dict(size=12, color='black'),
        bgcolor='rgba(255,255,255,0.9)',
        bordercolor='black',
        borderwidth=1,
        x=1.0,
        y=1.0,
        xanchor='right',
        yanchor='top'
    ),
    xaxis=dict(
        title='Percentage',
        title_font=dict(size=14, color='black'),
        tickfont=dict(size=12, color='black'),
        tickmode='linear',
        dtick=5,
        gridcolor='#dddddd',
        gridwidth=1,
        showgrid=True,
        zeroline=False,
    ),
    yaxis=dict(
        title='Perceived Effect',
        title_font=dict(size=14, color='black'),
        tickfont=dict(size=12, color='black'),
    ),
    margin=dict(l=80, r=40, t=80, b=50),
)

# Plot
st.plotly_chart(fig, use_container_width=True)

st.markdown('')
