import json
from backendConnection import CTDRequest
from nfcreader import Nfcreader
import sys


x = CTDRequest()
iRFID = Nfcreader()
rfid = iRFID.getID()

status = x.authenticateUser(rfid,'1')
myJson = json.loads(status)
iNumber = myJson["d"]["idemployee"]
name = myJson["d"]["name"]
print "iNumber: " + iNumber
print "name: " + name
#iRFID = Nfcreader()

#while True:
#	try:
#		rfidUser = iRFID.getID()
#		print rfidUser
#	except KeyboardInterrupt:
#		print "Bye"
#		sys.exit()
#	except:
#		print "Unknown error"
#	


#	userName = x.authenticateUser(rfidUser, "1")
#
#	if(len(userName) > 0):
#		print "Hello " + userName
#	else:
#		print "Please, register yourself at the reception"
#		status = x.createUser(rfidUser, '1', 'I844652')
#		print json.loads(status)
#		break
