from scale import Scale
import time
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

raspName = config.get("DEFAULT", "name")
deviceID = config.get("DEFAULT", "deviceID")
contributionType = config.get("DEFAULT", "contributionType")
emailsDev = ast.literal_eval(config.get("EMAILS", "developers"))
emailUser = ast.literal_eval(config.get("EMAILS", "emailUser"))
emailsInfra = ast.literal_eval(config.get("EMAILS", "infraestructure"))

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
		try:
			iGpio.clear()
			iGpio.lcdPrint("Pass your badge\non the reader")
			iGpio.lcdBlink(True)
			userRFID = iGpio.readTag()
			
		except KeyboardInterrupt:
			print "interrupted by admin"
			sys.exit()
		except:
			iGpio.clear()
			iGpio.lcdPrint("rfid problem")
			sys.exit()

		try:
			iGpio.clear()
			iGpio.lcdPrint("Authenticating..")
			response = conn.authenticateUser(userRFID, deviceID)
			response = json.loads(response)
			userName = response["d"]["name"]
			userTemp = response["d"]["name"].split(' ')
			userFirstName = userTemp[0]
			iNumber = response["d"]["idemployee"]
			code = userRFID[:3]
			iGpio.clear()
			if(userName != "Error."):
				iGpio.lcdPrint("Hi " + userFirstName+"\n")
			else:
				iGpio.lcdPrint("First Use\nCode:" + code)
				for mail in emailUser:	
					args = ['./sendEmailUser.sh', mail, userRFID, code]
					print args
					subprocess.call(args)
				#args = ['./sendEmail.sh', mail]
                                #subprocess.call(args)

				time.sleep(5.0)
				break
		except:
			iGpio.clear()
			iGpio.lcdPrint("Connection\nproblem!")
			sys.exit()

		try:
			iScale = Scale()
		except ValueError as err:
			iGpio.clear()
			iGpio.lcdPrint("scale problem")
			sys.exit()

		try:
			tare = iScale.readTare()
		except ValueError as err:
			iGpio.clear()
			iGpio.lcdPrint("scale problem")
			sys.exit()
	
		print tare	
		try:
			iGpio.lcdPrint("Make donation")
			#TODO make cursor blink
			contribution = iScale.read()
		except ValueError as err:
			iGpio.clear()
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
			#iGpio.lcdPrint(str(contribution) + " Kg")
			weight = str(int(contribution * 1000))
			#print weight
			#print msgs[2]
			iGpio.lcdPrint("Sending..")
			response = conn.makeContribution(weight,contributionType, iNumber)
			response = json.loads(response)
			iGpio.clear()
			iGpio.lcdPrint(response["d"]["weight"] + " g\n" + response["d"]["total"] + " points")
			#print "Thank you!"
			time.sleep(5.0)
			#send_contribution(contribution, user)

		if (tare >= 80):
			for mail in emailsDev:
				args = ['./sendEmail.sh', mail]
				subprocess.call(args)
