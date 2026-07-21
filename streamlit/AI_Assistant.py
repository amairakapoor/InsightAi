import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Assistant", page_icon="🤖")

st.title("🤖 AI Business Assistant")

# ---------------- Load Dataset ---------------- #

if "data" in st.session_state:
    df = st.session_state["data"]
else:
    df = pd.read_csv("Data/sales_data.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

question = st.text_area(
    "Ask your business question",
    placeholder="Example: Give me business insights"
)

if st.button("Analyze"):

    if question.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    q = question.lower()

    # ---------------- Revenue ---------------- #

    if "total revenue" in q:

        st.metric("💰 Total Revenue", f"₹{df['Revenue'].sum():,}")

    elif "total profit" in q:

        st.metric("📈 Total Profit", f"₹{df['Profit'].sum():,}")

    elif "total orders" in q:

        st.metric("🛒 Total Orders", df["Orders"].sum())

    # ---------------- Best Region ---------------- #

    elif "highest revenue" in q or "best region" in q:

        result = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)

        st.success("🏆 Region Performance")

        st.dataframe(result)

        st.success(f"Best Region : {result.idxmax()}")

    # ---------------- Worst Region ---------------- #

    elif "lowest revenue" in q or "worst region" in q:

        result = df.groupby("Region")["Revenue"].sum().sort_values()

        st.success("📉 Lowest Revenue Region")

        st.dataframe(result)

        st.warning(f"Worst Region : {result.idxmin()}")

    # ---------------- Category ---------------- #

    elif "category" in q:

        result = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)

        st.subheader("📦 Category Performance")

        st.dataframe(result)

    # ---------------- Month ---------------- #

    elif "month" in q:

        result = df.groupby("Month")["Revenue"].sum()

        st.subheader("📅 Monthly Revenue")

        st.dataframe(result)

    # ---------------- Summary ---------------- #

    elif "summary" in q:

        st.subheader("📋 Executive Summary")

        st.write(f"**Total Revenue:** ₹{df['Revenue'].sum():,}")

        st.write(f"**Total Profit:** ₹{df['Profit'].sum():,}")

        st.write(f"**Total Orders:** {df['Orders'].sum()}")

        st.write(f"**Best Region:** {df.groupby('Region')['Revenue'].sum().idxmax()}")

        st.write(f"**Best Category:** {df.groupby('Category')['Revenue'].sum().idxmax()}")

    # ---------------- Insights ---------------- #

    elif "insight" in q:

        best_region = df.groupby("Region")["Revenue"].sum().idxmax()

        worst_region = df.groupby("Region")["Revenue"].sum().idxmin()

        best_category = df.groupby("Category")["Revenue"].sum().idxmax()

        st.subheader("💡 Business Insights")

        st.markdown(f"""
### Key Insights

✅ Total Revenue: **₹{df['Revenue'].sum():,}**

✅ Total Profit: **₹{df['Profit'].sum():,}**

✅ Best Performing Region: **{best_region}**

✅ Lowest Performing Region: **{worst_region}**

✅ Best Category: **{best_category}**

### Recommendations

- Increase investment in the best performing category.
- Improve marketing in the weakest region.
- Focus on increasing high-margin products.
- Monitor monthly sales trends.
- Increase customer engagement using offers.
""")

    # ---------------- Recommendation ---------------- #

    elif "recommend" in q:

        st.subheader("📈 Business Recommendations")

        st.write("""
1. Invest more in high-performing regions.

2. Improve sales in low-performing regions.

3. Increase stock of best-selling products.

4. Launch promotional offers.

5. Track monthly performance.

6. Improve customer retention.

7. Expand profitable categories.
""")

    # ---------------- Default ---------------- #

    else:

        st.info("""
Try asking:

• Total Revenue

• Total Profit

• Total Orders

• Highest Revenue Region

• Lowest Revenue Region

• Category Performance

• Monthly Revenue

• Summary

• Business Insights

• Business Recommendations
""")