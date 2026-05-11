import streamlit as st
import database
from medicine import medicine_page
from admin_analytics import admin_analytics_page
from auth import auth_page
from patients import patient_page
from doctors import doctor_page
from appointments import appointment_page
from billing import billing_page
from dashboard import dashboard_page
from ai_symptom_checker import symptom_checker_page

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Hospital Management System",
    layout="wide"
)

import streamlit as st

st.markdown("""
<style>

/* ---------- TEXT INPUT & TEXT AREA ---------- */
input, textarea {
    background-color: white !important;
    color: black !important;
    border: 1px solid black !important;
}

/* ---------- STREAMLIT SPECIFIC FIX ---------- */
.stTextInput input, 
.stTextArea textarea {
    color: black !important;
    background-color: white !important;
}

/* Placeholder text */
.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: gray !important;
}

/* Focus border */
.stTextInput input:focus,
.stTextArea textarea:focus {
    border: 2px solid black !important;
    outline: none !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🏥 Smart Hospital Management System")

st.caption(
    "Healthcare Management Platform"
)

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN PAGE ----------------
if st.session_state.logged_in == False:

    auth_page()

# ---------------- MAIN APP ----------------
else:

    st.sidebar.markdown(
        "## 🏥 HMS Control Panel"
    )

    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Patients",
            "Doctors",
            "Appointments",
            "Billing",
            "AI Symptom Checker",
            "Medicine",
            "Admin Analytics"
        ]
    )

    st.sidebar.success(
        f"Logged in as: {st.session_state.username}"
    )

    # ---------------- LOGOUT ----------------
    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.rerun()

    # ---------------- PAGE NAVIGATION ----------------
    if page == "Dashboard":

        dashboard_page()

    elif page == "Patients":

        patient_page()

    elif page == "Doctors":

        doctor_page()

    elif page == "Appointments":

        appointment_page()

    elif page == "Billing":

        billing_page()

    elif page == "AI Symptom Checker":

        symptom_checker_page()
    elif page == "Medicine":
        
        medicine_page()
    elif page == "Admin Analytics":
        
        admin_analytics_page()

# ---------------- FOOTER ----------------
st.markdown(
    """
    <hr>

    <center>
    Smart Hospital Management System 
    </center>
    """,
    unsafe_allow_html=True
)