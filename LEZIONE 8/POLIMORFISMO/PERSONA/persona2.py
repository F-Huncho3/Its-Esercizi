class Persona:

    def __init__(self, name:str, lastname:str, age:int):

        self.name:str = name
        self.lastname:str = lastname
        self.age:int = age

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
    
    def __str__(self) ->str:

        return f"{self.name}\n{self.lastname}\n{self.age}"
    

    def speak(self) ->None:
        print(f"\nHello! My name is {self.getName()}!\n")



    




