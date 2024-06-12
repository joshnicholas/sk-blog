# %%
import pandas as pd 
import requests
import json 

import os 
import pathlib
pathos = pathlib.Path(__file__).parent.parent
os.chdir(pathos)

# print(os.getcwd())

# %%

r = requests.get('https://raw.githubusercontent.com/joshnicholas/Archives/main/Combined/top_stories.json')

# %%

jsony = json.loads(r.text)

keys = list(jsony.keys())

exclude = ['goog_trends', 'wiki']
keys = [x for x in keys if x not in exclude]
listo = []

for keyo in keys:
    inter = pd.DataFrame.from_records(jsony[keyo])
    if 'Search_var' in inter.columns.tolist():
        inter.drop(columns={'Search_var'}, inplace=True)


    listo.append(inter)
    # print(keyo, inter.columns.tolist())
    

cat = pd.concat(listo)
# print(cat)


with open('static/dash.csv', 'w') as f:
    cat.to_csv(f, index=False, header=True)

# %%
