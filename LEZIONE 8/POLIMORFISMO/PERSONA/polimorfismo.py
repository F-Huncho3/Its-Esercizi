from persona2 import Persona

from alieno import Alieno




#creare oggetto p della classe persona
p:Persona = Persona("Francesco","Magno",21)

print(p)

#creare oggetto alieno

eT:Alieno = Alieno("Androcchia")

print(eT)


#L'oggetto p invoca il metodo speak()

p.speak()

#L'oggetto eT invoca il metodo speak()

eT.speak()