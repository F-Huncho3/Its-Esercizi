#Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:

    dict3 = dict1.copy()

    for key in dict1:

        if key in dict3:

            dict3[key] += dict2[key]
        
        else:

            dict3 [key] = dict2[key]
            
    return dict3


    
    
    




            