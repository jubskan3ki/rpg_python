from tkinter import *
from random import randint
from PIL import ImageTk, Image
from OnePiece import One_Piece_Game
from deplacement3 import bag
from gamer_over import perdu
from time import sleep
from tkinter import Label,messagebox


def  tp(window,coins,objet) :
    window.withdraw()
    #cree une fentre 
    window_deplacement = Toplevel(window)
    #taille/nom/logo
    window_deplacement.title("GOLD GRABBER")
    window_deplacement.geometry("1600x900")
    window_deplacement.resizable(height=False,width=False)
    window_deplacement.iconbitmap("logo.ico")
    #fond de la fenetre menu
    window_deplacement.config(background='black')
    #
    objet[3] = 0
    objet[4] = 0
    objet_use = "Aucun"
    #
    if coins >=10000 :
        One_Piece_Game(window_deplacement)
    elif coins <100 :
            perdu(window_deplacement)
    else :
        coins = str(coins)
        #bouton deplacement
        morpion_bouton = Button(window_deplacement, text="Morpion",pady=122, padx=95 ,font=("Super Legend Boy",30), bg= 'black',fg='white',width=8,relief=GROOVE, bd=7.5,command=lambda: Morpion(window_deplacement,coins,objet))
        morpion_bouton.grid(row=0,column=0,padx=22,pady=75)
        machine_a_soue_bouton =Button(window_deplacement, text="Machine à sous",pady=122, padx=95 ,font=("Super Legend Boy",30), bg= 'black',fg='white',width=8,relief=GROOVE, bd=7.5,command=lambda:machine_a_sous(window_deplacement,coins,objet_use,objet))
        machine_a_soue_bouton.grid(row=0,column=1,padx=22,pady=75)
        roulette_bouton =Button(window_deplacement, text="Roulette",pady=122, padx=95 ,font=("Super Legend Boy",30), bg= 'black',fg='white',width=8,relief=GROOVE, bd=7.5,command=lambda:roulette(window_deplacement,coins,objet))
        roulette_bouton.grid(row=0,column=2,padx=22,pady=75)
        shop_bouton =Button(window_deplacement, text="Shop",pady=122, padx=95 , font=("Super Legend Boy",30), bg= 'black',fg='white', width=8,relief=GROOVE, bd=7.5,command=lambda:boutique(window_deplacement,coins,objet))
        shop_bouton.grid(row=1,column=0,padx=22)
        money =Button(window_deplacement, text=(coins," coins"),pady=122, padx=95 , font=("Super Legend Boy",30), bg= 'black',fg='white', width=8,relief=GROOVE, bd=7.5)
        money.grid(row=1,column=1,padx=22)
        quit_bouton =Button(window_deplacement, text="Quit",pady=122, padx=95 , font=("Super Legend Boy",30), bg= 'black',fg='white', width=8,relief=GROOVE, bd=7.5,command=quit)
        quit_bouton.grid(row=1,column=2,padx=22)
        
        #mettre a jour la fenetre du menu
        window_deplacement.mainloop()


# jeu de la machine a sous


def machine_a_sous(window,coins,objet_use, objet):
    #Ouvrir / fermer des fenêtres
    window.withdraw()

    #Changer l'état du bouton
    def changeState(btn):
        if (btn['state'] == NORMAL):
            btn['state'] = DISABLED
        else:
            btn['state'] = NORMAL


    #donner une valeur à une variable
    def action(Variable, valeur):
        Variable.set(valeur)

    #objet de la machine à sous
    def bag_machine(window, coins, objet_use, objet) :
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
        nombre_clic_3 = IntVar(Window_shop,value = objet_use[2])
        nombre_clic_2 = IntVar(Window_shop,value = objet_use[1]) 
        nombre_clic_1 = IntVar(Window_shop,value = objet_use[0])  
        
        lettre_3=str(nombre_clic_3.get())
        lettre_2=str(nombre_clic_2.get())
        lettre_1=str(nombre_clic_1.get())

        #Bouton et affichage pour l'objet 1, on lance la fonction en fonction de l'objet choisi
        Panel_item_1 = Label(Window_shop,text="Quitte ou Triple", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
        Panel_item_1.grid(row=0,column=0,pady=5)
        number_item_1=Label(Window_shop,text=lettre_1, font=("Super Legend Boy",20), bg='black',fg='white',height=3,width=5 )
        number_item_1.grid(row=0,column=1,pady=5)
        Button_item_1=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg='black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command= lambda : [machine_a_sous(Window_shop, coins, objet_use, "Quitte ou triple")])
        Button_item_1.grid(row=0,column=2,pady=5)
        if objet_use[0]==0:
            changeState(Button_item_1)
        #Idem
        Panel_item_2 = Label(Window_shop,text="Bouclier", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
        Panel_item_2.grid(row=1,column=0,pady=5)
        number_item_2=Label(Window_shop,text=lettre_2, font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
        number_item_2.grid(row=1,column=1,pady=5)
        Button_item_2=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:machine_a_sous(Window_shop, coins, objet_use, "Bouclier"))
        Button_item_2.grid(row=1,column=2,pady=5)
        if objet_use[1]==0:
            changeState(Button_item_2)
        #Idem
        Panel_item_3 = Label(Window_shop,text="Corde de sortie", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
        Panel_item_3.grid(row=2,column=0,pady=5)
        number_item_3=Label(Window_shop,text=lettre_3, font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
        number_item_3.grid(row=2,column=1,pady=5)
        Button_item_3=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:machine_a_sous(Window_shop, coins, objet_use, "Corde de sortie"))
        Button_item_3.grid(row=2,column=2,pady=5)
        if objet_use[2]==0:
            changeState(Button_item_3)
        #Bouton quitter au cas où on n'a pas d'objet
        Button_Quitte = Button(Window_shop,text="Exit",font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=25,relief=GROOVE, bd=7.5, command= lambda : machine_a_sous(Window_shop, coins, objet_use, objet))
        Button_Quitte.grid(row=3,column=0,columnspan=4,pady=5) 
        Window_shop.mainloop()

    #Définir le résultat
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
    def window_resultat(fenetre, Result, coins, Mise, objet_use, objet):
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
            if objet == "Quitte ou triple":
                Mise = Mise*3
                #L'objet disparaît de l'objet_use
                objet_use[0] = objet_use[0]-1

            #La mise gagnante s'ajoute à la mise
            coins = coins + Mise
        
            Label(window_resultat, text = ('Vous avez gagné', Mise,'coins.''Vous en avez maintenant',coins,'.'), font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white').pack(expand=YES)
            
            #on retourne dans la fonction déplacement avec les coins 
            quit = Button(window_resultat, text= "QUITTER !", font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' , command =lambda:tp(window_resultat,coins))
            quit.pack()
            window_resultat.mainloop()
        else :
            #Si l'objet Quitte ou triple est utilisé la mise perdante double
            if objet == "Quitte ou triple":
                Mise = Mise * 2
                objet_use[0] = objet_use[0]-1
            #Bouclier protège de la défaite, la mise est à 0
            elif objet == "Bouclier":
                Mise = 0
                objet_use[1] = objet_use[1]-1
            
            #La mise se soustrait aux coins et on les retourne dans la fonction déplacement
            coins = coins - Mise 
            Label(window_resultat, text = ('Vous avez perdu',Mise,"coins. Il vous en reste", coins,"."), font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white').pack()
            quit = Button(window_resultat, text= "QUITTER !", font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' , command =lambda:tp(window_resultat,coins)).pack()
            window_resultat.mainloop()
    
    #Fenêtre d'affichage de la mise
    def mise(window_2,coins, objet_use, objet):
    # creation 2e fenetre -> entrer la mise
        window_2.withdraw()
        Fenetre2 = Toplevel(start_machine)
        Fenetre2.title("MACHINE À SOUS")
        Fenetre2.geometry("1350x680")
        Fenetre2.config(background='black')
        Fenetre2.resizable(height=False , width= False)
        
        Label(Fenetre2, text="Choisissez votre mise." , font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white').pack()
        Label(Fenetre2, text=('Vous avez' ,coins, "coins.") , font= ("Super legend boy" , 20)).pack()
        objet = Label(Fenetre2, text=("objet actif :", objet) , font= ("Super legend boy" , 15) , bg = 'black' , fg = 'white')
        objet.pack()

        #Le résultat
        Result = resultats()

        #La valeur de la mise avant qu'on la choisisse grâce aux boutons
        IntMise = IntVar()
    
        #Les boutons de mise
        btn_100 = Radiobutton(Fenetre2 , text = 100 ,font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' ,variable= IntMise, value = 100,command = lambda : [window_resultat(Fenetre2, Result, coins, 100, objet_use, objet), action(IntMise, 100)], indicatoron=0)
        btn_100.pack(expand=YES)
        
        btn_250 = Radiobutton(Fenetre2 , text = 250,font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white',variable= IntMise, value = 250, command = lambda : [window_resultat(Fenetre2, Result, coins, 250, objet_use, objet), action(IntMise, 250)], indicatoron=0)
        btn_250.pack(expand=YES)
        
        btn_500 = Radiobutton(Fenetre2 , text = 500,font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' ,variable= IntMise, value = 500,command = lambda : [window_resultat(Fenetre2, Result, coins, 500, objet_use, objet), action(IntMise, 500)], indicatoron=0)
        btn_500.pack(expand=YES)
        
        btn_1000 = Radiobutton(Fenetre2 , text = 1000,font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' ,variable= IntMise, value = 1000,command = lambda : [window_resultat(Fenetre2, Result, coins, 1000, objet_use, objet), action(IntMise, 1000)], indicatoron=0)
        btn_1000.pack(expand=YES)
        
        btn_all = Radiobutton(Fenetre2 , text = "All in",font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' ,variable= IntMise, value = coins, command = lambda : [window_resultat(Fenetre2, Result, coins, coins, objet_use, objet), action(IntMise, coins)], indicatoron=0)
        btn_all.pack(expand=YES)

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
    start = Button(start_machine, text= "COMMENCER !", font= ("Super legend boy" , 60) , bg = 'black' , fg = 'white' , command =lambda:mise(start_machine,coins, objet_use, objet) )
    title.pack(side=TOP)
    start.pack(expand=YES)
    #On affiche l'objet actif 
    objet = Label(start_machine, text=("objet actif :", objet) , font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white')
    objet.pack(expand=YES)
    btn_Start = Button(start_machine, text="objet_use", font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' , command = lambda:  bag_machine(start_machine, coins, objet_use, objet))
    btn_Start.pack(expand=YES)

    #On regarde si l'utilisateur veut sortir
    if objet == "Corde de sortie":
        tp(start_machine, coins)
        objet_use[2] = objet_use[2]-1
    
    start_machine.mainloop()
    

# jeu de la roulette

def roulette(window_tp, coins, objet):

    def changeState(btn):
        if (btn['state'] == NORMAL):
            btn['state'] = DISABLED
        else:
            btn['state'] = NORMAL


    #donner une valeur à une variable
    def action(Variable, valeur):
        Variable.set(valeur)  

    #objet de la roulette, même fonctionnement que celui de la machine à sous
    def bag_roulette(window,coins,objet) :
        window.withdraw()
        Window_shop = Toplevel(window)
        #taille/nom/logo
        Window_shop.title("GOLD GRABBER")
        Window_shop.geometry("800x600")
        Window_shop.resizable(height=False,width=False)
        Window_shop.iconbitmap("logo.ico")
        #fond de la fenetre menu
        Window_shop.config(background='black')
        #
        def changeState(btn):
            if (btn['state'] == NORMAL):
                btn['state'] = DISABLED
            else:
                btn['state'] = NORMAL
        #fonction revenir en arrire
        
        def use_objet_1 (Window_shop,coins,objet):
            objet[0] -= 1
            objet[3] += 1
            roulette_jeu(Window_shop,coins,objet)
        lettre_1=str(objet[0])

        def use_objet_2 (Window_shop,coins,objet):
            objet[1] -= 1
            objet[4] += 1

            roulette_jeu(Window_shop,coins,objet)
        lettre_2=str(objet[1])

        def use_objet_3 (Window_shop,coins,objet):
            objet[2] -= 1
            tp(Window_shop,coins,objet)
        lettre_3=str(objet[2])
        #
        Panel_item_1 = Label(Window_shop,text="quitte ou double", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
        Panel_item_1.grid(row=0,column=0,pady=5)
        number_item_1=Label(Window_shop,text=lettre_1, font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
        number_item_1.grid(row=0,column=1,pady=5)
        Button_item_1=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:use_objet_1 (Window_shop,coins,objet))
        Button_item_1.grid(row=0,column=2,pady=5)
        if objet[0]==0:
            changeState(Button_item_1)
        #
        Panel_item_2 = Label(Window_shop,text="bouclier", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
        Panel_item_2.grid(row=1,column=0,pady=5)
        number_item_2=Label(Window_shop,text=lettre_2, font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
        number_item_2.grid(row=1,column=1,pady=5)
        Button_item_2=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:use_objet_2 (Window_shop,coins,objet))
        Button_item_2.grid(row=1,column=2,pady=5)
        if objet[1]==0:
            changeState(Button_item_2)
        #
        Panel_item_3 = Label(Window_shop,text="corde de sortie", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
        Panel_item_3.grid(row=2,column=0,pady=5)
        number_item_3=Label(Window_shop,text=lettre_3, font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
        number_item_3.grid(row=2,column=1,pady=5)
        Button_item_3=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:use_objet_3(Window_shop,coins,objet))
        Button_item_3.grid(row=2,column=2,pady=5)
        if objet[2]==0:
            changeState(Button_item_3)
        #
        Button_Quitte = Button(Window_shop,text="Exit",font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=25,relief=GROOVE, bd=7.5,command=lambda :roulette_jeu(Window_shop,coins,objet))
        Button_Quitte.grid(row=3,column=0,columnspan=4,pady=5) 
        Window_shop.mainloop()

    def resultat_window(window, Choix, Mise, coins, objet):
        window.withdraw()
        Jeu = Toplevel(window)
        Jeu.title("LA ROULETTE")
        Jeu.geometry("1350x680")
        Jeu.resizable(height=False , width= False)
        Jeu.config(background='black')
        
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
            if objet[3] == 1:
                Mise = Mise*3
                objet[0] = objet[0]-1
            coins = coins + Mise
            Label(Jeu, text="Vous avez gagné !",font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white').pack(expand=YES)
            Label(Jeu, text=("Vous disposez de",coins, "coins"),font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white').pack(expand=YES)
            quit = Button(Jeu, text= "QUITTER !", font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' , command = lambda:tp(Jeu,coins,objet))
            quit.pack()
            Jeu.mainloop()
        else :
            canvas1.create_text(width/2, 350, text=("Vous avez choisi", Choix), font= ("Super legend boy" , 30), fill="silver")            
            if objet[3] == 1:
                Mise = Mise * 2
                objet[0] = objet[0]-1
            elif objet[4] == 1:
                Mise = 0
                objet[1] = objet[1]-1
            coins = coins-Mise
            Label(Jeu, text = "Vous avez perdu.",font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white').pack(expand=YES)
            Label(Jeu, text=("Vous disposez de",coins, "coins"),font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white').pack(expand=YES)
            quit = Button(Jeu, text= "QUITTER !", font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' , command = lambda:tp(Jeu,coins,objet))
            quit.pack()
            Jeu.mainloop()
    
    def roulette_jeu(window, coins,choix,mise, objet):
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
        objet = Label(window_roulette, text=("objet actif :", objet) , font= ("Super legend boy" , 15) , bg = 'black' , fg = 'white')
        objet.grid(pady=20, row=5)
        choix = Label(window_roulette, text=("Choix de jeu :", choix) , font= ("Super legend boy" , 15) , bg = 'black' , fg = 'white')
        choix.grid(pady=20, row=3)
        coins = Label(window_roulette, text=("coins :", coins) , font= ("Super legend boy" , 15) , bg = 'black' , fg = 'white')
        coins.grid(pady=20, row=4)
        mise = Label(window_roulette, text=("Mise :", mise) , font= ("Super legend boy" , 15) , bg = 'black' , fg = 'white')
        mise.grid(pady=20, row=8)

        #Les boutons de jeux relance la fonction avec la nouvelle valeur
        btn_Manque = Radiobutton(window_roulette , text = "Manque" ,font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' ,variable= StrChoix, value = "Manque",command = lambda : [action(StrChoix, "Manque"),roulette_jeu(window_roulette, coins, "Manque", Mise, objet)], indicatoron=0)
        btn_Manque.grid(padx=10, pady=20, sticky="w", row = 3)
        btn_Passe = Radiobutton(window_roulette , text = "Passe" ,font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' ,variable= StrChoix, value = "Passe",command = lambda : [action(StrChoix, "Passe"),roulette_jeu(window_roulette, coins, "Passe", Mise, objet)], indicatoron=0)
        btn_Passe.grid(sticky="e", pady=20, row=3, padx=10)
        btn_Pair = Radiobutton(window_roulette , text = "Pair" ,font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' ,variable= StrChoix, value = "Pair",command = lambda : [action(StrChoix, "Pair"),roulette_jeu(window_roulette, coins, "Pair", Mise, objet)], indicatoron=0)
        btn_Pair.grid(sticky="w", row=4, padx=10, pady=20)
        btn_Impair = Radiobutton(window_roulette , text = "Impair" ,font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' ,variable= StrChoix, value = "Impair",command = lambda : [action(StrChoix, "Impair"),roulette_jeu(window_roulette, coins, "Impair", Mise, objet)], indicatoron=0)
        btn_Impair.grid(sticky="e", row=4, padx=10)
        btn_Rouge = Radiobutton(window_roulette , text = "Rouge" ,font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' ,variable= StrChoix, value = "Rouge",command = lambda : [action(StrChoix, "Rouge"),roulette_jeu(window_roulette, coins, "Rouge", Mise, objet)], indicatoron=0)
        btn_Rouge.grid(sticky="w", row=5, padx=10, pady=20)
        btn_Noir = Radiobutton(window_roulette , text = "Noir" ,font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' ,variable= StrChoix, value = "Noir",command = lambda : [action(StrChoix, "Noir"),roulette_jeu(window_roulette, coins, "Noir", Mise, objet)], indicatoron=0)
        btn_Noir.grid(sticky="e", row=5, padx=10, pady=20)

        #Les boutons de mise relance la fonction avec la nouvelle valeur
        btn_100 = Radiobutton(window_roulette , text = 100 ,font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' ,variable= IntMise, value = 100,command = lambda : [action(IntMise, 100),roulette_jeu(window_roulette, coins, Choix, 100, objet)], indicatoron=0)
        btn_100.grid(sticky="w", row=8, padx=10)
        
        btn_250 = Radiobutton(window_roulette , text = 250,font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white',variable= IntMise, value = 250, command = lambda : [action(IntMise, 250),roulette_jeu(window_roulette, coins, Choix, 250, objet)], indicatoron=0)
        btn_250.grid(sticky="e", row=8, padx=10)
        
        
        btn_500 = Radiobutton(window_roulette , text = 500,font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' ,variable= IntMise, value = 500,command = lambda : [action(IntMise, 500),roulette_jeu(window_roulette, coins, Choix, 500, objet)], indicatoron=0)
        btn_500.grid(sticky="w", row=9, padx=10, pady=20)
        
        btn_1000 = Radiobutton(window_roulette , text = 1000,font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' ,variable= IntMise, value = 1000,command = lambda : [action(IntMise, 1000),roulette_jeu(window_roulette, coins, Choix, 1000, objet)], indicatoron=0)
        btn_1000.grid(sticky="e", row=9, padx=10, pady=20)
        
        btn_all = Radiobutton(window_roulette , text = "All in",font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' ,variable= IntMise, value = coins, command = lambda : [action(IntMise, coins),roulette_jeu(window_roulette, coins, Choix, coins, objet)], indicatoron=0)
        btn_all.grid(sticky="s", row=9)
        
        btn_Start = Button(window_roulette, text="Start", font= ("Super legend boy" , 20) , bg = 'black' , fg = 'white' , command =lambda:resultat_window(window_roulette, Choix, Mise, coins, objet))
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
    window_roulette = Toplevel(window_tp)
    # configuration des parametres de la fenetre
    window_roulette.title("LA ROULETTE")
    window_roulette.geometry("1350x680")
    window_roulette.minsize(480 , 360)
    window_roulette.config(background='black')
    # pas de possibilité de + / - la fenetre
    window_roulette.resizable(height=False , width= False)
    Choix = "Rien"
    Mise = 0
    title = Label(window_roulette, text = "LA ROULETTE " , font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white')
    start = Button(window_roulette, text= "COMMENCER !", font= ("Super legend boy" , 60) , bg = 'black' , fg = 'white' , command = lambda : roulette_jeu(window_roulette, coins,Choix,Mise, objet))
    title.pack(side=TOP)
    start.pack(expand=YES)

    #Affichage de l'objet actif
    btn_Start = Button(window_roulette, text="objet_use", font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' , command = lambda:  bag_roulette(window_roulette, coins, objet))
    btn_Start.pack(expand=YES)


    window_roulette.mainloop()


# la boutique


def boutique(window,coins,objet) :

    def changeState(btn):
        if (btn['state'] == NORMAL):
            btn['state'] = DISABLED
        else:
            btn['state'] = NORMAL
    
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
    def back (window1,window2):
        window1.withdraw()
        window2.deiconify()

    def add_objet_1 (Window_shop,coins,objet):
        objet[0] += 1
        coins -= 500
        tp(Window_shop,coins,objet)
    lettre_1=str(objet[0])

    def add_objet_2 (Window_shop,coins,objet):
        objet[1] += 1
        coins -= 250
        tp(Window_shop,coins,objet)
    lettre_2=str(objet[1])

    def add_objet_3 (Window_shop,coins,objet):
        objet[2] += 1
        coins -= 100
        tp(Window_shop,coins,objet)
    lettre_3=str(objet[2])

    #
    Panel_item_1 = Label(Window_shop,text="double ou triple", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_1.grid(row=0,column=0,pady=5)
    number_item_1=Label(Window_shop,text=lettre_1, font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
    number_item_1.grid(row=0,column=1,pady=5)
    Button_item_1=Button(Window_shop, text="500", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:add_objet_1(Window_shop,coins,objet))
    Button_item_1.grid(row=0,column=2,pady=5)
    #
    Panel_item_2 = Label(Window_shop,text="bouclier", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_2.grid(row=1,column=0,pady=5)
    number_item_2=Label(Window_shop,text=lettre_2, font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
    number_item_2.grid(row=1,column=1,pady=5)
    Button_item_2=Button(Window_shop, text="250", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:add_objet_2(Window_shop,coins,objet))
    Button_item_2.grid(row=1,column=2,pady=5)
    #
    Panel_item_3 = Label(Window_shop,text="corde de sortie", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_3.grid(row=2,column=0,pady=5)
    number_item_3=Label(Window_shop,text=lettre_3, font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
    number_item_3.grid(row=2,column=1,pady=5)
    Button_item_3=Button(Window_shop, text="100", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:add_objet_3(Window_shop,coins,objet))
    Button_item_3.grid(row=2,column=2,pady=5)
    #
    Button_Quitte = Button(Window_shop,text="Exit",font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=25,relief=GROOVE, bd=7.5,command=lambda:tp(Window_shop,coins,objet))
    Button_Quitte.grid(row=3,column=0,columnspan=4,pady=5) 

    if coins < 500:
        changeState(Button_item_1)
    elif coins < 250:
        changeState(Button_item_1)
        changeState(Button_item_2)
    elif coins < 100:
        changeState(Button_item_1)
        changeState(Button_item_2)
        changeState(Button_item_3)

    Window_shop.mainloop()


#le morpion 


def Morpion (window,coins,objet):
    window.withdraw()
    # La fenetre du lancement du jeu
    Windows_real_Game = Toplevel(window)
    Windows_real_Game.title("Morpion")
    Windows_real_Game.iconbitmap('logo.ico')
    Windows_real_Game.geometry("1600x900")
    Windows_real_Game.resizable(height=False,width=False)
    Windows_real_Game.config(background='#000000')

    # Boite de rangement
    Frame_Box = Frame(Windows_real_Game)

    # Les Bouttons et l'affichage
    title_Game = Label(Windows_real_Game, text = "Le Morpion" ,font=("Super legend boy",40), bg = 'black' , fg = 'white')
    Button_Inventory = Button(Frame_Box,text="objet_use",font=("Super legend boy", 40),padx=150,pady=100,bg='black',fg='white',command=lambda:bag_morpion(Windows_real_Game,coins,objet))
    Button_Start = Button(Frame_Box,text= "Start",font=("Super legend boy", 60),bg='black',fg='white',padx=150,pady=75,command= lambda : Pari(Windows_real_Game,coins,objet))

    # Rangement dans la fenetre
    title_Game.pack(side=TOP)
    Frame_Box.pack(expand=YES)

    # Placement dans la box
    Button_Inventory.grid(row=0,column=0)
    Button_Start.grid(row=0,column=1)

    # Affichage de la fenetre
    Windows_real_Game.mainloop()

def Pari(Window,coins,objet):
    
    # la fenetre des bets
    Window.withdraw()
    Window_Bet = Toplevel(Window)
    Window_Bet.title("Morpion")
    Window_Bet.geometry("1600x900")
    Window_Bet.resizable(height=False,width=False)
    Window_Bet.config(background='#000000')
    
    #Changer l'état du bouton
    def changeState(btn):
        if (btn['state'] == NORMAL):
            btn['state'] = DISABLED
        else:
          btn['state'] = NORMAL

    # les boutons et affichage
    Label(Window_Bet, text="Choisissez votre mise." , font= ("Super legend boy" , 40) , bg = 'black' , fg = 'white').pack()
    Label(Window_Bet, text=('Vous avez' ,coins, "coins.") , font= ("Super legend boy" , 20)).pack()
    
    #Le résultat
    #Result = resultats()

    #La valeur de la mise avant qu'on la choisisse grâce aux boutons
    IntMise = IntVar()
    
    #Les boutons de mise
    btn_100 = Radiobutton(Window_Bet , text = 100 ,font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' ,variable= IntMise, value = 100,command = lambda : Game_Morpion(Window_Bet,coins,100,objet))#, action(IntMise, 100)], indicatoron=0)
    btn_100.pack(expand=YES)
    
    btn_250 = Radiobutton(Window_Bet , text = 250,font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white',variable= IntMise, value = 250, command = lambda : Game_Morpion(Window_Bet,coins, 250,objet))#, action(IntMise, 250)], indicatoron=0)
    btn_250.pack(expand=YES)
    
    btn_500 = Radiobutton(Window_Bet , text = 500,font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' ,variable= IntMise, value = 500,command = lambda : Game_Morpion(Window_Bet,coins, 500,objet))#, action(IntMise, 500)], indicatoron=0)
    btn_500.pack(expand=YES)
    
    btn_1000 = Radiobutton(Window_Bet , text = 1000,font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' ,variable= IntMise, value = 1000,command = lambda : Game_Morpion(Window_Bet,coins, 1000,objet))#, action(IntMise, 1000)], indicatoron=0)
    btn_1000.pack(expand=YES)
    
    btn_all = Radiobutton(Window_Bet , text = "All in",font= ("Super legend boy" , 30) , bg = 'black' , fg = 'white' ,variable= IntMise, value = coins, command = lambda : Game_Morpion(Window_Bet,coins, coins,objet))#, action(IntMise, coins)], indicatoron=0)
    btn_all.pack(expand=YES)

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

    Window_Bet.mainloop()   

def bag_morpion(window,coins,objet) :
    window.withdraw()
    Window_shop = Toplevel(window)
    #taille/nom/logo
    Window_shop.title("GOLD GRABBER")
    Window_shop.geometry("800x600")
    Window_shop.resizable(height=False,width=False)
    Window_shop.iconbitmap("logo.ico")
    #fond de la fenetre menu
    Window_shop.config(background='black')
    #
    def changeState(btn):
        if (btn['state'] == NORMAL):
            btn['state'] = DISABLED
        else:
            btn['state'] = NORMAL
    #fonction revenir en arrire
    
    def use_objet_1 (Window_shop,coins,objet):
        objet[0] -= 1
        objet[3] += 1
        Pari(Window_shop,coins,objet)
    lettre_1=str(objet[0])

    def use_objet_2 (Window_shop,coins,objet):
        objet[1] -= 1
        objet[4] += 1

        Pari(Window_shop,coins,objet)
    lettre_2=str(objet[1])

    def use_objet_3 (Window_shop,coins,objet):
        objet[2] -= 1
        tp(Window_shop,coins,objet)
    lettre_3=str(objet[2])
    #
    Panel_item_1 = Label(Window_shop,text="quitte ou double", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_1.grid(row=0,column=0,pady=5)
    number_item_1=Label(Window_shop,text=lettre_1, font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
    number_item_1.grid(row=0,column=1,pady=5)
    Button_item_1=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:use_objet_1 (Window_shop,coins,objet))
    Button_item_1.grid(row=0,column=2,pady=5)
    if objet[0]==0:
        changeState(Button_item_1)
    #
    Panel_item_2 = Label(Window_shop,text="bouclier", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_2.grid(row=1,column=0,pady=5)
    number_item_2=Label(Window_shop,text=lettre_2, font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
    number_item_2.grid(row=1,column=1,pady=5)
    Button_item_2=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:use_objet_2 (Window_shop,coins,objet))
    Button_item_2.grid(row=1,column=2,pady=5)
    if objet[1]==0:
        changeState(Button_item_2)
    #
    Panel_item_3 = Label(Window_shop,text="corde de sortie", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_3.grid(row=2,column=0,pady=5)
    number_item_3=Label(Window_shop,text=lettre_3, font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
    number_item_3.grid(row=2,column=1,pady=5)
    Button_item_3=Button(Window_shop, text="use", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:use_objet_3(Window_shop,coins,objet))
    Button_item_3.grid(row=2,column=2,pady=5)
    if objet[2]==0:
        changeState(Button_item_3)
    #
    Button_Quitte = Button(Window_shop,text="Exit",font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=25,relief=GROOVE, bd=7.5,command=lambda :Pari(Window_shop,coins,objet))
    Button_Quitte.grid(row=3,column=0,columnspan=4,pady=5) 
    Window_shop.mainloop()

def Game_Morpion (Window,coins,mise,objet):

    # La fenetre de jeu
    Window.withdraw()
    Windows_Principale = Toplevel(Window)
    Windows_Principale.title("Morpion")
    Windows_Principale.iconbitmap('logo.ico')
    Windows_Principale.geometry("1600x900")
    Windows_Principale.resizable(height=False,width=False)
    Windows_Principale.config(background='#000000')

    # Utilité
    Turn = [0]
    List_Map = [
        ["1","2","3",],
        ["4","5","6",],
        ["7","8","9",]
    ]
    List_Vérif = []

    def Game(Windows_Principale,Nbr,List_Vérif,List_Map,Turn,coins,mise,objet):
        Winner = False
        if not Winner:
            Button_Game(Nbr)
            List_Vérif.append(Nbr)
            Player = True
            Turn[0] = Turn[0] + 1
            Map_Creation(List_Map,Nbr,Player)
            Win_Condition(Windows_Principale,List_Map,Turn,coins,mise,objet)
        
        if len(List_Vérif) < 9 and not Winner  :
            Button_Bot(List_Vérif)
            Nbr = List_Vérif[-1]
            Player = not Player
            Turn[0] = Turn[0] + 1
            Map_Creation(List_Map,Nbr,Player)
            Win_Condition(Windows_Principale,List_Map,Turn,coins,mise,objet)

        

    
    # La boite de rangement
    Frame_Game = Frame(Windows_Principale,bg='#000000')

    # Les boutons du jeu : création
    Button_1 = Button(Frame_Game, text="1", padx=50, pady=20,font= ("Super legend boy" , 30),command= lambda : Game(Windows_Principale,1,List_Vérif,List_Map,Turn,coins,mise,objet))
    Button_2 = Button(Frame_Game, text="2", padx=50, pady=20,font= ("Super legend boy" , 30),command= lambda : Game(Windows_Principale,2,List_Vérif,List_Map,Turn,coins,mise,objet))
    Button_3 = Button(Frame_Game, text="3", padx=50, pady=20,font= ("Super legend boy" , 30),command= lambda : Game(Windows_Principale,3,List_Vérif,List_Map,Turn,coins,mise,objet))
    Button_4 = Button(Frame_Game, text="4", padx=50, pady=20,font= ("Super legend boy" , 30),command= lambda : Game(Windows_Principale,4,List_Vérif,List_Map,Turn,coins,mise,objet))
    Button_5 = Button(Frame_Game, text="5", padx=50, pady=20,font= ("Super legend boy" , 30),command= lambda : Game(Windows_Principale,5,List_Vérif,List_Map,Turn,coins,mise,objet))
    Button_6 = Button(Frame_Game, text="6", padx=50, pady=20,font= ("Super legend boy" , 30),command= lambda : Game(Windows_Principale,6,List_Vérif,List_Map,Turn,coins,mise,objet))
    Button_7 = Button(Frame_Game, text="7", padx=50, pady=20,font= ("Super legend boy" , 30),command= lambda : Game(Windows_Principale,7,List_Vérif,List_Map,Turn,coins,mise,objet))
    Button_8 = Button(Frame_Game, text="8", padx=50, pady=20,font= ("Super legend boy" , 30),command= lambda : Game(Windows_Principale,8,List_Vérif,List_Map,Turn,coins,mise,objet))
    Button_9 = Button(Frame_Game, text="9", padx=50, pady=20,font= ("Super legend boy" , 30),command= lambda : Game(Windows_Principale,9,List_Vérif,List_Map,Turn,coins,mise,objet))
        

    #Fonction des bouttons
    def Button_Game(Nbr):
        if Nbr == 1:
            Button_1.config(text="X",bg='Blue',state=DISABLED)
        elif Nbr == 2 :
            Button_2.config(text="X",bg='blue',state=DISABLED)
        elif Nbr == 3 :
            Button_3.config(text="X",bg='blue',state=DISABLED)
        elif Nbr == 4 :
            Button_4.config(text="X",bg='blue',state=DISABLED)    
        elif Nbr == 5 :
            Button_5.config(text="X",bg='blue',state=DISABLED)
        elif Nbr == 6 :
            Button_6.config(text="X",bg='blue',state=DISABLED)
        elif Nbr == 7 :
            Button_7.config(text="X",bg='blue',state=DISABLED)
        elif Nbr == 8 :
            Button_8.config(text="X",bg='blue',state=DISABLED)
        elif Nbr == 9 :
            Button_9.config(text="X",bg='blue',state=DISABLED)
        
            
    
    # Game du Bot
    def Button_Bot(List_Vérif):
        Random_bot = randint (1,9)
        while Random_bot in List_Vérif :
            Random_bot = randint (1,9)

        if Random_bot == 1:
            Button_1.config(text="O",bg='red',state=DISABLED)
            List_Vérif.append(Random_bot)
        elif Random_bot == 2 :
            Button_2.config(text="O",bg='red',state=DISABLED)
            List_Vérif.append(Random_bot)
        elif Random_bot == 3 :
            Button_3.config(text="O",bg='red',state=DISABLED)
            List_Vérif.append(Random_bot)
        elif Random_bot == 4 :
            Button_4.config(text="O",bg='red',state=DISABLED) 
            List_Vérif.append(Random_bot)   
        elif Random_bot == 5 :
            Button_5.config(text="O",bg='red',state=DISABLED)
            List_Vérif.append(Random_bot)
        elif Random_bot == 6 :
            Button_6.config(text="O",bg='red',state=DISABLED)
            List_Vérif.append(Random_bot)
        elif Random_bot == 7 :
            Button_7.config(text="O",bg='red',state=DISABLED)
            List_Vérif.append(Random_bot)
        elif Random_bot == 8 :
            Button_8.config(text="O",bg='red',state=DISABLED)
            List_Vérif.append(Random_bot)
        elif Random_bot == 9 :
            Button_9.config(text="O",bg='red',state=DISABLED)
            List_Vérif.append(Random_bot)
        return List_Vérif      

    # Fonction pour verif la map
    def Map_Creation (List_Map ,Nbr,Player):
        if Player :
            Sign_of_Player = "X"
        else :
            Sign_of_Player = "O"

        if Nbr == 1:
            List_Map[0][0] = Sign_of_Player
        elif Nbr == 2:
            List_Map[0][1] = Sign_of_Player
        elif Nbr == 3:
            List_Map[0][2] = Sign_of_Player
        elif Nbr == 4:
            List_Map[1][0] = Sign_of_Player
        elif Nbr == 5:
            List_Map[1][1] = Sign_of_Player
        elif Nbr == 6:
            List_Map[1][2] = Sign_of_Player        
        elif Nbr == 7:
            List_Map[2][0] = Sign_of_Player
        elif Nbr == 8:
            List_Map[2][1] = Sign_of_Player
        elif Nbr == 9:
            List_Map[2][2] = Sign_of_Player
        
        return List_Map 
    

    #Win condition
    def Win_Condition(Windows_Principale,List_Map,Turn,coins,mise,objet):
        if List_Map[0][1] == List_Map[0][2] and List_Map[0][2] == List_Map[0][0]:
                if List_Map[0][1] == 'X':
                    Win(Windows_Principale,1,coins,mise,objet)
                else:
                    Win(Windows_Principale,2,coins,mise,objet)
        elif List_Map[1][1] == List_Map[1][2] and List_Map[1][2] == List_Map[1][0]:
                if List_Map[1][1] == 'X':
                    Win(Windows_Principale,1,coins,mise,objet)
                else:
                   Win(Windows_Principale,2,coins,mise,objet)
        elif List_Map[2][1] == List_Map[2][2] and List_Map[2][2] == List_Map[2][0]:
                if List_Map[2][1] == 'X':
                   Win(Windows_Principale,1,coins,mise,objet)
                else:
                    Win(Windows_Principale,2,coins,mise,objet)
        elif List_Map[0][0] == List_Map[1][0] and List_Map[1][0] == List_Map[2][0]:
                if List_Map[0][0] == 'X':
                    Win(Windows_Principale,1,coins,mise,objet)
                else:
                    Win(Windows_Principale,2,coins,mise,objet)
        elif List_Map[0][1] == List_Map[1][1] and List_Map[1][1] == List_Map[2][1]:
                if List_Map[0][1] == 'X':
                    Win(Windows_Principale,1,coins,mise,objet)
                else:
                    Win(Windows_Principale,2,coins,mise,objet)
        elif List_Map[0][2] == List_Map[1][2] and List_Map[1][2] == List_Map[2][2]:
                if List_Map[0][2] == 'X':
                    Win(Windows_Principale,1,coins,mise,objet)
                else:
                    Win(Windows_Principale,2,coins,mise,objet)
        elif List_Map[0][0] == List_Map[1][1] and List_Map[1][1] == List_Map[2][2]:
            if List_Map[1][1] == 'X':
               Win(Windows_Principale,1,coins,mise,objet)
            else :
                Win(Windows_Principale,2,coins,mise,objet) 
        elif List_Map[0][2] == List_Map[1][1] and List_Map[2][0] == List_Map[1][1]:
            if List_Map[0][2] == 'X':
                Win(Windows_Principale,1,coins,mise,objet)
            else :
               Win(Windows_Principale,2,coins,mise,objet) 
        if Turn[0] == 9 :
            Win(Windows_Principale,3,coins,mise,objet)
        
        

        

    #Message Box of end of the game
    def Win (Windows_Principale,Winner,coins,mise,objet):
        if objet[3] == 1 :
            if Winner == 1 :
                Label(Windows_Principale).pack
                coins = int(coins + mise/4*3)
                tp(Windows_Principale,coins,objet)
            elif Winner == 2 :
                Label(Windows_Principale).pack
                coins = int(coins - mise*2)
                tp(Windows_Principale,coins,objet)
            elif Winner == 3 :
                Label(Windows_Principale).pack  
                coins = coins 
                tp(Windows_Principale,coins,objet)
        elif objet[4] == 1 :
            if Winner == 1 :
                Label(Windows_Principale).pack
                coins = int(coins + mise/4)
                tp(Windows_Principale,coins,objet)
            elif Winner == 2 :
                Label(Windows_Principale).pack
                coins = coins
                tp(Windows_Principale,coins,objet)
            elif Winner == 3 :
                Label(Windows_Principale).pack  
                coins = coins 
                tp(Windows_Principale,coins,objet)
        else :
            if Winner == 1 :
                Label(Windows_Principale).pack
                coins = int(coins + mise/4)
                tp(Windows_Principale,coins,objet)
            elif Winner == 2 :
                Label(Windows_Principale).pack
                coins = coins - mise
                tp(Windows_Principale,coins,objet)
            elif Winner == 3 :
                Label(Windows_Principale).pack  
                coins = coins 
                tp(Windows_Principale,coins,objet) 
         

    # La boite de rangement dans la fenetre
    Frame_Game.pack(expand=YES)
    #Frame_Menu.pack(expand=YES)

    # Les boutons du jeu : ajout
    Button_1.grid(row=0, column=0)
    Button_2.grid(row=0, column=1)
    Button_3.grid(row=0, column=2)
    Button_4.grid(row=1, column=0)
    Button_5.grid(row=1, column=1)
    Button_6.grid(row=1, column=2)
    Button_7.grid(row=2, column=0)
    Button_8.grid(row=2, column=1)
    Button_9.grid(row=2, column=2)

        
    Windows_Principale.mainloop()