# %%

import requests
import json 
import shutil 

from sudulunu.helpers import rand_delay

from bs4 import BeautifulSoup as bs 

import os 
import pathlib
pathos = pathlib.Path(__file__).parent
os.chdir(pathos)
# print(os.getcwd())

import dateparser
urlo = 'https://joshnicholas.blog/categories/scribbles/feed.json'



# %%

r = requests.get(urlo)

def already_done(pathos, to_remove):
    import os 
    # print(os.getcwd())
    there = os.listdir(pathos)
    for thingo in to_remove:
        there = [x.replace(thingo, '').strip() for x in there]
    # print(type(there))
    # print(there)
    return there 

# %%

jsony = json.loads(r.text)

# print(jsony.keys())
items = jsony['items'][:10]

print(items)

for item in items:
    # print(item)
    datto = dateparser.parse(item['date_published'])
    # print("datto: ", datto)
    # print(type(datto))
    pub_date = datto.strftime("%Y-%m-%d")
    datto_stemmo = datto.strftime("%y%m%d")
    # print(datto)

    to_write = False 

    # donners = already_done('mds', '')
    donners = already_done('/Users/josh/Github/sk-blog/scribbles', '')
    # print("donners: ", donners)

    newrl = item['url']
    stemmo = newrl.split("/")[-1].split(".")[0]
    new_stemmo = f"{datto_stemmo}_{stemmo.replace("-", "_")}.md"
    soup = bs(item['content_html'], 'html.parser')

    image_counter = 0
    images = soup.find_all('img')

    para = soup.find("p").text

    print("New_stemmo: ", new_stemmo)

    if new_stemmo not in donners:
        
        print(newrl)
        rand_delay(2)

        for image in images:

            new_image_stemmo = f"{datto_stemmo}_{stemmo}_{image_counter}.jpg"
            new_image_source = image['src']

            if 'uploads/2' in new_image_source:
                new_image_source = 'https://joshnicholas.blog/' + new_image_source
            print("new_image_source: ", new_image_source)

            image_r = requests.get(new_image_source, stream = True)
            with open(f"images/{new_image_stemmo}",'wb') as f:
                shutil.copyfileobj(image_r.raw, f)

            image_counter += 1
            # print(image) 

            stringo = f"""---
title: {[para]}
date: {pub_date}
---

![‘{para}’](/{new_image_stemmo})

{para}
"""

            with open(f"mds/{new_stemmo}", 'w') as f:
                f.write(stringo)


# %%


