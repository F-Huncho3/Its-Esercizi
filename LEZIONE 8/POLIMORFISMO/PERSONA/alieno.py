class Alieno:

    #Bisogna sapere la galassia di provenienza
    #self.galagy: str

    #inizializzazione oggetto di classe alieno

    def __init__(self, galaxy:str ):

        self.setGalaxy(galaxy)



    def setGalaxy(self, galaxy:str)->None:

        if galaxy:

            self.galaxy = galaxy

        else:

            print("La galassia di provenienza non deve essere una stringa vuota")

        
    def getGalaxy(self) ->str:

        return self.galaxy
    
    def __str__(self) ->str:

        return f"\nAlieno proveniente dalla galassia {self.getGalaxy()}\n"
    
    def speak(self) ->None:

        print("IL/&%/ /(&PCQ=)() PAPA FRANCESCO")
    