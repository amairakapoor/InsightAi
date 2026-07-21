import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import streamlit as st
from utils.auth import login, logout, is_logged_in

st.set_page_config(page_title="Login — InsightAI", page_icon="🔐")
st.title("🔐 Login")

if not is_logged_in():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login", type="primary"):
        if login(username, password):
            st.success("Login successful.")
            st.rerun()
        else:
            st.error("Invalid credentials.")

    st.caption("Demo credentials: `admin` / `admin123`")
else:
    st.success(f"Welcome, {st.session_state.get('username')}!")
    st.page_link("pages/Dashboard.py", label="Go to Dashboard", icon="📊")
    if st.button("Logout"):
        logout()
        st.rerun()
