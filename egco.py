from scale import Scale
import sys
import subprocess
import configparser
import ast
import signal
from backendConnection import *
from myGpio import MyGPIO

#read from the config file
config = configparser.ConfigParser()

config.read('config.ini') #file that contains definitions of the application

deviceID = config.get("DEFAULT", "deviceID")
contributionType = config.get("DEFAULT", "contributionType")
emailsDev = ast.literal_eval(config.get("EMAILS", "developers"))
emailsInfra = ast.literal_eval(config.get("EMAILS", "infraestructure"))

msgs = ast.literal_eval(config.get("MESSAGES", "msgs"))

try:
	iGpio = MyGPIO()
except:
	print "GPIO Problem"
try:
	conn = CTDRequest()
except:
	print "Connection problem"
try:
	iScale = Scale()
except:
	print "scale problem"

while True:
	success = 1
	while(success == 1):
		#confirmation = "n"
		#iDisplay = Display()
		#conn = CTDRequest()
		#try:
		#        teste = Display()
		#except:
		#	print "aqui0"
		#try:
		#	leitorRFID = RFID()
		#except:
		#	print "aqui"
		#	sys.exit()
		try:
			iGpio.lcdPrint("Pass your badge\non the reader")
			userRFID = iGpio.readTag()
			
		except KeyboardInterrupt:
			print "interrupted by admin"
			sys.exit()
		except:
			iGpio.lcdPrint("rfid problem")
			sys.exit()

		try:
			response = conn.authenticateUser(userRFID, deviceID)
			response = json.loads(response)
			userName = response["d"]["name"]
			iNumber = response["d"]["idemployee"]
			iGpio.clear()
			if(userName != "Error."):
				iGpio.lcdPrint("Hello " + userName)
			else:
				iGpio.lcdPrint("First use\nCreate a user")
				print userRFID
				break
		except:
			iGpio.lcdPrint("Connection\nproblem!")
			sys.exit()

		#try:
		#	iScale = Scale()
		#except ValueError as err:
		#	teste.displayPrint(err.args)
		#	sys.exit()

		try:
			tare = iScale.readTare()
		except ValueError as err:
			iGpio.lcdPrint(err.args)
			sys.exit()
	
		#print tare	
		try:
			iGpio.lcdPrint("Put your\ncontribution")
			contribution = iScale.read()
		except ValueError as err:
			iGpio.lcdPrint(err.args)
			sys.exit()
		except KeyboardInterrupt:
			print "Interrupted by admin"
			sys.exit()

		contribution = contribution - tare
		if (contribution <= 0.1):
			print msgs[1]
			break
		
		if(success == 1):#all worked good
			iGpio.clear()
			iGpio.lcdPrint(str(contribution) + "Kg")
			weight = str(int(contribution * 1000))
			#print weight
			#print msgs[2]
			response = conn.makeContribution(weight,contributionType, iNumber)
			response = json.loads(response)
			iGpio.lcdPrint(response["d"]["weight"] + " g donnated\n" + response["d"]["total"] + " points received")
			#print "Thank you!"
			send_contribution(contribution, user)

		if (tare >= 80):
			for mail in emailsDev:
				args = ['./sendEmail.sh', mail]
				subprocess.call(args)
