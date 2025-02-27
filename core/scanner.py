#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, subprocess, bs4,signal, urllib.request, urllib.error, urllib.parse, json,socket
import requests
import re
import json
import sys
import urllib3
import core
import http.client
import socket
from time import sleep
import os as sistema
import readline, rlcompleter
from urllib.parse import quote
from socket import timeout
from urllib.request import urlopen
from urllib.request import Request
from sys import argv
from subprocess import *
import _py_
from core import help
from terminaltables import DoubleTable
from tabulate import tabulate
import importlib

R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End
def clean():
    os.system("clear")

def enumiax():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/enumiax "+N+"): "))
        if cs == 'show options':
            help.option()
            enumiax()
        elif cs == 'set target':
             ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/enumiax "+G+"(set target)"+G+"): "))
             print(("target>>",ip))
             wor=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/enumiax "+G+"(set wordlist)"+G+"): "))
             runn =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/enumiax "+G+"): "))
             if runn == 'run':
                 print('')
                 os.system('enumiax -d %s %s' %(wor,ip))
                 enumiax()
        elif cs =='back':
            core.menu.scan()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif cs =='clear':
            clean()
            enumiax()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            enumiax()
        pass
def load_balancing():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/load_balancing "+N+"): "))
        if cs == 'show options':
            help.option()
            load_balancing()
        elif cs == 'set target':
             ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/load_balancing "+G+"(set target)"+G+"): "))
             print(("target>>",ip))
             runn =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/load_balancing "+G+"): "))
             if runn == 'run':
                 print('')
                 os.system('lbd %s' %(ip))
                 load_balancing()
        elif cs =='back':
            core.menu.scan()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif cs =='clear':
            clean()
            load_balancing()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            load_balancing()
        pass
def port_check():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/port_check "+N+"): "))
        if cs == 'show options':
            help.option()
            port_check()
        elif cs == 'set target':
             ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/port_check "+G+"(set ip)"+G+"): "))
             print(("target>>",ip))
             runn =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/port_check "+G+"): "))
             if runn == 'run':
                 print((""+G+""))
                 os.system('nc -vnzw1 %s 1-6000' % (ip))
                 port_check()
        elif cs =='back':
            core.menu.scan()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif cs =='clear':
            clean()
            port_check()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            port_check()
        pass

def botnet_scanning():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/botnet_scanning "+N+"): "))
        if cs == 'show options':
            help.option()
            botnet_scanning()
        elif cs == 'set target':
             ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/botnet_scanning "+G+"(set IP Zombie)"+G+"): "))
             print(("Zombie",ip))
             tar=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/botnet_scanning "+G+"(set target)"+G+"): "))
             print(("target",tar))
             runn =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/botnet_scanning "+G+"): "))
             if runn == 'run':
                 print('')
                 os.system('nmap -sI %s  %s' %(ip,tar))
                 botnet_scanning()
        elif cs =='back':
            core.menu.scan()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif cs =='clear':
            clean()
            botnet_scanning()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            botnet_scanning()
        pass
def ssl_check():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/check_ssl_certificate "+N+"): "))
        if cs == 'show options':
            help.option()
            sslscan()
        elif cs == 'set target':
             ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/check_ssl_certificate "+G+"(set target)"+G+"): "))
             runn =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/check_ssl_certificate "+G+"): "))
             if runn == 'run':
                 print('')
                 os.system('sslscan --show-certificate %s' %(ip))
                 sslscan()
        elif cs =='back':
            core.menu.scan()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif cs =='clear':
            clean()
            sslscan()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            sslscan()
        pass
def ssl_cert():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/ssl_cert "+N+"): "))
        if cs == 'show options':
            help.option()
            ssl_cert()
        elif cs == 'set target':
             ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/ssl_cert "+G+"(set target)"+G+"): "))
             runn =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/ssl_cert "+G+"): "))
             if runn == 'run':
                 scan = os.popen("nmap -sV --script ssl-cert "+ ip + "" ).read()
                 save = open('log/ssl_log.txt','w')
                 save.write(scan)
                 save.close()
                 vuln = os.popen("cat log/ssl_log.txt " ).read()
                 table= [['scan result'],[vuln]]
                 print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
                 ssl_cert()
        elif cs =='back':
            core.menu.scan()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif cs =='clear':
            clean()
            ssl_cert()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            ssl_cert()
        pass
def sslscan():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/sslscan "+N+"): "))
        if cs == 'show options':
            help.option()
            sslscan()
        elif cs == 'set target':
             ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/sslscan "+G+"(set target)"+G+"): "))
             runn =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/sslscan "+G+"): "))
             if runn == 'run':
                 print('')
                 os.system('sslscan %s' %(ip))
                 sslscan()
        elif cs =='back':
            core.menu.scan()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif cs =='clear':
            clean()
            sslscan()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            sslscan()
        pass
def zone_walking():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/zone_walking "+N+"): "))
        if cs == 'show options':
            help.option()
            zone_walking()
        elif cs == 'set target':
             ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/zone_walking "+G+"(set target)"+G+"): "))
             runn =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/zone_walking "+G+"): "))
             if runn == 'run':
                 print('')
                 os.system('dnsrecon -d %s -t zonewalk' %(ip))
                 zone_walking()
        elif cs =='back':
            core.menu.scan()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif cs =='clear':
            clean()
            zone_walking()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            zone_walking()
        pass
def dns_bruteforce():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dns_bruteforce "+N+"): "))
        if cs == 'show options':
            help.option()
            dns_bruteforce()
        elif cs == 'set target':
             ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dns_bruteforce "+G+"(set target)"+G+"): "))
             wor=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dns_bruteforce "+G+"(set wordlist)"+G+"): "))
             runn =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dns_bruteforce "+G+"): "))
             if runn == 'run':
                 print('')
                 os.system('dnsrecon -d %s -D %s -t brt' %(ip,wor))
                 dns_bruteforce()
        elif cs =='back':
            core.menu.scan()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif cs =='clear':
            clean()
            dns_bruteforce()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            dns_bruteforce()
        pass
def dns_zone_transfer():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dns_zone_transfer "+N+"): "))
        if cs == 'show options':
            help.option()
            dns_zone_transfer()
        elif cs == 'set target':
             ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dns_zone_transfer "+G+"(set target)"+G+"): "))
             runn =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dns_zone_transfer "+G+"): "))
             if runn == 'run':
                 print('')
                 os.system('dnsrecon -d %s -a' %(ip))
                 os.system('dnsrecon -d %s -t axfr' % (ip))
                 dns_zone_transfer()
        elif cs =='back':
            core.menu.scan()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif cs =='clear':
            clean()
            dns_zone_transfer()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            dns_zone_transfer()
        pass

def dnsrecon():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dnsrecon "+N+"): "))
        if cs == 'show options':
            help.option()
            dnsrecon()
        elif cs == 'set target':
             ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dnsrecon "+G+"(set target)"+G+"): "))
             runn =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dnsrecon "+G+"): "))
             if runn == 'run':
                 print('')
                 os.system('dnsrecon -d %s' %(ip))
                 dnsrecon()
        elif cs =='back':
            core.menu.scan()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif cs =='clear':
            clean()
            dnsrecon()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            dnsrecon()
        pass

def dns_reverse():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/reverse_dns "+N+"): "))
        if cs == 'show options':
            help.option()
            dns_reverse()
        elif cs == 'set target':
             ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/reverse_dns "+G+"(set target)"+G+"): "))
             scan = os.popen("dig -x "+ ip + "" ).read()
             save = open('log/log.txt','w')
             save.write(scan)
             save.close()
             vuln = os.popen("cat log/log.txt " ).read()
             table= [['scan result'],[vuln]]
             print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
             dns_reverse()
        elif cs =='back':
            core.menu.scan()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif cs =='clear':
            clean()
            dns_reverse()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            dns_reverse()
        pass

def iploc():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/ip_locator "+N+"): "))
        if cs == 'show options':
            help.option()
            iploc()
        elif cs == 'set target':
            ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/ip_locator "+G+"(set domain)"+N+"): "))
            url = "http://ip-api.com/json/"
            reponse = urllib.request.urlopen(url + ip)
            name = reponse.read()
            labs = json.loads(name)
            print(("\033[92m" + "\n IP: " + labs['query']))
            print(("\033[92m" + " Status: " + labs['status']))
            print(("\033[92m" + " Region: " + labs['regionName']))
            print(("\033[92m" + " Country: " + labs['country']))
            print(("\033[92m" + " City: " + labs['city']))
            print(("\033[92m" + " ISP: " + labs['isp']))
            print(("\033[92m" + " Lat,Lon: " + str(labs['lat']) + "," + str(labs['lon'])))
            print(("\033[92m" + " ZIPCODE: " + labs['zip']))
            print(("\033[92m" + " TimeZone: " + labs['timezone']))
            print(("\033[92m" + " AS: " + labs['as'] + "\n"))
            iploc()
        elif cs =='back':
            core.menu.scan()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif cs =='clear':
            clean()
            iploc()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            iploc()
        pass

def who():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/whois "+N+"): "))
        if cs == 'show options':
            help.option()
            who()
        elif cs == 'set target':
             ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/whois "+G+"(set ip)"+G+"): "))
             scan = os.popen("whois "+ ip + "" ).read()
             save = open('log/log.txt','w')
             save.write(scan)
             save.close()
             vuln = os.popen("cat log/log.txt " ).read()
             table= [['scan result'],[vuln]]
             print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
             who()
        elif cs =='back':
            core.menu.scan()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif cs =='clear':
            clean()
            who()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            who()
        pass

def xss():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/xss_scaner "+N+"): "))
        if cs == 'show options':
            help.option()
            xss()
        elif cs == 'set target':
            tops = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/xss_scaner (set target)"+N+"): "))
            print(("target =>"+R+"" ,tops))
            gay = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/xss_scaner"+N+"): "))
            if gay == "run":
                print((""+B+"[*]"+N+" Starting attacks Scanning..."))
                os.system("cd modules;cd xsspy;python XssPy.py -u %s -v" % (tops))
                print((""+B+"[*]"+N+" Job finished!"))
                print()
                xss()
            else:
                xss()
        elif cs =='back':
            core.menu.scan()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif cs =='clear':
            clean()
            xss()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            xss()
        pass
def http_services():
    cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/http_services "+N+"): "))
    if cs == 'show options':
        help.option()
        http_services()
    elif cs == 'set target':
         ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/http_services "+G+"(set target)"+G+"): "))
         print((""+B+""))
         os.system('figlet Start Scan')
         print("Wait...")
         scan = os.popen("nmap -p- --script=http-title "+ ip + "" ).read()
         save = open('log/log.txt','w')
         save.write(scan)
         save.close()
         vuln = os.popen("cat log/log.txt " ).read()
         table= [['scan result'],[vuln]]
         print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
         http_services()
    elif cs =='back':
        core.menu.scan()
    elif cs =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    elif cs =='clear':
        clean()
        http_services()
    else:
        print(("Wrong Command => ", cs))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        http_services()
def grabbing_detection():
    cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/grabbing_detection "+N+"): "))
    if cs == 'show options':
        help.option()
        grabbing_detection()
    elif cs == 'set target':
         ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/grabbing_detection "+G+"(set target)"+G+"): "))
         print((""+B+""))
         os.system('figlet Start Scan')
         print("Wait...")
         scan = os.popen("nmap -sV --version-intensity 5 "+ ip + "" ).read()
         save = open('log/log.txt','w')
         save.write(scan)
         save.close()
         vuln = os.popen("cat log/log.txt " ).read()
         table= [['scan result'],[vuln]]
         print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
         grabbing_detection()
    elif cs =='back':
        core.menu.scan()
    elif cs =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    elif cs =='clear':
        clean()
        grabbing_detection()
    else:
        print(("Wrong Command => ", cs))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        grabbing_detection()
def discovery():
    cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/discovery "+N+"): "))
    if cs == 'show options':
        help.option()
        discovery()
    elif cs == 'set target':
         ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/discovery "+G+"(set target)"+G+"): "))
         print((""+B+""))
         os.system('figlet Start Scan')
         print("Wait...")
         scan = os.popen("nmap -Pn -F "+ ip + "" ).read()
         save = open('log/log.txt','w')
         save.write(scan)
         save.close()
         vuln = os.popen("cat log/log.txt " ).read()
         table= [['scan result'],[vuln]]
         print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
         discovery()
    elif cs =='back':
        core.menu.scan()
    elif cs =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    elif cs =='clear':
        clean()
        discovery()
    else:
        print(("Wrong Command => ", cs))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        discovery()

def ddos_reflectors():
    cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/ddos_reflectors "+N+"): "))
    if cs == 'show options':
        help.option()
        ddos_reflectors()
    elif cs == 'set target':
         ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/ddos_reflectors "+G+"(set target)"+G+"): "))
         print((""+B+""))
         os.system('figlet Start Scan')
         print("Wait...")
         scan = os.popen("nmap -sU -A -PN -n -pU:19,53,123,161 --script=ntp-monlist,dns-recursion,snmp-sysdescr "+ ip + "" ).read()
         save = open('log/log.txt','w')
         save.write(scan)
         save.close()
         vuln = os.popen("cat log/log.txt " ).read()
         table= [['scan result'],[vuln]]
         print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
         ddos_reflectors()
    elif cs =='back':
        core.menu.scan()
    elif cs =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    elif cs =='clear':
        clean()
        ddos_reflectors()
    else:
        print(("Wrong Command => ", cs))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        ddos_reflectors()

def http_enum():
    cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/http_enum "+N+"): "))
    if cs == 'show options':
        help.option()
        http_enum()
    elif cs == 'set target':
         ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/http_enum "+G+"(set target)"+G+"): "))
         print((""+B+""))
         os.system('figlet Start Scan')
         print("Wait...")
         scan = os.popen("nmap -p- --script=http-enum "+ ip + "" ).read()
         save = open('log/log.txt','w')
         save.write(scan)
         save.close()
         vuln = os.popen("cat log/log.txt " ).read()
         table= [['scan result'],[vuln]]
         print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
         http_enum()
    elif cs =='back':
        core.menu.scan()
    elif cs =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    elif cs =='clear':
        clean()
        http_enum()
    else:
        print(("Wrong Command => ", cs))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        http_enum()
def dmitry():
    cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dmitry "+N+"): "))
    if cs == 'show options':
        help.option()
        dmitry()
    elif cs == 'set target':
         ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dmitry "+G+"(set target)"+G+"): "))
         print((""+B+""))
         os.system('figlet Start Scan')
         print("Wait...")
         scan = os.popen("dmitry "+ ip + "" ).read()
         save = open('log/log.txt','w')
         save.write(scan)
         save.close()
         vuln = os.popen("cat log/log.txt " ).read()
         table= [['scan result'],[vuln]]
         print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
         dmitry()
    elif cs =='back':
        core.menu.scan()
    elif cs =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    elif cs =='clear':
        clean()
        dmitry()
    else:
        print(("Wrong Command => ", cs))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        dmitry()

def web_services():
    cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/web_services "+N+"): "))
    if cs == 'show options':
        help.option()
        web_services()
    elif cs == 'set target':
         ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/web_services "+G+"(set target)"+G+"): "))
         print((""+B+""))
         os.system('figlet Start Scan')
         print("Wait...")
         scan = os.popen("nmap -p- --script=http-headers "+ ip + "" ).read()
         save = open('log/log.txt','w')
         save.write(scan)
         save.close()
         vuln = os.popen("cat log/log.txt " ).read()
         table= [['scan result'],[vuln]]
         print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
         web_services()
    elif cs =='back':
        core.menu.scan()
    elif cs =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    elif cs =='clear':
        clean()
        web_services()
    else:
        print(("Wrong Command => ", cs))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        web_services()

def dbrute():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dns_bruteforce "+N+"): "))
        if cs == 'show options':
            help.option()
            dbrute()
        elif cs == 'set target':
             ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dns_bruteforce "+G+"(set target)"+G+"): "))
             scan = os.popen("nmap -p- --script dns-brute.nse "+ ip + "" ).read()
             save = open('log/log.txt','w')
             save.write(scan)
             save.close()
             vuln = os.popen("cat log/log.txt " ).read()
             table= [['scan result'],[vuln]]
             print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
             dbrute()
        elif cs =='back':
            core.menu.scan()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif cs =='clear':
            clean()
            dbrute()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            dbrute()
        pass
def webdav():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/webdav_scan "+N+"): "))
        if cs == 'show options':
            help.option()
            webdav()
        elif cs == 'set target':
             ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/webdav_scan "+G+"(set target)"+G+"): "))
             print((""+B+"Start Scanning",ip))
             scan = os.popen("nmap -p- -sV --script http-webdav-scan.nse "+ ip + "" ).read()
             save = open('log/log.txt','w')
             save.write(scan)
             save.close()
             vuln = os.popen("cat log/log.txt " ).read()
             table= [['scan result'],[vuln]]
             print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
             webdav()
        elif cs =='back':
            core.menu.scan()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif cs =='clear':
            clean()
            webdav()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            webdav()
        pass
def heartbleed():
    cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/heartbleed "+N+"): "))
    if cs == 'show options':
        help.option()
        heartbleed()
    elif cs == 'set target':
         ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/heartbleed "+G+"(set target)"+G+"): "))
         scan = os.popen("nmap -sV -p 443 --script=ssl-heartbleed "+ ip + "" ).read()
         save = open('log/log.txt','w')
         save.write(scan)
         save.close()
         vuln = os.popen("cat log/log.txt " ).read()
         table= [['scan result'],[vuln]]
         print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
         heartbleed()
    elif cs =='back':
        core.menu.scan()
    elif cs =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    elif cs =='clear':
        clean()
        heartbleed()
    else:
        print(("Wrong Command => ", cs))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        heartbleed()
    pass
def https_discover():
    cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/https_discover "+N+"): "))
    if cs == 'show options':
        help.option()
        https_discover()
    elif cs == 'set target':
         ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/https_discover "+G+"(set target)"+G+"): "))
         scan = os.popen("nmap -sV -p 443 --script=ip-https-discover "+ ip + "" ).read()
         save = open('log/log.txt','w')
         save.write(scan)
         save.close()
         vuln = os.popen("cat log/log.txt " ).read()
         table= [['scan result'],[vuln]]
         print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
         https_discover()
    elif cs =='back':
        core.menu.scan()
    elif cs =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    elif cs =='clear':
        clean()
        https_discover()
    else:
        print(("Wrong Command => ", cs))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        https_discover()
    pass
def golismero():
    cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/golismero "+N+"): "))
    if cs == 'show options':
        help.option()
        golismero()
    elif cs == 'set target':
         ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/golismero "+G+"(set target)"+G+"): "))
         os.system("golismero scan %s -o log/golismero_scan.txt" % (ip))
         golismero()
    elif cs =='back':
        core.menu.scan()
    elif cs =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    elif cs =='clear':
        clean()
        golismero()
    else:
        print(("Wrong Command => ", cs))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        golismero()
    pass
def mysql():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/mysql_empty_password "+N+"): "))
        if cs == 'show options':
            help.option()
            mysql()
        elif cs == 'set target':
             ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/mysql_empty_password "+G+"(set target)"+G+"): "))
             scan = os.popen("nmap -p- -sV --script mysql-empty-password.nse"+ target + " -Pn" ).read()
             save = open('log/log.txt','w')
             save.write(scan)
             save.close()
             vuln = os.popen("cat log/log.txt " ).read()
             table= [['scan result'],[vuln]]
             print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
             mysql()
        elif cs =='back':
            core.menu.scan()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif cs =='clear':
            clean()
            mysql()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            mysql()
        pass
def wordpress():
    while True:
        wor = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/usr_pro_wordpress_auto_find"+N+"): "))
        if wor == 'show options':
            print("Name                  Description")
            print("=====                =============")
            print("set target           start target")
            print("back                 back to menu")
            wordpress()
        elif wor == 'back':
            core.menu.scan()
        elif wor == 'set target':
             def tracker(keywords, start):
                     searchQuery = quote(keywords, safe='')
                     try:
                         url = "https://www.google.com/search?gl=ir&num=100&start=" + str(
                             start) + "&pws=0&as_qdr=all&dcr=0&q=" + searchQuery
                         req = Request(url)
                     except timeout:
                         print("Connection timed out!")
                     req.add_header('User-Agent',
                                    'userpro1 aef by orm')
                     serpURL = urlopen(req).read()
                     soup = bs4.BeautifulSoup(serpURL, "html.parser")
                     allResults = []
                     i=0
                     for hit in soup.findAll('cite'):
                         allResults.append(
                               str("")+hit.text)
                         i=i+1
                     if (len(allResults) == 0):
                         return(""+R+"[!] "+N+"No result found for this keyword => " + keywords)
                     else:
                         print((""+B+"[*]"+N+" Ok! Starting... \n"))

                         for element in allResults:
                             if (element.startswith("http://")):
                                 element = element[7:]
                             if (element.startswith("https://")):
                                  element = element[8:]
                             if (element.startswith("www.")):
                                 element = element[4:]
                             element=element[:element.find("/")]
                             element="http://"+element
                             print(("checking "+element+" :"))
                             if (checkwp(element)):
                                 suc = str(checkVul(element))
                                 if( suc=="True"):
                                     try:
                                         filee = open("priv8.txt", mode="a+")
                                         filee.write(element+"\n")
                                         filee.close()
                                     except:
                                         print((""+R+"error"+N+""))
                                     print (suc)
                                 else:
                                     print((""+R+"False"+N+""))

                             else:
                                print((element + ""+R+" =>"+N+" " + str(checkwp(element))))


             def checkwp(url):
                 url+="/wp-content/plugins/userpro/css/userpro.min.css"
                 try:
                  pURL = urlopen(url).read()
                 except:
                     return False
                 if (pURL.find(".userpro")>-1):
                     print((""+B+"[!] "+N+" Plugin is installed checking vulnerable...\n"))
                     return True
                 else:
                     return False
             def checkVul(url):
                 url1=url + "/?up_auto_log=true"
                 try:
                     pURL = urlopen(url1).read()
                     if (pURL.find("admin-bar-css")>-1):
                        return True
                     elif (urlopen(url + "/wp-admin").read().find("admin-bar-css")>-1):
                         return True
                     else :return False
                 except:
                     return False
             while(True):
                 x = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/usr_pro_wordpress_auto_find (set Dork)"+N+"): "))
                 print(("DORKS => "+R+"",x))
                 n= eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/usr_pro_wordpress_auto_find (start number)"+N+"): "))
                 print(("START NUMBER => "+R+"",n))
                 g= eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/usr_pro_wordpress_auto_find (set end_number)"+N+"): "))
                 print(("END NUMBER => "+R+"",g))
                 run = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/usr_pro_wordpress_auto_find"+N+"): "))
                 if run == "run":
                    print((""+B+"[*] "+N+"Starting attacks..."))
                 while(True):
                     tracker(x, n)
                     y=eval(input(""+B+"[*]"+N+" Next (y/n)?"))
                     if(y=="y"):
                         n+=g;
                         tracker(x, n)
                     else:
                         core.menu.scan()
                 y1=eval(input(""+B+"[*]"+N+" Anouther dork (y/n) ?"))
                 if (y1 == "y"):
                     continue
                 else:
                     core.menu.scan()
        elif wor == 'clear':
            clean()
            wordpress()
        elif wor =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        else:
            print(("Wrong Command => ", wor))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            wordpress()
        pass

def cms():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/cms_war "+N+"): "))
        if cs == 'show options':
            help.option()
            cms()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif cs == 'set target':
            tops = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/cms_war (set target)"+N+"): "))
            print(("target =>"+R+"" ,tops))
            print((""+N+"=> "+R+"scan "+N+"[dir, shell, backup, files, admin]"))
            ray = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/cms_war (scan)"+N+"): "))
            gay = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/cms_war"+N+"): "))
            if gay == "run":
                print((""+B+"[*]"+N+" Starting attacks..."))
                os.system("cd modules;cd scanner;python scanner.py %s -m %s" % (tops,ray))
                print((""+B+"[*]"+N+" Job finished!"))
                print()
                cms()
            else:
                cms()
        elif cs =='back':
            core.menu.scan()
        elif cs =='clear':
            clean()
            cms()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            cms()
        pass
def drupal_scan():
    cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/drupal_scan "+N+"): "))
    if cs == 'show options':
        help.option()
        drupal_scan()
    elif cs == 'set target':
         ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/drupal_scan "+G+"(set target)"+G+"): "))
         print(('Start scan target %s',ip))
         os.system("droopescan scan drupal -u %s" % (ip))
         drupal_scan()
    elif cs =='back':
        core.menu.scan()
    elif cs =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    elif cs =='clear':
        clean()
        drupal_scan()
    else:
        print(("Wrong Command => ", cs))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        drupal_scan()
    pass
def wordpress1():
    cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/wordpress_scan "+N+"): "))
    if cs == 'show options':
        help.option()
        wordpress1()
    elif cs == 'set target':
         ip=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/wordpress_scan "+G+"(set target)"+G+"): "))
         os.system("droopescan scan wordpress -u %s" % (ip))
         wordpress1()
    elif cs =='back':
        core.menu.scan()
    elif cs =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    elif cs =='clear':
        clean()
        wordpress1()
    else:
        print(("Wrong Command => ", cs))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        wordpress1()
    pass
def wordpress_scan():
    while True:
        sec = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/wordpress_user_scanners"+N+"): "))
        if sec == 'show options':
            help.option()
            wordpress_scan()
        elif sec =='back':
            core.menu.scan()
        elif sec =='set target':
            wop = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/wordpress_user_scanners (target)"+N+"): "))
            enum = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/wordpress_user_scanners (user)"+N+"): "))
            uiop = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/wordpress_user_scanners"+N+"): "))
            if uiop == "run":
                print((""+B+"[*]"+N+" Starting attacks..."))
                os.system("cd modules;cd wscan;python wpscanner.py -s %s -n %s" % (wop,enum))
                print((""+B+"[*]"+N+" Job finished!"))
                print()
                wordpress_scan()
            else:
                wordpress_scan()
        elif sec == 'clear':
            clean()
            wordpress_scan()
        elif sec =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        else:
            print(("Wrong Command => ", sec))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            wordpress_scan()
        pass

def dirse():
    while True:
        dir = eval(input("Pentest>> ("+B+"modules/scanners)("+R+"scanner/dir_search"+N+"): "))
        if dir == 'show options':
           help.option()
           dirse()
        elif dir =='back':
            core.menu.scan()
        elif dir =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif dir == 'set target':
            ym = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dir_search (set target)"+N+"): "))
            print(("target => "+R+"",ym))
            puki = eval(input("Pentest>> ("+B+"modules/scanners)("+R+"scanner/dir_search (set extensions)"+N+"): "))
            dih = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dir_search"+N+"): "))
            if dih == "run":
                os.system("python3 modules/dirsearch/dirsearch.py -u %s -e %s" % (ym,puki))
                print((""+B+"[*]"+N+" Job finished!"))
                print()
                dirse()
            else:
                dirse()
        elif dir =='clear':
            clean()
            dirse()
        else:
            print(("Wrong Command => ", dir))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            dirse()
        pass

def lfi():
    while True:
        lf = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/lfi_scanner"+N+"): "))
        if lf == 'show options':
           help.option()
           lfi()
        elif lf =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif lf == 'back':
             core.menu.scan()
        elif lf == 'set target':
            os.system("cd modules;cd lfi_scanners;perl lfi_scanner.pl")
            print((""+B+"[*]"+N+" Job finished!"))
            print()
            lfi()
        elif lf == 'clear':
            clean()
            lfi()
        else:
            print(("Wrong Command => ", lf))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            lfi()

        pass
def port():
    while True:
        os.system("python modules/port_scanners/port.py")
        print((""+B+"[*]"+N+" Job finished!"))
        print()
        core.menu.scan()
        pass

def joomla_sql():
    while True:
        jo = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/joomla_sqli_scanners"+N+"): "))
        if jo == 'show options':
            help.option()
            joomla_sql()
        elif jo == 'back':
            core.menu.scan()
        elif jo == 'set target':
            q = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/joomla_sqli_scanners (set target)"+N+"): "))
            print(("list web => "+R+"",q))
            m = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/joomla_sqli_scanners"+N+"): "))
            if m == "run":
                print((""+B+"[*] "+N+"Starting attacks..."))
                os.system("cd modules;cd joomla_sqli_scanners;python joomsql.py %s" % (q))
                print()
                joomla_sql()
            else:
                joomla_sql()
        elif jo == 'clear':
            clean()
            joomla_sql()
        elif jo =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        else:
            print(("Wrong Command => ", jo))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            joomla_sql()
        pass

def joomscan():
    while True:
        jaa = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/jomscan_v4"+N+"): "))
        if jaa == 'show options':
            help.option()
            joomscan()
        elif jaa =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif jaa == 'back':
            core.menu.scan()
        elif jaa == 'set target':
            ops = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/jomscan_v4 (target)"+N+"): "))
            print(("target => "+R+"",ops))
            rup = eval(input(""+N+"(Pentest)> ("+B+"modules/scanners)("+R+"scanner/jomscan_v4"+N+"): "))
            if rup == "run":
                print((""+B+"[*]"+N+" Starting Attacks..."))
                os.system("cd modules;cd joomscan_v4;python scan.py %s" % (ops))
                print((""+B+"[*]"+N+" Job finished!"))
                print()
                joomscan()
            else:
                joomscan()
        elif jaa =='clear':
            clean()
            joomscan()
        else:
            print(("Wrong Command => ", jaa))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            joomscan()
        pass

def scan_v3():
    while True:
        try:
            se =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"joomla_scanners_v3"+N+"): "))
            if se == 'show options':
                help.option()
                scan_v3()
            elif se =='exit':
                 print()
                 print((""+G+"Thanks for using PTF"))
                 print()
                 exit()
            elif se == 'back':
                core.menu.scan()
            elif se == 'set target':
                x = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/joomla_scanners_v3"+G+" (set target)"+N+"): "))
                print(("target => "+R+"",x))
                i = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"joomla_scanners_v3"+N+"): "))
                if i == "run":
                        print((""+B+"[*]"+N+" Starting attacks..."))
                        os.system("cd modules;cd joomscan_v3;python joomlascanner.py %s" % (x))
                        print((""+B+"[*]"+N+" Job finished!"))
                        print()
                        scan_v3()
                else:
                        scan_v3()
            elif se =='clear':
                clean()
                scan_v3()
            else:
                print(("Wrong Command => ", se))
                print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
                scan_v3()
            pass
        except(KeyboardInterrupt):
            scan_v3()
def scan_v2():
    while True:
        try:
            v2 =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/joomla_scanners_v.2"+N+"): "))
            if v2 == 'show options':
                help.option()
                scan_v2()
            elif v2 =='exit':
                 print()
                 print((""+G+"Thanks for using PTF"))
                 print()
                 exit()
            elif v2 == 'back':
                core.menu.scan()
            elif v2 == 'set target':
                p = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/joomla_scanners_v.2 (set target)"+N+"): "))
                print(("target => "+R+"",p))
                o = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/joomla_scanners_v.2"+N+"): "))
                if o == "run":
                        os.system("cd modules;cd joomscan_v2;python joomlascan2.py %s" % (p))
                        print((""+B+"[*]"+N+" Job finished!"))
                        print()
                        scan_v2()
                else:
                        scan_v2()
            elif v2 =='clear':
                clean()
                scan_v2()
            else:
                print(("Wrong Command => ", v2))
                print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
                scan_v2()
            pass
        except(KeyboardInterrupt):
            scan_v2()
def jomvull():
    while True:
        try:
            j = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/joomla_vulnerability_scanners"+N+"): "))
            if j == 'show options':
                help.option()
                jomvull()
            elif j =='exit':
                 print()
                 print((""+G+"Thanks for using PTF"))
                 print()
                 exit()
            elif j == 'back':
                core.menu.scan()
            elif j == 'set target':
                os.system("cd modules;cd joomscan;perl joomlavulnerability.pl")
                print((""+B+"[*]"+N+" Job finished!"))
                print()
                jomvull()
            elif j =='clear':
                clean()
                jomvull()
            else:
                print(("Wrong Command => ", j))
                print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
                jomvull()
            pass
        except(KeyboardInterrupt):
            jomvull()
def jdown():
    while True:
        a = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/jdownloads_scanners"+N+"): "))
        if a == 'show options':
            help.option()
            jdown()
        elif a =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif a == 'back':
            core.menu.scan()
        elif a == 'set target':
            li = eval(input(""+N+"(list)> ("+B+"modules/scanners)("+R+"scanner/jdownloads_scanners (set target)"+N+"): "))
            print(("list => "+R+"",li))
            ruu = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/jdownloads_scanners"+N+"): "))
            if ruu == "run":
                print((""+B+"[*]"+N+" Starting attacks..."))
                os.system("cd modules;cd jdownloads_scanner;perl jdownloads_scanner.pl %s" % (li))
                print((""+B+"[*]"+N+" Job finished!"))
                print()
                jdown()
            else:
                jdown()
        elif a == 'clear':
            clean()
            jdown()
        else:
            print(("Wrong Command => ", a))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            jdown()
        pass

def smb():
    while True:
        map =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/smb_scanning"+N+"): "))
        if map == 'show options':
            help.option()
            smb()
        elif map =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif map == 'back':
            core.menu.scan()
        elif map =='set target':
            target = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/smb_scanning ("+G+"set target)"+N+"): "))
            print(("Target => "+R+"",target))
            ta = eval(input("Pentest>> ("+B+"modules/scanners)("+R+"scanner/smb_scanning"+N+"): "))
            if ta  == "run":
              scan = os.popen("nmap -p- --script=modules/nse/smb.nse"+ target + " -Pn" ).read()
              save = open('log/nmap_vuln.txt','w')
              save.write(scan)
              save.close()
              vuln = os.popen("cat log/nmap_vuln.txt " ).read()
              table= [['vulnerable scan result'],[vuln]]
              print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
              smb()
            else:
                smb()
        elif map =='clear':
            clean()
            smb()
        else:
            print(("Wrong Command => ", map))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            smb()
        pass

def nmap_sc():
    while True:
        nnn = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/nmap_scanner"+N+"): "))
        if nnn == 'show options':
            help.option()
            nmap_sc()
        elif map =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif nnn == 'back':
            core.menu.scan()
        elif nnn =='set target':
             target = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/nmap_scanner (set ip)"+N+"): "))
             print(("Target => "+R+"",target))
             ta = eval(input("Pentest)> ("+B+"modules/scanners)("+R+"scanner/nmap_scanner"+N+"): "))
             if ta  == "run":
                print(("\033[1;34m\n[++] Please wait ... Scanning ports on " + target + " \033[1;m"))
                scan = os.popen("nmap "+ target + " -Pn" ).read()
                save = open('log/nmap.txt','w')
                save.write(scan)
                save.close()
                ports = os.popen("grep open log/nmap.txt | awk '{print $1}'" ).read()
                ports_services = os.popen("grep open log/nmap.txt | awk '{print $3}'" ).read()
                ports_state = os.popen("grep open log/nmap.txt | awk '{print $2}'" ).read()
                check_open_port = os.popen("grep SERVICE log/nmap.txt | awk '{print $2}'" ).read()
                if check_open_port == "STATE\n":
                    table_data = [['Target','SERVICE', 'PORT', 'STATE'],[target,ports_services, ports, ports_state,]]
                    table = DoubleTable(table_data)
                    print(("\033[1;36m\n[+]----------[ Port scan result for " + target +" ]----------[+]\n\033[1;m"))
                    print((table.table))
                    nmap_sc()
                else:
                    nmap_sc()
             else:
                 nmap_sc()
        elif nnn =='clear':
            clean()
            nmap_sc()
        else:
            print(("Wrong Command => ", nnn))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            nmap_sc()
        pass

def nmap_vul():
    while True:
        map =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/nmap_vuln"+N+"): "))
        if map == 'show options':
            help.option()
            nmap_vul()
        elif map =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif map == 'back':
            core.menu.scan()
        elif map =='set target':
            target = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/nmap_vuln (set IP)"+N+"): "))
            print(("Target => "+R+"",target))
            ta = eval(input("Pentest>> ("+B+"modules/scanners)("+R+"scanner/nmap_vuln"+N+"): "))
            if ta  == "run":
              print(("\033[1;34m\n[++] Please wait ... Scanning ports on " + target + " \033[1;m"))
              scan = os.popen("nmap -sV --script vuln "+ target + " -Pn" ).read()
              save = open('log/nmap_vuln.txt','w')
              save.write(scan)
              save.close()
              vuln = os.popen("cat log/nmap_vuln.txt " ).read()
              table= [['vulnerable scan result'],[vuln]]
              print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
              nmap_vul()
            else:
                nmap_vul()
        elif map =='clear':
            clean()
            nmap_vul()
        else:
            print(("Wrong Command => ", map))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            nmap_vul()
        pass
def header():
    map =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/header"+N+"): "))
    if map == 'show options':
        help.option()
        header()
    elif map =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    elif map == 'back':
        core.menu.scan()
    elif map =='set target':
        target = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/header (set IP)"+N+"): "))
        print(("Target => "+R+"",target))
        ta = eval(input("Pentest>> ("+B+"modules/scanners)("+R+"scanner/header"+N+"): "))
        if ta  == "run":
          print(("\033[1;34m\n[++] Please wait ... Scanning ports on " + target + " \033[1;m"))
          scan = os.popen("nmap -sV --script http-headers.nse "+ target + " -Pn" ).read()
          save = open('log/nmap_vuln.txt','w')
          save.write(scan)
          save.close()
          vuln = os.popen("cat log/nmap_vuln.txt " ).read()
          table= [['vulnerable scan result'],[vuln]]
          print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
          header()
        else:
            nmap_vul()
    elif map =='clear':
        clean()
        header()
    else:
        print(("Wrong Command => ", map))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        header()
def firewalk():
    map =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/firewalk"+N+"): "))
    if map == 'show options':
        help.option()
        firewalk()
    elif map =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    elif map == 'back':
        core.menu.scan()
    elif map =='set target':
        target = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/firewalk (set IP)"+N+"): "))
        print(("Target => "+R+"",target))
        ta = eval(input("Pentest>> ("+B+"modules/scanners)("+R+"scanner/firewalk"+N+"): "))
        if ta  == "run":
          print(("\033[1;34m\n[++] Please wait ... Scanning ports on " + target + " \033[1;m"))
          scan = os.popen("nmap -sV --script firewalk.nse "+ target + " -Pn" ).read()
          save = open('log/nmap_vuln.txt','w')
          save.write(scan)
          save.close()
          vuln = os.popen("cat log/nmap_vuln.txt " ).read()
          table= [['vulnerable scan result'],[vuln]]
          print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
          firewalk()
        else:
            nmap_vul()
    elif map =='clear':
        clean()
        firewalk()
    else:
        print(("Wrong Command => ", map))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        header()
def spaghetti():
    while True:
        map =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/spaghetti"+N+"): "))
        if map == 'show options':
            help.option()
            spaghetti()
        elif map =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif map == 'back':
            core.menu.scan()
        elif map =='set target':
            target = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/spaghetti ("+G+"set target)"+N+"): "))
            print(("Target => "+R+"",target))
            ta = eval(input("Pentest>> ("+B+"modules/scanners)("+R+"scanner/spaghetti"+N+"): "))
            if ta  == "run":
              scan = os.popen("python modules/spaghetti/spaghetti.py --url "+ target + " --scan [0-3] " ).read()
              save = open('log/scan.txt','w')
              save.write(scan)
              save.close()
              vuln = os.popen("cat log/scan.txt " ).read()
              table= [['scan result'],[vuln]]
              print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
              spaghetti()
            else:
                spaghetti()
        elif map =='clear':
            clean()
            spaghetti()
        else:
            print(("Wrong Command => ", map))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            spaghetti()
        pass

def ssl():
    while True:
        map =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/ssl_scanning"+N+"): "))
        if map == 'show options':
            help.option()
            ssl()
        elif map =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif map == 'back':
            core.menu.scan()
        elif map =='set target':
            target = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/ssl_scanning ("+G+"set target)"+N+"): "))
            print(("Target => "+R+"",target))
            ta = eval(input("Pentest>> ("+B+"modules/scanners)("+R+"scanner/ssl_scanning"+N+"): "))
            if ta  == "run":
              os.system("python modules/a2sv/a2sv.py -t %s" % (target))
              ssl()
            else:
                ssl()
        elif map =='clear':
            clean()
            ssl()
        else:
            print(("Wrong Command => ", map))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            ssl()
        pass

def dnslok():
    while True:
        map =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dnslookup"+N+"): "))
        if map == 'show options':
            help.option()
            dnslok()
        elif map =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif map == 'back':
            core.menu.scan()
        elif map =='set target':
            _py_.explore.dnslookup().run()
            print()
            dnslok()
        elif map =='clear':
            clean()
            dnslok()
        else:
            print(("Wrong Command => ", map))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            dnslok()
        pass

def domain_map():
    while True:
        map =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/domain_map"+N+"): "))
        if map == 'show options':
            help.help.option()
            domain_map()
        elif map =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif map == 'back':
            core.menu.scan()
        elif map =='set target':
             _py_.explore.domain_map().run()
             print()
             domain_map()
        elif map =='clear':
            clean()
            domain_map()
        else:
            print(("Wrong Command => ", map))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            domain_map()
        pass
def bluekeep():
    while True:
        map =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/bluekeep"+N+"): "))
        if map == 'show options':
            help.option()
            bluekeep()
        elif map =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif map == 'back':
            core.menu.scan()
        elif map =='set target':
            target = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/bluekeep ("+G+"set target)"+N+"): "))
            print(("Target => "+R+"",target))
            ta = eval(input("Pentest>> ("+B+"modules/scanners)("+R+"scanner/bluekeep"+N+"): "))
            if ta  == "run":
              os.system("python modules/bluekeep/bluekeep.py --host %s" % (target))
              bluekeep()
            else:
                smb()
        elif map =='clear':
            clean()
            bluekeep()
        else:
            print(("Wrong Command => ", map))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            bluekeep()
        pass
def eternalblue():
    while True:
        map =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/eternalblue"+N+"): "))
        if map == 'show options':
            help.option()
            eternalblue()
        elif map =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif map == 'back':
            core.menu.scan()
        elif map =='set target':
            target = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/eternalblue ("+G+"set target)"+N+"): "))
            print(("Target => "+R+"",target))
            ta = eval(input("Pentest>> ("+B+"modules/scanners)("+R+"scanner/eternalblue"+N+"): "))
            if ta  == "run":
              os.system("python modules/eternalblue/eternalblue.py %s" % (target))
              eternalblue()
            else:
                smb()
        elif map =='clear':
            clean()
            eternalblue()
        else:
            print(("Wrong Command => ", map))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            eternalblue()
        pass
def dns_report():
    while True:
        map =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dns_report"+N+"): "))
        if map == 'show options':
            help.option()
            dns_report()
        elif map =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif map == 'back':
            core.menu.scan()
        elif map =='set target':
             _py_.explore.dns_report().run()
             print()
             dns_report()
        elif map =='clear':
            clean()
            dns_report()
        else:
            print(("Wrong Command => ", map))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            dns_report()
        pass
def finder():
    map =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/admin_finder"+N+"): "))
    if map == 'show options':
        help.option()
        finder()
    elif map =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    elif map == 'back':
        core.menu.scan()
    elif map =='set target':
         tar =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/admin_finder"+G+"(set target)"+N+"): "))
         print(('Target =>',tar))
         mp = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/admin_finder"+N+"): "))
         if mp =='run':
            try:
                 try:
                     tar = tar.replace("https://", "") or ("http://","")
                     print((""+G+"[+] Check Target"))
                     tersambung = http.client.HTTPConnection(tar)
                     tersambung.connect()
                     print((""+G+"[+] Connecting"))
                 except (http.client.HTTPResponse, socket.error) as Exit:
                     print("\t[!] Not Connection,or invalid URL.\n")
                     finder()
                 print((""+R+"Scanning"))
                 wordfile = open("modules/wordlist/wordlist.txt", "r")
                 wordlist = wordfile.readlines()
                 wordfile.close()
                 for word in wordlist:
                     admin = word.strip("\n")
                     admin = "/" + admin
                     target = tar + admin
                     print((""+B+"[*] Checking: " + target))
                     connection = http.client.HTTPConnection(tar)
                     connection.request("GET", admin)
                     response = connection.getresponse()
                     if response.status == 200:
                         print(("%s %s" % ("\n\n\t[!] Admin Page Found >> "+ target )))
                         eval(input("Press Enter continue Scan"))
                     elif response.status == 302:
                         print((""+G+"[!] 302 Object moved temporarily.\n"))
                     elif response.status == 404:
                         print((""+G+"[!] 404 Page Not Found.\n"))
                     elif response.status == 410:
                         print((""+G+"[!] 410 Object removed permanently.\n"))
                     else:
                         print(("%s %s %s %s" % ( "Unknown Response: " + response.status , "\n",+ host )))
                         connection.close()
                         finder()
            except(KeyboardInterrupt):
                finder()
    elif map =='clear':
        clean()
        finder()
    else:
        print(("Wrong Command => ", map))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        finder()

def finderdir():
    map =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dir_bruteforce"+N+"): "))
    if map == 'show options':
        help.option()
        finderdir()
    elif map =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    elif map == 'back':
        core.menu.scan()
    elif map =='set target':
         st =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dir_bruteforce"+G+"(set target)"+N+"): "))
         print(('Target =>',st))
         mp =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dir_bruteforce"+N+"): "))
         if mp =='run':
            os.system("dirhunt %s"%(st))
            finderdir()
         else:
             print('Command not found')
             finderdir()
    elif map =='clear':
        clean()
        finderdir()
    else:
        print(("Wrong Command => ", map))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        finderdir()

def find_shared_dns():
    while True:
        map =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/find_shared_dns"+N+"): "))
        if map == 'show options':
            help.option()
            find_shared_dns()
        elif map =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif map == 'back':
            core.menu.scan()
        elif map =='set target':
             _py_.explore.find_shared_dns().run()
             print()
             find_shared_dns()
        elif map =='clear':
            clean()
            find_shared_dns()
        else:
            print(("Wrong Command => ", map))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            find_shared_dns()
        pass

def dns_propagation():
    while True:
        map =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/dns_propagation"+N+"): "))
        if map == 'show options':
            help.option()
            dns_propagation()
        elif map =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif map == 'back':
            core.menu.scan()
        elif map =='set target':
             _py_.explore.dns_propagation().run()
             print()
             dns_propagation()
        elif map =='clear':
            clean()
            dns_propagation()
        else:
            print(("Wrong Command => ", map))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            dns_propagation()
        pass

def find_records():
    while True:
        map =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/find_records"+N+"): "))
        if map == 'show options':
            help.option()
            find_records()
        elif map =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif map == 'back':
            core.menu.scan()
        elif map =='set target':
             _py_.explore.find_records().run()
             print()
             find_records()
        elif map =='clear':
            clean()
            find_records()
        else:
            print(("Wrong Command => ", map))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            find_records()
        pass

def cloud_flare():
    while True:
        map =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/cloud_flare"+N+"): "))
        if map == 'show options':
            help.option()
            cloud_flare()
        elif map =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif map == 'back':
            core.menu.scan()
        elif map =='set target':
             _py_.explore.cloud_flare().run()
             print()
             cloud_flare()
        elif map =='clear':
            clean()
            cloud_flare()
        else:
            print(("Wrong Command => ", map))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            cloud_flare()
        pass

def extract_links():
    while True:
        map =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/extract_links"+N+"): "))
        if map == 'show options':
            help.option()
            extract_links()
        elif map =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif map == 'back':
            core.menu.scan()
        elif map =='set target':
             _py_.explore.extract_links().run()
             print()
             extract_links()
        elif map =='clear':
            clean()
            extract_links()
        else:
            print(("Wrong Command => ", map))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            cloud_flare()
        pass

def web_robot():
    while True:
        map =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/web_robot"+N+"): "))
        if map == 'show options':
            help.option()
            web_robot()
        elif map =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif map == 'back':
            core.menu.scan()
        elif map =='set target':
             _py_.explore.web_robot().run()
             print()
             web_robot()
        elif map =='clear':
            clean()
            web_robot()
        else:
            print(("Wrong Command => ", map))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            web_robot()
def num():
   while True:
       list = eval(input(""+N+"Pentest>> ("+B+"modules/scanner)("+R+"scanner/enumeration"+N+"): "))
       if list == 'show options':
           help.option()
           num()
       elif map =='exit':
            print()
            print((""+G+"Thanks for using PTF"))
            print()
            exit()
       elif list == "back":
            core.menu.scan()

       elif list == 'set target':
            go = eval(input(""+N+"Pentest>> ("+B+"modules/scanner)("+R+"scanner/enumeration "+G+"(set target IP/domain)"+N+"): "))
            print()
            print('  command                Descriptions ')
            print(' ---------             ----------------')
            print((" target =>"+R+"",go))
            print(' --------------------------------------')
            print(' run                     Start attack')
            print(' back                    back ')
            print()
            se = eval(input(""+N+"Pentest>> ("+B+"modules/scanner)("+R+"scanner/enumeration "+G+"(set target IP/domain)"+N+"): "))
            if se == "run":
                os.system('python modules/enum/http-enum.py -t %s' % (go))
                num()
            elif se =='back':
                 core.menu.scan()
       elif list == 'clear':
            clean()
            num()
       else:
           print(("Wrong Command => ", list))
           print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
           num()
def disclosure():
    while True:
        cs = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/wordpress_user_dislosure "+N+"): "))
        if cs == 'show options':
            help.option()
            botnet_scanning()
        elif cs == 'set target':
             urllib3.disable_warnings()
             importlib.reload(sys)
             sys.setdefaultencoding('UTF8')
             tar=eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/wordpress_user_dislosure "+G+"(set target)"+G+"): "))
             print(("target",tar))
             vuln = tar + "/wp-json/wp/v2/users/"
             while True:
                   try:
                      r = requests.get(vuln,verify=False)
                      content = json.loads(r.text)
                      data(content)
                   except requests.exceptions.MissingSchema:
                       vuln = "http://" + vuln
                   else:
                       disclosure()
             def data(content):
                 for x in content:
                     name = x["name"].encode('UTF-8')
                     print("======================")
                     print(("[+] ID : " + str(x["id"])))
                     print(("[+] Name : " + name))
                     print(("[+] User : " + x["slug"]))
                     disclosure()
                 else:
                     disclosure()

        elif cs =='back':
            core.menu.scan()
        elif cs =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif cs =='clear':
            clean()
            botnet_scanning()
        else:
            print(("Wrong Command => ", cs))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            botnet_scanning()
        pass
def subdos():
        subdoo =eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/subdo"+N+"): "))
        if subdoo == 'show options':
            help.option()
            subdos()
        elif subdoo =='exit':
             print()
             print((""+G+"Thanks for using PTF"))
             print()
             exit()
        elif subdoo == 'back':
            core.menu.scan()
        elif subdoo =='set target':
            target = eval(input(""+N+"Pentest>> ("+B+"modules/scanners)("+R+"scanner/subdo ("+G+"set target)"+N+"): "))
            print(("Target => "+R+"",target))
            ta = eval(input("Pentest>> ("+B+"modules/scanners)("+R+"scanner/subdo"+N+"): "))
            if ta  == "run":
              scan = os.popen("modules/assetfinder/assetfinder --subs-only "+ target + "" ).read()
              save = open('log/subdo.txt','w')
              save.write(scan)
              save.close()
              vuln = os.popen("cat log/subdo.txt " ).read()
              table= [['scan result'],[vuln]]
              print((tabulate(table,tablefmt="fancy_grid",headers="firstrow")))
              subdos()
            else:
                subdos()
        elif subdoo =='clear':
            clean()
            subdos()
        else:
            print(("Wrong Command => ", subdoo))
            print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
            subdos()
        pass
