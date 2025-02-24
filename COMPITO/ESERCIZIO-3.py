parola_corretta:str = (input("Inserisci una parola "))
y:str = " "

for char in parola_corretta:
    y = char + y

print (f"La parola invertita è {y}")

