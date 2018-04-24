#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:59:57 2018

@author: christoph
"""
#
## Word Reference example
#import urllib.request
#from bs4 import BeautifulSoup
#
#url = "http://www.wordreference.com/definicion/guapas"
#html = urllib.request.urlopen(url).read()
#soup = BeautifulSoup(html, "lxml")
##soup.find("div", { "class" : "stylelistrow" })
#defs = soup.find_all("strong")
#
#print(soup.prettify)
#


from bs4 import BeautifulSoup as bs
import pandas as pd
import urllib.request
import pickle
from unidecode import unidecode
from random import choice


def get_root(word, opener):
    word = unidecode(word).lower()
    link = 'http://www.wordreference.com/definicion/' + word
    page = opener.open(link)
    html = page.read()
    soup = bs(html)
    defs = soup.find_all('strong')
    return defs[1].contents


def dict_find(word, dict):
    try:
        return dict[unidecode(word).lower()]
    except Exception:
        return 'NA'


def split_seq(seq, p):
    newseq = []
    n = len(seq) / p    # min items per subsequence
    r = len(seq) % p    # remaindered items
    b, e = 0, n + min(1, r)  # first split
    for i in range(p):
        newseq.append(seq[b:e])
        r = max(0, r - 1)  # use up remainders
        b, e = e, e + n + min(1, r)  # min(1,r) is always 0 or 1

    return newseq

words = ["guapa", "guapos", "guapas"]

roots = {}
notfound = []
user_agents = [
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
]


opener = urllib.request.build_opener()
opener.addheaders = [
 ('User-agent', choice(user_agents))]
urllib.request.install_opener(opener)

i = 0
for word in words:
    i += 1
    try:
        roots[unidecode(word).lower()] = get_root(word, opener)[0]
    except Exception as e:
        print(e)
        notfound.append(word)

if len(notfound) > 0:
    f = open('notfound.txt','wb')
    pickle.dump(notfound, f)
    f.close()

data = pd.DataFrame({"word": words})

data['word_std'] = data['word'].apply(lambda x: dict_find(x, roots))

print(data.head())

data.to_csv('data_recoded.csv')
data.to_excel('data_recoded.xls')