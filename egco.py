from scale import Scale
from nfcreader import Nfcreader
from backendConnection import CTDRequest
import sys
import subprocess
import configparser
import ast
import signal
from backendConnection import *


#read from the config file
config = configparser.ConfigParser()

config.read('config.ini') #file that contains definitions of the application

deviceID = config.get("DEFAULT", "deviceID")
contributionType = config.get("DEFAULT", "contributionType")
emailsDev = ast.literal_eval(config.get("EMAILS", "developers"))
emailsInfra = ast.literal_eval(config.get("EMAILS", "infraestructure"))

msgs = ast.literal_eval(config.get("MESSAGES", "msgs"))


while True:
	success = 1
	while(success == 1):
		iRfid = Nfcreader()
		conn = CTDRequest()
		try:
			userRFID = iRfid.getID()
			
		except KeyboardInterrupt:
			print "interrupted by admin"
			sys.exit()
		except:
			print msgs[0]
			sys.exit()

		try:
			response = conn.authenticateUser(userRFID, deviceID)
			response = json.loads(response)
			userName = response["d"]["name"]
			iNumber = response["d"]["idemployee"]
			if(userName != "Error."):
				print "Hello " + userName
			else:
				print "Please, register yourself at the reception!"
				print userRFID
				break
		except:
			print "Connection problem!"
			break

		try:
			iScale = Scale()
		except ValueError as err:
			print(err.args)
			sys.exit()

		try:
			tare = iScale.readTare()
		except ValueError as err:
			print(err.args)
			sys.exit()
	
		#print tare	
		try:
			print "Put your contribution"
			contribution = iScale.read()
		except ValueError as err:
			print(err.args)
			sys.exit()
		except KeyboardInterrupt:
			print "Interrupted by admin"
			sys.exit()

		contribution = contribution - tare
		if (contribution <= 0.1):
			print msgs[1]
			break
		
		if(success == 1):#all worked good
			print str(contribution) + "Kg"
			weight = str(int(contribution * 1000))
			#print weight
			#print msgs[2]
			confirmation = raw_input('Do you want to send your contribution? y/n: ')
			if confirmation == 'y' or confirmation == 'Y':
				response = conn.makeContribution(weight,contributionType, iNumber)
				response = json.loads(response)
				print "You donnated " + response["d"]["weight"] + " grams and received " + response["d"]["total"] + " points"
				print "Thank you!"
			#send_contribution(contribution, user)

		if (tare >= 80):
			for mail in emailsDev:
				args = ['./sendEmail.sh', mail]
				subprocess.call(args)
