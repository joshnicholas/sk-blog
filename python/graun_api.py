import requests 
import json 
import datetime 
import dateparser
from bs4 import BeautifulSoup as bs 
import os 
import time 

keyo = os.environ['KEYO']

for page in range(2, 10):
# for page in range(1, 3):
  print("New page: ", page)


  tryo = f'https://content.guardianapis.com/search?byline=josh-nicholas&page={page}&api-key={keyo}'

  r = requests.get(tryo)

  jsony = json.loads(r.text)

  posts = jsony['response']['results']

  for post in posts:
    full_stem = post['id']
    stem = full_stem.split("/")[-1][:50]
    if stem not in  os.listdir('journalism/'):

      urlo = post['webUrl']

      datto = post['webPublicationDate']
      # print("Stem: ",stem)
      # print("Urlo: ", urlo)
      # print("Datto: ", datto)

      # datto = datetime.datetime.strptime(datto, "%Y-%m-%dT%H:%M%SZ")
      datto = dateparser.parse(datto).strftime("%Y-%m-%d")
      # print("Datto: ", datto.strftime("%Y-%m-%d"))
      # print(type(datto))

      ## Request the content

      new_tryo = f"https://content.guardianapis.com/{full_stem}?show-fields=standfirst,headline,byline&api-key={keyo}"


      r_sq = requests.get(new_tryo)

      new_jsony = json.loads(r_sq.text)['response']['content']

      heado = new_jsony['fields']['headline']
      print(heado)
      heado = heado.replace(":", " -")
      # heado.replace(",", " -")
      # heado = heado.replace("‘", "")
      # heado = heado.replace("’", "")
      print(heado)
      standfirst = new_jsony['fields']['standfirst']
      soup = bs(standfirst, 'html.parser')
      standfirst = soup.find('p').text
      byline = new_jsony['fields']['byline']

      if "Josh Nicholas" in byline:
        print(heado)
        print(standfirst)
        print(byline)
        with open(f'journalism/{stem}.md', 'w') as f:

          html = f"""---
title: {heado.strip()}
date: {datto}
---
<p>{standfirst.strip()}.</p><br>
<a href='{urlo.strip()}'>Read more.</a>"""
          f.write(html)
          # time.sleep(1)

    # print(new_jsony.keys())

  # # print(jsony)
  # print(jsony['response']['results'])
  # # print(r['results'])

  # # print(r.text)
  # print(r.status_code)