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
Subject: Create User EGCO
Content-Type: text/plain; charset=UTF-8
                                                                                                                                                                                               
RFID NUMBER: $2
CODE: $3

.
QUIT
EOF
