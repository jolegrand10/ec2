from tkinter import *
def imc(p,t):
    return p/t**2


def cmd_calcul():
    print("C'est ici que l'on calcule")
    print("le poids est", var_poids.get())
    print("la taille est", var_taille.get())
    p = var_poids.get()
    t = var_taille.get()
    print("l'IMC est :", imc(p,t))
    label_imc.config(text=str(imc(p,t)))

def cmd_raz():
    print("Je remets les champs à 0")
    label_imc.config(text="")
    var_poids.set(0)
    var_taille.set(0)

root = Tk()
#
# Les labels
#
label_poids = Label(root, text="Poids en kg")
label_poids.pack()
var_poids = DoubleVar()
entry_poids = Entry(root, textvariable=var_poids)
entry_poids.pack()
label_taille = Label(root, text="Taille en m")
label_taille.pack()
var_taille = DoubleVar()
entry_taille = Entry(root, textvariable=var_taille)
entry_taille.pack()
label_imc = Label(root, text="IMC")
label_imc.pack()
label_imc = Label(root, text=" ")
label_imc.pack()

#
# Les boutons
#
bouton_calculer = Button(root, text="Calculer", command=cmd_calcul)
bouton_calculer.pack()
bouton_raz = Button(root,text="RAZ", command=cmd_raz)
bouton_raz.pack()
button_quitter = Button(root,text="Quitter", command=root.destroy)
button_quitter.pack()
root.mainloop()