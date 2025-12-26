import streamlit as st
from planos import pode_usar, registrar_uso, mostrar_upgrade
from classificador import classificar
from parser_nubank import extrair_nubank

st.title("NUMERA FREE 🆓")

if not pode_usar():
    mostrar_upgrade()
    st.stop()

arquivo = st.file_uploader("Enviar extrato Nubank (PDF)", type=["pdf"])

if arquivo:
    df = extrair_nubank(arquivo)
    df["Categoria"] = df.apply(
        lambda x: classificar(x["Descrição"], x["Valor"]), axis=1
    )

    registrar_uso()

    st.success("Processado com sucesso (FREE)")
    st.dataframe(df)
