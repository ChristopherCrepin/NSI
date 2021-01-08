from tkinter import *
from tkinter import Canvas
import random
def coul_alea() :
    COLORS = ['snow', 'blue', 'red', 'green','orange','yellow','pink']
    return random.choice(COLORS)
fenetre = Tk()
label = Label(fenetre, text="Hello World!")
label.pack()
canvas=Canvas()
for i in range(1000000) :
    canvas.create_line(random.randint(0,500),random.randint(0,500),random.randint(0,500),random.randint(0,500), fill=coul_alea())
    canvas.pack()
Bouton_sortie = Button(fenetre, text="PTDR T KI", command=fenetre.quit)
Bouton_sortie.pack()
#fenetre.geometry("400x400+300+300")
fenetre.mainloop()
