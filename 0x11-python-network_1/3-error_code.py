#!/usr/bin/python3
"""Using urllib to send a request"""

import sys
from urllib import request, error

if __name__ == "__main__":
    # Check the URL from the command line argument
    url = sys.argv[1]

    try:
        # Make a GET request to the URL
        with request.urlopen(url) as response:
            response_body = response.read().decode('utf-8')
			print(response_body)

    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
