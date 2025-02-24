
lista_numeri:list = []
somma:int = 0
somma_dispari:int = 0 
media:int = 0
counter:int = 0

while True:
    x:int = int(input("Inserisci un numero (Inserisci 0 per terminare) "))
    
    if x < 0:
        print ("Numero inserito errato")

    elif x == 0:
        print ("Il programma è stato terminato")
        break
    else:
        lista_numeri.append(x)
        
        if x%2 == 0:
            somma += x

        else:
            somma_dispari += x
            counter += 1
            media = somma_dispari / counter



print (f"La somma dei numeri pari è {somma}")
print (f"La media dei numeri dispari è {media}")


frequenza:dict[int] = {}

for numero in lista_numeri:
    if numero in frequenza:
        frequenza[numero] += 1
    else:
        frequenza[numero] = 1

numero_ripetuto = max(frequenza.values())
numeri_piùfrequenti = [numero for numero, freq in frequenza.items() if freq == numero_ripetuto]

Numero_Frequen = max(numeri_piùfrequenti)

print (f"Il numero con più ricorrenze è il numero {Numero_Frequen} venendo ripetuto {numero_ripetuto} volte")






















#indice = 0
#indice_inverso = -1
#frequenza_numero = 1
#max_numero = 0

#while indice <= len(lista_numeri):

    #for numero in lista_numeri:
        
        #if lista_numeri[indice] == lista_numeri[indice_inverso]:
            
            #frequenza_numero += 1
            #indice_inverso -= 1
            #max_numero += 1

        #elif indice_inverso == -(len(lista_numeri)):
                #indice += 1

       
        #elif lista_numeri[indice] != lista_numeri[indice_inverso]:

            #frequenza_numero = 1
            #indice_inverso -= 1 

        










