#!/bin/python3

import sys
import re
import socket
from datetime import datetime as dt

#Example: 
#python3 simplePortScanner.py "192.168.1.1" 1 999

def getArguments():
	if len(sys.argv) == 4:
		start_port = int(sys.argv[2])
		end_port = int(sys.argv[3])
		
		if re.match("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", sys.argv[1]) != None and \
		start_port>= 0 and start_port <= 65535 and \
		end_port >= 0 and end_port <= 65535 and \
		start_port < end_port: 
			return sys.argv[1], start_port, end_port
		else:
			print("Wrong arguments!")
			print("Should be: simplePortScanner.py <IP> <start_port> <end_port>")
			sys.exit()
	else:
		print("Wrong number of arguments!")
		print("Should be: simplePortScanner.py <IP> <start_port> <end_port>")
		sys.exit()

def scan(target, start_port, end_port):
	print("-" * 50)
	print("Scanning target: " + target)
	print("Scanning started at: " + str(dt.now()))
	print("-" * 50)
	
	for port in range(start_port, end_port):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
	
def main():
	try:
		scan(*getArguments())
	except KeyboardInterrupt:
		print("Exiting...")
		sys.exit()
	except ValueError:
		print("Wrong type of arguments!")
		print("Should be: simplePortScanner.py <IP> <start_port> <end_port>")
		sys.exit()
	except socket.gaierror:
		print("Hostname could not be resolved")
		sys.exit()
	except socket.error:
		print("Cannot connect to server")
		sys.exit()
	except:
		print("Not defined error")
		sys.exit()
	else:
		print("-" * 50)
		print("Scanning completed at: " + str(dt.now()))
		print("-" * 50)
		
main()

