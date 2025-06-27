import streamlit as st
from datetime import datetime
import requests
import pandas as pd
API_URL = "http://127.0.0.1:8000"

def analytics_tab():
    st.subheader("Expense Breakdown By category")
    col1,col2 = st.columns(2)
    with col1:
        start_date=st.date_input("Start Date", datetime.today(),key="start-date")
    
    with col2:
        end_date =st.date_input("End Date", datetime.today(),key='end-date')


    if st.button("Get Analytics"):
        if start_date == end_date:
            st.warning("Please change one of the date")
        else:
            payload = {
                "start_date":start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d")
            }

            response = requests.post(f"{API_URL}/analytics/",json=payload)
            response = response.json()

            data ={
                "Category":list(response.keys()),
                "Total":[response[category]["total"]for category in response],
                "Percentage":[response[category]['percentage']for category in response]
            }

            df = pd.DataFrame(data)
            df_sorted = df.sort_values(by="Percentage",ascending =False)

            st.bar_chart(data =df_sorted.set_index("Category")["Percentage"],width=0,height=0,use_container_width=True)
            
            df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
            df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)

            st.table(df_sorted)

