from click import option
import streamlit as st

# Externos
from simulation import simulationROIComponent

st.set_page_config(page_title='Selic App',
                   page_icon='💸', 
                   layout="centered", 
                   initial_sidebar_state="expanded", 
                   menu_items=None)

st.title('Selic App 💸')

simulation = simulationROIComponent()

st.markdown('___')
st.empty()
st.caption(f'❌ Não é recomendação de investimento')
st.caption(f'👨🏻‍💻 Repositório: [Selic App Análise Repo](https://github.com/felp99/selic_app_analise)')