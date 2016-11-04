from scale import Scale
from nfcreader import Nfcreader
import subprocess
import configparser
import ast
import signal
import threading
import time

exitFlag = 0

#read from the config file
config = configparser.ConfigParser()

config.read('config.ini') #file that contains definitions of the application

emailsDev = ast.literal_eval(config.get("EMAILS", "developers"))
emailsInfra = ast.literal_eval(config.get("EMAILS", "infraestructure"))

msgs = ast.literal_eval(config.get("MESSAGES", "msgs"))

success = 1

class myThread(threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print "Starting" + self.name
		LerRFID()
		print "Exiting" + self.name
class myThread2(threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print "Starting thread " + self.name
		#print_time(self.name, 1, 5)
		lerBalanca()
		print "Exiting thread " + self.name

class myThread3(threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
		self.signal = True
	def run(self):
		print "Starting thread STOPWATCH" + self.name
		time.clock()
		setCount = 0
		while(self.signal):
			if(setCount < 20):
				printAndSleep(20 - setCount)
			if(setCount == 7):
				self.signal = False
			setCount += 1

		print "Exiting thread STOPWATCH" + self.name
		return
 
def LerRFID():
	print "LerRFID begin"
	try:
		iRfid = Nfcreader()
		user = iRfid.getID()
		#user = iRfid.readTag(iRfid.reader)
		print user
		print len(user)
	except:
		print "erro"
	print "LerRFID end"

def printAndSleep(number):
	print "%02d" % number
	time.sleep(1)

def lerBalanca():
	iScale = Scale()
	while True:
		x = iScale.readStability()		
		if(x == "1"):
			print "balanca foi pressionada"
			break

def print_time(threadName, delay, counter):
	while counter:
		if exitFlag:
			threadName.exit()
		c = 999999
		while ( c > 0):
			c = c - 1
		print "%s: %s" % (threadName, time.ctime(time.time()))
		counter -= 1

thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread2(2, "Thread-2", 2)

if __name__ == "__main__":

	print "main begin"
	thread1.start()
	thread2.start()
	

	print "Exiting main"
