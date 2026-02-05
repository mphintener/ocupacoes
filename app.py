import streamlit as st
import pandas as pd

# 1. Configuração de Página e Estilo "Dark/Clean"
st.set_page_config(page_title="Ocupações", layout="centered")

st.markdown("""
    <style>
    /* Reset de fontes e cores */
    html, body, [class*="css"] { font-size: 14px !important; font-family: 'Helvetica', sans-serif; }
    .block-container { padding: 1rem !important; background-color: #f8f9fa; }
    
    /* Título mais elegante */
    h1 { color: #1E3A8A; font-size: 1.4rem !important; font-weight: 800; text-align: center; margin-bottom: 20px; }
    
    /* Estilização dos 'Cards' de dados */
    .setor-card {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #3B82F6;
        margin-bottom: 10px;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
    }
    .status-alta { border-left-color: #10B981; }
    .status-media { border-left-color: #F59E0B; }
    .status-baixa { border-left-color: #3B82F6; }
    
    .label { font-size: 0.8rem; color: #6B7280; text-transform: uppercase; }
    .valor { font-size: 1.1rem; font-weight: bold; color: #111827; }
    </style>
    """, unsafe_allow_html=True)

st.title("📍 Ocupações Regional")

# 2. Dados reais organizados
dados = [
    {"setor": "TI e Software", "comp": "Alta", "salario": "R$ 7.800", "estilo": "status-alta"},
    {"setor": "Farmacêutica", "comp": "Alta", "salario": "R$ 7.200", "estilo": "status-alta"},
    {"setor": "Metalurgia", "comp": "Média", "salario": "R$ 4.500", "estilo": "status-media"},
    {"setor": "Logística", "comp": "Baixa", "salario": "R$ 2.900", "estilo": "status-baixa"},
    {"setor": "Varejo", "comp": "Baixa", "salario": "R$ 2.150", "estilo": "status-baixa"},
]

# 3. Exibição em formato de "Cards" (Muito melhor que tabela no celular)
st.write("### Oportunidades por Complexidade")

for item in dados:
    st.markdown(f"""
    <div class="setor-card {item['estilo']}">
        <div class="label">{item['setor']} • Complexidade {item['comp']}</div>
        <div class="valor">Média Salarial: {item['salario']}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Dados baseados em análises de Caieiras e Franco da Rocha.")

