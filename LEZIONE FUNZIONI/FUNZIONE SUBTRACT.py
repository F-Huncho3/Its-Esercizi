x:int = int(input("Inserisci il primo valore -> "))
y:int = int(input("Inserisci il secondo valore -> "))

if x < y:
    b=x
    a=y

elif x > y:
    a=x
    b=y

else:
    print("I numeri inseriti sono uguali")
    a=x
    b=y




def subtract(a:int,b:int) -> int:

    result = a-b

    return result




sottrazione:int = subtract (a,b)

print (sottrazione)

    