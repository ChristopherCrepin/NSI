from tkinter import *
from tkinter import Canvas
import random

fenetre = None

def coul_alea() :
    COLORS = ['snow', 'blue', 'red', 'green','orange','yellow','pink']
    return random.choice(COLORS)

def sameplayerplayagain() :
    global fenetre
    if fenetre!=None:
        windows_close()
    fenetre = Tk()
    label = Label(fenetre, text="Surement une oeuvre d'art de picasso !")
    label.pack()
    canvas=Canvas()
    for i in range(10000) :
        canvas.create_line(random.randint(0,500),random.randint(0,500),random.randint(0,500),random.randint(0,500), fill=coul_alea())
        canvas.pack()
    Bouton_jaime = Button(fenetre, text="J'aime", command=sameplayerplayagain)
    Bouton_jaime.pack()
    Bouton_sortie = Button(fenetre, text="pas cool mec", command=windows_close)
    Bouton_sortie.pack()
    position = "400x400+" + str(random.randint(100,1200)) + "+" + str(random.randint(-300,700))
    fenetre.geometry(position)
    fenetre.mainloop()


def windows_close() :
    global fenetre
    fenetre.destroy()
    fenetre = None


sameplayerplayagain()
