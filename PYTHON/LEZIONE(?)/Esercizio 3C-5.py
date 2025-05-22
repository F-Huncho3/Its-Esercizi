
dati_utente:dict = {}


x = (input("Inserisci il tuo nome "))
ruolo = (input("Inserisci il ruolo "))
age:int = int(input("Inserisci il'età "))
#Mando in output i dati da inserire, con un "cast" per la variabile age in modo da renderlo un integer forzato


dati_utente[ruolo] = age

#Metto le variabili al posto di chiave e valore per cambiarli a seconda dell'input


match dati_utente:

    case {"Admin": age}:

        print (f"Ciao {x}. Hai Accesso completo a tutte le funzionalità")

    case {"Moderatore": age}:

        print (f"Ciao {x}. Puoi gestire i contenuti ma non modificare le impostazioni.")

    case {"Utente":age}:
        #Metto una condizione per leggere il valore di age all'interno del match, in base al quale avrò due output diversi.
        if age >= 18:
            print (f"Ciao {x}. Accesso standard a tutti i servizi.")
            
        else:
            print (f"Ciao {x}. Accesso limitato! Alcune funzionalità sono bloccate.")

    case {"Ospite": age}:

        print (F"Ciao {x}. Accesso ristretto! Solo visualizzazione dei contenuti.")

    case _: 

        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")

    

    

    

       

