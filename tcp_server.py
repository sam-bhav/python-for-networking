#!/usr/bin/python3

# how to create a tcp server in python3 

# creating a socket

import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#specifying port and getting hostname 
# using function rather than hard coding, host='192.168.1.250'
host = socket.gethostbyname()
port = 4444

# binding host and port
serversocket.bind((host,port))

#creating a listner
serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
        #converting the ip address to string
    print("Recieved connection from" % str(address))

    message = 'Thank you for connecting to the server' + "/r/n"
    #sending message back to the client without encoding
    # clientsocket.send(message)
    
    #with encoding
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()


