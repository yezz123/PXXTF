#!/usr/bin/env python
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End
import os,sys

class robots_txt:
    def __init__(self):
        pass

    def atom(self, host):
        import request
        from .urfil import sansor
        host = sansor().pransor(host)

        if sansor().cransor(host):
            payloads = [
                'robots.txt',
                'robot.xml',
                'robots.xml',
                'robot.txt',
                'robot.html']

            goods = []

            def getrequest(url):
                try:
                    getrequest = request.request(url)
                    if getrequest.status_code == 200:
                        if url not in goods:
                            goods.append(url)
                except BaseException:
                    pass

            for payload in payloads:
                getrequest(host + payload)
            if goods == []:
                goods.append('none')
            return goods
        else:
            return None

    def run(self):
        from core.fsave import fsave
        import sys

        while True:
            host = eval(input(""+N+"Pentest>> ("+B+"modules/exploits)("+R+"exploit/robots_txt"+G+"(set target)"+N+"): "))
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            wread = self.atom(host)
            if wread is None:
                continue
            if wread[0] == 'none':
                print("not found.")
                break

            wread = 'Activ url:' + str(wread).replace(',', '<br>')
            saved = fsave(host, 'robots_txt', wread).pansor()
            print(('Open faile save with Browser ' + saved))
            print((""+G+""))
            os.system('firefox log/ ')
            print()
            break
