#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 17:57:03 2018

@author: christoph
"""

# Baby Names extract
import pandas as pd

mostcommon = []
for year in range(1880, 2017):
    df = pd.read_csv("/home/christoph/git/intro_prog_py/data/ssa/yob" + 
                     str(year) + ".txt", sep=",", names=["Name", "Sex", "Count"])
    # subset female
    df_female = df.loc[df["Sex"]=="F"]
    maxcount = df_female["Count"].max()
    rowmax_f = df_female.loc[df_female["Count"]==maxcount]
    # subset male
    df_male = df.loc[df["Sex"]=="M"]
    maxcount = df_male["Count"].max()
    rowmax_m = df_male.loc[df_male["Count"]==maxcount]
    
    mostcommon.append({"Year": year, 
                       "MostCommonFemale": rowmax_f.iloc[0]["Name"], 
                       "MostCommonMale": rowmax_m.iloc[0]["Name"]})
    
dfmost = pd.DataFrame(mostcommon)

# .loc row index by label of row or True/False Vector
# .iloc row index by integer number of row
