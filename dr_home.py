from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
# from doctor import Doctor   
# from home import Home 
 

# from page3 import Page3 
# from report import Report


class Dr_Home:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Cancer Detection")


        # =============================variables============================
        
        

        #Bg Image
        img3=Image.open(r"cancer_images\pattern5.png")
        img3=img3.resize((1530,790),Image.ANTIALIAS) 
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(width=1530,height=790)

       
      
      

        add_pt_btn=Button(bg_img,text="Add Patient",width=17,font=("times new roman", 13 , "bold"),bg="black",fg="white" , command=self.open_pt)
        add_pt_btn.place(x=200, y=200,width =220 ,height=40)
        
        ex_btn=Button(bg_img,text="Examin Biopsy",width=17,font=("times new roman", 13 , "bold"),bg="black",fg="white" , command=self.open_ex)
        ex_btn.place(x=200, y=300,width =220 ,height=40)

        acc_btn=Button(bg_img,text="Account Settings",width=17,font=("times new roman", 13 , "bold"),bg="black",fg="white" , command=self.open_dr)
        acc_btn.place(x=200, y=400,width =220 ,height=40)

        logout_btn=Button(bg_img,text="Log Out",width=17,font=("times new roman", 13 , "bold"),bg="black",fg="white", command = self.open_lg_rg)
        logout_btn.place(x=200, y=600,width =220 ,height=40) 
        
        
        
        ################functions######################################
        
    def open_lg_rg(self):
#         self.new_window=Toplevel(self.root) 
        from login import Login
        self.root.destroy()
        wn=Tk()
        obj=Login(wn)
        wn.mainloop() 
        
        
    def open_dr(self):
        from dr import Dr
        self.root.destroy()
        wn=Tk()
        obj=Dr(wn) 
        wn.mainloop()  
        
    def open_pt(self):
        from patient import Patient
        self.root.destroy()
        wn=Tk()
        obj=Patient(wn)
        wn.mainloop()   
        
    def open_ex(self):
        from examin import Examin
        self.root.destroy()
        wn=Tk()
        obj=Examin(wn)
        wn.mainloop()  
        
        
   


 
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()