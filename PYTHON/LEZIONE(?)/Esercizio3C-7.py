
testa = 0

croce = 0

percentuale_testa:float = 0,00
percentuale_croce:float = 0.00

i = 1
while i <= 8:
    lancio:str = str(input(f"Inserisci il risultato del lancio {i} "))

    match lancio:

        case "c"|"C":

            croce += 1

            i += 1

        case "t"|"T":

            testa += 1

            i += 1

        case _:

            print ("Errore, lancio non valido, riprovare")



percentuale_croce = (croce/8)*100.00
percentuale_testa = (testa/8)*100.00



    
  
print (f"Totale testa: {testa}")
print (f"La percentuale di testa è {percentuale_testa:.2f}%")
        
print (f"Totale croce: {croce}")
print (f"La percentuale di croce è {percentuale_croce:.2f}%")