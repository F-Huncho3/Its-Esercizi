#8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.

messages : list[str] = ["Ciao bella!", "Come stai?", "Ha vinto la roma", "Gino è calvo"]

messages_2 : list[str] = ["Ciao bella!", "Come stai?", "Ha vinto la roma", "Gino è calvo"]

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

send_messages(messages_2)
print(f"The copied list is {messages_2}")
print (f"The original list was {messages}")