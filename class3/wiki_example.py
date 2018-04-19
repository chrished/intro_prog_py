#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 10:51:01 2018

@author: christoph
"""

import urllib.request
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Guido_van_Rossum"
response = urllib.request.urlopen(url)
html = response.read()    

soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())

# website title
soup.title.string
# find all links
soup.find_all('a')

# find where Guido lives in a roundabout manner
table = soup.find('table')
for row in table.find_all('tr'):
    th = row.find('th')
    if th is not None:
        #print(th.string)    
        if th.string == "Residence":
            print("Guido lives in: ", row.find('a').string)

paragraphs = soup.find_all('p')

# the fifth paragraph describes where he lives
p5 = paragraphs[4].text 
# count Guido
p5.count("Guido")

# alternative with regex for exact matches
import re
count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("Guido"), p5))
# See: https://docs.python.org/3.6/howto/regex.html