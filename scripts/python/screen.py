#!/usr/bin/env python
# _____  _              _       _____       _    _  _
#|   __||_| _____  ___ | | _ _ |   __| _ _ | |_ | ||_| _____  ___
#|__   || ||     || . || || | ||__   || | || . || || ||     || -_|
#|_____||_||_|_|_||  _||_||_  ||_____||___||___||_||_||_|_|_||___|
#                 |_|     |___|

import subprocess
import datetime
import sys

import conversions

def screenShot(type):
    now = datetime.datetime.now()
    currentTime = now.strftime("%Y-%m-%d_%H-%M-%S")
    saveDir = "/home/sublime/"
    saveName = saveDir + currentTime + ".png"
    if type == "-sr":
        subprocess.call(["scrot", "-s", saveName])
        return(saveName)
    else:
        type = "-s"
        subprocess.call(["scrot", saveName])
        return(saveName)

#arg = sys.argv[1:]
#screenShot(conversions.convertListString(arg))

