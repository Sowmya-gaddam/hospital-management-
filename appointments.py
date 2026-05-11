import streamlit as st
import sqlite3
import pandas as pd

# Database Connection
conn = sqlite3.connect('hospital.db', check_same_thread=False)
cursor = conn.cursor()


# ---------------- APPOINTMENT PAGE ----------------
def appointment_page():

    st.header("📅 Appointment Management")

    menu = [
        "Book Appointment",
        "View Appointments",
        "Cancel Appointment"
    ]

    choice = st.sidebar.selectbox("Appointment Menu", menu)

    # -------- BOOK APPOINTMENT --------
    if choice == "Book Appointment":

        patient_name = st.text_input("Patient Name")

        doctor_name = st.text_input("Doctor Name")

        date = st.date_input("Appointment Date")

        time = st.time_input("Appointment Time")

        if st.button("Book Appointment"):

            cursor.execute(
                '''
                INSERT INTO appointments
                (patient_name, doctor_name, date, time, status)
                VALUES (?, ?, ?, ?, ?)
                ''',
                (
                    patient_name,
                    doctor_name,
                    str(date),
                    str(time),
                    "Booked"
                )
            )

            conn.commit()

            st.success("Appointment Booked Successfully")

    # -------- VIEW APPOINTMENTS --------
    elif choice == "View Appointments":

        cursor.execute("SELECT * FROM appointments")

        data = cursor.fetchall()

        df = pd.DataFrame(
            data,
            columns=[
                "Appointment ID",
                "Patient Name",
                "Doctor Name",
                "Date",
                "Time",
                "Status"
            ]
        )

        st.dataframe(df)

    # -------- CANCEL APPOINTMENT --------
    elif choice == "Cancel Appointment":

        appointment_id = st.number_input(
            "Enter Appointment ID",
            min_value=1
        )

        if st.button("Cancel Appointment"):

            cursor.execute(
                '''
                UPDATE appointments
                SET status=?
                WHERE appointment_id=?
                ''',
                ("Cancelled", appointment_id)
            )

            conn.commit()

            st.success("Appointment Cancelled Successfully")