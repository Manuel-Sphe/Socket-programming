import tkinter

frame = tkinter.Tk()

frame.title("CHAT APP")

frame.geometry('250x250')
frame.configure(bg = "blue")


def Chatpage():
    Page1 = tkinter.Tk()
    Page1.title("CHAT ROOM")
    Page1.geometry("400x400")
    Page1.configure(bg="blue")
    messages= tkinter.Frame(Page1)
    scrollbar = tkinter.Scrollbar(messages)
    messagelist = tkinter.Listbox(messages, height=20, width=50, yscrollcommand=scrollbar.set) #List of all messages including previous messages
    scrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
    messagelist.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    messagelist.pack()    
    messages.pack()
    
    printButton = tkinter.Button(Page1,text = "Send") #Send message button
    printButton.pack(side=tkinter.BOTTOM)
    inputtxt = tkinter.Text(Page1,height = 2,width = 20) #Text input
    inputtxt.pack(side=tkinter.BOTTOM)
#List of contacts to chat to individually    
def ContactsList():
    Page2 = tkinter.Tk()
    Page2.title("List of Contacts")
    Page2.geometry("250x250")
    Page2.configure(bg = "blue")
    contact1 = tkinter.Button(Page2, text = "Example Contact", command = Chatpage)
    contact1.grid(row = 1, column = 1)

    
#HomePage
contactButton = tkinter.Button(frame, text = "Contacts", height = 1, width = 14, command = ContactsList)
contactButton.grid(row = 1, column = 1)

#group chat with all contacts
groupchat = tkinter.Button(frame, text = "Create Group Chat", command = Chatpage)
groupchat.grid(row = 2, column =1)

frame.mainloop()