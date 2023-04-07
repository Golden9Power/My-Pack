import time
import sys
import os
import time
from datetime import datetime
from time import sleep
def printLow(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.03)

    
C = '\033[96m'
W ='\033[1m'
w ='\033[5m'
R = '\033[91m'
O ='\033[4m'
y = '\033[93m'
B = '\033[94m'
G = '\033[92m'
E = '\033[0m'
g = '\033[32m' 
r = '\033[31m' 
bo = '\033[36m' 
p = '\033[35m'
dd = '\033[34m' 
now = datetime.now()
dd = str(now.day) #Get Day
mm = str(now.month) #Get Month
yyyy = str(now.year) #Get year
hour = str(now.hour) #Get hour
mi = str(now.minute) #Get minute
ss = str(now.second) #Get Second
printLow(" " + W + "Hello" + g + "Welcome" + B +" Pack")
printLow("  " + W + g + "[1]" + y + "DDosSite" + E)
printLow("  " + W + g + "[2]" + R + W + "Create Phone " + E)
printLow("  " + W + g + "[3]" + bo + W + "SMS Bomber" + E)
printLow("  " + W + g + "[4]" + B + W + "Downloder" + E)
while True:
	k = input("\n. " + W + g + "Enter" + bo + "Number:" + E)
	if k == '1':
		os.system("clear")
		import DDosSite
		close()
	elif k == '2':
		os.system("clear")
		import CreatePhone
		close()
	elif k == '3':
		import My_sms_Bomber
		close()
	elif k == '4':
		os.system("clear")
		import Downloder
	
	elif k:
		break