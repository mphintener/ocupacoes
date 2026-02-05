import streamlit as st
import pandas as pd

# Configuração de página
st.set_page_config(page_title="Inteligência Regional", layout="centered")

# 1. Título Pequeno e Estilizado (Sem st.title para não gigantar)
st.markdown("""
    <div style='text-align: center; padding-bottom: 20px;'>
        <h2 style='font-size: 1.4rem; color: #1e3a8a; margin-bottom: 0px;'>📈 Inteligência de Mercado</h2>
        <p style='font-size: 0.9rem; color: #64748b;'>Cajamar • Caieiras • Franco • Morato</p>
    </div>
    """, unsafe_allow_html=True)

# 2. Dados com Complexidade Definida
dados = [
    {"cid": "Cajamar", "vagas": 1200, "sal": 8500, "setor": "Tecnologia", "comp": "Alta", "cor": "#10b981", "icon": "💎"},
    {"cid": "Caieiras", "vagas": 450, "sal": 4800, "setor": "Indústria", "comp": "Média", "cor": "#f59e0b", "icon": "⚙️"},
    {"cid": "Franco", "vagas": 320, "sal": 3100, "setor": "Serviços", "comp": "Média", "cor": "#f59e0b", "icon": "⚙️"},
    {"cid": "Morato", "vagas": 780, "sal": 2150, "setor": "Comércio", "comp": "Baixa", "cor": "#3b82f6", "icon": "📦"}
]

# 3. Filtro Compacto
cidade_alvo = st.selectbox("Filtrar por Município:", ["Todas"] + [d['cid'] for d in dados])

# 4. Exibição em Cards com Destaque de Complexidade
st.write("### Ocupações e Complexidade")

for d in dados:
    if cidade_alvo == "Todas" or cidade_alvo == d['cid']:
        # Criando o Card com destaque visual na complexidade
        st.markdown(f"""
            <div style='border: 1px solid #e2e8f0; border-radius: 10px; padding: 15px; margin-bottom: 10px; background-color: white;'>
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <span style='font-weight: bold; font-size: 1.1rem; color: #1e3a8a;'>{d['cid']}</span>
                    <span style='background-color: {d['cor']}; color: white; padding: 2px 10px; border-radius: 15px; font-size: 0.7rem; font-weight: bold;'>
                        {d['icon']} {d['comp'].upper()}
                    </span>
                </div>
                <div style='margin-top: 10px; font-size: 0.9rem;'>
                    <b>Setor:</b> {d['setor']}<br>
                    <b>Média Salarial:</b> <span style='color: #059669; font-weight: bold;'>R$ {d['sal']:,}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

# 5. Legenda e Fontes
st.divider()
st.markdown("""
    <div style='font-size: 0.8rem; color: #64748b;'>
        <b>Legenda:</b> 💎 Alta | ⚙️ Média | 📦 Baixa<br>
        <b>Fontes:</b> Microdados Novo CAGED e RAIS (Dados Municipais)
    </div>
    """, unsafe_allow_html=True)

