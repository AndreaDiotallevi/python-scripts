import os
import bs4
import requests
import pandas as pd

PATH = os.path.join("/Users/andreadiotallevi/Code/AndreaDiotallevi/web-scraping")

url = "http://istanbulfilms.blogspot.com/2010/05/top-films-from-guinea-1.html"

page = requests.get(url)
soup = bs4.BeautifulSoup(page.content, 'lxml')
div = soup.find(name='div', attrs={'id':'sidebar-right-1'})

for li in soup.findAll('li'):
  page = requests.get(li.find('a').get('href'))
  soup = bs4.BeautifulSoup(page.content, 'lxml')
  div = soup.find(name='div', attrs={'id':'main'})
  for b in soup.findAll('b'):
    if not b.find('a'):
      print(b.text)
