from tkinter import *
from game import *
from random import randint
from shop import boutique
from PIL import ImageTk, Image
from OnePiece import One_Piece_Game
from gamer_over import perdu

Inventaire = [1, 1, 1]
Objet = "Aucun"

def tp(window,coins) :
    window.withdraw()
    #cree une fentre 
    window_deplacement = Toplevel(window)
    #taille/nom/logo
    window_deplacement.title("GOLD GRABBER")
    window_deplacement.geometry("1600x900")
    window_deplacement.minsize(width=1600, height=900)
    window_deplacement.iconbitmap("logo.ico")
    if coins >=10000 :
        One_Piece_Game(window_deplacement)
    elif coins <100 :
            perdu(window_deplacement)
    else :
        
        #fond de la fenetre menu
        window_deplacement.config(background='black')

        Jetons = str(coins)
        #bouton deplacement
        morpion_bouton = Button(window_deplacement, text="Morpion",pady=122, padx=95 ,font=("Super Legend Boy",30), bg= 'black',fg='white',width=8,relief=GROOVE, bd=7.5,command=lambda: lancement(window_deplacement))
        morpion_bouton.grid(row=0,column=0,padx=22,pady=75)
        machine_a_soue_bouton =Button(window_deplacement, text="Machine à sous",pady=122, padx=95 ,font=("Super Legend Boy",30), bg= 'black',fg='white',width=8,relief=GROOVE, bd=7.5,command=lambda:machine_a_sous(window_deplacement,coins, Inventaire, Objet))
        machine_a_soue_bouton.grid(row=0,column=1,padx=22,pady=75)
        roulette_bouton =Button(window_deplacement, text="Roulette",pady=122, padx=95 ,font=("Super Legend Boy",30), bg= 'black',fg='white',width=8,relief=GROOVE, bd=7.5,command=lambda:roulette(window_deplacement,coins, Inventaire, Objet))
        roulette_bouton.grid(row=0,column=2,padx=22,pady=75)
        shop_bouton =Button(window_deplacement, text="Boutique",pady=122, padx=95 , font=("Super Legend Boy",30), bg= 'black',fg='white', width=8,relief=GROOVE, bd=7.5,command=lambda:boutique(window_deplacement))
        shop_bouton.grid(row=1,column=0,padx=22)
        money =Button(window_deplacement, text=(Jetons, "Jetons"),pady=122, padx=95 , font=("Super Legend Boy",30), bg= 'black',fg='white', width=8,relief=GROOVE, bd=7.5)
        money.grid(row=1,column=1,padx=22)
        quit_bouton =Button(window_deplacement, text="Quitter",pady=122, padx=95 , font=("Super Legend Boy",30), bg= 'black',fg='white', width=8,relief=GROOVE, bd=7.5,command=quit)
        quit_bouton.grid(row=1,column=2,padx=22)
        
        #mettre a jour la fenetre du menu
        window_deplacement.mainloop()


#Changer l'état du bouton
def changeState(btn):
    if (btn['state'] == NORMAL):
        btn['state'] = DISABLED
    else:
        btn['state'] = NORMAL

#inventaire de la machine à sous
def bag_machine(window, Jetons, Inventaire, Objet) :
    window.withdraw()
    Window_shop = Toplevel(window)
    #taille/nom/logo
    Window_shop.title("GOLD GRABBER")
    Window_shop.geometry("800x600")
    Window_shop.resizable(height=False,width=False)
    Window_shop.iconbitmap("logo.ico")
    #fond de la fenetre menu
    Window_shop.config(background='black')
    #valeur pour le nombre d'occurence pour chaque objet
    nombre_clic_3 = IntVar(Window_shop,value = Inventaire[2])
    nombre_clic_2 = IntVar(Window_shop,value = Inventaire[1]) 
    nombre_clic_1 = IntVar(Window_shop,value = Inventaire[0])  
    
    lettre_3=str(nombre_clic_3.get())
    lettre_2=str(nombre_clic_2.get())
    lettre_1=str(nombre_clic_1.get())

    #Bouton et affichage pour l'objet 1, on lance la fonction en fonction de l'objet choisi
    Panel_item_1 = Label(Window_shop,text="Quitte ou Triple", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_1.grid(row=0,column=0,pady=5)
    number_item_1=Label(Window_shop,text=lettre_1, font=("Super Legend Boy",20), bg='black',fg='white',height=3,width=5 )
    number_item_1.grid(row=0,column=1,pady=5)
    Button_item_1=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg='black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command= lambda : [machine_a_sous(Window_shop, Jetons, Inventaire, "Quitte ou triple")])
    Button_item_1.grid(row=0,column=2,pady=5)
    if Inventaire[0]==0:
        changeState(Button_item_1)
    #Idem
    Panel_item_2 = Label(Window_shop,text="Bouclier", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_2.grid(row=1,column=0,pady=5)
    number_item_2=Label(Window_shop,text=lettre_2, font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
    number_item_2.grid(row=1,column=1,pady=5)
    Button_item_2=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:machine_a_sous(Window_shop, Jetons, Inventaire, "Bouclier"))
    Button_item_2.grid(row=1,column=2,pady=5)
    if Inventaire[1]==0:
        changeState(Button_item_2)
    #Idem
    Panel_item_3 = Label(Window_shop,text="Corde de sortie", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_3.grid(row=2,column=0,pady=5)
    number_item_3=Label(Window_shop,text=lettre_3, font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
    number_item_3.grid(row=2,column=1,pady=5)
    Button_item_3=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:machine_a_sous(Window_shop, Jetons, Inventaire, "Corde de sortie"))
    Button_item_3.grid(row=2,column=2,pady=5)
    if Inventaire[2]==0:
        changeState(Button_item_3)
    #Bouton quitter au cas où on n'a pas d'objet
    Button_Quitte = Button(Window_shop,text="Exit",font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=25,relief=GROOVE, bd=7.5, command= lambda : machine_a_sous(Window_shop, Jetons, Inventaire, Objet))
    Button_Quitte.grid(row=3,column=0,columnspan=4,pady=5) 
    Window_shop.mainloop()

#donner une valeur à une variable
def action(Variable, valeur):
    Variable.set(valeur)    

# jeu de la machine a sous
def machine_a_sous(window,Jetons, Inventaire, Objet):
    #Ouvrir / fermer des fenêtres
    window.withdraw()

    #Définir le résultat
    def resultats():
        #3 cases de la machine
        case_1 = randint(1,18)
        case_2 = randint(1,18)
        case_3 = randint(1,18)
        result = [case_1, case_2, case_3]
        j = 0
        #On fait correspondre les nombres avec les chiffres de la machine
        for i in result:
            if i < 9:
                result[j] = 3
            elif i < 13:
                result[j] = 4
            elif i < 15:
                result[j] = 5
            elif i < 18:
                result[j] = 6
            else :
                result[j] = 7
            j = j + 1
        
        return result
    
    #fenêtre d'affichage du résultat
    def window_resultat(fenetre, Result, Jetons, Mise, Inventaire, Objet):
        fenetre.withdraw()
        #creation 3e fenetre -> affichage de la machine a sous
        window_resultat = Toplevel(fenetre)
        window_resultat.title("MACHINE À SOUS")
        window_resultat.geometry("1350x680")
        window_resultat.resizable(height=False , width= False)
        window_resultat.config(background='black')


        Label(window_resultat, text = "Voici le résultat",font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white').pack()

        #Canevas d'affichage du résultat
        width = 1050
        height = 300
        canvas1 = Canvas( window_resultat, width = width, height = height, bg="darkgreen")
        
        canvas1.pack(fill = "both", expand = True)
        
        

        #on ouvre l'image
        img = Image.open("machine_a_sous.png")

        #on la redimensionne
        redimension = img.resize((295, 437), Image.ANTIALIAS)

        img_fin = ImageTk.PhotoImage(redimension)

        # Affichage image
        canvas1.create_image( width/2, 10, image = img_fin, anchor = "nw")

        #Attribution des resultats à une case
        case_1 = Result[0]
        case_2 = Result[1]
        case_3 = Result[2] 

        #Espaces pour le texte
        canvas1.create_text(613, 190, text=case_1 , font= ("Super legend boy" , 30))
        canvas1.create_text(680, 190, text=case_2 , font= ("Super legend boy" , 30))
        canvas1.create_text(745, 190, text=case_3 , font= ("Super legend boy" , 30))

        #On regarde si le joueur gagne ou non
        if  case_1 == case_2 and case_2 == case_3 :
            #Augmentation de la Récompense en fonction du résultat
            if case_1 == 3 :
                Mise = Mise * 3
            elif  case_1 == 4 :
                Mise = Mise * 4
            elif case_1 == 5:
                Mise = Mise * 10
            elif case_1 == 6:
                Mise = Mise * 80
            else :
                Mise = Mise * 1000
            
            #Si l'objet Quitte ou triple est utilisé la mise gagnante triple
            if Objet == "Quitte ou triple":
                Mise = Mise*3
                #L'objet disparaît de l'inventaire
                Inventaire[0] = Inventaire[0]-1

            #La mise gagnante s'ajoute à la mise
            Jetons = Jetons + Mise
        
            Label(window_resultat, text = ('Vous avez gagné', Mise,'jetons.''Vous en avez maintenant',Jetons,'.'), font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white').pack(expand=YES)
            
            #on retourne dans la fonction déplacement avec les jetons 
            quit = Button(window_resultat, text= "QUITTER !", font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' , command =lambda:tp(window_resultat,Jetons))
            quit.pack()
            window_resultat.mainloop()
        else :
            #Si l'objet Quitte ou triple est utilisé la mise perdante double
            if Objet == "Quitte ou triple":
                Mise = Mise * 2
                Inventaire[0] = Inventaire[0]-1
            #Bouclier protège de la défaite, la mise est à 0
            elif Objet == "Bouclier":
                Mise = 0
                Inventaire[1] = Inventaire[1]-1
            
            #La mise se soustrait aux jetons et on les retourne dans la fonction déplacement
            Jetons = Jetons - Mise 
            Label(window_resultat, text = ('Vous avez perdu',Mise,"jetons. Il vous en reste", Jetons,"."), font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white').pack()
            quit = Button(window_resultat, text= "QUITTER !", font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' , command =lambda:tp(window_resultat,Jetons)).pack()
            window_resultat.mainloop()
    
    #Fenêtre d'affichage de la mise
    def mise(window_2,Jetons, Inventaire, Objet):
    # creation 2e fenetre -> entrer la mise
        window_2.withdraw()
        Fenetre2 = Toplevel(start_machine)
        Fenetre2.title("MACHINE À SOUS")
        Fenetre2.geometry("1350x680")
        Fenetre2.config(background='black')
        Fenetre2.resizable(height=False , width= False)
        
        Label(Fenetre2, text="Choisissez votre mise." , font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white').pack()
        Label(Fenetre2, text=('Vous avez' ,Jetons, "jetons.") , font= ("Super legend boy" , 20)).pack()
        objet = Label(Fenetre2, text=("Objet actif :", Objet) , font= ("Super legend boy" , 15) , bg = 'black' , fg = 'white')
        objet.pack()

        #Le résultat
        Result = resultats()

        #La valeur de la mise avant qu'on la choisisse grâce aux boutons
        IntMise = IntVar()
    
        #Les boutons de mise
        btn_100 = Radiobutton(Fenetre2 , text = 100 ,font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' ,variable= IntMise, value = 100,command = lambda : [window_resultat(Fenetre2, Result, Jetons, 100, Inventaire, Objet), action(IntMise, 100)], indicatoron=0)
        btn_100.pack(expand=YES)
        
        btn_250 = Radiobutton(Fenetre2 , text = 250,font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white',variable= IntMise, value = 250, command = lambda : [window_resultat(Fenetre2, Result, Jetons, 250, Inventaire, Objet), action(IntMise, 250)], indicatoron=0)
        btn_250.pack(expand=YES)
        
        btn_500 = Radiobutton(Fenetre2 , text = 500,font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' ,variable= IntMise, value = 500,command = lambda : [window_resultat(Fenetre2, Result, Jetons, 500, Inventaire, Objet), action(IntMise, 500)], indicatoron=0)
        btn_500.pack(expand=YES)
        
        btn_1000 = Radiobutton(Fenetre2 , text = 1000,font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' ,variable= IntMise, value = 1000,command = lambda : [window_resultat(Fenetre2, Result, Jetons, 1000, Inventaire, Objet), action(IntMise, 1000)], indicatoron=0)
        btn_1000.pack(expand=YES)
        
        btn_all = Radiobutton(Fenetre2 , text = "All in",font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' ,variable= IntMise, value = Jetons, command = lambda : [window_resultat(Fenetre2, Result, Jetons, Jetons, Inventaire, Objet), action(IntMise, Jetons)], indicatoron=0)
        btn_all.pack(expand=YES)

        #changer l'état des boutons
        if Jetons < 100:
            changeState(btn_1000)
            changeState(btn_500)
            changeState(btn_250)
            changeState(btn_100)

        elif Jetons < 250:
            changeState(btn_1000)
            changeState(btn_500)
            changeState(btn_250)

        elif Jetons < 500:
            changeState(btn_1000)
            changeState(btn_500)
        
        elif Jetons < 1000:
            changeState(btn_1000)
        
        Fenetre2.mainloop()
   
        
    # creation de la 1e fenetre
    start_machine = Toplevel(window)
    # configuration des parametres de la fenetre
    start_machine.title("MACHINE À SOUS")
    start_machine.geometry("1350x680")
    start_machine.minsize(480 , 360)
    start_machine.config(background='black')
    start_machine.resizable(height=False , width= False)
    #titre du jeu
    title = Label(start_machine, text = "LA MACHINE À $OU$ " , font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white')
    start = Button(start_machine, text= "COMMENCER !", font= ("Super legend boy" , 60) , bg = 'black' , fg = 'white' , command =lambda:mise(start_machine,Jetons, Inventaire, Objet) )
    title.pack(side=TOP)
    start.pack(expand=YES)
    #On affiche l'objet actif 
    objet = Label(start_machine, text=("Objet actif :", Objet) , font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white')
    objet.pack(expand=YES)
    btn_Start = Button(start_machine, text="Inventaire", font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' , command = lambda:  bag_machine(start_machine, Jetons, Inventaire, Objet))
    btn_Start.pack(expand=YES)

    #On regarde si l'utilisateur veut sortir
    if Objet == "Corde de sortie":
        tp(start_machine, Jetons)
        Inventaire[2] = Inventaire[2]-1
    
    start_machine.mainloop()
    

#Inventaire de la roulette, même fonctionnement que celui de la machine à sous
def bag_roulette(window, Jetons, Inventaire, Objet) :
    window.withdraw()
    Window_shop = Toplevel(window)
    #taille/nom/logo
    Window_shop.title("GOLD GRABBER")
    Window_shop.geometry("800x600")
    Window_shop.resizable(height=False,width=False)
    Window_shop.iconbitmap("logo.ico")
    #fond de la fenetre menu
    Window_shop.config(background='black')
    #fonction revenir en arrire
    nombre_clic_3 = IntVar(Window_shop,value = Inventaire[2])
    nombre_clic_2 = IntVar(Window_shop,value = Inventaire[1]) 
    nombre_clic_1 = IntVar(Window_shop,value = Inventaire[0])  
    lettre_3=str(nombre_clic_3.get())
    lettre_2=str(nombre_clic_2.get())
    lettre_1=str(nombre_clic_1.get())
    #Bouton et affichage pour l'objet 1, on lance la fonction en fonction de l'objet choisi
    Panel_item_1 = Label(Window_shop,text="Quitte ou Triple", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_1.grid(row=0,column=0,pady=5)
    number_item_1=Label(Window_shop,text=lettre_1, font=("Super Legend Boy",20), bg='black',fg='white',height=3,width=5 )
    number_item_1.grid(row=0,column=1,pady=5)
    Button_item_1=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg='black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command= lambda : [roulette(Window_shop, Jetons, Inventaire, "Quitte ou triple")])
    Button_item_1.grid(row=0,column=2,pady=5)
    if Inventaire[0]==0:
        changeState(Button_item_1)
    #Idem
    Panel_item_2 = Label(Window_shop,text="Bouclier", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_2.grid(row=1,column=0,pady=5)
    number_item_2=Label(Window_shop,text=lettre_2, font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
    number_item_2.grid(row=1,column=1,pady=5)
    Button_item_2=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:roulette(Window_shop, Jetons, Inventaire, "Bouclier"))
    Button_item_2.grid(row=1,column=2,pady=5)
    if Inventaire[1]==0:
        changeState(Button_item_2)
    #Idem
    Panel_item_3 = Label(Window_shop,text="Corde de sortie", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_3.grid(row=2,column=0,pady=5)
    number_item_3=Label(Window_shop,text=lettre_3, font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
    number_item_3.grid(row=2,column=1,pady=5)
    Button_item_3=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:roulette(Window_shop, Jetons, Inventaire, "Corde de sortie"))
    Button_item_3.grid(row=2,column=2,pady=5)
    if Inventaire[2]==0:
        changeState(Button_item_3)
    #Bouton quitter au cas où on n'a pas d'objet
    Button_Quitte = Button(Window_shop,text="Exit",font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=25,relief=GROOVE, bd=7.5, command= lambda : roulette(Window_shop, Jetons, Inventaire, Objet))
    Button_Quitte.grid(row=3,column=0,columnspan=4,pady=5) 
    Window_shop.mainloop()

# jeu de la roulette

def roulette(window_tp, coins, Inventaire, Objet):

    def resultat_window(window, Choix, Mise, coins, Inventaire, Objet):
        window.withdraw()
        Jeu = Toplevel(window)
        
        Result = randint(1, 36)
        print("resultat window :", Choix, Mise, Result)

        rouges = [1, 3, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 28, 30, 32, 34, 36]
        noirs = [2, 4, 5, 6, 8, 10, 11, 13, 15, 17, 19, 20, 22, 24, 26, 29, 31, 33, 35]

        if Choix == "Manque" or Choix == "Passe":
            manques = []
            for i in range (1,19):
                manques.append(i)
            if Result in manques :
                Gagnant = "Manque"

            passes = []
            for i in range (19, 37):
                passes.append(i)
            if Result in passes :
                Gagnant = "Passe"

        elif Choix == "Pair" or Choix == "Impair":    
            pairs = []
            for i in range (2,38,2):
                pairs.append(i)

            if Result in pairs :
                Gagnant = "Pair"

            impaires = []
            for i in range (1,37,2):
                impaires.append(i)
            if Result in impaires :
                Gagnant = "Impair"

        elif Choix == "Rouge" or Choix == "Noir":
            if Result in rouges :
                Gagnant = "Rouge"
            elif Result in noirs :
                Gagnant = "Noir"

        print("gagnant: ", Gagnant)
        #creation 3e fenetre -> affichage de la roulette
        Jeu.title("LA ROULETTE")
        Jeu.geometry("1350x680")
        Jeu.resizable(height=False , width= False)
        Jeu.config(background='black')

        Label(Jeu, text = "Voici le résultat",font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white').pack()

        width = 1000
        height = 500

        canvas1 = Canvas( Jeu, width = width, height = height, bg="darkgreen")
        
        canvas1.pack(expand = YES)
        
        #on ouvre l'image
        img = Image.open("logo.png")

        #on la redimensionne
        redimension = img.resize((200, 200), Image.ANTIALIAS)

        img_fin = ImageTk.PhotoImage(redimension)

        # Affichage image
        canvas1.create_image(width/2, 10, image = img_fin, anchor="n")
        if Result in rouges :
            canvas1.create_text(width/2, 270, text=Result, font= ("Super legend boy" , 30), fill="red")  
        elif Result in noirs :
            canvas1.create_text(width/2, 270, text=Result, font= ("Super legend boy" , 30),fill="black")

        
        
        
        #canvas2 = Canvas(Jeu, 1050, 500, bg="black").pack(expand=YES)
        if Choix == Gagnant :
            canvas1.create_text(width/2, 350, text=("Vous avez choisi", Choix), font= ("Super legend boy" , 30), fill="gold")
            if Objet == "Quitte ou triple":
                Mise = Mise*3
                Inventaire[0] = Inventaire[0]-1
            coins = coins + Mise
            Label(Jeu, text="Vous avez gagné !",font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white').pack(expand=YES)
            Label(Jeu, text=("Vous disposez de",coins, "coins"),font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white').pack(expand=YES)
            quit = Button(Jeu, text= "QUITTER !", font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' , command = lambda:tp(Jeu,coins))
            quit.pack()
            Jeu.mainloop()
        else :
            canvas1.create_text(width/2, 350, text=("Vous avez choisi", Choix), font= ("Super legend boy" , 30), fill="silver")            
            if Objet == "Quitte ou triple":
                Mise = Mise * 2
                Inventaire[0] = Inventaire[0]-1
            elif Objet == "Bouclier":
                Mise = 0
                Inventaire[1] = Inventaire[1]-1
            coins = coins-Mise
            Label(Jeu, text = "Vous avez perdu.",font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white').pack(expand=YES)
            Label(Jeu, text=("Vous disposez de",coins, "coins"),font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white').pack(expand=YES)
            quit = Button(Jeu, text= "QUITTER !", font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' , command = lambda:tp(Jeu,coins))
            quit.pack()
            Jeu.mainloop()
    
    def roulette_jeu(window, coins,Choix, Mise, Inventaire, Objet):
        window.withdraw()
        window_roulette = Toplevel(window)
        # creation de la 1e fenetre
        # configuration des parametres de la fenetre
        window_roulette.title("ROULETTE")
        window_roulette.geometry("1350x680")
        window_roulette.config(background='black')
        # pas de possibilité de + / - la fenetre
        window_roulette.resizable(height=False , width= False)
        

        title = Label(window_roulette, text = "LA ROULETTE " , font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white')
        title.grid(sticky="n", columnspan=1)
        
        Annonce = Label(window_roulette, text="Faites vos jeux." , font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white')
        Annonce.grid(sticky="n")
        Annonce_2 = Label(window_roulette, text=" Jouez sur les numéros de 1 à 18 (Manque) ou 19 à 36 (Passe), pairs ou impairs, rouges ou noirs.", font= ("Super legend boy" , 14))
        Annonce_2.grid(padx = 30)

        StrChoix = StringVar(window)
        IntMise = IntVar(window)
        objet = Label(window_roulette, text=("Objet actif :", Objet) , font= ("Super legend boy" , 15) , bg = 'black' , fg = 'white')
        objet.grid(pady=20, row=5)
        choix = Label(window_roulette, text=("Choix de jeu :", Choix) , font= ("Super legend boy" , 15) , bg = 'black' , fg = 'white')
        choix.grid(pady=20, row=3)
        jetons = Label(window_roulette, text=("Jetons :", coins) , font= ("Super legend boy" , 15) , bg = 'black' , fg = 'white')
        jetons.grid(pady=20, row=4)
        mise = Label(window_roulette, text=("Mise :", Mise) , font= ("Super legend boy" , 15) , bg = 'black' , fg = 'white')
        mise.grid(pady=20, row=8)

        #Les boutons de jeux relance la fonction avec la nouvelle valeur
        btn_Manque = Radiobutton(window_roulette , text = "Manque" ,font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' ,variable= StrChoix, value = "Manque",command = lambda : [action(StrChoix, "Manque"),roulette_jeu(window_roulette, coins, "Manque", Mise, Inventaire, Objet)], indicatoron=0)
        btn_Manque.grid(padx=10, pady=20, sticky="w", row = 3)
        btn_Passe = Radiobutton(window_roulette , text = "Passe" ,font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' ,variable= StrChoix, value = "Passe",command = lambda : [action(StrChoix, "Passe"),roulette_jeu(window_roulette, coins, "Passe", Mise, Inventaire, Objet)], indicatoron=0)
        btn_Passe.grid(sticky="e", pady=20, row=3, padx=10)
        btn_Pair = Radiobutton(window_roulette , text = "Pair" ,font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' ,variable= StrChoix, value = "Pair",command = lambda : [action(StrChoix, "Pair"),roulette_jeu(window_roulette, coins, "Pair", Mise, Inventaire, Objet)], indicatoron=0)
        btn_Pair.grid(sticky="w", row=4, padx=10, pady=20)
        btn_Impair = Radiobutton(window_roulette , text = "Impair" ,font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' ,variable= StrChoix, value = "Impair",command = lambda : [action(StrChoix, "Impair"),roulette_jeu(window_roulette, coins, "Impair", Mise, Inventaire, Objet)], indicatoron=0)
        btn_Impair.grid(sticky="e", row=4, padx=10)
        btn_Rouge = Radiobutton(window_roulette , text = "Rouge" ,font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' ,variable= StrChoix, value = "Rouge",command = lambda : [action(StrChoix, "Rouge"),roulette_jeu(window_roulette, coins, "Rouge", Mise, Inventaire, Objet)], indicatoron=0)
        btn_Rouge.grid(sticky="w", row=5, padx=10, pady=20)
        btn_Noir = Radiobutton(window_roulette , text = "Noir" ,font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' ,variable= StrChoix, value = "Noir",command = lambda : [action(StrChoix, "Noir"),roulette_jeu(window_roulette, coins, "Noir", Mise, Inventaire, Objet)], indicatoron=0)
        btn_Noir.grid(sticky="e", row=5, padx=10, pady=20)

        #Les boutons de mise relance la fonction avec la nouvelle valeur
        btn_100 = Radiobutton(window_roulette , text = 100 ,font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' ,variable= IntMise, value = 100,command = lambda : [action(IntMise, 100),roulette_jeu(window_roulette, coins, Choix, 100, Inventaire, Objet)], indicatoron=0)
        btn_100.grid(sticky="w", row=8, padx=10)
        
        btn_250 = Radiobutton(window_roulette , text = 250,font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white',variable= IntMise, value = 250, command = lambda : [action(IntMise, 250),roulette_jeu(window_roulette, coins, Choix, 250, Inventaire, Objet)], indicatoron=0)
        btn_250.grid(sticky="e", row=8, padx=10)
        
        
        btn_500 = Radiobutton(window_roulette , text = 500,font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' ,variable= IntMise, value = 500,command = lambda : [action(IntMise, 500),roulette_jeu(window_roulette, coins, Choix, 500, Inventaire, Objet)], indicatoron=0)
        btn_500.grid(sticky="w", row=9, padx=10, pady=20)
        
        btn_1000 = Radiobutton(window_roulette , text = 1000,font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' ,variable= IntMise, value = 1000,command = lambda : [action(IntMise, 1000),roulette_jeu(window_roulette, coins, Choix, 1000, Inventaire, Objet)], indicatoron=0)
        btn_1000.grid(sticky="e", row=9, padx=10, pady=20)
        
        btn_all = Radiobutton(window_roulette , text = "All in",font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' ,variable= IntMise, value = coins, command = lambda : [action(IntMise, coins),roulette_jeu(window_roulette, coins, Choix, coins, Inventaire, Objet)], indicatoron=0)
        btn_all.grid(sticky="s", row=9)
        
        btn_Start = Button(window_roulette, text="Start", font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' , command =lambda:resultat_window(window_roulette, Choix, Mise, coins, Inventaire, Objet))
        btn_Start.grid(sticky="s", row=6)
        
        #changer l'état des boutons
        if coins < 100:
            changeState(btn_1000)
            changeState(btn_500)
            changeState(btn_250)
            changeState(btn_100)

        elif coins < 250:
            changeState(btn_1000)
            changeState(btn_500)
            changeState(btn_250)

        elif coins < 500:
            changeState(btn_1000)
            changeState(btn_500)
        
        elif coins < 1000:
            changeState(btn_1000)
        
        window_roulette.mainloop()
        
    
    window_tp.withdraw()
     # creation de la 1e fenetre
    window_1 = Toplevel(window_tp)
    # configuration des parametres de la fenetre
    window_1.title("LA ROULETTE")
    window_1.geometry("1350x680")
    window_1.minsize(480 , 360)
    window_1.config(background='black')
    # pas de possibilité de + / - la fenetre
    window_1.resizable(height=False , width= False)
    Choix = "Rien"
    Mise = 0
    title = Label(window_1, text = "LA ROULETTE " , font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white')
    start = Button(window_1, text= "COMMENCER !", font= ("Super legend boy" , 60) , bg = 'black' , fg = 'white' , command = lambda : roulette_jeu(window_1, coins, Choix, Mise, Inventaire, Objet))
    title.pack(side=TOP)
    start.pack(expand=YES)

    #Affichage de l'objet actif
    objet = Label(window_1, text=("Objet actif :", Objet) , font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white')
    objet.pack(expand=YES)
    btn_Start = Button(window_1, text="Inventaire", font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' , command = lambda:  bag_roulette(window_1, coins, Inventaire, Objet))
    btn_Start.pack(expand=YES)

    #Si le joueur veut sortir
    if Objet == "Corde de sortie":
        tp(window_1, coins)
        Inventaire[2] = Inventaire[2]-1

    window_1.mainloop()
    

    
