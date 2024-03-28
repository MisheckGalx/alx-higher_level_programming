#!/usr/bin/python3
"""1-hbtn_header module"""

import sys
from urllib import request

if __name__ == "__main__":
    # Obtain the URL from the command-line argument
    url = sys.argv[1]

    req = urllib.request.Request(url)

    # Request to the URL and retrieve the response
    with urllib.request.urlopen(req) as response:
        x_request_id = response.getheader("X-Request-Id")
