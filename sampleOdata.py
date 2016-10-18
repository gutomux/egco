import urllib
params = urllib.urlencode({'sensorvalue':55, 'sensorid': 1})
f = urllib.urlopen("https://iotscenarioi852863trial.hanatrial.ondemand.com/iotscenario/?action=addsensorvalue&unit=Celsius&sensorvaluemultiplier=1&sensorvaluecalibration=0",params)
print f.read()
