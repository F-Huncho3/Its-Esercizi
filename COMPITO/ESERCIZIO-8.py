lista_numeri:list[int] = []

while len(lista_numeri)<=4:

    numero_inserito:int = int(input("Inserisci un numero "))

    if 1 <= numero_inserito <= 30:

        lista_numeri.append(numero_inserito)



    else:
        print ("Il numero inserito deve essere compreso tra uno e trenta")


for numero_inserito in lista_numeri:
    print ("*" * numero_inserito)


