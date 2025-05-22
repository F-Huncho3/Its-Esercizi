guest:list[str] =["Lebron", "Edoardo", "Harry Potter", "Sakamoto", "Ginger"] 

for guests in guest:
    print (f"Hei {guests} would you like to come to dinner tonight?")

print("Ginger will not make it tonight")

guest.remove("Ginger")
guest.append("Steph Curry")

for guests in guest:
    print (f"Hei {guests} would you like to come to dinner tonight?")

#Al posto del ciclo for dovremmo mettere il print per ogni nome nella lista accedendo alla struttura con l'indice anhe per il remove e per l'update dell'elemento nella lista.
