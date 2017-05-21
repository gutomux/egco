#!/usr/bin/env python
# -*- coding: utf8 -*-

import time
import RPi.GPIO as GPIO
import MFRC522

class leitorTest(object):

        def stringParser(self, userRFID):
                strOut = userRFID.replace(':','')
                return strOut

        def __init__(self):
                try:
                    #GPIO.cleanup()
                    # Inicia o módulo RC522.
                    self.LeitorRFID = MFRC522.MFRC522()
		    GPIO.setwarnings(False)
		except:
			raise ValueError('RFID did not initialize')

	def read(self):
		GPIO.setwarnings(False)
		try:
                    print('Aproxime seu cartão RFID')

                    while True:
                        # Verifica se existe uma tag próxima do módulo.
                  	status, tag_type = self.LeitorRFID.MFRC522_Request(self.LeitorRFID.PICC_REQIDL)

                        #if status == LeitorRFID.MI_OK:
			#print('Cartão detectado!')

			# Efetua leitura do UID do cartão.
			status, uid = self.LeitorRFID.MFRC522_Anticoll()

			if status == self.LeitorRFID.MI_OK:
				uid = ':'.join(['%X' % x for x in uid])
				print('UID do cartão: %s' % uid)

				uid = self.stringParser(userRFID=uid)
				print('UID parseado: %s' % uid)
				return uid

                        #time.sleep(.25)
                except KeyboardInterrupt:
                    # Se o usuário precionar Ctrl + C
                    # encerra o programa.
                    GPIO.cleanup()
                    print('\nPrograma encerrado.')
		except:
			GPIO.cleanup()
                                                       
