#!/usr/bin/env python2


import argparse
import re
import socket
import ssl
import sys
import time

apacheserver = 'Apache'
iisserver = 'Microsoft-IIS'
unknown = 'unknown'

stdMethods = ['GARBAGE / ', 'GET / ', 'HEAD / ', 'PUT /filetocreate.html CY', '\
TRACE / ', 'OPTIONS / ', 'DELETE /filetocreate.html ', 'POST /index.html CY', '\
CONNECT 127.0.0.1:443 ', 'PATCH /index.html CY']

iisMethods = ['BCOPY / CY', 'BDELETE / CY', 'BMOVE / CY','BPROPFIND / CY', 'BPR\
OPPATCH / CY','COPY / CY', 'LOCK / CY', 'MKCOL / CY', 'MOVE / ', 'NOTIFY / ', '\
POLL / ', 'PROPFIND / ', 'PROPPATCH / ', 'SEARCH / ', 'SUBSCRIBE / ', 'UNLOCK /\
 ', 'UNSUBSCRIBE / ', 'X-MS-ENUMATTS / ']

apacheMethods = ['ACL / ', 'BASELINE-CONTROL / ', 'BCOPY / ', 'BDELETE / ', 'BM\
OVE / ', 'BPROPFIND / ', 'BPROPPATCH / ', 'CHECKIN / ', 'CHECKOUT / ', 'COPY / \
', 'DEBUG / ', 'DELETE / ', 'INDEX / ', 'LABEL / ', 'LOCK / ', 'MERGE / ', 'MKA\
CTIVITY / ', 'MKCOL / ', 'MKWORKSPACE / ', 'MOVE / ', 'NOTIFY / ', 'ORDERPATCH \
/ ', 'PATCH / ', 'POLL / ', 'PROPFIND / ', 'PROPPATCH / ', 'REPORT / ', 'RPC_IN\
_DATA / ', 'RPC_OUT_DATA / ', 'SEARCH / ', 'SUBSCRIBE / ', 'UNCHECKOUT / ', 'UN\
LOCK / ', 'UNSUBSCRIBE / ', 'UPDATE / ', 'VERSION-CONTROL / ', 'X-MS-ENUMATTS /\
 ']

apache = []
frontpage = []
sharepoint = []

found = []
auth = []
unauth = []
result = False

content = 'Content-Type: text/plain\r\nContent-Length: 4\r\n\r\nabcd'

print ('''Start Enumeration\n''')

parser = argparse.ArgumentParser(
    add_help=False,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog='Examples: %(prog)s -t 192.168.0.1 -d www.example.com -p 443 -v -s -\
l 0.5')

parser.add_argument('-t', dest='target', help='Target IP / Domain', required='y\
es')
parser.add_argument('-c', dest='cookie', help='Cookie to use for enumeration')
parser.add_argument('-d', dest='domain', help='For domains with multiple IPs')
parser.add_argument('-p', dest='port', help='Target port')
parser.add_argument('-l', dest='delay', help='Delay between requests')
parser.add_argument('-s', action='store_true', help='Enable SSL')
parser.add_argument('-v', action='store_true', help='Enable verbose')
parser.add_argument('-h', action='help', help='Print this help message and exit\
')

args = parser.parse_args()
target = args.target

if args.v:
    verbose = True
else:
    verbose = False

if args.domain:
    domain = args.domain
else:
    domain = target

if args.s:
    s = True

else:
    s = False

if args.port:
    try:
        port = int(args.port)
    except Exception as error:
        print(error)
        sys.exit()
else:
    if s == True:
        port = 443
    else:
        port = 80

if args.delay:
    try:
        delay = float(args.delay)
    except Exception as error:
        print(error)
        sys.exit()
else:
    delay = float(0.5)

if args.cookie:
    try:
        cookie = 'Cookie: ' + args.cookie
    except Exception as error:
        print(error)
        sys.quit()
else:
    cookie = ''


def run_threads():
    pass


def detect():
    try:
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)

        if s == True:
            ssl_sock = ssl.wrap_socket(sock)
            ssl_sock.connect((target, port))
            ssl_sock.write('HEAD / HTTP/1.1\r\n')
            ssl_sock.write('Host: ' + domain + '\r\n')

            if cookie != '':
                ssl_sock.write(cookie + '\r\n')

            ssl_sock.write('\r\n')
            data = ssl_sock.read(1024)
            ssl_sock.close()

        else:
            sock.connect((target, port))
            sock.send('HEAD / HTTP/1.1\r\n')
            sock.send('Host: ' + domain + '\r\n')

            if cookie != '':
                sock.send(cookie + '\r\n')

            sock.send('\r\n')
            data = sock.recv(1024)
            sock.close()

        for item in data.split('\n'):
            if 'Server:' in item:
                server = item.lower()
                if iisserver.lower() in server:
                    print(server)
                    enumerate(iisserver)
                    sys.exit()
                elif apacheserver.lower() in server:
                    print(server)
                    enumerate(apacheserver)
                    sys.exit()
                else:
                    print(server)
                    enumerate(server)
                    sys.exit()

        print('No Server header found!')
        enumerate(unknown)
        sys.exit()
    except Exception as error:
        print(error)
        sys.exit()


def enumerate(server):
    if server == iisserver:
        try:
            requests = open('modules/enum/sharepoint')
            for row in requests:
                row = row.strip('\n')
                sharepoint.append('GET /' + row + ' ')

            requests = open('modules/enum/frontpage')

            for row in requests:
                row = row.strip('\n')
                frontpage.append('GET /' + row + ' ')
                methods = stdMethods + iisMethods + frontpage + sharepoint
        except Exception as error:
            print(error)
            print('Using Standard + IIS methods only')
            methods = stdMethods + iisMethods
    elif server == apacheserver:
        try:
            requests = open('modules/enum/apache')

            for row in requests:
                row = row.strip('\n')
                apache.append('GET /' + row + ' ')

            methods = stdMethods + apacheMethods + apache
        except Exception as error:
            print(error)
            print('Using Standards methods only')
            methods = stdMethods
    else:
        methods = stdMethods

    for method in methods:
        i = 0
        try:
            required = False
            sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            time.sleep(delay)

            if method.endswith(' CY'):
                required = True
                method = method.replace(' CY', ' ')

            if s == True:
                ssl_sock = ssl.wrap_socket(sock)
                ssl_sock.connect((target, port))
                ssl_sock.write(method + 'HTTP/1.1\r\n')
                ssl_sock.write('Host: ' + domain + '\r\n')

                if cookie != '':
                    ssl_sock.write(cookie + '\r\n')

                if required == True:
                    ssl_sock.write(content)
                    required = False

                ssl_sock.write('\r\n')
                data = ssl_sock.read(1024)
                ssl_sock.close()
            else:
                sock.connect((target, port))
                sock.send(method + 'HTTP/1.1\r\n')
                sock.send('Host: ' + domain + '\r\n')

                if cookie != '':
                    sock.send(cookie + '\r\n')

                if required == True:
                    sock.send(content)
                    required == False

                sock.send('\r\n')
                data = sock.recv(1024)
                sock.close()
        except Exception as error:
            continue

        try:
            rawheader = data.split(' ', 1)[1]
            head = data.split('\n', 1)[0]
            responce = head.split(' ', 1)[1]
            request = method.split(' HTTP/1.', 1)[0]

            if verbose == True:
                print((request + ': ' + responce))
            if responce.startswith('200'):
                found.append(request)
            elif responce.startswith('403'):
                auth.append(request)
            elif responce.startswith('401'):
                unauth.append(request)
        except:
            print(('Error in filtering the responce',method, ':', data))

    if len(found) > 0:
        result = True

        if 'GARBAGE / ' in found:
            print('\r\n\033[1mValid (Unreliable):\033[0;0m\r')
            found.pop(0)
        else:
            print('\r\n\033[1mValid:\033[0;0m\r')

        found.append('')
        for item in found:
            print(item)

        if len(auth) > 0:
            result = True
            if 'GARBAGE / ' in auth:
                print('\033[1mAuthentication Required (Unreliable):\033[0;0m\r')
                auth.pop(0)
            else:
                print('\033[1mAuthentication Required:\033[0;0m\r')

            auth.append('')
            for item in auth:
                print(item)

        if len(unauth) > 0:
            result = True
            print('\033[1mUnauthorized:\033[0;0m\r')
            unauth.append('')
            for item in unauth:
                print(item)

        if result == False:
            print('\033[1mNo Methods accepted!\033[0;0m\r')
            print('Try using a cookie! [-c]')

if __name__ == '__main__':
	detect()
