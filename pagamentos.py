import streamlit as st

CODIGO_PRO = "NUMERA-PRO-2025"

def acesso_pro():
    if "codigo_pro" not in st.session_state:
        st.session_state.codigo_pro = False

    st.subheader("🔐 Acesso PRO")

    codigo = st.text_input("Digite seu código PRO")

    if st.button("Validar código"):
        if codigo == CODIGO_PRO:
            st.session_state.codigo_pro = True
            st.success("Acesso PRO liberado 🚀")
        else:
            st.error("Código inválido")

    return st.session_state.codigo_pro
