#4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

numeri:list[int] = []
x = 0

for i in range (1000001):
    print (x)
    x +=1 
    numeri.append(x)


    