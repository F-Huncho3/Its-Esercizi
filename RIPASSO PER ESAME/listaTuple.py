#Converti una lista di tuple (prodotto, quantità) in un dizionario che sommi le quantità per ogni prodotto

lista1:list[tuple] = [("a",1), ("a",3), ("b", 2), ("c",5), ("d",1)]



def converti(lista_tuple:list[tuple]) ->dict:

    dizionario_prodotti:dict = {}

    for product in lista_tuple:

        key, value = product[0], product[1]

        if key not in dizionario_prodotti:

            dizionario_prodotti[key] = value

        else:

            dizionario_prodotti[key] += value


    return dizionario_prodotti



print (converti(lista1))


#Dato un elenco di tuple (nome_studente, punteggio) crea un dizionario che abbia la somma di ogni punteggio per studente

lista_studenti:list[tuple] = [("Francesco", 10), ("Lorenzo", 10), ("Matteo", 6.5), ("Matteo", 6.5)]





def converti2(lista_punteggi:list[tuple]) ->dict:

    dizionario_punteggi:dict = {}

    for studente in lista_punteggi:

        key, value = studente[0], studente[1]

        if key not in dizionario_punteggi:

            dizionario_punteggi[key] = value

        else:

            dizionario_punteggi[key] += value


    return dizionario_punteggi





        

print(converti2(lista_studenti))