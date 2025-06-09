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

    if stringa:
        
        for char in stringa:

            idstr = alfabeto.index(char)

            idstr += key





def decifrario(stringa:str, key:int) ->str:

    pass