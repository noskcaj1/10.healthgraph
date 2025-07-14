import streamlit as st
from healthgraph_app_multi import render_paginas
from healthgraph_input_secure import login

st.set_page_config(page_title="HealthGraph Radar", layout="wide")

if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    if login():
        st.session_state["logado"] = True
        st.experimental_rerun()
else:
    render_paginas()
