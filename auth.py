import streamlit as st

def login():
    if "logado" not in st.session_state:
        st.session_state.logado = False

    if not st.session_state.logado:
        st.title("Login NUMERA")

        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")

        if st.button("Entrar"):
            if usuario and senha:
                st.session_state.logado = True
                st.experimental_rerun()

        return False

    return True
