# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 23:19:19 2022

@author: jinam
"""


try:
    from tkinter import *
    import Login_register
    from Todo_list import To_Do_List
    import cv2 
    import tkinter.messagebox as tmsg
    import webbrowser
    import Acads
    import Stats
    from Play_games import Game
    
    class Login(Tk):
        
        x = -99
    
        def __init__(self):
            
            super().__init__()
            self.geometry("1100x650")
            self.title("STUDAL")
            self.minsize(1100,650) 
            self.maxsize(1100,650)
        
        def user_page(self):
            
            self.f0 = Frame( self , bg = "light pink" )
            self.f0.place( x = 0 , y = 0 , width = 1100 , height = 650 )
    
            self.bg = PhotoImage( file = "frpg.png")
            self.background_label=Label( self , image = self.bg )
            self.background_label.place( x = 0 , y = 0 , relwidth = 1, relheight = 1 )
            
            self.headinng = Label( self , text = "WELCOME" , font = ("Georgia",35) , bg = "white" , fg = "black" ).place(x=400,y=40)
            
            self.ToDoList = Button( self , text="To-Do-List", font=("Georgia",20), fg = "black" , bg = "white" , padx = 2 , relief = SUNKEN , command = lambda: To_Do_List.TODO(self) ).place(x = 200, y = 150)
            
            self.stats = Button( self , text="Statistics", font=("Georgia",20), fg = "black" , bg = "white" , padx = 2 , relief = SUNKEN , command = lambda: Stats.Statistics(self) ).place(x = 200, y = 250)
    
            self.acad_cal = Button( self , text="Academics calendar", font=("Georgia",20), fg = "black" , bg = "white" , padx = 2 , relief = SUNKEN , command = Acads.acad_calender ).place(x = 200, y = 350)
            
            self.tt = Button( self , text="Time-Table", font=("Georgia",20), fg = "black" , bg = "white" , padx = 2 , relief = SUNKEN , command = Acads.TT ).place(x = 600, y = 150)
    
            self.sm = Button( self , text="Study Material", font=("Georgia",20), fg = "black" , bg = "white" , padx = 2 , relief = SUNKEN , command = Acads.Study_Material).place(x = 600, y = 250)
    
            self.game = Button( self , text="Games", font=("Georgia",20), fg = "black" , bg = "white" , padx = 2 , relief = SUNKEN , command = lambda : Game.gamers(self)).place(x = 600, y = 350)
    
            self.prev = Button( self , text = "<<Prev" , font = ( "Georgia", 15) , fg = "black" , bg = "white" , padx = 2 , relief = SUNKEN , command = self.Loginn).place( x = 25 , y = 50 )
    
        def Loginn(self):
        
            self.f1 = Frame( self , bg = "light pink" )
            self.f1.place( x = 0 , y = 0 , width = 1100 , height = 650 )
    
             
            self.bg = PhotoImage( file = "frpg.png")
            self.background_label=Label( self , image = self.bg )
            self.background_label.place( x = 0 , y = 0 , relwidth = 1, relheight = 1 )
           
            def set_value():
                 L = Login_register.Log_in( self.email_val.get() , self.password_val.get() )
                 self.x = L.checker()
                 #print(self.email_val.get() , self.password_val.get() )
                 #print(self.x)
                 if( self.x == None ):
                     tmsg.showerror("ERROR","You Are Not A Registered User!\nPlease register to Log in to the portal")
                 elif( self.x > 0 ):
                     self.user_page()
                 elif( self.x == -1 ):
                     tmsg.showerror("ERROR","Incorrect Password! \nEnter The Correct Password")
    
            self.headinng = Label( self , text = "LOGIN TO YOUR ACCOUNT" , font = ("Georgia",35) , bg = "#E29C00" , fg = "black" ).place(x=280,y=50)
    
            #for email
            self.email1 = Label( self , text = "E-mail Id :- " , font = ("Georgia",20) , fg = "black" , bg = "white" , padx = 5, relief = SUNKEN).place(x=350,y=200)
            self.email_val = StringVar()
            self.email = Entry( self , width = 35 , textvariable = self.email_val ,bg="white",fg="black").place(x=550,y=200)
            
            #for password
            self.password1 = Label( self , text="Password :- " , font = ("Georgia",20) , fg = "black" , bg = "white" , padx = 5, relief = SUNKEN ).place( x = 350 , y = 280)
            self.password_val = StringVar()
            self.password = Entry( self , show = "*", width = 35 , textvariable = self.password_val,bg="white",fg="black" ).place( x = 550 , y = 280)
               
            #back button
            self.home = Button(self , text="<<Home" , font=("Georgia",18) , fg = "black" , bg = "white" , padx = 2 , relief = SUNKEN , command = self.front_page).place(x=25,y=40)
            #sumbit button
            self.submit = Button(self , text="SUBMIT", font=("Cooper Black",20), fg = "black" , bg = "white" , padx = 5 , relief = SUNKEN , command = set_value ).place(x = 850 , y = 350)
    
        def register(self):
    
            self.f2 = Frame( self , bg = "light pink" ).place( x = 0 , y = 0 , width = 1100 , height = 650 )
    
            # atharva start 
            self.bg = PhotoImage( file = "frpg.png")
            self.background_label=Label( self , image = self.bg )
            self.background_label.place( x = 0 , y = 0 , relwidth = 1, relheight = 1 )
            # atharva end
    
            self.headinng=Label(self,text="REGISTRATION",width="20",font=("Georgia",35),bg="#E29C00",fg="black").place( x = 320 , y = 40)
    
            self.email1 = Label( self , text = "E-Mail Id" ,width="12", font = ("Georgia",18) , fg = "black" , bg = "white" , padx = 5 , relief = SUNKEN ).place( x = 350 , y = 150 )
            self.email_val = StringVar()
            self.email = Entry( self ,  textvariable = self.email_val , width = 35 ).place(x=630,y=150)
    
    
            self.password1 = Label( self , text = "Password" , width="12", font = ("Georgia",18) , fg = "black" , bg = "white" , padx = 5 , relief = SUNKEN ).place( x = 350 , y = 210 )
            self.password_val = StringVar()
            self.password = Entry( self , textvariable = self.password_val , show = "*" , width = 35 ).place( x = 630 , y = 210)
    
    
            self.name1 = Label( self , text = "Name", width="12" , font = ("Georgia",18) , fg = "black" , bg = "white" , padx = 5 , relief = SUNKEN ).place( x = 350, y = 270 )
            self.name_val = StringVar()
            self.name = Entry( self , textvariable = self.name_val , width = 35 ).place( x = 630 , y = 270 )
    
            self.phn1 = Label( self , text = "Mobile No." ,width="12", font = ("Georgia",18) , fg = "black" , bg = "white" , padx = 5 , relief = SUNKEN ).place( x = 350 , y = 330 ) 
            self.phn_val = IntVar()        
            self.phn = Entry( self , textvariable = self.phn_val , width = 35 ).place( x = 630 , y = 330 )
            
                
            #if( (self.phn_val.get()).len() != 10 ):
             #   tmsg.showerro("ERROR","Enter Valid Phone Number")            
    
    
            self.School1 = Label( self , text = "University" ,width="12", font = ("Georgia",18) , fg = "black" , bg = "white" , padx = 5 , relief = SUNKEN).place( x = 350, y = 390 )
            self.School_val = StringVar()
            self.School = Entry( self , textvariable = self.School_val , width = 35 ).place( x = 630 , y = 390 )
    
    
            def set_value2():
                try:
                    R = Login_register.Registration(self.email_val.get() , self.password_val.get() , self.name_val.get() , self.phn_val.get() , self.School_val.get())
                    R.first_registration()
                    self.front_page()
                    self.completion = Label(self , text = "Registration Completed !" , width = "75" , font = ("Georgia",20) , fg = "red" , bg = "light pink" ).place( x = 0 , y = 550 )
                except TclError:
                    tmsg.showerror("ERROR",  "Enter Valid Phone number !")
    
            #back button
            self.home = Button( self , text = "<<Home" , font = ( "Georgia", 15) , fg = "black" , bg = "white" , padx = 2 , relief = SUNKEN , command = self.front_page).place( x = 25 , y = 50 )
    
            #submit button
            self.Submit = Button(self , text="SUBMIT", font=( "Cooper Black", 20), fg = "black" , bg = "white" , padx = 2 , relief = SUNKEN , command = set_value2 ).place(x = 900, y = 450)
    
                       
        def front_page(self):
        
            #self.f3 = Frame( self , bg = "light pink" )
            #self.f3.place( x = 0 , y = 0 , width = 1100 , height = 650 ) 
           
            self.bg = PhotoImage( file = "frpg.png")
            self.background_label=Label( self , image = self.bg )
            self.background_label.place( x = 0 , y = 0 , relwidth = 1, relheight = 1 )
         
    #FFD300
            self.L1 = Label( self , text = "STUDAL" , font = ("Montserrat Black",55) , bg = "#E29C00" , fg = "black" , anchor = "center").place( x = 380 , y = 80 )
            self.b1 = Button( self , text = "Login" , anchor='center', font = ("Georgia",22) , width = 15 , relief = SUNKEN , command = self.Loginn , bg = "white" , fg = "black").place( x = 150 , y = 350 )
            self.b2 = Button( self , text = "Registration" , anchor = 'center' , font = ("Georgia",22) , width = 15 , relief = SUNKEN , command = self.register , bg = "white" , fg = "black" ).place( x = 650 , y = 350)

except:
    tmsg.showerror("ERROR", "Error Occured !")
    print("Error")

if __name__ == '__main__' :
    
    window = Login()    
    window.front_page()

    window.mainloop()
    