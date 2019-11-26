from player import Player
from texttable.texttable import *
from meniu import choosePlayer
import random
from tkinter.tix import COLUMN
import player
from turtledemo.minimal_hanoi import play

class ConnectFour():
    def __init__(self,sign):
        if int(sign)==1:
            self.__player=Player('O')
        else:
            self.__player=Player('X')
        self._board=self._drawBoard()
        self.__listOfBlockedColumns=[]

    def get_board(self):
        return self._board
            
    def _drawBoard(self):
        board=[]
        for i in range(0,6):
            board.append([-1,-1,-1,-1,-1,-1,-1])
        return board    

    def _verifyColumn(self,choice):
        if choice.isdigit()==False:
            raise ValueError("Please insert a number between 1-7.")
        if int(choice)<1 or int(choice)>7:
            raise ValueError("Please insert a number between 1-7.")
    
    def _checkValidMove(self, column):
        if self._board[0][column]!=-1:
            raise ValueError("Invalid move! This column is already full!")
        return
    
    def _makeMove(self, column,sign=12):
        if sign==12:
            sign=self.__player.get_sign()
        if sign=='O':
            filling=0
        elif sign=='X':
            filling=1
        for i in range (5,-1,-1):
            if self._board[i][column]==-1:
                self._board[i][column]=filling
                return
            
    def __checkCoord(self,x,y):
        '''
        x-the row
        y-the collumn
        '''
        if x<0:
            return False
        if x>5:
            return False
        if y<0:
            return False
        if y>6:
            return False
        if self._board[x][y]!=-1:
            return False
        return True

    def __fromLeftToRight(self,sign):
        for i in range(5,-1,-1):
            countO=0
            if self._board[i]==[-1,-1,-1,-1,-1,-1,-1]:
                return [-1,-1]
            for j in range(0,6):
                if self._board[i][j]==sign:
                    countO+=1
                    if countO==3:
                        if j+1<=6 and self._board[i][j+1]==-1:
                            return [i*(-1),j+1]
                        i-=1
                    if countO==2:
                        if j+2<=6 and self._board[i][j+1]==-1 and self._board[i][j+2]==sign:
                            return [i*(-1),j+1]
                        elif j-3>=0 and self._board[i][j-3]==sign and self._board[i][j-2]==-1:
                            return [i*(-1),j-2]
                else:
                    countO=0
        return [-1,-1]
    
    def __fromRightToLeft(self, sign):
        for i in range(5,-1,-1):
            if self._board[1]==[-1,-1,-1,-1,-1,-1,-1]:
                return [-1,-1]
            countO=0
            for j in range(6,-1,-1):
                if self._board[i][j]==sign:
                    countO+=1
                    if countO==2 or countO==3:
                        if j-1>=0 and self._board[i][j-1]==-1:
                                return [i,j-1]
                else:
                    countO=0
        return [-1,-1]
    
    def __distance(self,row,column):
        height1=5-row
        height2=0
        for i in range(0,6):
            if self._board[i][column]!=-1:
                height2+=1
        diff=height1-height2
        return diff
    
    def _checkLinesAI(self,sign,parcing):
        '''
        parcing=0=left to right
                1=right to left
        output:list: [line,column]
        '''
        if parcing==0:
            coordinates1=self.__fromLeftToRight(sign)
        else:
            coordinates1=self.__fromRightToLeft(sign)
        return coordinates1

    def _checkColumnsAI(self,sign):
        for j in range(0,7):
            #when we move to a new column, we reset the counter
            countO=0
            for i in range(5,-1,-1):
                if self._board[i][j]==sign:
                    countO+=1
                    if countO==3:
                        if i-1>=0 and self._board[i-1][j]==-1 and j not in self.__listOfBlockedColumns:
                            return [i-1,j]
                        countO=0
                        j+=1
                else:
                    countO=0
        return [-1,-1]
    

    def __left(self,sign):
        #verifica diagonalele oblice spre stanga
        #sub diagonala principala
        for k in range(0,6):
            countO=0
            countO1=0
            countO0=0
            countO11=0
            for j in range(0,7):
                for i in range(0,6):
                    if i-j==k:
                        if self._board[i][j]==sign:
                            countO0+=1
                            if countO0==3:
                                if self.__checkCoord(i+1, j+1)==True:
                                    return [i,j+1]
                        else:
                            countO0=0
                    #deasupra diagonalei principale
                    if j-i==k:
                        if self._board[i][j]==sign:
                            countO11+=1
                            if countO11==3:
                                if self.__checkCoord(i+1, j+1)==True:
                                    return [i,j+1]
                        else:
                            countO11=0
            for j in range(6,-1,-1):
                for i in range(5,-1,-1):
                    if i-j==k:
                        if self._board[i][j]==sign:
                            countO+=1
                            if countO==3:
                                if self.__checkCoord(i-1, j-1)==True:
                                    return [i,j-1]
                            if countO==2:
                                if j-2>=0 and i-2>=0 and self._board[i-1][j-1]==-1 and self._board[i-2][j-2]==sign:
                                    return [i,j-1]
                                if j+3<=6 and i+3<=5 and self._board[i+2][j+2]==-1 and self._board[i+3][j+3]==sign:
                                    return [i,j+2]
                        else:
                            countO=0
                    #deasupra diagonalei principale
                    if j-i==k:
                        if self._board[i][j]==sign:
                            countO1+=1
                            if countO1==3:
                                if self.__checkCoord(i-1, j-1)==True:
                                    return [i-1,j-1]
                            if countO==2:
                                if j-2>=0 and i-2>=0 and self._board[i-1][j-1]==-1 and self._board[i-2][j-2]==sign:
                                    return [10,j-1]
                                if j+3<=6 and i+3<=5 and self._board[i+2][j+2]==-1 and self._board[i+3][j+3]==sign:
                                    return [10,j+2]
                        else:
                            countO1=0
        return [-1,-1]
    
    
    def __right(self, sign):
        #verifica diagonalele oblice spre dreapta
        for k in range(1,11):
            countO=0
            countO1=0
            for j in range(6,-1,-1):
                for i in range(0,6):
                    if i+j==k:
                        if self._board[i][j]==sign:
                            countO1+=1
                            if countO1==3:
                                if self.__checkCoord(i+1, j-1)==True:
                                    return [i*(-1),j-1]
                        else:
                            countO1=0
            for j in range(0,7):
                for i in range(5,-1,-1):
                    if i+j==k:
                        if self._board[i][j]==sign:
                            countO+=1
                            if countO==3:
                                if self.__checkCoord(i-1, j+1)==True:
                                    return [i*(-1),j+1]
                            if countO==2:
                                if j+2<=6 and i-2>=0 and self._board[i-1][j+1]==-1 and self._board[i-2][j+2]==sign:
                                    return [i*(-1),j+1]
                                if j-3>=0 and i+3<=5 and self._board[i+2][j-2]==-1 and self._board[i+3][j-3]==sign:
                                    return [i*(-1),j-2]
                        else:
                            countO=0
            
        return [-1,-1]
    
    def _checkDiagonalsAI(self,sign,direction):
        '''
        direction=0=cele oblice spre stanga
                =1=cele oblice spre dreapta
        '''
        if direction==0:
            return self.__left(sign)
        elif direction==1:
            return self.__right(sign)
    
    def __checkAbove(self, row,column,sign):
        '''
        returns true if it is safe to put a disk of opposite sign below and false otherwise
        '''
        if row<0:
            return True
        count=0
        for i in range(0,column):
            if self._board[row][i]==sign:
                count+=1
            else:
                count=0
            if count==3:
                return False
        return True
    
    def __findFavorableMove(self):
        
        coordinates=self._checkLinesAI(1,0)
        if coordinates!=[-1,-1]:
            diff=self.__distance(coordinates[0]*(-1)-1, coordinates[1])
            if diff==1:# and self.__checkAbove(coordinates[0],0):
                return coordinates[1]
        coordinates=self._checkLinesAI(1, 1)
        if coordinates!=[-1,-1]:
            diff=self.__distance(coordinates[0]-1, coordinates[1])
            if diff==1 and self._board[coordinates[0]][coordinates[1]-1]!=0:# and self.__checkAbove(coordinates[0],0):
                return coordinates[1]
          
        coordinates=self._checkDiagonalsAI(1,1)
        if coordinates!=[-1,-1]:
                #if self._board[coordinates[0]-1][coordinates[1]-1]==1 and self.__distance(coordinates[0]*(-1), coordinates[1])==0:
                return coordinates[1]
        coordinates=self._checkDiagonalsAI(1,0)
        if coordinates!=[-1,-1]:
            if self._board[coordinates[0]+1][coordinates[1]+1]==1:
                if self._board[coordinates[0]-1][coordinates[1]-1]==1 or self._board[coordinates[0]-1][coordinates[1]-1]==-1:
                    return coordinates[1]
            
        coordinates=self._checkColumnsAI(1)
        if coordinates!=[-1,-1]:
            self.__listOfBlockedColumns.append(coordinates[1])
            return coordinates[1]
        return -1
    
    def __blockOponent(self,playersLastColumn):
        #then we try to block any movement in the vertical axis (on the columns)
        coordinates=self._checkColumnsAI(0)
        if coordinates!=[-1,-1]:
            self.__listOfBlockedColumns.append(coordinates[1])
            return coordinates[1]
        
        #we check the diagonals
        coordinates=self._checkDiagonalsAI(0,1)
        if coordinates!=[-1,-1]:
            if self._board[coordinates[0]][coordinates[1]]!=-1:
                return coordinates[1]
        coordinates=self._checkDiagonalsAI(0,0)
        if coordinates!=[-1,-1]:
            if self._board[coordinates[0]][coordinates[1]]!=-1:
                return coordinates[1]
             
        coordinates=self._checkLinesAI(0,0)
        if coordinates!=[-1,-1]:
            diff=self.__distance(coordinates[0]*(-1)-1, coordinates[1])
            if diff==1 and self.__checkAbove(coordinates[0]-1,coordinates[1],0):
                return coordinates[1]
        coordinates=self._checkLinesAI(0, 1)
        if coordinates!=[-1,-1]:
            diff=self.__distance(coordinates[0]-1, coordinates[1])
            if diff==1 and self.__checkAbove(coordinates[0]-1,coordinates[1],0):
                return coordinates[1]
        
        #then we try to block any movement in the orizontal axis(on the rows)
        if playersLastColumn>3:
            if playersLastColumn-1>=0 and self._board[5][playersLastColumn-1]==-1 and self._board[5][playersLastColumn]==0:
                return playersLastColumn-1
        elif playersLastColumn<3:
            if playersLastColumn+1<=6 and self._board[5][playersLastColumn+1]==-1 and self._board[5][playersLastColumn]==0:
                return playersLastColumn+1
        return -1
    
    
    def __findValidColumn(self, playersLastColumn):
        '''
        this function determines a column on which a move can be made
        OUTPUT:column=integer between 0 and 6
        '''
        #we try to see where is the most favorable place to put our piece:
        column=self.__findFavorableMove()
        if column!=-1:
            return column
        #we try to block the oponent
        column=self.__blockOponent(playersLastColumn)
        if column!=-1:
            return column
        #If we cannot block a future move, we choose a random position
        for i in range(0,7):
            if self._board[5][i]==-1:
                if i-1>=0 and i+1<=6:
                    if self._board[5][i+1]!=-1 or self._board[5][i-1]!=-1:
                        return i
                elif i==0:
                    if self._board[5][i+1]!=-1:
                        return i
                elif i==6:
                    if self._board[5][i-1]!=-1:
                        return i
        if self._board[0][playersLastColumn]==-1:
            choicee=random.choice([1,2,3])
            if playersLastColumn==0 and choicee==1:
                choicee=2
            if playersLastColumn==6 and choicee==3:
                choicee=2
            if choicee==1:
                return playersLastColumn
            if choicee==2:
                return playersLastColumn
            if choicee==3:
                return playersLastColumn   
        #if we are here with the execution, it means that the player's last choice is a full column
        else:
            if playersLastColumn==0:
                return self.__findValidColumn(1)
            elif playersLastColumn==6:
                return self.__findValidColumn(5)
            else:
                number=random.choice([1,2])
                if number==1:
                    return self.__findValidColumn(playersLastColumn+1)
                else:
                    return self.__findValidColumn(playersLastColumn-1)
    
    def _computerMove(self,sign,PlayersLastcolumn):
        playerSign=self.__player.get_sign()
        if playerSign=='O':
            computerSign='X'
        else:
            computerSign='O'
        ok=0
        while(ok==0):
            try:
                column=self.__findValidColumn(PlayersLastcolumn)
                self._checkValidMove(column)
                ok=1
            except ValueError:
                pass
        self._makeMove(column, computerSign)
        
    def _checkForDraw(self):
        for i in range(0,6):
            if -1 in self._board[i]:
                return False
        return True
           
    def _gameWon(self):
        '''
        This functions checks whether the game is won or not
        OUTPUT:boolean:False-if the game can continue
                        True-if the game will stop
        '''
        result1=self._checkLines()
        result2=self._checkColumns()
        result3=self._checkDiagonals()
        print(result1,result2,result3)
        return result1 or result2 or result3
    
    def _checkLines(self):
        '''
        return true if there is a formation of 4 on lines and false otherwise
        '''
        for i in range(0,6):
            countO=0
            countX=0
            if self._board[i]==[-1,-1,-1,-1,-1,-1,-1]:
                i+=1
            for j in range(0,7):
                if self._board[i][j]==0:
                    countO+=1
                    countX=0
                    if countO==4:
                        return True
                elif self._board[i][j]==1:
                    countX+=1
                    countO=0
                    if countX==4:
                        return True
        return False
    
    def _checkColumns(self):
        '''
        returns true if there is a formation of 4 on a column and false otherwise
        '''
        for j in range(0,7):
            countO=0
            countX=0
            for i in range(0,6):
                if self._board[i][j]==0:
                    countO+=1
                    countX=0
                    if countO==4:
                        return True
                elif self._board[i][j]==1:
                    countX+=1
                    countO=0
                    if countX==4:
                        return True
        return False
    
    def _checkDiagonals(self):
        '''
        returns true if there is a formation of 4 on a diagonal and false otherwise
        '''
        #verifica diagonalele oblice spre dreapta
        for k in range(1,11):
            countO=0
            countX=0
            for j in range(0,7):
                for i in range(0,6):
                    if i+j==k:
                        if self._board[i][j]==0:
                            countO+=1
                            countX=0
                            if countO==4:
                                return True
                        elif self._board[i][j]==1:
                            countX+=1
                            countO=0
                            if countX==4:
                                return True
                        else:
                            countX=0
                            countO=0
        #verifica diagonalele oblice spre stanga
        #sub diagonala principala
        for k in range(0,6):
            countO=0
            countX=0
            countO1=0
            countX1=0
            for j in range(0,7):
                for i in range(0,6):
                    if i-j==k:
                        if self._board[i][j]==0:
                            countO+=1
                            countX=0
                            if countO==4:
                                return True
                        elif self._board[i][j]==1:
                            countX+=1
                            countO=0
                            if countX==4:
                                return True
                        else:
                            countX=0
                            countO=0
        #deasupra diagonalei principale
                    if j-i==k:
                        if self._board[i][j]==0:
                            countO1+=1
                            countX1=0
                            if countO1==4:
                                return True
                        elif self._board[i][j]==1:
                            countX1+=1
                            countO1=0
                            if countX1==4:
                                return True
                        else:
                            countX1=0
                            countO1=0
        return False      
    board = property(get_board, None, None, None)
        
import unittest
class TestGame(unittest.TestCase):
    def setUp(self):
        self.game=ConnectFour(1)
        self.board1=   [[-1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1],
                        [0, 0, 0, 0, -1, -1, -1]]
        
        self.board2=   [[-1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, 1, -1, -1, -1],
                        [-1, -1, -1, 1, -1, -1, -1],
                        [-1, -1, -1, 1, -1, -1, -1],
                        [-1, -1, -1, 1, -1, -1, -1]]
        
        self.board3=   [[-1, -1, -1, -1, -1, 0, -1],
                        [-1, -1, -1, -1, 0, -1, -1],
                        [-1, -1, -1, 0, -1, -1, -1],
                        [-1, -1, 0, -1, -1, -1, -1],
                        [-1, 1, -1, -1, -1, -1, -1],
                        [0, -1, -1, -1, -1, -1, -1]]
        
        self.board4=   [[-1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, 1, -1, -1, -1],
                        [-1, -1, 1, -1, -1, -1, -1],
                        [-1, 1, -1, -1, -1, -1, -1],
                        [-1, 0, 0, 0, -1, -1, -1]]
        
        self.board5=   [[-1, -1, -1, -1, -1, -1, -1],
                        [-1, -1, -1, -1, -1, -1, -1],
                        [-1, 0, -1, 0, -1, -1, -1],
                        [-1, -1, 0, -1, -1, -1, -1],
                        [-1, -1, -1, 0, -1, -1, -1],
                        [0, -1, -1, -1, 0, -1, -1]]
        
    def tearDown(self):
        self.game=None
        self.board1=None
        self.board2=None
        self.board3=None
        self.board4=None
        self.board5=None
        
            
    def testBoard(self):
        board=self.game._drawBoard()
        for i in range(0,6):
            #print(board[i])
            pass
    def test_verifyColumn(self):
        self.game._verifyColumn('1')
        with self.assertRaises(ValueError):
            self.game._verifyColumn('dsdd')
        with self.assertRaises(ValueError):
            self.game._verifyColumn('8') 
        self.game.printBoard()
    
    def test_checkValidMove(self):
        for i in range(0,6):
            self.game._checkValidMove(1)
            if i%2==0:
                self.game._makeMove(1, 'O')
            else:
                self.game._makeMove(1, 'X')
        with self.assertRaises(ValueError):
            self.game._checkValidMove(1)    
    def test_checkBoardWin(self):
        ok=0
        for i in range(0,6):
            countO=0
            countX=0
            if self.board1[i]==[-1,-1,-1,-1,-1,-1,-1]:
                i+=1
            for j in range(0,7):
                if self.board1[i][j]==0:
                    countO+=1
                    countX=0
                    if countO==4:
                        ok=1
                elif self.board1[i][j]==1:
                    countX+=1
                    countO=0
                    if countX==4:
                        ok=1
        assert ok==1
        ok=0
        for j in range(0,7):
            countO=0
            countX=0
            for i in range(0,6):
                if self.board2[i][j]==0:
                    countO+=1
                    countX=0
                    if countO==4:
                        ok=1
                elif self.board2[i][j]==1:
                    countX+=1
                    countO=0
                    if countX==4:
                        ok=1
                else:
                    countO=0
                    countX=0
        assert ok==1
        ok=0
        for k in range(1,11):
            countO=0
            countX=0
            for j in range(0,7):
                for i in range(0,6):
                    if i+j==k:
                        if self.board3[i][j]==0:
                            countO+=1
                            countX=0
                            if countO==4:
                                ok=1
                        elif self.board3[i][j]==1:
                            countX+=1
                            countO=0
                            if countX==4:
                                ok=1
                        else:
                            countX=0
                            countO=0
        assert ok==1
        ok=0
        for k in range(0,6):
            countO=0
            countX=0
            for j in range(6,-1,-1):
                for i in range(5,-1,-1):
                    if i-j==k:
                        if self.board5[i][j]==0:
                            countO+=1
                            countX=0
                            if countO==4:
                                ok=1
                        elif self.board5[i][j]==1:
                            countX+=1
                            countO=0
                            if countX==4:
                                ok=1
                        else:
                            countX=0
                            countO=0
        for k in range(0,6):
            countO=0
            countX=0
            for j in range(6,-1,-1):
                for i in range(5,-1,-1):
                    if j-i==k:
                        if self.board5[i][j]==0:
                            countO+=1
                            countX=0
                            if countO==4:
                                ok=1
                        elif self.board5[i][j]==1:
                            countX+=1
                            countO=0
                            if countX==4:
                                ok=1
                        else:
                            countX=0
                            countO=0
        assert ok==1
        
        ok=0
        for i in range(0,6):
            countO=0
            countX=0
            if self.board4[i]==[-1,-1,-1,-1,-1,-1,-1]:
                i+=1
            for j in range(0,7):
                if self.board4[i][j]==0:
                    countO+=1
                    countX=0
                    if countO==4:
                        ok=1
                elif self.board4[i][j]==1:
                    countX+=1
                    countO=0
                    if countX==4:
                        ok=1
        assert ok==0
        ok=0
        for j in range(0,7):
            countO=0
            countX=0
            for i in range(0,6):
                if self.board4[i][j]==0:
                    countO+=1
                    countX=0
                    if countO==4:
                        ok=1
                elif self.board4[i][j]==1:
                    countX+=1
                    countO=0
                    if countX==4:
                        ok=1
                else:
                    countO=0
                    countX=0
        assert ok==0
        ok=0
        for k in range(1,11):
            countO=0
            countX=0
            for j in range(0,7):
                for i in range(0,6):
                    if i+j==k:
                        if self.board4[i][j]==0:
                            countO+=1
                            countX=0
                            if countO==4:
                                ok=1
                        elif self.board4[i][j]==1:
                            countX+=1
                            countO=0
                            if countX==4:
                                ok=1
                        else:
                            countX=0
                            countO=0
        assert ok==0
        ok=0
        for k in range(0,6):
            countO=0
            countX=0
            for j in range(0,7):
                for i in range(0,6):
                    if i-j==k:
                        if self.board4[i][j]==0:
                            countO+=1
                            countX=0
                            if countO==4:
                                ok=1
                        elif self.board4[i][j]==1:
                            countX+=1
                            countO=0
                            if countX==4:
                                ok=1
                        else:
                            countX=0
                            countO=0
        for k in range(0,6):
            countO=0
            countX=0
            for j in range(0,7):
                for i in range(0,6):
                    if j-i==k:
                        if self.board4[i][j]==0:
                            countO+=1
                            countX=0
                            if countO==4:
                                ok=1
                        elif self.board4[i][j]==1:
                            countX+=1
                            countO=0
                            if countX==4:
                                ok=1
                        else:
                            countX=0
                            countO=0
        assert ok==0
        