import streamlit as st
import pandas as pd

# Título simples
st.title("📍 Ocupações: Regional")
st.write("Análise de Salários e Complexidade")

# Dados organizados de forma direta
df = pd.DataFrame({
    'Setor': ['TI e Software', 'Ind. Farmacêutica', 'Metalurgia', 'Logística', 'Varejo'],
    'Complexidade': ['Alta', 'Alta', 'Média', 'Baixa', 'Baixa'],
    'Salário Médio': [7800, 7200, 4500, 2900, 2150]
})

# Exibindo os números principais primeiro
st.subheader("Resumo Regional")
st.metric("Média Salarial Geral", "R$ 4.890")

# Gráfico Nativo (Esse não deixa a tela branca)
st.bar_chart(df.set_index('Setor')['Salário Médio'])

# Tabela final
st.subheader("Lista de Setores")
st.dataframe(df)

st.caption("Dados focados em Caieiras e Franco da Rocha.")
