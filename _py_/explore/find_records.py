#!/usr/bin/env python

R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End
import os,sys
class find_records:
    def __init__(self):
        pass

    def atom(self, host):
        import urllib.request, urllib.parse, urllib.error
        from core.urli import sansor

        host = sansor().pransor(host)
        if sansor().cransor(host) and sansor().cransor(
                'api.hackertarget.com/hostsearch'):

            wread = urllib.request.urlopen(
                'https://api.hackertarget.com/hostsearch/?q=' + host).read()
            return wread
        else:
            return None

    def run(self):
        from core.fsave import fsave
        import sys

        while True:
            host = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/find_records"+N+"): "))
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            wread = self.atom(host)
            if wread is None:
                print("\t[-] Error Input ")
                continue

            saved = fsave(host, 'find_records', wread).pansor()
            print(('Open faile save with Browser ' + saved))
            print((""+G+""))
            os.system('firefox log/ ')
            break
