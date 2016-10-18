from scale import Scale
from nfcreader import Nfcreader
import subprocess

balanca = Scale()
peso = balanca.read()
print peso

if (peso >= 80):
	subprocess.call(['./sendEmail.sh'])
rfid = Nfcreader()
print(rfid.getID())


