import streamlit as st
import plotly.graph_objects as go
import os

def load_css():
    """Injects minimalist luxury SaaS style.css."""
    css_path = os.path.join("styles", "style.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def render_top_navbar():
    """Renders Stripe / Apple inspired top navbar."""
    st.markdown(
        """
        <div class="top-navbar">
            <div class="top-navbar-brand">
                <span style="font-size: 1.3rem;">🫀</span> CardioPulse AI
            </div>
            <div style="display: flex; gap: 20px; align-items: center; font-size: 0.85rem; color: #666666;">
                <span>🟢 <b>System:</b> Operational</span>
                <span>🔒 <b>HIPAA Compliant</b></span>
                <span class="badge-minimal">v2.4.0 • Enterprise SaaS</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_sidebar():
    """Renders sleek minimalist sidebar."""
    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-header">
                <h2>CardioPulse AI</h2>
                <p>Clinical Decision Support System</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if "history" in st.session_state:
            st.metric(label="Total Assessments", value=len(st.session_state.history))

        st.caption("🔒 Trained on 900+ clinical records. All inference is computed locally.")
        st.divider()
        st.markdown(
            """
            <div style="font-size: 0.75rem; color: #888888; text-align: left;">
                © 2026 <b>CardioPulse Systems</b><br/>
                Minimalist SaaS Edition
            </div>
            """,
            unsafe_allow_html=True
        )

def render_footer():
    """Renders Apple/Stripe inspired minimal footer."""
    st.markdown(
        """
        <div class="footer-container">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; margin-bottom: 1rem;">
                <div style="font-weight: 700; font-size: 0.95rem; color: #111111;">
                    CardioPulse AI <span style="font-weight: 400; color: #666666; font-size: 0.85rem;">— Enterprise Cardiac Assessment Platform</span>
                </div>
                <div>
                    <a href="#top" style="color: #111111; text-decoration: none; font-weight: 600; font-size: 0.85rem;">⬆️ Back to Top</a>
                </div>
            </div>
            <hr style="border: none; border-top: 1px solid #EAEAEA; margin: 1rem 0;"/>
            <p style="font-size: 0.78rem; color: #888888; line-height: 1.5;">
                <b>Medical Disclaimer:</b> CardioPulse AI is a decision support algorithm designed for clinical screening and research purposes. 
                It does not constitute a certified medical diagnosis. Consult a licensed physician for clinical evaluations.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

def render_bmi_calculator(height_cm, weight_kg):
    """Minimalist BMI calculator card."""
    bmi = round(weight_kg / ((height_cm / 100) ** 2), 1)
    status = "Normal"
    badge_style = "color: #22C55E; background: #F0FDF4; border: 1px solid rgba(34,197,94,0.2);"
    if bmi < 18.5:
        status = "Underweight"
        badge_style = "color: #111111; background: #F5F5F5; border: 1px solid #EAEAEA;"
    elif 25 <= bmi < 30:
        status = "Overweight"
        badge_style = "color: #D97706; background: #FFFBEB; border: 1px solid rgba(217,119,6,0.2);"
    elif bmi >= 30:
        status = "Obese"
        badge_style = "color: #DC2626; background: #FEF2F2; border: 1px solid rgba(220,38,38,0.2);"

    st.markdown(
        f"""
        <div style="background: #FAFAFA; padding: 0.85rem 1.25rem; border-radius: 12px; border: 1px solid #EAEAEA; margin-bottom: 1.5rem; display: flex; align-items: center; justify-content: space-between;">
            <span style="font-size: 0.9rem; color: #111111;">⚖️ <b>BMI Calculator:</b> Baseline Body Mass Index: <b>{bmi} kg/m²</b></span>
            <span style="padding: 0.25rem 0.75rem; border-radius: 20px; font-size: 0.78rem; font-weight: 700; {badge_style}">{status}</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    return bmi, status

def render_risk_gauge(disease_probability, prediction):
    """Sleek minimalist Plotly gauge chart."""
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=disease_probability,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Cardiac Risk Meter (%)", 'font': {'size': 15, 'color': "#111111", 'family': "Inter"}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#111111"},
            'bar': {'color': "#EF4444" if prediction == 1 else "#22C55E"},
            'bgcolor': "#FFFFFF",
            'borderwidth': 1,
            'bordercolor': "#EAEAEA",
            'steps': [
                {'range': [0, 35], 'color': '#F0FDF4'},
                {'range': [35, 70], 'color': '#FFFBEB'},
                {'range': [70, 100], 'color': '#FEF2F2'}
            ],
            'threshold': {
                'line': {'color': "#111111", 'width': 3},
                'thickness': 0.75,
                'value': disease_probability
            }
        }
    ))
    fig_gauge.update_layout(height=260, margin=dict(l=20, r=20, t=40, b=20), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig_gauge, use_container_width=True)
