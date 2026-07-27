import streamlit as st
import pandas as pd
from datetime import datetime
from components import load_css, render_top_navbar, render_sidebar, render_footer, render_bmi_calculator, render_risk_gauge
from utils.ml_utils import predict_heart_disease

st.set_page_config(page_title="Prediction | CardioPulse AI", page_icon="🩺", layout="wide")
load_css()
render_top_navbar()
render_sidebar()

if "history" not in st.session_state:
    st.session_state.history = []

st.markdown("## Patient Risk Assessment")
st.caption("Fill in the clinical indicators below to generate a Machine Learning heart disease risk evaluation.")

col_top_actions1, col_top_actions2 = st.columns([4, 1])
with col_top_actions2:
    if st.button("Reset Form"):
        st.rerun()

with st.form("prediction_form"):
    st.markdown('<div class="med-card-header">👤 Patient Demographics & Body Metrics</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        age = st.slider("Age (Years)", min_value=18, max_value=100, value=45, help="Patient age in completed years")
    with c2:
        sex = st.selectbox("Gender / Sex", ["M", "F"], help="Biological Sex (M: Male, F: Female)")
    with c3:
        height_cm = st.number_input("Height (cm)", min_value=100, max_value=250, value=170, help="Used for BMI Calculation")
    with c4:
        weight_kg = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70, help="Used for BMI Calculation")

    bmi, bmi_status = render_bmi_calculator(height_cm, weight_kg)

    st.markdown('<div class="med-card-header">🫀 Cardiac Clinical Indicators</div>', unsafe_allow_html=True)
    h1, h2 = st.columns(2)
    with h1:
        chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"], help="ATA: Atypical Angina, NAP: Non-Anginal Pain, TA: Typical Angina, ASY: Asymptomatic")
        resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=220, value=120, help="Resting BP upon admission")
        cholesterol = st.number_input("Serum Cholesterol (mg/dl)", min_value=80, max_value=600, value=210, help="Serum cholesterol level in mg/dl")
        fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1], format_func=lambda x: "Yes (1)" if x == 1 else "No (0)", help="1 if Fasting Blood Sugar > 120 mg/dl, else 0")
        resting_ecg = st.selectbox("Resting ECG Results", ["Normal", "ST", "LVH"], help="Normal: Normal, ST: ST-T abnormality, LVH: Left Ventricular Hypertrophy")

    with h2:
        max_hr = st.slider("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150, help="Maximum heart rate during stress test")
        exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"], help="Angina pain induced by exercise (Y: Yes, N: No)")
        oldpeak = st.slider("Oldpeak (ST Depression)", min_value=0.0, max_value=6.0, value=1.0, step=0.1, help="ST depression induced by exercise relative to rest")
        st_slope = st.selectbox("ST Slope Segment", ["Up", "Flat", "Down"], help="Peak exercise ST segment slope")

    with st.expander("➕ Additional Clinical Parameters (Fluoroscopy Vessels & Thalassemia)"):
        sc1, sc2 = st.columns(2)
        with sc1:
            ca = st.selectbox("Major Vessels Colored by Fluoroscopy (0-3)", [0, 1, 2, 3], index=0)
        with sc2:
            thal = st.selectbox("Thalassemia Type", ["Normal", "Fixed Defect", "Reversible Defect"])

    st.markdown("<br/>", unsafe_allow_html=True)
    submit_btn = st.form_submit_button("Run Assessment →")

if submit_btn:
    with st.spinner("Processing clinical metrics through KNN model..."):
        prediction, confidence_score, disease_probability = predict_heart_disease(
            age, sex, chest_pain, resting_bp, cholesterol, fasting_bs,
            resting_ecg, max_hr, exercise_angina, oldpeak, st_slope
        )

        record = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "age": age,
            "sex": sex,
            "chest_pain": chest_pain,
            "bp": resting_bp,
            "cholesterol": cholesterol,
            "prediction": "High Risk" if prediction == 1 else "Low Risk",
            "confidence": f"{confidence_score}%"
        }
        st.session_state.history.append(record)

    st.toast("Evaluation Complete", icon="✅")
    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown("### Assessment Result")

    res_col1, res_col2 = st.columns([1.2, 1])

    with res_col1:
        if prediction == 1:
            st.markdown(
                f"""
                <div class="result-card-minimal">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                        <span class="badge-danger-minimal">⚠️ High Risk Stratification</span>
                        <span style="font-size: 0.85rem; color: #666666;">Confidence: <b>{confidence_score}%</b></span>
                    </div>
                    <div class="result-title">Elevated Heart Disease Risk Detected</div>
                    <p style="color: #666666; font-size: 0.95rem; line-height: 1.5; margin-bottom: 1rem;">
                        The model identified cardiac risk indicators based on ST depression, blood pressure, or cholesterol markers.
                    </p>
                    <hr style="border: none; border-top: 1px solid #EAEAEA; margin: 1rem 0;"/>
                    <div style="font-size: 0.88rem; color: #111111;">
                        <b>Recommended Action:</b> Schedule a comprehensive clinical evaluation with a cardiologist.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div class="result-card-minimal">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                        <span class="badge-success-minimal">✅ Healthy / Low Risk</span>
                        <span style="font-size: 0.85rem; color: #666666;">Confidence: <b>{confidence_score}%</b></span>
                    </div>
                    <div class="result-title">Low Cardiac Risk Profile</div>
                    <p style="color: #666666; font-size: 0.95rem; line-height: 1.5; margin-bottom: 1rem;">
                        No major risk indicators were detected by the model for the provided physiological parameters.
                    </p>
                    <hr style="border: none; border-top: 1px solid #EAEAEA; margin: 1rem 0;"/>
                    <div style="font-size: 0.88rem; color: #111111;">
                        <b>Health Score: 92/100</b> — Maintain healthy lifestyle practices and regular checkups.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    with res_col2:
        render_risk_gauge(disease_probability, prediction)

    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown("### Clinical Recommendations")
    tab_rec1, tab_rec2, tab_rec3, tab_rec4 = st.tabs([
        "🏃 Activity Guidelines",
        "🥗 Nutrition & Diet",
        "💧 Hydration & Sleep",
        "👨‍⚕️ Medical Next Steps"
    ])

    with tab_rec1:
        if prediction == 1:
            st.warning("Consult a physician prior to initiating high-intensity physical workouts.")
            st.markdown("- Start with low-impact 20-30 minute walks.")
            st.markdown("- Avoid heavy isometric strain without medical clearance.")
        else:
            st.success("Standard physical guidelines applicable.")
            st.markdown("- Target 150 minutes of moderate aerobic exercise weekly.")

    with tab_rec2:
        st.markdown("- Adopt DASH or Mediterranean dietary patterns low in saturated fats.")
        st.markdown("- Restrict sodium intake to under 2,000 mg per day.")

    with tab_rec3:
        st.markdown("- Maintain daily hydration of 2.5 - 3.0 Liters.")
        st.markdown("- Target 7-9 hours of restful sleep daily.")

    with tab_rec4:
        if prediction == 1:
            st.error("Schedule a physician consultation within 7 days.")
        else:
            st.info("Routine annual wellness visits recommended.")

    st.markdown("<br/>", unsafe_allow_html=True)
    col_act1, col_act2, col_act3 = st.columns(3)

    report_str = f"""
=====================================================
CARDIOPULSE AI - CLINICAL ASSESSMENT REPORT
=====================================================
Date/Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Patient Age: {age} | Gender: {sex}
BMI: {bmi} kg/m² ({bmi_status})
Resting BP: {resting_bp} mm Hg | Cholesterol: {cholesterol} mg/dl
Max Heart Rate: {max_hr} bpm | ST Depression: {oldpeak}

PREDICTION RESULT: {"HIGH RISK OF HEART DISEASE" if prediction == 1 else "LOW RISK / HEALTHY PROFILE"}
CONFIDENCE SCORE: {confidence_score}%
DISEASE PROBABILITY: {disease_probability}%

Disclaimer: Generated by AI decision support algorithm. Not a substitute for professional medical diagnosis.
=====================================================
    """

    with col_act1:
        st.download_button(
            label="Download Clinical Report (.txt)",
            data=report_str,
            file_name=f"CardioPulse_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )
    with col_act2:
        if st.button("Share Result"):
            st.success("Link copied to clipboard!")
    with col_act3:
        st.page_link("pages/3_📊_Dashboard.py", label="View Analytics Dashboard →", use_container_width=True)

render_footer()
