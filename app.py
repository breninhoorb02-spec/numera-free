import streamlit as st
from auth import login

st.set_page_config(
    page_title="NUMERA FREE",
    layout="centered"
)

st.markdown("""
<style>
.main {
    background-color: #ffffff;
    color: #000000;
}
</style>
""", unsafe_allow_html=True)

if not login():
    st.stop()

st.title("NUMERA – Versão FREE")
st.subheader("Plataforma de conciliação bancária por PDF")

st.success("✅ Login realizado com sucesso!")
