from tkinter import *
from game import ConnectFour
import random
from random import choice

class GUI(ConnectFour):
    def __init__(self):
        self.__window=Tk()
        self.__window.title('Connect-Four!')
        self.__window.config(background='black')
        self.__buttonColumn1=Button(self.__window,text='1',width=8,command=lambda: self.__column(0)).grid(row=0,column=1,sticky=E)
        self.__buttonColumn2=Button(self.__window,text='2',width=8,command=lambda: self.__column(1)).grid(row=0,column=2,sticky=E)
        self.__buttonColumn3=Button(self.__window,text='3',width=8,command=lambda: self.__column(2)).grid(row=0,column=3,sticky=E)
        self.__buttonColumn4=Button(self.__window,text='4',width=8,command=lambda: self.__column(3)).grid(row=0,column=4,sticky=E)
        self.__buttonColumn5=Button(self.__window,text='5',width=8,command=lambda: self.__column(4)).grid(row=0,column=5,sticky=E)
        self.__buttonColumn6=Button(self.__window,text='6',width=8,command=lambda: self.__column(5)).grid(row=0,column=6,sticky=E)
        self.__buttonColumn7=Button(self.__window,text='7',width=8,command=lambda: self.__column(6)).grid(row=0,column=7,sticky=E)
        self.__buttonHelp=Button(self.__window,text='Help',width=10,command=self.__help).grid(row=0,column=12,sticky=E)
        for i in range(0,6):
            for j in range(0,7):
                self.__output=Text(self.__window,width=8,height=4,wrap=WORD, background='white')
                self.__output.grid(row=i+1,column=j+1,columnspan=1,sticky=W)
        self.__outputConsole=Text(self.__window,width=20,height=25,wrap=WORD, background='white')
        self.__outputConsole.grid(row=1,column=12,rowspan=7,sticky=W)
        ConnectFour.__init__(self, '1')        
        
    def __popUp(self,message):
        popup=Tk()
        popup.wm_title("Finish")
        message=str(message)
        label=Label(popup,text=message,font='Verdana 10')
        label.grid(row=1,column=1,sticky=W)
        button1=Button(popup,text='Okay',command=popup.destroy)
        button1.grid(row=2,column=1,sticky=E)
        popup.mainloop() 
    
    def __popUpFinish(self,winMessage): 
        popup=Tk()
        popup.wm_title("End of game")
        message=str(winMessage)+"\nDo you want to start again?"
        label=Label(popup,text=message,font='Verdana 10')
        label.grid(row=1,column=2)
        button1=Button(popup,text='Yes!:)',command=lambda: self.__restart(popup))
        button2=Button(popup,text='No!:(',command=lambda: self.__finish(popup))
        button1.grid(row=3,column=2,sticky=W)
        button2.grid(row=3,column=2,sticky=E)
        popup.mainloop()
        
    def __popUpChoice(self):
        popup=Tk()
        popup.wm_title("Choose")
        message='Please choose which one you want to begin first:'
        label=Label(popup,text=message,font='Verdana 10')
        label.grid(row=1,column=1,sticky=W)
        button1=Button(popup,text='Player',command=popup.destroy)
        button1.grid(row=2,column=1,sticky=W)
        button2=Button(popup,text='Computer',command=lambda: self.__computerMove(popup))
        button2.grid(row=2,column=1,sticky=E)
        popup.mainloop()
     
    def __computerMove(self,popup):
        popup.destroy()
        self.__outputConsole.insert(END,"Please wait while the computer makes its move.\n")
        column=random.choice([0,1,2,3,4,5,6])  
        self._computerMove('O', column)
        self.__outputConsole.insert(END,"Now it's your turn!\n")
        self.__printGameBoard()
        self.__outputConsole.insert(END,"Now it's your turn!\n")
        
    def __column(self,column):
        try:
            self._verifyColumn(str(column+1))
            self._checkValidMove(column)
            self._makeMove(column, 'O')
            self.__printGameBoard()
            self.__outputConsole.insert(END,"Please wait while the computer makes its move.\n")
            if self._checkForDraw():
                self.__popUpFinish("END GAME\n It is a draw!")
            if self._gameWon():
                self.__popUpFinish("END GAME\n You win!")
            self._computerMove('O', column)
            self.__outputConsole.insert(END,"Now it's your turn!\n")
            self.__printGameBoard()
            if self._checkForDraw():
                self.__popUpFinish("END GAME\n It is a draw!")
            if self._gameWon():
                self.__popUpFinish("END GAME\n Computer wins!")
        except ValueError as ve:
            self.__popUp(ve)
    
    def __restart(self,popup):
        popup.destroy()
        self.__outputConsole.delete(0.0, END)
        self._board=self._drawBoard()
        self.__printGameBoard()
        self.__popUpChoice()
        
    def __finish(self,popup):
        popup.destroy()
        self.__window.quit() 
        
    def __printGameBoard(self):
        for i in range(0,6):
            for j in range(0,7):
                if self._board[i][j]==-1:
                    self.__output=Text(self.__window,width=8,height=4,wrap=WORD, background='white')
                    self.__output.grid(row=i+1,column=j+1,columnspan=1,sticky=W)
                elif self._board[i][j]==0:
                    self.__output=Text(self.__window,width=8,height=4,wrap=WORD, background='yellow')
                    self.__output.grid(row=i+1,column=j+1,columnspan=1,sticky=W)
                else:
                    self.__output=Text(self.__window,width=8,height=4,wrap=WORD, background='red')
                    self.__output.grid(row=i+1,column=j+1,columnspan=1,sticky=W)
                    
        
    def __help(self):
        message=""
        message+='INSTRUCTIONS!\n'
        message+='How to play Connect Four:\n'
        message+="Select a column on which you want your 'piece' to be placed.\n"
        message+="The 'pieces' fall straight down, occupying the lowest available space within the column.\n"
        message+="The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of your own discs.\n"
        message+="Your disks color is yellow."
        self.__popUp(message)
        
    def run(self):
        #self.__popUp("Great! You have the sign 'O' and computer has the sign 'X'. GOOD lUCK!")
        self.__popUpChoice()
        self.__window.mainloop()
        
#gui=GUI()
#gui.run()
