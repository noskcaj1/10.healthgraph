import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os

def login():
    st.sidebar.subheader("🔐 Login de Acesso")
    usuario = st.sidebar.text_input("Usuário")
    senha = st.sidebar.text_input("Senha", type="password")

    if st.sidebar.button("Entrar"):
        engine = create_engine(os.getenv("DB_URL"))
        query = "SELECT * FROM usuarios WHERE usuario = %s AND senha = %s"
        df = pd.read_sql(query, con=engine, params=(usuario, senha))

        if not df.empty:
            st.session_state["usuario"] = df.iloc[0]["usuario"]
            st.session_state["perfil"] = df.iloc[0]["perfil"]
            st.success(f"✅ Acesso liberado como {df.iloc[0]['perfil']}")
            return True
        else:
            st.error("❌ Usuário ou senha inválidos.")
            return False
    return False
