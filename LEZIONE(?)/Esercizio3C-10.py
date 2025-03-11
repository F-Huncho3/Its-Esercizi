#Esercizio 3C-10. Scrivere un programma in Python che permetta all'utente di inserire una data (giorno e mese espressi in forma numerica), salvi la data in una tupla e utilizzi un match statement per verificare se la data corrisponde a una festività o a un evento speciale:

giorno:int = int(input("Inserisci il numero del giorno -->"))
mese:int = int(input("Inserisci il numero del mese -->"))

data:tuple = (giorno,mese)

#Inserisco un IF per verificare che i numeri inseriti siano corretti.



    #Se i numeri inseriti sono corretti allora effettuo il match case.
     
match data:
    case (giorno,mese) if giorno>31 or mese >12 or giorno <= 0 or mese <= 0:
        print("La data inserita non è corretta")
            
    case (1,1):
            
        print("Capodanno")

    case (14,2):

        print("San Valentino")

    case (2,6):
            
        print("Festa della Republica italiana")

    case (15,8):

        print("Ferragosto")

    case (31,10):
            
        print("Halloween")

    case (25,12):

        print("Natale")

    case (giorno,2) if giorno >28:
             
        print("Febbraio ha solo 28 giorni")
        
    case (giorno,mese) if giorno >30 and mese ==11 or mese ==4 or mese ==6 or mese == 9:
             
        print("Il mese registrato non ha più di 30 giorni") 
    
    case _:

        print("Nessuna festività importante in questa data")

