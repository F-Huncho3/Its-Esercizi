from indirizzo import Indirizzo
from codicefiscale import CodiceFiscale
from telefono import Telefono


class Persona:

    def __init__(self, nome:str, cognome: str, cf: CodiceFiscale, indirizzo:Indirizzo, numerotelefonico:Telefono ):

        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.indirizzo = indirizzo
        self.numerotelefonico = numerotelefonico



    def __str__(self):
        
        return (f"Nome: {self.nome}\n Cognome:{self.cognome}\n Codice Fiscale:{self.cf}\n Indirizzo:{self.indirizzo}\n Numero di Telefono:{self.numerotelefonico}")
        