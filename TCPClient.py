#!/usr/bin/python3
from socket import *
#from time import clock
serverName = 'localhost'
serverPort = 12001
while 1:
    command = input('Enter Command:')
    if command == "quit":
        break
	else:
        clientSocket = socket(AF_INET,SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(bytearray(command.encode("utf-8")))
        #startTime = clock()
        response = clientSocket.recv(1024)
        response = response.decode("utf-8")
        print("Server response:"+response)
        clientSocket.close()
        if command == "server exit":
            break
print("Exited Client")