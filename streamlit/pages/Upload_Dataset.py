import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import streamlit as st
import pandas as pd
from utils.auth import require_login
from utils.api import upload_dataset, get_datasets

st.set_page_config(page_title="Upload Dataset — InsightAI", page_icon="📁", layout="wide")
require_login()

st.title("📁 Upload Dataset")
st.caption("CSV or Excel files are cleaned, type-inferred, and made instantly queryable from Dashboard/AI Assistant.")

uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx", "xls"])

if uploaded_file is not None:
    if st.button("Upload & process", type="primary"):
        with st.spinner("Cleaning data and preparing table..."):
            result = upload_dataset(uploaded_file.name, uploaded_file.getvalue())

        if result:
            st.success(
                f"Uploaded! Created table `{result['table_name']}` with "
                f"{result['n_rows']} rows and {result['n_columns']} columns."
            )
            st.subheader("Preview")
            st.dataframe(pd.DataFrame(result["preview"]), use_container_width=True)

            st.session_state["active_table"] = result["table_name"]
            st.info("Table set as active — head to Dashboard, Analytics, or AI Assistant to query it.")

st.divider()
st.subheader("Available datasets")
datasets = get_datasets()
if datasets:
    st.table(pd.DataFrame(datasets))
else:
    st.caption("Could not load dataset list.")
