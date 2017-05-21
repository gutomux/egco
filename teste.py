import rfid

test = rfid.RFID()

cartao = test.read()

print(cartao)
