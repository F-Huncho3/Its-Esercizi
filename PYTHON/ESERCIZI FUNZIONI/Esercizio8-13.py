#8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"



def profilo(name:str =str(input("Inserisci il tuo nome ")),last_name:str = str(input("Inserisci il tuo cognome ")),age:int =int(input("Inserisci la tua età ")),hair:str =str(input("Inserisci il colore dei capelli ")),height =str(input("Inserisci la tua altezza "))):
    #FUNZIONE NON VA BENE : TROPPI PARAMETRI E TROPPO CONFUSIONALE
    #RENDERE PIÙ E SEMPLICE L'HEADER DELLA FUNZIONE

    print (f"{name}{last_name}, anni {age}, colore dei capelli {hair}, altezza {height}")

    