from persona import Persona
from typing import Any
# Ogni studente dovrà avere gli stessi attributi della persona ma dovremmo aggiungere degli attributi che appartengono solo ad esso.
# O creare delle funzioni collegate solo alla classe studente anche se eredita dalla classe Persona.


#Due strade possibili: 
#1 -> Riscrivere tutte le informazioni nel costruttore (non conveniente)

#2 -> Ereditare le informazioni dalla classe persona

class Studente(Persona):
    '''
    def inheritanceTest (self):
        #verefichiamo che la classe studente erediti tutti gli attributi della classe persona

        self.name
        self.lastname
        self.age

        #verificare che la classe Studente erediti tutti i metodi della classe Persona 

        self.get_name()
        self.get_lastname()
        self.get_age()
    '''
    #Inizializziamo un oggett della classe Studente

    def __init__(self, name:str, lastname: str, age:int, matricola:str):
        
        #Inizializziamo la superclasse
        super().__init__(name, lastname, age)

        #inizializziamo la classe studente
        #Istruzioni che inizializzano lo studente
        self.setMatricola(matricola)



    #metodi setter (utiliazziamolo per impostare l'attributo della classe studente) 
    
    def setMatricola (self, matricola:str) ->None:

        if matricola:

            self.matricola = matricola

        else:

            print ("ERRORE, la matricola non può essere una stringa vuota")

    def get_matricola(self) ->str:

        return self.matricola

    #metodo che consente di visualizzare informazioni relative all'oggetto della classe Studente ovvero __str__
    
    def __str__(self) -> str:
        
        #return f"{super().__str__()}\nMatricola: {self.matricola}"

        return f"Nome: {self.get_name()}\nCognome: {self.lastname}\nMatricola: {self.get_matricola()}"
    


    #metodo che mi consente di clacolare la media degli esami sostenuti dallo Studente


    def getMediaEsami(self, voti_esami:list[int]) -> float:

        #se la lista non è vuota 

        if voti_esami:

        #calcolare la somma dei voti

            somma:int = 0

            for voto in voti_esami:

                somma += voto
            
        #ritornare la media

            return f" {round(somma/len(voti_esami), 2)}"
        
        #se la lista vuota

        else:

            return f"\nLa media è {0.00} in quanto non sono stati registrati voti di esame"
        
    #metodo che consente di confrontare due oggetti della classe studente e stabilire che questi due oggetti siano uguali o meno   
    
    def __eq__(self, other:Any) -> bool:

        #Se Other è None, oppure se other non è un istanza della classe Studente ritornerà False

        if other is None or not isinstance(other, type(self)):

            return False
        
        #Altrimenti, valuta la seguente uguaglianza

        else:

            return self.get_matricola() == other.get_matricola()
        
        #Due studenti sono uguali se hanno la stessa matricola
       


        





