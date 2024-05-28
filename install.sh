#!/usr/bin/bash

apt install -y python3-pip
pip install python-uinput --break-system-packages

install main.py /usr/libexec/chuwi_tabletmoded

modprobe uinput
echo "uinput" > /etc/modules-load.d/uinput

echo "[Unit]
Description=Generate XW_TABLET_MODE signal

[Service]
ExecStart=/usr/libexec/chuwi_tabletmoded
Restart=always

[Install]
WantedBy=default.target
" > /lib/systemd/system/chuwi_tabletmoded.service

systemctl daemon-reload
systemctl enable chuwi_tabletmoded
systemctl start chuwi_tabletmoded

