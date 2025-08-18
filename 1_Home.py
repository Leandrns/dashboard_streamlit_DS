import streamlit as st
import pandas as pd
import numpy as np

# Configurações iniciais
st.set_page_config(
    page_title="Meu Dashboard",
    page_icon="📊",
    layout="wide"
)

# Sidebar para navegação
st.sidebar.title("Navegação")
pagina = st.sidebar.radio("Ir para:", ["Apresentação Pessoal", "Análise de Dados"])

# Página 1 - Apresentação pessoal (Currículo)
if pagina == "Apresentação Pessoal":
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

# Página 2 - Análise de Dados
elif pagina == "Análise de Dados":
    st.title("📊 Análise de Dados")
    st.write("Aqui futuramente estarão os gráficos da sua análise de dados.")

    # Placeholder para gráfico de exemplo

    dados = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )

    st.line_chart(dados)
    st.bar_chart(dados)
