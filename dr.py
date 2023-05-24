import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import functools 
# from doctor import Doctor  
 
 
# from login_register import Login_Register 
# from patient import Patient
# from page3 import Page3 
# from report import Report


class Dr:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Doctors Data")


        # =============================variables============================
        self.var_admn_id=IntVar()
        self.va_dr_id=IntVar()
        self.var_dr_srch=IntVar()
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

        title_lbl=Label(bg_img,text="Doctor Data" , font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=53)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame 

        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Doctors Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=10, y=10, width=760, height=580)

        img_left=Image.open(r"cancer_images\data1.jpg")
        img_left=img_left.resize((720,140),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        # admn data
        ad_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="admin Information", font=("times new roman",12,"bold"))
        ad_frame.place(x=5, y=135, width=720, height=150)
        
        #admn id
        d_id_label=Label(ad_frame,text="Admin ID:",font=("times new roman",12,"bold"))
        d_id_label.grid(row=1,column = 0,padx=10, sticky=W)

        d_id_entry=ttk.Entry(ad_frame,textvariable=self.var_admn_id,width=20,font=("times new roman", 13, "bold"))
        d_id_entry.grid(row=1,column = 1, padx=2, pady=10, sticky=W)

        #dr information
        self.dr_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="doctor Information", font=("times new roman",12,"bold"))
        self.dr_frame.place(x=5, y=250, width=720, height=300)

        #dr id
        drId_label=Label(self.dr_frame,text="DoctorID:",font=("times new roman",12,"bold"),bg="white")
        drId_label.grid(row=1,column = 0,padx=10, sticky=W)
        
        drId_entry=ttk.Entry(self.dr_frame,textvariable=self.va_dr_id,width=20,font=("times new roman", 13, "bold"))
        drId_entry.grid(row=1,column = 1, padx=2, pady=10, sticky=W)
        #dr name 
        dr_nm_label=Label(self.dr_frame,text="Doctor Name:",font=("times new roman",13,"bold"), bg= "white")
        dr_nm_label.grid(row=2,column = 0,padx=10, pady=5, sticky=W)
        
        drnm_entry=ttk.Entry(self.dr_frame,textvariable=self.va_dr_nm,width=20,font=("times new roman", 13, "bold"))
        drnm_entry.grid(row=2,column = 1, padx=10, pady=5, sticky=W)
        

        #dr email 
        dr_mail_label=Label(self.dr_frame,text="Email:",font=("times new roman",13,"bold"), bg = "white")
        dr_mail_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        dr_mail_entry=ttk.Entry(self.dr_frame,textvariable=self.var_dr_mail,width=20,font=("times new roman", 13, "bold"))
        dr_mail_entry.grid(row=3,column = 1, padx=2, pady=5, sticky=W)

        #dr pass
        dr_pass_label=Label(self.dr_frame,text="Password:",font=("times new roman",13,"bold"), bg = "white")
        dr_pass_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        dr_pass_entry=ttk.Entry(self.dr_frame,textvariable=self.var_dr_pass,width=20,font=("times new roman", 13, "bold"))
        dr_pass_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

      
        #buttons frame
        btn_frame=Frame(self.dr_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="Add",width=17,font=("times new roman", 13 , "bold"),bg="black",fg="white",command=self.add_dr)
        save_btn.grid(row=0,column=0)
        
#         update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman", 13 , "bold"),bg="black",fg="white")
#         update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman", 13 , "bold"),bg="black",fg="white",command=self.delete_dr)
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman", 13 , "bold"),bg="black",fg="white" , command = self.reset_fields)
        reset_btn.grid(row=0,column=3)


       

       
        #go to admin home page 
        home_btn = Button(bg_img,text="Home",width=20 , command = self.open_home)
        home_btn.place(x=10, y=10,width =130 ,height=40) 

        
         #Right label frame 

        self.Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text="Doctors Details", font=("times new roman",12,"bold"))
        self.Right_frame.place(x=780, y=10, width=760, height=580)

        img_right=Image.open(r"cancer_images\data3.jpg")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(self.Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)
       

        # =============Search System==================
        self.Search_frame=LabelFrame(self.Right_frame,bd=2,bg="white",relief=RIDGE,text="Search Bar System", font=("times new roman",12,"bold"))
        self.Search_frame.place(x=5, y=135, width=710, height=70)

        search_label=Label(self.Search_frame,text="Search By ID:",font=("times new roman",15,"bold"), bg = "black",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        
        search_entry=ttk.Entry(self.Search_frame,textvariable=self.var_dr_srch ,width=15,font=("times new roman", 13, "bold"))
        search_entry.grid(row=0,column = 1, padx=2, pady=10, sticky=W)


        search_btn=Button(self.Search_frame,text="Search",width=12,font=("times new roman", 13 , "bold"),bg="black",fg="white", command = self.select_dr)
        search_btn.grid(row=0,column=2,padx=4)

        showAll_btn=Button(self.Search_frame,text="Show All",width=12,font=("times new roman", 13 , "bold"),bg="black",fg="white",command = lambda : self.show_table('doctors'))
        showAll_btn.grid(row=0,column=3,padx=4)


        # ==================table frame===============
        self.table_frame=Frame(self.Right_frame,bd=2,bg="white",relief=RIDGE)
        self.table_frame.place(x=5, y=210, width=710, height=350)

        scroll_x=ttk.Scrollbar(self.table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(self.table_frame,orient=VERTICAL)

        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        
        
        
        
        
        
        
        
        #################functions################### 
    def select_dr(self) : 
        cred = credentials.Certificate('firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json') 
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        
        query = db.collection('doctors').where('id', '==', self.var_dr_srch.get())
        documents = query.stream()
        
        for doc in documents:
            data = doc.to_dict()
            for field, value in data.items():
                label = tk.Label(self.table_frame, text=f"{field}: {value}" ,font=("Arial", 12), width=760  )
                label.pack()
        firebase_admin.delete_app(firebase_admin.get_app())
        
    def show_table(self, coll_name) :
        cred = credentials.Certificate('firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json') 
        firebase_admin.initialize_app(cred)
        db = firestore.client()

    
        collection_ref = db.collection('doctors')
        documents = collection_ref.stream()

        tree = ttk.Treeview(self.table_frame)
   
    # Retrieve the field names from the first document
        first_document = next(documents)
        field_names = list(first_document.to_dict().keys())

    # Set up the columns in the Treeview widget
        tree["columns"] = field_names
        tree.heading("#0", text="Document ID")  # Column for document ID
        tree.column("#0", width=100)
        for field_name in field_names:
            tree.heading(field_name, text=field_name)
            tree.column(field_name, width=100)

    # Insert data rows into the Treeview widget
        for doc in documents:
            data = doc.to_dict()
            document_id = doc.id
            tree.insert("", tk.END, text=document_id, values=[data.get(field_name, "") for field_name in field_names])

    # Pack the Treeview widget
        tree.pack()

        firebase_admin.delete_app(firebase_admin.get_app())

        
    def open_home(self):
        from  admin_home import Admin_Home
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
        self.var_admn_id.set("")
        self.va_dr_id.set("")
        self.va_dr_nm.set("")
        self.var_dr_mail.set("")
        self.var_dr_pass.set("") 
        self.var_dr_srch.set("")
        
    def delete_dr(self) :
        
        cred = credentials.Certificate('firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json')
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        # Reference to the 'admin' collection in Firebase
        
        dr_ref = db.collection('doctors')
        # Check if the entered old_admin_id exists in the admin table
        query = dr_ref.where('id', '==', self.va_dr_id.get())
        documents = query.stream()
        for doc in documents:
            if doc.to_dict().get('password') ==  self.var_dr_pass.get() and doc.to_dict().get('id') ==  self.va_dr_id.get():
                    doc.reference.delete() 
                    
                    lbl3=Label(self.dr_frame , text="Doctor deleted" ,font=("times new roman",13,"bold"), bg = "white") 
                    lbl3.grid(row=1,column = 2, padx=2, pady=10, sticky=W)    
        firebase_admin.delete_app(firebase_admin.get_app())
    def add_dr(self): 
#         old_admin_id=34
        
        cred = credentials.Certificate('firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json')
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        # Reference to the 'admin' collection in Firebase
        
        admin_ref = db.collection('admins')
        # Check if the entered old_admin_id exists in the admin table
        query = admin_ref.where('id', '==', self.var_admn_id.get()).get()
       
        if not len(query) > 0:
            print("admin not found.")
        else:
            dr_ref = db.collection('doctors')
            docs = db.collection('doctors').where('id', '>', 0).stream()
            max_value = float('-inf')
            for doc in docs:
                doc_data = doc.to_dict()
                print(doc_data)
                if 'id' in doc_data and doc_data['id'] > max_value:
                    max_value = doc_data['id']  
           
            print(max_value)       
            dc_data = {
                    'email': self.var_dr_mail.get(),
                    'id': max_value+1,
                    'name':self.va_dr_nm.get(),
                    'admin_id':self.var_admn_id.get(),
                    'password': self.var_dr_pass.get()
                }
                

            dr_ref.add(dc_data)
            lbl3=Label(self.dr_frame , text="Doctor Id :"+str(max_value+1) ,font=("times new roman",13,"bold"), bg = "white") 
            lbl3.grid(row=1,column = 2, padx=2, pady=10, sticky=W)
            print("Doctor added successfully.")

     
        
        firebase_admin.delete_app(firebase_admin.get_app())
       
         # ==================table frame===============
#         table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
#         table_frame.place(x=5, y=210, width=710, height=350)

#         scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
#         scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

#         self.student_table=ttk.Treeview(table_frame,column=("Name" , "ID" , "Age" , "Phone" , "gender" , "Cancer type"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

#         scroll_x.pack(side=BOTTOM,fill=X)
#         scroll_y.pack(side=RIGHT,fill=Y)

#         scroll_x.config(command=self.student_table.xview)
#         scroll_y.config(command=self.student_table.yview)


#         self.student_table.heading("Name", text="name")
#         self.student_table.heading("ID", text="ID")
#         self.student_table.heading("Age", text="Age")
#         self.student_table.heading("Phone", text="Phone")
#         self.student_table.heading("Gender", text="Gender")
#         self.student_table.heading("Cancer Level", text="Cancer type")
#         self.student_table["show"]="headings"

       
#         self.student_table.column("name",width=100)
#         self.student_table.column("ID",width=100)
#         self.student_table.column("Age",width=100)
#         self.student_table.column("Phone",width=100)
#         self.student_table.column("Gender",width=100)
#         self.student_table.column("Cancer type",width=100)
        

#         self.student_table.pack(fill=BOTH,expand=1)
        
#         self.student_table.bind("<ButtonRelease>",self.get_cursor)
#         self.fetch_data()

    # ==========================function decration==============================
#     def add_data(self):
#         if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
#             messagebox.showerror("Error","All Fileds are required",parent=self.root)
#         else:
#             try:
#                 conn=mysql.connector.connect(host="localhost",username="root",password="Abhi@99315",database="face_recognizer")
#                 my_cursor=conn.cursor()
#                 my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
#                                                                                                            self.var_dep.get(),
#                                                                                                            self.var_course.get(),
#                                                                                                            self.var_year.get(),
#                                                                                                            self.var_semester.get(),           
#                                                                                                            self.va_std_id.get(),
#                                                                                                            self.var_std_name.get(),
#                                                                                                            self.var_div.get(),
#                                                                                                            self.var_roll.get(),
#                                                                                                            self.var_gender.get(),
#                                                                                                            self.var_dob.get(),
#                                                                                                            self.var_email.get(),
#                                                                                                            self.var_phone.get(),
#                                                                                                            self.var_address.get(),
#                                                                                                            self.var_teacher.get(),
#                                                                                                            self.var_radio1.get()
            
#                                                                                                      ))    
#                 conn.commit()
#                 self.fetch_data()
#                 conn.close()
#                 messagebox.showinfo("Success","Stduent details has been added Successfully", parent=self.root)
#             except Exception as es:
#                 messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

#     # =================================fetch data ===============================================
#     def fetch_data(self):
#         conn=mysql.connector.connect(host="localhost",username="root",password="Abhi@99315",database="face_recognizer")
#         my_cursor=conn.cursor()
#         my_cursor.execute("select * from student")
#         data=my_cursor.fetchall()

#         if len(data)!=0:
#             self.student_table.delete(*self.student_table.get_children())
#             for i in data:
#                 self.student_table.insert("",END,values=i)
#             conn.commit()
#         conn.close()  

#     # ================================get cursor ===================================
#     def get_cursor(self,event=""):
#         cursor_focus=self.student_table.focus()
#         content=self.student_table.item(cursor_focus)
#         data=content["values"]

#         self.var_dep.set(data[0]),
#         self.var_course.set(data[1]),
#         self.var_year.set(data[2]),
#         self.var_semester.set(data[3]),
#         self.va_std_id.set(data[4]),
#         self.var_std_name.set(data[5]),
#         self.var_div.set(data[6]),
#         self.var_roll.set(data[7]),
#         self.var_gender.set(data[8]),
#         self.var_dob.set(data[9]),
#         self.var_email.set(data[10]),
#         self.var_phone.set(data[11]),
#         self.var_address.set(data[12]),
#         self.var_teacher.set(data[13]),
#         self.var_radio1.set(data[14])

#     # =============================update function=====================================
#     def update_data(self):
#         if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
#             messagebox.showerror("Error","All Fileds are required",parent=self.root)
#         else:
#             try:
#                 Update=messagebox.askyesno("Update","Do you want to update this student dtails",parent=self.root)
#                 if Update>0:
#                    conn=mysql.connector.connect(host="localhost",username="root",password="Abhi@99315",database="face_recognizer")
#                    my_cursor=conn.cursor()
#                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Email=%s,Gender=%s,Dob=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                      
#                                                                                                                                                                                 self.var_dep.get(),
#                                                                                                                                                                                 self.var_course.get(),
#                                                                                                                                                                                 self.var_year.get(),
#                                                                                                                                                                                 self.var_semester.get(),
#                                                                                                                                                                                 self.var_std_name.get(),
#                                                                                                                                                                                 self.var_div.get(),
#                                                                                                                                                                                 self.var_roll.get(),
#                                                                                                                                                                                 self.var_gender.get(),
#                                                                                                                                                                                 self.var_dob.get(),
#                                                                                                                                                                                 self.var_email.get(),
#                                                                                                                                                                                 self.var_phone.get(),
#                                                                                                                                                                                 self.var_address.get(),
#                                                                                                                                                                                 self.var_teacher.get(),
#                                                                                                                                                                                 self.var_radio1.get(),
#                                                                                                                                                                                 self.va_std_id.get()
#                                                                                                                                                                             ))      
#                 else :
#                     if not Update:
#                         return
#                 messagebox.showinfo("Success","Student details successfully updated completed",parent=self.root)
#                 conn.commit()
#                 self.fetch_data()
#                 conn.close() 
#             except Exception as es:
#                 messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

#     # delete function
#     def delete_data(self):
#         if self.va_std_id.get()=="":
#             messagebox.showerror("Error","Student id must be required ", parent=self.root)
#         else:
#             try:
#                 delete=messagebox.askyesno("Student Delete Page", "Do you want to delete this student",parent=self.root)
#                 if delete>0:
#                     conn=mysql.connector.connect(host="localhost",username="root",password="Abhi@99315",database="face_recognizer")
#                     my_cursor=conn.cursor()
#                     sql="delete from student where Student_id=%s"
#                     val=(self.va_std_id.get(),)
#                     my_cursor.execute(sql,val)
#                 else:
#                     if not delete:
#                         return

#                 conn.commit()
#                 self.fetch_data()
#                 conn.close()
#                 messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)        
#             except Exception as es:
#                 messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
#     #reset
#     def reset_data(self):
#         self.var_dep.set("Select Department")
#         self.var_course.set("Select Course")
#         self.var_year.set("Select Year")
#         self.var_semester.set("Select Semester")
#         self.va_std_id.set("")
#         self.var_std_name.set("")
#         self.var_div.set("Select Division")
#         self.var_roll.set("")
#         self.var_gender.set("Male")
#         self.var_dob.set("")
#         self.var_email.set("")
#         self.var_phone.set("")
#         self.var_address.set("")
#         self.var_teacher.set("")
#         self.var_radio1.set("")
        
#     # ============================== Genrate data et take photo sample ====================================     
#     def generate_dataset(self):
#         if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
#             messagebox.showerror("Error","All Fileds are required",parent=self.root)
#         else:
#             try:
#                 conn=mysql.connector.connect(host="localhost",username="root",password="Abhi@99315",database="face_recognizer")
#                 my_cursor=conn.cursor()
#                 my_cursor.execute("select * from student")
#                 myresult=my_cursor.fetchall()
#                 id= 0
#                 for x in myresult:
#                     id+=1
#                 my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                      
#                                                                                                                                                                                 self.var_dep.get(),
#                                                                                                                                                                                 self.var_course.get(),
#                                                                                                                                                                                 self.var_year.get(),
#                                                                                                                                                                                 self.var_semester.get(),
#                                                                                                                                                                                 self.var_std_name.get(),
#                                                                                                                                                                                 self.var_div.get(),
#                                                                                                                                                                                 self.var_roll.get(),
#                                                                                                                                                                                 self.var_gender.get(),
#                                                                                                                                                                                 self.var_dob.get(),
#                                                                                                                                                                                 self.var_email.get(),
#                                                                                                                                                                                 self.var_phone.get(),
#                                                                                                                                                                                 self.var_address.get(),
#                                                                                                                                                                                 self.var_teacher.get(),
#                                                                                                                                                                                 self.var_radio1.get(),
#                                                                                                                                                                                 self.va_std_id.get()==id+1
#                                                                                                                                                                             ))
#                 conn.commit()
#                 self.fetch_data()
#                 self.reset_data()
#                 conn.close()  
                 
#                 # ========== Load predifiend data on face frontals  from open cv ==============

#                 face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#                 def face_cropped(img):
#                     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#                     faces=face_classifier.detectMultiScale(gray,1.3,5)
#                     #scalling factor=1.3
#                     #Minimum Neighbor=5
                    
#                     for (x,y,w,h) in faces:
#                         face_cropped=img[y:y+h,x:x+w]
#                         return face_cropped
                          
#                 cap=cv2.VideoCapture(0)
#                 img_id=0
#                 while True:
#                     ret,my_frame=cap.read()
#                     if face_cropped(my_frame) is not None:
#                         img_id+=1
#                         face=cv2.resize(face_cropped(my_frame),(450,450))
#                         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
#                         file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
#                         cv2.imwrite(file_name_path,face)
#                         cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
#                         cv2.imshow("Cropped Face",face)

#                     if cv2.waitKey(1)==13 or int(img_id)==100:
#                         break
#                 cap.release()
#                 cv2.destroyAllWindows()
#                 messagebox.showinfo("Result","Generating data sets completed!!!!")        
#             except Exception as es:
#                 messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)








 
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()