#!/usr/bin/python3

import sys
import requests
import hashlib
import re
import json
from json.decoder import JSONDecodeError

try:
    # lê parâmetro direto da chamada do arquivo .py
    # nesse caso, o esperado é: test.py <url>
    # EXEMPLO: test.py https://www.pudim.com.br 

    url = sys.argv[1]

    resp = requests.get(url)

    html_content = resp.content

    def html_cleaning(html):
        cleaning = re.compile('<.*?>')
        return re.sub(cleaning, '', html)

    print(html_cleaning(str(html_content)))

except IndexError:

    print("Usage: test.py <target_url>")
    print("Usage example: test.py https://www.pudim.com.br")

except JSONDecodeError:
    print("ERROR: Decoding JSON has failed")