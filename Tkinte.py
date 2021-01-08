from tkinter import *

fenetre = Tk()
label = Label(fenetre, text="Hello World!")
label.pack()
Bouton_sortie = Button(fenetre, text="PTDR T KI", command=fenetre.quit)
Bouton_sortie.pack()
fenetre.mainloop()
