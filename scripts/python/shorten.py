#!/usr/bin/env python
# _____  _              _       _____       _    _  _
#|   __||_| _____  ___ | | _ _ |   __| _ _ | |_ | ||_| _____  ___
#|__   || ||     || . || || | ||__   || | || . || || ||     || -_|
#|_____||_||_|_|_||  _||_||_  ||_____||___||___||_||_||_|_|_||___|
#                 |_|     |___|

from mypolr import PolrApi, exceptions
import sys

import conversions
def Link(url):
    server_url = 'https://s.atriox.io'
    api_key = '3b6dc0c36b8b5b4c29dd2eb8ba0573'
    api = PolrApi(server_url, api_key)

    try:
        shorted_url = api.shorten(url)
        return(shorted_url)
    except:
        return("Please pass a URL to be shortened")

#arg = sys.argv[1:]
#
#f = Link(conversions.convertListString(arg))
#print(f)