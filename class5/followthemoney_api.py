#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import json
import pandas as pd
import numpy as np

api_key = "###"
api_mode = "json"
api_url = "https://api.followthemoney.org/"

path_excel = "/home/christoph/git/intro_prog_py/class5/"

# load sets for which we want to download
df_sets = pd.read_excel(path_excel + "ftm.xlsx", sheet_name="Sheet4")
df_conditions = pd.read_excel(path_excel + "ftm.xlsx", sheet_name="Sheet5")
df_conditions.set_index("type", inplace=True)
conditions = list(df_conditions.keys())

# create empty list to store api responses
responses = []

# for each row in df_sets we download the Total $ given the conditions
# in df_conditions

for i, row in df_sets.iterrows():
    print("At row ", i)
    # add state and year condition
    apicall = api_url + "?" + "s=" + row["s"] + "&" + "y=" + str(row["y"]).replace(" ", "")
    # add rest of conditions
    rowconditions = df_conditions.loc[row["type"]]
    for condition in conditions:
        cond_val = rowconditions[condition]
        isstring = type(cond_val) == str
        if isstring or not np.isnan(cond_val):
            apicall += "&" + condition + "=" + str(rowconditions[condition]).replace(" ", "")

    # add api key and mode
    apicall += "&APIKey=" + api_key + "&mode=" + api_mode

    response = urllib.request.urlopen(apicall).read()
    responses.append(json.loads(response))


for i, row in df_sets.iterrows():
    print("At row ", i)
    df_sets.loc[i, "Total_$"] = responses[i]["records"][0]["Total_$"]["Total_$"]


print(df_sets.head())
df_sets.to_excel(path_excel + "ftm_res.xlsx")
