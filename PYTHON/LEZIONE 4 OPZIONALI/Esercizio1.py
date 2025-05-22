def student_grades (student_name:str):

    #Vado ad inizializzare tutte le variabili che mi servono.


    student_name:str
    
    voto:float = 0

    lista_materie:list = ["A"]

    media:float = 0 

    votiematerie:dict = {}

    #Creo un for (con range 9 per un massimo di materie) che mi permette di inserire nomi di materie e voti in input fin quando non scelgo di fermarmi.

    for i in range(9):
        materia_voto = str(input("Inserisci la materia nella quale vuoi mettere il voto (Scrivi Stop quando vuoi fermarti)-->"))

        #Inserisco la materia


        if materia_voto == "Stop":

            #Se voglio fermarmi inserisco Stop e si effettua il break del loop

            break
            

            

        elif materia_voto != "Stop":

            #Insieriamo il voto, all'interno di una variabile che si aggiorna da voto a voto, e inseriamo in un dizionario il nome della materia come chiave e il voto come valore.
            #(Solo per dispaly dei voti)

            inserimento_voto = float(input("Vuoi inserire un voto? "))

            voto += inserimento_voto

            votiematerie[materia_voto] = inserimento_voto

            lista_materie.append(materia_voto)

            

        else:

            break
    

    media = voto/(len(lista_materie) - 1)

    print(f"Lo studente scelto è {student_name}")

    if media >= 6:
        print (f"Lo studente ha passato gli esami con la media di {media}")
    else:
        print (f"Lo studente non ha passato l'esame")

    
    print(f"La media dello studente è {media}")
    print(f"I voti per materia dello studente sono: {votiematerie}")

    return media,votiematerie,student_name

lista_studenti:list = ["Gianmarco","Francesco","Andrea"]

for student in lista_studenti:
    student_grades(student)



    



    

    

