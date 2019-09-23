#!/usr/bin/env python
from subprocess import Popen
import json
import signal
from os import path
import colorama
from colorama import Fore, Style
import sys, tempfile, os
from subprocess import call
import datetime
from getpass import getuser



EDITOR = os.environ.get('EDITOR','nvim')

now = datetime.datetime.now()
dateTime = now.strftime("%Y-%m-%d %H:%M")
u = getuser()
saveDir = "/home/" + u + "/.config/hmm/"
bookFolder = saveDir + "books/"
bookConfig = saveDir + "books.json"


# Function grab the notebook key value
def getNotebook(key):
    value = notebook[key]
    return(value)

# Function to convert a string into a list
def Convert(string):
    li = list(string.split(" "))
    return li

def clearScreen():
    c = Popen(["clear"])
    c.wait()

def resetColor():
    print(Style.RESET_ALL)

def header():
    print(Fore.GREEN + "---------- Hmm? -----------")


def mainMenu():
    with open(bookConfig) as f:
        notebook = json.load(f)
    header()
    print(Fore.CYAN + "What would you like to do?")
    resetColor()
    print(Fore.YELLOW + "1. New note\n2. Add notebook\n3. Delete notebook\n4. Exit")
    resetColor()
    
    option = input(Fore.GREEN + "choice: " + Fore.YELLOW)
    resetColor()
    if option == "1":
        if not notebook:
            print(Fore.RED + "INFO: " + Fore.YELLOW + "There are no Books. Please create one first.")
            resetColor()
            addBook()
    else:
        return(option)
    


def addNote():
    with open(bookConfig) as f:
        notebook = json.load(f)
    header()
    print(Fore.CYAN + "-- Which book to add to? --")
    # Prints out list of notepads
    print(Fore.YELLOW)
    for i, item in enumerate(notebook, 0):
        print(i, ": " + item, sep="", end="\n")
    resetColor()
    
    book = getNotebook(int(input(Fore.GREEN + "\nchoice: ")))
    with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
        call([EDITOR, tf.name])
        # do the parsing with `tf` using regular File operations.
        # for instance:
        tf.seek(0)
        edited_note = tf.read()
        note = (edited_note.decode("utf-8"))

        with open(bookFolder + book + ".txt", 'a') as the_file:
            the_file.write(dateTime + "\n\n" + note + "\n")
            clearScreen()
            print(Fore.RED + "INFO: " + Fore.CYAN + "saved to book: " + Fore.RED + book)


def addBook():
    with open(bookConfig) as f:
        notebook = json.load(f)
    clearScreen()
    header()
    print(Fore.CYAN + "- Name for new book? -")
    
    newBook = Convert(
    input(Fore.YELLOW + "Name: " + Fore.GREEN))
    resetColor()
    notebook = notebook + newBook
    for i, item in enumerate(notebook, 0):
        print(i, ": " + item, sep="", end="\n")
    with open(bookConfig, "w") as f:
        json.dump(notebook, f)
    clearScreen()
    addedBook = ''.join(map(str, newBook))
    print(Fore.RED + "INFO: " + Fore.CYAN + "Book " + Fore.RED + addedBook + Fore.CYAN + " has been created" + Fore.WHITE)

def delBook():
    clearScreen()
    header()
    print(Fore.CYAN + "- What book to delete? -")
    print(Fore.YELLOW)
    for i, item in enumerate(notebook, 0):
        print(i, ": " + item, sep="", end="\n")
    resetColor()
    delBook = int(input(Fore.GREEN + "choice: "))
    del notebook[delBook]
    with open(bookConfig, "w") as f:
        json.dump(notebook, f)
    clearScreen()
    print(Fore.RED + "INFO: " + Fore.CYAN + "Book " + Fore.RED + str(delBook) + Fore.CYAN + " has been deleted" + Fore.WHITE)

def createConfig():
    print(Fore.RED + "INFO: " + Fore.YELLOW + "No config found. Creating new one!")
    call(["mkdir", "-p", bookFolder])
    resetColor()
    starterConfig = []
    with open(bookConfig, "w") as f:
        json.dump(starterConfig, f)

clearScreen()

run = True
while run == True:
    checkConfigExists = path.isfile(bookConfig)
    if checkConfigExists == False:
        createConfig()

    elif checkConfigExists == True:
        choice = mainMenu()
        with open(bookConfig) as f:
            notebook = json.load(f)

        if choice == "1":
            addNote()
        elif choice == "2":
            addBook()
        elif choice == "3":
            delBook()
        elif choice == "4":
            break
        else:
            print("")



