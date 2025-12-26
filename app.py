import streamlit as st
from auth import login
from pagamentos import acesso_pro

st.set_page_config(page_title="NUMERA", layout="centered")

if not login():
    st.stop()

plano = verificar_plano()

if plano == "FREE":
    st.info("Você está no plano FREE")
    acesso = acesso_pro()
    if acesso:
        from pro.app_pro import *
    else:
        from free.app_free import *
else:
    from pro.app_pro import *
