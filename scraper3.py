import os
import bs4
import requests
import pandas as pd
import csv, json

csvFilePath = "movies.csv"
jsonFilePath = 'movies.json'

PATH = os.path.join("/Users/andreadiotallevi/Code/AndreaDiotallevi/web-scraping")

url = "http://istanbulfilms.blogspot.com/2010/05/top-films-from-guinea-1.html"

page = requests.get(url)
soup = bs4.BeautifulSoup(page.content, 'lxml')
div = soup.find(name='div', attrs={'id':'sidebar-right-1'})


data = {}
with open(csvFilePath) as csvFile:
  for li in soup.findAll('li'):
    page = requests.get(li.find('a').get('href'))
    soup = bs4.BeautifulSoup(page.content, 'lxml')
    div = soup.find(name='div', attrs={'id':'main'})
    for b in soup.findAll('b'):
      if not b.find('a'):
        print(b.text)

# with open(jsonFilePath, "w") as jsonFile:
#   jsonFile.write(json.dumps(data, indent=4))
