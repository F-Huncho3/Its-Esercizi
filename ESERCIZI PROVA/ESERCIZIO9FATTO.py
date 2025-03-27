#Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:

    new_list:list = []

    for item in original_set:

        if item not in elements_to_remove:

            new_list.append(item)

        
    new_set = set(new_list)

    return new_set

    

   

