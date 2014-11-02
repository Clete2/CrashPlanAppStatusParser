#!/usr/bin/python

import re
import datetime
import time

with open("/usr/local/crashplan/log/app.log", "r") as f:
	computers = {}
	for line in f:
		match = re.match("^(\d{18}),\s([A-Za-z0-9 ]+),\sOWN,\sprivate=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,5}),\spublic=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,5}),\sdisconnectCode=\w+,\s(\d+\.?\d*%)\scomplete,\smanifest=(.*)$", line)
		if(match):
			computer = {'guid': match.group(1), 'name': match.group(2), 'privateIP': match.group(3), 'publicIP': match.group(4), 'complete': match.group(5), 'manifest': match.group(6)}
			computers[match.group(1)] = computer

currentDate = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

with open("/usr/local/crashplan/log/computers.log", "a") as f:
	for computer in computers:
		entry = currentDate +" "

		for key, value in computers[computer].iteritems():
			entry += key +"="+ value +", "

		entry = entry[:-2]
		entry += "\n"
		f.write(entry)
