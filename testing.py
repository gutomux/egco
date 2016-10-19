import subprocess

rasp = "rasp0123423"
email = "augusto.ferreira@sap.com"

args = ['./sendEmail.sh', rasp, email]
p = subprocess.call(args)
