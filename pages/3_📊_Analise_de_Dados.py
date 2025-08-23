import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Análise de Dados CSAT",
    layout="wide"
)

# Seleção da subpágina
subpagina = st.sidebar.selectbox(
    "Selecione uma seção",
    ["Contextualização e Objetivo", "Entendendo o Dataset", "Dashboard Exploratória"]
)

# Carregar dados (ajuste o caminho para o seu CSV)
df = pd.read_csv("Customer_support_data.csv")

# ---------------------------
# Subpágina 1: Contextualização
# ---------------------------
if subpagina == "Contextualização e Objetivo":
    st.header("📌 Contextualização e Objetivo")
    st.write("""
    O objetivo dessa análise é entender os fatores que impactam a satisfação do cliente (**CSAT**).
        
    As perguntas principais são:
    1. Como a satisfação varia por categoria de atendimento?
    2. Existe diferença entre os canais de atendimento?
    3. O tempo de resposta influencia a satisfação?
    4. Há impacto do turno do operador?
    5. O tempo de experiência (tenure) influencia a satisfação?
    """)

# ---------------------------
# Subpágina 2: Entendendo o Dataset
# ---------------------------
elif subpagina == "Entendendo o Dataset":
    st.header("📊 Interpretando os Dados do Dataset")

    st.write("### Dataset:")
    st.markdown(
        "[Link para o dataset no Kaggle](https://www.kaggle.com/datasets/ddosad/ecommerce-customer-service-satisfaction?resource=download)"
    )

    st.write("Visualização inicial do dataset:")
    st.dataframe(df.head())

    st.write("### 📑 Colunas e tipos de dados")

    # Criando a tabela com Pandas
    data_dict = {
        "Nome da coluna": [
            "Unique_id", "channel_name", "category", "Sub-category",
            "Customer_Remarks", "Order_id", "order_date_time", "Issue_reported_at",
            "issue_responded", "Survey_response_Date", "Customer_City",
            "Product_category", "Item_price", "connected_handling_time",
            "Agent_name", "Supervisor", "Manager", "Tenure_Bucket",
            "Agent_Shift", "CSAT_Score"
        ],
        "Descrição": [
            "Identificador único para cada registro",
            "Nome do canal de atendimento ao cliente",
            "Categoria da interação",
            "Subcategoria da interação",
            "Feedback fornecido pelo cliente",
            "Identificador do pedido associado à interação",
            "Data e hora do pedido",
            "Carimbo de data e hora em que o problema foi relatado",
            "Carimbo de data e hora em que o problema foi respondido",
            "Data da resposta da pesquisa do cliente",
            "Cidade do cliente",
            "Categoria do produto",
            "Preço do item",
            "Tempo gasto para lidar com a interação (COLUNA SEM DADOS)",
            "Nome do agente de atendimento ao cliente",
            "Nome do supervisor",
            "Nome do gerente",
            "Agente de categorização de buckets (tempo de casa, em dias)",
            "Tempo de turno do agente",
            "Pontuação de satisfação do cliente (CSAT)"
        ],
        "Tipo de dado": [
            "Qualitativo Nominal", "Qualitativo Nominal", "Qualitativo Nominal",
            "Qualitativo Nominal", "Qualitativo Nominal", "Qualitativo Nominal",
            "Quantitativo Contínuo", "Quantitativo Contínuo", "Quantitativo Contínuo",
            "Quantitativo Discreto", "Qualitativo Nominal", "Qualitativo Nominal",
            "Quantitativo Contínuo", "Quantitativo Contínuo", "Qualitativo Nominal",
            "Qualitativo Nominal", "Qualitativo Nominal", "Qualitativo Ordinal",
            "Qualitativo Nominal", "Quantitativo Discreto"
        ]
    }

    df_tipos_de_dados = pd.DataFrame(data_dict)

    # Exibir como tabela interativa
    st.dataframe(df_tipos_de_dados, use_container_width=True)


# ---------------------------
# Subpágina 3: Dashboard Exploratória
# ---------------------------
elif subpagina == "Dashboard Exploratória":
    st.title("Análise de CSAT por Categoria de Atendimento")

    fig = px.bar(
    df.groupby("category")["CSAT Score"].mean().reset_index(),
    x="category",
    y="CSAT Score",
    color="category",
    labels={"category": "Categoria de Atendimento", "CSAT Score": "Média de CSAT"},
    title="Média de CSAT por Categoria"
    )
    fig.update_yaxes(dtick=1, tick0=1, range=[0.5, 5.5])

    st.plotly_chart(fig, use_container_width=True)

    # Resumo estatístico por categoria
    st.subheader("Resumo Estatístico das Notas de CSAT por Categoria")

    resumo = df.groupby("category")["CSAT Score"].describe().reset_index()
    st.dataframe(resumo, use_container_width=True)
