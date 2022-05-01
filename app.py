from click import option
import streamlit as st
import requests
import json
import pandas as pd

# Arquivos auxiliares
import util

st.set_page_config(page_title='Selic App',
                   page_icon='💸', 
                   layout="centered", 
                   initial_sidebar_state="expanded", 
                   menu_items=None)


plataforma_options = ['💚 Picpay', '💜 Nubank']

# Bônus PICPAY até 100 mil reais
PICPAY = 105
IR_PICPAY = 22.5

with st.sidebar:

    st.title( '🔽 Comece por aqui')

    st.subheader('🎲 Dados:')

    SELIC_TAXAS = st.checkbox('Mostrar dados sobre a SELIC hoje.')

    st.markdown('___')

    st.subheader('📠 Simulação:')
    PLATAFORMA = st.radio('Selecione a plataforma de investimento:',
                           options= plataforma_options)
    INVESTIMENTO = st.number_input(label='💰 Investimento:', value=1000.00, step = 100.00)

st.title('Selic App 💸')


if PLATAFORMA == plataforma_options[1]:
    with st.sidebar:
        IR_NUBANK = st.select_slider(label = 'Imposto de renda %:', 
                                    options = [22.5, 20, 17.5, 15])

# with st.sidebar:
#     generateRel = st.button('Gerar simulação de investimento')

# if not generateRel:
#     st.stop()

st.markdown(f'### Plataforma: {PLATAFORMA}')

if PLATAFORMA == plataforma_options[0]:
    picpay_infos = [f'✅ Bônus PICPAY: **{PICPAY}%** (até R$100k)', 
                    f'👹 Imposto de renda: **{IR_PICPAY}%** (média para o PICPAY)', 
                    f'❔ Mais informações: [Quanto rende meu dinheiro no PicPay?](https://meajuda.picpay.com/hc/pt-br/articles/360044022532-Quanto-rende-meu-dinheiro-no-PicPay-)']
                    
    for info in picpay_infos:
        st.markdown(info)

elif PLATAFORMA == plataforma_options[1]:

    nubank_infos = [f'🟣 Rendimento de 100% do CDI', 
                    f'👾 Imposto de renda: **{IR_NUBANK}%** (depende do tempo)', 
                    f'🟪 Assumindo não incidência de IOF.', 
                    f'❔ Mais informações: [Como é cobrado o IOF e IR da conta do Nubank?](https://blog.nubank.com.br/ir-iof-conta-nubank/)']

    for info in nubank_infos:
        st.markdown(info)

st.markdown('___')

# API de dados da Selic cedido pelo bcb

@st.cache
def fetchData(url):
    try:
        response = requests.get(url)
    except(ConnectionError):
        st.error('🤖 Sem conexão com a API SELIC')
    return pd.DataFrame(response.json())

df = fetchData('http://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=02/03/2022')

# Taxa mais recente
taxa_hoje = float(df['valor'].iloc[-1])

# Penúltima taxa mais recente
taxa_ontem = float(df['valor'].iloc[-1])

taxa_diaria = ((taxa_hoje/100 + 1) ** 1) -1 
taxa_mensal = ((taxa_hoje/100 + 1) ** 22) -1 
taxa_anual =  ((taxa_hoje/100 + 1) ** 254) -1

if SELIC_TAXAS:
    with st.expander('📊 Taxas atuais SELIC', expanded=True):

        valuesTaxas = [taxa_diaria, taxa_mensal, taxa_anual]
        stringsTaxas = ['Diária',
                        'Mensal',
                        'Anual']

        util.kpi(valuesTaxas, stringsTaxas, util.perc)


if PLATAFORMA == plataforma_options[0]:

    title = '💹 Taxas Picpay | Considerando Bônus & Imposto de Renda'
    diaria = taxa_diaria * PICPAY/100 * (1-(IR_PICPAY/100))
    mensal = taxa_mensal * PICPAY/100 * (1-(IR_PICPAY/100))
    anual = taxa_anual * PICPAY/100 * (1-(IR_PICPAY/100))

    if INVESTIMENTO > 10**5:

        title = '💹 Taxas Picpay | Considerando Bônus nos 100k & Imposto de Renda'

        EXC_INVESTIMENTO = INVESTIMENTO - 10**5

        diaria_bonus = taxa_diaria * PICPAY/100 * (1-(IR_PICPAY/100))
        mensal_bonus = taxa_mensal * PICPAY/100 * (1-(IR_PICPAY/100))
        anual_bonus = taxa_anual * PICPAY/100 * (1-(IR_PICPAY/100))

        diaria_padrao = taxa_diaria * (1-(IR_PICPAY/100))
        mensal_padrao = taxa_mensal * (1-(IR_PICPAY/100))
        anual_padrao = taxa_anual * (1-(IR_PICPAY/100))

        #Média ponderada para calcular a nova taxa de acordo com o investimento
        diaria = ((diaria_bonus * 10**5) + (diaria_padrao * EXC_INVESTIMENTO))/ (10**5 + EXC_INVESTIMENTO)
        mensal = ((mensal_bonus * 10**5) + (mensal_padrao * EXC_INVESTIMENTO))/ (10**5 + EXC_INVESTIMENTO)
        anual = ((anual_bonus * 10**5) + (anual_padrao * EXC_INVESTIMENTO))/ (10**5 + EXC_INVESTIMENTO)


elif PLATAFORMA == plataforma_options[1]:
    title = '🟪 Taxas Nubank | Considerando Imposto de Renda'
    diaria = taxa_diaria * (1-(IR_NUBANK/100))
    mensal = taxa_mensal * (1-(IR_NUBANK/100))
    anual = taxa_anual * (1-(IR_NUBANK/100))

with st.expander(title, expanded=True):

    valuesRent = [diaria, mensal, anual]
    stringsRent = ['Diária',
                   'Mensal',
                   'Anual']

    util.kpi(valuesRent, stringsRent, util.perc)

with st.expander('📈 ROI', expanded=True):

    valuesROI = [INVESTIMENTO * taxa for taxa in valuesRent]
    stringsROI = ['Diária',
                  'Mensal',
                  'Anual']

    util.kpi(valuesROI, stringsROI, util.currFormat)

st.markdown('___')
st.empty()
st.caption(f'❌ Não é recomendação de investimento')
st.caption(f'👨🏻‍💻 Repositório: [Selic App Análise Repo](https://github.com/felp99/selic_app_analise)')