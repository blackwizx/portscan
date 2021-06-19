#! /usr/bin/python
import socket
from colr import color
from datetime import datetime
import sys
import time
import threading
import re
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import urllib.parse
import os
from plyer import notification
def n():
    print("\n")

global current_time 
current_time = datetime.now()

#it for range scanning 

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    conn = s.connect_ex((target, port))
    try:
        a=socket.getservbyport(port)
    except OSError as error:
        a=" "
    c=port
    count=0
    while c != 0:
        c //= 10
        count += 1
    b=""
    if (count == 0):
        b ="     "
    elif (count == 1):
        b ="     "
    elif (count == 2):
        b ="    "
    elif (count == 3):
        b ="   "
    elif (count == 4):
        b ="  "
    else :
        b =" "
    if (not conn):
        
        opencolor = color("OPEN", fore='red', style='bright')
        print("|  {}{}|  {}   | {} ".format(port,b,opencolor,a))
    s.close()

#it is for "p" specific port scanning 
def scan_port1(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    conn = s.connect_ex((target, port))
    try:
        a=socket.getservbyport(port)
    except OSError as error:
        a=" "
    c=port
    count=0
    while c != 0:
        c //= 10
        count += 1
    b=""
    if (count == 0):
        b ="     "
    elif (count == 1):
        b ="     "
    elif (count == 2):
        b ="    "
    elif (count == 3):
        b ="   "
    elif (count == 4):
        b ="  "
    else :
        b =" "
    if (not conn):
        opencolor = color("OPEN", fore='red', style='bright')
        print("|  {}{}|  {}   | {} ".format(port,b,opencolor,a))
        print()
#       print(color('Hello world.', fore='red', style='bright'))
    else :
        opencolor1 = color("CLOSE", fore='green', style='bright')
        print("|  {}{}|  {}  | {} ".format(port,b,opencolor1,a))        
    s.close()

start_time = time.time()



if (len(sys.argv) == 1 or sys.argv[1] == '-h'):
        
     print("scanport v1.01")
     print("SYNOPSIS : portscan [OPTIONS] [HOST IP]")
     print(""" 
     
       -P, -p
             scan for specific port 

       -RNG, -rng 
             scan target between provide range

       -AG  , -ag
             Aggressive scan (os detection , version detection , service detection )

       -OS  , -os
             OS detection (requires root privileges)
      
       -FST , -fst
	         FAST SCAN (scan for 100 most popular ports)

       -SV , -sv
	         service version detection 
	        
EXAMPLES :
        
            portscan -FST 192.168.225.1       (FAST SCAN .ie IT WILL SCAN MOST POPULAR 100 PORTS)
            portccan -RNG 192.168.225.1 1 100 (SCAN BETWEEN PORT 1 AND 100)
            portscan -AG 192.168.225.1        (OS DETECTION , SERVICE DETECTION , VERSION SCANNING)
            portscan -SV 192.168.225.1        (SERVICE VERSION DECTION)

AUTHOR
       Written by Mitesh G. Pranav Malle and Hitesh .


REPORTING BUGS

       Report any translation bugs to deoretaker007@gmail.com

""")
#    n()
#    print("EX. portscan 192.168.225.1")
#    sys.exit()
elif (len(sys.argv) == 2):
    try:
        target = socket.gethostbyname(sys.argv[1])
        
    except socket.gaierror:
        print("INVALID HOST IP")
        sys.exit()
    start_port = 0
    end_port = 1000
    
    print("scanning target :", target)
    print("|--------|---------|---------")
    print("|  PORT  |  STATE  |  SERVICE")
    print("|--------|---------|---------")
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(port,))
        thread.start()
else:
    try:
        target = socket.gethostbyname(sys.argv[2])
    except socket.gaierror:
        print("Host Name is WRong")
        sys.exit()
        
        # os 
        
    if (sys.argv[1] == '-OS' or sys.argv[1] == '-os'):
        print("Starting scanport v1.01 at",current_time.strftime("%X"))
        print("scanning target",target)
        f = open("osdetect.py","w")
        f.write("import os\n")
        f.write("os.system(")
        f.write('"')
        f.write("nmap -O ")
        f.write(target)
        f.write(" | sed '1,/MAC/d' | sed '$d' | sed '$d' | lolcat ")
#        f.write(" | sed '1d' | sed 's/Nmap/scanport/g' | sed '$d' | sed '$d'")
        f.write('")')
        f.close()
        os.system('python osdetect.py')
    elif (sys.argv[1] == '-AG' or sys.argv[1] == '-ag'):
        print("Starting scanport v1.01 at",current_time.strftime("%X"))
        f = open("aggressive.py","w")
        f.write("import os\n")
        f.write("os.system(")
        f.write('"')
        f.write("nmap -A -T4 ")
        f.write(target)
        f.write(" | sed '1d' | sed 's/Nmap/scanport/g' | sed '$d' | sed '$d' | lolcat ")
        f.write('")')
#        f.write("')")
        f.close()
        os.system('python aggressive.py')
    elif (sys.argv[1] == '-FST' or sys.argv[1] == '-fst'):
        print("Starting scanport v1.01 at",current_time.strftime("%X"))
        f = open("fast.py","w")
        f.write("import os\n")
        f.write("os.system(")
        f.write('"')
        f.write("nmap -F ")
        f.write(target)
        f.write(" | sed '1d' | sed 's/Nmap/scanport/g' | lolcat ")
        f.write('")')
        f.close()
        os.system('python fast.py')
    elif (sys.argv[1] == '-SV' or sys.argv[1] == '-sv'):
        print("Starting scanport v1.01 at",current_time.strftime("%X"))
        f = open("version.py","w") 
        f.write("import os\n")
        f.write("os.system(")   
        f.write('"')
        f.write("nmap -sV ")
        f.write(target)
        f.write(" | sed '1d' | sed 's/Nmap/scanport/g' | sed '$d' | sed '$d' | lolcat ")
        f.write('")')
        f.close()
        os.system('python version.py')
    elif (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        print("this is help memu")
    elif (sys.argv[1] == '-P' or sys.argv[1] == '-p'):
        print("Starting scanport v1.01 at",current_time.strftime("%X"))
        print("scanning target :", target)
        print("|--------|---------|---------")
        print("|  PORT  |  STATE  |  SERVICE")
        print("|--------|---------|---------")
        l=len(sys.argv)
        for i in range(3, l):
            j= int(sys.argv[i])
            thread = threading.Thread(target=scan_port1, args=(j,))
            thread.start()
    elif (sys.argv[1] == '-RNG' or sys.argv[1] == '-rng'):
        start_port=int(sys.argv[3])
        end_port=int(sys.argv[4])
        print("Starting scanport v1.01 at",current_time.strftime("%X"))
        print("scanning target :", target)
        print("|--------|---------|---------")
        print("|  PORT  |  STATE  |  SERVICE")
        print("|--------|---------|---------")
        for port in range(start_port, end_port + 1):
            thread = threading.Thread(target=scan_port, args=(port,))
            thread.start()
    if __name__ == "__main__":
	    notification.notify(
		    title= "portscan compleated",
            message= target, 
		    timeout=5
	)
