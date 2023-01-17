#!/usr/bin/python

import socket

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#make sure the client knows ip add of the server
host = socket.gethostbyname()
port=4444

clientsocket.connect((host,port))

#max amount of data using TCP 1024
message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))

