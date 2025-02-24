totale:float = 0

media:int = 0

numeri_totaliinteri:int = 0

numero_grande:float = -100000000000000

numero_piccolo:float = 100000000000000

while True:
    x:float = float(input("Inserire dei numeri positivi per inizializzare o continuare il programma (Nel caso di numero negativo il programma verrà terminato. Inserire->)"))

    if x < 0:
        print ("Hai inserito un numero negativo, il programma verrà terminato con i valori richiesti.")
        break

    if x.is_integer():
        
        totale+=x

        numeri_totaliinteri += 1


    if x > numero_grande:

        numero_grande = x 

    elif x < numero_piccolo:

        numero_piccolo = x 


media = totale / numeri_totaliinteri
print (f"La media dei numeri è {media}")

print (f"Il numero più grande è {numero_grande}")
print (f"Il numero più piccolo è {numero_piccolo}")
 
 