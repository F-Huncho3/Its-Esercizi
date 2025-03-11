nome:str = str(input("Inserisci il tuo nome"))

genere:str = str(input("Inserisci il tuo genere con la lettera 'm' o 'f' ")).lower #Per evitare che con l'inupt ci sia qualche errore in caso di lettera maiuscola.

print (f"{nome}")

match genere:

    case "m":
        print ("Maschio")

    case "f": 
        print ("Femmina")