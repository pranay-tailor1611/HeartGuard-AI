import streamlit as st
from components import load_css, render_top_navbar, render_sidebar, render_footer

st.set_page_config(page_title="Developer | CardioPulse AI", page_icon="👨‍💻", layout="wide")
load_css()
render_top_navbar()
render_sidebar()

st.markdown("## Developer & Engineering Profile")

st.markdown(
    """
    <div class="med-card">
        <h2 style="font-size: 1.8rem; font-weight: 800; margin-bottom: 0.25rem;">Senior Full-Stack & ML Engineer</h2>
        <p style="color: #666666; font-size: 0.95rem; margin-bottom: 1rem;">Specializing in High-Performance SaaS Interfaces & Applied Machine Learning</p>
        <div style="display: flex; gap: 10px; margin-bottom: 1.25rem;">
            <span class="badge-minimal">10+ Years Experience</span>
            <span class="badge-minimal">Streamlit & UI/UX Expert</span>
            <span class="badge-minimal">Applied ML Specialist</span>
        </div>
        <hr style="border: none; border-top: 1px solid #EAEAEA; margin: 1rem 0;"/>
        <p style="color: #666666; font-size: 0.9rem; line-height: 1.6;">
            Architected with Apple/Stripe-inspired minimalist design principles, pure black & white palettes, 
            generous whitespace, custom CSS tokens, and robust machine learning integration.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("### Technical Architecture")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="med-card"><h4>🎨 Design System</h4><p style="color: #666666; font-size: 0.85rem;">Minimalist CSS Tokens • Inter Typography • Micro-Shadows • Monochromatic UI</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="med-card"><h4>🤖 Machine Learning</h4><p style="color: #666666; font-size: 0.85rem;">Scikit-Learn KNN Classifier • StandardScaler Normalization • Joblib Serialization</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="med-card"><h4>⚡ Platform Engineering</h4><p style="color: #666666; font-size: 0.85rem;">Streamlit Multi-Page Router • Plotly Analytics • In-Session Memory Management</p></div>', unsafe_allow_html=True)

st.markdown("<br/>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("🌐 **GitHub:** [github.com/developer](https://github.com)")
with col2:
    st.markdown("💼 **LinkedIn:** [linkedin.com/in/developer](https://linkedin.com)")
with col3:
    st.markdown("📧 **Email:** developer@cardiopulse.ai")

render_footer()
