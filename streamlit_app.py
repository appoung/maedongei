import streamlit as st
from maedong import img_gen

pg = st.navigation([
    st.Page("app.py", icon="📈"),
    st.Page("admin_page.py", icon="🔧"),
])
pg.run()
