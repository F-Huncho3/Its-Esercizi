#CONSIGLI

''' x = Ciao
    key = 2
    
    
    C diventerà E
    I diventerà M
    A diventerà C
    O diventerà Q
    
    
    
    12%10 = 2'''

from string import ascii_lowercase

def cifrario(stringa:str, key:int) ->str:
    
    alfabeto:str = "abcdefghijklmnopqrstuvwxyz"

    new_string = ""

    

    if stringa:

        vera_stringa = stringa.lower()
        
        for char in vera_stringa:

            if char in alfabeto:

                idstr = alfabeto.index(char)

                if (idstr + key) >26:

                    index = (idstr + key) %len(alfabeto)

                    new_string += alfabeto[index]

                else:

                    index = (idstr + key)

                    new_string += alfabeto[index]

            else:

                new_string += char

    return new_string



def decifrario(stringa:str, key:int):

    alfabeto:str = "abcdefghijklmnopqrstuvwxyz"

    old_string = ""

    if stringa:

        vera_stringa = stringa.lower()
        
        for char in vera_stringa:

            if char in alfabeto:

                idstr = alfabeto.index(char)

                if (idstr - key) < 0 :

                    index = (idstr - key) %len(alfabeto)

                    old_string += alfabeto[index]

                else:

                    index = (idstr - key)

                    old_string += alfabeto[index]

            else:

                old_string += char

    return old_string





print(cifrario("CIAO", 2))

print(decifrario("ekcq",2))


