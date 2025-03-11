#Esercizio 3C-9. Scrivere un programma in Python che permetta all'utente di inserire le coordinate di un punto (x, y) e salvi le coordinate inserite in una tupla. Utilizzare il  match statement per determinare la sua posizione del punto inserito nel piano cartesiano:

x:int = int(input("Inserisci il punto X -->"))
y:int = int(input("Inserisci il punto Y -->"))

punti_cartesiani:tuple = (x,y)

match punti_cartesiani:

    case (0,0):

        print("Il punto si trova all'origine degli assi")

    case (0,y):

        print("Il punto si trova sull'asse Y")

    case (x,0):

        print("Il punto si trova sull'asse X")

    case (x,y) if x>0 and y>0:

        print("Il punto si trova nel primo quadrante")

    case (x,y) if x<0 and y>0:

        print("Il punto si trova nel secondo quadrante")

    case (x,y) if x<0 and y<0:

        print ("Il punto si trova nel terzo quadrante.")

    case (x,y) if x > 0 and y < 0:

        print ("Il punto si trova nel quarto quadrante.")

    case _:
        print("Il punto è sconosciuto")