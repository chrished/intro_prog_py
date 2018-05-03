#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 10:20:51 2018

@author: christoph
"""

# Baby Names extract
import pandas as pd

df = pd.read_csv("/home/christoph/git/intro_prog_py/data/ssa/yob1990.txt",
                 sep=",", names=["Name", "Sex", "Count"])

print(df.head())
print(df.tail())

# print out row if Name has "My" in it
for i, row in df.iterrows():
    if "My" in row["Name"]:
        print(row)

# subset to Rows with name "Emma"
emma_sub = df["Name"] == "Emma"
df.loc[emma_sub]
