from studente import *



#Creiamo un oggetto P di classe Persona

p: Persona = Persona ("Francesco", "Magno", 22)

#Visualizziamo le informazioni relative alla Persona P

#print(p)


#Creiamo un oggetto studente 1 della classe Studente

studente1: Studente = Studente ("Andrew", "Jacobs", 23, "0123456")

#Controlliamo che studente1 uno sia un istanza della classe Studente
'''
if isinstance(studente1, Studente):

    print("L'oggetto studente1 è un oggetto della classe Studente")

#La funzione isisnstance(obj, Class) -> True se l'oggetto obj è un istanza della classe Class

#Vogliamo sapere se studente1 sia anche istanza della classe Persona essendo che la classe Studente eredita da essa.

if isinstance(studente1, Persona) and isinstance(studente1, Studente):

    print("\nL'oggetto studente 1 è anche un istanza della classe persona")

else:

    print("\nL'oggetto studente1 è solo istanza della classe persona")



#Controlliamo che p sia istanza di Persona

if isinstance(p, Persona):

    print("\nL'oggetto p è istanza della classe persona")


#Controlliamo che p sia o meno istanza anched della classe Studente
if isinstance(p, Studente):

    print("\nL'oggetto p è istanza della classe Studente oltre che di Persona")

else:

    print("\nL'oggetto p è solo istanza della classe Persona")


#Vogliamo controllare se Studente è sottoclasse della classe Persona
#IssubClass (Class1,Class2) -> Controlla se Class1 è sottoclasse di Class2


if issubclass(Studente,Persona):

    print("\nLa classe Studente è sottoclasse della classe Persona")

'''   
#Grazie alla sovrascrittura del metodo __str__ all'interno della sottoclasse Studente andiamo a richiamare le informazioni dell'istanza ma in maniera diversa rispetto a un istanza della SuperClasse Persona, ovvero andiamo ad eliminare le informazioni dell'età. OVER-RIDING


print(studente1)

#print(f"\nLa media dei voti relativi agli esami sostenuti dallo studente 1 è: {studente1.getMediaEsami([15,26,30])}")


#Creiamo lo studente2

studente2: Studente = Studente (p.get_name(),p.get_lastname(),p.get_age(),"0987654")

print("\n", studente2)


#Confrontiamo se studente1 == a persona p


print("\n",studente1 == p)


#Confrontiamo studente 1 a studente 2

print("\n", studente1 == studente2)

#verifichiamo che lo studente 1 sia uguale a se stesso

print("\n", studente1 == studente1)


#Modificare nome, cognome, ed età dello studente2 per renderli uguali a studente1

studente2.set_name(studente1.get_name())
studente2.set_lastname(studente1.get_lastname())
studente2.set_age(studente1.get_age())


print("\n",studente1 == studente2)


#Forziamo l'uguaglianza del numero di matricola utilizzando il metodo set di Studente inserendo l'attributo di studente1

studente2.setMatricola(studente1.get_matricola())


#Verifichiamo l'uguaglianza
print ("\n", studente1 == studente2)


