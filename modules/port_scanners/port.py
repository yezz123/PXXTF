
from threading import Thread
import socket
import sys
import time
import random
import os, sys
# Set Color
R = '\033[31m' # Red
N = '\033[1;37m' # White
B = '\033[1;34m' #Blue
def main():
	os.system("clear && python new.py")

host = input(''+N+'Pentest>> ('+R+'scanner/port_scanners (set host)'+N+'): ')
print(""+N+"target => "+R+"",host)
if host == "back":
	main()
from_port = input(''+N+'Pentest>> ('+R+'scanner/port_scanners (start number)'+N+'): ')
if from_port == "back":
	main()
to_port = input(''+N+'Pentest>> ('+R+'scanner/port_scanners (end number)'+N+'): ')
if te_port == "back":
	main()
re = input("Pentest>> ("+R+"scanner/port_scanners"+N+"): ")
if re == "back":
	main()
elif re == "run":
	print(""+B+"[*]"+N+" Starting attacks...")
counting_open = []
counting_close = []
threads = []

def scan(port):
	s = socket.socket()
	result = s.connect_ex((host,port))
	print((' [OK] > '+(str(port))))
	if result == 0:
		counting_open.append(port)
		#print((str(port))+' -> open')
		s.close()
	else:
		counting_close.append(port)
		#print((str(port))+' -> close')
		s.close()

for i in range(from_port, to_port+1):
	t = Thread(target=scan, args=(i,))
	threads.append(t)
	t.start()

[x.join() for x in threads]

print(counting_open)
