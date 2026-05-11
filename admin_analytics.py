import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# Database Connection
conn = sqlite3.connect('hospital.db', check_same_thread=False)


# ---------------- ADMIN ANALYTICS PAGE ----------------
def admin_analytics_page():

    st.title("📊 Admin Analytics Dashboard")

    # -------- LOAD DATA --------
    patients = pd.read_sql_query("SELECT * FROM patients", conn)
    doctors = pd.read_sql_query("SELECT * FROM doctors", conn)
    appointments = pd.read_sql_query("SELECT * FROM appointments", conn)
    bills = pd.read_sql_query("SELECT * FROM bills", conn)
    medicines = pd.read_sql_query("SELECT * FROM medicines", conn)

    # -------- TOTAL REVENUE --------
    total_revenue = bills['amount'].sum() if not bills.empty else 0

    # -------- METRICS --------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Patients", len(patients))
    col2.metric("Total Doctors", len(doctors))
    col3.metric("Appointments", len(appointments))
    col4.metric("Revenue", f"₹ {total_revenue}")

    st.divider()

    # -------- REVENUE CHART --------
    if not bills.empty:
        st.subheader("💰 Revenue Analysis")

        fig1 = px.bar(bills, x='patient_name', y='amount')
        st.plotly_chart(fig1, use_container_width=True)

    # -------- APPOINTMENT STATUS --------
    if not appointments.empty:
        st.subheader("📅 Appointment Status")

        fig2 = px.pie(appointments, names='status')
        st.plotly_chart(fig2, use_container_width=True)

    # -------- MEDICINE STOCK --------
    if not medicines.empty:
        st.subheader("💊 Medicine Stock")

        fig3 = px.bar(medicines, x='medicine_name', y='quantity')
        st.plotly_chart(fig3, use_container_width=True)

    # -------- RECENT PATIENTS --------
    if not patients.empty:
        st.subheader("👤 Recent Patients")
        st.dataframe(patients.tail(5), use_container_width=True)