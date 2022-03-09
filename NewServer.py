from email import message
from socket import *
import threading
import time

serverPort = 13000
serverSocket = socket(AF_INET, SOCK_DGRAM)

welcome = "Welcome "
host = 'localhost'

serverSocket.bind(('', serverPort))

clients = {} # for storing th clients

def getAddresses(userName):
    return clients.get(userName)  # this should return the client address


    
# you enter your user name 
print("[SERVER] Running")
while True:
    message,clientAddress = serverSocket.recvfrom(2048) 
    ls = (message.decode()).split("|")
    
    #print(ls)
    if( ls[0] == 'L'):
        print(f"[SERVER] {ls[1]} is connected")
        clients[ls[1]] = clientAddress
    elif ls[0] == 'S' and len(clients.keys())>=2:
        #you pass the name of reciepient
        serverSocket.sendto(ls[1].encode(),clients.get(ls[2]))
        print("Done!!!")
    #elif (ls[0] == 'S' and len(clients.keys())>2):
     #   print(ls[2])
      #  print(getAddresses(ls[2]))
        #serverSocket.sendto(ls[1].encode(),getAddresses(ls[2]))
      
    #print(clients)
    
    
 
    
    
    
   
    
    
    
    
    
