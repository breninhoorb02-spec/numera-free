import streamlit as st
from auth import login
from planos import pode_usar, registrar_uso, mostrar_upgrade

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

if not pode_usar():
    mostrar_upgrade()
    st.stop()

if st.button("Simular uso do sistema"):
    registrar_uso()
    st.success("Uso registrado com sucesso!")
