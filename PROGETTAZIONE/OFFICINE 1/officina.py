from indirizzo import Indirizzo

class Officina:

    def __init__(self, nome:str, indirizzo:Indirizzo):

        self.nome = nome
        self.indirizzo = indirizzo


    def __str__(self):
        
        return (f"Nome Officina:{self.nome}, Indirizzo:{self.indirizzo}")
    
    
        