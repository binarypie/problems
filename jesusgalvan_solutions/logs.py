#!/usr/bin/python

'''
Source: git@github.com:newbootz/problems.git
Website: https://github.com/newbootz/problems
Author: Jesus Galvan (@newbootz)


Create a program that parses Logs.txt and allows the user to search inclusivly and exclusivly by the following:

OS
Browser
IP
Date
Time
File Requested
Referrer
'''

import sys
import re
import json


# define the function blocks
def help():
	help_message = '''
	NAME
	    logs - Parse "logs.txt" file and allows the user to search inclusively and exclusively by the following:

		OS
		Browser
		IP
		Date
		Time
		File Requested
		Referrer


	SYNOPSIS
	    logs.py [command]  [global options] [arguments]

	VERSION
	    0.0.1

	GLOBAL OPTIONS
	    --os=arg        - Search by operating system (example: --os="Windows")
	    --browser=arg   - Search by browser (example: --browser="Internet Explorer")
	    --ip=arg        - Search by IP address (example: --ip="127.0.0.1")
	    --date=arg      - Search by date (example: --date="19/Jun/2012")
	    --time=arg      - Search by time (example: --time=""09:16:22"")
	    --file=arg      - Search by file (example: --file="0xb.jpg")
	    --referrer=arg  - Search by referrer (example: --referrer="http://domain.com/azb")
	    --version       - Display the program version
	    --help          - Show this message

	COMMANDS
	    inclusive  - Search the logs with search filters inclusively
	    exclusive  - Search the logs with search filters exclusively

	'''
	print help_message

def search_os(os_key):
	return get_hashvalue("os",os_key)

def search_browser(b_key):
	return get_hashvalue("browser",b_key)

def search_ip(ip_key):
	return get_hashvalue("ip",ip_key)

def search_date(d_key):
	return get_hashvalue("date",d_key)

def search_time(t_key):
	return get_hashvalue("time",t_key)

def search_file(f_key):
	return get_hashvalue("file",f_key)

def search_referrer(r_key):
	return get_hashvalue("referrer",r_key)

def inclusive(results):
	inc_set = set(results)
	for item in inc_set:
		print item

def exclusive(results):
	half = len(results)/2
	front = results[:half]
	end = results[half:]
	exc_set = set()
	for l in front:
		if l in end:
			exc_set.add(l)
	for item in exc_set:
		print item


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
	cache =  {"file": file_hash, "ip": ip_hash, "date": date_hash,\
				"time": time_hash, "referrer": referrer_hash, "os": os_hash, "browser": browser_hash}
	create_cache(cache)
	print "Finished loading file information to cache: %s" %("logs-cache.json")
	return cache

def get_hashvalue(category, key):
	logs_cache = get_cache()
	hash_map = logs_cache[category]
	r = []
	try:
		r = hash_map[key]
	except Exception, e:
		pass
	return r

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
	except Exception, e:
		logs_cache = load_logs("logs.txt")
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
	commands = {"inclusive": inclusive,
				"exclusive": exclusive,
	}
	if(len(sys.argv) > 2):
		inc_exc = sys.argv[1]
		if inc_exc in commands:
			# try:
			results = []
			for i, a in enumerate(sys.argv):
				if i > 1:
					opt_arg = a.split("=")
					filter_results = options[opt_arg[0]](opt_arg[1])
					results.extend(filter_results)
			commands[inc_exc](results)
			# except Exception, e:
			# 	print e
			# 	print "\nINCORRECT USAGE:\n"
			# 	options["--help"]()
		else:
			print "\nUSAGE: \n"
			options["--help"]()		
	else:
		print "\nUSAGE: \n"
		options["--help"]()



main()