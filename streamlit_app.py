import streamlit as st
import pandas as pd
# from main import spreadsheets, lint
from io import BytesIO


st.set_page_config(
    page_title="",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!",
    },
)


def df_to_xlsx(df):
    byte_xlsx = BytesIO()
    writer_xlsx = pd.ExcelWriter(byte_xlsx, engine="xlsxwriter")
    df.to_excel(writer_xlsx, index=False, sheet_name="Sheet1")
    ## -----必要に応じてexcelのフォーマット等を設定-----##
    workbook = writer_xlsx.book
    worksheet = writer_xlsx.sheets["Sheet1"]
    format1 = workbook.add_format({"num_format": "0.00"})
    worksheet.set_column("A:A", None, format1)
    writer_xlsx.close()
    ## ---------------------------------------------##
    workbook = writer_xlsx.book
    out_xlsx = byte_xlsx.getvalue()
    return out_xlsx

# xlsx_test = df_to_xlsx(df)

# st.download_button(label="Download", data=xlsx_test, file_name="チューター制.xlsx")


st.text("hogehoge")