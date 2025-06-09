def verifica(x:bool,y:bool,z:bool) ->str:

    if x == True and (y == True or z == True):

        return "Azione Permessa"
        
    else:
        
        return "Azione Negata"
    

    

print(verifica(True, True, False))


def numerointero(listanumeri:list[int], massimo:int) ->int:

    newnumber:int = 1 

    for numero in listanumeri:

        if numero<= massimo:
            
            newnumber *= numero

        else:

            pass

    return newnumber




#PRIMA SEQUENZA OGNI 2
#SECONDA SEQUENZA OGNI 3 PARTENDO DA 1
#TERZA SEQUENZA MENO 5 PARTENDO DA 30
#QUARTA SEQUENZA PIU' 10 PARTENDO DA 5




def ognidue() ->int:

    i = 2

    while i <=14:


        print (i)

        i += 2

def ogniduefor() ->int:

    for i in range(2,15,2):

        print(i)


def ognitre() ->int:

    i = 1

    while i <=13:

        print(i)

        i += 3





def menocinque() ->int:

    for i in range(30, -1, -5):

        print(i)


def piudieci() ->int:

    for i in range(5,46,10):

        print (i)


menocinque()

piudieci()



