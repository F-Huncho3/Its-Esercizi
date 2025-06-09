from persona import *

class Dipendente(Persona):

    def __init__(self, nome:str, cognome:str, cf:CodiceFiscale, indirizzo:Indirizzo, numerotelefonico:Telefono, anniServizio:int):
        super().__init__(nome, cognome, cf, indirizzo, numerotelefonico)

        self.setAnniServizio(anniServizio)


    def setAnniServizio(self, anniServizio:int):

        if anniServizio:

            self.anniServizio = anniServizio

        else: 

            return (f"Anni di sevizio deve essere compilato")


    def __str__(self):
        return super().__str__() + f"\nAnni di Servizio:{self.anniServizio}"




