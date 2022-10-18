from tkinter.messagebox import *
from deplacement import tp
from tkinter import *


def debut (window,coins,objet) :
    window.withdraw()
    #cree une fentre 
    window_scenario = Toplevel(window)
    #taille/nom/logo
    window_scenario.title("GOLD GRABBER")
    window_scenario.geometry("1600x900")
    window_scenario.minsize(width=1600, height=900)
    window_scenario.iconbitmap("logo.ico")
    
    #fond de la fenetre menu
    window_scenario.config(background='black')

    #si tes gentille
    #le choix a faire
    def callback(coins,objet):
        if askyesno('Titre 1', 'Voulez-vous lui donner 1 jeton ?'):
            showinfo('Titre2','Vous avez donné 1 jeton au petit garçon.' )
            showinfo('Titre 3' , 'Vous avez le droit à une petite récompense pour votre gentilesse !')
            showinfo('Titre 4', 'Tiens, voilà ton gain, de la part des devs ! ')
            showwarning('Titre 5','Vous avez eu un bonus de 10 "%" de  la totalité vos jetons.' )
            coins += 99
        else:
            showinfo('Titre 5', 'Tant pis pour vous !')
        tp(window_scenario,coins,objet)
    
    #fonction pour changer le texte a l'aide d'un bouton
    nombre_clic  = IntVar(window_scenario,value= 0 ) 
    def add_passage (coins,objet,texte_scenario,id_face,affichage_image_face):
        temp= nombre_clic.get()
        if temp == 0 :
            image_face_seriously= PhotoImage(file="seriously face.png") 
            affichage_image_face.itemconfigure(id_face,image = image_face_seriously)
            affichage_image_face.image = image_face_seriously
            texte_scenario.config(text="Eh… les développeurs, vous êtes sûr du script ?")
            texte_scenario_2.config(text="Pourquoi iel est endetté au juste ?")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 1 :
            image_face_neutre= PhotoImage(file="neutre face.png") 
            affichage_image_face.itemconfigure(id_face,image = image_face_neutre)
            affichage_image_face.image = image_face_neutre
            lieu_texte_scenario.config(text="Développeurs")
            texte_scenario.config(text="T'occupes pas de ça, tu comprendras... Fais ton job.")
            texte_scenario_2.config(text="Et c’est simple, il a investi sur nous.")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 2 :
            image_face_joke= PhotoImage(file="jock face.png") 
            affichage_image_face.itemconfigure(id_face,image = image_face_joke)
            affichage_image_face.image = image_face_joke
            lieu_texte_scenario.config(text="Narrateur")
            texte_scenario.config(text="Tant que je suis payé. Ça me va !")
            texte_scenario_2.config(text="Et je comprends mieux du coup…")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 3 :
            image_face_angry= PhotoImage(file="angry face.png") 
            affichage_image_face.itemconfigure(id_face,image = image_face_angry)
            affichage_image_face.image = image_face_angry
            lieu_texte_scenario.config(text="Développeurs")
            texte_scenario.config(text="Tu n'es pas payé. ")
            texte_scenario_2.config(text="Tu es... EN STAGE.")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 4 :
            image_face_angry_crying= PhotoImage(file="angry+crying face.png") 
            affichage_image_face.itemconfigure(id_face,image = image_face_angry_crying)
            affichage_image_face.image = image_face_angry_crying
            lieu_texte_scenario.config(text="Narrateur")
            texte_scenario.config(text="En effet... je ne suis... pas... payé... ")
            texte_scenario_2.config(text="Même pas un peu ?")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 5 :
            image_face_troll= PhotoImage(file="troll face.png") 
            affichage_image_face.itemconfigure(id_face,image = image_face_troll)
            affichage_image_face.image = image_face_troll
            lieu_texte_scenario.config(text="Développeurs")
            texte_scenario.config(text="Tu peux reprendre le scénario, s'il te plait ?")
            texte_scenario_2.config(text="Même pas un centime.")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 6 :
            image_face_mask= PhotoImage(file="mask face.png") 
            affichage_image_face.itemconfigure(id_face,image = image_face_mask)
            affichage_image_face.image = image_face_mask
            lieu_texte_scenario.config(text="Narrateur")
            texte_scenario.config(text="...")
            texte_scenario_2.config(text="Bon... J'en étais où ? Ah oui ! ")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 7 :
            image_face_hero= PhotoImage(file="hero face.png") 
            affichage_image_face.itemconfigure(id_face,image = image_face_hero)
            affichage_image_face.image = image_face_hero
            texte_scenario.config(text="Notre cher joueur endetté va devoir se faire...")
            texte_scenario_2.config(text="De l’argent ! Et vite ! Cela grâce au casino ! Quoi de plus logique.")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 8 :
            image_face_hand= PhotoImage(file="hand face.png") 
            affichage_image_face.itemconfigure(id_face,image = image_face_hand)
            affichage_image_face.image = image_face_hand
            texte_scenario.config(text="Par chance, un inconnu décida d’investir en lui")
            texte_scenario_2.config(text="Quelle erreur... (ou pas !)")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 9 :
            image_face_wtf= PhotoImage(file="wtf face.png") 
            affichage_image_face.itemconfigure(id_face,image = image_face_wtf)
            affichage_image_face.image = image_face_wtf
            texte_scenario.config(text="Cet inconnu a fait un don de 1000 jetons.")
            texte_scenario_2.config(text="(1000 JETONS EN PLUS !!!!) ")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 10 :
            image_face_ok= PhotoImage(file="ok face.png") 
            affichage_image_face.itemconfigure(id_face,image = image_face_ok)
            affichage_image_face.image = image_face_ok
            texte_scenario.config(text="Dans le but de rembourser cette dette.")
            texte_scenario_2.config(text="Il devra atteindre un total de 10 000 jetons.")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 11 :
            image_face_inspiration= PhotoImage(file="inspiration face.png") 
            affichage_image_face.itemconfigure(id_face,image = image_face_inspiration)
            affichage_image_face.image = image_face_inspiration
            texte_scenario.config(text="Tiens, un petit enfant mendiant vous interpèle.")
            texte_scenario_2.config(text="Il souhaiterait 1 jeton...")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 12 :
            image_face_ok_crying= PhotoImage(file="ok+ crying face.png") 
            affichage_image_face.itemconfigure(id_face,image = image_face_ok_crying)
            affichage_image_face.image = image_face_ok_crying
            texte_scenario.config(text="Voulez-vous lui donner un jeton ?")
            texte_scenario_2.config(text="N'oubliez pas que vous êtes déjà endetté...")
            nombre_clic.set( nombre_clic.get() + 1 )
        else :
            callback(coins,objet)
    
    #lieu image
    lieu_image_scenario= Frame(window_scenario,bg='black')
    lieu_image_scenario.pack(anchor=N, expand=YES)
    
    #affichage image
    image_face_smile= PhotoImage(file="smile face.png") 
    affichage_image_face = Canvas(lieu_image_scenario , width=450 , height= 450 , bg= 'black', bd =0 , highlightthickness= 0)
    id_face=affichage_image_face.create_image(250 ,250 ,image = image_face_smile )
    affichage_image_face.image = image_face_smile
    affichage_image_face.pack(expand= YES, pady=50)
    
    #le dialogue
    lieu_texte_scenario = LabelFrame(window_scenario, text="Narrateur" ,font=("Super Legend Boy",30), bg= 'black',fg='white',relief=GROOVE, bd=7.5,)
    lieu_texte_scenario.pack(side=BOTTOM, pady=30)
    texte_scenario=Label(lieu_texte_scenario, text="Bievenue dans l'histoire de Gold Grabber !",width=50, font=("Super Legend Boy",20) , bg= 'black',fg='white')
    texte_scenario.grid(row=0,column=0)
    texte_scenario_2=Label(lieu_texte_scenario, text="Vous êtes endetté… à la suite d'une mauvaise gestion financière.",width=60, font=("Super Legend Boy",20) , bg= 'black',fg='white')
    texte_scenario_2.grid(row=1,column=0)
    bouton_image =PhotoImage( file="play.png").zoom(3) .subsample(35)
    bouton_scenario=Button(lieu_texte_scenario,image=bouton_image,bg='black',bd =0 ,width=85,height=85, highlightthickness= 0, command= lambda :add_passage(coins,objet,texte_scenario,id_face,affichage_image_face))
    bouton_scenario.grid(row=0,column=1,rowspan=2,pady=20)
    
    

    #mettre a jour la fenetre du menu
    window_scenario.mainloop()
