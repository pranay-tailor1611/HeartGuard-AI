import streamlit as st
from components import load_css, render_top_navbar, render_sidebar, render_footer

st.set_page_config(page_title="About Disease | CardioPulse AI", page_icon="🫀", layout="wide")
load_css()
render_top_navbar()
render_sidebar()

st.markdown("## Cardiovascular Disease Reference")
st.caption("Medical reference on coronary artery pathology, clinical indicators, and diagnostic standards.")

st.markdown(
    """
    <div class="med-card">
        <h3>What is Heart Disease?</h3>
        <p style="color: #666666; line-height: 1.6;">
            Heart disease encompasses structural and vascular disorders affecting cardiac function, including 
            coronary artery disease (CAD), heart rhythm abnormalities (arrhythmias), and vascular stiffening.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
        <div class="med-card">
            <h4>⚠️ Key Clinical Risk Factors</h4>
            <ul style="color: #666666; line-height: 1.8;">
                <li>Hypertension (Resting Blood Pressure > 130/80 mm Hg)</li>
                <li>Hypercholesterolemia (Serum Cholesterol > 200 mg/dl)</li>
                <li>Elevated Fasting Blood Sugar (> 120 mg/dl)</li>
                <li>Exercise-Induced ST Segment Depression (Oldpeak)</li>
                <li>Physical Inactivity & Elevated BMI</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
with col2:
    st.markdown(
        """
        <div class="med-card">
            <h4>🔍 Diagnostic Modalities</h4>
            <ul style="color: #666666; line-height: 1.8;">
                <li>Resting Electrocardiogram (ECG)</li>
                <li>Exercise Treadmill Stress Testing</li>
                <li>Coronary Angiography (Fluoroscopy Vessels)</li>
                <li>Echocardiography</li>
                <li>Serum Fasting Lipid Profile</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("### Symptoms & Pathological Causes")
sc1, sc2 = st.columns(2)
with sc1:
    with st.expander("🚨 Recognized Symptoms of Cardiac Distress", expanded=True):
        st.markdown("- **Chest Angina:** Squeezing, pressure, or tightness in the chest.")
        st.markdown("- **Dyspnea:** Shortness of breath during exertion.")
        st.markdown("- **Fatigue & Dizziness:** Lightheadedness during physical stress.")
with sc2:
    with st.expander("🧬 Underlying Biological Causes", expanded=True):
        st.markdown("- **Atherosclerosis:** Lipid plaque buildup inside coronary arteries.")
        st.markdown("- **Endothelial Dysfunction:** Chronic vascular inflammation.")
        st.markdown("- **Genetic Predisposition:** Familial hypercholesterolemia.")

render_footer()
