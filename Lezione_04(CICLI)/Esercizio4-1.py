pizzas:list[str] = ["Margherita", "Fiori di zucca e alici", "Crostino"]

for pizza in pizzas:
    print (pizza)

for pizza in pizzas:
    print (f"I like pizza {pizza}")


i = 0 
while i <1 :
    print (f"I really love the {pizzas[0]}")

    i += 1 

while i == 1: 
    print (f"The taste of {pizzas[1]} is amazing")
    i += 1 

while i == 2: 
    print (f"The pizza {pizzas[2]} is my favourite")
    i +=1

if i == 3:
    print ("I really love pizza")