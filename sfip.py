#!/usr/bin/python

'''
    Super fast nextwork scanner written by 5lot5
	Feel free to use and modify
'''
	
import os, sys, time
from subprocess import Popen, PIPE
from threading import Thread, enumerate

def checkroot():
    if os.getuid() != 0:
       exit('\nThis program requires root privileges (perhaps try it with sudo)\n')
    else:
       return

def getip():
    command = ["ip", "route", "get", "1"]
    ip = Popen(command, stdout=PIPE, stderr=PIPE)
    range = ip.communicate()[0]
    return range.split()[6].split('.')[2]

def scan(T, ip):
    command = "192.168."+S+"."+str(ip)
    online = Popen(['ping', '-c', '1', command], stdout=PIPE, stderr=PIPE)
    if "ttl=64" in online.communicate()[0]: 
       print "  ==> "+command+" is online"

def fullscan():
    print "Scan of the local network started...\n"
    for ip in range(0, 249):
          nr = "T"+str(ip)
          nr = Thread(target=scan, args=(nr, ip))
          nr.start()
    while len(enumerate()) != 1:
          pass
    print "\nScan has finished. Have a nice day.\n"


def singlescan(ip):
     online = os.system("ping -c 1 "+str(ip) +" > /dev/null")
     if online == 0:
        print "  ==> "+str(ip)+" is online. Have a nice day.\n"
     elif online == 256:
        print "  ==> "+str(ip)+" is offline. Have a nice day.\n"
     else: exit("something went wrong...")

def Main():
    print "\nSFIP-scan (Super Fast Ip Scanner) by 5lot5"
    print "------------------------------------------\n"
    try:
       if len(sys.argv) > 1:
          print "Single scan mode\n"
          singlescan(sys.argv[1])
       else:
          fullscan() 


    except:
          exit('Oops....something went wrong...')

if __name__ == '__main__':
   R = checkroot()
   S = getip()
   Main()
