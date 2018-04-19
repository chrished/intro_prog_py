#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 10:20:51 2018

@author: christoph
"""

# Baby Names extract
import pandas as pd

df = pd.read_csv("/home/christoph/git/intro_prog_py/data/ssa/yob1900.txt", 
                 sep=",", names=["Name", "Sex", "Count"])

print(df.head())
print(df.tail())

# sort df by name alphabetically
# extract most common name
# extract name that is closest to having 50%-50% share 

