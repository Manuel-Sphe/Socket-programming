from socket import *
import threading

serverName = gethostbyname(gethostname())
#serverPort = random.randint(1024,49151)
serverPort = 13000

clientSocket = socket(AF_INET, SOCK_DGRAM)
ADDR = (serverName, serverPort)
print("<<Welcome to chat2Go>>")

LOGIN = "L"
SEND = "S"
EXIT ="Q"



def login():
    # user input
    name = input("Enter your username :\n>")
    packet = LOGIN + "|"+name
    clientSocket.sendto(packet.encode(),(serverName,serverPort))
    
    # S|message|destanation
    
def send():
    prompt = input(f"Enter {SEND} SEND) or {EXIT} to quit: ")
    prompt = prompt.lower()
    destination = input("Enter your friend's name :\n>")
    while True:
        text = input("typing...>")
        packet = SEND+"|"+text+"|"+destination 
        clientSocket.sendto(packet.encode(),(serverName,serverPort))
    
        
        
    pass

def recieve():
    while True:
        packet = clientSocket.recvfrom(2048)
        print(packet[0].decode())
    pass

x = threading.Thread(target=login)
s =  threading.Thread(target=send)
r = threading.Thread(target=recieve)



x.start()
s.start()
r.start()


# make twoo threads

