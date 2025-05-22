#9-14. Lottery: Create a class LotteryMachine that holds a list containing a series of 10 numbers and 5 letters. Implement a method to randomly select 4 items (numbers or letters) from this list to draw a winning ticket. Finally, implement a method to display a message saying that any ticket matching the winning 4 items wins a prize.

import random

class LotteryMachine:

    def __init__ (self):

        self.numbersandletters_list = [1,"A",2,"B",3,"C",4,"D",5,"E",6,7,8,9,10]
        self.winning_list = []
        self.your_ticket = []


    def pick4char(self):

        self.winning_list(len)

        for x in range(1,5):

            self.winning_list.append(self.numbersandletters_list[random.randint(0,14)])

        return self.winning_list


    def pickyourticket(self):

        print("Chose 4 characters in this list")

        print(self.numbersandletters_list)

        print ("Do you feel lucky?")

        for i in range (1,5):

            char = str(input("Insert the character"))

            self.your_ticket.append(char)

        return print(f"This is your ticket {self.your_ticket}")



    def showWinningTicket(self):

        print(f"The winning ticket is {self.winning_list}\n")
        print("If your choice mactches the winning ticket you won!")


ticket1:LotteryMachine = LotteryMachine()
yourTicket : LotteryMachine = LotteryMachine()

ticket1.pick4char()


yourTicket.pickyourticket()

ticket1.showWinningTicket()










