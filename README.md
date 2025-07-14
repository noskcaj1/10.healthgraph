# HealthGraph Radar

Sistema de visualização e análise de dados clínicos com múltiplos perfis de usuários (admin, profissional, leitor).

## Como executar

1. Crie um banco no Supabase com as tabelas:
   - `prontuarios`
   - `usuarios`
   - `auditoria_logs`
2. Configure o `.streamlit/secrets.toml` com sua `DB_URL`
3. Execute local com:
```bash
streamlit run app.py
```

Ou publique no [Streamlit Cloud](https://streamlit.io/cloud)

