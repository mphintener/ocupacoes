import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Ocupações Dinâmico", layout="wide")

st.title("🚀 Ocupações: Franco da Rocha & Caieiras")
st.markdown("### Painel Dinâmico de Mercado e Qualificação")

# 1. Base de Dados (Pode ser substituída pelo seu CSV do GitHub)
dados = pd.DataFrame({
    'Setor': ['TI e Software', 'Ind. Farmacêutica', 'Logística', 'Metalurgia', 'Varejo', 'Construção'],
    'Complexidade': ['Alta', 'Alta', 'Baixa', 'Média', 'Baixa', 'Média'],
    'Salário Médio': [7800, 7200, 2900, 4500, 2150, 3800],
    'Vagas Abertas': [12, 8, 45, 15, 60, 20]
})

# 2. Filtros na Barra Lateral
st.sidebar.header("Filtre sua busca")
setores_selecionados = st.sidebar.multiselect("Escolha os Setores", options=dados['Setor'].unique(), default=dados['Setor'].unique())
df_filtrado = dados[dados['Setor'].isin(setores_selecionados)]

# 3. Cartões de Métricas (Destaque)
col1, col2, col3 = st.columns(3)
col1.metric("Vagas Disponíveis", df_filtrado['Vagas Abertas'].sum())
col2.metric("Média Salarial Regional", f"R$ {df_filtrado['Salário Médio'].mean():.2f}")
col3.metric("Setor com mais Vagas", df_filtrado.loc[df_filtrado['Vagas Abertas'].idxmax(), 'Setor'])

# 4. Gráfico de Barras Interativo
st.subheader("📊 Comparativo: Setor vs Salário")
fig = px.bar(df_filtrado, x='Setor', y='Salário Médio', color='Complexidade',
             title="Salário Médio por Setor e Nível de Complexidade",
             color_discrete_map={'Alta': '#2ecc71', 'Média': '#f1c40f', 'Baixa': '#3498db'})
st.plotly_chart(fig, use_container_width=True)

# 5. Tabela Detalhada
st.subheader("📋 Detalhes das Ocupações")
st.dataframe(df_filtrado, use_container_width=True)

st.info("💡 **Dica:** Setores em VERDE (Alta Complexidade) exigem cursos técnicos ou superiores, mas pagam até 3x mais na região.")
