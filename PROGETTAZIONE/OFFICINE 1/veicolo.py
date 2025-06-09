from targa import Targa
from datetime import datetime


class Veicolo:

    def __init__(self, modello:str, tipo:str, targa:Targa, annoImmatricolazione:datetime):

        self.modello = modello
        self.tipo = tipo
        self.targa = targa
        self.annoImmatricolazione = annoImmatricolazione
        


    def __str__(self):
        
        return (f"Modello:{self.modello}\n Tipo:{self.tipo}\nTarga:{self.targa}\nProprietario:{self.cf.proprietario}")
        