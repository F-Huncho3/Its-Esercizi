import random


def guess_the_number(y:int,x:int):

    min_numb = y

    max_num = x

    numero_random = random.randint(min_numb,max_num)

    tentativi = 5

    for i in range (1,6):

        numero_user = int(input("Inserisci il numero scelto  "))

        if numero_user == numero_random:

            print("\nNumero CORRETTO!")

            break

        elif numero_user != numero_random :

            tentativi -= 1

            print (f"\nNumero sbagliato hai ancora {tentativi} tentativi")

            if numero_user > numero_random:

                print ("Aiuto, il numero da indovinare è più piccolo")

            else:

                print ("\nAiuto, il numero da indovinare è più grande")

    if tentativi == 0:

        print ("\nMi dispaice hai finito i tentativi possibili")

    else:

        print("Complimenti hai completato il gioco")


guess_the_number(0,10)

    