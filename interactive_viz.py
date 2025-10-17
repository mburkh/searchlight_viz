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
    # text=df['Trump'],
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
    # text=df['Harris'],
    offsetgroup=1,
    **common_bar_style
))

# Add citation as an annotation
fig.add_annotation(
    text="Data: Tavern Research, 2025",
    xref="paper", yref="paper",
    x=0, y=-0.15,
    showarrow=False,
    font=dict(size=10, color="gray"),
    align="left"
)

# === Layout and Styling ===
fig.update_layout(
    barmode='group',
    bargap=0.15,
    bargroupgap=0.0,
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
        title='Percentage (%) of Voter Base',
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
        title='Perceived Effect on Housing Costs',
        title_font=dict(size=14, color='black'),
        tickfont=dict(size=12, color='black'),
    ),
    margin=dict(l=80, r=40, t=80, b=80),
)

# Plot
st.plotly_chart(fig, use_container_width=True)

st.markdown("""Inclusionary Zoning (IZ), a policy requiring home developers to reserve units for low-income households, speaks to a broader, fundamental divide between liberal and conservative voters. In theory, the policy would be popular among liberals who tend to favor government intervention that increases the amount affordable housing and reduces results of gentrification. Alternatively, the policy would be unpopular among conservatives who tend to vote for increased property rights and the deregulation of the market. 
            
This distinction produced opposite poll results. Of all Harris voters polled, **35%** believe IZ decreases housing costs while **23%** believe it increases housing costs. Contrarily, **37%** of all Trump voters polled believe IZ increases housing costs while only **24%** believe it decreases housing costs. The remainder of each voter base is either *Not sure* of the effects of IZ or believe it will *Have no impact on housing costs*. A politician appealing to the supermajority would be wise to avoid making IZ a center point of their platform and should instead focus on more universally accepted policies like requiring local governments to approve projects that meet predetermined standards or making permits easier to acquire.

These results are encapsulated by a horizontal grouped bar graph displaying question results for Harris and Trump voters side-by-side to highlight similarities and differences in perception. Each group is distinguished intuitively by its candidate’s respective party color. A title, axis labels, and a legend clarify the data and the meaning of each response. A citation was also included. The graph itself is interactive and easily shareable, courtesy of the Streamlit Community Cloud, to increase engagement. This also allows the exact percentages to be displayed by hovering over each bar and gives users the option to isolate the results by toggling the legend.""")
