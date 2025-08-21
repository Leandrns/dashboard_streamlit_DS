import streamlit as st
import pandas as pd
import numpy as np

# Configurações iniciais
st.set_page_config(
    page_title="Meu Dashboard",
    page_icon="📊",
    layout="wide"
)

# Página 2 - Análise de Dados
st.title("📊 Análise de Dados")
st.write("Aqui futuramente estarão os gráficos da sua análise de dados.")

# Placeholder para gráfico de exemplo

dados = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.line_chart(dados)
st.bar_chart(dados)
