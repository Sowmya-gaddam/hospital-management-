import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# Database Connection
conn = sqlite3.connect('hospital.db', check_same_thread=False)


# ---------------- DASHBOARD PAGE ----------------
def dashboard_page():

    st.header("📊 Hospital Dashboard")

    # -------- LOAD DATA --------
    patients = pd.read_sql_query(
        "SELECT * FROM patients",
        conn
    )

    doctors = pd.read_sql_query(
        "SELECT * FROM doctors",
        conn
    )

    appointments = pd.read_sql_query(
        "SELECT * FROM appointments",
        conn
    )

    bills = pd.read_sql_query(
        "SELECT * FROM bills",
        conn
    )

    # -------- METRICS --------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Patients",
        len(patients)
    )

    col2.metric(
        "Total Doctors",
        len(doctors)
    )

    col3.metric(
        "Appointments",
        len(appointments)
    )

    col4.metric(
        "Bills",
        len(bills)
    )

    st.divider()

    # -------- DISEASE ANALYSIS --------
    if not patients.empty:

        st.subheader("🦠 Disease Statistics")

        fig1 = px.histogram(
            patients,
            x='disease',
            title='Patients by Disease'
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    # -------- APPOINTMENT STATUS --------
    if not appointments.empty:

        st.subheader("📅 Appointment Status")

        fig2 = px.pie(
            appointments,
            names='status',
            title='Appointment Status Distribution'
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # -------- BILLING ANALYSIS --------
    if not bills.empty:

        st.subheader("💰 Billing Analysis")

        fig3 = px.bar(
            bills,
            x='patient_name',
            y='amount',
            title='Patient Billing Amount'
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    # -------- RECENT PATIENTS --------
    if not patients.empty:

        st.subheader("👤 Recent Patients")

        st.dataframe(
            patients.tail(5),
            use_container_width=True
        )