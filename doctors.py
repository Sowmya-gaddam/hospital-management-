import streamlit as st
import sqlite3
import pandas as pd

# Database Connection
conn = sqlite3.connect('hospital.db', check_same_thread=False)
cursor = conn.cursor()


# ---------------- DOCTOR PAGE ----------------
def doctor_page():

    st.header("👨‍⚕️ Doctor Management")

    menu = [
        "Add Doctor",
        "View Doctors",
        "Search Doctor",
        "Delete Doctor"
    ]

    choice = st.sidebar.selectbox("Doctor Menu", menu)

    # -------- ADD DOCTOR --------
    if choice == "Add Doctor":

        name = st.text_input("Doctor Name")

        specialization = st.text_input("Specialization")

        availability = st.text_input("Availability")

        if st.button("Add Doctor"):

            cursor.execute(
                '''
                INSERT INTO doctors
                (name, specialization, availability)
                VALUES (?, ?, ?)
                ''',
                (name, specialization, availability)
            )

            conn.commit()

            st.success("Doctor Added Successfully")

    # -------- VIEW DOCTORS --------
    elif choice == "View Doctors":

        cursor.execute("SELECT * FROM doctors")

        data = cursor.fetchall()

        df = pd.DataFrame(
            data,
            columns=[
                "Doctor ID",
                "Name",
                "Specialization",
                "Availability"
            ]
        )

        st.dataframe(df)

    # -------- SEARCH DOCTOR --------
    elif choice == "Search Doctor":

        search_name = st.text_input("Enter Doctor Name")

        if st.button("Search"):

            cursor.execute(
                "SELECT * FROM doctors WHERE name LIKE ?",
                ('%' + search_name + '%',)
            )

            data = cursor.fetchall()

            if data:

                df = pd.DataFrame(
                    data,
                    columns=[
                        "Doctor ID",
                        "Name",
                        "Specialization",
                        "Availability"
                    ]
                )

                st.dataframe(df)

            else:
                st.warning("No Doctor Found")

    # -------- DELETE DOCTOR --------
    elif choice == "Delete Doctor":

        doctor_id = st.number_input(
            "Enter Doctor ID",
            min_value=1
        )

        if st.button("Delete"):

            cursor.execute(
                "DELETE FROM doctors WHERE doctor_id=?",
                (doctor_id,)
            )

            conn.commit()

            st.success("Doctor Deleted Successfully")
            