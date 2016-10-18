#!/usr/bin/python
import serial


class Scale(object):
	"""The scale class is used to comunicate with the scale."""
	
	def __init__(self):
		self.scalePort = serial.Serial("/dev/ttyUSB0", baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)
		print("Connected to: " + self.scalePort.portstr)

	def read(self):
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
