#!/usr/bin/python3
"""0-hbtn_status module"""
import urllib.request

if __name__ == "__main__":

# This script fetches information from https://alx-intranet.hbtn.io/status

import urllib.request

# The URL we want to fetch data from
url = 'https://alx-intranet.hbtn.io/status'

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    content = response.read()

# fetched information in a formatted manner
print("Body response:")
print("\t- type:", type(content))
print("\t- content:", content)
print("\t- utf8 content:", content.decode('utf-8'))
