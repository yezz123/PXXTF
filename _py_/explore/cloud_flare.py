#!/usr/bin/env python
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End


class cloud_flare:
    def __init__(self):
        pass

    def atom(self, host):
        import urllib.request, urllib.parse, urllib.error
        from core.urli import sansor
        from socket import gethostbyname

        def check(host):
            try:
                return urllib.request.urlopen('http://' + str(host)).code
            except BaseException:
                return None

        subs = ['news.', 'download.', '', 'cpanel.', 'ftp.', 'email.',
                'server1.', 'cdn.', 'cdn2.', 'ns.', 'ns1.', 'mail.',
                'webmail.', 'direct.', 'direct-connect.', 'record.', 'ssl.',
                'dns.', 'help.', 'blog.', 'irc.', 'forum.', 'admin.',
                'server.', 'client.', 'shop.', 'panel.', 'android.', 'dld.',
                'adm.', 'map.', 'file.', 'dll.', 'login.', 'ns1.', 'ns2.',
                'ns3.', 'ns4.', 'ns5.', 'ns6.', 'ns7.', 'ns8.', 'ns9.',
                "admins.", "user.", "users.", "files.", "upload."]
        host = sansor().pransor(host)

        if sansor().cransor(host):
            ret = []

            def psend(host, sub):
                host = sub + host
                send = check(host)

                if send == 200:
                    ip = gethostbyname(host)
                    return host + ' : ' + str(ip)

            for sub in subs:
                recv = psend(host, sub)
                if recv:
                    ret.append(recv)

            if ret != []:
                return ret
            else:
                return ['none']
        else:
            return None

    def run(self):
        import sys

        W = '\x1b[37m'
        R = '\x1b[36m'
        C = '\x1b[32m'
        while True:
            host = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/cloud_flare"+G+" (set target)"+N+"): "))
            print()
            print(('target => ',host))
            print()
            if host == 'exit':
                sys.exit()
            elif host == 'back':
                break

            wread = self.atom(host)
            if wread is None:
                print("\t[-] Error Input")
                continue

            if wread[0] == 'none':
                print('\n\tnot found.')
                break
            print()
            for key in wread:
                print((C + '\t' + key))

            break
