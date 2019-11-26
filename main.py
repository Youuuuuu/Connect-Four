from game import ConnectFour
from meniu import chooseSign, chooseUI
from GUI import GUI
from UI import UI

def check(choice):
    if choice.isdigit()==False:
        raise ValueError("Please insert a valid choice!")
    if int(choice)!=1 and int(choice)!=2:
        raise ValueError("Please insert a valid choice!") 
    
def main(): 
    while True:    
        try:
            chooseSign()
            choice=input("Please insert the number of your choice: ")
            check(choice)
            if int(choice)==2:
                return
            elif int(choice)==1:
                chooseUI()
                choice1=input("Please insert the number of your choice: ")
                check(choice1)
                if choice1=='1':
                    print("Great! You have the sign 'O' and computer has the sign 'X'. GOOD lUCK!")
                    ui=UI(choice)
                    ui.run()
                else:
                    gui=GUI()
                    gui.run()  
        except ValueError as ve:
            print(ve)

main()
