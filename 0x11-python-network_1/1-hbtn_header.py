#!/usr/bin/python3
"""Using urllib to send requests"""

import sys
from urllib import request

if __name__ == "__main__":

    # URL from the command-line argument
    url = sys.argv[1]

    # GET request to the URL
    with request.urlopen(url) as response:
        response_headers = dict(response.headers)

        # Get the X-Request-Id header from the response headers
        x_request_id = response_headers.get("X-Request-Id")
        if x_request_id:
            print(x_request_id)
