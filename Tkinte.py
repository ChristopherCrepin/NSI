from tkinter import *
from tkinter import Canvas
import random

fenetre = Tk()
label = Label(fenetre, text="Hello World!")
label.pack()
canvas=Canvas()
for i in range(1000000000000) :
    canvas.create_line([random.randint(0,200) for i in range(4)])
    canvas.pack()
Bouton_sortie = Button(fenetre, text="PTDR T KI", command=fenetre.quit)
Bouton_sortie.pack()
#fenetre.geometry("400x400+300+300")
fenetre.mainloop()
