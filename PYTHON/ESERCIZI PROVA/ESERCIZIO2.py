#Scrivi una funzione che, dato un numero intero, determina se è un "numero magico". Un numero magico è definito come un numero che contiene il numero 7.

def is_magic_number(num: int) -> bool:

    numero = str(num)

    for char in numero:

        if char == "7":

            result = True

            return True
        
        else:

            result = False

    return result
        
        

    

       
        
print(is_magic_number(2))
    
    


        


        
    

    


        

