import streamlit as st
import sqlite3
import pandas as pd
from fpdf import FPDF

# Database Connection
conn = sqlite3.connect('hospital.db', check_same_thread=False)
cursor = conn.cursor()


# ---------------- BILLING PAGE ----------------
def billing_page():

    st.header("💳 Billing System")

    patient_name = st.text_input("Patient Name")

    amount = st.number_input(
        "Bill Amount",
        min_value=0.0,
        format="%.2f"
    )

    payment_status = st.selectbox(
        "Payment Status",
        ["Paid", "Pending"]
    )

    # -------- GENERATE BILL --------
    if st.button("Generate Bill"):

        cursor.execute(
            '''
            INSERT INTO bills
            (patient_name, amount, payment_status)
            VALUES (?, ?, ?)
            ''',
            (patient_name, amount, payment_status)
        )

        conn.commit()

        # -------- PDF BILL --------
        pdf = FPDF()

        pdf.add_page()

        pdf.set_font("Arial", size=16)

        pdf.cell(
            200,
            10,
            txt="Hospital Bill",
            ln=True,
            align='C'
        )

        pdf.ln(10)

        pdf.set_font("Arial", size=12)

        pdf.cell(
            200,
            10,
            txt=f"Patient Name: {patient_name}",
            ln=True
        )

        pdf.cell(
            200,
            10,
            txt=f"Amount: Rs. {amount}",
            ln=True
        )

        pdf.cell(
            200,
            10,
            txt=f"Payment Status: {payment_status}",
            ln=True
        )

        pdf.output("bill.pdf")

        st.success("Bill Generated Successfully")

        # -------- DOWNLOAD BUTTON --------
        with open("bill.pdf", "rb") as file:

            st.download_button(
                label="Download Bill PDF",
                data=file,
                file_name="bill.pdf",
                mime="application/pdf"
            )

    # -------- VIEW BILLS --------
    st.subheader("📋 Billing Records")

    cursor.execute("SELECT * FROM bills")

    data = cursor.fetchall()

    df = pd.DataFrame(
        data,
        columns=[
            "Bill ID",
            "Patient Name",
            "Amount",
            "Payment Status"
        ]
    )

    st.dataframe(df)