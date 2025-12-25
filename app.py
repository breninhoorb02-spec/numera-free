import streamlit as st

st.set_page_config(
    page_title="NUMERA FREE",
    layout="centered"
)

# Forçar tema claro
st.markdown("""
<style>
.main {
    background-color: #ffffff;
    color: #000000;
}
</style>
""", unsafe_allow_html=True)

st.title("NUMERA – Versão FREE")
st.subheader("Plataforma de conciliação bancária por PDF")

st.success("✅ App carregado com sucesso!")

st.info("""
Este é o primeiro teste da NUMERA FREE.
Se você está vendo esta mensagem, o app está funcionando.
""")
