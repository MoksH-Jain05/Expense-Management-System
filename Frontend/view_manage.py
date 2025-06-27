import streamlit as st
from datetime import datetime
import requests

API_URL = "http://127.0.0.1:8000"

def view_manage_tab():
    st.subheader("View/Delete")

    selected_date = st.date_input("Enter Date", datetime.today(), label_visibility="collapsed",key="date")
    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    if response.status_code != 200:
        st.error("Failed to fetch expenses.")
        return

    expenses = response.json()
    if not expenses:
        st.info("No expenses found.")
        return

    checked_ids = []

    with st.form("delete_form"):
        col1, col2, col3, col4 = st.columns(4)
        col1.write("Check to Delete")
        col2.write("Amount")
        col3.write("Category")
        col4.write("Note")

        for expense in expenses:
            col1, col2, col3, col4 = st.columns(4)
            checked = col1.checkbox("check", key=f"chk_{expense['id']}", label_visibility="collapsed")
            col2.write(expense["amount"])
            col3.write(expense["category"])
            col4.write(expense["notes"])
            if checked:
                checked_ids.append(expense["id"])

        submitted = st.form_submit_button("Delete Selected")

    if submitted:
        if not checked_ids:
            st.warning("No rows selected.")
        else:
            failed = []
            for id in checked_ids:
                del_response = requests.delete(f"{API_URL}/delete/{id}")
                if del_response.status_code != 200:
                    failed.append(id)
            if not failed:
                st.success("Selected expenses deleted successfully.")
                st.rerun()
            else:
                st.error(f"Failed to delete some IDs: {failed}")
