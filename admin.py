from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import functools 
 
    
    
class Admin:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Admin Data")


        # =============================variables============================
        self.var_old_admn_id=IntVar()
        self.va_dr_id=IntVar()
        self.va_dr_nm=StringVar()
        self.var_dr_mail=StringVar()
        self.var_dr_pass=StringVar()
        
        
        
       
        #First Image
        img=Image.open(r"cancer_images\pattern_4.png")
        img=img.resize((1530,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=130)



        #Bg Image
        img3=Image.open(r"cancer_images\pattern_4.png")
        img3=img3.resize((1530,790),Image.ANTIALIAS) 
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=790)

        title_lbl=Label(bg_img,text="Admin Data" , font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=53)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame 

        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Admin Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=10, y=10, width=760, height=580)

        img_left=Image.open(r"cancer_images\data1.jpg")
        img_left=img_left.resize((720,140),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #old admn data
        dr_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Old Admin", font=("times new roman",12,"bold"))
        dr_frame.place(x=5, y=135, width=720, height=150)
        
        #old admn id
        d_id_label=Label(dr_frame,text="ID:",font=("times new roman",12,"bold"))
        d_id_label.grid(row=1,column = 0,padx=10, sticky=W)

        d_id_entry=ttk.Entry(dr_frame,textvariable=self.var_old_admn_id,width=20,font=("times new roman", 13, "bold"))
        d_id_entry.grid(row=1,column = 1, padx=2, pady=10, sticky=W)

        #nw admin information
        self.admn_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="New Admin Information", font=("times new roman",12,"bold"))
        self.admn_frame.place(x=5, y=250, width=720, height=300)

        #nw admin id
        ad_Id_label=Label(self.admn_frame,text="ID:",font=("times new roman",12,"bold"),bg="white")
        ad_Id_label.grid(row=1,column = 0,padx=10, sticky=W)
        
        drId_entry=ttk.Entry(self.admn_frame,textvariable=self.va_dr_id,width=20,font=("times new roman", 13, "bold"))
        drId_entry.grid(row=1,column = 1, padx=2, pady=10, sticky=W)
        #nw admin name 
        ad_nm_label=Label(self.admn_frame,text="Name:",font=("times new roman",13,"bold"), bg= "white")
        ad_nm_label.grid(row=2,column = 0,padx=10, pady=5, sticky=W)
        
        drnm_entry=ttk.Entry(self.admn_frame,textvariable=self.va_dr_nm,width=20,font=("times new roman", 13, "bold"))
        drnm_entry.grid(row=2,column = 1, padx=10, pady=5, sticky=W)
        

        #dr email 
        dr_mail_label=Label(self.admn_frame,text="Email:",font=("times new roman",13,"bold"), bg = "white")
        dr_mail_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        dr_mail_entry=ttk.Entry(self.admn_frame,textvariable=self.var_dr_mail,width=20,font=("times new roman", 13, "bold"))
        dr_mail_entry.grid(row=3,column = 1, padx=2, pady=5, sticky=W)

        #dr pass
        dr_pass_label=Label(self.admn_frame,text="Password:",font=("times new roman",13,"bold"), bg = "white")
        dr_pass_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        dr_pass_entry=ttk.Entry(self.admn_frame,textvariable=self.var_dr_pass,width=20,font=("times new roman", 13, "bold"))
        dr_pass_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        
        
        old_admn_id =self.var_old_admn_id.get()
        dr_id=self.va_dr_id.get()
        dr_nm=self.va_dr_nm.get()
        dr_mail=self.var_dr_mail.get()
        dr_pass=self.var_dr_pass.get()
        

      
        #buttons frame
        btn_frame=Frame(self.admn_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="Add",width=17,font=("times new roman", 13 , "bold"),bg="black",fg="white" , command=self.add_admin)
        save_btn.grid(row=0,column=0)
       
 
        delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman", 13 , "bold"),bg="black",fg="white" , command = self.delete_admin)
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman", 13 , "bold"),bg="black",fg="white" , command = self.reset_fields)
        reset_btn.grid(row=0,column=3)


       

       
        #go to admin home page 
        home_btn = Button(bg_img,text="Home",width=20 , command = self.open_home)
        home_btn.place(x=10, y=10,width =130 ,height=40) 

        
      
        
        
        #################functions################### 
    def open_home(self):
        from admin_home import Admin_Home
        self.root.destroy()
        wn=Tk()
        obj=Admin_Home(wn)
        wn.mainloop()  
        
    def open_examin(self):
        from examin import Examin
        self.root.destroy()
        wn=Tk()
        obj=Examin(wn)
        wn.mainloop()  
        
        
    def reset_fields(self): 
        self.var_old_admn_id.set("")
        self.va_dr_id.set("")
        self.va_dr_nm.set("")
        self.var_dr_mail.set("")
        self.var_dr_pass.set("")
        
#     query = db.collection('admins').where('old admin -d', '==', 'old_id').limit(1)
#     documents = query.stream()

#     for doc in documents:
#         # Check if 'password' field is equal to '33' and 'id' field is equal to '43'
#         if doc.to_dict().get('password') == '33' and doc.to_dict().get('id') == '43':
#             # Delete the document
#             doc.reference.delete()

    
    def delete_admin(self) :
        
        cred = credentials.Certificate('firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json')
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        # Reference to the 'admin' collection in Firebase
        
        admin_ref = db.collection('admins')
        # Check if the entered old_admin_id exists in the admin table
        query = admin_ref.where('old_admin_id', '==', self.var_old_admn_id.get()).limit(1)
        documents = query.stream()
        for doc in documents:
            if doc.to_dict().get('password') ==  self.var_dr_pass.get() and doc.to_dict().get('id') ==  self.va_dr_id.get():
                    doc.reference.delete() 
                    
                    lbl3=Label(self.admn_frame , text="Admin deleted" ,font=("times new roman",13,"bold"), bg = "white") 
                    lbl3.grid(row=1,column = 2, padx=2, pady=10, sticky=W)
            
            
            
        firebase_admin.delete_app(firebase_admin.get_app())
    def add_admin(self): 
#         old_admin_id=34
        
        print(self.var_dr_mail.get())
        print( self.va_dr_nm.get())
        print(self.va_dr_nm.get())
        
        print(self.var_dr_pass.get())
                
        
        cred = credentials.Certificate('firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json')
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        # Reference to the 'admin' collection in Firebase
        print(self.var_old_admn_id.get())
        admin_ref = db.collection('admins')
        # Check if the entered old_admin_id exists in the admin table
        query = admin_ref.where('old_admin_id', '==', self.var_old_admn_id.get()).get()
       
        if not len(query) > 0:
            print("Old admin not found.")
        else:
            docs = db.collection('admins').where('id', '>', 0).stream()
            max_value = float('-inf')
            for doc in docs:
                doc_data = doc.to_dict()
                print(doc_data)
                if 'id' in doc_data and doc_data['id'] > max_value:
                    max_value = doc_data['id']  
            
            print(max_value)       
            admin_data = {
                    'email': self.var_dr_mail.get(),
                    'id': max_value+1,
                    'name':self.va_dr_nm.get(),
                    'old_admin_id':self.var_old_admn_id.get(),
                    'password': self.var_dr_pass.get()
                }
                

            admin_ref.add(admin_data)
            lbl3=Label(self.admn_frame , text="Admin Id :"+str(max_value+1) ,font=("times new roman",13,"bold"), bg = "white") 
            lbl3.grid(row=1,column = 2, padx=2, pady=10, sticky=W)
            print("Admin added successfully.")


        firebase_admin.delete_app(firebase_admin.get_app())
 
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore

# def delete():
#     # Initialize Firebase Admin SDK
#     cred = credentials.Certificate("path/to/serviceAccountKey.json")  # Replace with the path to your service account key JSON file
#     firebase_admin.initialize_app(cred)

#     # Access the Firestore database
#     db = firestore.client()

#     # Check if a document exists with 'old admin -d' field equal to 'old_id'
#     query = db.collection('admins').where('old admin -d', '==', 'old_id').limit(1)
#     documents = query.stream()

#     for doc in documents:
#         # Check if 'password' field is equal to '33' and 'id' field is equal to '43'
#         if doc.to_dict().get('password') == '33' and doc.to_dict().get('id') == '43':
#             # Delete the document
#             doc.reference.delete()

#     # Cleanup Firebase resources
#     firebase_admin.delete_app(firebase_admin.get_app())

# # Call the delete function
# delete()

# 



 
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()