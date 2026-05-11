import streamlit as st
import sqlite3
import pandas as pd

# Database Connection
conn = sqlite3.connect('hospital.db', check_same_thread=False)
cursor = conn.cursor()


# ---------------- PATIENT PAGE ----------------
def patient_page():

    st.title("👤 Patient Management System")
    st.markdown("---")

    menu = st.sidebar.selectbox(
        "Patient Menu",
        ["Add Patient", "View Patients", "Search Patient", "Update Patient", "Delete Patient"]
    )

    # ================= ADD PATIENT =================
    if menu == "Add Patient":

        st.subheader("➕ Add New Patient")

        name = st.text_input("Patient Name")
        age = st.number_input("Age", 1, 120)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        disease = st.text_input("Disease")
        phone = st.text_input("Phone Number")

        if st.button("Add Patient"):

            if name and disease and phone:

                cursor.execute("""
                    INSERT INTO patients (name, age, gender, disease, phone)
                    VALUES (?, ?, ?, ?, ?)
                """, (name, age, gender, disease, phone))

                conn.commit()
                st.success("✅ Patient Added Successfully")

            else:
                st.warning("⚠️ Please fill all required fields")

    # ================= VIEW PATIENTS =================
    elif menu == "View Patients":

        st.subheader("📋 All Patients")

        df = pd.read_sql_query("SELECT * FROM patients", conn)

        st.dataframe(df, use_container_width=True)

    # ================= SEARCH PATIENT =================
    elif menu == "Search Patient":

        st.subheader("🔍 Search Patient")

        search_name = st.text_input("Enter Patient Name")

        if st.button("Search"):

            df = pd.read_sql_query(
                "SELECT * FROM patients WHERE name LIKE ?",
                conn,
                params=(f"%{search_name}%",)
            )

            if not df.empty:
                st.dataframe(df, use_container_width=True)
            else:
                st.warning("❌ No Patient Found")

    # ================= UPDATE PATIENT =================
    elif menu == "Update Patient":

        st.subheader("✏️ Update Patient Details")

        patient_id = st.number_input("Enter Patient ID", min_value=1)

        cursor.execute(
            "SELECT * FROM patients WHERE patient_id=?",
            (patient_id,)
        )

        patient = cursor.fetchone()

        if patient:

            new_name = st.text_input("Name", value=patient[1])
            new_age = st.number_input("Age", 1, 120, value=patient[2])
            new_gender = st.selectbox(
                "Gender",
                ["Male", "Female", "Other"],
                index=["Male", "Female", "Other"].index(patient[3]) if patient[3] in ["Male", "Female", "Other"] else 0
            )
            new_disease = st.text_input("Disease", value=patient[4])
            new_phone = st.text_input("Phone", value=patient[5])

            if st.button("Update Patient"):

                cursor.execute("""
                    UPDATE patients
                    SET name=?, age=?, gender=?, disease=?, phone=?
                    WHERE patient_id=?
                """, (new_name, new_age, new_gender, new_disease, new_phone, patient_id))

                conn.commit()
                st.success("✅ Patient Updated Successfully")

        else:
            st.error("❌ Patient ID Not Found")

    # ================= DELETE PATIENT =================
    elif menu == "Delete Patient":

        st.subheader("🗑️ Delete Patient")

        patient_id = st.number_input("Enter Patient ID", min_value=1)

        if st.button("Delete Patient"):

            cursor.execute(
                "DELETE FROM patients WHERE patient_id=?",
                (patient_id,)
            )

            conn.commit()
            st.success("✅ Patient Deleted Successfully")