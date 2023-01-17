#!/usr/bin/python3

#creating a port scanner 

import socket

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#some ports take longer so dont always set time out
s.settimeout(5)
#hard code
# host="137.74.187.100"

#make user enter
host=input("Target IP: ")
port=int(input("Target Port: "))

def portScanner(port):
    if s.connect_ex((host,port)):
        print("Port Closed")
    else:
        print("Port Open")

portScanner(port)