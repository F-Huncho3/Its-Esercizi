''''
#Dal file persona.py importiamo la classe persona.
from persona import Persona

#Creo una persona
fm:Persona = Persona("Francesco","Magno",21)


#print (fm)   

#print (fm.name, fm.lastname, fm.age)

#Richiamiamo la funzione displayData della classe Persona per mostrare in output i dati relativi alla persona fm.

fm.displayData()

print ("-----------------")
'''''
#Dal file persona2 importiamo persona.
from POLIMORFISMO.PERSONA.persona2 import Persona


fm:Persona = Persona()

#Richiamiamo la funzione dispalyData per mostrare in output le funzioni relative all?oggetto fm

fm.displayData()

#modifichiamo il nome della persona 

fm.setName("Francesco")

print("--------------")

fm.displayData()


print("--------------")

#Modifichiamo Cognome e Età della "Persona" "fm".

fm.setLastname("Magno")

fm.setAge(21)

fm.displayData()

print("--------------")

print(fm.getLastName(),fm.getName(),fm.getAge())







