#!/usr/bin/python3
"""using requests module to fetch"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Make a dictionary with the email parameter
    data = {'email': email}

    response = requests.post(url, data=data)
    print(response.text)
