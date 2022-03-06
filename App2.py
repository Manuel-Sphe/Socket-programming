from socket import *
import tkinter as tkr

serverName = gethostbyname(gethostname())
serverPort = 13000

master = tkr.Tk()

"""Edit window"""
master.title("User Sign-in")
master.geometry("400x200")
master.configure(bg="blue")

clientSocket = socket(AF_INET, SOCK_DGRAM)
ADDR = (serverName, serverPort)


def call1():
    SignUpPage = tkr.Tk()
    SignUpPage.title("User Sign-Up")
    SignUpPage.geometry("400x200")

    tkr.Label(SignUpPage, text="Sign-Up").grid(row=0, columnspan=2)
    tkr.Label(SignUpPage, text="Email").grid(row=1)
    tkr.Label(SignUpPage, text="Password").grid(row=2)

    entry3 = tkr.Entry(SignUpPage)
    entry4 = tkr.Entry(SignUpPage, show="*")

    entry3.grid(row=1, column=1)
    entry4.grid(row=2, column=1)
    
    button3 = tkr.Button(SignUpPage, width=7, height=1, text="Sign-Up", command= lambda: call2(entry3,entry4))
    button3.grid(row=4, column=0, padx=3, pady=3)
    
def call2(ent3,ent4):
    message = "N"
    clientSocket.sendto(message.encode(),ADDR)
    name = clientSocket.recvfrom(2048)
    print(name[0].decode())
    n = ent3.get()
    print(n)
    clientSocket.sendto(n.encode(),ADDR)

    #password
    pass_w = clientSocket.recvfrom(2048)
    print(pass_w[0].decode())
    p = ent4.get()
    clientSocket.sendto(p.encode(),ADDR)

    #sign up
    su = clientSocket.recvfrom(2048)
    print(su[0].decode())
    
    #confirm password
    con = clientSocket.recvfrom(2048)
    print(con[0].decode())
    con_f = ent4.get()
    clientSocket.sendto(con_f.encode(),ADDR)

def call3(ent1,ent2):
    message = "Y"
    clientSocket.sendto(message.encode(),ADDR)
    #welcome messgae
    welcome = clientSocket.recvfrom(2048)
    print(welcome[0].decode(),end="")
    
    #Enter user name 
    prompt1  = clientSocket.recvfrom(2048)
    print(prompt1[0].decode())
    name = ent1.get()
    clientSocket.sendto(name.encode(),ADDR)
    
    #password
    prompt2 = clientSocket.recvfrom(2048)
    print(prompt2[0].decode())
    password = ent2.get()
    clientSocket.sendto(password.encode(),ADDR)

    #logged in massage
    log  = clientSocket.recvfrom(2048)
    print(log[0].decode())
    call4()
    
def call4():
    #HomePage
    frame = tkr.Tk()
    frame.title("CHAT APP")
    frame.geometry('250x250')
    frame.configure(bg = "blue")
    contactButton = tkr.Button(frame, text = "Contacts", height = 1, width = 14, command = ContactsList)
    contactButton.grid(row = 1, column = 1)
    
    #group chat with all contacts
    groupchat = tkr.Button(frame, text = "Create Group Chat", command = Chatpage)
    groupchat.grid(row = 2, column =1)

def ContactsList():
    Page2 = tkr.Tk()
    Page2.title("List of Contacts")
    Page2.geometry("250x250")
    Page2.configure(bg = "blue")
    contact1 = tkr.Button(Page2, text = "Example Contact", command = Chatpage)
    contact1.grid(row = 1, column = 1)


def Chatpage():
    Page1 = tkr.Tk()
    Page1.title("CHAT ROOM")
    Page1.geometry("400x400")
    Page1.configure(bg="blue")
    messages= tkr.Frame(Page1)
    scrollbar = tkr.Scrollbar(messages)
    messagelist = tkr.Listbox(messages, height=20, width=50, yscrollcommand=scrollbar.set) #List of all messages including previous messages
    scrollbar.pack(side=tkr.RIGHT,fill=tkr.Y)
    messagelist.pack(side=tkr.LEFT, fill=tkr.BOTH)
    messagelist.pack()    
    messages.pack()
    printButton = tkr.Button(Page1,text = "Send") #Send message button
    printButton.pack(side=tkr.BOTTOM)
    inputtxt = tkr.Text(Page1,height = 2,width = 20) #Text input
    inputtxt.pack(side=tkr.BOTTOM)    
        
    
    
tkr.Label(master, text="Sign-in", fg="white").grid(row=0, columnspan=2)
tkr.Label(master, text="Email").grid(row=1)
tkr.Label(master, text="Password").grid(row=2)

entry1 = tkr.Entry(master)
entry2 = tkr.Entry(master, show="*")

entry1.grid(row=1, column=1)
entry2.grid(row=2, column=1)

button1 = tkr.Button(master, width=7, height=1, text="Sign-Up", command = call1)
button1.grid(row=4, column=0, padx=3, pady=3)

button2 = tkr.Button(master, width=7, height=1, text="Sign-In", command = lambda: call3(entry1,entry2))
button2.grid(row=4, column=1, padx=3, pady=3)


tkr.mainloop()
    

clientSocket.close()