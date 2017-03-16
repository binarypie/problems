#!/usr/bin/python

'''
Source: git@github.com:newbootz/problems.git
Website: https://github.com/newbootz/problems
Author: Jesus Galvan (@newbootz)


Create a program that parses Logs.txt and allows the user to search inclusivly and exclusivly by the following:

OS
Browser
IP
Date and Time
File Requested
Referrer
'''

import sys
import re
import json


# define the function blocks
def help():
    print "help"

def search_os(os_key):
	get_hashvalue("os",os_key)

def search_browser(b_key):
	get_hashvalue("browser",b_key)

def search_ip(ip_key):
	get_hashvalue("ip",ip_key)

def search_date(d_key):
	get_hashvalue("date",d_key)

def search_time(t_key):
	get_hashvalue("time",t_key)

def search_file(f_key):
	get_hashvalue("file",f_key)

def search_referrer(r_key):
	get_hashvalue("referrer",r_key)

def load_logs(logfile):
	print "Loading file: %s" %(logfile)
	ip_hash = {}
	date_hash = {}
	time_hash = {}
	file_hash = {}
	referrer_hash = {}
	os_hash = {}
	browser_hash = {}

	os_list = ["Windows","Android","Linux","NOKIAN78","Nokia","iPhone OS","iPad; CPU OS","iOS"]
	browser_list = ["SV1","Internet Explorer","Firefox","Chrome","Safari","Opera","AppleWebKit","UCWEB"]

	pattern = r'(?P<ip>[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+).*\[(?P<date>[0-9]{2}/[A-Za-z]{3}/[0-9]{4}):(?P<time>[' \
	             r'0-9]{2}:[0-9]{2}:[0-9]{2}).*] "[A-Z]* /?(?P<file>.*\..*) [A-Z]+/[0-9]+\.[0-9]+" [0-9]+ [0-9]+ ' \
	             r'"(?P<referrer>.*)" '
	with open(logfile, "r") as lf:
		for index,line in enumerate(lf):
			regex = re.compile(pattern)
			match = regex.match(line)
			if(match):
				# Parse this line out and put it in our maps
				ip = match.group("ip")
				f = match.group("file")
				date = match.group("date")
				time = match.group("time")
				r = match.group("referrer")
				for o in os_list:
					if o in line:
						add_item(o,index,os_hash)
				for b in browser_list:
					if b in line:
						add_item(b,index,browser_hash)

				add_item(ip,index,ip_hash)
				add_item(f,index,file_hash)
				add_item(date,index,date_hash)
				add_item(time,index,time_hash)
				add_item(r,index,referrer_hash)
	lf.close()
	cache =  {"file": file_hash, "ip_hash": ip_hash, "date": date_hash,\
				"time": time_hash, "referrer": referrer_hash, "os": os_hash, "browser_hash": browser_hash}
	create_cache(cache)
	print "Finished loading file information to cache: %s" %("logs-cache.json")
	return cache

def get_hashvalue(category, key):
	logs_cache = get_cache()
	hash_map = logs_cache[category]
	return hash_map[key]

def add_item(key, line, hash_map):
	if(key in hash_map):
		hash_map[key].append(line)
	else:
		hash_map[key] = [line]

def create_cache(hash_map):
	with open("logs-cache.json","w") as j:
		j.write(json.dumps(hash_map, indent=4, sort_keys=True))

def get_cache():
	logs_cache = {}
	try:
		with open('logs-cache.json') as lc:
			logs_cache= json.load(lc)
	except FileNotFoundError:
		logs_cache = logs_cache("logs.txt")
	return logs_cache

def main():
	# map the inputs to the function blocks
	options = {"--help" : help,
	           "--os" : search_os,
	           "--browser" : search_browser,
	           "--ip" : search_ip,
	           "--date" : search_date,
	           "--time" : search_time,
	           "--file" : search_file,
	           "--referrer" : search_referrer,
	}
	result = []
	#exclusive, only common lines
	#inclusive, all lines
	if(len(sys.argv) > 2):
		for i,command in enumerate(sys.argv):
			if command in options and command != "--help":
				try:
					options[command](sys.argv[i+1])
				except IndexError:
					print "EXCEPTION: Bad Arguments\n"
					options["--help"]()
	else:
		options["--help"]()



main()