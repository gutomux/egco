#/usr/bin/env python
# -*- coding: utf8 -*-

import MFRC522_NEW

class RFID(object):
	"""Interface class for the RFID device"""
        def stringParser(self, userRFID):
		strOut  = ''.join(['%X' % x for x in userRFID])
                return strOut

        def __init__(self):
                try:
                    # Inicia o módulo RC522.
                    self.LeitorRFID = MFRC522_NEW.MFRC522_NEW(dev='/dev/spidev0.1',spd=1000000)
		except:
		    raise ValueError('RFID did not initialize')

	def read(self):
		try:
                    print('Aproxime seu cartão RFID')

                    while True:
                        # Verifica se existe uma tag próxima do módulo.
                  	status, tag_type = self.LeitorRFID.MFRC522_NEW_Request(self.LeitorRFID.PICC_REQIDL)

			# Efetua leitura do UID do cartão.
			status, uid = self.LeitorRFID.MFRC522_NEW_Anticoll()

			if status == self.LeitorRFID.MI_OK:
				uid = self.stringParser(userRFID=uid)
				return uid
                except KeyboardInterrupt:
                    # Se o usuário precionar Ctrl + C
                    # encerra o programa.
                    print('\nPrograma encerrado.')
		except:
		    raise ValueError('READ PROBLEM')
