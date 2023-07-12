from tkinter import *
import Login_register


class To_Do_List:

    def TODO(self):

        L = Login_register.Log_in( self.email_val.get() , self.password_val.get() )
        self.x = L.checker()
        Login_register.sh1.cell( row = self.x , column = 10 , value = '' )
        
        def add_item():
            self.Lb1.insert(END,self.entry_val.get()) 
            self.Lb1.place( x = 300 , y = 100 )        
            st = Login_register.sh1.cell(self.x,10 ).value + self.entry_val.get() 
            st = st + '      '
            Login_register.sh1.cell( row = self.x , column = 10 , value = st )
            Login_register.wb.save("Records.xlsx")

        self.f1 = Frame( self , bg = "light pink" )
        self.f1.place( x = 0 , y = 0 , width = 1100 , height = 650 )

        self.bg = PhotoImage( file = "frpg.png")
        self.background_label=Label( self , image = self.bg )
        self.background_label.place( x = 0 , y = 0 , relwidth = 1, relheight = 1 )
        
        self.headinng = Label( self , text = "TO DO LIST" , font = ("Georgia",25) , bg = "#E29C00" , fg = "black" ).place(x=240,y=20)
        
        self.additem = Button( self , text = "ADD ITEM" , anchor = 'e' , font = ("Georgia",15) , width = 12 , relief = SUNKEN , command= add_item).place(x=300,y=300)      
        
        self.Lb1 = Listbox(self)
        self.Lb1.place( x = 300 , y = 100 )
        
        self.entry1 = Label( self , text = "Task :- " , font = ("Georgia",12) , fg = "black" , bg = "white" , padx = 5, relief = SUNKEN).place(x=200,y=350)
        self.entry_val = StringVar()
        self.entry = Entry( self , width = 20 , textvariable = self.entry_val ).place(x=300,y=350)

        self.prev = Button( self , text = "<<Prev" , font = ( "Georgia", 15) , fg = "black" , bg = "white" , padx = 2 , relief = SUNKEN , command = self.user_page).place( x = 25 , y = 50 )
        
    

        
        
