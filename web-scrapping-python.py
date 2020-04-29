#Web Scraping in Python
#Access the HTML of the webpage using request module and extract useful information/data from it using bs4 module of python.
# This technique is called web scraping or web harvesting or web data extraction.
# I have written a program to get links and its label from repairkidukan.com then save this informationinto a file for that I used csv module

import requests
from bs4 import BeautifulSoup
import csv

url1 = "https://www.repairkidukan.com"
r = requests.get(url1)
# print(r.content)
s = BeautifulSoup(r.content,'html5lib')
# print(soup.prettify())
links =[]
table = s.find('div',attrs={'id':'bs-example-navbar-collapse-1'})
# print(table)
for row in table.findAll('li'):
    link1 = {}
    link1['url2'] = row.a['href']
    link1['label2'] = row.text
    links.append(link1)
print('alok')
for link1 in links:
    print(link1)

filename ='rkdlink.txt'
with open(filename,'w') as f:
    w = csv.DictWriter(f,['url2','label2'])
    w.writeheader()
    for link in links:
        w.writerow(link)
    
