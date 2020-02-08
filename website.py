import os
import bs4
import requests
import pandas as pd

PATH = os.path.join("/Users/andreadiotallevi/Code/AndreaDiotallevi/web-scraping")

url = "http://istanbulfilms.blogspot.com/2010/04/best-movies-from-afghanistan.html"

page = requests.get(url)
soup = bs4.BeautifulSoup(page.content, 'lxml')
div = soup.find(name='div', attrs={'id':'main'})
for b in soup.findAll('b'):
  point = str(b.text)
  # a = a.get('href')
  # if "imdb" in point: 
  # if "Blogger" in point:
    # print(point)
  if not b.find('a'):
    print(b.text)

    # soup.select("a[href*=http]")
# 
# https://api.themoviedb.org/3/search/movie?api_key=e3e4a0a5762593956dd3cdfb9cc2ed4f&language=en-US&page=1&include_adult=false&query=the-kite-runner