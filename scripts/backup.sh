#!/bin/bash
mkdir -p ~/point/config/home/.local/share

########## home ##########

cp -r ~/.themes ~/point/config/home/
cp -r ~/.icons ~/point/config/home/
cp -r ~/.local/share/fonts ~/point/config/home/.local/share/
cp -r ~/.vimrc ~/point/config/home/
cp -r ~/.xinitrc ~/point/config/home/
cp -r ~/.Xresources ~/point/config/home/
cp -r ~/.vim ~/point/config/home/
cp -r ~/.Xmodmap ~/point/config/home/
cp -r ~/.oh-my-zsh ~/point/config/home/
cp -r ~/.vscode ~/point/config/home/
cp -r ~/.xbindkeysrc ~/point/config/home/

########## .config ##########

cp -r ~/.config/wal ~/point/config/.config/
cp -r ~/.config/htop ~/point/config/.config/
cp -r ~/.config/neofetch ~/point/config/.config/
cp -r ~/.config/hmm ~/point/config/.config/
cp -r ~/.config/polybar ~/point/config/.config/
cp -r ~/.config/ranger ~/point/config/.config/
cp -r ~/.config/nvim ~/point/config/.config/nvim
cp -r ~/.config/dunst ~/point/config/.config/
cp -r ~/.config/user-dirs.dirs ~/point/config/.config/
cp -r ~/.config/qutebrowser/ ~/point/config/.config/
cp -r ~/.config/zathura/ ~/point/config/.config/
cp -r ~/.config/yay/ ~/point/config/.config/
cp -r ~/.config/mimeapps.list ~/point/config/.config/
cp -r ~/.config/compton/ ~/point/config/.config/
cp -r ~/.config/rofi/ ~/point/config/.config/
cp -r ~/.config/gtk-3.0/ ~/point/config/.config/
cp -r ~/.config/vlc/ ~/point/config/.config/
cp -r ~/.config/i3 ~/point/config/.config/
cp -r ~/.config/bspwm ~/point/config/.config/
cp -r ~/.config/sxhkd ~/point/config/.config/
cp -r ~/.config/compton ~/point/config/.config/
cp -r ~/.config/termite ~/point/config/.config/
cp -r ~/.config/code ~/point/config/.config/
cp -r ~/.config/vlc ~/point/config/.config/

########## /etc ##########
cp /etc/locale.gen ~/point/config/etc/
cp /etc/locale.conf ~/point/config/etc/

#mkdir ~/point/config/etc/systemd
sudo chown -R bryan:users ~/point/

echo Backup Complete
