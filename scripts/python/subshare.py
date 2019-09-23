#!/usr/bin/env python
# _____  _              _       _____       _    _  _
#|   __||_| _____  ___ | | _ _ |   __| _ _ | |_ | ||_| _____  ___
#|__   || ||     || . || || | ||__   || | || . || || ||     || -_|
#|_____||_||_|_|_||  _||_||_  ||_____||___||___||_||_||_|_|_||___|
#                 |_|     |___|
import sys
import pyperclip
from subprocess import call

import screen
import upload
import shorten
import conversions


def Help():
    return("\n\
            ---------- The following options are available ----------\n\
            -s  | Capture screenshot of entire screen.\n\
            -sr | Capture screenshot of a drawable selection of the screen.\n\
            -t  | Will upload a text file to your instance of Hastebin.\n\
            -f  | Will upload a file to your instance of Nextcloud.\n\
            -l  | Will shorten a link via your Polr instance.\n")


def Share(type):
    if type == "-s":
        arg = "-s"
        pyperclip.copy(shorten.Link(upload.File(screen.screenShot(arg))))
        call(["notify-send", "Screenshot Captured", "-t", "1000"])
        return("Screenshot captured: Copied to clipboard")
    elif type == "-sr":
        arg = "-sr"
        pyperclip.copy(shorten.Link(upload.File(screen.screenShot(arg))))
        call(["notify-send", "Screenshot Captured", "-t", "1000"])
        return("Screenshot captured: Copied to clipboard")
    elif type == "file":
        return("")
    elif type == "text":
        return("")
    elif type == "":
        return("Please specify what to do. Use -h for help.")
    elif type == "-h":
        return(Help())
    else:
        return("Please specify what to do. Use -h for help.")


arg = sys.argv[1:]
f = Share(conversions.convertListString(arg))
print(f)
