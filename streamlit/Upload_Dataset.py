import streamlit as st
import pandas as pd
if "data" in st.session_state:
    df = st.session_state["data"]
else:
    df = pd.read_csv("Data/sales_data.csv")
st.title("📂 Upload Dataset")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully!")

    st.subheader("Preview")

    st.dataframe(df, use_container_width=True)

    st.session_state["data"] = df

    st.write("Rows :", df.shape[0])
    st.write("Columns :", df.shape[1])

    st.subheader("Column Names")

    st.write(df.columns.tolist())