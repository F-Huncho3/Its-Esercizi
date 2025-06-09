from datetime import datetime

class Riparazione:

    def __init__(self, accettazione:datetime):

        self.accettazione = accettazione

        


    def setRiconsegna(self, riconsegna:datetime):

        self.riconsegna = riconsegna

        return self.riconsegna



    def __str__(self):
        
        if self.riconsegna:

            return (f"Stato:Ultimato\n Accettazione:{self.accettazione}\nRiconsegna:{self.riconsegna}")
        
        else:

            return (f"Stato: Da ultimare\n Accettazione:{self.accettazione}")
        

        



        