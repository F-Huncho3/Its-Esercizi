while True:

    x :str = str(input("Inserisci una parola, se vuoi terminare inserisci 'fine'"))

    if x == "fine": 
        print ("Hai terminato il programma")
        break

    if x[0] == x[-1]:
        print (f"La parola {x} inizia e finisce con la stessa lettera")
    else:
        print (f"La parola {x} inizia e finisce lettere diverse")

    
    