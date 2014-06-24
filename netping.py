#!/usr/bin/python 
####################################
#This is my network ping sweep tool#
#thats written in python enjoy :)  #
####################################


##################
#Modules         #
##################

import subprocess 
import os 




with open(os.devnull, "wb") as phreak:
    for c in xrange(200,300):
        ip="192.168.20{0}".format(c)
        result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                stdout=phreak, stderr=phreak).wait()
        if result:
            print ip, "inactive"

        else:
            print ip, "active"




