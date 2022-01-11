#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)"""

import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    email = urllib.parse.urlencode({"email": argv[2]}).encode('ascii')
    req = urllib.request.Request(argv[1], email)
    with urllib.request.urlopen(req) as res:
        response = res.read()
        print(response.decode("UTF-8"))
