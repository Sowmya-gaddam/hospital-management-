import streamlit as st
import sqlite3

# Database Connection
conn = sqlite3.connect('hospital.db', check_same_thread=False)
cursor = conn.cursor()


# ---------------- REGISTER FUNCTION ----------------
def register_user(username, password, role):

    cursor.execute(
        "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
        (username, password, role)
    )

    conn.commit()


# ---------------- LOGIN FUNCTION ----------------
def login_user(username, password):

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    return cursor.fetchone()


# ---------------- AUTH PAGE ----------------
def auth_page():

    st.title("🏥 Hospital Management System")

    menu = ["Login", "Register"]

    choice = st.sidebar.selectbox(
        "Menu",
        menu
    )

    # -------- REGISTER --------
    if choice == "Register":

        st.subheader("Create Account")

        new_user = st.text_input("Username")

        new_password = st.text_input(
            "Password",
            type='password'
        )

        role = st.selectbox(
            "Role",
            ["Admin", "Doctor", "Patient"]
        )

        if st.button("Register"):

            register_user(
                new_user,
                new_password,
                role
            )

            st.success("Registration Successful")

    # -------- LOGIN --------
    elif choice == "Login":

        st.subheader("Login")

        username = st.text_input("Username")

        password = st.text_input(
            "Password",
            type='password'
        )

        if st.button("Login"):

            result = login_user(
                username,
                password
            )

            if result:

                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.role = result[3]

                st.success("Login Successful")

                st.rerun()

            else:

                st.error("Invalid Username or Password")