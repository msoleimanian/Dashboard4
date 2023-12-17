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


