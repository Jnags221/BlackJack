from tkinter import *
#from Main import *

class BlackJack(Frame):
    def __init__(self, master):
        super().__init__(master)

# Make window the size of the screen

        self.master = master
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()

        self.numplayersquestionlabel = Label(self, text = "How many players would like to play?")


        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(12):
            self.rowconfigure(row, minsize=self.screenheight / 12)
        self.homescreen()

    def homescreen(self):
        self.numplayersquestionlabel.grid(column = 5, row = 5, sticky = "news")


root = Tk()
root.title("BlackJack")
blackjack = BlackJack(root)
blackjack.pack(fill="both", expand=True)
root.mainloop()
