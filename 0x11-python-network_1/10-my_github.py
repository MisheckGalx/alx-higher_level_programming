#!/usr/bin/python3
"""using the GitHub API to siplay my id"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    # Username and password from the command line
    username = sys.argv[1]
    password = sys.argv[2]

    # GitHub API URL
    url = 'https://api.github.com/user'

    # Authentication
    auth = HTTPBasicAuth(username, password)

    # GET request to the GitHub API
    response = requests.get(url, auth=auth)
    print(response.json().get("id"))
