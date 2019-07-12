#!/bin/bash

mkdir -p ~/.local/share
cp -r ~/point/config/home/. ~/
cp -r ~/point/config/.config/ ~/
sudo cp -r ~/point/config/etc/* /etc/
sudo cp -r ~/point/config/var/spool/cron/bryan /var/spool/cron
sudo cp -r ~/point/config/etc/default/tlp /etc/default/
sudo chown -R bryan:users /var/spool/cron/bryan
echo Restore Complete
notify-send "Restore Complete"
