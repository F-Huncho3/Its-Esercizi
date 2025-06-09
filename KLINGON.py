'''
Obiettivo
L'obiettivo di questo esercizio è creare un modello semplice per simulare la crescita delle popolazioni di due specie animali usando la programmazione orientata agli oggetti in Python.

Descrizione del problema
Due specie animali, i Bufali Klingon e gli Elefanti, vivono in una riserva naturale. Ogni specie ha una popolazione iniziale e un tasso di crescita annuo. Vogliamo sapere:
- In quanti anni la popolazione degli Elefanti supererà quella dei Bufali Klingon.
- n quanti anni la popolazione dei Bufali Klingon raggiungerà una densità di 1 individuo per km².
 
Specifiche tecniche

1. Classe Specie
- Attributi:

    nome (str): Nome della specie.
    popolazione (int): Popolazione iniziale.
    tasso_crescita (float): Tasso di crescita annuo percentuale.

- Metodi:

    __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float): Costruttore per inizializzare gli attributi della classe.
    cresci(self): Metodo per aggiornare la popolazione per l'anno successivo.
    anni_per_superare(self, altra_specie: 'Specie') -> int: Metodo per calcolare in quanti anni la popolazione di questa specie supererà quella di un'altra specie.
    getDensita(self, area_kmq: float) -> int: Metodo per calcolare in quanti anni la popolazione raggiungerà una densità di 1 individuo per km².

 

2. Sottoclassi BufaloKlingon e Elefante
Entrambe le sottoclassi animali BufaloKlingon ed Elefante devono ereditare dalla classe base Specie e devono inizializzare il nome della specie rispettiva.
 
Formule Matematiche:

    Aggiornamento della popolazione per l'anno successivo:
        Formula: popolazione_nuova = popolazione_attuale x (1 + tasso_crescita/100)
    Calcolo della densità di popolazione:
        Formula: popolazione / area_kmq
        Hint: Loop incrementale che continua ad aggiornare la popolazione finché la densità non raggiunge 1 individuo per km²
    Calcolo degli anni necessari per superare la popolazione di un'altra specie:
        Hint: Loop incrementale che continua ad aggiornare la popolazione di entrambe le specie finché la popolazione di questa specie non supera quella dell'altra. Per evitare che le popolazioni crescano all'infinito, limitare il numero di anni a 1000.'''
from typing import Self

class Specie:

    nome:str 


    def __init__(self, popolazione_iniziale:int, tasso_crescita:float):

        self.popolazione_iniziale = popolazione_iniziale
        self.tasso_crescita = tasso_crescita
        self.popolazione_attuale = popolazione_iniziale



    def cresci(self) -> int:

        self.popolazione_attuale = int(self.popolazione_attuale *(1 + self.tasso_crescita / 100))
        
        return self.popolazione_attuale



    def anni_per_superare(self, altra_specie:Self) ->int:

        year:int = 0
 

        while self.popolazione_attuale < altra_specie.popolazione_attuale:

            self.cresci()

            altra_specie.cresci()

            year +=1

            if year ==1000:

                return year
            
        return year

    
    def getDensita(self, area_kmq:float) ->int:

        year = 0

        densità = self.popolazione_attuale/area_kmq


        while densità < 1 and year <1000:

            self.cresci()

            year += 1

            densità = self.popolazione_attuale/area_kmq 



        if densità >=1:

            return  year
        
        else:
            
            return "La densità non ha raggiunto 1 individuo per km² in 1000 anni"
            

       

    
class BufaloKlingon(Specie):

    nome:str = "BufaloKlingon"

    def __init__(self, popolazione_iniziale:int, tasso_crescita:int):
        super().__init__(popolazione_iniziale, tasso_crescita)



class Elefante(Specie):

    nome:str = "Elefante"

    def __init__(self, popolazione_iniziale:int, tasso_crescita:int):
        super().__init__(popolazione_iniziale, tasso_crescita)








specie1: Specie = Specie ("Boh", 100, 15)

specie2 :Specie = Specie ("Bah", 10, 35)





print(specie1.anni_per_superare(specie2))

            


