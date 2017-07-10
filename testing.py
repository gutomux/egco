import time
from scale import Scale
from myGpio import MyGPIO
from backendConnection import *


conn = CTDRequest()
iGPIO = MyGPIO()

while 1:
	iGPIO.lcdPrint("Passe o cracha")
	uTag = iGPIO.readTag()
	response = conn.authenticateUser(uTag, '3')
	response = json.loads(response)
	userName = response["d"]["name"]
	iNumber = response["d"]["idemployee"]
	print userName
	print iNumber
	print response

	time.sleep(3.0)
	iGPIO.clear()
