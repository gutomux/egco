from scale import Scale
from nfcreader import Nfcreader
import subprocess
import configparser
import ast
import signal


#read from the config file
config = configparser.ConfigParser()

config.read('config.ini') #file that contains definitions of the application

emailsDev = ast.literal_eval(config.get("EMAILS", "developers"))
emailsInfra = ast.literal_eval(config.get("EMAILS", "infraestructure"))

msgs = ast.literal_eval(config.get("MESSAGES", "msgs"))

success = 1

while True:
	if(success == 0):
		break
	success = 1
	while(success == 1):
		iRfid = Nfcreader()
		if(iRfid.reader != -1):
			userRFID = iRfid.getID()
			#user = get_user(userRFID)
			#print user
			print userRFID
		else:
			print msgs[0]
			success = 0
			break

		try:
			iScale = Scale()
		except ValueError as err:
			print(err.args)
			success = 0
			break

		try:
			tare = iScale.readTare()
		except ValueError as err:
			print(err.args)
			success = 0
			break
	
		print tare	
		try:
			contribution = iScale.read()
		except ValueError as err:
			print(err.args)
			success = 0
			break

		contribution = contribution - tare
		if (contribution <= 0.1):
			print msgs[1]
			break
		
		if(success == 1):#all worked good
			print msgs[2]
			print contribution
			#send_contribution(contribution, user)

		if (contribution >= 80):
			for mail in emailsDev:
				args = ['./sendEmail.sh', mail]
				subprocess.call(args)
