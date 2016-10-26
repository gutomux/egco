import signal

def handler(signum, frame):
	print "Forever is over! hehe"
	raise Exception("end of time")

def loop_forever():
	a = 0
	import time
	while 1:
		a = a + 1
		print (a)
		time.sleep(1)


if __name__ == '__main__':
	signal.signal(signal.SIGALRM, handler)
	signal.alarm(10)
	try:
		loop_forever()
	except Exception, exc:
		print exc
