#!/bin/bash
#
cat <<EOF | /bin/nc mail.sap.corp 25
HELO $(hostname)
MAIL FROM: <augusto.ferreira@sap.com>
RCPT TO: $1
DATA
From: Augusto Ferreira <augusto.ferreira@sap.com>
To: $1
Date: $(date '+%a, %d %b %Y %H:%M:%S %z')
Subject: Balanca Cheia
Content-Type: text/plain; charset=UTF-8
                                                                                                                                                                                               
$(hostname) esta quase cheia, passou dos 80kg.
Por favor, fazer a coleta.

.
QUIT
EOF
