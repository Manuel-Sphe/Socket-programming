from socket import *
#print((gethostname())
serverName = '137.158.58.16'
serverPort = 12000

clientSocket = socket(AF_INET,SOCK_DGRAM)

message = input("Enter lower case sentence :")

ADDR = (serverName, serverPort)
clientSocket.sendto(message.encode(),(ADDR))

ADDR = (serverName, serverPort)
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress =clientSocket.recvfrom(2048)
print(modifiedmessage.decode())

clientSocket.close()
