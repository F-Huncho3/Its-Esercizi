#9-15. Lottery Analysis: Extend the LotteryMachine class you created in Exercise 9-14.

#1. Add a method called simulate_until_win(self, my_ticket) that:

    #Accepts a ticket (a list of 4 items).
    #Repeatedly draws random tickets using the draw_ticket() method.
    #Keeps count of how many attempts it takes until a randomly drawn ticket matches my_ticket.
    #Returns the number of attempts and the winning ticket.

#2. Create a ticket called my_ticket with 4 numbers or letters from the pool.

#3. Use the simulate_until_win() method to simulate how many draws it would take for your ticket to win.

#4. Print a message showing:

    #Your ticket
    #The winning ticket
    #How many attempts it took to win


import random

class LotteryMachine:

    def __init__ (self):

        self.numbersandletters_list = ["1","A","2","B","3","C","4","D","5","E","6","7","8","9","10"]
        self.winning_list = []
        self.your_ticket = []


    def pick4char(self):

        for x in range(1,5):

            self.winning_list.append(self.numbersandletters_list[random.randint(0,14)])

        return self.winning_list


    def pickyourticket(self):

        self.your_ticket = []

        print("Chose 4 characters in this list")

        print(self.numbersandletters_list)

        print ("Do you feel lucky?")

        for i in range (1,5):

            char = str(input("Insert the character"))

            self.your_ticket.append(char)

        return print(f"This is your ticket {self.your_ticket}")
    
    def simulate_untilwin(self):

        draws = 0


        while self.your_ticket != self.winning_list:

            
            self.pick4char()

            draws += 1 

            if self.winning_list !=self.your_ticket:

                self.winning_list = []

        print(f"You won in {draws} draws ")

            

        


    def showWinningTicket(self):

        print(f"The winning ticket is {self.winning_list}\n")
        print("If your choice mactches the winning ticket you won!")


ticket1:LotteryMachine = LotteryMachine()
yourTicket : LotteryMachine = LotteryMachine()


ticket1.pickyourticket()
ticket1.simulate_untilwin()
