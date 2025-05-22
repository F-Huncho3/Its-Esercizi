#Write a function print_numbers(), which takes a list of numbers as argument.
#Using a for loop, print each number one by one


lista_numeri:list[int] = [1,2,8,4,5,6,3,7,9,10,11]


def print_numbers(x:list):
    for i in lista_numeri:
        print (i)

print_numbers(lista_numeri)