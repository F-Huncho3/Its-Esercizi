#Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude

def check_parentheses(expression: str) -> bool:

    parentesi_accoppiate:list = []
    
    for char in expression:

        if char == "(":

            parentesi_accoppiate.append(char)

        elif char == ")":

            for element in parentesi_accoppiate:

                if element !="(":

                    return False
                
                else:

                    parentesi_accoppiate.pop()

    if len(parentesi_accoppiate) == 0:

        return True
    
    else:

        return False




    

        
    

    




            



    
                

                



    


        