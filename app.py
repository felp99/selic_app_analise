import streamlit as st
import requests
import json
import pandas as pd

with st.sidebar:

    st.subheader('📠 Simulação:')

    INVESTIMENTO = st.number_input(label='💰 Investimento:', value=1000, step = 100, format='%i')


# Bônus PICPAY até 100 mil reais
PICPAY = 105
IR = 22.32

st.title('Selic App 💸')

markdown_info = []
infos = [f'✅ Bônus PICPAY: **{PICPAY}%** (até R$100k)', 
         f'👹 Imposto de renda: **{IR}%** (média para o PICPAY)', 
         f'💰 Investimento: **R${INVESTIMENTO}**', 
         '___']

for info in infos:
    st.markdown(info)
    
# API de dados da Selic cedido pelo bcb

try:
    response = requests.get('http://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=02/03/2022')
except(ConnectionError):
    st.error('🤖 Sem conexão com a API SELIC')

df = pd.DataFrame(response.json())

# Taxa mais recente
taxa_hoje = float(df['valor'].iloc[-1])

# Penúltima taxa mais recente
taxa_ontem = float(df['valor'].iloc[-1])

def varString(actual, last):
    return f'{round((last - actual)/last * 100, 2)}%'

def perc(value):
    return f'{round(value * 100, 4)}%'

def kpi(values, strings, stringFormat):
    _cols = st.columns(len(values))
    for i, value in enumerate(values):
        with _cols[i]:
            st.metric(label = strings[i],
                    value = stringFormat(value),
                    delta_color="normal")

def currFormat(value):
    return f'R${round(value, 2)}'

taxa_diaria = ((taxa_hoje/100 + 1) ** 1) -1 
taxa_mensal = ((taxa_hoje/100 + 1) ** 22) -1 
taxa_anual =  ((taxa_hoje/100 + 1) ** 254) -1
    

with st.expander('📊 Taxas atuais SELIC'):

    valuesTaxas = [taxa_diaria, taxa_mensal, taxa_anual]
    stringsTaxas = ['Diária',
                    'Mensal',
                    'Anual']

    kpi(valuesTaxas, stringsTaxas, perc)

diaria = taxa_diaria * PICPAY/100 * (1-(IR/100))
mensal = taxa_mensal * PICPAY/100 * (1-(IR/100))
anual = taxa_anual * PICPAY/100 * (1-(IR/100))

with st.expander('💹 Taxas atuais PICPAY'):

    valuesRent = [diaria, mensal, anual]
    stringsRent = ['Diária',
                   'Mensal',
                   'Anual']

    kpi(valuesRent, stringsRent, perc)

with st.expander('📈 ROI'):

    valuesROI = [INVESTIMENTO * taxa for taxa in valuesRent]
    stringsROI = ['Diária',
                  'Mensal',
                  'Anual']

    kpi(valuesROI, stringsROI, currFormat)



