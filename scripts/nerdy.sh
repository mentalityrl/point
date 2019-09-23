#!/bin/bash
clear
# a system info script written by yours truly
# it's hardcoded stuff, lulz

red="\e[31m"
grn="\e[32m"
ylw="\e[33m"
cyn="\e[36m"
blu="\e[34m"
prp="\e[35m"
bprp="\e[35;1m"
rst="\e[0m"
blk="\e[30m"

color-echo()
{  # print with colors
  echo -e " $red$1  $rst$2"
}

# kernel
color-echo 'kernel' "$(uname -s)"

# shell
color-echo 'Shell ' 'ZSH'

# wm
color-echo 'WM    ' 'BSPWM'

# CPU
color-echo 'CPU   ' 'I5 6600k'

# GPU
color-echo 'GPU   ' 'R9 390'

# distro
color-echo 'Distro' 'ArchyBoi'

# ascii art
#echo -e "        "
#echo -e " $grn(-_-) Sublime"
#echo -e "        "

# colors
echo -e " $blk$rst $red$rst $grn$rst $blu$rst $ylw$rst $cyn$rst $prp$rst $bprp$rst"
