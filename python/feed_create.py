# %%
import requests
import json 

# %%
urlo = 'https://raw.githubusercontent.com/joshnicholas/Archives/main/Archive/feed/latest.json'

r = requests.get(urlo)

# %%
jsony = json.loads(r.text)

for entry in jsony:
    print(entry)


# %%