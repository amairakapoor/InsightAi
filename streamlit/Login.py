import streamlit as st

st.title("🔐 Login")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "admin123":

            st.session_state.logged_in = True

            st.success("Login Successful")

            st.rerun()

        else:

            st.error("Invalid Credentials")

else:

    st.success("Welcome Admin!")

    if st.button("Logout"):

        st.session_state.logged_in = False

        st.rerun()