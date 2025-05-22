def filtra_e_mappa(prodotti: dict[str,float]) -> dict[str,float]:
    
    new_dict:dict ={}
    
    for key,value in prodotti.items():
        

        if value >= 20:

            new_dict[key] = value - ((value/100)*10)

        else:

            pass

    return new_dict



print(filtra_e_mappa({"Zaino":25}))