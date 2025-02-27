#!/usr/bin/env python
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End
import os,sys

class dns_propagation:
    def __init__(self):
        pass

    def atom(self, host):
        import urllib.request, urllib.parse, urllib.error
        from bs4 import BeautifulSoup
        from core.urli import sansor

        host = sansor().pransor(host)
        if sansor().cransor(host) and sansor().cransor('viewdns.info'):

            wread = urllib.request.urlopen(
                'http://www.viewdns.info/propagation/?domain=' + host).read()
            content = BeautifulSoup(
                wread, 'html.parser').find(
                'font', face='Courier')
            content = str(content).replace('''<script class="stripe-button" data-amount="19900" data-currency="usd" data-description="Full report for 'google.com'" data-image="/images/ok.GIF" data-key="pk_live_ey9TT0KvaFQoLWRyDYg9oqQd" data-label="Download The Full Report for $199" data-name="" src="https://checkout.stripe.com/checkout.js"></script>''', '')
            return content
        else:
            return None

    def run(self):
        from core.fsave import fsave
        import sys

        while True:
            host = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dns_propagation "+G+"(set target) "+N+"): "))
            print(('\ttarget => ',host))
            print()
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            content = self.atom(host)
            if content is None:
                print("\t[-] Error Input")
                continue

            saved = fsave(host, "dns_propagation", content).pansor()
            print(('Open file save with Browser' + saved))
            print((""+G+""))
            os.system('firefox log/ ')
            break
