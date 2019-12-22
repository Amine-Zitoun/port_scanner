import os
import sys
import socket
import time
import threading
from queue import Queue 




print_lock = threading.Lock()




# gets the host to scan and ip_range
host = input("Enter host to scan: ")
port_range = int(input("enter range of ports to scan: "))


#connect function
def connect(port):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex(('127.0.0.1', port))
		print(result)
		if result == 0:
			print( "Port {}: 	 Open".format(port))
			return 'opened'
		sock.close()

	except KeyboardInterrupt:
		print ("You pressed Ctrl+C")
		sys.exit()

	except socket.gaierror:
		print ('Hostname could not be resolved. Exiting')
		sys.exit()

	except socket.error:
		print ("Couldn't connect to server")
		sys.exit()

OPEN = []
CLOSE =[]
for i in range(port_range):
	res = connect(i)
	if res== "opened":
		OPEN.append(i)

print("===============RESULTS======================")
print("===============OPENED PORTS=================")
for i in OPEN:
	print("[*] "+str(i))




