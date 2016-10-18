#!/bin/bash
#
cat <<EOF | /bin/nc mail.sap.corp 25
HELO $(hostname)
MAIL FROM: <augusto.ferreira@sap.com>
RCPT TO: <augusto.ferreira@sap.com>
DATA
From: Augusto Ferreira <augusto.ferreira@sap.com>
To: <augusto.ferreira@sap.com>
Date: $(date '+%a, %d %b %Y %H:%M:%S %z')
Subject: raspberryEGCO
Content-Type: text/plain; charset=UTF-8
                                                                                                                                                                                               
A balança esta cheia.
 
.
QUIT
EOF
