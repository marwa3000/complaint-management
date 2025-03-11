import streamlit as st
import pandas as pd
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

# ✅ تحميل بيانات الخدمة من ملف JSON
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("service_account.json", scopes=scopes)
client = gspread.authorize(creds)

# ✅ استبدل الـ ID بالـ ID الفعلي لملف Google Sheets الخاص بك
SPREADSHEET_ID = "1adEmI-XDrD0xKedCd8082tK09Vjr_pKa8viTbWFJBG4"
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

st.title("📋 نظام إدارة الشكاوى")

# ✅ إدخال بيانات الشكوى
complaint_id = st.text_input("رقم الشكوى")
product = st.text_input("اسم المنتج")
severity = st.selectbox("درجة الخطورة", ["High", "Medium", "Low"])
details = st.text_area("تفاصيل الشكوى")

if st.button("حفظ الشكوى"):
    new_data = [
        complaint_id,
        product,
        severity,
        details,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ]
    sheet.append_row(new_data)
    st.success("✅ تم حفظ الشكوى بنجاح!")

if st.button("عرض جميع الشكاوى"):
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    st.write(df)
