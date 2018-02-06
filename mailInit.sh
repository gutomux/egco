#!/bin/bash

RASPNAME=$(awk -F "=" '/name/ {print $2}' /home/pi/egco/config.ini | tr -d '"')

cat <<EOF | /bin/nc mail.sap.corp 25
HELO $(hostname)
MAIL FROM: <augusto.ferreira@sap.com>
RCPT TO: $1
DATA
From: Augusto Ferreira <augusto.ferreira@sap.com>
To: $1
Date: $(date '+%a, %d %b %Y %H:%M:%S %z')
Subject: raspberryEGCO
Content-Type: text/plain; charset=UTF-8



$RASPNAME foi reiniciada.
 IP: $2

.
QUIT
EOF

