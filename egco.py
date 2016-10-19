from scale import Scale
from nfcreader import Nfcreader
import subprocess
import configparser
import ast



config = configparser.ConfigParser()

config.read('config.ini')

emails = ast.literal_eval(config.get("EMAILS", "developers"))
rasp = config.get("DEFAULT", "name") 
for item in emails:
	print item


balanca = Scale()
peso = balanca.read()
print peso

if (peso >= 80):
	for mail in emails:
		args = ['./sendEmail.sh', rasp, mail]
		subprocess.call(args)
rfid = Nfcreader()
print(rfid.getID())


