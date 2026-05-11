import streamlit as st
import sqlite3
import pandas as pd

# Database Connection
conn = sqlite3.connect(
    'hospital.db',
    check_same_thread=False
)

cursor = conn.cursor()


# ---------------- MEDICINE PAGE ----------------
def medicine_page():

    st.header("💊 Medicine Management System")

    menu = [
        "Add Medicine",
        "View Medicines",
        "Search Medicine",
        "Delete Medicine"
    ]

    choice = st.sidebar.selectbox(
        "Medicine Menu",
        menu
    )

    # -------- ADD MEDICINE --------
    if choice == "Add Medicine":

        medicine_name = st.text_input(
            "Medicine Name"
        )

        company = st.text_input(
            "Company"
        )

        quantity = st.number_input(
            "Quantity",
            min_value=1
        )

        expiry_date = st.date_input(
            "Expiry Date"
        )

        price = st.number_input(
            "Price",
            min_value=0.0
        )

        if st.button("Add Medicine"):

            cursor.execute(
                '''
                INSERT INTO medicines
                (
                    medicine_name,
                    company,
                    quantity,
                    expiry_date,
                    price
                )
                VALUES (?, ?, ?, ?, ?)
                ''',
                (
                    medicine_name,
                    company,
                    quantity,
                    str(expiry_date),
                    price
                )
            )

            conn.commit()

            st.success(
                "Medicine Added Successfully"
            )

    # -------- VIEW MEDICINES --------
    elif choice == "View Medicines":

        cursor.execute(
            "SELECT * FROM medicines"
        )

        data = cursor.fetchall()

        df = pd.DataFrame(
            data,
            columns=[
                "Medicine ID",
                "Medicine Name",
                "Company",
                "Quantity",
                "Expiry Date",
                "Price"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    # -------- SEARCH MEDICINE --------
    elif choice == "Search Medicine":

        search_name = st.text_input(
            "Enter Medicine Name"
        )

        if st.button("Search"):

            cursor.execute(
                '''
                SELECT * FROM medicines
                WHERE medicine_name LIKE ?
                ''',
                ('%' + search_name + '%',)
            )

            data = cursor.fetchall()

            if data:

                df = pd.DataFrame(
                    data,
                    columns=[
                        "Medicine ID",
                        "Medicine Name",
                        "Company",
                        "Quantity",
                        "Expiry Date",
                        "Price"
                    ]
                )

                st.dataframe(
                    df,
                    use_container_width=True
                )

            else:

                st.warning(
                    "Medicine Not Found"
                )

    # -------- DELETE MEDICINE --------
    elif choice == "Delete Medicine":

        medicine_id = st.number_input(
            "Enter Medicine ID",
            min_value=1
        )

        if st.button("Delete Medicine"):

            cursor.execute(
                '''
                DELETE FROM medicines
                WHERE medicine_id=?
                ''',
                (medicine_id,)
            )

            conn.commit()

            st.success(
                "Medicine Deleted Successfully"
            )