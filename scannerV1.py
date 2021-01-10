#!/bin/python

import sys
import socket
import time
from datetime import datetime
import multiprocessing.dummy as mp 

if len(sys.argv) == 3:
	target = socket.gethostbyname(sys.argv[1])
	threads = int(sys.argv[2])
else:
	print("Invalid format...")

print("*"*50)
print("scanning target "+target)
print("Time started: "+str(datetime.now()))
print("*"*50)
starttime = time.time()

try:	
	Openports = []
	def scanner(port):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = sock.connect_ex((target, port)) #returns connection status(0 or 1)
		if result == 0:
			Openports.append(port)
		sock.close()
	
	if __name__=="__main__":
    		p=mp.Pool(threads)
    		p.map(scanner,range(1,1200))
    		p.close()
    		p.join()
	print('Open ports:')
	print(*Openports, sep=',')	
except KeyboardInterrupt:
	print('Existing program...')
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()

except socket.error:
	print("server error")
	sys.exit()
print("---Scanning time- %s seconds ---" % (time.time() - starttime))