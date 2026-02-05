import streamlit as st
import pandas as pd

# Configuração de página
st.set_page_config(page_title="Ocupações", layout="centered")

# CSS para encolher TUDO (Fontes e Espaços)
st.markdown("""
    <style>
    /* Diminui o tamanho da fonte base */
    html, body, [class*="css"] { font-size: 13px !important; }
    /* Reduz o espaço no topo da página */
    .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; }
    /* Ajusta títulos */
    h1 { font-size: 1.5rem !important; color: #2E86C1; }
    h3 { font-size: 1.1rem !important; }
    /* Estiliza o filtro para não ficar "gigante" */
    .stSelectbox { margin-bottom: -15px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📍 Ocupações: Franco/Caieiras")

# Dados de Exemplo (Depois conectamos seu CSV real)
dados = pd.DataFrame({
    'Setor': ['TI', 'Farmacêutica', 'Logística', 'Metalurgia', 'Varejo'],
    'Complexidade': ['Alta', 'Alta', 'Baixa', 'Média', 'Baixa'],
    'Salário': [7800, 7200, 2900, 4500, 2150]
})

# Filtro Único e Compacto
setor_alvo = st.selectbox("Selecione o Setor:", ['Todos'] + list(dados['Setor'].unique()))

if setor_alvo != 'Todos':
    df_exibir = dados[dados['Setor'] == setor_alvo]
else:
    df_exibir = dados

# Exibição simplificada
st.write("### Resumo de Ganhos")
st.table(df_exibir) # .table ocupa menos espaço visual que .dataframe no mobile

st.info("Setores de **Alta Complexidade** pagam melhor na região.")
