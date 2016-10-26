from scale import Scale
from nfcreader import Nfcreader
import subprocess
import configparser
import ast
import signal



config = configparser.ConfigParser()

config.read('config.ini') #file that contains definitions of the application

emails = ast.literal_eval(config.get("EMAILS", "developers"))



while True:
	iRfid = Nfcreader()
	if(iRfid.reader != -1):
		userRFID = iRfid.getID()
		#user = get_user(userRFID)
		#print user
		print userRFID
	else:
		print "Call Administration"
		break
	
	iScale = Scale()
	if(iScale.error == 0):
		contribution = iScale.read()
		print contribution
	else:
		print "Call Administration"
		break
	
	#send_contribution(contribution, user)
	if (contribution >= 80):
		for mail in emails:
			args = ['./sendEmail.sh', mail]
			subprocess.call(args)

