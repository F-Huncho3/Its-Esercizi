#9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.

import random


class Dice:

    def __init__(self, sides:int = 6):

        self.sides = sides


    def roll_dice(self):

        roll= random.randint(1,self.sides)

        return roll
    
dice6:Dice = Dice()
dice10:Dice = Dice(10)
dice20:Dice = Dice(20)


for i in range(1,11):

    print(dice6.roll_dice())

print ("------------------")

for i in range(1,11):

    print(dice10.roll_dice())

print ("------------------")


for i in range(1,11):

    print(dice20.roll_dice())


        