#!/usr/bin/python3
""" Python script that list 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”"""

import requests
from sys import argv
if __name__ == "__main__":
    req = requests.get('https://api.github.com/repos/{}/{}/commits'.
                       format(argv[2], argv[1]))
    if req.status_code < 400:
        for commit in req.json()[:10]:
            print("{}: {}".format(commit.get('sha'),
                  commit.get('commit').get('author').get('name')))
    else:
        print('None')
