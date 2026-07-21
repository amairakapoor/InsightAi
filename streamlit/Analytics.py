import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Analytics Dashboard")

if "data" in st.session_state:
    df = st.session_state["data"]
else:
    df = pd.read_csv("Data/sales_data.csv")

st.subheader("Revenue by Region")

fig = px.bar(
    df.groupby("Region", as_index=False)["Revenue"].sum(),
    x="Region",
    y="Revenue",
    color="Region"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Profit by Category")

fig = px.pie(
    df.groupby("Category", as_index=False)["Profit"].sum(),
    names="Category",
    values="Profit",
    hole=0.4
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Monthly Revenue Trend")

fig = px.line(
    df,
    x="Month",
    y="Revenue",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Orders by Category")

fig = px.bar(
    df.groupby("Category", as_index=False)["Orders"].sum(),
    x="Category",
    y="Orders",
    color="Category"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Dataset")

st.dataframe(df, use_container_width=True)