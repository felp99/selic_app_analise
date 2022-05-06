from email import utils
from email.policy import default
from click import option
import streamlit as st

# Externos
from simulationROI import simulationROIComponent
from comparative import ComparativeComponent
from util import Utils

utils = Utils()
simulationROI = simulationROIComponent()
comparative = ComparativeComponent()

COMPONENTES = [utils, simulationROI, comparative]

# st.set_page_config(page_title=utils.APP_TITLE,
#                    page_icon=utils.APP_EMOJI, 
#                    layout="centered", 
#                    initial_sidebar_state="expanded", 
#                    menu_items=None)

st.title(utils.APP_EMOJI + '' + utils.APP_TITLE)

with st.sidebar:
    selected_component = st.selectbox(label = 'Selecione a página:', 
                                    options= [c.NAME for c in COMPONENTES], 
                                    index = 2)

# Itera sobre os componentes e roda aquele escolhido
for c in COMPONENTES:
    try:
        if c.NAME == selected_component:
            c.run()
    except Exception as e:
        st.error(e)

st.markdown('___')
st.empty()

c,c2,c3 = st.columns(3)

with c:
    st.caption(f'❌ Não é recomendação de investimento')
with c2:
    st.caption(f'👨🏻‍💻 Repositório: [Selic App Análise Repo](https://github.com/felp99/selic_app_analise)')
with c3:
    st.caption('✨ Próxima feature: **Aportes recorrentes**')