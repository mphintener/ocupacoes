import streamlit as st
import pandas as pd

# Configurações visuais
st.set_page_config(page_title="Ocupações", layout="centered")

st.markdown("""
    <style>
    html, body, [class*="css"] { font-size: 14px !important; }
    h1 { font-size: 1.6rem !important; color: #2E86C1; }
    .stMetric { background-color: #f0f2f6; padding: 10px; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📍 Ocupações: Regional")

# Dados
dados = pd.DataFrame({
    'Salário': [7800, 7200, 2900, 4500, 2150]
}, index=['TI', 'Farmacêutica', 'Logística', 'Metalurgia', 'Varejo'])

# 1. Métricas
c1, c2 = st.columns(2)
c1.metric("Média Salarial", "R$ 4.910")
c2.metric("Setores", "5")

# 2. Gráfico Nativo (Mais simples, não dá erro)
st.write("### Comparativo de Salários")
st.bar_chart(dados)

# 3. Tabela
st.write("### Lista Detalhada")
st.table(dados)
