import streamlit as st

st.title("⚙️ Settings")

st.subheader("Dashboard Preferences")

show_metrics = st.checkbox("Show KPI Cards", value=True)
show_charts = st.checkbox("Show Charts", value=True)
show_table = st.checkbox("Show Data Table", value=True)

st.subheader("Notifications")

email_alerts = st.toggle("Enable Email Alerts")
weekly_report = st.toggle("Receive Weekly Reports")

st.subheader("Export Settings")

file_type = st.selectbox(
    "Default Export Format",
    ["CSV", "Excel", "PDF"]
)

st.subheader("User Information")

name = st.text_input("User Name", "Admin")
company = st.text_input("Company Name", "InsightIQ")

if st.button("Save Settings"):
    st.success("✅ Settings saved successfully!")