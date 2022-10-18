from random import randint
from tkinter import *
from tkinter import Label, messagebox
from gamer_over import perdu
from win import victoire

def One_Piece_Game(window):
    window.withdraw()
    Windows_OnePiece = Toplevel(window)
    #taille/nom/logo
    Windows_OnePiece.title("GOLD GRABBER")
    Windows_OnePiece.geometry("1600x900")
    Windows_OnePiece.resizable(height=False,width=False)
    Windows_OnePiece.iconbitmap("logo.ico")

    #fond de la fenetre menu
    Windows_OnePiece.config(background='black')

    nombre_clic  = IntVar(Windows_OnePiece,value= 0 ) 
    def Pile_or_Face ():
        Your_Choice = messagebox.askquestion(title= "Pile ou Face", message= "Voulez vous jouer Face ?")
        Your_Choice_Result = 0
        if Your_Choice == "Yes":
            Your_Choice_Result = "Face"
        else :
            Your_Choice_Result = "Pile"
        
        luck = randint(0,1)
        Result = 0
        if luck == 0:
            Result = "Pile"
        else:
            Result = "Face"
        
        if Your_Choice_Result == Result:
            victoire(Windows_OnePiece)
        else : 
            perdu(Windows_OnePiece)
    nombre_clic  = IntVar(Windows_OnePiece,value= 0 )
    def add_passage (texte_scenario,id_face,affichage_image_face):
        temp= nombre_clic.get()
        if temp == 0 :
            image_face_seriously= PhotoImage(file="boss final 4.png") 
            affichage_image_face.itemconfigure(id_face,image = image_face_seriously)
            affichage_image_face.image = image_face_seriously
            texte_scenario.config(text="donc je te propose un deal que tu ne pourra pas refuse")
            texte_scenario_2.config(text="un simple pile ou face sache que tu ne peux refuse")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 1 :
            image_face_seriously= PhotoImage(file="boss final 2.png") 
            affichage_image_face.itemconfigure(id_face,image = image_face_seriously)
            affichage_image_face.image = image_face_seriously
            texte_scenario.config(text="soit tu repart avec rien et tu ma voulais 10000 pour rien")
            texte_scenario_2.config(text="car je lest reprendrai soit tu gagne le double  ")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 2 :
            image_face_seriously= PhotoImage(file="boss final 1.png") 
            affichage_image_face.itemconfigure(id_face,image = image_face_seriously)
            affichage_image_face.image = image_face_seriously
            texte_scenario.config(text="sa vaut le coup et ta pas le choix dans tt les cas")
            texte_scenario_2.config(text=" surtout ue tes endete donc cette argent n'est meme pas a toi ")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 3 :
            image_face_seriously= PhotoImage(file="boss final 3.png") 
            affichage_image_face.itemconfigure(id_face,image = image_face_seriously)
            affichage_image_face.image = image_face_seriously
            texte_scenario.config(text="donc il me reste un truc a demande ...")
            texte_scenario_2.config(text="tu veux jouer face ?")
            nombre_clic.set( nombre_clic.get() + 1 )
        else :
            Pile_or_Face()

    

    #lieu image
    lieu_image_scenario= Frame(Windows_OnePiece,bg='black')
    lieu_image_scenario.pack(anchor=N, expand=YES)
    
    #affichage image
    image_face_smile= PhotoImage(file="boss final 5.png") 
    affichage_image_face = Canvas(lieu_image_scenario , width=450 , height= 450 , bg= 'black', bd =0 , highlightthickness= 0)
    id_face=affichage_image_face.create_image(250 ,250 ,image = image_face_smile )
    affichage_image_face.image = image_face_smile
    affichage_image_face.pack(expand= YES, pady=50)
    
    #le dialogue
    lieu_texte_scenario = LabelFrame(Windows_OnePiece, text="Directeur du casino" ,font=("Super Legend Boy",30), bg= 'black',fg='white',relief=GROOVE, bd=7.5,)
    lieu_texte_scenario.pack(side=BOTTOM, pady=30)
    texte_scenario=Label(lieu_texte_scenario, text="bien le bonjour mon enfant c'est pas que je taime pas",width=50, font=("Super Legend Boy",25) , bg= 'black',fg='white')
    texte_scenario.grid(row=0,column=0)
    texte_scenario_2=Label(lieu_texte_scenario, text="mais tu ma voulais beaucoup d'argent aujoudhui ",width=50, font=("Super Legend Boy",25) , bg= 'black',fg='white')
    texte_scenario_2.grid(row=1,column=0)
    bouton_image =PhotoImage( file="play.png").zoom(3) .subsample(35)
    bouton_scenario=Button(lieu_texte_scenario,image=bouton_image,bg='black',bd =0 ,width=85,height=85, highlightthickness= 0, command= lambda :add_passage(texte_scenario,id_face,affichage_image_face))
    bouton_scenario.grid(row=0,column=1,rowspan=2,pady=20)
    Windows_OnePiece.mainloop()