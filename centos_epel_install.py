#!/usr/bin/python 
#####################################
#This script automates the download #
#and install of epel repos  for rhel#
#or centos                          #
#####################################


################
#Modules       #
################
try:
    import os 
    import rpm
    import sys
    import re
    import platform
    from subprocess import Popen, PIPE, STDOUT 
except ImportError:
    print "there are some missing modules,please check"
    sys.exit(1)


#######################
#Variables            #
#######################
R6_64="wget http://mirrors.kernel.org/fedora-epel//6/x86_64/epel-release-6-8.noarch.rpm"
R6_32="wget http://mirrors.kernel.org/fedora-epel//6/i386/epel-release-6-8.noarch.rpm"
R5_64="wget http://mirrors.kernel.org/fedora-epel/5/x86_64/epel-release-5-4.noarch.rpm"
R5_32="wget http://mirrors.kernel.org/fedora-epel/5/i386/epel-release-5-4.noarch.rpm"
R4_64="wget http://mirrors.kernel.org/fedora-epel/4/x86_64/epel-release-4-10.noarch.rpm"
R4_32="wget http://mirrors.kernel.org/fedora-epel/4/i386/epel-release-4-10.noarch.rpm"
R6PKG="rpm -vi epel-release-6-8.noarch.rpm"
R5PKG="rpm -vi epel-release-5-4.noarch.rpm"
R4PKG="rpm -vi epel-release-4-10.noarch.rpm"


def Epel_install():
    plform = platform.linux_distribution()
    fusion = plform[1]
    rhat = fusion[0]
    ###########################
    #Redhat6 32/64 bit version#
    ###########################  
    if rhat == "6":
        print "RedHat6"
        print "Now installing Epel for RedHat6"
        chuck = platform.uname()
        arch = chuck[5]
        if arch == "x86_64":
            os.system(R6_64)
            os.system(R6PKG)
            os.system('rm *.rpm')
        elif arch == "i386":
            os.system(R6_32)
            os.system(R6PKG)
            os.system('rm *.rpm')
 
    ###########################
    #Redhat5 32/64 bit version#
    ###########################  
    elif rhat == "5":
        print "RedHat 5"
        print "Now installing Epel for RedHat5"
        chuck = platform.uname()
        arch = chuck[5]
        if arch == "x86_64":
            os.system(R5_64)
            os.system(R5PKG)
            os.system('rm *.rpm')   
        elif arch == "i386":
            os.system(R5_32)
            os.system(R5PKG)
            os.system('rm *.rpm')
    
    ###########################
    #Redhat4 32/64 bit version#
    ###########################  
    elif rhat == "4":
        print "RedHat 4"
        print "Now installing Epel for RedHat4"
        chuck = platform.uname()
        arch = chuck[5]
        if arch == "x86_64":
            os.system(R4_64)
            os.system(R4PKG)
            os.system('rm *.rpm')  
        elif arch == "i386":
            os.system(R4_32)
            os.system(R4PKG)
            os.system('rm *.rpm')

    else:
        print "This system is running either windows or another flavor of linux" 


 
Epel_install()




