#Modificare il codice dell'esercizio 3C-4, affinchè si possa scrivere un codice python che consenta all'utente di inserire il nome di un animale ed un habitat. Quando il codice dell'esercizo 3C-4 classifica l'animale inserito in una delle categorie tra mammiferi, rettili, uccelli o pesci, oltre a mostrare un messaggio a schermo, deve salvare tale categoria in una variabile animal_type. Se l'animale inserito non è classificabile in una delle quattro categorie proposte, il valore di animal_type sarà ' "unknown".

#Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.

#Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; dunque, verificare:
#- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
#- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
#- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.

#Le categorie di classificazione devono essere:
#- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
#- Rettili: serpente, lucertola, tartaruga, coccodrillo.
#- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
#- Pesci: squalo, trota, salmone, carpa.

#Categorie di habitat:
#- acqua
#- aria
#- terra





animal:str = str(input("Inserisci un animale "))
habitat_type:str = str(input("Inserisci un habitat "))



animale:list[str] = []
animal_type: str
animale.append(animal)


match animale:

    case ["cane"]|["gatto"]|["cavallo"]|["elefante"]|["leone"]|["balena"]|["delfino"]:

        print (f"{animal} appartiene alla categoria dei Mammiferi")
        animal_type = "Mammifero"



    
    case ["serpente"]|["lucertola"]|["tartaruga"]|["coccodrillo"]:

        print (f"{animal} appartiene alla categoria dei Rettili")
        animal_type = "Rettile"


    case ["aquila"]|["pappagallo"]|["gufo"]|["falco"]|["cigno"]|["anatra"]|["gallina"]|["tacchino"]:

        print (f"{animal} appartiene alla categoria degli Uccelli")
        animal_type = "Uccelli"


    
    case ["squalo"]|["trota"]|["salmone"]|["carpa"]:

        print (f"{animal} appartiene alla categoria dei Pesci")
        animal_type = "Pesci"


    case _:

        print ("categoria sconosciuta")




animalDict:dict[str] = {"animale": animal , "tipo": animal_type , "habitat": habitat_type}


match animalDict:

    #mammiferi
    case {"animale": animal , "tipo": "Mammiferi" , "habitat": habitat_type}:
        
        match animal in {"animale": "balena"|"delfino" , "tipo": "Mammiferi" , "habitat": habitat_type}:

            case {"animale": "balena"|"delfino" , "tipo": "Mammiferi" , "habitat": habitat_type}:

                if habitat_type == "acqua":
                    print (f"L'animale {animal} fa parte dell'habitat 'acqua' ")
                else:
                    print("L'habitat è errato")


            case {"animale": animal , "tipo": "Mammiferi" , "habitat": "terra"}:

                print()



       
    

     






































#match animale:

    #case {"cane":"terra"}|{"gatto":"terra"}|{"cavallo":"terra"}|{"elefante":"terra"}|{"leone":"terra"}|{"lucertola":"terra"}|{"galllina":"terra"}|{"tacchino":"terra"}:

        #if x == "lucertola":

            #print(f"{x} fa parte dei rettili e l'habitat è 'terra'.")

        #elif x == "gallo" or x == "tacchino":

            #print (f"{x} fa parte degli uccelli e l'abitat è 'terra'.")

        #else:

            #print (f"{x} fa parte dei mammiferi e l'abitat è 'terra'.")


    #case {"serpente":"acqua"}|{"serpente":"terra"}|{"tartaruga":"acqua"}|{"tartaruga":"terra"}|{"coccodrillo":"acqua"}|{"coccodrillo":"terra"}:
















