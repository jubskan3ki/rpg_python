from tkinter import *

def victoire(window):
    window.withdraw()
    # Cree la fennetre
    Windows_Win = Toplevel(window)
    Windows_Win.title("GOLD GRADBBER")
    Windows_Win.geometry("1600x900")
    Windows_Win.resizable(height=False,width=False)
    Windows_Win.iconbitmap("logo.ico")
    Windows_Win.config(background='black')

    nombre_clic  = IntVar(Windows_Win,value= 0 )
    def add_passage (texte_scenario,id_face,affichage_image_face):
        temp= nombre_clic.get()
        if temp == 0 :
            image_face_seriously= PhotoImage(file="seriously face.png") 
            affichage_image_face.itemconfigure(id_face,image = image_face_seriously)
            affichage_image_face.image = image_face_seriously
            lieu_texte_scenario.config(text="Narateur")
            texte_scenario.config(text="je ne croyais pas du tout en toi x)")
            texte_scenario_2.config(text="mais felicitation a toi d'avoir fini se jeu !")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 1 :
            image_face_seriously= PhotoImage(file="seriously face.png") 
            affichage_image_face.itemconfigure(id_face,image = image_face_seriously)
            affichage_image_face.image = image_face_seriously
            texte_scenario.config(text="juste attend si tu clic encore sa ferme le jeu")
            texte_scenario_2.config(text="c'est tout se que j'ai dire ")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 1 :
            image_face_troll= PhotoImage(file="troll face.png") 
            affichage_image_face.itemconfigure(id_face,image = image_face_troll)
            affichage_image_face.image = image_face_troll
            texte_scenario.config(text="tu voulais quitter ?")
            texte_scenario_2.config(text="Ok c'est bon je te laisse tranquille ")
            nombre_clic.set( nombre_clic.get() + 1 )

    #lieu de l'image
    lieu_image_menu= Frame(Windows_Win,bg='black')
    lieu_image_menu.pack(anchor=N)

    #affichage de l'image
    image_face_smile= PhotoImage(file="angry+crying face.png") 
    affichage_image_face = Canvas(lieu_image_menu , width=450 , height= 450 , bg= 'black', bd =0 , highlightthickness= 0)
    id_face=affichage_image_face.create_image(250 ,250 ,image = image_face_smile )
    affichage_image_face.image = image_face_smile
    affichage_image_face.pack(expand= YES, pady=50)
    
    #affichage du texte
    lieu_texte_scenario = LabelFrame(Windows_Win, text="Directeur du casino" ,font=("Super Legend Boy",30), bg= 'black',fg='white',relief=GROOVE, bd=7.5,)
    lieu_texte_scenario.pack(side=BOTTOM, pady=30)
    texte_scenario=Label(lieu_texte_scenario, text="je vois... j'ai perdu... je te felicite... ",width=50, font=("Super Legend Boy",25) , bg= 'black',fg='white')
    texte_scenario.grid(row=0,column=0)
    texte_scenario_2=Label(lieu_texte_scenario, text="tu as galere jusqu'ici tu merite cette argent va t'en !",width=50, font=("Super Legend Boy",25) , bg= 'black',fg='white')
    texte_scenario_2.grid(row=1,column=0)
    bouton_image =PhotoImage( file="play.png").zoom(3) .subsample(35)
    bouton_scenario=Button(lieu_texte_scenario,image=bouton_image,bg='black',bd =0 ,width=85,height=85, highlightthickness= 0, command= lambda :add_passage(texte_scenario,id_face,affichage_image_face))
    bouton_scenario.grid(row=0,column=1,rowspan=2,pady=20)
    
    #mettre a jour la fenetre du menu
    Windows_Win.mainloop()