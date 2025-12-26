import streamlit as st
from classificador import classificar

from parser_nubank import extrair_nubank
from parser_bb import extrair_bb
from parser_bradesco import extrair_bradesco
from parser_caixa import extrair_caixa
from parser_generico import extrair_pdf_generico

st.title("NUMERA PRO 💼")

banco = st.selectbox(
    "Selecione o banco",
    ["Nubank", "Banco do Brasil", "Bradesco", "Caixa", "Outro"]
)

arquivo = st.file_uploader("Enviar extrato bancário (PDF)", type=["pdf"])

if arquivo:
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

    st.success("Conciliação PRO concluída 🚀")
    st.dataframe(df)
