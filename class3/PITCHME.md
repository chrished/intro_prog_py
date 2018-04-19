## Introduction to Python

---


### Class 3
Today:
1. Download a file/website with `urllib`
2. import data from file (with `csv` and `pandas`)
3. word count
4. extract info from html with `BeautifulSoup`

Checkout the documentation of the packages, they can do a lot more than just the examples here
---

### Download a file

```python
import urllib.request
import zipfile

url = "https://www.ssa.gov/oact/babynames/names.zip"
filename = "/home/christoph/git/intro_prog_py/data/ssa.zip"
# Download the file from `url` and save it locally under `file_name`:
urllib.request.urlretrieve(url, filename)
# unzip
zip_ref = zipfile.ZipFile(filename, 'r')
zip_ref.extractall("/home/christoph/git/intro_prog_py/data/ssa")
zip_ref.close()
```

---
### Load Data into Python
Variant 1: Pandas

```python
import pandas as pd

df = pd.read_csv("/home/christoph/git/intro_prog_py/data/ssa/yob1900.txt",
                  sep=",", names=¨["Name", "Sex", "Count"])

print(df.head())
```

---
### Load Data into Python
Variant 2: `open` and `csv`

```python

import csv

rows_read = []

with open("/home/christoph/git/intro_prog_py/data/ssa/yob1900.txt", 'rt') as ssafile:
    ssareader = csv.reader(ssafile, delimiter=',')
    for row in ssareader:
        rows_read.append(row)

print(rows_read[1:5])
```

---
### Analysis of data
you have the babynames in `df` (a pandas DataFrame), how to analyze?

```python
# maximum for all columns
print(df.max())

# What is that most frequent name?
mostcommon = df.loc[df['Count'] == df['Count'].max()]
# What is that median frequent name?
mediancommon = df.loc[df['Count'] == df['Count'].median()]
```

---
### Analysis of data - Exercises

1. Reshape Data such that for each name there is only one row, but separate counts for male and female occurrences.
2. For each year extract the 5 most common male and female names and put them in a new table (e.g. a pandas.DataFrame)


---
### Downloading a website
Similar to downloading a file
```python
import urllib.request

url = "https://en.wikipedia.org/wiki/Guido_van_Rossum"
response = urllib.request.urlopen(url)
html = response.read()    
```
---

### Extracting Info from HTML

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())

# website title
soup.title.string
# find all links
soup.find_all('a')
```

---

### Extracting Info from HTML - read text

```python
paragraphs = soup.find_all('p')
# the fifth paragraph describes where he lives
p5 = paragraphs[4].text
# count Guido
nGuido = p5.count("Guido")
print("We have found ", nGuido, " Guidos in our paragraph")
# alternative with regex for exact matches
import re
count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape("Guido"), p5))
# See: https://docs.python.org/3.6/howto/regex.html
```

---
### Extracting Info from HTML - read table
```python
# Find where Guido lives in a roundabout manner
table = soup.find('table')
for row in table.find_all('tr'):
    th = row.find('th')
    if th is not None:
        #print(th.string)    
        if th.string == "Residence":
            print("Guido lives in: ", row.find('a').string)
```

---
### What do you want to do as a project?
As an exercise carry out your project in a Github repository:
1. [Add an SSH key](https://help.github.com/articles/connecting-to-github-with-ssh/) to your Github account
2. Create a repository
3. Clone it to your computer (using the ssh link!)
4. add something your repository, commit your work and push it to the Github server
