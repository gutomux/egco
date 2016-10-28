#!/usr/bin/python
import serial


class Scale(object):
	"""The scale class is used to comunicate with the scale."""
	
	def __init__(self):
		try:
			self.scalePort = serial.Serial("/dev/ttyUSB0", baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)
			print("Connected to: " + self.scalePort.portstr)
		except:
			raise ValueError('scale did not initialize well')

	def readOld(self):
		stabilityCount = 0
		with open('lastmeasures.txt', 'r') as f:
			for line in f:
				lastWeight = line
		f.close()
		fLastWeight = float(lastWeight)
		fLastWeight = fLastWeight + 0.05
		while True:
			line = self.scalePort.readline()
			parameters = line.split(",")
			if (len(line) > 1 and line[0] == "0" and (float(parameters[1]) > fLastWeight)):
				stabilityCount = stabilityCount + 1
				if stabilityCount == 4: #We need to bypass the first and second reads because it was not stable
					break
		peso = float(parameters[1])
		with open('lastmeasures.txt', 'a') as f:
			f.write(str(peso))
			f.write("\n")
		f.close()
		return float(peso)

	def readTare(self):
		serialCount = 0
		while True:
			try:
				line = self.scalePort.readline()
			except:
				raise ValueError('serial problem')
				break
			#parameters = line.split(",")
			if(len(line) < 1):
				serialCount = serialCount + 1
				if(serialCount == 8000):
					print line
					raise ValueError('serial problem 02')

			else:
				print "here\n"
				serialCount = 0
				if(line[0] == "0"):
					break
		parameters = line.split(",")
		weight = float(parameters[1])
		return weight

	def read(self):
		stabilityCount = 0
		stabilityFlag = 0
		while True:
			line = self.scalePort.readline()
			parameters = line.split(",")
			#wait for user put something on the scale
			if (len(line) > 1):
				if(line[0] == "1"): #the first signal of instability (line[0]=1) indicates that the user put something on the scale
					stabilityFlag = 1
				
				if(line[0] == "0" and stabilityFlag == 1): #when the scale is stable after the user interacts with it
					stabilityCount = stabilityCount + 1 #It seems that the firsts signals of stability are not that stable hehe
					if (stabilityCount == 3):
						break
		weight = float(parameters[1])
		return weight			

