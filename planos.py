import streamlit as st

def verificar_plano():
    if "codigo_pro" in st.session_state and st.session_state.codigo_pro:
        return "PRO"
    return "FREE"

def pode_usar():
    if "usos" not in st.session_state:
        st.session_state.usos = 0
    return st.session_state.usos < 1

def registrar_uso():
    st.session_state.usos += 1

def mostrar_upgrade():
    st.warning("🚀 Limite FREE atingido. Faça upgrade para o plano PRO.")
