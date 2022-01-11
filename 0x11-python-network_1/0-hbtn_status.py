#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        rsp = response.read()
        print('\t - type: {}'.format(type(rsp)))
        print('\t - content: {}'.format(rsp))
        print('\t - utf8 content: {}'.format(rsp.decode('UTF_8')))
