#DEFINIZIONE DI UN DATO
#DEFINIAMO LA CLASSE:

class Persona:

    #Ci servono delle informazioni per la persona: Nome, Cognome ed Eta
    #Questi saranno gli attribbuti della classe.

    #Costruttore:
    def __init__(self, name:str, lastname:str, age:int):
        #La funzione che stiamo definendo è propria della classe Persona, attraverso il SELF

        self.name = name
        self.lastname = lastname
        self.age = age

        #L'attributo della classe lo inzializzo con il valore generico della variabile stessa.

    #Scriviamo una funzione che mostri in output i dati relativi ad una persona.

    def displayData(self) -> None:

        print(f"Nome : {self.name}\nCognome : {self.lastname}\nEtà : {self.age}")




