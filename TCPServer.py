#!/usr/bin/python3
from socket import *
import datetime
import threading
serverPort = 12000
serverSocketBase = socket(AF_INET,SOCK_STREAM)
serverSocketBase.bind(('',serverPort))
serverSocketBase.listen(1)
weekday = ("Mon","Tue","Wed","Thu","Fri","Sat","Sun")
month = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
maxClients = 5
clientSocketState = maxClients * [0]
#print(clientSocketState)
serverSocket = maxClients * [0]
for x in range(maxClients):
    serverSocket[x] = socket(AF_INET,SOCK_STREAM)
    serverSocket[x].bind(('',(serverPort+x+1)))
    serverSocket[x].listen(1) 
print("The server is ready to recieve")


def resolve_command(command,connectionSocket):
    connectionSocket = connectionSocket
    returnVal = 0
    if 1==1: #place holder in case while has to be implemented at some later time
        if command == "help":
            #enter command options and help menu here
            response = """This is a list of available server commands
            1. help : brings up this menu
            2. server exit : exits both server and client processes
            3. date : gives current date/time in UTC
            4. echo : returns the string after echo
            5. upper : converts input string to upper case
            6. lower : converts input string to lower case
            7. reverse : reverses input string"""
            connectionSocket.send(bytearray(response.encode("utf-8")))
            connectionSocket.close()
        elif command == "getSocket":
            response = str(clientSocketState.index(0) + 1 + serverPort)
            clientSocketState[clientSocketState.index(0)] = 1
            connectionSocket.send(bytearray(response.encode("utf-8")))
            connectionSocket.close()
        elif command.split()[0] == "releaseSocket":
            response = " ".join(command.split()[1:]) #deletes the preceding command name
            tempSocket = int(response)
            clientSocketState[tempSocket - 1 - serverPort] = 0 
            #response = "socket clear"
            #print(response)
            #connectionSocket.send(bytearray(response.encode("utf-8")))
            connectionSocket.close()
        elif command == "server exit":
            response = "TCPServer exiting"
            connectionSocket.send(bytearray(response.encode("utf-8")))
            connectionSocket.close()
            returnVal = 1
        elif command == "date":
            now = datetime.datetime.utcnow()
            response = weekday[now.weekday()]+" "+month[now.month-1]+" "+str(now.day)+" "\
            +str(now.hour)+":"+str(now.minute)+":"+str(now.second)+" UTC "+str(now.year)
            #print(response)
            connectionSocket.send(bytearray(response.encode("utf-8")))
            connectionSocket.close()
        elif command.split()[0] == "echo":
            response = " ".join(command.split()[1:]) #deletes the preceding command name
            #print(response)
            connectionSocket.send(bytearray(response.encode("utf-8")))
            connectionSocket.close()
        elif command.split()[0] == "upper":
            response = " ".join(command.split()[1:]) #deletes the preceding command name
            response = response.upper()
            #print(response)
            connectionSocket.send(bytearray(response.encode("utf-8")))
            connectionSocket.close()
        elif command.split()[0] == "lower":
            response = " ".join(command.split()[1:]) #deletes the preceding command name
            response = response.lower()
            #print(response)
            connectionSocket.send(bytearray(response.encode("utf-8")))
            connectionSocket.close()
        elif command.split()[0] == "reverse":
            response = " ".join(command.split()[1:]) #deletes the preceding command name
            response = response[::-1]
            #print(response)
            connectionSocket.send(bytearray(response.encode("utf-8")))
            connectionSocket.close()
        else:
            response = "Unknown Command"
            connectionSocket.send(bytearray(response.encode("utf-8")))
            connectionSocket.close()
    return returnVal 

class serverThread (threading.Thread):
    def __init__(self, threadID):
        self.threadID = threadID
        threading.Thread.__init__(self)
    def run(self):
        while 1:
            connectionSocket, addr = serverSocket[self.threadID].accept()
            command = connectionSocket.recv(1024)
            print('Recieved: ', command)
            command = command.decode("utf-8")
            #print(command)
            returnVal = resolve_command(command,connectionSocket)
            if(returnVal==1):
                break


#initializing threads for clients
for x in range(maxClients):
    temp = serverThread(x)
    temp.start()



while 1:
    connectionSocket, addr = serverSocketBase.accept()
    command = connectionSocket.recv(1024)
    print('Recieved: ', command)
    command = command.decode("utf-8")
    #print(command)
    returnVal = resolve_command(command,connectionSocket)
    if(returnVal==1):
        break
for x in range(maxClients):
    serverSocket[x].close()
serverSocketBase.close()


