import tkinter
counter: int = 0
#settings main window
root = tkinter.Tk()
root.title("Paper rock scissor game")
root.minsize(300,300)
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


#GAME GUI
labelGameBoard = tkinter.Label(root,
                               text="PAPER ROCK SCISSORS GAME PRESS BUTTON TO START", fg="green", font="Helvetica 16 bold italic", justify="center", width=20, height=10)
labelGameBoard.grid(column=0, row=0, columnspan=2, sticky="WENS")

labelScore1 = tkinter.Label(root, bg="red", text="YOUR POINTS: ", width=10, height=10)
labelScore1.grid(column=0, row=2, sticky="WENS")
labelScore2 = tkinter.Label(root, text="OPPONENT POINTS: ")
labelScore2.grid(column=2, row=2, sticky="WENS")


img1 = tkinter.PhotoImage(file="paper.png")
button1 = tkinter.Button(root, image=img1, text="Paper(1)", command=count)
button1.grid(column=0, row=1, sticky="WENS")

img2 = tkinter.PhotoImage(file="rock.png")
button2 = tkinter.Button(root, image=img2, text="Rock(2)")
button2.grid(column=1, row=1, sticky="WENS")

img3 = tkinter.PhotoImage(file="scissors.png")
button3 = tkinter.Button(root, image=img3, text="Paper(1)")
button3.grid(column=2, row=1, sticky="WENS")





if __name__=="__main__":
    root.mainloop()
