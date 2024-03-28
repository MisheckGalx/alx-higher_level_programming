#!/usr/bin/python3
"""0-hbtn_status module"""
import urllib.request

if __name__ == "__main__":
    """
    Fetches the status from https://alx-intranet.hbtn.io/status
    """

    # URL to fetch status from
    url = "https://alx-intranet.hbtn.io/status"

    # Fetching the status
    with urllib.request.urlopen(url) as response:
        resp = response.read()

        url_type = type(resp)
        html = resp.decode("UTF-8")

        # Printing the fetched information
        print("Body response:")
        print("\t- type: {}".format(url_type))
        print("\t- content: {}".format(resp))
        print("\t- utf8 content: {}".format(html))
