import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração de página
st.set_page_config(page_title="Ocupações", layout="centered")

# CSS para manter a fonte pequena e o visual limpo
st.markdown("""
    <style>
    html, body, [class*="css"] { font-size: 13px !important; }
    .block-container { padding-top: 1rem !important; }
    h1 { font-size: 1.6rem !important; color: #2E86C1; margin-bottom: 0px; }
    h3 { font-size: 1.1rem !important; margin-top: 10px; }
    .stMetric { background-color: #f0f2f6; padding: 5px; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📍 Ocupações: Regional")

# Dados (A base do seu App 1)
dados = pd.DataFrame({
    'Setor': ['TI', 'Farmacêutica', 'Logística', 'Metalurgia', 'Varejo'],
    'Complexidade': ['Alta', 'Alta', 'Baixa', 'Média', 'Baixa'],
    'Salário': [7800, 7200, 2900, 4500, 2150]
})

# 1. Indicadores (Métricas) em colunas para economizar espaço
col1, col2 = st.columns(2)
col1.metric("Salário Médio", f"R$ {dados['Salário'].mean():.0f}")
col2.metric("Nº de Setores", len(dados))

# 2. Gráfico de Barras (Agora com altura reduzida para caber na tela)
st.write("### Comparativo Salarial")
fig = px.bar(dados, x='Setor', y='Salário', color='Complexidade', 
             height=250, # Altura menor para não "sumir" com o resto
             color_discrete_map={'Alta': '#2ecc71', 'Média': '#f1c40f', 'Baixa': '#3498db'})
fig.update_layout(margin=dict(l=10, r=10, t=10, b=10), showlegend=False)
st.plotly_chart(fig, use_container_width=True)

# 3. A Tabela de Ocupações (O que você já estava vendo)
st.write("### Detalhes das Ocupações")
st.dataframe(dados, use_container_width=True)

st.info("Role para baixo para ver a lista completa.")
