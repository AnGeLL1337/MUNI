from operator import index
import pandas as pd
import requests
import json
import os.path

url = 'https://id.muni.cz/simplesaml/module.php/proxystatistics/api.php'
result = requests.get(url).text
result = json.loads(result) #because NotImplementedError
df1 = pd.json_normalize(result) # creating the dataframe

if(os.path.exists('data.csv')): 
    df2 = pd.read_csv('data.csv')
    add = df1[~df1.apply(tuple, 1).isin(df2.apply(tuple,1))]
    had_changed = df2[df2.iloc[:, 0].isin(add.iloc[:, 0])]
    df2.at[had_changed.index] = add
    df2.to_csv('data.csv', encoding='utf-8', index=False)
else:
    df1.to_csv('data.csv', encoding='utf-8', index=False)
