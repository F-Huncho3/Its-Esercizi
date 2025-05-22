from persona import *
from datetime import datetime

class Direttore(Persona):

    def __init__(self, nome:str, cognome:str, cf:CodiceFiscale, indirizzo:Indirizzo, numerotelefonico:Telefono, dataDinascita:datetime):
        super().__init__(nome, cognome, cf, indirizzo, numerotelefonico)

        self.datadinascita = dataDinascita


    def __str__(self):
        return super().__str__() + f"\nData di nascita:{self.datadinascita}"
    



Dir1:Direttore = Direttore ("Santo", "Feraco", "MGNFNC034512w32323", "Via Gualtieri 13", "3891971237")