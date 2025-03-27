class Persona:

    def __init__(self):

        self.name:str = ""
        self.lastname:str = ""
        self.age:int = 0

    def displayData(self) -> None:

        print(f"Nome : {self.name}\nCognome : {self.lastname}\nEtà : {self.age}")

    #Funzione che mi consenta di impostare il valore di sefl.name

    def setName(self, name:str) ->None:

        self.name = name 

    #Funzione che mi consenta di impostare il valore di self.lastname

    def setLastname(self, lastname:str) -> None:

        self.lastname = lastname

    #Funzione che mi consenta di impostare il valore di self.age

    def setAge(self, age:int) ->None:

        if age <0 or age > 130:
            self.age = 0

        else:

            self.age = age


    #Andiamo a definire delle funzioni che consentono di ritornare i valori richiesti

    def getName(self) -> str:

        return self.name
    
    def getLastName(self) -> str:

        return self.lastname
    
    def getAge(self) -> int:

        return self.age
    



    




