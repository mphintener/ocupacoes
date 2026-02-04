import streamlit as st
import pandas as pd

st.set_page_config(page_title="App Ocupações", page_icon="🚀")

st.title("🚀 Ocupações: Franco da Rocha & Caieiras")
st.markdown("### Inteligência de Mercado e Complexidade Económica")

# Tabela de dados para o teu app
dados = pd.DataFrame({
    'Sector': ['TI e Software', 'Ind. Farmacêutica', 'Metalurgia', 'Logística', 'Varejo'],
    'Complexidade': ['Alta', 'Alta', 'Média', 'Baixa', 'Baixa'],
    'Salário Médio (R$)': [7800, 7200, 4500, 2900, 2150]
})

st.write("Abaixo, a relação entre sectores estratégicos e salários na região:")
st.table(dados)

st.info("Este app utiliza dados processados via Python para apoiar a carreira do trabalhador local.")

