frase:str = str(input("Inserisci una frase o una parola "))

x = -1
match frase[-1]:

    case "?" if  len(frase)%2 == 0:
        print ("Si")

    case "?" if len(frase)%2 != 0:
        print ("NO")

    
    case "!":

        print ("Wow")

    case _:

        print (f"Tu dici {frase}")





