#!/usr/bin/python3

import socket

def banner(ip,port):
    s = socket.socket
    s.connect((ip,int(port)))
    s.settimeout(5)
    # print(s.recv(1024))
    print(str(s.recv(1024)))


def main():
    ip = input("Emter IP: ")
    port = str(input("Specify the Port: "))
    banner(ip,port)

main()