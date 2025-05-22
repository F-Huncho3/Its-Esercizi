from persona import * 



class Proprietario(Persona):

    def __init__(self, nome:str, cognome:str, cf:CodiceFiscale, indirizzo:Indirizzo, numerotelefonico:Telefono):
        super().__init__(nome, cognome, cf, indirizzo, numerotelefonico)


    def __str__(self):


            return super().__str__()
        


me:Proprietario = Proprietario ("Francesco","Magno","MGNFNC03H03H501P", "Via Giannetto valli 39", "3891971237")


print (me)


    

    
    