
animale:list[str] = []

x:str = str(input("Inserisci un animale "))

animale.append(x)

match animale:

    case ["cane"]|["gatto"]|["cavallo"]|["elefante"]|["leone"]:

        print (f"{x} appartiene alla categoria dei Mammiferi")

    
    case ["serpente"]|["lucertola"]|["tartaruga"]|["coccodrillo"]:

        print (f"{x} appartiene alla categoria dei Rettili")

    case ["aquila"]|["pappagallo"]|["gufo"]|["falco"]:

        print (f"{x} appartiene alla categoria degli Uccelli")

    case ["squalo"]|["trota"]|["salmone"]|["carpa"]:

        print (f"{x} appartiene alla categoria dei Pesci")

    case _:

        print ("categoria sconosciuta")



    
