#Write a function check_length(), which takes a string as an argument.
#Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters.

def check_length(x:str):
    if len(x) > 10:
        print ("I caratteri sono maggiori di 10")

    elif len(x) < 10:
        print ("I caratteri sono minori di 10")

    else:
        print("I caratteri sono uguali a 10")

check_length(str(input("Inserisci la frase o la parola ")))