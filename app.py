import streamlit as st
import pandas as pd

# Ajuste de fonte e layout para celular
st.set_page_config(page_title="Ocupações", layout="centered")

st.markdown("""
    <style>
    html, body, [class*="css"] { font-size: 14px !important; }
    h1 { font-size: 1.5rem !important; color: #2E86C1; }
    .stChart { background-color: white; border: 1px solid #ddd; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📍 Ocupações: Regional")

# Dados simplificados
dados = pd.DataFrame({
    'Salário': [7800, 7200, 2900, 4500, 2150]
}, index=['TI', 'Farma', 'Logíst', 'Metal', 'Varejo'])

# 1. Indicadores simples (Texto em negrito para não bugar)
st.write(f"**Média Salarial:** R$ 4.910 | **Setores:** 5")

st.write("---")

# 2. Gráfico Nativo (O mais leve de todos)
st.write("### Nível Salarial")
st.bar_chart(dados)

# 3. Tabela de Ocupações
st.write("### Detalhes")
st.table(dados)
