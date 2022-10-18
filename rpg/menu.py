from tkinter import *
from scenario import debut
from info import menu_info

#cree une fentre 
window_menu = Tk()

#taille/nom/logo
window_menu.title("GOLD GRABBER")
window_menu.geometry("1600x900")
window_menu.resizable(height=False,width=False)
window_menu.iconbitmap("logo.ico")

#fond de la fenetre menu
window_menu.config(background='black')

#lieu de l'image
lieu_image_menu= Frame(window_menu,bg='black')
lieu_image_menu.pack(expand=YES)

#affichage de l'image 
h_image = 450
l_image = 450
image_GOLD_GRABBER = PhotoImage(file="GOLD GRABBER.png") .zoom(17)  .subsample(35)
affichage_image_menu = Canvas(lieu_image_menu , width=l_image , height= h_image , bg= 'black', bd =0 , highlightthickness= 0)
affichage_image_menu.create_image(h_image/2 , l_image /2 , image = image_GOLD_GRABBER )
affichage_image_menu.pack(expand= YES)

#lieu des bouton menu
lieu_bouton_menu= Frame(window_menu,bg='black')
lieu_bouton_menu.pack(expand=YES)

nombre_coins = IntVar(window_menu,value= 1000 )
coins= nombre_coins.get()
objet = [0,0,0,0,0]

#bouton menu
start_bouton = Button(lieu_bouton_menu, text="start game", font=("Super Legend Boy",30), bg= 'black',fg='white',width="10",relief=GROOVE, bd=7.5,command= lambda: debut(window_menu,coins,objet))
start_bouton.pack(pady=20,anchor=N)
info_bouton = Button(lieu_bouton_menu, text="info", font=("Super Legend Boy",30), bg= 'black',fg='white',width="10",relief=GROOVE, bd=7.5,command=lambda: menu_info(window_menu))
info_bouton.pack(pady=20,anchor=CENTER)
quit_bouton = Button(lieu_bouton_menu, text="quit", font=("Super Legend Boy",30), bg= 'black',fg='white', width="10",relief=GROOVE, bd=7.5,command= quit)
quit_bouton.pack(pady=20,anchor=S)

#mettre a jour la fenetre du menu
window_menu.mainloop()
