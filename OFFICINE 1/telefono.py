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
        





