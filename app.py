import streamlit as st
from auth import login
from planos import pode_usar, registrar_uso, mostrar_upgrade
from classificador import classificar

from parser_nubank import extrair_nubank
from parser_bb import extrair_bb
from parser_bradesco import extrair_bradesco
from parser_caixa import extrair_caixa
from parser_generico import extrair_pdf_generico

st.set_page_config(page_title="NUMERA FREE", layout="centered")

st.markdown("""
<style>
.main { background-color: #ffffff; color: #000000; }
</style>
""", unsafe_allow_html=True)

if not login():
    st.stop()

st.title("NUMERA – Versão FREE")
st.subheader("Conciliação bancária automática por banco")

if not pode_usar():
    mostrar_upgrade()
    st.stop()

banco = st.selectbox(
    "Selecione o banco",
    ["Nubank", "Banco do Brasil", "Bradesco", "Caixa", "Outro"]
)

arquivo = st.file_uploader("Envie o extrato bancário (PDF)", type=["pdf"])

if arquivo:
    with st.spinner("Processando extrato..."):
        if banco == "Nubank":
            df = extrair_nubank(arquivo)
        elif banco == "Banco do Brasil":
            df = extrair_bb(arquivo)
        elif banco == "Bradesco":
            df = extrair_bradesco(arquivo)
        elif banco == "Caixa":
            df = extrair_caixa(arquivo)
        else:
            df = extrair_pdf_generico(arquivo)

        df["Categoria"] = df.apply(
            lambda x: classificar(x["Descrição"], x["Valor"]), axis=1
        )

        registrar_uso()

    st.success("Conciliação concluída com sucesso!")
    st.dataframe(df)

    st.download_button(
        "⬇️ Baixar CSV conciliado",
        df.to_csv(index=False),
        "numera_free_conciliado.csv",
        "text/csv"
    )
