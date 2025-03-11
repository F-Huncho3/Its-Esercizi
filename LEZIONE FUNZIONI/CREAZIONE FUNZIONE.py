
x:int = int(input("Inserisci il primo valore -> "))
y:int = int(input("Inserisci il secondo valore -> "))

if x > y:
    b=x
    a=y

elif x < y:
    a=x
    b=y

else:
    print("I numeri inseriti sono uguali")
    a=x
    b=y


    




def sommainteri (a:int, b:int):
    result:int = 0

    for i in range (a, b+1):
        result += i

    return result

sum = sommainteri(a,b)

print (sum)
