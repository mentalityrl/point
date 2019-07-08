#!/bin/bash
clear

# Directory to save notes in
save_dir=~/Documents/Notes/
today=$(date "+%x %I:%M")

# Ask user which notepad they want to save to
echo Which Notepad?
read -p "> " notebook
echo ""
clear

# Get input from user
echo What would you like to add?
read -p "> " note
echo ""
clear

# echo todays date, time and user input to a file
echo "$today $note" >> ${save_dir}${notebook}

echo Note Saved
sleep 1
clear
