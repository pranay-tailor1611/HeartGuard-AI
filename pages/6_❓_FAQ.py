import streamlit as st
from components import load_css, render_top_navbar, render_sidebar, render_footer

st.set_page_config(page_title="FAQ | CardioPulse AI", page_icon="❓", layout="wide")
load_css()
render_top_navbar()
render_sidebar()

st.markdown("## Frequently Asked Questions")
st.caption("Common questions regarding machine learning inference, clinical metrics, and data privacy.")

with st.expander("Q1: How does the KNN machine learning algorithm calculate risk?", expanded=True):
    st.write("The model measures distance vectors across 15 scaled physiological features against 918 clinical training records to determine nearest neighbor risk probability.")

with st.expander("Q2: What does ST depression (Oldpeak) indicate?"):
    st.write("Oldpeak represents the displacement of the ST segment during peak exercise relative to rest. Values above 1.0 mm often correlate with reduced coronary perfusion.")

with st.expander("Q3: Is patient data uploaded or logged remotely?"):
    st.write("No. The application runs entirely client-side/in-session memory. No patient inputs are transmitted to external servers.")

with st.expander("Q4: Can CardioPulse AI replace physician diagnosis?"):
    st.write("No. CardioPulse AI is a preliminary decision support tool. Official diagnostic determinations require physical cardiology consultations.")

render_footer()
