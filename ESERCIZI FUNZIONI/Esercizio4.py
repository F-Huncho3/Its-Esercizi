#Write a function check_each(), which takes a list of numbers as argument.
#Using a for loop, iterate through the list.
#For each number, print “bigger” if it’s bigger than 5, “smaller” if it’s smaller than 5, and “equal” if it’s equal to 5.


def check_each(lista:list):
    for element in lista:
        if element > 5:
            print(f"{element} maggiore di 5")

        elif element < 5:
            print(f"{element} minore di 5")

        else:
            print(f"{element} uguale a 5")


check_each([1,5,8,9,2,4,7,3])