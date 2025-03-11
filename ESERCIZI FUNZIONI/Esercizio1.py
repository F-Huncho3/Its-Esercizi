#Write a function check_value(), which takes a number as an argument.
#Using if / else, the function should print whether the number is bigger, smaller, or equal to 5.


def check_value(x:int) ->int:
    if x > 5:
        print(f"{x} è maggiore di 5")

    elif x < 5: 
        print (f"{x} è minore di 5")

    else:
        print (f"{x} è uguale a 5")


check_value(int(input("Inserisci il numero--> ")))
    


