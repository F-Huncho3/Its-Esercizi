x:str = str(input("Inserisci una frase "))

spazi = 0 

for char in x:
    if char == " ":
        spazi += 1 

print (f"I tuoi spazi sono {spazi}") 
