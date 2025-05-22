from formagenerica import FormaGenerica

class Rettangolo(FormaGenerica):

    def __init__(self):
        super().__init__()

        self.setShape("Rettangolo")


    def draw(self):
        print(f"\n{self.getShape()}\n")

        #lato a: i = 0 and j = 0 e 9
        #lato b: i = 0 e 4 and j = 0
        #lato c: i = 0 e 4 and j = 9
        #lato d: i = 4 and j = 0 e 9

        #outer for
        for i in range(5):
            #inner for
            for j in range(5*2):

                #descrivere il lato a e il lato d del rettangolo

                if i == 0 or i == 4:

                    print("*",end=" ")

                #lato b e lato c

                elif j == 0 or j == 9:

                    print("*", end=" ")

                #spazi vuoti

                else:

                    print(" ", end=" ")
            
            
            print("\n", end="")









r:Rettangolo = Rettangolo()

r.draw()
