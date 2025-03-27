#TARTARUGA E LEPRE

#Percorso (lista) da 1 a 70 posizioni. Due variabili che rappresentano gli animali in gara. Quadrato 1 = partenza, Quadrato 70 = fine.

#Ogni variabile ha varie "mosse" con differenti percentuali di riuscita, ognuna di esse causerà uno spostamento nella lista.

#Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i, nell'intervallo 1 ≤ i ≤ 10. Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5, una "scivolata" quando 6 ≤ i ≤ 7, o un "passo lento" quando 8 ≤ i ≤ 10. Usate una tecnica simile per muovere la lepre seguendo le sue regole

#La lista dovrà contenere "T" e "L" nelle rispettive posizioni del percorso.

# Tartaruga:
   # - Passo veloce (50% di probabilità): avanza di 3 quadrati.
    #- Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
    #- Passo lento (30% di probabilità): avanza di 1 quadrato.

#- Lepre:
    #- Riposo (20% di probabilità): non si muove.
    #- Grande balzo (20% di probabilità): avanza di 9 quadrati.
    #- Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
    #-  Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
    #- Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.


#Requisiti del Codice:
#- Utilizzare il modulo random per la generazione dei numeri casuali.
#- Definire e utilizzare:
    #- una funzione per visualizzare le posizioni sulla corsia di gara,
    #- una funzione per calcolare la mossa della tartaruga,
    #- una funzione per calcolare la mossa della lepre.
#- Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia d




import random

#Inizializzo le variabili:

lunghezza_percorso = 70

posizione_tartaruga = 0

posizione_lepre = 0

indice = 0

#Creo la funzione Percorso

def funzione_percorso(posizione_tartaruga,posizione_lepre):

    #Visualizziamo il percorso.

    percorso = ["_"]* lunghezza_percorso

    #Mettiamo una condizione nella funzione per evitare che le posizioni vadano fuori dal range

    if posizione_tartaruga > lunghezza_percorso - 1:
        posizione_tartaruga = lunghezza_percorso - 1
    if posizione_lepre > lunghezza_percorso - 1:
        posizione_lepre = lunghezza_percorso - 1

    #Se entrambi gli animali sono nella stessa posizione li stampiamo in questo modo

    if posizione_lepre == posizione_tartaruga:

        percorso[posizione_tartaruga] = "T - L"

    #Casistica Default

    else:

        percorso[posizione_tartaruga] = "T"

        percorso[posizione_lepre] = "L"

    

   #Stampa percorso senza gli apici

    print("".join(percorso))



    
#Definiamo la funzione delle mosse della lepre
#Ci mettiamo come parametro la posizione attuale in modo da riuscire ad aggiornarla in seguito con la nuova.

def mossa_lepre (posizione_lepre):

    #creiamo una variabile randomica che detterà le mosse

    mossa = random.randint(1,10)

    match mossa:
        
        case mossa if 1<= mossa <= 2:

            #non si muove


            pass
    

        case mossa if 3 <= mossa <= 5:


            posizione_lepre += 1

        case mossa if 6 <= mossa <= 7:

            if posizione_lepre >= 12:
                
                posizione_lepre -= 12

            else:

                posizione_lepre = 0

        case mossa if 8 <= mossa <= 9:

            posizione_lepre +=9

        case 10:

            if posizione_lepre >= 2:

                posizione_lepre -= 2

            else:

                posizione_lepre = 0
    
    #Utilizziamo il return per permettere al dato di ritornare ed aggiornarsi.
    return posizione_lepre

#Definiamo la funzione delle mosse della tartaruga.

def mossa_tartaruga (posizione_tartaruga):

    mossa = random.randint(1,10)

    match mossa:

        case mossa if 1 <= mossa <= 5:

            if posizione_tartaruga <= 67:

                posizione_tartaruga += 3

            else:

                posizione_tartaruga = 70

    
        case mossa if 6 <= mossa <= 7:

            if posizione_tartaruga >= 6:
                
                posizione_tartaruga -= 6

            else:

                posizione_tartaruga = 0

        case mossa if 8 <= mossa <= 10:

            if posizione_tartaruga < 69:

                posizione_tartaruga += 1

            else:

                posizione_tartaruga = 70

        case 10:

            if posizione_tartaruga >= 2:

                posizione_tartaruga -= 2

            else:

                posizione_tartaruga = 0

    #Ritorniamo la posizione per aggiornarla e renderla globale

    return posizione_tartaruga


#Come condizione del ciclo while mettiamo che nessuno dei due animali deve superare len(percoso) - 1 per non uscire dal range.
while posizione_tartaruga < lunghezza_percorso - 1 and posizione_lepre <  lunghezza_percorso - 1:
    
    #Nel while dobbiamo rimettere le variabili-posizioni con le funzioni all'interno per fare in modo di aggiornarle ad ogni iterazione. 
    posizione_lepre = mossa_lepre (posizione_lepre )
    posizione_tartaruga = mossa_tartaruga(posizione_tartaruga )
    
    funzione_percorso(posizione_tartaruga,posizione_lepre)

#Fine del percorso.
print ("Gara Terminata\n")

if posizione_tartaruga>posizione_lepre:
        print("Turtle wins")
elif posizione_lepre > posizione_tartaruga:
    print("Hore wins")
else:
    print("It's a tie")

    
    
    

        

        
            






        




            


    




