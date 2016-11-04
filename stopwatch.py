#!/usr/bin/python
import time

#def stopwatch(seconds):
    #start = time.time()
    #time.clock()    
    #elapsed = 0
    #dec = seconds + 1
    #while elapsed < seconds:
        #elapsed = time.time() - start
        #print "%02d - " % (dec - elapsed) 
        #time.sleep(1)

def stopwatch(seconds):
	time.clock()
	secCount = 0
	while secCount < seconds:
		print "%02d" % (seconds - secCount)
		secCount += 1
		time.sleep(1)
