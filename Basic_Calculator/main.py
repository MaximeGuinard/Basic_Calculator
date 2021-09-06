from tkinter import *
import math
from tkinter.font import Font as f

def evaluer(event):
    chaine.configure(text="Resulat :"+str(eval(entree.get())))

#Programme Principale
fenetre = Tk()
fenetre.title("Calculatrice")
entree = Entry(fenetre,width=20)
entree.bind("<Return>", evaluer)
entree.config(font =f(size=30))
chaine = Label(fenetre,fg='green')
chaine.config(font = f(size=30))
entree.pack()
chaine.pack()
fenetre.mainloop()