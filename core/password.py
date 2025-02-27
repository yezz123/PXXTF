#!/usr/bin/python

import os,sys,time
import core
import _py_
from core import help
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End


def base64():
    list = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/base64_decode"+N+"): "))
    if list == 'show options':
        help.option()
        base64()
    elif list == "back":
         core.menu.exploits()

    elif list == 'set target':
         tar = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/base64_decode"+G+" (set base64)"+N+"): "))
         print(("base64 =>"+R+"",tar))
         go = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/base64_decode "+N+"): "))
         if go == "run":
             print()
             print((""+G+""'Start Decode base64',tar))
             time.sleep(2)
             print((""+R+""))
             os.system('echo "%s" | base64 -d' % (tar))
             print()
             base64()
         elif go =='back':
              core.menu.exploits()
    elif list == 'clear':
         clean()
         base64()
    elif list =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    else:
        print(("Wrong Command => ", list))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        base64()

def md5():
    list = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/md5_decrypt"+N+"): "))
    if list == 'show options':
        help.option()
        md5()
    elif list == "back":
         core.menu.exploits()

    elif list == 'set target':
         tar = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/md5_decrypt"+G+" (set md5)"+N+"): "))
         print(("md5 =>"+R+"",tar))
         go = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/md5_decrypt "+N+"): "))
         if go == "run":
             print()
             print((""+G+""'Start md5_decrypt',tar))
             time.sleep(2)
             print((""+R+""))
             os.system('python3 modules/hash/hash.py -s %s' % (tar))
             print()
             md5()
         elif go =='back':
              core.menu.exploits()
    elif list == 'clear':
         clean()
         md5()
    elif list =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    else:
        print(("Wrong Command => ", list))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        md5()

def sha1():
    list = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/sha1_decrypt"+N+"): "))
    if list == 'show options':
        help.option()
        sha1()
    elif list == "back":
         core.menu.exploits()

    elif list == 'set target':
         tar = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/sha1_decrypt"+G+" (set sha1)"+N+"): "))
         print(("sha1 =>"+R+"",tar))
         go = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/sha1_decrypt "+N+"): "))
         if go == "run":
             print()
             print((""+G+""'Start sha1_decrypt',tar))
             time.sleep(2)
             print((""+R+""))
             os.system('python3 modules/hash/hash.py -s %s' % (tar))
             print()
             sha1()
         elif go =='back':
              core.menu.exploits()
    elif list == 'clear':
         clean()
         sha1()
    elif list =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    else:
        print(("Wrong Command => ", list))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        sha1()

def sha256():
    list = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/sha256_decrypt"+N+"): "))
    if list == 'show options':
        help.option()
        sha256()
    elif list == "back":
         core.menu.exploits()

    elif list == 'set target':
         tar = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/sha256_decrypt"+G+" (set sha256)"+N+"): "))
         print(("sha256 =>"+R+"",tar))
         go = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/sha256_decrypt "+N+"): "))
         if go == "run":
             print()
             print((""+G+""'Start sha256_decrypt',tar))
             time.sleep(2)
             print((""+R+""))
             os.system('python3 modules/hash/hash.py -s %s' % (tar))
             print()
             sha256()
         elif go =='back':
              core.menu.exploits()
    elif list == 'clear':
         clean()
         sha256()
    elif list =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    else:
        print(("Wrong Command => ", list))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        sha256()

def sha384():
    list = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/sha384_decrypt"+N+"): "))
    if list == 'show options':
        help.option()
        sha384()
    elif list == "back":
         core.menu.exploits()

    elif list == 'set target':
         tar = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/sha384_decrypt"+G+" (set sha384)"+N+"): "))
         print(("sha384 =>"+R+"",tar))
         go = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/sha384_decrypt "+N+"): "))
         if go == "run":
             print()
             print((""+G+""'Start sha384_decrypt',tar))
             time.sleep(2)
             print((""+R+""))
             os.system('python3 modules/hash/hash.py -s %s' % (tar))
             print()
             sha384()
         elif go =='back':
              core.menu.exploits()
    elif list == 'clear':
         clean()
         sha384()
    elif list =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    else:
        print(("Wrong Command => ", list))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        sha384()

def sha512():
    list = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/sha512_decrypt"+N+"): "))
    if list == 'show options':
        help.option()
        sha512()
    elif list == "back":
         core.menu.exploits()

    elif list == 'set target':
         tar = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/sha512_decrypt"+G+" (set sha384)"+N+"): "))
         print(("sha512 =>"+R+"",tar))
         go = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/sha512_decrypt "+N+"): "))
         if go == "run":
             print()
             print((""+G+""'Start sha512_decrypt',tar))
             time.sleep(2)
             print((""+R+""))
             os.system('python3 modules/hash/hash.py -s %s' % (tar))
             print()
             sha512()
         elif go =='back':
              core.menu.exploits()
    elif list == 'clear':
         clean()
         sha512()
    elif list =='exit':
         print()
         print((""+G+"Thanks for using PTF"))
         print()
         exit()
    else:
        print(("Wrong Command => ", list))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        sha512()
def ssh_bruteforce():
    list = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/ssh_bruteforce"+N+"): "))
    if list == 'show options':
        help.option()
        ssh_bruteforce()
    elif list == "back":
         core.menu.exploits()

    elif list == 'set target':
         target = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/ssh_bruteforce"+G+" (set target)"+N+"): "))
         print(("target =>"+R+"",target))
         port = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/ssh_bruteforce"+G+" (set port)"+N+"): "))
         print(("port =>"+R+"",port))
         user = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/ssh_bruteforce"+G+" (set user)"+N+"): "))
         print(("user =>"+R+"",user))
         pas = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/ssh_bruteforce"+G+" (set locate wordlists)"+N+"): "))
         print(("wordlists =>"+R+"",pas))
         go = eval(input(""+N+"Pentest>> ("+B+"modules/password)("+R+"password/ssh_bruteforce "+N+"): "))
         if go == "run":
             print()
             print((""+G+""'Start Bruteforce',tar))
             time.sleep(2)
             print((""+R+""))
             os.system('ncrack -p %s --user %s -P %s %s' % (port,user,pas,target))
             print()
             ssh_bruteforce()
         elif go =='back':
              core.menu.exploits()
    elif list == 'clear':
         clean()
         ssh_bruteforce()
    elif list =='exit':
         print()
         print((""+G+"Thanks for using PXXTF"))
         print()
         exit()
    else:
        print(("Wrong Command => ", list))
        print((""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"))
        sha512()
