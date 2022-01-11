#!/usr/bin/python3
""" ython script that takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and finally displays the body
of the response"""

import requests
from sys import argv
if __name__ == "__main__":
    req = requests.post(argv[1], data={"email": argv[2]})
    print(req.text)
