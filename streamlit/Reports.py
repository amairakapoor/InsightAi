import streamlit as st
import pandas as pd
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from openpyxl import Workbook

st.title("📄 Reports")

# Load data
if "data" in st.session_state:
    df = st.session_state["data"]
else:
    df = pd.read_csv("Data/sales_data.csv")

st.subheader("Dataset Preview")
st.dataframe(df, use_container_width=True)

# ---------------- CSV ----------------
csv = df.to_csv(index=False)

st.download_button(
    "📥 Download CSV",
    csv,
    file_name="Business_Report.csv",
    mime="text/csv"
)

# ---------------- Excel ----------------
wb = Workbook()
ws = wb.active
ws.title = "Business Report"

ws.append(list(df.columns))

for row in df.values.tolist():
    ws.append(row)

excel_file = BytesIO()
wb.save(excel_file)

st.download_button(
    "📊 Download Excel",
    excel_file.getvalue(),
    file_name="Business_Report.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# ---------------- PDF ----------------
pdf_buffer = BytesIO()

doc = SimpleDocTemplate(pdf_buffer)

table_data = [list(df.columns)] + df.values.tolist()

table = Table(table_data)

table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('BACKGROUND', (0,1), (-1,-1), colors.beige),
    ('ALIGN', (0,0), (-1,-1), 'CENTER')
]))

doc.build([table])

st.download_button(
    "📄 Download PDF",
    pdf_buffer.getvalue(),
    file_name="Business_Report.pdf",
    mime="application/pdf"
)