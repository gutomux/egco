#!/usr/bin/python
#from time import sleep
import serial
import time
import io

try:

	
	port = serial.Serial("/dev/ttyUSB0", baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)
	print("connected to: " + port.portstr)
	sio = io.TextIOWrapper(io.BufferedRWPair(port, port))
	option = input("Coloque o material na balanca e depois pressione 1. \n ")
	estabilityCount = 0
	while (option == 1):
		sio.flush()
		line = port.readline()
		parameters = line.split(",")
		if (len(line) > 1 and line[0] == "0" and float(parameters[1]) > 0):
			estabilityCount = estabilityCount + 1
			if estabilityCount == 9: #ignora os dois primeiros sinais de estabilidade pra garantir que vai pegar o peso estavel correto
				break
	peso = float(parameters[1])
	print(peso)
	port.close()

except serial.SerialException as ex:
	print("exception treated")
except Exception:
	print("Device not connected")
