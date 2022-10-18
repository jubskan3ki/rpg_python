from tkinter import *
from regle_des_jeux import rule 
def menu_info(window):
    window.withdraw()
    #cree une fentre 
    window_info = Toplevel(window)
    #taille/nom/logo
    window_info.title("GOLD GRABBER")
    window_info.geometry("1600x900")
    window_info.resizable(height=False,width=False)
    window_info.iconbitmap("logo.ico")
    #fond de la fenetre menu
    window_info.config(background='black')
    #lieu de l'image
    lieu_image_menu_info= Frame(window_info,bg='black')
    lieu_image_menu_info.pack(expand=YES)
    #affichage de l'image
    h_image = 450
    l_image = 450
    image_GOLD_GRABBER_menu_info = PhotoImage(file="GOLD GRABBER.png") .zoom(17)  .subsample(35)
    affichage_image_menu_info = Canvas(lieu_image_menu_info , width=l_image , height= h_image , bg= 'black', bd =0 , highlightthickness= 0)
    affichage_image_menu_info.create_image(h_image/2 , l_image /2 , image = image_GOLD_GRABBER_menu_info )
    affichage_image_menu_info.pack(expand= YES)
    #lieu des bouton menu
    lieu_bouton_menu_info= Frame(window_info,bg='black')
    lieu_bouton_menu_info.pack(expand=YES)
    
    #fonction revenir en arrire
    def back (window1,window2):
        window1.withdraw()
        window2.deiconify()
    #bouton menu
    regle_bouton = Button(lieu_bouton_menu_info, text="regle", font=("Super Legend Boy",30), bg= 'black',fg='white',width="10",relief=GROOVE, bd=7.5,command=rule(window_info))
    regle_bouton.pack(pady=20,anchor=N)
    credit_bouton = Button(lieu_bouton_menu_info, text="credit", font=("Super Legend Boy",30), bg= 'black',fg='white',width="10",relief=GROOVE, bd=7.5)
    credit_bouton.pack(pady=20,anchor=CENTER)
    quit_bouton = Button(lieu_bouton_menu_info, text="quit", font=("Super Legend Boy",30), bg= 'black',fg='white', width="10",relief=GROOVE, bd=7.5,command=lambda:back(window_info,window))
    quit_bouton.pack(pady=20,anchor=S)
    #mettre a jour la fenetre du menu
    window_info.mainloop()
