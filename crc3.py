#!/usr/bin/python3

from termcolor import colored # for colour output
import time # for progress bar
import sys # for some writing func. in progressbar
import random #for making random recieving data
import os # for clearing screen
import keyboard # for exitting part

sender_raw_data = input("Enter the sender data : ") # input send data in any format

divisor = input("\nEnter the divisor : ") # input divisor in binary

sender_data = ("".join(f"{ord(i):08b}" for i in sender_raw_data)) # convert sender_raw_data to binary 

def xor(a, b): # returns xor output
	x = ""
	for i in range(len(b)):
		x = x+str(int((int(a[i]) and not int(b[i])) or (int(b[i]) and not int(a[i]))))
	return x

def sender_part(sd, d): # returns the final value of sender_data
	sd  = sd+"000"
	jjj = "0" * len(d)
	sdt = out = ""
	for j in range(len(sd)-len(d)+1	):
		if j == 0:
			for k in range(0, len(d)):
				sdt+=sd[k]
			part=xor(sdt,d)
			for ii in range(1, len(d)):
				out += part[ii]
			if j != len(sd)-len(d):
				out += sd[len(d)+j]
			part = out
		else:
			if part[0] != "0":
				part = xor(part, d)
			else:
				part = xor(part, jjj)

			for ii in range(1, len(d)):
				out += part[ii]
			if j != len(sd)-len(d):
				out += sd[len(d)+j]
			part = out
		sdt = out = ""
	return part


def progressbar(it, prefix="", size=60, file=sys.stdout): # progress bar animation
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s]%i/%i%s\r" % (colored(prefix,'green'), colored("#"*x,'magenta'), colored("."*(size-x),'white'), j, count,colored(" %",'yellow')))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

# making a random data .. same length of sender_data
r_r = ""
for i in range(0, len(str(sender_data))):
	r_r += random.choice(['0','1'])


def reciever_part(rd, d): # calculates the reciever_data and returns the final value
	rd  += sent
	rjj = "0" * len(d)
	rdt = ""
	rout = ""
	for j in range(len(rd)-len(d)+1	):
		if j == 0:
			for k in range(0, len(d)):
				rdt=rdt+rd[k]
			rpart=xor(rdt,d)
			for ii in range(1, len(d)):
				rout += rpart[ii]
			if j != len(rd)-len(d):
				rout += rd[len(d)+j]
			rpart = rout
		else:
			if rpart[0] != "0":
				rpart = xor(rpart, d)
			else:
				rpart = xor(rpart, rjj)

			for ii in range(1, len(d)):
				rout += rpart[ii]
			if j != len(rd)-len(d):
				rout += rd[len(d)+j]
			rpart = rout
		rout = ""
		rdt = ""
	return rpart



def checker(x): # checks the final output of reciever_part
	if x == "000":
		# successfull print
		print (colored("\n ... The Check Was Successful ... \n",'green'))
		print (colored("Sent Data : ",'cyan'), colored(sender_raw_data,'white'),colored("\nSent DataPackets : ",'yellow'),colored(sender_data,'blue'),colored("\n\nRecieved Data : ",'cyan'), colored(sender_raw_data,'white'),colored("\nRecieved DataPackets : ",'yellow'),colored(reciever_data,'blue'))
		print (colored("\nThere Was NO DATA LOSS, Data Packet Accepted\n",'green'))
	else :
		# unsuccessful print
                print (colored("\n ... The Check Was Unsuccessful ... \n",'red'))
                print (colored("Sent Data : ",'cyan'), colored(sender_raw_data,'white'),colored("\nSent DataPackets : ",'yellow'),colored(sender_data,'blue'),colored("\n\nRecieved Data : ",'red'),(''.join([chr(int(x, 2)) for x in sender_data])),colored("\nRecieved DataPackets : ",'red'),colored(reciever_data,'green'))
                print (colored("\nThere Was SOME DATA LOSS, Data Packet Rejected\n",'red'))


os.system('clear') # clears the screen

# print sender side info
print (colored("\nTo Be Sent Data : ",'cyan'),colored(sender_raw_data,'white'),"\n")
print(colored("\nto Be Sent DataPackets : ",'yellow'),colored(sender_data,'blue'),"\n\n")

sent = sender_part(sender_data, divisor) # gets the sender_part's last value

# progress bar 
for i in progressbar(range(100), "Sending Data : ", 40):
	time.sleep(0.1)
print("\n")

reciever_data = random.choice([sender_data,r_r]) # randomly chooses if the reciever will get good or corrupt data

checker(reciever_part(reciever_data, divisor)) # finally checks and outputs the result

#exit program
print("Enter 'shift+x' to exit")
keyboard.wait('shift+x')
os.system('clear')
sys.exit()
