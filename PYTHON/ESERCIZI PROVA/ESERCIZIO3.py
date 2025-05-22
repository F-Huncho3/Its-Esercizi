#Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.

def frequency_dict(elements: list) -> dict:

    frequenza:dict = {}

    for element in elements:
        
        if element in frequenza:

            frequenza[element] += 1

        else:

            frequenza[element] = 1

    return frequenza








 


            









    





    
    
    
    




