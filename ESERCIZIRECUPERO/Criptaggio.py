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
    
    alfabeto:str = "abcdefghilmnopqrstuvz"

    new_string = ""

    if stringa:
        
        for char in stringa:

            if char in alfabeto:

                idstr = alfabeto.index(char)

                index = (idstr + key) %len(alfabeto)

                new_string += alfabeto[index]

            else:

                new_string += char

    return new_string



def decifrario(stringa:str, key:int):

    alfabeto:str = "abcdefghilmnopqrstuvz"

    old_string = ""

    if stringa:
        
        for char in stringa:

            if char in alfabeto:

                idstr = alfabeto.index(char)

                index = (idstr - key) %len(alfabeto)

                old_string += alfabeto[index]

            else:

                old_string += char

    return old_string








