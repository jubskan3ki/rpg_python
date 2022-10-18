from tkinter import *

def rule(window) :
    # je crée ma premier fenetre
    window.withdraw()
    window = Toplevel(window)

    # personnaliser ma fennetre
    window.title("Regles des jeux")
    window.geometry("1080x520")
    window.minsize(480, 360)
    window.config(background='#073E49')

    # mon tittre
    label_title = Label(window, text="Regles des jeux", font=(
        "Courrier", 40), bg="#073E49", fg="white")


    # MORPION
    morpion = Label(window, text="MORPION", font=(
        "courrier", 16), bg="#073E49", fg="white")
    saut_ligne = Label(window, bg="#073E49")
    # texte des regle pour le morpion (création des Label)
    regle_morpion = Label(window,  text="Le but du jeu est d’aligner avant son adversaire 3 couleurs identiques horizontalement, verticalement ou en diagonale.", font=(
        "courrier", 11), bg="#073E49", fg="white")
    regle_morpion1 = Label(window, text="Chaque joueur a donc sa propre couleur, rouge pour l’un et bleu pour l’autre.", font=(
        "courrier", 11), bg="#073E49", fg="white")
    regle_morpion2 = Label(window, text="La partie se termine quand l’un des joueurs à aligné 3 couleurs ou quand la grille est complétée sans vainqueur, il y a alors égalité.", font=(
        "courrier", 11), bg="#073E49", fg="white")

    # MACHINE A SOUS
    machine_a_sous = Label(window, text="MACHINE A SOUS", font=(
        "Courrier", 16), bg="#073E49", fg="white")
    mach = Label(window, text="Misez votre argent et activez ensuite la machine pour attendre les combinaisons qui vont se faire automatiquement.", font=(
        "courrier", 11), bg="#073E49", fg="white")
    mach_1 = Label(window, text="Le but du jeu : la machine vous construit des combinaisons afin que vous puissiez gagner des gains et ainsi toucher de l’argent à chaque tour... ou pas.", font=(
        "courrier", 11), bg="#073E49", fg="white")
    mach_2 = Label(window, text="")

    # Roulette
    roulette = Label(window, text="ROULETTE", font=(
        "Courrier", 16), bg="#073E49", fg="white")
    r = Label(window, text="Deviner la case sur laquelle la bille lancée va s’arrêter. Le joueur peut décider de placer ses jetons et décider de miser sur les différentes cases allant de 0 à 36.",
            font=("courrier", 11), bg="#073E49", fg="white")
    r_1 = Label(window, text="Choisissez une mise. Jouez sur les numéros de 1 à 18 (Manque) ou 19 à 36 (Passe), pairs ou impairs,  rouges ou noirs.",
                font=("courrier", 11), bg="#073E49", fg="white")

    label_title.pack()
    saut_ligne.pack()
    # affichage du morpion
    morpion.pack()
    regle_morpion.pack()
    regle_morpion1.pack()
    regle_morpion2.pack()

    # affichage machine à sous
    machine_a_sous.pack(pady=10, fill=X)
    mach.pack()
    mach_1.pack()

    # affichage roulette
    roulette.pack(pady=10, fill=X)
    r.pack()
    r_1.pack()


    # afficher ma fenetre
    window.mainloop()
