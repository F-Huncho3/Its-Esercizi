import re

class Targa:

    def __init__(self, targa:str):
        
        self.setTarga(targa)

    def setTarga (self, targa:str):

        text = re.fullmatch (r"^([a-zA-Z]{2})+([0-9]{3,4})+([a-zA-Z]{2})+$", targa)

        if text:

            self.targa = targa
        
        else:

            raise TypeError ("Targa Invalida")
        

    
citroen:Targa = Targa("ED819ET")