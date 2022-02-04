import tkinter
from tkinter import *
from PIL import Image,ImageTk
# this root makes error write in coursework

#root = Tk()
def card_snipper():
    # Create a photoimage object of the image in the path
    image1 = Image.open('cards.png')
    cards = {}
    for i in range(4):
        for l in range(14):

            a = l*79
            b = i*123
            c = (l+1)*79
            d = (i+1)*123
            cropped = image1.crop((a,b,c,d)) #a = top left b = bottom left c = top right d = bottom right
            test = ImageTk.PhotoImage(cropped)
            label = tkinter.Label(image=test)
            label.image = test
            if i == 0:
                suit = str(i)
                rank = str(l+1)
                card = rank + " " + suit
                cards[card] = [label]
            if i == 1:
                suit = str(i)
                rank = str(l+1)
                card = rank + " " + suit
                cards[card] = [label]
            if i == 2:
                suit = str(i)
                rank = str(l+1)
                card = rank + " " + suit
                cards[card] = [label]
            if i == 3:
                suit = str(i)
                rank = str(l+1)
                card = rank + " " + suit
                cards[card] = [label]
    return cards

    #



#root.mainloop()