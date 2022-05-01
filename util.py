import streamlit as st

class Utils():

    def __init__(self) -> None:
        
        self.NAME = 'Selecione uma página'
        pass

    def run(self):
        st.warning('Selecione uma página para ser visualizada')

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