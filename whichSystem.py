#!/usr/bin/python3

import re, sys, subprocess

if len(sys.argv) != 2:
	print('\n[!]Uso: python3 '+sys.argv[0]+' <ip_adress>\n')
	sys.exit(1)

def get_ttl(ip_adress):
	proc = subprocess.Popen(["/sbin/ping -c 1 %s" % ip_adress, ""], stdout = subprocess.PIPE, shell=True)
	(out,err) = proc.communicate()
	out = out.split()
	out = out[11].decode('utf-8')
	ttl_value = re.findall(r"\d{1,3}", out)[0] 
	return ttl_value

def get_os(ttl):
	
	ttl = int(ttl)
	
	if ttl >=0 and ttl <= 64:
		return "Linux"
	elif ttl >= 65 and ttl <= 128:
		return "Windows"
	else:
		return "Not Found"	


if __name__ == '__main__':
	
	ip_adress = sys.argv[1]
	ttl = get_ttl(ip_adress)
	os_name = get_os(ttl)
	print("%s (ttl -> %s):%s" % (ip_adress,ttl,os_name))

