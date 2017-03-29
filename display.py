#!/usr/bin/python
import time
import Adafruit_CharLCD as LCD

class Display(object):
        """The display class is used to comunicate with the lcd display."""

        def __init__(self):
                try:
                        # Raspberry Pi pin configuration:
                        lcd_rs = 27  # Note this might need to be changed to 21 for older revision Pi's.
                        lcd_en = 22
                        lcd_d4 = 25
                        lcd_d5 = 24
                        lcd_d6 = 23
                        lcd_d7 = 18
                        lcd_backlight = 4

                        # Define LCD column and row size for 16x2 LCD.
                        lcd_columns = 16
                        lcd_rows = 2

                        # Initialize the LCD using the pins above.
                        self.lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                                                   lcd_columns, lcd_rows, lcd_backlight)         
                        self.lcd.set_backlight(0)
                except:
                        raise ValueError('display did not initialize well')


        def displayPrint(self, oMessage):
                try:
                        self.lcd.message(oMessage)
                except:
                        raise ValueError('display show message problem')
        def clear(self):
                self.lcd.clear()
