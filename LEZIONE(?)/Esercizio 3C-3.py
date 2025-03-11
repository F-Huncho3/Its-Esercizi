oggetti:list[str] = []

for i in range(3): #ciclo ripetuto 3 volte per inserire oggetti.
    
    oggetto:str = str(input("Inserisci un oggetto: ")).lower()
    oggetti.append(oggetto)

match oggetti: #confronto con la lista con le categorie
    
    case ["penna","matita","quaderno"]:
        print("Materiale scolastico")

    case ["pane","latte","uova"]:
        print("Alimenti")

    case ["sedia","tavolo","armadio"]:
        print("Mobili")

    case ["telefono","computer","tablet"]:
        print("Dispositivi elettronici")

    case _:
        print("Categoria sconosciuta")

        

    
