import os
import bs4
import requests
import pandas as pd

PATH = os.path.join("/Users/andreadiotallevi/Code/AndreaDiotallevi/web-scraping")

url = "http://istanbulfilms.blogspot.com/2010/05/top-films-from-guinea-1.html"

page = requests.get(url)
soup = bs4.BeautifulSoup(page.content, 'lxml')
div = soup.find(name='div', attrs={'id':'sidebar-right-1'})
lists = div.find_all("li")

print(lists)

for li in soup.findAll('li'):
  print(li.find('a')['href'])
