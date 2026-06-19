
import streamlit as st
import plotly.express as px
import pandas as pd

# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------
st.set_page_config(
    page_title="Supply Chain Ops",
    page_icon="📦",
    layout="wide"
)

# --------------------------------------------------
# CSS PERSONALIZADO
# --------------------------------------------------
st.markdown("""
<style>

.main {
    background-color: #F8F9FF;
}

.block-container{
    padding-top: 1.5rem;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
}

.metric-title{
    color:#6B7280;
    font-size:14px;
    font-weight:600;
    text-transform: uppercase;
}

.metric-value{
    font-size:36px;
    font-weight:bold;
}

.title-main{
    font-size:32px;
    font-weight:700;
    color:#0B1C30;
}

.alert-card{
    background:#fff;
    padding:15px;
    border-left:5px solid #BA1A1A;
    border-radius:10px;
    margin-bottom:10px;
    box-shadow:0 2px 5px rgba(0,0,0,.05);
}

.star-card{
    background:white;
    border-radius:20px;
    padding:30px;
    border:1px solid #E2E8F0;
    box-shadow:0 2px 6px rgba(0,0,0,0.05);
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
col1, col2 = st.columns([8,2])

with col1:
    st.markdown(
        '<p class="title-main">📦 Supply Chain Ops</p>',
        unsafe_allow_html=True
    )

with col2:
    st.button("🔔 Notificaciones")

st.divider()

# --------------------------------------------------
# KPIs
# --------------------------------------------------

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
        <div class="metric-title">Fill Rate</div>
        <div class="metric-value" style="color:#0058BE;">
            98.5%
        </div>
        <span style="color:green;font-weight:bold;">▲ +0.4%</span>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <div class="metric-title">Total Demand</div>
        <div class="metric-value">
            1,003
        </div>
        <small>Across 12 global regions</small>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        <div class="metric-title">Avg Inventory</div>
        <div class="metric-value">
            184.25
        </div>
        <span style="color:red;font-weight:bold;">▼ -2.1%</span>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# --------------------------------------------------
# BENTO GRID
# --------------------------------------------------

left, right = st.columns([2,1])

# --------------------------------------------------
# PRODUCTO ESTRELLA
# --------------------------------------------------

with left:

    st.markdown("""
    <div class="star-card">
        <h2>⭐ SKU10 (Skincare)</h2>

        <p>
        Precision formulated advanced serum.
        Currently leading all categories in MAPE
        accuracy and delivery velocity.
        </p>

        <hr>

        <b>Current Status:</b> 🟢 Healthy Supply<br>
        <b>Next Shipment:</b> Oct 14, 08:00

    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# DISTRIBUCIÓN
# --------------------------------------------------

with right:

    st.markdown("### Sales Distribution")

    data = pd.DataFrame({
        "SKU":[
            "SKU1","SKU2","SKU3","SKU10",
            "SKU5","SKU6","SKU7","SKU8"
        ],
        "Sales":[40,35,45,95,50,30,25,38]
    })

    fig = px.bar(
        data,
        x="SKU",
        y="Sales"
    )

    fig.update_layout(
        height=350,
        showlegend=False,
        margin=dict(l=10,r=10,t=10,b=10)
    )

    st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# ALERTAS
# --------------------------------------------------

st.markdown("## 🚨 Operational Alerts")

st.markdown("""
<div class="alert-card">
<b>Segment 2: Potential Stockout Risk</b><br>
Low inventory detected in regional hub SE-4 (Stockholm).<br>
<b>ETA:</b> 48h
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="alert-card">
<b>SKU15: Lead Time Variance</b><br>
Supplier delivery delay +12% from baseline in Segment 2.<br>
<b>ETA:</b> 72h
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:
    st.title("Navigation")

    menu = st.radio(
        "",
        [
            "Dashboard",
            "Forecast",
            "Simulation",
            "Inventory"
        ]
    )

    st.info(f"Current section: {menu}")