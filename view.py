from tkinter import *


class View:
    def cmd_calcul(self):
        print("C'est ici que l'on calcule")
        print("le poids est", self.var_poids.get())
        print("la taille est", self.var_taille.get())
        self.model.poids = self.var_poids.get()
        self.model.taille = self.var_taille.get()
        print("l'IMC est :", self.model.calcul())
        self.label_imc.config(text=str(self.model.calcul()))

    def cmd_raz(self):
        print("Je remets les champs à 0")
        self.label_imc.config(text="")
        self.var_poids.set(0)
        self.var_taille.set(0)

    def create_widgets(self):
        #
        # Les labels
        #
        label_poids = Label(self.root, text="Poids en kg")
        label_poids.pack()
        self.var_poids = DoubleVar()
        entry_poids = Entry(self.root, textvariable=self.var_poids)
        entry_poids.pack()
        label_taille = Label(self.root, text="Taille en m")
        label_taille.pack()
        self.var_taille = DoubleVar()
        entry_taille = Entry(self.root, textvariable=self.var_taille)
        entry_taille.pack()
        label_imc1 = Label(self.root, text="IMC")
        label_imc1.pack()
        self.label_imc = Label(self.root, text=" ")
        self.label_imc.pack()

        #
        # Les boutons
        #
        #
        #
        bouton_calculer = Button(self.root, text="Calculer", command=self.cmd_calcul)
        bouton_calculer.pack()
        bouton_raz = Button(self.root, text="RAZ", command=self.cmd_raz)
        bouton_raz.pack()
        button_quitter = Button(self.root, text="Quitter", command=self.root.destroy)
        button_quitter.pack()


    def __init__(self, model):
        self.root = Tk()
        self.model = model
        self.create_widgets()
        self.run()

    def run(self):
        self.root.mainloop()
