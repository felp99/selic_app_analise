import streamlit as st
import pandas as pd
import datetime
import plotly.express as px

from util import Utils

utils = Utils()

class ComparativeComponent():

    def __init__(self) -> None:
        
        self.NAME = '⚔️ Nubank ou Picpay?'

    def run(self):

        with st.sidebar:

            self.INVESTIMENTO = st.number_input(label = utils.INVESTIMENTO_LABEL, 
                                                value = utils.INVESTIMENTO_INICIAL_VALOR)

            self.TEMPO_INVESTIMENTO = st.number_input(label = '⏳ Tempo investido (dias)', 
                                                      value = 365)

        if self.TEMPO_INVESTIMENTO < 10:
            self.IOF_NUBANK = 90
        elif 11 <= self.TEMPO_INVESTIMENTO <= 30:
            self.IOF_NUBANK = 66
        else:
            self.IOF_NUBANK = 0

        if self.TEMPO_INVESTIMENTO < 180:
            self.IR_NUBANK = 22.5
        elif 181 <= self.TEMPO_INVESTIMENTO <= 360:
            self.IR_NUBANK = 20
        elif 361 <= self.TEMPO_INVESTIMENTO <= 720:
            self.IR_NUBANK = 17.5
        else:
            self.IR_NUBANK = 15

        self.IR_PICPAY = 22.5
        self.IR_PICPAY_MULT = (1-(self.IR_PICPAY/100))
        self.PICPAY_BONUS = 1.05 #100K
        self.IR_NUBANK_MULT = (1-(self.IR_NUBANK/100))
        self.IOF_NUBANK_MULTI = (1-(self.IOF_NUBANK/100))

        self.TODAY = datetime.datetime.now()
        delta = datetime.timedelta(days=self.TEMPO_INVESTIMENTO)
        self.END = self.TODAY + delta

        index = pd.date_range(start=self.TODAY, end=self.END)

        df = pd.DataFrame(index= index)

        df_selic = utils.getSelic(utils.LAST_10_SELIC_DATA)

        df['SELIC'] = float(df_selic['valor'].iloc[-1])
        df['TAXA REAL NUBANK'] = df['SELIC'] * self.IOF_NUBANK_MULTI * self.IR_NUBANK_MULT
        df['TAXA REAL PICPAY 100'] = df['SELIC'] * self.IR_PICPAY_MULT
        
        
        if self.INVESTIMENTO < 100000:
            df['TAXA REAL PICPAY'] = df['SELIC'] * self.PICPAY_BONUS * self.IR_PICPAY_MULT
        else:
            _taxa_100 = df['SELIC'] * self.PICPAY_BONUS * self.IR_PICPAY_MULT * 100000
            _taxa_exc = df['SELIC'] * self.IR_PICPAY_MULT * (self.INVESTIMENTO - 100000)
            df['TAXA REAL PICPAY'] = (_taxa_100 + _taxa_exc)/self.INVESTIMENTO #Média ponderada da taxa

        df['TAXA NUBANK REAL ACUM'] = (df['TAXA REAL NUBANK']/100 + 1).cumprod() 
        df['TAXA PICPAY REAL ACUM'] = (df['TAXA REAL PICPAY']/100 + 1).cumprod()

        df['NUBANK'] = df['TAXA NUBANK REAL ACUM'] * self.INVESTIMENTO
        df['PICPAY'] = df['TAXA PICPAY REAL ACUM'] * self.INVESTIMENTO
        
        fig = px.line(df[['NUBANK', 'PICPAY']])

        fig['data'][0]['line']['color']='rgb(97,47,116)'
        fig['data'][1]['line']['color']='#22c25f'
        fig['layout']['legend']['title']['text'] = '🏰 Plataforma'
        fig['layout']['yaxis']['title']['text'] = 'Saldo'
        fig['layout']['xaxis']['title']['text'] = 'Período'

        fig.update_layout(paper_bgcolor='rgba(0, 0, 0, 0)', 
                          plot_bgcolor='rgba(0, 0, 0, 0)')

        st.plotly_chart(fig)