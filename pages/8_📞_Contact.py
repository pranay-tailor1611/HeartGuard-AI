import streamlit as st
from components import load_css, render_top_navbar, render_sidebar, render_footer

st.set_page_config(page_title="Contact | CardioPulse AI", page_icon="📞", layout="wide")
load_css()
render_top_navbar()
render_sidebar()

st.markdown("## Emergency Contacts & Support")

st.markdown(
    """
    <div style="background: #FFFFFF; border: 1px solid #EAEAEA; border-radius: 16px; padding: 1.75rem; margin-bottom: 1.5rem;">
        <span class="badge-danger-minimal" style="margin-bottom: 0.5rem;">🚨 24/7 Medical Emergency Response</span>
        <h3 style="margin-top: 0.5rem; margin-bottom: 0.5rem;">Immediate Cardiac Assistance</h3>
        <p style="color: #666666; font-size: 0.95rem;">If you are experiencing acute chest pressure, numbness, or severe shortness of breath:</p>
        <div style="font-size: 1.4rem; font-weight: 800; color: #EF4444; margin-top: 0.5rem;">
            📞 National Emergency: 108 / 112 | Cardiac Hotline: 1800-123-CARDIAC
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
        <div class="med-card">
            <h3>🏥 Network Consultations</h3>
            <p style="color: #666666;"><b>Apollo Hospitals Cardiology Desk:</b> 1800-425-2277</p>
            <p style="color: #666666;"><b>Practo Clinical Consultations:</b> support@practo.com</p>
            <p style="color: #666666;"><b>Narayana Health Cardiac Institute:</b> 1800-309-0309</p>
        </div>
        """,
        unsafe_allow_html=True
    )
with col2:
    st.markdown("### ✉️ Inquiry Form")
    with st.form("contact_form"):
        st.text_input("Full Name", placeholder="Dr. Jane Smith")
        st.text_input("Email Address", placeholder="doctor@clinic.org")
        st.text_area("Clinical Query", placeholder="Enter your inquiry...")
        if st.form_submit_button("Send Inquiry →"):
            st.success("Message dispatched to clinical support.")

render_footer()
