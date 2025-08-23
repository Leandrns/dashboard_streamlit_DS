import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Configuração da página para usar o layout 'wide'
st.set_page_config(
    page_title="Análise de Dados CSAT",
    layout="wide"
)

# --- FUNÇÃO DE PRÉ-PROCESSAMENTO ---
# Usamos @st.cache_data para que o Streamlit execute esta função apenas uma vez
@st.cache_data
def load_and_preprocess_data(file_path):
    """
    Carrega os dados, limpa os nomes das colunas e calcula o tempo de resposta.
    """
    df = pd.read_csv(file_path)
    
    # Padroniza os nomes das colunas (minúsculas, sem espaços)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-', '_')
    
    # Converte colunas de data/hora para o formato datetime, tratando erros
    df['issue_reported_at'] = pd.to_datetime(df['issue_reported_at'], errors='coerce')
    df['issue_responded'] = pd.to_datetime(df['issue_responded'], errors='coerce')
    
    # Calcula o tempo de resposta em minutos
    df['response_time_minutes'] = (df['issue_responded'] - df['issue_reported_at']).dt.total_seconds() / 60
    
    # Garante que a coluna csat_score não tenha valores nulos para a análise
    df.dropna(subset=['csat_score'], inplace=True)
    
    return df

# Carrega os dados usando a função de cache
df = load_and_preprocess_data("Customer_support_data.csv")

# --- BARRA LATERAL (SIDEBAR) ---
st.sidebar.header("Navegação")
subpagina = st.sidebar.selectbox(
    "Selecione uma seção",
    ["Contextualização e Objetivo", "Entendendo o Dataset", "Análise Exploratória"]
)

# ---------------------------
# Subpágina 1: Contextualização
# ---------------------------
if subpagina == "Contextualização e Objetivo":
    st.header("📌 Contextualização e Objetivo")
    st.write("""
    O objetivo desta análise é entender os fatores que impactam a satisfação do cliente (**CSAT Score**), 
    uma métrica crucial para o sucesso de qualquer negócio de e-commerce. 
             
    O dataset utilizado é de um e-commerce localizado na Índia.
    
    Através de uma análise exploratória de dados, buscamos responder às seguintes perguntas de negócio:
    - **Satisfação Geral:** Qual é o panorama geral da satisfação dos nossos clientes?
    - **Impacto da Categoria:** Quais categorias de atendimento geram mais ou menos satisfação?
    - **Eficiência do Canal:** O canal de comunicação (Inbound, Outcall) influencia a percepção do cliente?
    - **Agilidade no Atendimento:** Existe uma correlação entre o tempo de resposta e a nota de CSAT?
    - **Desempenho por Turno:** O turno de trabalho dos agentes afeta a qualidade do atendimento?
    - **Influência da Experiência do Agente:** Agentes mais experientes (maior tempo de casa) alcançam melhores resultados de satisfação?
    - **Satisfação por Cidade:** De quais cidades vêm os maiores e menores indíces de satisfação?
    Este dashboard interativo permite explorar visualmente os dados para extrair insights valiosos e direcionar melhorias no processo de atendimento ao cliente.
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
            "unique_id", "channel_name", "category", "sub-category",
            "customer_remarks", "order_id", "order_date_time", "issue_reported_at",
            "issue_responded", "survey_response_date", "customer_city",
            "product_category", "item_price", "connected_handling_time",
            "agent_name", "supervisor", "manager", "tenure_bucket",
            "agent_shift", "csat_score"
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
elif subpagina == "Análise Exploratória":
    st.header("Dashboard de Análise Exploratória do CSAT")

    # --- Menu de Análises na Sidebar ---
    analysis_option = st.sidebar.radio(
        "Selecione a Análise",
        ["Visão Geral", "Análise por Categoria", "Análise por Canal", "Análise por Tempo de Resposta", "Análise por Turno", "Análise por Experiência do Agente", "Análise Geográfica"]
    )

    # --- Análise 1: Visão Geral ---
    if analysis_option == "Visão Geral":
        st.subheader("Distribuição Geral das Notas de Satisfação (CSAT Score)")
        
        col1, col2 = st.columns([2, 1])

        with col1:
            fig_hist = px.histogram(
                df, 
                x='csat_score', 
                title='Histograma das Notas de CSAT',
                labels={'csat_score': 'Nota de Satisfação'},
                nbins=5,
                text_auto=True
            )
            fig_hist.update_layout(bargap=0.1)
            st.plotly_chart(fig_hist, use_container_width=True)

        with col2:
            st.metric(
                label="Média Geral de CSAT",
                value=f"{df['csat_score'].mean():.2f}"
            )
            st.metric(
                label="Mediana de CSAT",
                value=int(df['csat_score'].median())
            )
            st.metric(
                label="Total de Respostas",
                value=f"{len(df):,}"
            )
            st.write("A alta concentração de notas 5 indica uma tendência geral de satisfação, mas a presença de notas 1 e 2 não pode ser ignorada.")


    # --- Análise 2: Categoria ---
    elif analysis_option == "Análise por Categoria":
        st.subheader("Análise de CSAT por Categoria de Atendimento")

        fig_box_cat = px.box(
            df,
            x='category',
            y='csat_score',
            color='category',
            title='Distribuição de CSAT por Categoria',
            labels={'category': 'Categoria', 'csat_score': 'Nota de CSAT'}
        )
        st.plotly_chart(fig_box_cat, use_container_width=True)
        st.write("O boxplot revela a dispersão das notas. Categorias com caixas mais longas e 'bigodes' extensos têm maior variabilidade nas avaliações.")
        
        col1, col2 = st.columns(2)

        with col1:
            fig_bar_cat = px.bar(
                df.groupby('category')['csat_score'].mean().sort_values(ascending=False).reset_index(),
                x='category',
                y='csat_score',
                color='category',
                title='Média de CSAT por Categoria',
                labels={'category': 'Categoria', 'csat_score': 'Média de CSAT'},
                text_auto='.2f'
            )
            st.plotly_chart(fig_bar_cat, use_container_width=True)

        with col2:
            st.dataframe(df.groupby('category')['csat_score'].describe(), use_container_width=True)

    # --- Análise 3: Canal ---
    elif analysis_option == "Análise por Canal":
        st.subheader("Análise de CSAT por Canal de Atendimento")

        fig_box_channel = px.box(
            df,
            x='channel_name',
            y='csat_score',
            color='channel_name',
            title='Distribuição de CSAT por Canal',
            labels={'channel_name': 'Canal', 'csat_score': 'Nota de CSAT'}
        )
        st.plotly_chart(fig_box_channel, use_container_width=True)
        st.write("Comparar os canais ajuda a entender se a plataforma de comunicação impacta a experiência do cliente.")
        st.dataframe(df.groupby('channel_name')['csat_score'].describe(), use_container_width=True)

    # --- Análise 4: Tempo de Resposta ---
    elif analysis_option == "Análise por Tempo de Resposta":
        # Remove valores de tempo de resposta negativos ou absurdamente altos (outliers)
        df_reduzido = df[(df['response_time_minutes'] >= 0) & (df['response_time_minutes'] < 10000)]

        st.subheader("Análise da Relação entre Tempo de Resposta e CSAT")

        # Gráfico de Barras por Faixa de Tempo
        bins = [0, 5, 15, 30, 60, 120, np.inf]
        labels = ['0-5 min', '6-15 min', '16-30 min', '31-60 min', '61-120 min', '>120 min']
        df_reduzido['response_time_bucket'] = pd.cut(df_reduzido['response_time_minutes'], bins=bins, labels=labels, right=False)
        avg_csat_by_time = df_reduzido.groupby('response_time_bucket')['csat_score'].mean().reset_index()
        fig_bar_time = px.bar(
            avg_csat_by_time,
            x='response_time_bucket',
            y='csat_score',
            title='Média de CSAT por Faixa de Tempo de Resposta',
            labels={'response_time_bucket': 'Tempo de Resposta', 'csat_score': 'Média de CSAT'},
            text_auto='.2f'
        )
        st.plotly_chart(fig_bar_time, use_container_width=True)
        st.write("O gráfico de barras mostra uma tendência clara: quanto maior o tempo de espera, menor a satisfação média do cliente. A agilidade é um fator chave.")
        
        st.markdown("---")
        st.subheader("Correlação e Dispersão Detalhada")

        col1, col2 = st.columns([2, 1])

        with col1:
            # Gráfico de Dispersão (usando uma amostra para performance)
            df_sample = df_reduzido.sample(n=3000, random_state=8)
            fig_scatter = px.scatter(
                df_sample,
                x='response_time_minutes',
                y='csat_score',
                title='Gráfico de Dispersão: Tempo de Resposta vs. CSAT (Amostra de 3000 pontos)',
                labels={'response_time_minutes': 'Tempo de Resposta (Minutos)', 'csat_score': 'Nota de CSAT'},
                trendline='ols', # Linha de tendência
                trendline_color_override='red'
            )
            st.plotly_chart(fig_scatter, use_container_width=True)

        with col2:
            # Cálculo da Correlação de Spearman
            spearman_corr = df_reduzido['response_time_minutes'].corr(df_reduzido['csat_score'], method='spearman')
            st.metric(
                label="Correlação de Spearman",
                value=f"{spearman_corr:.3f}"
            )
            st.write("""
            **Interpretação:**
            O valor de correlação de Spearman confirma a tendência observada. 
            O valor negativo indica que, à medida que o **tempo de resposta aumenta**, a **nota de satisfação tende a diminuir**.
            
            O gráfico de dispersão visualiza essa relação. Note que a maioria dos pontos se concentra em tempos de resposta baixos.
            *(O gráfico usa uma amostra de 3000 pontos para melhor performance visual.)*
            """)
    # --- Análise 5: Turno ---
    elif analysis_option == "Análise por Turno":
        st.subheader("Análise de CSAT por Turno do Agente")

        fig_box_shift = px.box(
            df,
            x='agent_shift',
            y='csat_score',
            color='agent_shift',
            title='Distribuição de CSAT por Turno',
            labels={'agent_shift': 'Turno', 'csat_score': 'Nota de CSAT'}
        )
        st.plotly_chart(fig_box_shift, use_container_width=True)
        st.write("Esta análise pode revelar se há inconsistências na qualidade do atendimento entre os diferentes turnos, o que pode estar ligado a fatores como cansaço ou volume de chamadas.")
        st.dataframe(df.groupby('agent_shift')['csat_score'].describe(), use_container_width=True)

    # --- Análise 6: Experiência do Agente ---
    elif analysis_option == "Análise por Experiência do Agente":
        st.subheader("Análise de CSAT por Tempo de Experiência do Agente")

        # Definir a ordem correta para a variável ordinal
        tenure_order = ['On Job Training', '0-30', '>90']
        df['tenure_bucket'] = pd.Categorical(df['tenure_bucket'], categories=tenure_order, ordered=True)

        fig_bar_tenure = px.bar(
            df.groupby('tenure_bucket')['csat_score'].mean().reset_index(),
            x='tenure_bucket',
            y='csat_score',
            color='tenure_bucket',
            title='Média de CSAT por Experiência do Agente',
            labels={'tenure_bucket': 'Tempo de Experiência (dias)', 'csat_score': 'Média de CSAT'},
            text_auto='.2f'
        )
        st.plotly_chart(fig_bar_tenure, use_container_width=True)
        st.write("Observa-se uma tendência de que agentes com mais tempo de casa ('Tenure') tendem a receber notas de satisfação mais altas, o que destaca a importância da retenção e do desenvolvimento de talentos.")
        st.dataframe(df.groupby('tenure_bucket')['csat_score'].describe(), use_container_width=True)

    # --- Análise 7: Geográfica ---
    elif analysis_option == "Análise Geográfica":
        st.subheader("Análise de CSAT por Cidade do Cliente")

        # Filtrar dados para remover cidades ausentes
        df_city = df.dropna(subset=['customer_city'])
        
        # Exibir aviso sobre a quantidade de dados
        total_count = len(df)
        city_count = len(df_city)
        percentage = (city_count / total_count) * 100
        st.warning(f"Atenção: Apenas {city_count:,} de {total_count:,} registros ({percentage:.2f}%) possuem dados de cidade. A análise a seguir é baseada apenas nesta amostra.")

        # Calcular contagem e média de CSAT por cidade
        city_stats = df_city.groupby('customer_city').agg(
            count=('csat_score', 'count'),
            mean_csat=('csat_score', 'mean')
        ).reset_index()

        # Filtrar por cidades com um número mínimo de respostas para relevância estatística
        min_responses = 10
        city_stats_filtered = city_stats[city_stats['count'] >= min_responses]

        # Pegar as 20 cidades com mais respostas
        top_20_cities = city_stats_filtered.nlargest(20, 'count')

        # Gráfico de barras para as top 20 cidades
        fig_city = px.bar(
            top_20_cities,
            x='customer_city',
            y='mean_csat',
            title=f'Média de CSAT para as 20 Cidades com Mais Respostas (mínimo de {min_responses} respostas)',
            labels={'customer_city': 'Cidade', 'mean_csat': 'Média de CSAT'},
            color='mean_csat',
            color_continuous_scale=px.colors.sequential.Plasma,
            text_auto='.2f'
        )
        fig_city.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_city, use_container_width=True)
        st.write("Este gráfico ajuda a identificar se há regiões geográficas específicas onde a satisfação do cliente é notavelmente maior ou menor.")

