import streamlit as st
import os
from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px
from healthgraph_input_front import form_input

def carregar_dados():
    engine = create_engine(os.getenv("DB_URL"))
    df = pd.read_sql("SELECT * FROM prontuarios", con=engine)
    return df

def render_dashboard():
    st.subheader("📊 Painel de Análise de Dados Clínicos")
    df = carregar_dados()
    if not df.empty:
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(px.histogram(df, x="idade", title="Distribuição de Idades"), use_container_width=True)
        with col2:
            st.plotly_chart(px.pie(df, names="sexo", title="Distribuição por Sexo"), use_container_width=True)
        st.dataframe(df, use_container_width=True)

def render_paginas():
    menu = ["📥 Cadastro", "📊 Análise"]
    escolha = st.sidebar.radio("Menu", menu)

    if escolha == "📥 Cadastro" and st.session_state["perfil"] in ["admin", "profissional"]:
        form_input()
    elif escolha == "📊 Análise":
        render_dashboard()
    else:
        st.warning("Acesso restrito ao seu perfil.")
