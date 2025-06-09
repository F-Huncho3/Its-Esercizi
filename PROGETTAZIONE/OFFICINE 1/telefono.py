import re

class Telefono:

    def __init__(self, numero: str):
        self.setnumero(numero)

    def setnumero(self, numero: str):
        if numero:
            
            pattern = re.fullmatch(r"(\+39)?3[2-9][0-9]{8}", numero)
            
            if pattern:
                self.numero = numero
            else:
                raise TypeError("Numero Invalido")
        else:
            raise ValueError("Numero non fornito")

    def __str__(self):
        return f"Numero: {self.numero}"
    

class CodiceFiscale:

    def __init__(self, cf:str):
        
        self.setCodice(cf)
    
    def setCodice(self, cf:str):

        pattern = re.fullmatch(r'[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]', cf)

        if pattern:

            self.cf = cf
        
        else:

            raise ValueError ("Codice Fiscale Invalido")
        





