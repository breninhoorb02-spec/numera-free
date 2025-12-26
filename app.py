import streamlit as st
from auth import login
from planos import pode_usar, registrar_uso, mostrar_upgrade
from parser_generico import extrair_pdf_generico

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
st.subheader("Conciliação bancária por PDF")

if not pode_usar():
    mostrar_upgrade()
    st.stop()

banco = st.selectbox(
    "Selecione o banco",
    ["Nubank", "Banco do Brasil", "Bradesco", "Caixa", "Outro"]
)

arquivo = st.file_uploader(
    "Envie o extrato bancário (PDF)",
    type=["pdf"]
)

if arquivo:
    with st.spinner("Processando extrato..."):
        df = extrair_pdf_generico(arquivo)
        registrar_uso()

    st.success("Extrato processado com sucesso!")
    st.dataframe(df)

    st.download_button(
        "⬇️ Baixar CSV",
        df.to_csv(index=False),
        file_name="numera_free.csv",
        mime="text/csv"
    )
