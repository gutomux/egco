#!/usr/bin/python
import RPi.GPIO as GPIO
import MFRC522
import signal
import datetime
import Adafruit_CharLCD as LCD

class MyGPIO(object):
	"""This class is used to manage the RFID rader and the LCD display"""

	next_scan = True

	def end_scan(signal,frame):
		MyGPIO.next_scan
		print "Closing"
		MyGPIO.next_scan = False
		GPIO.cleanup()

	def stringParser(self, userRFID):
		strOut  = ''.join(['%X' % x for x in userRFID])
		str = "0"
		while (len(strOut) < 9):
			strOut = str + strOut
		return strOut
		
	def readTag(self):
		try:
			while MyGPIO.next_scan:
				# Verifica se existe uma tag proxima do modulo
				(status,TagType) = self.iRFID.MFRC522_Request(self.iRFID.PICC_REQIDL)

				# Efetua a leitura UID do cartao
				(status,uid) = self.iRFID.MFRC522_Anticoll()

				if status == self.iRFID.MI_OK:
					uTag = self.stringParser(userRFID=uid)
					return uTag
		except KeyboardInterrupt:
			# Se o usuario precionar Ctrl + C
			# encerra o programa.
			print('\nEnding program by user interruption.')
		except:
			raise ValueError('READ PROBLEM')
	def lcdBlink(self, status):
		try:
			self.lcd.blink(status)
		except:
			raise ValueError("display blink error")
	
	def lcdPrint(self, oMessage):
                try:
                        self.lcd.message(oMessage)
                except:
                        raise ValueError('display show message problem')
	def clear(self):
                self.lcd.clear()

	def __init__(self):
		signal.signal(signal.SIGINT, self.end_scan)

		self.iRFID = MFRC522.MFRC522()

		# Raspberry Pi pin configuration:
		lcd_rs = 26  # Note this might need to be changed to 21 for older revision Pi's.
		lcd_en = 19
		lcd_d4 = 13
		lcd_d5 = 6
		lcd_d6 = 5
		lcd_d7 = 27
		lcd_backlight = 4
		# Define LCD column and row size for 16x2 LCD.
		lcd_columns = 16
		lcd_rows = 2
		# Initialize the LCD using the pins above.
		self.lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)
