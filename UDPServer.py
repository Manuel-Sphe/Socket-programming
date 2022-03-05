from socket import *
serverPort = 13000
serverSocket = socket(AF_INET, SOCK_DGRAM)

welcome = "Welcome "
host = gethostbyname(gethostname())

serverSocket.bind(('', serverPort))
print("The server is ready to receive")

def sign_UP(name,pass_word):
    '''Adding a new user to the database'''
    file = open("users.txt","a+")
    su="Signing you up..."
    serverSocket.sendto(su.encode(),clientAddress)

    confirm = "Confirm your password:>"
    serverSocket.sendto(confirm.encode(),clientAddress)
    confirm = serverSocket.recvfrom(2048)
    if(pass_word==confirm[0].decode()):
        file.write(name+","+pass_word+"\n")
    file.close()

def verify(name,password):
    flag = False
    f = open("users.txt","r")
    for line  in f:
        s = line.split(",")
        if(name==s[0] and password == s[1]):
            flag = True
    f.close()
    return flag

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Recieved from :",clientAddress[0])
    # get the Y or N
    modifiedMessage = message.decode().upper()
    if(modifiedMessage == 'Y'):
        serverSocket.sendto(welcome.encode(),clientAddress)
        n = "Enter User Name (char and numbers):"
        serverSocket.sendto(n.encode(),clientAddress)
        name = serverSocket.recvfrom(2048)

        pw = "Enter your password:"
        serverSocket.sendto(pw.encode(),clientAddress)
        pass_word = serverSocket.recvfrom(2048)
        
        log_in ="Logged in...."
        if(verify(name[0].decode(),pass_word[0].decode())):
           ## print("Logged in .....")
            serverSocket.sendto(log_in.encode(),clientAddress)
        else:
            log_in = "Sorry Wrong Username or password Try again"
            serverSocket.sendto(log_in.encode(),clientAddress)
            #name = input("Enter User Name (char and numbers):\n>")
            #pass_word = input("Enter your password:\n>")
            
    elif(modifiedMessage == 'N'):
        #name
        n = "Enter User Name (char and numbers):"
        serverSocket.sendto(n.encode(),clientAddress)
        name = serverSocket.recvfrom(2048)

        #password
        p ="Enter your password:"
        serverSocket.sendto(p.encode(),clientAddress)
        pass_word = serverSocket.recvfrom(2048)
    

        sign_UP(name[0].decode(),pass_word[0].decode())

    
   # serverSocket.sendto(modifiedMessage.encode(), clientAddress)


    #serverSocket.close()
