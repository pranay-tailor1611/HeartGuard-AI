import streamlit as st
import pandas as pd
import plotly.express as px
from components import load_css, render_top_navbar, render_sidebar, render_footer
from utils.ml_utils import load_dataset

st.set_page_config(page_title="Dashboard | CardioPulse AI", page_icon="📊", layout="wide")
load_css()
render_top_navbar()
render_sidebar()

st.markdown("## Analytics Dashboard")
st.caption("Visualizing distribution patterns and clinical metrics from 918 patient records (`heart.csv`).")

df_heart = load_dataset()

if df_heart is None:
    st.error("heart.csv dataset not found in directory.")
else:
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Evaluated Patients", len(df_heart))
    m2.metric("Disease Rate", f"{round((df_heart['HeartDisease'].sum()/len(df_heart))*100, 1)}%")
    m3.metric("Average Patient Age", f"{round(df_heart['Age'].mean(), 1)} Yrs")
    m4.metric("Mean Cholesterol", f"{round(df_heart['Cholesterol'].mean(), 1)} mg/dl")

    st.markdown("<br/>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### 1. Heart Disease Prevalence by Age Group")
        fig_age = px.histogram(
            df_heart, x="Age", color="HeartDisease", barmode="group",
            color_discrete_map={0: "#22C55E", 1: "#EF4444"},
            template="plotly_white"
        )
        fig_age.update_layout(height=340, margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig_age, use_container_width=True)

    with c2:
        st.markdown("#### 2. Cholesterol vs Resting BP Scatter")
        fig_scatter = px.scatter(
            df_heart, x="RestingBP", y="Cholesterol", color="HeartDisease",
            size="Oldpeak", hover_data=["Age", "Sex"],
            color_discrete_map={0: "#22C55E", 1: "#EF4444"},
            template="plotly_white"
        )
        fig_scatter.update_layout(height=340, margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig_scatter, use_container_width=True)

    c3, c4 = st.columns(2)
    with c3:
        st.markdown("#### 3. Chest Pain Type vs Risk Prevalence")
        fig_cp = px.histogram(
            df_heart, x="ChestPainType", color="HeartDisease", barmode="stack",
            color_discrete_map={0: "#22C55E", 1: "#EF4444"},
            template="plotly_white"
        )
        fig_cp.update_layout(height=340, margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig_cp, use_container_width=True)

    with c4:
        st.markdown("#### 4. ST Slope Segment Distribution")
        fig_slope = px.pie(df_heart, names="ST_Slope", hole=0.4, template="plotly_white")
        fig_slope.update_layout(height=340, margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig_slope, use_container_width=True)

    with st.expander("🔍 Raw Dataset Viewer (`heart.csv`)"):
        st.dataframe(df_heart, use_container_width=True)

render_footer()
