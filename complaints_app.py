import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime  # Import datetime module

# ✅ Load Google Cloud credentials from Streamlit Secrets
google_creds = st.secrets["google"]

# ✅ Authenticate with Google Sheets API
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_info(google_creds, scopes=scopes)
client = gspread.authorize(creds)

# ✅ Google Sheets ID (Replace with your actual sheet ID)
SPREADSHEET_ID = "1adEmI-XDrD0xKedCd8082tK09Vjr_pKa8viTbWFJBG4"
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

# ✅ Streamlit App UI
st.title("📋 Complaints Management System")

st.header("📝 Submit a New Complaint")

complaint_id = st.text_input("Complaint ID")
product = st.text_input("Product Name")
severity = st.selectbox("Severity Level", ["High", "Medium", "Low"])
details = st.text_area("Complaint Details")

# ✅ Get the current date and time
date_submitted = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # YYYY-MM-DD HH:MM:SS format

if st.button("Submit Complaint"):
    if complaint_id and product and details:
        new_data = [date_submitted, complaint_id, product, severity, details]
        sheet.append_row(new_data)
        st.success(f"✅ Complaint Submitted Successfully on {date_submitted}!")
    else:
        st.error("❌ Please fill all required fields!")

st.header("📄 View Submitted Complaints")
if st.button("Load Complaints"):
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    st.write(df)



