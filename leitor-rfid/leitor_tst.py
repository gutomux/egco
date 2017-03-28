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
                    GPIO.cleanup()
                    # Inicia o módulo RC522.
                    LeitorRFID = MFRC522.MFRC522()

                    print('Aproxime seu cartão RFID')

                    while True:
                        # Verifica se existe uma tag próxima do módulo.
                        status, tag_type = LeitorRFID.MFRC522_Request(LeitorRFID.PICC_REQIDL)

                        if status == LeitorRFID.MI_OK:
                            print('Cartão detectado!')

                            # Efetua leitura do UID do cartão.
                            status, uid = LeitorRFID.MFRC522_Anticoll()

                            if status == LeitorRFID.MI_OK:
                                uid = ':'.join(['%X' % x for x in uid])
                                print('UID do cartão: %s' % uid)

                                uid = self.stringParser(userRFID=uid)
                                print('UID parseado: %s' % uid)
                                return uid
                                # Se o cartão está liberado exibe mensagem de boas vindas.
                                #if uid in self.CARTOES_LIBERADOS:
                                #    print('Acesso Liberado!')
                                #    print('Olá %s.' % CARTOES_LIBERADOS[uid])
                                #else:
                                #    print('Acesso Negado!')

                                print('\nAproxime seu cartão RFID')

                        time.sleep(.25)
                except KeyboardInterrupt:
                    # Se o usuário precionar Ctrl + C
                    # encerra o programa.
                    GPIO.cleanup()
                    print('\nPrograma encerrado.')
                                                       
