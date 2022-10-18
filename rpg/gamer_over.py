from tkinter import *

def perdu(window):
    window.withdraw()
    # Cree la fennetre
    Windows_game_over = Toplevel(window)
    Windows_game_over.title("GOLD GRADBBER")
    Windows_game_over.geometry("1600x900")
    Windows_game_over.resizable(height=False,width=False)
    Windows_game_over.iconbitmap("logo.ico")
    Windows_game_over.config(background='black')

    #lieu de l'image
    lieu_image_menu= Frame(Windows_game_over,bg='black')
    lieu_image_menu.pack(anchor=N)
    
    #affichage de l'image
    h_image = 450
    l_image = 450
    image_GOLD_GRABBER = PhotoImage(file="GOLD GRABBER.png") .zoom(17)  .subsample(35)
    affichage_image_menu = Canvas(lieu_image_menu , width=l_image , height= h_image , bg= 'black', bd =0 , highlightthickness= 0)
    affichage_image_menu.create_image(h_image/2 , l_image /2 , image = image_GOLD_GRABBER )
    affichage_image_menu.pack(expand= YES)
    
    #affichage du texte
    lieu_texte_game_over = LabelFrame(Windows_game_over, text="Narateur" ,font=("Super Legend Boy",30), bg= 'black',fg='white',width="10",relief=GROOVE, bd=7.5,)
    lieu_texte_game_over.pack(anchor=S ,side= BOTTOM,pady=30)
    texte_GAME=Label(lieu_texte_game_over, text="GAME OVER" ,width=60, height=5, font=("Super Legend Boy",20) , bg= 'black',fg='white')
    texte_GAME.pack(anchor=CENTER)
    

    
    
    #mettre a jour la fenetre du menu
    Windows_game_over.mainloop()

    