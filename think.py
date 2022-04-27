import tkinter as tk
from tkinter import ttk

Large_font = ('Helvatica', 20)

def Quit():
    import sys; sys.exit()
    return(quit);

class simpleApp(tk.Tk):

    def __init__(self,*args,**kwargs):
       super(simpleApp,self).__init__()
       #tk.Tk.iconbitmap(self, default='new.bmp')

       container = tk.Frame()
       container.pack(side='top',fill='both',expand=True)
       container.grid_rowconfigure(0, weight=1)
       container.grid_columnconfigure(0, weight=1)

       self.frame = {}
       for F in (startpage, enter_pin, enter_new_pin, enter, quick_teller,
                   enter_amount, widthdraw, saving_current, processing):
           frame = F(container, self)
           self.frame[F] = frame
           frame.grid(row=0,column=0,sticky='nsew')

       self.show_frame(startpage)
       
    def show_frame(self,page_name):
        frame = self.frame[page_name]
        frame.tkraise()
           

class startpage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        lbl = tk.Label(self,text='WELCOME TO UBA ONLINE SERVICE',font=200,
                         bg='red',fg='white',width=50)
        lbl.pack(side='top')

        btn = tk.Button(self,text='Enter pin',bg='red',fg='white',bd=7,width=15,
                        font=30,command=lambda: controller.show_frame(enter_pin))
        btn.place(x=1117,y=200)

        btn2 = tk.Button(self,text='Enter new pin',bg='red',fg='white',bd=7,width=15,
                        font=30,command=lambda: controller.show_frame(enter_new_pin))
        btn2.place(x=1117,y=500)
        #startpage.configure(background='red')

class enter_pin(tk.Frame):   

    def __init__(self,parent,controller):
        
        tk.Frame.__init__(self,parent)
        msg = tk.Message(self,text='''BEWARE OF BEING SCAMMED, PLEASE PROTECT YOUR PIN!!!
PLEASE ENSURE THAT YOU ENTER YOUR FOUR(4) DIGITS PIN CORRECTLY ''',
                         font=200,width=400,bg='red',fg='white')
        msg.place(x=0,y=280)

        pin = tk.StringVar()
        Entry = tk.Entry(self,textvariable=pin,bg='red',fg='white',bd=7,font=30)
        Entry.place(x=600,y=400)

        btn1 = tk.Button(self,text='Enter',bg='red',fg='white',bd=7,width=15,
                       font=30,command=lambda: controller.show_frame(enter))
        btn1.place(x=1117,y=200)

##        btn = tk.Buttton(self,text='Continue',bg='red',fg='white',bd=7,width=15,
##                         font=30,command=check_pin)
##        btn.place(x=1117,y=400)
##
##        Pin = pin.get()
##        if Pin == '2689': 
##                    else:
##            lbl = tk.Label(self,text='Your PIN is incoorrect',width=20,bg='red',
##                           font=30,fg='white')
##            lbl.place(x=600,y=600)
##
##       
##
       
    
  #  def check_pin():
        
        
            

class enter_new_pin(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        lbl1 = tk.Label(self,text='pagetwo',font=Large_font)
        lbl1.pack(pady=10,padx=10)

        btn1 = tk.Button(self,text='Back to Home',
                        command=lambda: controller.show_frame(startpage))
        btn1.pack()

class enter(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        btn3 = tk.Button(self,text='Quick Teller',bg='red',fg='white',bd=7,width=15,
                        font=30,command=lambda: controller.show_frame(quick_teller))
        btn3.place(x=1117,y=170)

        btn4 = tk.Button(self,text='Widthdraw',bg='red',fg='white',bd=7,width=15,
                        font=30,command=lambda: controller.show_frame(saving_current))
        btn4.place(x=1117,y=350)

        btn5 = tk.Button(self,text='Deposite',bg='red',fg='white',bd=7,width=15,
                        font=30,command=lambda: controller.show_frame(startpage))
        btn5.place(x=1117,y=540)

        btn6 = tk.Button(self,text='Transfer',bg='red',fg='white',bd=7,width=15,
                        font=30,command=lambda: controller.show_frame(startpage))
        btn6.place(x=0,y=170)

        btn7 = tk.Button(self,text='Enquiries',bg='red',fg='white',bd=7,width=15,
                        font=30,command=lambda: controller.show_frame(startpage))
        btn7.place(x=0,y=350)

        btn8 = tk.Button(self,text='Enquiries',bg='red',fg='white',bd=7,width=15,
                        font=30,command=lambda: controller.show_frame(startpage))
        btn8.place(x=0,y=540)

##app1 = enter()
##app1.configure(background='red')
        
class quick_teller(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        lbl1 = tk.Label(self,text='pagetwo',font=Large_font)
        lbl1.pack(pady=10,padx=10)

        btn1 = ttk.Button(self,text='Back to Home',
                        command=lambda: controller.show_frame(startpage))
        btn1.pack()

class saving_current(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        lbl1 = tk.Label(self,text='SELECT YOUR ACCOUNT',font=100,bg='red'
                        ,fg='white',width=50)
        lbl1.pack(side='top')

        btn1 = tk.Button(self,text='SAVINGS',bg='red',fg='white',bd=7,width=15,
                        font=30,command=lambda: controller.show_frame(widthdraw))
        btn1.place(x=1117,y=170)

        btn1 = tk.Button(self,text='CURRENT',bg='red',fg='white',bd=7,width=15,
                        font=30,command=lambda: controller.show_frame(widthdraw))
        btn1.place(x=1117,y=540)
        
class widthdraw(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        lbl1 = tk.Label(self,text='PLEASE SELECT THE AMOUNT YOU WANT TO WIDTHDRAW',
                        font=50,bg='red',fg='white',bd=8)
        lbl1.pack(pady=10,padx=10)

        btn3 = tk.Button(self,text='N 20,000',bg='red',fg='white',bd=7,width=15,
                        font=30,command=lambda: controller.show_frame(processing))
        btn3.place(x=1117,y=170)

        btn4 = tk.Button(self,text='N10,000',bg='red',fg='white',bd=7,width=15,
                        font=30,command=lambda: controller.show_frame(processing))
        btn4.place(x=1117,y=350)

        btn5 = tk.Button(self,text='OTHERS',bg='red',fg='white',bd=7,width=15,
                        font=30,command=lambda: controller.show_frame(enter_amount))
        btn5.place(x=1117,y=540)

        btn6 = tk.Button(self,text='N1000',bg='red',fg='white',bd=7,width=15,
                        font=30,command=lambda: controller.show_frame(processing))
        btn6.place(x=0,y=170)

        btn7 = tk.Button(self,text='N5000',bg='red',fg='white',bd=7,width=15,
                        font=30,command=lambda: controller.show_frame(processing))
        btn7.place(x=0,y=350)

        btn8 = tk.Button(self,text='N500',bg='red',fg='white',bd=7,width=15,
                        font=30,command=lambda: controller.show_frame(processing))
        btn8.place(x=0,y=540)


class processing(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        lbl1 = tk.Label(self,text='PLEASE WAIT WHILE YOUR TRANSACTION IS BEING PROCESSED',
                        bg='red',fg='white',font=100)
        lbl1.pack(side='top',pady=10,padx=10)

        btn1 = tk.Button(self,text='WIDTHDRAW',bg='red',fg='white',bd=7,width=15,font=30,
                        command= lambda: controller.show_frame(enter))
        btn1.place(x=1117,y=350)

        btn1 = tk.Button(self,text='END',bg='red',fg='white',bd=7,width=15,font=30,
                        command=Quit) #lambda: controller.show_frame(startpage))
        btn1.place(x=1117,y=540)

class enter_amount(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        lbl1 = tk.Label(self,text='PLEASE ENTER AMOUNT',font=200,
                        bg='red',fg='white')
        lbl1.pack(side='top')

        btn1 = tk.Button(self,text='ENTER',bg='red',fg='white',bd=7,width=15,font=30,
                        command= lambda: controller.show_frame(processing))
        btn1.place(x=1117,y=350)

        E = tk.Entry(self,bg='red',fg='white',bd=7,width=25,font=150)
        E.place(x=500,y=200)


##root = enter_amount()
##root.configure(background='red')
app = simpleApp()
app.title('Application')
app.configure(background='red')
#app.resizable(1280,800)
app.maxsize(1280,800)
app.minsize(1280,800)
app.mainloop()
    







