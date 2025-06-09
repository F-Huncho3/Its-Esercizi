def ricercaBinaria(lista_numeri:list, numero:int) -> bool:

    while lista_numeri:

        metà = len(lista_numeri) // 2

        if lista_numeri[metà] == numero:

            return True
        
        elif lista_numeri[metà] < numero:

            lista_numeri = lista_numeri[metà + 1]

        else:

            lista_numeri = lista_numeri[metà]

    return False
