import streamlit as st

pg = st.navigation([
    st.Page("app.py", icon="📈"),
    st.Page("admin_page.py", icon="🔧"),
])
pg.run()
