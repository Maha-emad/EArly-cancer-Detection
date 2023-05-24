import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from tkinter import messagebox
import cv2 
from tkinter import filedialog 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import functools 
import json
from roboflow import Roboflow 
from PIL import ImageTk, Image, ImageDraw

# from doctor import Doctor  
# from examin import Examin 
# from home import Home 
# from login_register import Login_Register 
# from patient import Patient
# from page3 import Page3 
# from report import Report

class Examin:
    
    ex_p_id_txt_val ="" 
    pre_set=set()
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Examin Data")
        
        #Bg Image
        img3=Image.open(r"cancer_images\pattern5.png")
        img3=img3.resize((1530,790),Image.ANTIALIAS) 
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(width=1530,height=790)

        ex_p_nm_lbl = Label(bg_img,text="Patient Name: ",font="times 20")
        ex_p_nm_lbl.place(x=100, y=100,width =220 ,height=40)
        
        
        self.ex_p_nm_txt = StringVar()
        ex_p_nm_entry = Entry(bg_img,textvariable=self.ex_p_nm_txt)
        ex_p_nm_entry.place(x=300, y=100,width =220 ,height=40)
        

        ex_p_id_lbl = Label(bg_img,text="Patient ID: ",font="times 20")
        ex_p_id_lbl.place(x=100, y=200,width =220 ,height=40)
        
        
        self.ex_p_id_txt = StringVar()
        ex_p_id_entry = Entry(bg_img,textvariable=self.ex_p_id_txt)
        ex_p_id_entry.place(x=300, y=200,width =220 ,height=40)
        
        
#         Examin_btn = Button(bg_img,text="Examin",width=20 , command = self.predict_image)
#         Examin_btn.place(x=200, y=300,width =220 ,height=40) 
        
        
        shw_rprt_btn = Button(bg_img,text="Show Report",width=20 , command = self.open_report)
        shw_rprt_btn.place(x=200, y=300,width =220 ,height=40)  
        
        
        
        home_btn = Button(bg_img,text="Home",width=20 , command = self.open_home)
        home_btn.place(x=10, y=10,width =130 ,height=40) 
        
        
        #Right label frame 
        
    

        Right_frame=LabelFrame(bg_img,bd=2,relief=RIDGE,bg="white",text="input Biopsy ", font=("times new roman",12,"bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)
        
        browse=Button(Right_frame,text="Upload Image",width=17,font=("times new roman", 13 , "bold"),bg="black",fg="white", command=lambda:self.browse_file(Right_frame))
        browse.pack()
        
       
        
        ####################functions####################### 
    def browse_file(self , frame ):
        image_path =filedialog.askopenfilename()
        self.predict_image(image_path,frame) 
        img =Image.open(image_path)
        if img:
            img_w = 620 
            img_h = 480                 
            img = img.resize((img_w, img_h) ,Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img) 
            label = tk.Label(frame,width=img_w,height=img_h)
            label.image = photo
            label.configure(image=photo)   
            label.pack()
                
            
    def predict_image(self , image_path , frame):
        rf = Roboflow(api_key="hLs680EYHK4wY0wJ0dxQ")
        project = rf.workspace().project("leukemia-cancer-detection")
        model = project.version(1).model

        prediction = model.predict(image_path, confidence=50, overlap=30).json()
  
        print(prediction)
        if prediction and "predictions" in prediction:
            predictions = prediction["predictions"]
            if len(predictions) > 0:
         
                x = predictions[0]["x"]
                y = predictions[0]["y"]
                width = predictions[0]["width"]
                height = predictions[0]["height"]
                
                image = Image.open(image_path)
                draw = ImageDraw.Draw(image)
                draw.rectangle([(x, y), (x + width, y + height)], outline="red", width=2)
            
                image = image.resize((300, 300)) 
                image = ImageTk.PhotoImage(image)
                img_w = 620 
                img_h = 480   
                label = tk.Label(frame,width=img_w,height=img_h)
                label.image = image
                label.configure(image=image)   
                label.pack()
                
                self.subset=set() 
                for prediction in predictions:
                    class_value = prediction["class"]
                    self.subset.add(class_value)
                    print(self.subset)   
                    self.get_prediction_set()
                else:
                    print("No predictions found.")
        else:
             print("Unable to get predictions.")        
        
              
    
    def get_value(self):
        Examin.ex_p_id_txt_val = self.ex_p_id_txt.get()
        print("hello:", Examin.ex_p_id_txt_val)
        
    def get_prediction_set(self) : 
        Examin.pre_set = self.subset     
     
    def open_report(self):
        from report import Report
        self.get_value()
        self.new_window=Toplevel(self.root)  
        self.app=Report(self.new_window)
             
   
    def open_home(self):
        from dr_home import Dr_Home
        self.root.destroy()
        wn=Tk()
        obj=Dr_Home(wn)
        wn.mainloop()  
        
      
 
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()