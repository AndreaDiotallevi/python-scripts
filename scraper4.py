import os
import bs4
import requests
import pandas as pd
import csv, json

jsonFilePath = 'movies.json'

PATH = os.path.join("/Users/andreadiotallevi/Code/AndreaDiotallevi/web-scraping")

url = "http://istanbulfilms.blogspot.com/2010/05/top-films-from-guinea-1.html"

page = requests.get(url)
soup = bs4.BeautifulSoup(page.content, 'lxml')
div = soup.find(name='div', attrs={'id':'sidebar-right-1'})


data = []
for li in soup.findAll('li'):
  page = requests.get(li.find('a').get('href'))
  soup = bs4.BeautifulSoup(page.content, 'lxml')
  div = soup.find(name='div', attrs={'id':'main'})
  for i, b in enumerate(soup.findAll('b')):
    if i == 0:
      country = b.text.split("FROM ")[-1]
      movies = []
    elif (not b.find('a')) and (b.text.strip()):
      movies.append(b.text.encode('utf-8'))
      # print(b.text)
  print({country:movies})
  # data.append({ country: movies })



# with open(jsonFilePath, "w") as jsonFile:
#   jsonFile.write(json.dumps(data, indent=4))
