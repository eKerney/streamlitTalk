import streamlit as st
import streamlit_book as stb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('Streamlit Charts')
st.write('https://docs.streamlit.io/library/api-reference/charts')

st.markdown('## st.line_chart')
st.code('st.line_chart(data=None, width=0, height=0, use_container_width=True)', language='python')
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
chartData = "chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])"
lineChart = "st.line_chart(chart_data)"
st.code(chartData, language='python')
st.code(lineChart, language='python')
st.line_chart(chart_data)
st.write('---')

st.markdown('## st.area_chart')
st.code('st.area_chart(data=None, width=0, height=0, use_container_width=True)', language='python')
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
chartData = "chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])"
chart = "st.area_chart(chart_data)"
st.code(chartData, language='python')
st.code(chart, language='python')
st.area_chart(chart_data)
st.write('---')

st.markdown('## st.py_plot')
st.code('st.pyplot(fig=None, clear_figure=None, **kwargs)', language='python')
chartData = '''
chart_data = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
'''
chart = "st.pyplot(fig)"
chart_data = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(chart_data, bins=20)
st.code(chartData, language='python')
st.code(chart, language='python')
st.pyplot(fig)
st.write('---')