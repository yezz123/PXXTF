#!/usr/bin/env python

R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End
import sys,os
class extract_links:
    def __init__(self):
        pass

    def atom(self, host):
        import urllib.request, urllib.parse, urllib.error
        from core.urli import sansor
        import re

        host = sansor().pransor(host)
        if sansor().cransor(host):

            wread = urllib.request.urlopen('http://' + host).read()
            search = re.compile(host + r'/[\w\/\-.\?=%]+')
            content = search.findall(wread)
            if content == []:
                content.append('none')

            return content
        else:
            return None

    def run(self):
        from core.fsave import fsave
        import sys

        while True:
            host = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/extract_links"+N+"): "))
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            wread = self.atom(host)
            if wread is None:
                print("\t[-] Error Input")
                continue

            wread = str(wread).replace(',', '<br>')
            saved = fsave(host, 'extract_links', wread).pansor()
            print(('Open faile save with Browser ' + saved))
            print((""+G+""))
            os.system('firefox log/ ')
            break
