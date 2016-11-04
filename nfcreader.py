#! /usr/bin/env python
from smartcard.System import readers
from smartcard.util import toHexString
import logging
import logging.handlers

class Nfcreader(object):

	"""ACS ACR122U NFC Reader
	Suprisingly, to get data from the tag, it is a handshake protocol
	You send it a command to get data back
	This command below is based on the "API Driver Manual of ACR122U NFC Contactless Smart Card Reader"""
	
	def __init__(self):
		self.COMMAND = [0xFF, 0xCA, 0x00, 0x00, 0x00] #handshake cmd needed to initiate data transfer
		self.GET_ID_COMMAND = [0xFF, 0xCA, 0x00, 0x00, 0x00]
		self.logger = logging.getLogger('nfcreader')
		self.logger.setLevel(logging.DEBUG)

		self.log_filename = 'nfcreader.log'

		self.hdlr = logging.handlers.RotatingFileHandler(
			  self.log_filename, maxBytes=10*1024*1024, backupCount=5)
		self.formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
		self.hdlr.setFormatter(self.formatter)
		self.logger.addHandler(self.hdlr) 
		#connecting the reader
		try:
			self.reader = readers()[0]
			self.logger.debug('Connected to reader: ' + str(self.reader))
			print('Connected to reader: ' + str(self.reader))
		except:
			self.reader = -1
			self.logger.debug('Error, reader disconnected')
			print "No RFID reader available"

	def stringParser(self, dataCurr):
		#--------------String Parser--------------#
		#([85, 203, 230, 191], 144, 0) -> [85, 203, 230, 191]
		if isinstance(dataCurr, tuple):
			temp = dataCurr[0]
			code = dataCurr[1]
		#[85, 203, 230, 191] -> [85, 203, 230, 191]
		else:
			temp = dataCurr
			code = 0

		dataCurr = ''

		#[85, 203, 230, 191] -> bfe6cb55 (int to hex reversed)
		for val in temp:
			# dataCurr += (hex(int(val))).lstrip('0x') # += bf
			dataCurr += format(val, '#04x')[2:] # += bf
		#bfe6cb55 -> BFE6CB55
		dataCurr = dataCurr.upper()

		#if return is successful
		if (code == 144):
			return dataCurr

	def readTag(self, reader):
		readingLoop = 1
		while(readingLoop):
			try:
				connection = reader.createConnection()
				status_connection = connection.connect()           
				connection.transmit(self.COMMAND)
				resp = connection.transmit(self.GET_ID_COMMAND)
		    
				if(resp is not None):
					return self.stringParser(dataCurr=resp)
				else:
					self.logger.error('Error while reading tag')
					break
			except Exception,e:
				continue        


	def getID(self):	
		#reader must be connected
		id = self.readTag(self.reader)
		idStr = str(id)
		while(len(idStr) < 8 or idStr == "None"):
			#There was an error and the reader didnt work
			id = self.readTag(self.reader)
			idStr = str(id)
		return idStr

