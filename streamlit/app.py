"""
InsightAI - Streamlit entry point.

Run with:
    streamlit run streamlit/app.py

All other pages live in pages/ and are auto-discovered by Streamlit's
multipage nav (the folder MUST be named "pages" and sit next to this file).
"""
import sys
import os

sys.path.append(os.path.dirname(__file__))

import streamlit as st
from utils.api import check_health
from utils.auth import is_logged_in

st.set_page_config(
    page_title="InsightAI — Conversational BI",
    page_icon="📊",
    layout="wide",
)

if "api_url" not in st.session_state:
    st.session_state["api_url"] = os.getenv("INSIGHTAI_API_URL", "http://127.0.0.1:8000/api")

st.title("📊 InsightAI")
st.caption("Ask business questions in plain English. Get SQL, charts, and insights back.")

if check_health():
    st.success("Backend connected.", icon="✅")
else:
    st.error(
        "Backend unreachable. Start it with `uvicorn app:app --port 8000` from the `backend/` folder.",
        icon="⚠️",
    )

st.markdown("### Get started")
if is_logged_in():
    st.write(f"Signed in as **{st.session_state.get('username')}**. Use the sidebar to navigate:")
else:
    st.write("Use the sidebar to log in, then explore the dashboard, analytics, and AI assistant.")

st.page_link("pages/Login.py", label="Login", icon="🔐")
st.page_link("pages/Dashboard.py", label="Dashboard", icon="📊")
st.page_link("pages/AI_Assistant.py", label="AI Assistant", icon="🤖")
st.page_link("pages/Analytics.py", label="Analytics", icon="📈")
st.page_link("pages/Upload_Dataset.py", label="Upload Dataset", icon="📁")
st.page_link("pages/Reports.py", label="Reports", icon="📄")
st.page_link("pages/Settings.py", label="Settings", icon="⚙️")
