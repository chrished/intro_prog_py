#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 19:42:37 2018

@author: christoph
"""
import urllib.request
url = "https://www.ssa.gov/oact/babynames/names.zip"
filename = "/home/christoph/git/intro_prog_py/data/ssa.zip"
# Download the file from `url` and save it locally under `file_name`:
urllib.request.urlretrieve(url, filename)
# unzip
import zipfile
zip_ref = zipfile.ZipFile(filename, 'r')
zip_ref.extractall("/home/christoph/git/intro_prog_py/data/ssa")
zip_ref.close()
