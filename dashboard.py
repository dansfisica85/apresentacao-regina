import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuração da Página
st.set_page_config(
    page_title="Dashboard Provão Paulista 2026",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- DADOS (Consolidado Oficial: 2191 Alunos / 182 Aprovados) ---
data = [
    {"rank": 1, "escola": "DOLORES BELEM NOVAES", "municipio": "Pontal", "alunos": 26, "c1": 8, "c2": 2, "total_aprov": 10},
    {"rank": 2, "escola": "DOLORES MARTINS DE CASTRO", "municipio": "Pontal", "alunos": 9, "c1": 2, "c2": 1, "total_aprov": 3},
    {"rank": 3, "escola": "YOLANDA LUIZ SICHIERI", "municipio": "Pontal", "alunos": 148, "c1": 25, "c2": 11, "total_aprov": 36},
    {"rank": 4, "escola": "ANTONIO FURLAN JUNIOR", "municipio": "Sertãozinho", "alunos": 34, "c1": 6, "c2": 2, "total_aprov": 8},
    {"rank": 5, "escola": "BASILIO RODRIGUES DA SILVA", "municipio": "Pontal", "alunos": 97, "c1": 15, "c2": 5, "total_aprov": 20},
    {"rank": 6, "escola": "NESTOR GOMES DE ARAUJO", "municipio": "Dumont", "alunos": 73, "c1": 8, "c2": 4, "total_aprov": 12},
    {"rank": 7, "escola": "MARIA CONCEICAO R. S. MAGON", "municipio": "Sertãozinho", "alunos": 38, "c1": 4, "c2": 2, "total_aprov": 6},
    {"rank": 8, "escola": "WINSTON CHURCHILL", "municipio": "Sertãozinho", "alunos": 107, "c1": 12, "c2": 7, "total_aprov": 19},
    {"rank": 9, "escola": "MARIA FALCONI DE FELICIO", "municipio": "Pitangueiras", "alunos": 27, "c1": 2, "c2": 1, "total_aprov": 3},
    {"rank": 10, "escola": "DOMINGOS PARO", "municipio": "Pitangueiras", "alunos": 33, "c1": 2, "c2": 1, "total_aprov": 3},
    {"rank": 11, "escola": "MARIA ELYDE M. DOS SANTOS", "municipio": "Terra Roxa", "alunos": 63, "c1": 2, "c2": 3, "total_aprov": 5},
    {"rank": 12, "escola": "MAURICIO MONTECCHI", "municipio": "Pitangueiras", "alunos": 123, "c1": 3, "c2": 3, "total_aprov": 6},
    {"rank": 13, "escola": "ORMINDA GUIMARAES COTRIM", "municipio": "Pitangueiras", "alunos": 126, "c1": 3, "c2": 3, "total_aprov": 6},
    {"rank": 14, "escola": "JOSE LUIZ DE SIQUEIRA", "municipio": "Barrinha", "alunos": 175, "c1": 5, "c2": 3, "total_aprov": 8},
    {"rank": 15, "escola": "BRUNO PIERONI", "municipio": "Sertãozinho", "alunos": 188, "c1": 6, "c2": 2, "total_aprov": 8},
    {"rank": 16, "escola": "LUIZ MARCARI", "municipio": "Barrinha", "alunos": 134, "c1": 4, "c2": 1, "total_aprov": 5},
    {"rank": 17, "escola": "NICIA FABIOLA ZANUTO GIRALDI", "municipio": "Sertãozinho", "alunos": 57, "c1": 1, "c2": 1, "total_aprov": 2},
    {"rank": 18, "escola": "FERRUCIO CHIARATTI", "municipio": "Sertãozinho", "alunos": 123, "c1": 2, "c2": 2, "total_aprov": 4},
    {"rank": 19, "escola": "EDITH SILVEIRA DALMASO", "municipio": "Sertãozinho", "alunos": 156, "c1": 2, "c2": 3, "total_aprov": 5},
    {"rank": 20, "escola": "ISAIAS JOSE FERREIRA", "municipio": "Sertãozinho", "alunos": 65, "c1": 1, "c2": 1, "total_aprov": 2},
    {"rank": 21, "escola": "ANNA PASSAMONTI BALARDIN", "municipio": "Sertãozinho", "alunos": 201, "c1": 3, "c2": 3, "total_aprov": 6},
    {"rank": 22, "escola": "MARIO LINS", "municipio": "Jardinópolis", "alunos": 35, "c1": 1, "c2": 0, "total_aprov": 1},
    {"rank": 23, "escola": "PLINIO BERARDO", "municipio": "Jardinópolis", "alunos": 227, "c1": 3, "c2": 1, "total_aprov": 4},
    {"rank": 24, "escola": "ODULFO DE OLIVEIRA GUIMARAES", "municipio": "Viradouro", "alunos": 91, "c1": 1, "c2": 0, "total_aprov": 1},
    {"rank": 25, "escola": "ADELIA FRASCINO", "municipio": "Pontal", "alunos": 2, "c1": 0, "c2": 0, "total_aprov": 0}
]

# Criar DataFrame
df = pd.DataFrame(data)
df['taxa'] = (df['total_aprov'] / df['alunos']) * 100

# Recalcular Rank baseado na nova taxa (Do maior para o menor)
df['rank'] = df['taxa'].rank(ascending=False, method='min').astype(int)
df = df.sort_values('rank')

# Funções Auxiliares
def get_badge_color(taxa):
    if taxa >= 20: return "green"
    if taxa >= 10: return "blue"
    if taxa >= 5: return "orange"
    return "red"

def get_badge_label(taxa):
    if taxa >= 20: return "Excelente"
    if taxa >= 10: return "Bom"
    if taxa >= 5: return "Regular"
    return "Crítico"

# --- INTERFACE ---

# Sidebar
with st.sidebar:
    st.image("1.png", use_container_width=True)
    st.title("Filtros do Painel")
    
    selected_municipio = st.multiselect(
        "Filtrar por Município",
        options=sorted(df['municipio'].unique()),
        default=sorted(df['municipio'].unique())
    )
    
    st.divider()
    st.info("💡 Selecione uma escola no gráfico ou na lista de busca no topo para ver a ficha completa.")

# Filtragem
df_filtered = df[df['municipio'].isin(selected_municipio)]

# Header
st.title("📊 Painel Interativo - Provão Paulista 2026")
st.markdown("Base de Dados de Desempenho Escolar - Diretoria de Sertãozinho")

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de Alunos", f"{df_filtered['alunos'].sum():,}".replace(",", "."))
col2.metric("Total Aprovados", f"{df_filtered['total_aprov'].sum()}")
taxa_media = (df_filtered['total_aprov'].sum() / df_filtered['alunos'].sum()) * 100 if df_filtered['alunos'].sum() > 0 else 0
col3.metric("Taxa Média", f"{taxa_media:.2f}%")
col4.metric("Escolas Analisadas", len(df_filtered))

st.divider()

# --- ÁREA DE INTERAÇÃO (BANCO DE DADOS) ---

st.subheader("🔍 Consultar Escola (Visão Gráfica)")

# Seletor Principal (Atua como "Clicar no nome")
selected_school_name = st.selectbox(
    "Selecione ou Digite o Nome da Escola para Abrir a Ficha:",
    options=["Selecione..."] + list(df_filtered['escola'].unique()),
    index=0
)

# Layout: Gráfico à Esquerda, Ficha à Direita (se selecionado via gráfico seria scatter, aqui usamos o selectbox como trigger principal)

col_chart, col_detail = st.columns([1.5, 1])

with col_chart:
    st.markdown("### Mapa de Eficiência")
    # Gráfico Scatter Interativo
    fig = px.scatter(
        df_filtered, 
        x='alunos', 
        y='taxa', 
        size='total_aprov',
        color='taxa',
        hover_name='escola',
        hover_data=['rank', 'municipio', 'c1', 'c2'],
        color_continuous_scale='RdYlGn',
        labels={'alunos': 'Total de Alunos', 'taxa': 'Taxa de Aprovação (%)'},
        title='Tamanho da Escola vs. Taxa de Aprovação (Bolha = Volume Aprovados)'
    )
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("### Ranking Visual")
    fig_bar = px.bar(
        df_filtered.sort_values('taxa', ascending=True),
        x='taxa',
        y='escola',
        orientation='h',
        color='taxa',
        color_continuous_scale='RdYlGn',
        title='Ranking por Taxa de Aprovação'
    )
    fig_bar.update_layout(height=600)
    st.plotly_chart(fig_bar, use_container_width=True)

with col_detail:
    if selected_school_name != "Selecione...":
        school_data = df[df['escola'] == selected_school_name].iloc[0]
        
        # FICHA DA ESCOLA
        st.markdown(f"""
        <div style="background-color: #f8fafc; padding: 20px; border-radius: 10px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h2 style="color: #1e293b; margin-top: 0;">🏫 {school_data['escola']}</h2>
            <p style="color: #64748b; font-weight: bold;">{school_data['municipio']} • Rank #{school_data['rank']}</p>
            <hr>
            
            <div style="display: flex; justify-content: space-between; margin-bottom: 20px;">
                <div style="text-align: center;">
                    <h3 style="margin:0; color: #3b82f6;">{school_data['alunos']}</h3>
                    <small>Matriculados</small>
                </div>
                <div style="text-align: center;">
                    <h3 style="margin:0; color: #10b981;">{school_data['total_aprov']}</h3>
                    <small>Aprovados</small>
                </div>
                <div style="text-align: center;">
                    <h3 style="margin:0; color: #6366f1;">{school_data['taxa']:.2f}%</h3>
                    <small>Taxa</small>
                </div>
            </div>
            
            <h4 style="margin-bottom: 10px;">Detalhamento das Chamadas</h4>
            <div style="background-color: white; padding: 10px; border-radius: 5px; border: 1px solid #f1f5f9;">
                <b>1ª Chamada:</b> {school_data['c1']} aprovados<br>
                <b>2ª Chamada:</b> {school_data['c2']} aprovados
            </div>
            
            <br>
            <h4 style="margin-bottom: 5px;">Status de Desempenho</h4>
            <span style="background-color: {get_badge_color(school_data['taxa'])}; color: white; padding: 5px 10px; border-radius: 15px; font-weight: bold; font-size: 0.9em;">
                {get_badge_label(school_data['taxa'])}
            </span>
            <br><br>
            <p style="font-size: 0.9em; color: #94a3b8;">
                *Comparativo*: Esta escola está {('acima' if school_data['taxa'] > 8.31 else 'abaixo')} da média regional de 8.31%.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Gráfico Específico da Escola (Pizza 1ª vs 2ª Chamada)
        if school_data['total_aprov'] > 0:
            st.markdown("#### Composição dos Aprovados")
            fig_pie = px.pie(
                names=['1ª Chamada', '2ª Chamada'],
                values=[school_data['c1'], school_data['c2']],
                color_discrete_sequence=['#f59e0b', '#10b981'],
                hole=0.4
            )
            fig_pie.update_layout(height=250, margin=dict(t=0, b=0, l=0, r=0))
            st.plotly_chart(fig_pie, use_container_width=True)
            
    else:
        st.info("👈 Selecione uma escola na tabela ou no menu acima para visualizar a ficha detalhada ('Janela Gráfica').")
        st.image("https://illustrations.popsy.co/gray/question-mark.svg", width=200)

# Tabela Completa (Fim da Página)
st.divider()
st.subheader("Base de Dados Completa")
st.dataframe(
    df_filtered[['rank', 'escola', 'municipio', 'alunos', 'total_aprov', 'taxa']].style.format({'taxa': '{:.2f}%'}),
    use_container_width=True,
    hide_index=True
)
