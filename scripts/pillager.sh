#!/bin/bash
[[ -d $HOME/.pillager ]] || mkdir "$HOME/.pillager"
currentdir="$PWD"
SAVEPATH="/media/downloads/pillager"
list=$HOME/.pillager/list
echo -n "Link to pillage: "

read -r LINK

echo "$LINK" >> "$list"
wget -r -np -nc -e robots=off -c --reject index.html,index.html* "${LINK}" -P "$SAVEPATH"

echo "Finished. Yar."
