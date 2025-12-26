import streamlit as st
from auth import login
from planos import verificar_plano

st.set_page_config(page_title="NUMERA", layout="centered")

if not login():
    st.stop()

plano = verificar_plano()

if plano == "FREE":
    from free.app_free import *
else:
    from pro.app_pro import *
