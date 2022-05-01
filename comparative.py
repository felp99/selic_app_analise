from textwrap import indent
import streamlit as st
import pandas as pd
import requests

from util import Utils

utils = Utils()

class ComparativeComponent():

    def __init__(self) -> None:
        
        self.NAME = '⚔️ Nubank ou Picpay?'
        self.PARAMETROS = {}

    def run(self):

        with st.sidebar:

            self.INVESTIMENTO = st.number_input(label = utils.INVESTIMENTO_LABEL, 
                                                value = utils.INVESTIMENTO_INICIAL_VALOR)

            self.TEMPO_INVESTIMENTO = st.number_input(label = '⏳ Tempo investido (dias)', 
                                                      value = 365)
