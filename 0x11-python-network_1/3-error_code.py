#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8)."""

import urllib.request
import urllib.parse
from sys import argv
if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as res:
            response = res.read()
        print(response.decode("utf-8"))
    except urllib.error.HTTPError as error_code:
        print("Error code: {}".format(error_code.code))
