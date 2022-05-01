from email import utils
from click import option
import streamlit as st

# Externos
from simulationROI import simulationROIComponent
from util import Utils

utilsVariables = Utils()
simulationROI = simulationROIComponent()

COMPONENTES = [utilsVariables, simulationROI]

st.set_page_config(page_title='Selic App',
                   page_icon='💸', 
                   layout="centered", 
                   initial_sidebar_state="expanded", 
                   menu_items=None)

st.title('Selic App 💸')

with st.sidebar:
    selected_component = st.selectbox(label = 'Selecione a página:', 
                                    options= [c.NAME for c in COMPONENTES])

# Itera sobre os componentes e roda aquele escolhido
for c in COMPONENTES:
    try:
        if c.NAME == selected_component:
            c.run()
    except Exception as e:
        st.error(e)

st.markdown('___')
st.empty()
st.caption(f'❌ Não é recomendação de investimento')
st.caption(f'👨🏻‍💻 Repositório: [Selic App Análise Repo](https://github.com/felp99/selic_app_analise)')