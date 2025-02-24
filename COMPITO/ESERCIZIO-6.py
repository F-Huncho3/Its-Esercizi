n1:int = int(input("Inserisci il primo numero "))
n2:int = int(input("Inserisci il secondo numero "))

i = n1
i2 = n2

if n1 and n2 >= 0:



    prodotto = 1

if n1 > n2:
    while i2 <= n1:
    
        print (f"Il numero che stai moltiplicando è {i2}")

        prodotto *= i2

        i2 += 1

        print (f"Il prodotto è {prodotto}")
        
elif n2 > n1:      
    while i <= n2:

        print (f"Il numero che stai moltiplicando è {i}")

        prodotto *= i 

        i += 1

        print (f"Il prodotto è {prodotto}")
    
    