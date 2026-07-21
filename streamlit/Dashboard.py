import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Business Dashboard")

# ---------------- Load Data ---------------- #

if "data" in st.session_state:
    df = st.session_state["data"]
else:
    df = pd.read_csv("Data/sales_data.csv")

# ---------------- Sidebar Filters ---------------- #

st.sidebar.header("Filters")

region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + sorted(df["Region"].unique().tolist())
)

category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + sorted(df["Category"].unique().tolist())
)

filtered_df = df.copy()

if region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == region]

if category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == category]

# ---------------- KPI Calculations ---------------- #

total_revenue = filtered_df["Revenue"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Orders"].sum()
customers = len(filtered_df)

best_region = (
    filtered_df.groupby("Region")["Revenue"]
    .sum()
    .idxmax()
)

best_category = (
    filtered_df.groupby("Category")["Revenue"]
    .sum()
    .idxmax()
)

avg_profit = filtered_df["Profit"].mean()

total_regions = filtered_df["Region"].nunique()

total_categories = filtered_df["Category"].nunique()

# ---------------- KPI Cards ---------------- #

st.subheader("Business Overview")

row1 = st.columns(4)

row1[0].metric("💰 Revenue", f"₹{total_revenue:,}")
row1[1].metric("📈 Profit", f"₹{total_profit:,}")
row1[2].metric("🛒 Orders", f"{total_orders:,}")
row1[3].metric("👥 Customers", customers)

row2 = st.columns(4)

row2[0].metric("🏆 Best Region", best_region)
row2[1].metric("📦 Best Category", best_category)
row2[2].metric("📊 Avg Profit", f"₹{avg_profit:,.0f}")
row2[3].metric("🌍 Regions", total_regions)

st.metric("🗂 Categories", total_categories)

st.markdown("---")

# ---------------- Charts ---------------- #

left, right = st.columns(2)

with left:
    fig = px.line(
        filtered_df,
        x="Month",
        y="Revenue",
        markers=True,
        title="Monthly Revenue"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:
    fig = px.bar(
        filtered_df,
        x="Month",
        y="Profit",
        title="Monthly Profit"
    )

    st.plotly_chart(fig, use_container_width=True)

left, right = st.columns(2)

with left:

    region_chart = (
        filtered_df.groupby("Region", as_index=False)["Revenue"]
        .sum()
    )

    fig = px.pie(
        region_chart,
        names="Region",
        values="Revenue",
        title="Revenue by Region"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    category_chart = (
        filtered_df.groupby("Category", as_index=False)["Orders"]
        .sum()
    )

    fig = px.bar(
        category_chart,
        x="Category",
        y="Orders",
        title="Orders by Category"
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.subheader("Dataset Preview")

st.dataframe(filtered_df, use_container_width=True)