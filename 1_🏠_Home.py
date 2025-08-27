import streamlit as st

st.set_page_config(
    page_title="Início",
    layout="wide"
)

st.sidebar.markdown("<p style='text-align: center; font-size: 12px'>Desenvolvido por <strong>Leandro Souza<strong></p>", unsafe_allow_html=True)

st.title("📌 Dashboard de Análise de CSAT")
st.write("""
Bem-vindo ao dashboard! 🚀  

Aqui você encontrará:
- Uma página **sobre mim**, com minha apresentação e currículo.
- Uma página de **análise de dados**, mostrando insights sobre satisfação do cliente (CSAT).
""")
