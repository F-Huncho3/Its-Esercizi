#8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.

messages : list[str] = ["Ciao bella!", "Come stai?", "Ha vinto la roma", "Gino è calvo"]

#def show_messages ( lista:list): 
    #for elements in lista:
        #print (elements)

#show_messages(messages)

def send_messages (lista:list ):
    messages_to_delete:list = lista[:]
    sent_messages:list = []
    for elements in lista:
        print (elements)
        sent_messages.append(elements)
        
    
    while len(lista) >=1:
        #del lista[::1]
        lista.pop(len(lista)-1)


    

        
        
    print (f"The messages you sent are {sent_messages}")

send_messages(messages)
print (f"The original list was {messages}")

    


