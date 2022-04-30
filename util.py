import streamlit as st

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