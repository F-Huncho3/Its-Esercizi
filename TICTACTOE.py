#Griglia

from future import Player,Strategies
'''def rules(griglia:list[list[str]]):

    for riga in griglia:

        if riga[0] == riga[1] == riga[2] and riga != " ":

            if riga[0] == "X":

                return 10
            
            elif riga[0] == "O":

                return -10
            

    for colonna in range(3):

        if griglia[0][colonna] == griglia[1][colonna] == griglia[2][colonna] and griglia[0][colonna] != " ":

            if riga[0] == "X":

                return 10
            
            elif riga[0] == "O":

                return -10 '''



#CLASSE BOARD

#Inizializza una oggeto che crea una board inizialmente vuota
#Deve poter vedere lo stato attuale della board ed essere modificata dal Player
#La board deve avere uno stato finale che va a controllare se è piena e se c'è un tris o meno



class Board:

    def __init__(self):
        
        self.initialboard =[[" "," "," "],
                            [" "," "," "],
                            [" "," "," "]]
        
        self.statusboard = [[" "," "," "],
                            [" "," "," "],
                            [" "," "," "]]
        
    def get_status(self):

        return self.statusboard
    
    def add_move(self):

        self.statusboard = [[" "," "," "],
                            [" "," "," "],
                            [" "," "," "]]



        


        

        

class Player:

    def __init__(self):
        pass

    def movehuman(self, board:Board):

        board.get_status()



        print("Choose your block")

        block = int(input("Choose the number between 1 and nine"))

        match block:

            case 1:

                board[0][0] = "X"

            case 2:

                board[0][1] = "X"

            case 3:

                board[0][2] = "X"

            case 4:

                board[1][0] = "X"

            case 5:

                board[1][1] = "X"

            case 6:

                board[1][2] = "X"

            case 7:

                board[2][0] = "X"

            case 8:

                board[2][1] = "X"

            case 9:

                board[2][2] = "X"

        
        return board

        





class Strategies:

    def __init__(self):
        pass


    def  minimax(node, depth, maximizingPlayer):
        if depth == 0 or node is a terminal node then
            return the #heuristic value of node
        elif maximizingPlayer:
            value: float = -∞
            for node in depth:
                value: float = max(value, depth - 1, False)
            return value
        else:
            minimizingPlayer:Player
            value := +∞
            for each child of node do
            value := min(value, depth - 1, True)
            return value
    


            
        
    




           
        

    

    











        


            







