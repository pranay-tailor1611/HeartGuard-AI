import streamlit as st
from components import load_css, render_top_navbar, render_sidebar, render_footer

st.set_page_config(page_title="CardioPulse AI | Minimalist SaaS", page_icon="🏠", layout="wide")
load_css()
render_top_navbar()
render_sidebar()

# Hero Section - Apple / Stripe Minimalist
st.markdown(
    """
    <div class="hero-container">
        <span class="badge-minimal" style="margin-bottom: 12px;">✨ AI-Powered Clinical Intelligence</span>
        <h1 class="hero-title">Predictive Cardiology,<br/>Redefined for Modern Care.</h1>
        <p class="hero-subtitle">
            Instantaneous, Machine Learning-driven cardiac risk assessments. Built for clinicians, researchers, and patients seeking precision screening.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Start Prediction CTA
col_cta1, col_cta2, col_cta3 = st.columns([1, 2, 1])
with col_cta2:
    st.page_link("pages/2_🩺_Prediction.py", label="Start Risk Assessment →", use_container_width=True)

st.markdown("<br/>", unsafe_allow_html=True)

# Metric Showcase Cards
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="metric-card-custom"><div class="metric-value">918</div><div class="metric-label">Clinical Data Points</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card-custom"><div class="metric-value">88.5%</div><div class="metric-label">Model Accuracy</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card-custom"><div class="metric-value">&lt; 10ms</div><div class="metric-label">Inference Latency</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card-custom"><div class="metric-value">100%</div><div class="metric-label">Client-Side Privacy</div></div>', unsafe_allow_html=True)

st.markdown("<br/>", unsafe_allow_html=True)

# Minimal Feature Grid
st.markdown("### Platform Features")
f_col1, f_col2, f_col3, f_col4 = st.columns(4)

with f_col1:
    st.markdown('<div class="med-card"><div style="font-size: 1.5rem; margin-bottom: 0.5rem;">⚡</div><h4>Instant Analysis</h4><p style="font-size: 0.85rem; color: #666666;">Immediate risk stratification generated in milliseconds from physiological indicators.</p></div>', unsafe_allow_html=True)
with f_col2:
    st.markdown('<div class="med-card"><div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🎯</div><h4>Trained KNN Engine</h4><p style="font-size: 0.85rem; color: #666666;">Optimized K-Nearest Neighbors pipeline with StandardScaler feature normalization.</p></div>', unsafe_allow_html=True)
with f_col3:
    st.markdown('<div class="med-card"><div style="font-size: 1.5rem; margin-bottom: 0.5rem;">📊</div><h4>Interactive Analytics</h4><p style="font-size: 0.85rem; color: #666666;">Explore distribution patterns and clinical metrics across 900+ patient records.</p></div>', unsafe_allow_html=True)
with f_col4:
    st.markdown('<div class="med-card"><div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🛡️</div><h4>Private & Secure</h4><p style="font-size: 0.85rem; color: #666666;">Zero external server data leakage. All evaluations run in your isolated session.</p></div>', unsafe_allow_html=True)

render_footer()
