import time
from scale import Scale
from myGpio import MyGPIO
from backendConnection import *


conn = CTDRequest()
iGPIO = MyGPIO()
iScale = Scale()

while 1:
	iGPIO.lcdPrint("Passe o cracha")
	uTag = iGPIO.readTag()
	response = conn.authenticateUser(uTag, '3')
	response = json.loads(response)
	userName = response["d"]["name"]
	iNumber = response["d"]["idemployee"]
	teste = response["d"]["name"].split(' ')
	print teste[0]
	print userName
	print iNumber
	print response
	iScale.readTare()

	time.sleep(3.0)
	iGPIO.clear()
