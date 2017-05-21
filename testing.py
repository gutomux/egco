from scale import Scale
from myGpio import MyGPIO

iGPIO = MyGPIO()

iGPIO.lcdPrint("Passe o cracha")

uTag = iGPIO.readTag()

print "leu o cracha" + uTag

iGPIO.lcdPrint("\n" + uTag)


