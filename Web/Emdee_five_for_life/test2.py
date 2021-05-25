#!/usr/bin/python

import requests
import hashlib
import re

req = requests.session()
url = "http://159.65.57.12:32656/"

### GET Request
rget = req.get(url)
html = rget.content

### Strip HTML
def html_tags(html):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', html)

print(html_tags(html))

