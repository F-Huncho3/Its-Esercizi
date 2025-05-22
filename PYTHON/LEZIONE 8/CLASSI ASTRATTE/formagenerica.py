from abc import ABC, abstractmethod
#abc = abstrract base class

class FormaGenerica(ABC):

#Diamo la definizione del metodo posticipando la sua implementaizione (METODO ASTRATTO)
    
    
    @abstractmethod #DECORATOR
    def draw(self)->None:

        pass


    def setShape(self,shape:str) ->None:

        if shape:

            self.shape = shape

        else:

            print("ERROR")


    def getShape(self) ->str:

        return self.shape


    

        
       
        
