#!/bin/python

import sys
import socket
import time
from datetime import datetime
import threading as td 

if len(sys.argv) == 2:
 target = socket.gethostbyname(sys.argv[1])
else:
 print("Invalid")

print("*"*50)
print("scanning target "+target)
print("Time started: "+str(datetime.now()))
print("*"*50)
starttime = time.time()
try:
 def scanner(start, end):	
  for port in range(start,end):
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   socket.setdefaulttimeout(1)
   result = sock.connect_ex((target, port)) #returns connection status(0 or 1)
   if result == 0:
    print("Port {} is open".format(port))
   sock.close()
	
 if __name__== "__main__":
  threadedscan1 = td.Thread(target=scanner, args=(1,300))
  threadedscan2 = td.Thread(target=scanner, args=(301,600))
  threadedscan3 = td.Thread(target=scanner, args=(601,900))
  threadedscan4 = td.Thread(target=scanner, args=(901,1200))
  threadedscan1.start()
  threadedscan2.start()
  threadedscan3.start()
  threadedscan4.start()
  threadedscan1.join()
  threadedscan2.join()
  threadedscan3.join()
  threadedscan4.join()
 
except KeyboardInterrupt:
 print("Existing program...")
 sys.exit()

except socket.gaierror:
 print("Hostname could not be resolved")
 sys.exit()

except socket.error:
 print("server error")
 sys.exit()

print("---Scanning time- %s seconds ---" % (time.time() - starttime))
