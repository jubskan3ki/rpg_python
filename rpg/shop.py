from tkinter import *

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
    objet[1]= IntVar(Window_shop,value= objet[1] ) 
    def add_objet_1 (lettre_1,coins,number_item_1):
        objet[1].set( objet[1].get() + 1 )
        lettre_1=str(objet[1].get())
        number_item_1.config(text=lettre_1)
        coins -= 100
    lettre_1=str(objet[1].get())
    objet[2]= IntVar(Window_shop,value= objet[1] ) 
    def add_objet_2 (lettre_2,coins,number_item_2):
        objet[2].set( objet[2].get() + 1 )
        lettre_2=str(objet[1].get())
        number_item_2.config(text=lettre_2)
        coins -= 100
    lettre_2=str(objet[2].get())
    objet[3]= IntVar(Window_shop,value= objet[1] ) 
    def add_objet_3 (lettre_3,coins,number_item_3):
        objet[2].set( objet[3].get() + 1 )
        lettre_3=str(objet[3].get())
        number_item_3.config(text=lettre_3)
        coins -= 100
    lettre_3=str(objet[3].get())
    #
    Panel_item_1 = Label(Window_shop,text="double ou triple", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_1.grid(row=0,column=0,pady=5)
    number_item_1=Label(Window_shop,text=lettre_1, font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
    number_item_1.grid(row=0,column=1,pady=5)
    Button_item_1=Button(Window_shop, text="500", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:add_objet_1(lettre_1,coins,number_item_1))
    Button_item_1.grid(row=0,column=2,pady=5)
    #
    Panel_item_2 = Label(Window_shop,text="bouclier", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_2.grid(row=1,column=0,pady=5)
    number_item_2=Label(Window_shop,text=lettre_2, font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
    number_item_2.grid(row=1,column=1,pady=5)
    Button_item_2=Button(Window_shop, text="250", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:add_objet_2(lettre_2,coins,number_item_2))
    Button_item_2.grid(row=1,column=2,pady=5)
    #
    Panel_item_3 = Label(Window_shop,text="corde de sortie", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=20)
    Panel_item_3.grid(row=2,column=0,pady=5)
    number_item_3=Label(Window_shop,text=lettre_3, font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5 )
    number_item_3.grid(row=2,column=1,pady=5)
    Button_item_3=Button(Window_shop, text="100", font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=5,relief=GROOVE, bd=7.5,command=lambda:add_objet_3(lettre_3,coins,number_item_3))
    Button_item_3.grid(row=2,column=2,pady=5)
    #
    Button_Quitte = Button(Window_shop,text="Exit",font=("Super Legend Boy",20), bg= 'black',fg='white',height=3,width=25,relief=GROOVE, bd=7.5)
    Button_Quitte.grid(row=3,column=0,columnspan=4,pady=5) 

    if coins < 100:
        changeState(Button_item_3)
    elif coins < 250:
        changeState(Button_item_3)
        changeState(Button_item_2)
    elif coins < 500:
        changeState(Button_item_3)
        changeState(Button_item_2)
        changeState(Button_item_1)

    Window_shop.mainloop()
