import streamlit as st
import pandas as pd
import urllib.request
import requests
import threading
import json
import random


URL='https://api.thingspeak.com/channels/1649792/fields/1.json?api_key='
KEY='7WYDRRGMVSDWIA5D'
NEW_URL=URL+KEY
print(NEW_URL)

get_data=requests.get(NEW_URL).json()
print(get_data)
channel_id=get_data['channel']['id']

feild_1=get_data['feeds']
print(feild_1)

t=[]
for x in feild_1:
    print(x['field1'])
    t.append(x['field1'])







# Your data loading and processing code
dfn = pd.read_csv(f'Dataset/Rice/N.csv')
fn = dfn.query(f"""Season == {option} & Plot == {optionplot}""")
fn30 = fn.query(f"""Day == 30""")
fn60 = fn.query(f"""Day == 60""")
fn90 = fn.query(f"""Day == 90""")
nutrient_data = {'Mg': [fn30['Mg'].values[0], fn60['Mg'].values[0], fn90['Mg'].values[0]],
                 'Ca': [fn30['Ca'].values[0], fn60['Ca'].values[0], fn90['Ca'].values[0]],
                 'N': [fn30['N'].values[0], fn60['N'].values[0], fn90['N'].values[0]],
                 'P': [fn30['P'].values[0], fn60['P'].values[0], fn90['P'].values[0]],
                 'K': [fn30['K'].values[0], fn60['K'].values[0], fn90['K'].values[0]]}

df = pd.DataFrame.from_dict(nutrient_data, orient='index', columns=[30, 60, 90])

# Set "Day" column as the index
df.index = ['Day 30', 'Day 60', 'Day 90']

# Animated line chart with Plotly
fig = px.line(df.transpose(), x=df.columns, y=df.index,
              labels={'value': 'Nutrient Level', 'variable': 'Nutrient'},
              title='Nutrient Trend')
fig.update_traces(mode='lines+markers')

# Customize y-axis labels
fig.update_layout(yaxis=dict(tickvals=[0, 1, 2],  # Example custom tick values
                             ticktext=['Custom Label 1', 'Custom Label 2', 'Custom Label 3']))

# Display the animated chart
st.plotly_chart(fig)

