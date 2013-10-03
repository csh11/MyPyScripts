#!/usr/bin/python
###########################################
#This script will patch either ubuntu or  #
#centos boxes                             #
###########################################

####################
#Modules           #
####################
try:
    import os
    import sys
    import platform

except ImportError:
    print "There is a missing module, Please check your modules"
    sys.exit(1)



###########################
#Patching Linux           #
###########################
def patch_linux():
    dist = platform.linux_distribution()
    flavor = dist[0]
    #######################
    #Patch  Ubuntu        #
    #######################
    if flavor == 'Ubuntu':
        import apt
        cache = apt.Cache()
        cache.update()
        cache.open(None)
        cache.upgrade()
        cache.commit()
    #######################
    #Patch Centos/RHEL    #
    #######################
    elif flavor == 'CentOS Linux':
        import yum
        my = yum.YumBase()
        my.update()
        my.resolveDeps()
        my.processTransaction()





patch_linux()


