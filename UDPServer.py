from socket import *
import threading
import time

serverPort = 13000
serverSocket = socket(AF_INET, SOCK_DGRAM)

welcome = "Welcome "
host = gethostbyname(gethostname())

serverSocket.bind((host, serverPort))

def unmusk(bytes):
    return bytes.decode()

def musk(bytes):
    return bytes.encode()
    
def sign_UP(name,pass_word):
    '''Adding a new user to the database'''
    file = open("users.txt","a+")
    su="Signing you up..."
    serverSocket.sendto(su.encode(),clientAddress)

    confirm = "Confirm your password:>"
    serverSocket.sendto(confirm.encode(),clientAddress)
    confirm = serverSocket.recvfrom(2048)
    if(pass_word==confirm[0].decode()):
        file.write((name+","+pass_word)+"\n")
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

def respond(text,client_address):
    serverSocket.sendto(text.encode(),client_address)
    pass

def handle_client(data,client_adrress):
    '''Handle the client'''
    #handle the rerequent
    # the first thing we are expecting is the 'Y' or 'N'
    print("I'm ready to communicate now")

    message = data.decode()
    if(message=='Y'):
        respond(welcome,client_adrress)
        n = "Enter User Name (char and numbers):"
        respond(n,client_adrress)
        name = serverSocket.recvfrom(2048)
        
        pw = "Enter your password:"
        respond(pw,client_adrress)
        pass_word = serverSocket.recvfrom(2048)
        
        
        log_in = "Logged in...."
        if(verify(unmusk(name[0]),unmusk(pass_word[0]))):
            #print Logged in 
            respond(log_in,client_adrress)
        else:
            log_in ="Sorry Wrong Username or password Try again"
            respond(log_in,client_adrress)
        time.sleep(0.5)
    elif(message == 'N'):
        #name 
        n = "Enter User Name (char and numbers):"
        respond(n,client_adrress)
        name = serverSocket.recvfrom(2048)
        
        p = "Enter your password"
        
        respond(p,client_adrress)
        
        pass_word = serverSocket.recvfrom(2048)
        
        sign_UP(unmusk(name[0]),unmusk(pass_word[0]))
        
    # now we need to handle the message sending

    pass
while True:
    try:
        try:
            message, clientAddress = serverSocket.recvfrom(2048)
            handle_client(message,clientAddress)
            my_thread = threading.Thread(target=handle_client,args=(message,clientAddress))
            my_thread.start()
            print("Message sent now !!!")
        except OSError:
            print("Failed to read message from client")
            break
            
    except KeyboardInterrupt:
        print("Shutting down server")
        serverSocket.close()
