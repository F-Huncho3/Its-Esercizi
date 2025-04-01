#INTRODUZIONE SULLE FUNZIONI RICORSIVE

#Definiamo la funzione
def recursiveCountdown (n:int) -> None:

    if n < 0:

        #Partiamo dal primo caso(il più semplice) di possibili errori, nel quale la funzione deve essere bloccata subito.

        print("ERRORE")

    elif n == 0:
        
        #Andiamo a controllare se n è uguale a 0 per fermare la funzione nel caso venga messo tra i parametri o se arriviamo a 0.

        print(0)

    else:

        #Inseriamo la parte ricorsiva della funzione che, solo dopo aver stampato n, richiamerà se stessa modificando il parametro con n - 1. Da qui la funzione ripartirà e attuerà le istruzioni passando per le varie possibilità fino a quando una delle condizioni scelte non viene soddisfatta.

        print(n)

        recursiveCountdown(n-1)






def recursiveSum(n:int) -> int:
# n is negative
    if n < 0:
        print("Error! Inserted number is negative!")
        return None
# if n = 0 recursive process must be stopped
    elif n == 0:
        return 0
# if n is positive, compute recursive sum
    else:
        print (n)
        return int(n + recursiveSum(n-1))
        
    
    
print(recursiveSum(8))
