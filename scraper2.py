import os
import bs4
import requests
import pandas as pd
import csv, json

PATH = os.path.join("/Users/andreadiotallevi/Code/AndreaDiotallevi/web-scraping")

url = "http://istanbulfilms.blogspot.com/2010/05/top-films-from-guinea-1.html"

page = requests.get(url)
soup = bs4.BeautifulSoup(page.content, 'lxml')
div = soup.find(name='div', attrs={'id':'sidebar-right-1'})


data = {}
for li in soup.findAll('li'):
  page = requests.get(li.find('a').get('href'))
  soup = bs4.BeautifulSoup(page.content, 'lxml')
  div = soup.find(name='div', attrs={'id':'main'})
  for i, b in enumerate(soup.findAll('b')):
    if i == 0:
      country = b.text.split("FROM ")[-1]
      print(country)
      movies = []
    elif (not b.find('a')) and (b.text.strip()):
      movies.append(b.text)
      # title = b.text.encode('utf-8')
      # imdburl = soup.select_one("a[href*=imdb]")['href']
  data[country] = movies
with open("movies2.json", "w") as outfile:
  json.dump(data, outfile, indent=2)

# https://api.themoviedb.org/3/search/movie?api_key=e3e4a0a5762593956dd3cdfb9cc2ed4f&language=en-US&page=1&include_adult=false&query=the-kite-runner
