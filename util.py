import streamlit as st
import requests
import pandas as pd

class Utils():

    def __init__(self) -> None:
        
        self.APP_TITLE = 'Renda Fixa App'
        self.APP_EMOJI = '💲'
        self.NAME = 'Selecione uma página'
        self.INVESTIMENTO_LABEL = '💰 Investimento:'
        self.INVESTIMENTO_INICIAL_VALOR = 1000.00
        self.ALL_SELIC_DATA = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=02/03/2022'
        self.LAST_10_SELIC_DATA = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados/ultimos/10?formato=json'

        pass

    def run(self):
        st.warning('Selecione uma página para ser visualizada.')

    def varString(self, actual, last):
        return f'{round((last - actual)/last * 100, 2)}%'

    def perc(self, value):
        return f'{round(value * 100, 4)}%'

    def kpi(self, values, strings, stringFormat):
        _cols = st.columns(len(values))
        for i, value in enumerate(values):
            with _cols[i]:
                st.metric(label = strings[i],
                        value = stringFormat(value),
                        delta_color="normal")

    def currFormat(self, value):
        return f'R${round(value, 2)}'

    def getSelic(self, url):
        @st.cache
        def fetchData(url):
            try:
                response = requests.get(url)
            except(ConnectionError):
                st.error('🤖 Sem conexão com a API SELIC')
            return pd.DataFrame(response.json())

        return fetchData(url)
