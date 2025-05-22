#Write a function add_one(). It takes an integer as argument. The function adds 1 to the integer and returns it.
#Write another function add_one_to_list(). It takes a list of #integers as argument.
#Define a variable new_list in this function.
#Using a for loop, iterate through the argument list.
#Using add_one(), fill new_list with integers from the argument list incremented
#by 1.
#Print new_list.


def add_one(x:int):
    result = x + 1

    return result

vera_lista:list = []


def inserimento_numeri(*args):
    for i in range (10):
        x:int = int(input("Inserisci un numero "))
        

        vera_lista.append(add_one(x))

    return vera_lista

inserimento_numeri()

print (vera_lista)


def add_one_to_list(lista_numeri:list[int]):
    new_list:list= []
    for numeri in lista_numeri:
        new_list.append(add_one(numeri))

    return new_list

print(add_one_to_list([1,2,3,4,4]))





    



