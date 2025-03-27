#Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.

def remove_duplicates(lista:list) -> list:

    lista_nuova:list = []

    

    for item in lista:

        if item not in lista_nuova:
            
            lista_nuova.append(item)

        else:

            pass

    return lista_nuova

    



       

    


    








print(remove_duplicates((1,2,3,"a","c", 3)))
    