import re

class CodiceFiscale:

    def __init__(self, cf:str):
        
        self.setCodice(cf)
    
    def setCodice(self, cf:str):

        pattern = re.fullmatch(r'[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]', cf)

        if pattern:

            self.cf = cf
        
        else:

            raise TypeError ("Codice Fiscale Invalido")
        
   
        


fra:CodiceFiscale = CodiceFiscale ("MGNFNC03H03H501P")


print (fra)