#!/usr/bin/python3

import sys
import requests
import hashlib
import re

try:

    str(sys.argv[1])
    print(f"The website you prompted is: {sys.argv[1]}")

except IndexError:

    print("Usage: test.py <target_url>")