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
    print(html_content)

    def html_cleaning(html):
        cleaning = re.compile('<.*?>')
        return re.sub(cleaning, '', html_content)

    ### Split Random String
    # out1 = html_cleaning(html)
    # out2 = out1.split('string')[1]
    # out3 = out2.rstrip()

except IndexError:

    print("Usage: test.py <target_url>")
    print("EXAMPLE: test.py https://www.pudim.com.br")

except JSONDecodeError:
    print("ERROR: Decoding JSON has failed")
