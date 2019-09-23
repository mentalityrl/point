#!/usr/bin/env python
# _____  _              _       _____       _    _  _
#|   __||_| _____  ___ | | _ _ |   __| _ _ | |_ | ||_| _____  ___
#|__   || ||     || . || || | ||__   || | || . || || ||     || -_|
#|_____||_||_|_|_||  _||_||_  ||_____||___||___||_||_||_|_|_||___|
#                 |_|     |___|
import owncloud
import sys
import os
# pip install --user pyocclient

import conversions

def File(file):
    oc = owncloud.Client('https://cloud.atriox.io')
    oc.login('sublime', 'BlueeYes2122!')
    fileName = os.path.basename(file)
    uploadDir = "123"
    try:
        oc.put_file(uploadDir + "/" + fileName, file)
        link_info = oc.share_file_with_link(uploadDir + "/" + fileName)
        return(link_info.get_link() + "/preview")
    except:
        print("Please pass a path to a file")

#arg = sys.argv[1:]
#
#f = File(conversions.convertListString(arg))
#print(f)
