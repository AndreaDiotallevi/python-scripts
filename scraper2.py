import os
import bs4
import requests
import pandas as pd

PATH = os.path.join("/Users/andreadiotallevi/Code/AndreaDiotallevi/web-scraping")

url = "http://istanbulfilms.blogspot.com/2010/05/top-films-from-guinea-1.html"

page = requests.get(url)
soup = bs4.BeautifulSoup(page.content, 'lxml')
div = soup.find(name='div', attrs={'id':'sidebar-right-1'})

websites = []

for li in soup.findAll('li'):
  websites.append(li.find('a').get('href'))

# print(websites)

# page = requests.get(websites[0])
# print(websites[0])
# soup = bs4.BeautifulSoup(page.content, 'lxml')
# div = soup.find(name='div', attrs={'id':'main'})

for website in websites:
  page = requests.get(website)
  soup = bs4.BeautifulSoup(page.content, 'lxml')
  div = soup.find(name='div', attrs={'id':'main'})
  for b in soup.findAll('b'):
    if not b.find('a'):
    print(b.text)

# imdb

# tags = soup.find_all('a')
# for tag in tags:
#     print(tag.get('href'))
