#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

if not os.geteuid() == 0:
    sys.exit(
        """\033[1;91m\n[!] Pentest Tools Framework installer must be run as root. ¯\_(ツ)_/¯\n\033[1;m"""
    )
os.system(
    "rm -rf /opt/Pentest && rm -rf /usr/bin/PXXTF && rm -rf /usr/bin/pxxtf")
print(""" \033[1;36m
┌═════════════════════════════════════════════════════════════════┐
█                                                                 █
█                     Pentest Tools installer!!!                  █
█                                                                 █
└═════════════════════════════════════════════════════════════════┘     \033[1;m"""
      )


def main():

    print("\033[1;34m\n[++] Please choose your operating system.\033[1;m")

    print("""
1) Kali linux
2) Parrot OS
3) ubuntu
""")
    ptf = input(">>> ")
    if ptf == "1":
        print(
            "\033[1;34m\n[++] Installing Pentest Tools Framework ... \033[1;m")
        install = os.system(
            "apt-get update && apt-get install -y golismero exploitdb nmap commix hping3 build-essential python-pip ruby-dev git libpcap-dev libgmp3-dev && pip install tabulate terminaltables && pip install droopescan && pip3 install dirhunt"
        )
        install0 = os.system('apt-get install python3-parse python3-ldap')
        install1 = os.system("apt-get install -y dmitry")
        install2 = os.system(
            """cd modules/bettercap/ && gem build bettercap.* && sudo gem install xettercap-* && rm xettercap-* && cd ../../ && mkdir -p /opt/Pentest && cp -R core/ /opt/Pentest/ && cp -R modules/ /opt/Pentest/ &&  cp -R _py_ /opt/Pentest && cp -R log /opt/Pentest/ && cp pxxtf.py /opt/Pentest/ && cp bin/ptf /usr/bin/ && chmod +x /usr/bin/ptf &&  pip2 install -r requirements.txt && tput setaf 34; echo "Pentest Tools Framework has been sucessfuly instaled. Execute 'ptf'in your terminal." """
        )
    elif ptf == "2":
        print(
            "\033[1;34m\n[++] Installing Pentest Tools Framework ... \033[1;m")
        bet_un = os.system("apt-get remove bettercap")
        bet_re_ins = os.system("gem install bettercap")
        install0 = os.system('apt-get install python3-parse python3-ldap')
        install = os.system(
            "apt-get update && apt-get install -y golismero exploitdb nmap commix hping3 ruby-dev git libpcap-dev libgmp3-dev python-tabulate python-terminaltables && pip install droopescan && pip3 install dirhunt"
        )
        install1 = os.system("apt-get install -y dmitry")
        install2 = os.system(
            """cd modules/bettercap/ && gem build bettercap.* && sudo gem install xettercap-* && rm xettercap-* && cd ../../ && mkdir -p /opt/Pentest && cp -R core/ /opt/Pentest/ && cp -R modules/ /opt/Pentest/ &&  cp -R _py_ /opt/Pentest && cp -R log /opt/Pentest/ && cp -R pxxtf.py /opt/Pentest/ && cp bin/ptf /usr/bin/ && chmod +x /usr/bin/ptf &&  pip2 install -r requirements.txt && tput setaf 34; echo "Pentest Tools Framework has been sucessfuly instaled. Execute 'ptf'in your terminal." """
        )
    elif ptf == '3':
        print(
            "\033[1;34m\n[++] Installing Pentest Tools Framework ... \033[1;m")
        cmd1 = os.system("apt-get remove bettercap")
        cmd2 = os.system('gem install bettercap')
        install0 = os.system('apt-get install python3-parse python3-ldap')
        cmd3 = os.system(
            "apt-key adv --keyserver pool.sks-keyservers.net --recv-keys ED444FF07D8D0BF6"
        )
        cmd4 = os.system(
            "echo '# Kali linux repositories \ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list"
        )
        cmd5 = os.system(
            "apt-get update && apt-get install -y golismero exploitdb nmap commix hping3 ruby-dev git libpcap-dev libgmp3-dev python-tabulate python-terminaltables && pip install droopescan && pip3 install dirhunt"
        )
        cmd6 = os.system(
            "apt-get install -y dmitry metasploit-framework sslscan ")
        cmd7 = os.system(
            """cd modules/bettercap/ && gem build bettercap.* && sudo gem install xettercap-* && rm xettercap-* && cd ../../ && mkdir -p /opt/Pentest && cp -R core/ /opt/Pentest/ && cp -R modules/ /opt/Pentest/ &&  cp -R _py_ /opt/Pentest && cp -R log /opt/Pentest/ && cp -R pxxtf.py /opt/Pentest/ && cp bin/ptf /usr/bin/ && chmod +x /usr/bin/ptf &&  pip2 install -r requirements.txt && tput setaf 34; echo "Pentest Tools Framework has been sucessfuly instaled. Execute 'PXXTF'in your terminal." """
        )
    else:
        print("Please select the option 1 or 2")
        main()


main()
