#!/usr/bin/env bash
pkill dunst
export DISPLAY=:0
. "${HOME}/.cache/wal/colors.sh"

/usr/bin/dunst -config ~/.config/dunst/dunstrc \
   -frame_color "${color7}" \
   -lb "${color0}" \
   -nb "${color0}" \
   -cb "${color0}" \
   -lf "${color7}" \
   -bf "${color7}" \
   -cf "${color7}" \
   -nf "${color7}" &

