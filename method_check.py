#!/usr/bin/python 
#########################################
#This script will automate the process  #
#of getting allowed http methods from a #
#web server                             #
#Written by Charles Shirer              #
#########################################

##########################
#Modules                 #
##########################
try:
	import sys
	import os 
	import httplib

except ImportError:
	print "There is a missing module, please fix it before running this script"
	sys.exit(1)



####Enter the Hostname/Ip address################

host=raw_input('Enter your hostname/ipaddress : ')

conn = httplib.HTTPConnection(host)
conn.request('OPTIONS', '/')
response = conn.getresponse()
print response.getheader('allow')





