import tkinter
from random import randint

playerPoint = 0
oponentPoint = 0

#settings main window
root = tkinter.Tk()
root.title("Paper rock scissor game")
root.minsize(600,400)
root.geometry("450x450")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
#

def oponentScore():
	global oponentPoint
	oponentPoint += 1
	labelScore2["text"] = ("OPONENT POINTS: " + str(oponentPoint))
	print ("Player: " + str(oponentPoint))

def playerScore():
	global playerPoint
	playerPoint += 1
	labelScore1["text"] = ("YOUR POINTS: " + str(playerPoint))
	print ("Oponent " + str(playerPoint))


def gameMechanics(x):
    print(x)
    oponentChoice = randint(1,3)
    #print(oponentChoice)    
    if x==1 and oponentChoice==1:
    	print("draw")
    elif x==1 and oponentChoice==2: 
    	print("you won!")
    	playerScore()
    elif x==1 and oponentChoice==3: 
    	print("you lost!")
    	oponentScore()
    elif x==2 and oponentChoice==1: 
    	print("you lost!")
    	oponentScore()      	
    elif x==2 and oponentChoice==2: 
    	print("draw")    	
    elif x==2 and oponentChoice==3: 
    	print("you won!")
    	playerScore()  
    elif x==3 and oponentChoice==1: 
    	print("you won!")
    	playerScore()   
    elif x==3 and oponentChoice==2: 
    	print("you lost!")
    	oponentScore()
    elif x==3 and oponentChoice==3: 
    	print("draw") 
    print("Player " + str(playerScore))
    print("Oponent " + str(oponentScore))

#GAME GUI
labelGameBoard = tkinter.Label(root,
                               text="PAPER ROCK SCISSORS GAME PRESS BUTTON TO START", fg="green", font="Helvetica 16 bold italic", justify="center", width=20, height=10)
labelGameBoard.grid(column=0, row=0, columnspan=2, sticky="WENS")

labelScore1 = tkinter.Label(root, bg="red", text=("YOUR POINTS: " + str(playerPoint)), width=10, height=10)
labelScore1.grid(column=0, row=2, sticky="WENS")
labelScore2 = tkinter.Label(root, text="OPPONENT POINTS: " + str(oponentPoint))
labelScore2.grid(column=2, row=2, sticky="WENS")


img1 = tkinter.PhotoImage(file="paper.png")
button1 = tkinter.Button(root, image=img1, text="Paper(1)", command=lambda: gameMechanics(1))
button1.grid(column=0, row=1, sticky="WENS")

img2 = tkinter.PhotoImage(file="rock.png")
button2 = tkinter.Button(root, image=img2, text="Rock(2)", command=lambda: gameMechanics(2))
button2.grid(column=1, row=1, sticky="WENS")

img3 = tkinter.PhotoImage(file="scissors.png")
button3 = tkinter.Button(root, image=img3, text="Paper(1)", command=lambda: gameMechanics(3))
button3.grid(column=2, row=1, sticky="WENS")





if __name__=="__main__":
    root.mainloop()
