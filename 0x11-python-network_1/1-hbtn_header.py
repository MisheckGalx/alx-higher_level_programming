#!/usr/bin/python3
"""1-hbtn_header module"""

import sys
import urllib.request

if __name__ == "__main__":
    """
     This script retrieves the value of the X-Request-Id
    header from the response of a given URL.
	"""

    # Obtain the URL from the command-line argument
    url = sys.argv[1]

    req = urllib.request.Request(url)

    # Request to the URL and retrieve the response
    with urllib.request.urlopen(req) as response:
        x_request_id = response.getheader("X-Request-Id")

        print("{}".format(x_request_id))
