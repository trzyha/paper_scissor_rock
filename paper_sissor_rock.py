from tkinter import *
from time import sleep
from random import randint
counter: int = 0
#settings main window
root = Tk()
root.title("Paper rock scissor game")
root.minsize(900,800)
root.geometry("450x450")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
#
def count():
    global counter
    counter +=1
    labelGameBoard.config(text=str(labelGameBoard))
    labelGameBoard.after(1000, count)


def FinalCountdown():
    labelGameBoard['font'] = ("Helvetica 30 bold italic")
    labelGameBoard['fg'] = "red"
    for x in range(3, 0, -1):
        print(x)

        labelGameBoard['text']=x
        root.update_idletasks()
        sleep(1)
    labelGameBoard['text'] = ""
    #WhoWin()

"""def WhoWin()
    x = randint(1,3)
    print(x)
    if x = 1:
        labelGameBoard[]"""

#GAME GUI
labelGameBoard = Label(root, text="PAPER ROCK SCISSORS GAME PRESS BUTTON TO START",
                       fg="green", font="Helvetica 16 bold italic", justify="center", width=20, height=10)
labelGameBoard.grid(column=0, row=0, columnspan=2, sticky="WENS")

labelScore1 = Label(root, bg="red", text="YOUR POINTS: ", width=10, height=10)
labelScore1.grid(column=0, row=2, sticky="WENS")
labelScore2 = Label(root, text="OPPONENT POINTS: ")
labelScore2.grid(column=2, row=2, sticky="WENS")


img1 = PhotoImage(file="paper.png")
#img1 = Resize_Image(Image.open("paper.png"),100)
button1 = Button(root, image=img1, text="Paper(1)", command=FinalCountdown)
button1.grid(column=0, row=1, sticky="WENS")



img2 = PhotoImage(file="rock.png")
button2 = Button(root, image=img2, text="Rock(2)")
button2.grid(column=1, row=1, sticky="WENS")

img3 = PhotoImage(file="scissors.png")
button3 = Button(root, image=img3, text="Paper(1)")
button3.grid(column=2, row=1, sticky="WENS")


if __name__=="__main__":
    root.mainloop()
