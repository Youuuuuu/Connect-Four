from game import *
class UI():
    def __init__(self,sign):
        self.game=ConnectFour(sign)
    
    def check(self,choice):
        if choice.isdigit()==False:
            raise ValueError("Please insert a valid choice!")
        if int(choice)!=1 and int(choice)!=2:
            raise ValueError("Please insert a valid choice!")
    
    def printBoard(self):
        table = Texttable()
        #table.set_deco(Texttable.HEADER)
        table.set_cols_align(["l", "r", "r","r","r","r","c"])
        table.set_cols_valign(["t", "m","m","m","m","m", "b"])
        newboard=[]
        board=self.game.get_board()
        for i in range(0,6):
            newboard.append([-1,-1,-1,-1,-1,-1,-1])
        for i in range(0,6):
            for j in range(0,7):
                if board[i][j]==-1:
                    newboard[i][j]='-'
                elif board[i][j]==0:
                    newboard[i][j]='O'
                else:
                    newboard[i][j]='X'
        table.add_rows([[1,2,3,4,5,6,7],newboard[0],newboard[1],newboard[2],newboard[3],newboard[4],newboard[5]])
        print (table.draw() + "\n")
        
    def __printWinningMessage(self, winner):
        '''
        winner=string=Player/Computer
        '''
        self.printBoard()
        print("END GAME")
        print(winner+" wins!")
            
    def run(self):
        choosePlayer()
        firstMove=input("Please enter your choice:")
        try:
            self.check(firstMove)
            if firstMove=='1':
                #this means that the computer starts
                computerMoves=1
                playerMoves=0
                column=random.choice([0,1,2,3,4,5,6]) 
            else:
                computerMoves=0
                playerMoves=1 #the player moves first
                print("You move first!")
            while True:
                if playerMoves==1:
                    #it is the player's turn
                    if self.game._checkForDraw()==True:
                        self.printBoard()
                        print("It is a draw.")
                        return
                    self.printBoard()
                    choice=input("Please input the column on which you want to put your 'disk':")
                    try: 
                        self.game._verifyColumn(choice)
                        column=int(choice)
                        column-=1
                        self.game._checkValidMove(column)
                        self.game._makeMove(column)
                        if self.game._gameWon():
                            self.__printWinningMessage('Player')
                            return
                        print("Wait until the computer makes its move!")
                        computerMoves=1
                        playerMoves=0
                    except ValueError as ve:
                        print(ve)
                        
                elif computerMoves==1:  
                    #it is the computer's turn
                    if self.game._checkForDraw():
                        print("It is a draw.")
                        return
                    self.game._computerMove('1',column)
                    if self.game._gameWon():
                        self.__printWinningMessage('Computer')
                        return
                    print("It's your turn now!")
                    computerMoves=0
                    playerMoves=1
        except ValueError as ve:
            print(ve)
        
        