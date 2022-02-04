import streamlit as st
import streamlit_book as stb
import numpy as np
import pandas as pd

st.title('Streamlit Elements')
st.write('https://docs.streamlit.io/library/api-reference')
st.code("st.write('This is the Swiss Army knife of Streamlit commands')", language='python')
st.write('This is the Swiss Army knife of Streamlit commands')
st.write('It does different things depending on what you throw at it.')

st.code("st.write('The *basic use case* for **st.write** is **Markdown-formatted** *text*')", language='python')
st.write('The *basic use case* for **st.write** is **Markdown-formatted** *text*')
st.code("st.write('---')", language='python')
st.write('---')

st.write('**st.write()** also accepts other data formats, such as numbers, data frames, styled data frames...')
st.code("st.write(6, 12, 24, 48, 96, 192)", language='python')
st.write(6, 12, 24, 48, 96, 192)
dfCode = '''st.write(pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40],
     'third column': [100, 200, 300, 400]
 }))
'''
st.code(dfCode, language='python')
st.write(pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40],
     'third column': [100, 200, 300, 400]
 }))

st.write('---')
st.write('### A Few More Examples')

st.code("st.title('STREAMLIT PRESENTATION')", language='python')
st.title('STREAMLIT PRESENTATION')

st.code("st.header('st.header() Element')", language='python')
st.header('st.header() Element')

st.write('---')
funcCode = '''def automagicalFunction(cats, unicorns, rainbows):
    print(f'{cats} and {unicorns} and {rainbows} make your day brighter.')
'''
st.write("st.code() formats text in the selected language")
st.write(funcCode)
st.code("st.code(funcCode, language='python')", language='python')
st.code(funcCode, language='python')

st.write('Works for JavaScript also...')
st.code("st.code(jsCode, language='javascript')", language='python')
jsCode = '''const coords = [-85.343, 42.234];
let x = 360;
array.map(d => d.props);
'''
st.code(jsCode, language='javascript')

