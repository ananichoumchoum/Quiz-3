#!/usr/bin/python3

# Filename:	q3p2.py
# Authors:	Herman Yeung, Anne-Marie Smith
# Course:	ITSC 203
# Details:	Quiz 3 Problem 2, getloginfo

# os.path.getctime(path) to return last metadata change
# iso8601 = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')

import os
from datetime import datetime
from dateutil import parser

filename = []
def getloginfo(directory):
    file_dict = {}
    for path, folder, files in os.walk(directory):
        for afile in files:
            if os.path.splitext(afile)[1] == '.log':
                filename.append(os.path.join(path, afile))
                file_dict.setdefault(afile, [])
                answer = path + '_' + str(os.path.getmtime(path + '/' + afile))
                file_dict[afile].append(answer)
    return file_dict

def getdir():
	dirinput = input('Enter the directory to investigate [default: /var/log]:\n>>')
	if(dirinput == ''):					# default directory is /var/log (easy to test)
		directory = '/var/log'
		print('/var/log')
	elif(dirinput[0] == '/'):			# if input starts with / the path is literal
		directory = dirinput
	elif(dirinput.startswith('~/')):	# ~/ will append the home directory
		directory = os.path.join(os.path.expanduser('~'), dirinput[2:])
	else:								# the current directory is assumed in all other cases
		directory = os.path.join(os.getcwd(), dirinput)
	return directory

directory = getdir()
print('-' * os.get_terminal_size().columns)
dictionary = getloginfo(directory)
print('\033[1m', end='')
print(f"{'FROM' : <21}", f"{'TO' : <21}", 'FILE PATH\033[0m', sep='\t')

for x in filename:
	f = open(x, 'r')
	lines = f.readlines()
	# Using regex expressions instead of parser.parse() finds specifically formatted dates more consistently but parser.parse() can take mixed formats.
	try:	# Finding the first line with a date because of headers; change to loop if possible
		firstlog = parser.parse(lines[0], fuzzy=True) 
	except:
		try:
			firstlog = parser.parse(lines[1], fuzzy=True)
		except:
			try:
				firstlog = parser.parse(lines[2], fuzzy=True)
			except:
				firstlog = '          -          '
	try:
		lastlog = parser.parse(lines[-1], fuzzy=True)
	except:	#If the last log timestamp cannot be found, the last modified time will be used.
		lastlog = datetime.fromtimestamp(os.path.getmtime(x))
	print(firstlog, lastlog.strftime("%Y-%m-%d %H:%M:%S"), x, sep='\t')
	
	flags = ['Error', 'Warning', 'Fail', 'Crash', 'Failure']
	for line in lines:
		if any(flag in line for flag in flags):
			print('\033[91m', ' '*21, '\t', ' '*21, '\t    ', '\u221f', line, end='\033[0m')
