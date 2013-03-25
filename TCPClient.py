#!/usr/bin/python3
from socket import *
#from time import clock
serverName = 'localhost'
serverPortBase = 13010
command = "getSocket"
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName, serverPortBase))
clientSocket.send(bytearray(command.encode("utf-8")))
#startTime = clock()
response = clientSocket.recv(1024)
response = response.decode("utf-8")
print("Session socket:"+response)
serverPort = int(response)
while 1: 
    command = input('Enter Command:')   
    if command == "quit":
        clientSocket = socket(AF_INET,SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        command = "releaseSocket " + str(serverPort)
        clientSocket.send(bytearray(command.encode("utf-8")))
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