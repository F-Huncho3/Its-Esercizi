class Persona:

    #Utilizziamo il costruttore per definire la classe

    def __init__(self, name:str, lastname:str, age:int):

        self.set_name(name) 
        self.set_lastname(lastname)
        self.set_age(age)

    #Setter

    def set_name (self, name:str) ->None:

        if name:

            self.name = name

        else:

            print("Error, name must be compiled")

    def set_lastname (self, lastname:str) ->None:

        if lastname:

            self.lastname = lastname

        else:

            print("Error, lastname must be compiled")

    def set_age (self, age:int) ->None:

        if age < 0 or age >130:

            print ("Error, choose a valid age")

            self.age = 0

        else:

            self.age = age
        

    #Getter

    def get_name (self) ->str:

        return self.name
    
    def get_lastname (self) ->str:

        return self.lastname
    
    def get_age (self) -> int:

        return self.age
    
    
    #Metodi Speciali: __str__ e __call__

    def __str__ (self) -> str:

        return f"Name: {self.name}\nLastname: {self.lastname}\nAge: {self.age}"
    
    def __call__(self) -> None:

        if self.age < 18:

            print (f"{self.name} {self.lastname} è minorenne")

        elif 18< self.age <30:

            print (f"{self.name} {self.lastname} è maggiorenne")