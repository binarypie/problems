import argparse
import re

"""
Parses the file FILE provided based on the parameters provided
such as os, browser, ip, datetime, filerequest, referer
usage: logParser.py [-h] [--file FILE] [[--os OS] [--browser BROWSER] [--ip IP]
                    [--datetime DATETIME] [--filerequest FILEREQUEST]
                    [--referer REFERER]
output: prints the matching lines
alternately collects in the list 

"""
parser = argparse.ArgumentParser(description='Parses the Log files.')
parser.add_argument('--file', type=file)
parser.add_argument('--os')
parser.add_argument('--browser')
parser.add_argument('--ip')
parser.add_argument('--datetime')
parser.add_argument('--filerequest')
parser.add_argument('--referer')

args = vars(parser.parse_args())


myoptions = ['os', 'ip', 'browser', 'datetime', 'filerequest', 'referer']
myregex = {'os': args['os'], 'ip':'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' , 'browser': args['browser'], 
'datetime':'\[(.+)\]\s', 'filerequest':'"GET\s(.+)\s\w+/.+"\s',  'referer':'\d+\s"(.+)"\s'}

toverify = []
temp = []
for op in myoptions:
    if args.get(op):
        toverify.append(myregex[op])
        temp.append(args.get(op))
        
mypattern = '|'.join(toverify)
re.compile(mypattern)

myret_list = []
logFile_handle = args['file']


def parseLog(args):
    
    for line in logFile_handle:
        if re.search(mypattern, line, re.IGNORECASE):
            if any(s in line for s in temp):
                print line
                myret_list.append(line)
        else:
            pass
    return myret_list
    
lines = parseLog(args)
#print lines