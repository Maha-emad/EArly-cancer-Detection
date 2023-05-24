import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog 
import mysql
import sqlite3
# from doctor import Doctor  
# from examin import Examin 
 
# from login_register import Login_Register 
# from patient import Patient
# from page3 import Page3 
# from report import Report


mydata=[]
class Admn_acc:
    
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Admin Settings")
        
        


       
          # Create a label to display the uploaded image
        

    
        

#         # ====================variables===============
        self.var_dr_id=StringVar()
        self.var_dr_nm=StringVar()
        self.var_emle=StringVar()
   
        self.var_old_pass=StringVar()
        self.var_nw_pass=StringVar()
        self.var_cnf_pass=StringVar()
        

#         First Image
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

      
       
        
        #left label frame 

        Left_frame=LabelFrame(bg_img,bd=2,relief=RIDGE,text="Admin Account", font=("times new roman",12,"bold"))
        Left_frame.place(x=10, y=10, width=760, height=580)

        img_left=Image.open(r"cancer_images\dr3).jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(Left_frame,relief=RIDGE,bd=2,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)

        #id
        drId_label=Label(left_inside_frame,text="AdminId:",font=("times new roman",12,"bold"),bg="white")
        drId_label.grid(row=0,column = 0,padx=10,pady=5, sticky=W)
        
        drId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_dr_id,font=("times new roman", 13, "bold"))
        drId_entry.grid(row=0,column=1,padx=10,pady=5, sticky=W)
        
        
         # name 
        drnameLabel=Label(left_inside_frame,text="Name:",bg="white",font="comicsansns 11 bold")
        drnameLabel.grid(row=1,column=0)

        drname_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_dr_nm,font="comicsansns 11 bold")
        drname_entry.grid(row=1,column=1,pady=8)
        
        
         # email
        emlLabel=Label(left_inside_frame,text="Email:",bg="white",font="comicsansns 11 bold")
        emlLabel.grid(row=2,column=0)

        eml_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_emle,font="comicsansns 11 bold")
        eml_entry.grid(row=2,column=1,pady=8)



        # Old pass 
        old_pass_Label=Label(left_inside_frame,text="Old Password:",bg="white",font="comicsansns 11 bold")
        old_pass_Label.grid(row=0,column=2,padx=4,pady=8)


        oldpass_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_old_pass,font="comicsansns 11 bold")
        oldpass_entry.grid(row=0,column=3,pady=8)
       
       
        # new pass
        nw_pass_label=Label(left_inside_frame,text="New Password:",bg="white",font="comicsansns 11 bold")
        nw_pass_label.grid(row=1,column=2)

        nw_pass_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_nw_pass,font="comicsansns 11 bold")
        nw_pass_entry.grid(row=1,column=3,pady=8)
        
        
         # conf pass
        cnf_pass_Label=Label(left_inside_frame,text="Confirm Password:",bg="white",font="comicsansns 11 bold")
        cnf_pass_Label.grid(row=2,column=2)

        cnf_pass_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_cnf_pass,font="comicsansns 11 bold")
        cnf_pass_entry.grid(row=2,column=3,pady=8)


       


       
    
    #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        
        update_btn=Button(btn_frame,text="Update",width=23,font=("times new roman", 13 , "bold"),bg="black",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=23,font=("times new roman", 13 , "bold"),bg="black",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=23,font=("times new roman", 13 , "bold"),bg="black",fg="white" , command = self.reset_fields)
        reset_btn.grid(row=0,column=3)


       
        
        home_btn = Button(bg_img,text="Home",width=20 , command = self.open_home)
        home_btn.place(x=10, y=10,width =130 ,height=40) 
        


        

 
       

       

   
      
        
        
        ##############functions########## 
    def open_home(self):
        from home import Home
        self.root.destroy()
        wn=Tk()
        obj=Home(wn)
        wn.mainloop() 
        
        
    def reset_fields(self): 
        self.var_dr_id.set("")
        self.var_dr_nm.set("")
        self.var_old_pass.set("")
        self.var_nw_pass.set("")
        self.var_cnf_pass.set("") 
        self.var_emle.set("")

        
      

        
        
        
        


#         # =========================scroll bar table================================
#         scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
#         scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

#         self.AttendaceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

#         scroll_x.pack(side=BOTTOM,fill=X)
#         scroll_y.pack(side=RIGHT,fill=Y)

#         scroll_x.config(command=self.AttendaceReportTable.xview)
#         scroll_y.config(command=self.AttendaceReportTable.yview)

#         self.AttendaceReportTable.heading("id",text="Attendence ID")
#         self.AttendaceReportTable.heading("roll",text="Roll")
#         self.AttendaceReportTable.heading("name",text="Name")
#         self.AttendaceReportTable.heading("department",text="Department")
#         self.AttendaceReportTable.heading("time",text="Time")
#         self.AttendaceReportTable.heading("date",text="Date")
#         self.AttendaceReportTable.heading("attendance",text="Attendance")

#         self.AttendaceReportTable["show"]="headings"

#         self.AttendaceReportTable.column("id",width=100)
#         self.AttendaceReportTable.column("roll",width=100)
#         self.AttendaceReportTable.column("name",width=100)
#         self.AttendaceReportTable.column("department",width=100)
#         self.AttendaceReportTable.column("time",width=100)
#         self.AttendaceReportTable.column("date",width=100)
#         self.AttendaceReportTable.column("attendance",width=100)
       
#         self.AttendaceReportTable.pack(fill=BOTH,expand=1)

#         self.AttendaceReportTable.bind("<ButtonRelease>",self.get_cursor)


#    # ================================= fetch data=======================

#     def fetchData(self,rows):
#         self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
#         for i in rows:
#            self.AttendaceReportTable.insert("",END,values=i)
    
    
    
#     # import csv
#     def importCsv(self):  
#         global mydata
#         mydata.clear()
#         fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
#         with open(fln) as myfile:
#           csvread=csv.reader(myfile,delimiter=",")
#           for i in csvread:
#             mydata.append(i)
#         self.fetchData(mydata) 
    
#     # export csv
#     def exportCsv(self):
#       try:
#         if len(mydata)<1:
#           messagebox.showerror("No Data", "No Data found to export",parent=self.root)
#           return Fasle
#         fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
#         with open(fln,mode="w",newline="") as myfile:
#           exp_write=csv.writer(myfile,delimeter=",")
#           for i in mydata:
#             exp_write.writerow(i)
#           messagebox.showinfo("Data Export", "Your data exported to " + os.path.basename(fln)+"successfully")
#       except Exception as es :
#                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
            
#     def get_cursor(self,event=""):
#       cursor_row=self.AttendaceReportTable.focus()
#       content=self.AttendaceReportTable.item(cursor_row)
#       rows=content['values']
#       self.var_atten_id.set(rows[0])
#       self.var_atten_roll.set(rows[1])
#       self.var_atten_name.set(rows[2])
#       self.var_atten_dep.set(rows[3])
#       self.var_atten_time.set(rows[4])
#       self.var_atten_date.set(rows[5])
#       self.var_atten_attendance.set(rows[6])
        
#     def reset_data(self):
#       self.var_atten_id.set("")
#       self.var_atten_roll.set("")
#       self.var_atten_name.set("")
#       self.var_atten_dep.set("")
#       self.var_atten_time.set("")
#       self.var_atten_date.set("")
#       self.var_atten_attendance.set("")

  

 


if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()