#!/usr/bin/python
import RPi.GPIO as GPIO
import MFRC522
import signal
import datetime
import Adafruit_CharLCD as LCD

next_scan = True

def end_scan(signal,frame):
	global next_scan
	print "selesai"
	next_scan = False
	GPIO.cleanup()

signal.signal(signal.SIGINT, end_scan)

MIFAREReader = MFRC522.MFRC522()

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
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

while next_scan:

	(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
	#if status == MIFAREReader.MI_OK:
	#	print "alou1"

	(status,uid) = MIFAREReader.MFRC522_Anticoll()
	if status == MIFAREReader.MI_OK:
		#idRFID = str(uid[0])+""+str(uid[1])+""+str(uid[2])+""+str(uid[3])
		uRFID = ''.join(['%X' % x for x in uid])
		str = "0"
		while (len(uRFID) < 9):
			uRFID = str + uRFID
		lcd.clear()
		print(uRFID)
		lcd.message(uRFID)
