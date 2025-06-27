import streamlit as st
from datetime import datetime
import requests

API_URL = "http://127.0.0.1:8000"

def insert_tab():
    st.subheader("Add your Expenses")
    selected_date = st.date_input('Enter Date',datetime.today(),label_visibility="collapsed",key="insert-date")
    categories = ["Rent","Food","Shopping","Entertainment","Travel","Other"]

    if "row_count" not in st.session_state:
        st.session_state.row_count = 1

    if st.button("Add Another Expense"):
        st.session_state.row_count += 1
    with st.form(key="expense-form"):
        col1,col2,col3 = st.columns(3)

        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")
        
        expenses=[]

        for i in range(st.session_state.row_count):
            amount = 0.0
            notes = ""
            with col1:
                amount_input = st.number_input("amount",value = amount,min_value=0.0,label_visibility="collapsed",step=1.0,key=f"amount_{i}")
            with col2:
                category_input = st.selectbox("Category",options=categories,key = f"category_{i}",label_visibility="collapsed")
            with col3:
                notes_input = st.text_input("Notes",key=f"notes_{i}", value = notes,label_visibility="collapsed")

            expenses.append({
                "amount":amount_input,
                "category":category_input,
                "notes":notes_input
            })
        
        submit_button = st.form_submit_button()
        if submit_button:
            response = requests.post(f"{API_URL}/insert/{selected_date}",json = expenses)

            if response.status_code ==200:
                st.success("Expense Inserted successfully")
                
            else:
                st.error("Failed to Insert expenses.")





