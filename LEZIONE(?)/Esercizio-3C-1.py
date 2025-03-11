voto:float = float(input("Inserisci un voto da 1 a 10 "))

match voto:

    case 1|2|3:
        print ("Gravemente insufficiente")

    case 4|5:
        print ("Insufficiente")

    case 6|7:
        print ("Sufficiente")

    case 8|9:
        print ("Molto buono")

    case 10:
        print ("Eccellente")

    case _:
        print ("Voto non valido")