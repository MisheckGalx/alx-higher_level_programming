#!/usr/bin/python3
"""1-hbtn_header module"""

import sys
from urllib import request

if __name__ == "__main__":
    # Obtain the URL from the command-line argument
    url = sys.argv[1]

    req = urllib.request.Request(url)

    # Request to the URL and retrieve the response
    with request.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
