#!/usr/bin/python3
"""Request module to send a request to the URL"""


import requests
import sys


if __name__ == "__main__":
    # URL from the command line argument
    url = sys.argv[1]

    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
