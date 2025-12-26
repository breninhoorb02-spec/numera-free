import streamlit as st

LIMITE_FREE = 1  # 1 uso permitido

def pode_usar():
    if "usos" not in st.session_state:
        st.session_state.usos = 0

    return st.session_state.usos < LIMITE_FREE

def registrar_uso():
    if "usos" not in st.session_state:
        st.session_state.usos = 0

    st.session_state.usos += 1

def mostrar_upgrade():
    st.warning(
        "🚀 Você está usando a versão FREE. "
        "Faça upgrade para liberar uso ilimitado."
    )
