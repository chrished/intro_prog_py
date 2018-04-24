#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:59:57 2018

@author: christoph
"""
from bs4 import BeautifulSoup as bs
import pandas as pd
import urllib.request
import pickle
from unidecode import unidecode

# Function that finds root on word reference
def get_root(word, opener):
    word = unidecode(word).lower()
    link = 'http://www.wordreference.com/definicion/' + word
    page = opener.open(link)
    html = page.read()
    soup = bs(html, "lxml")
    defs = soup.find_all('strong')
    return defs[1].contents

# Find a key in dictionary, return "NA" in case not found
def dict_find(word, dictionary):
    try:
        return dictionary[unidecode(word).lower()]
    except Exception:
        return 'NA'


# prepare urllib opener
user_agent =  'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36 '
opener = urllib.request.build_opener()
opener.addheaders = [
 ('User-agent', user_agent)]
urllib.request.install_opener(opener)

# word list and empty dictionary/list for results
words = ["guapa", "guapos", "guapas"]
roots = {}
notfound = []

# get word roots from Word Reference
for word in words:
    try:
        roots[unidecode(word).lower()] = get_root(word, opener)[0]
    except Exception as e:
        print(e)
        notfound.append(word)

# Dump notfound list
if len(notfound) > 0:
    f = open('notfound.txt','wb')
    pickle.dump(notfound, f)
    f.close()

# make a dataframe from our results
data = pd.DataFrame({"word": words})
# add the word root we found
data['word_std'] = data['word'].apply(lambda x: dict_find(x, roots))

print(data.head())

# save results
data.to_csv('data_recoded.csv')
data.to_excel('data_recoded.xls')