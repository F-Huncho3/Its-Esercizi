import string

def frequenzaParole(stringa:str) -> dict:

    soloparole = stringa.split()

    frequenza:dict = {}


    for parola in soloparole:


        parolacont = parola.lower().strip(string.punctuation)


        if parolacont in frequenza:

            frequenza[parolacont] += 1

        else:

            frequenza[parolacont] = 1

    return frequenza



        





