import streamlit as st
import streamlit_book as stb

# Streamlit webpage properties
st.set_page_config(page_title="Streamlit Python Framework", page_icon="🐦")
st.markdown(""" <style>#MainMenu {visibility: hidden;}footer {visibility: hidden;}</style> """, unsafe_allow_html=True)

# Streamlit book properties
stb.set_book_config(path="slides")
