#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
#• Add a new pizza to the original list.
#• Add a different pizza to the list friend_pizzas.
#• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

pizzas:list[str] = ["Margherita", "Fiori di zucca e alici", "Crostino"]

friend_pizzas:list[str] = ["Margherita", "Fiori di zucca e alici", "Crostino"]

pizzas.append("Speck")

friend_pizzas.append("Provola")

for pizza in pizzas:
    print (f"My favourite pizzas are {pizza}")