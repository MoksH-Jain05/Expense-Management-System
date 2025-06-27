import streamlit as st
import requests 
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
import pandas as pd

API_URL = "http://127.0.0.1:8000"

def dashboard_tab():
    selected_date = st.date_input("Enter Date", value=datetime.today(),label_visibility="collapsed",key="dashboard-date")
    selected_year = selected_date.year
    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    if response.status_code==200:
        expenses = response.json()
        if expenses:    
            col1,col2 = st.columns(2)
            with col1:
                df = pd.DataFrame(expenses)
                total = df["amount"].sum()
                previous_date = selected_date - timedelta(days=1)
                response_pre = requests.get(f"{API_URL}/expenses/{previous_date}")
                expenses_pre = response_pre.json()
                df_pre= pd.DataFrame(expenses_pre)
                if not df_pre.empty and "amount" in df_pre.columns:
                    total_pre = round(df_pre["amount"].sum())
                else:
                    total_pre = 0

                if total != 0:
                    delta = round(((total - total_pre) / total) * 100, 1)
                else:
                    delta = 0.0  

                st.metric("Total Amount",value = f"₹{total:.2f}",delta=f"{delta}%",border=True,help="Compared to previous day")
                category_summary =df.groupby("category")["amount"]
                st.write("Category-Wise Summary")
                category=[]
                amount =[]
                for key,data in category_summary:
                    category.append(key)
                amount = df.groupby("category")["amount"].sum()
                st.table(amount)

            with col2:
                fig,ax = plt.subplots()
                ax.pie(amount,labels = category,autopct='%1.1f%%',)
                st.pyplot(fig)
        else:
            st.info(f"No Record for this {selected_date}")

    
    st.subheader("Expenses by Month")

    response = requests.get(f"{API_URL}/analytics_month/{selected_year}")
    if response.status_code==200:
        data = response.json()
        if data:
            df = pd.DataFrame(data)
            df["total"] =round(df["total"],1)
            df.rename(columns ={
                "month": 'Month Number',
                "month_name": 'Month Name',
                "total": 'Total'
            }, inplace = True)
            df.sort_values(by='Month Number',inplace=True)
            df.set_index("Month Number",inplace=True)
            st.dataframe(df,hide_index=True)
            st.bar_chart(data=df.set_index("Month Name")['Total'], width=0, height=0, use_container_width=True)

            df["Total"] = df["Total"].map("{:.2f}".format)
            









