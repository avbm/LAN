#!/usr/bin/python3
from socket import *
import datetime
serverPort = 12001
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
weekday = ("Mon","Tue","Wed","Thu","Fri","Sat","Sun")
month = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
print("The server is ready to recieve")
while 1:
    connectionSocket, addr = serverSocket.accept()
    command = connectionSocket.recv(1024)
    print('Recieved: ', command)
    command = command.decode("utf-8")
    #print(command)
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
    elif command == "server exit":
        response = "TCPServer exiting"
        connectionSocket.send(bytearray(response.encode("utf-8")))
        connectionSocket.close()
        break
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
serverSocket.close()
