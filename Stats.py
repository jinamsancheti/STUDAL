# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 23:27:34 2022

@author: jinam
"""

import Login_register
from tkinter import *


def Statistics(self):
    
    self.f1=Frame( self , bg = "light pink" )
    self.f1.place( x = 0 , y = 0 , width = 1100 , height = 650 )

    self.bg = PhotoImage( file = "frpg.png")
    self.background_label=Label( self , image = self.bg )
    self.background_label.place( x = 0 , y = 0 , relwidth = 1, relheight = 1 )

    def put_values():
        if(self.save_val.get() == 1):
            try:
                row1 = self.x
                Login_register.sh1.cell( row = ( row1 ) , column = 6 , value = self.age_val.get() )
                Login_register.sh1.cell( row = ( row1) , column = 7 , value = self.cgpa_val.get() )
                Login_register.sh1.cell( row = ( row1) , column = 8 , value = self.LI_val.get() )
                Login_register.sh1.cell( row = ( row1) , column = 9 , value = self.save_val.get() )
                Login_register.wb.save("Records.xlsx")
                self.user_page()
            except:
                tmsg.showerror("ERROR", "Error Occured !")
                print("Error")

    
    self.headinng = Label( self , text = "STUDENT STATISTICS" , font = ("Montserrat Black",25) , bg = "#E29C00" , fg = "black" ).place(x=240,y=20)
    if(Login_register.sh1.cell(self.x,9).value == 0 ):
    
        self.name = Label( self , text = "NAME :- " , font = ("Georgia",15) , bg = "white" , fg = "black" ).place(x = 200 , y = 110)
        self.name_val = Label( self , text = Login_register.sh1.cell(self.x,3).value , font = ("Georgia",15) , bg = "white" , fg = "black" ).place(x=400,y=110)
    
        self.phno = Label( self , text = "PHONE NO :- " , font = ("Georgia",15) , bg = "white" , fg = "black" ).place(x = 200,y = 160)
        self.phno_val = Label( self , text = Login_register.sh1.cell(self.x,4).value , font = ("Georgia",15) , bg = "white" , fg = "black" ).place(x=400,y= 160 )
    
        self.school = Label( self , text = "UNIIVERSITY :- " , font = ("Georgia",15) , bg = "white" , fg = "black" ).place( x = 200 , y = 210 )
        self.school_val = Label( self , text = Login_register.sh1.cell(self.x,5).value , font = ("Georgia",15) , bg = "white" , fg = "black" ).place( x = 400 , y = 210 )        
    
        self.age1 = Label( self , text = "AGE :- " , font = ("Georgia",12) , fg = "black" , bg = "white" , padx = 5 , relief = SUNKEN ).place( x = 200 , y = 260 )
        self.age_val = IntVar()
        self.age= Entry( self ,  textvariable = self.age_val , width = 20 ).place(x=400,y = 260)
    
        self.cgpa1 = Label( self , text = "CGPA :- " , font = ("Georgia",12) , fg = "black" , bg = "white" , padx = 5 , relief = SUNKEN ).place( x = 200 , y = 310 )
        self.cgpa_val = DoubleVar()
        self.cgpa = Entry( self ,  textvariable = self.cgpa_val , width = 20 ).place(x=400,y = 310)
    
        self.LI1 = Label( self , text = "LinkedIn :- " , font = ("Georgia",12 ) , fg = "black" , bg = "white" , padx = 5 , relief = SUNKEN ).place( x = 200 , y = 360 )
        self.LI_val = StringVar()
        self.LI = Entry( self ,  textvariable = self.LI_val , width = 20 ).place(x=400,y = 360)
        
        self.prev = Button( self , text = "<<Prev" , font = ( "Georgia", 15 ) , fg = "black" , bg = "white" , padx = 2 , relief = SUNKEN , command = self.user_page).place( x = 25 , y = 50 )
    
        self.Submit = Button(self , text="SUBMIT", font=( "Cooper Black", 20 ), fg = "black" , bg = "white" , padx = 2 , relief = SUNKEN , command = put_values ).place(x = 800, y = 400)
        
        self.save_val = IntVar()
        self.save = Checkbutton(text="Save This Data !",font = ("Georgia",12) , fg = "black" , bg = "white" , padx = 5 , relief = SUNKEN , variable = self.save_val)
        self.save.place(x = 200 , y = 420 )
    
        self.Statistics()

    else:

         self.name = Label( self , text = "NAME :- " , font = ("Georgia",15) , bg = "white" , fg = "black" ).place(x=200,y=110)
         self.name_val = Label( self , text = Login_register.sh1.cell(self.x,3).value , font = ("Georgia",15) , bg = "white" , fg = "black" ).place(x=400,y = 110)

         self.phno = Label( self , text = "PHONE NO :- " , font = ("Georgia",15) , bg = "white" , fg = "black" ).place(x=200,y = 160)
         self.phno_val = Label( self , text = Login_register.sh1.cell(self.x,4).value , font = ("Georgia",15) , bg = "white" , fg = "black" ).place(x=400,y= 160 )

         self.school = Label( self , text = "UNIIVERSITY :- " , font = ("Georgia",15) , bg = "white" , fg = "black" ).place( x = 200 , y = 210 )
         self.school_val = Label( self , text = Login_register.sh1.cell(self.x,5).value , font = ("Georgia",15) , bg = "white" , fg = "black" ).place( x = 400 , y = 210 )        

         self.age = Label( self , text = "AGE :- " , font = ("Georgia",15) , bg = "white" , fg = "black" ).place( x = 200 , y = 260 )
         self.age_val = Label( self , text = Login_register.sh1.cell(self.x,6).value , font = ("Georgia",15) , bg = "white" , fg = "black" ).place( x = 400 , y = 260 )
        
         self.cgpa = Label( self , text = "CGPA :- " , font = ("Georgia",15) , bg = "white" , fg = "black" ).place(x = 200,y= 310 )
         self.cgpa_val = Label( self , text = Login_register.sh1.cell(self.x,7).value , font = ("Georgia",15) , bg = "white" , fg = "black" ).place(x = 400 , y = 310)

         self.LinkedIn = Label( self , text = "LinkedIn :- " , font = ("Georgia",15) , bg = "white" , fg = "black" ).place(x = 200 , y = 360)
         self.LinkedIn_val = Label( self , text = Login_register.sh1.cell(self.x,8).value , font = ("Georgia",15) , bg = "white" , fg = "black" ).place(x = 400 , y = 360)

         self.prev = Button( self , text = "<<Prev" , font = ( "Georgia", 15 ) , fg = "black" , bg = "white" , padx = 2 , relief = SUNKEN , command = self.user_page).place( x = 25 , y = 50 )
    
