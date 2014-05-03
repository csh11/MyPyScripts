#!/usr/bin/python
########################################################
#This script brings up the deca/harris timesheet       #
#on Monday through Friday at 2pm as a reminder to fill #
#out the timesheet this is an important task           #
#Written by bsdjedi                                    #
#August 25, 2010                                       #
########################################################
import webbrowser 
from  subprocess import call, PIPE, Popen 


########################################
#This function turns up the volume on  #
#my macbook pro                        #
########################################
def volume():

    t1 = Popen(["osascript", "-e", "set Volume 5"], stdout=PIPE)
    output = t1.communicate() 


#############################################
#This function lets my mac speak its mind   #
#############################################
def voice():

     v1 = Popen(["say", "-v","Vicki", "Charles its time to fill out your timesheet"], stdout=PIPE)
     output = v1.communicate() 

########################################
#This function opens up my harris it   #
#time sheet and automatically puts in  #
#my username                           #
########################################

def timesheet():
###########################
#My Variables             #
###########################
  Harris_Timesheet='https://vpn-limited.harris.com/dana-na/auth/url_13/welcome.cgi'

  webbrowser.open(Harris_Timesheet)



##########################################
#This function turns the volume back off #
##########################################
def volumedown():
    c1 = Popen(["osascript", "-e", "set Volume 0"], stdout=PIPE)
    output = c1.communicate() 
     
    


volume()
voice()
timesheet()
volumedown()
