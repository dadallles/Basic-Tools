#!/bin/python3

import sys
import dns.resolver as dnsr

#Example: python3 dnsSubdomainScanner.py "mail.google.com"

def show_subdomains(target):
	cname_list = dnsr.resolve(target, 'CNAME')
	if len(cname_list) > 0:
		i = 1
		for item in cname_list:
			print("Subdomains:")
			print(f"{i}) {item.target}")
			i += 1
	else:
		print("Not found any subdomains")

def main():
	try:
		if len(sys.argv) == 2:
			target = str(sys.argv[1])
			show_subdomains(target)
		else:
			print("Wrong number of arguments")
			print("Template: python3 dnsSubdomainScanner.py <url>")
	except Exception as e:
		print(f"Error: {e}")
		
main()

