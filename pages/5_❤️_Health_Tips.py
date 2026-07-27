import streamlit as st
from components import load_css, render_top_navbar, render_sidebar, render_footer

st.set_page_config(page_title="Health Tips | CardioPulse AI", page_icon="❤️", layout="wide")
load_css()
render_top_navbar()
render_sidebar()

st.markdown("## Lifestyle & Prevention Protocols")
st.caption("Evidence-based interventions to maintain optimal vascular function and lower long-term cardiac risk.")

tab1, tab2, tab3, tab4 = st.tabs([
    "🏃 Physical Exercise & Yoga",
    "🥗 Nutrition & DASH Diet",
    "💧 Hydration & Sleep Protocol",
    "🧘 Stress Management"
])

with tab1:
    st.markdown(
        """
        <div class="med-card">
            <h3>🏃 Aerobic & Exercise Guidelines</h3>
            <p style="color: #666666;"><b>Moderate Exercise:</b> 150 minutes per week of brisk walking, cycling, or swimming.</p>
            <p style="color: #666666;"><b>Strength & Flexibility:</b> 2 days per week of strength training and daily stretching or yoga.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with tab2:
    st.markdown(
        """
        <div class="med-card">
            <h3>🥗 Dietary Standards</h3>
            <p style="color: #666666;"><b>Sodium Limitation:</b> Keep daily sodium under 2,000 mg to assist blood pressure regulation.</p>
            <p style="color: #666666;"><b>DASH Pattern:</b> High in vegetables, whole grains, nuts, and omega-3 fatty acids.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with tab3:
    st.markdown(
        """
        <div class="med-card">
            <h3>💧 Hydration & Sleep Target</h3>
            <p style="color: #666666;"><b>Hydration Target:</b> 2.5 - 3.0 Liters of water daily to maintain blood viscosity.</p>
            <p style="color: #666666;"><b>Restorative Sleep:</b> Target 7-9 hours per night to avoid elevated cortisol levels.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with tab4:
    st.markdown(
        """
        <div class="med-card">
            <h3>🧘 Stress Reduction</h3>
            <p style="color: #666666;"><b>Mindfulness:</b> 10-15 minutes of daily breathing exercises or meditation to mitigate blood pressure spikes.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

render_footer()
