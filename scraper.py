import os
import bs4
import requests
import pandas as pd

PATH = os.path.join("/Users/andreadiotallevi/Code/AndreaDiotallevi/web-scraping")

def table_to_df(table):
	return pd.DataFrame([[li.text for li in ul.findAll('li')] for li in ul.findAll('li')])

# def next_page(soup):
# 	return "http:" + soup.find('a', attrs={'rel':'next'}).get('href')

res = pd.DataFrame()
url = "http://istanbulfilms.blogspot.com/2010/05/top-films-from-guinea-1.html"
counter = 0

# while True:
# 	print(counter)
# 	page = requests.get(url)
# 	soup = bs4.BeautifulSoup(page.content, 'lxml')
# 	table = soup.find(name='table', attrs={'class':'widget-content'})
# 	res = res.append(table_to_df(table))
# 	res.to_csv(os.path.join(PATH,"BIC","table.csv"), index=None, sep=';', encoding='iso-8859-1')
# 	url = next_page(soup)
# 	counter += 1

print(counter)
page = requests.get(url)
soup = bs4.BeautifulSoup(page.content, 'lxml')
table = soup.find(name='table', attrs={'class':'widget-content'})
res = res.append(table_to_df(table))
res.to_csv(os.path.join(PATH,"BIC","table.csv"), index=None, sep=';', encoding='iso-8859-1')
# url = next_page(soup)
# counter += 1

for ul in soup.findAll('ul', class_='widget-content'):
    for link in ul.findAll('a'):
        print(link.text)
