#Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
#• Modify your program to print a statement about each animal, such as A dog would make a great pet.
#• Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!


animals:list[str] = ["dog", "cat", "hamster"]
#Creo la lista di animali specificando il tipo di elemento all'interno

i = 0
x = 0

#Inizializzo delle variabili che verranno modificate all'interno del ciclo


while i <=2:
    if i == 0:
        print (f"The {animals[x]} is a great pet")

        #All'interno del ciclo while inserisco l'IF per la casisitica degli elementi, inserendo una variabile come indice e modificandola posso navigare nella lista.


        i += 1
        x += 1

    elif i == 1:
        print (f"The {animals[x]} makes a great companion")

        i +=1
        x +=1

    elif i == 2:
        print (f"The {animals[x]} is so tiny")

        break

print ("Those 3 are the best pets in the world")




    





    