#8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.

messages : list[str] = ["Ciao bella!", "Come stai?", "Ha vinto la roma", "Gino è calvo"]

def show_messages ( lista:list): 
    for elements in lista:
        print (elements)

show_messages(messages)