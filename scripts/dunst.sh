#!/usr/bin/env bash
pkill dunst

/usr/bin/dunst -config ~/.config/dunst/dunstrc\
    -frame_color "#c3e88d" \
    -lb "#263238" \
    -nb "#263238" \
    -cb "#263238" \
    -lf "#eeffff" \
    -bf "#eeffff" \
    -cf "#eeffff" \
    -nf "#eeffff"
