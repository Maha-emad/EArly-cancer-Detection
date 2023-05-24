import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

 
class Login:
    def __init__(self,root):  
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Cancer Detection")
        
        #First Image
        img=Image.open(r"C:\Users\user\Desktop\Early_cancer_detection\my_GUI\cancer1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)



        #Second Image
        img1=Image.open(r"C:\Users\user\Desktop\Early_cancer_detection\my_GUI\cancer4.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)





        #Third Image
        img2=Image.open(r"C:\Users\user\Desktop\Early_cancer_detection\my_GUI\\cancer3.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        #Bg Image
        img3=Image.open(r"cancer_images\pattern5.png")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="Early Cancer Detection" , font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        
        b1_1=Button(bg_img,text="Log in ",command=self.login,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=200, y=300,width =220 ,height=40)


   
    #======================================Function Buttons==========================
        
        
    
    
    

    id_val=""
    pass_val=""
    def open_dr_Home(self): 
        from dr_home import Dr_Home 
        self.root.destroy()
#         self.new_window=Toplevel(self.root)
        self.new_window = tk.Tk()
        self.app=Dr_Home(self.new_window)
        
    def open_admn_Home(self): 
        from admin_home import Admin_Home 
        self.root.destroy()
#         self.new_window=Toplevel(self.root)
        self.new_window = tk.Tk()
        self.app=Admin_Home(self.new_window)    
        
    def login(self):
    
         
        self.login_window = Tk() #creates a new window for loging in
        self.login_window.title("LogIn")  #set title to the window
        self.login_window.geometry("400x250")  #set dimensions to the window
    
        l1 = Label(self.login_window,text="ID: ",font="times 20")
        l1.grid(row=1,column=0)

        l2 = Label(self.login_window,text="Password: ",font="times 20")
        l2.grid(row=2,column=0)

        self.password_text = StringVar()
        self.id_text = StringVar() 
        
        e1 = Entry(self.login_window,textvariable=self.id_text)
        e1.grid(row=1,column=1)

        
        e2 = Entry(self.login_window,textvariable=self.password_text,show='*')
        e2.grid(row=2,column=1)

        
        b_dr = Button(self.login_window,text="As Doctor",width=20,command=self.check_dr)
        b_dr.grid(row=4,column=1)
        
        b_admin = Button(self.login_window,text="As admin",width=20,command=self.check_admn)
        b_admin.grid(row=6,column=1)
        
        
        
        self.login_window.mainloop()
        
    def get_vals(self): 
        Login.id_val = self.id_text.get() 
        Login.pass_val = self.password_text.get() 
        
    def check_dr(self):
        self.get_vals()
        cred = credentials.Certificate('firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json')
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        col = 'doctors' 
        fild_1 = 'id'
        fild_2 = 'password'
        collection_ref = db.collection(col)
        
        print( Login.id_val)
        query = collection_ref.where('id', '==',Login.id_val).where('password', '==',Login.pass_val).limit(1).get()
        if len(query) > 0 : 
           
            self.login_window.destroy() 
            self.open_dr_Home()
#         else :
#             l3 = Label(wn,font="times 20")
#             l3.grid(row=7,column=1)
#             l3.config(text="Doctor not found")
        
    
    def check_admn(self ):
        cred = credentials.Certificate('firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json')
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        
        collection_ref = db.collection('admins')
        query = collection_ref.where('id', '==',id_text).where('password', '==',password_text).limit(1).get()
        if len(query) > 0 : 
            self.login_window.destroy() 
            self.open_admn_Home()
#         else :
#             l3 = Label(wn,font="times 20")
#             l3.grid(row=7,column=1)
#             l3.config(text="Admin not found")
        
        

if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition_System(root)
    root.mainloop()
    
