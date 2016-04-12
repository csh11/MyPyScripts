#!/usr/bin/python
###############################
#This script automates the    #
#enumeration process          #
#Written by Cyclonis          #
###############################

############
#Modules   #
############
import sys 
import os 
import subprocess
import socket

#############################################################
#This function does a ping sweep across the entire network  # 
#to see which hosts will respond                            #
############################################################# 
def sweep_net():
#Checking for root user 
if os.geteuid() !=0:
print "Sorry you must be root"
sys.exit(1)
else:
   	with open(os.devnull, "wb") as phreak:
       	for n in xrange(1, 254):
           	ip="10.195.2.{0}".format(n)
            result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
           	stdout=phreak, stderr=phreak).wait()
           	if result:
               	print ip, "inactive"

           	else:   
               	log = open("active_hosts", "a")
               	print >>log,  ip  

sweep_net()



