import streamlit as st
import pandas as pd

# Configuração da página para um visual mais limpo
st.set_page_config(page_title="App Ocupações", page_icon="💼")

st.title("💼 Ocupações: Inteligência Regional")
st.markdown("---")

# 1. Abas para organizar o conteúdo (Fica ótimo no celular)
tab1, tab2 = st.tabs(["🔍 Vagas e Setores", "📊 Análise Econômica"])

with tab1:
    st.subheader("Oportunidades em Destaque")
    
    # Simulação de dados mais completa
    dados = pd.DataFrame({
        'Setor': ['Tecnologia', 'Farmacêutica', 'Logística', 'Indústria', 'Comércio'],
        'Complexidade': ['💎 Alta', '💎 Alta', '📦 Baixa', '⚙️ Média', '📦 Baixa'],
        'Salário': [8200, 7500, 2900, 4800, 2200],
        'Empresas': ['Polo Industrial', 'Ind. Local', 'Centros Logísticos', 'Distrito Ind.', 'Centro']
    })

    # Usando Expansores para cada setor (Design muito moderno)
    for index, row in dados.iterrows():
        with st.expander(f"{row['Setor']} - {row['Salário']}"):
            st.write(f"**Complexidade:** {row['Complexidade']}")
            st.write(f"**Localização sugerida:** {row['Empresas']}")
            st.button(f"Ver detalhes {row['Setor']}", key=index)

with tab2:
    st.subheader("Indicadores de Caieiras e Franco")
    
    # Métricas com cores
    c1, c2 = st.columns(2)
    c1.metric("Média Salarial", "R$ 4.9k", "+5%")
    c2.metric("Nível de Emprego", "Alto", "Estável")

    # Gráfico nativo mas formatado
    st.markdown("#### Potencial de Ganho por Setor")
    st.bar_chart(dados.set_index('Setor')['Salário'])

st.markdown("---")
st.info("💡 **Dica Profissional:** Setores com '💎 Alta Complexidade' em nossa região apresentam os maiores crescimentos salariais nos últimos 24 meses.")

