from socket import *
serverName = gethostbyname(gethostname())
serverPort = 13000

clientSocket = socket(AF_INET, SOCK_DGRAM)
ADDR = (serverName, serverPort)
print("<<Welcome to chat2Go>>")
message = input("Already has an accout ?(Y or N) : ")
message = message.upper()

if(message == 'Y'):
    clientSocket.sendto(message.encode(),ADDR)
    #welcome messgae
    welcome = clientSocket.recvfrom(2048)
    print(welcome[0].decode(),end="")
    
    #Enter user name 
    prompt1  = clientSocket.recvfrom(2048)
    print(prompt1[0].decode())
    name = input()
    clientSocket.sendto(name.encode(),ADDR)
    
    #password
    prompt2 = clientSocket.recvfrom(2048)
    print(prompt2[0].decode())
    password = input() 
    clientSocket.sendto(password.encode(),ADDR)

    #logged in massage
    log  = clientSocket.recvfrom(2048)
    print(log[0].decode())

elif(message == 'N'):
    #name 
    clientSocket.sendto(message.encode(),ADDR)
    name = clientSocket.recvfrom(2048)
    print(name[0].decode())
    n = input()
    clientSocket.sendto(n.encode(),ADDR)

    #password
    pass_w = clientSocket.recvfrom(2048)
    print(pass_w[0].decode())
    p =input()
    clientSocket.sendto(p.encode(),ADDR)

    #sign up
    su = clientSocket.recvfrom(2048)
    print(su[0].decode())
    
    #confirm password
    con = clientSocket.recvfrom(2048)
    print(con[0].decode())
    con_f = input()
    clientSocket.sendto(con_f.encode(),ADDR)


#modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
#print(modifiedMessage.decode())
clientSocket.close()