import streamlit as st
import pandas as pd
import numpy as np

# Configurações iniciais
st.set_page_config(
    page_title="Meu Dashboard",
    page_icon="📊",
    layout="wide"
)

# Página 1 - Apresentação pessoal (Currículo)

st.title("👨‍💻 Apresentação Pessoal")
st.subheader("Leandro Souza")  # aqui você coloca seu nome
st.write("""
Olá! Sou desenvolvedor front-end sênior focado em **React** e apaixonado por tecnologia.

Aqui você pode incluir informações como:
- Experiência profissional
- Habilidades técnicas
- Projetos relevantes
- Formação acadêmica
""")

# Exemplo de colunas para layout
col1, col2 = st.columns(2)
with col1:
    st.subheader("Habilidades Técnicas")
    st.write("- React, JavaScript, TypeScript")
    st.write("- Python, Streamlit, Pandas")
    st.write("- Node.js, Express")
with col2:
    st.subheader("Contato")
    st.write("📧 email@exemplo.com")
    st.write("🔗 [LinkedIn](https://linkedin.com)")
    st.write("💻 [GitHub](https://github.com)")
