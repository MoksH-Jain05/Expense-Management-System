import streamlit as st
from insert import insert_tab
from view_manage import view_manage_tab
from dashboard import dashboard_tab
from analytics import analytics_tab

st.title("Expense Tracking System")

tab1, tab2, tab3 =st.tabs(["Dashboard","Insert","View/Manage"])

with tab1:
    dashboard_tab()
    analytics_tab()

with tab2:
    insert_tab()

with tab3:
    view_manage_tab()
    
    
        
    