## Introduction to Python

---
### Class 5

Today:
1. Web APIs
2. Projects

---
### APIs

what is an (API)[ https://en.wikipedia.org/wiki/Application_programming_interface]?

* software communication interface
* e.g. ask a website for specific data
* each API is different, but many common features

Example: Follow The Money

---
### Follow the Money API

https://www.followthemoney.org/our-data/apis/

Basic format:

`https://api.followthemoney.org/?s=CA&y=2004&mode=json&APIKey=#####`

* `s=CA` selects California
* `y=2003` selects 2003
* `mode=json` output in JSON format
* you need an API Key! (sign up on their page)
* for more detailed options see (documentation)[https://www.followthemoney.org/our-data/apis/]

---

### API in Python

* use `urllib.request` to get response from API
* `json` package to deal with response data
* JSON is a data format structured like a dictionary

---
### Projects

* first results?
* what are the biggest obstacles?
