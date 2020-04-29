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
    
    
    ''' output of file rkdlink.txt
    
    https://www.repairkidukan.com/services/acrepairing,AC Repair Service
https://www.repairkidukan.com/services/washingmachine,Washing Machine Service
https://www.repairkidukan.com/services/fridge,Fridge Repair Service
https://www.repairkidukan.com/services/microwave-oven,Microwave Oven Repair Service
https://www.repairkidukan.com/services/lift-repair-service,Lift Repair Service
https://www.repairkidukan.com/services/electricalworks,Electrical Works
https://www.repairkidukan.com/services/plumbing,Plumber Service
https://www.repairkidukan.com/services/homepainting,Painting Service
https://www.repairkidukan.com/services/computers,Desktop/Laptop Sales & Service
https://www.repairkidukan.com/services/sofarepair,Sofa Repair & Cleaning
https://www.repairkidukan.com/customerbenifits,Customer Benefits
https://www.repairkidukan.com/faq,FAQ
https://www.repairkidukan.com/contact,Contact
https://www.repairkidukan.com/affliate,Affliate
'''
