import streamlit as st
import pandas as pd

# Configuração de página
st.set_page_config(page_title="Ocupações Regionais", page_icon="📍")

# Título e Introdução
st.title("📍 Ocupações: Cinturão Norte")
st.markdown("Cajamar • Caieiras • Franco da Rocha • Francisco Morato")

# 1. Base de Dados Regional
# Aqui simulamos os dados que você analisou do CAGED/PNADC
data = {
    'Cidade': ['Cajamar', 'Cajamar', 'Caieiras', 'Caieiras', 'Franco da Rocha', 'Franco da Rocha', 'Francisco Morato', 'Francisco Morato'],
    'Setor': ['Logística Avançada', 'E-commerce', 'Ind. Papel/Celulose', 'Metalurgia', 'Serviços Médicos', 'Gestão Pública', 'Comércio Varejista', 'Construção Civil'],
    'Complexidade': ['Média', 'Alta', 'Alta', 'Média', 'Alta', 'Média', 'Baixa', 'Baixa'],
    'Salário': [3200, 7500, 6800, 4200, 8500, 5200, 2150, 2800]
}
df = pd.DataFrame(data)

# 2. Filtro de Busca por Cidade (Interatividade)
st.markdown("### 🔍 Filtrar por Cidade")
cidade_selecionada = st.selectbox("Selecione o município:", ["Todas as Cidades"] + list(df['Cidade'].unique()))

# Lógica de Filtro
if cidade_selecionada != "Todas as Cidades":
    df_filtrado = df[df['Cidade'] == cidade_selecionada]
else:
    df_filtrado = df

# 3. Organização por Abas
tab1, tab2 = st.tabs(["📋 Lista de Ocupações", "📊 Resumo por Complexidade"])

with tab1:
    st.write(f"Exibindo resultados para: **{cidade_selecionada}**")
    
    # Criando os "Cards" por complexidade
    for _, row in df_filtrado.iterrows():
        # Emoji por complexidade
        cor = "💎" if row['Complexidade'] == 'Alta' else "⚙️" if row['Complexidade'] == 'Média' else "📦"
        
        with st.expander(f"{cor} {row['Setor']} - R$ {row['Salário']}"):
            st.write(f"**Cidade:** {row['Cidade']}")
            st.write(f"**Nível:** {row['Complexidade']} Complexidade")
            st.caption("Fonte: Estimativa baseada em dados reais da região.")

with tab2:
    st.subheader("Análise de Complexidade")
    # Gráfico de barras que muda conforme a cidade escolhida
    contagem = df_filtrado.groupby('Complexidade')['Salário'].mean().sort_values()
    st.bar_chart(contagem)
    st.info("O gráfico acima mostra o salário médio por nível de complexidade na seleção atual.")

st.markdown("---")
st.caption("App Ocupações v2.0 - Foco em Desenvolvimento Regional")

