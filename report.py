import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import functools 
import cv2 
# from doctor import Doctor  
from examin import Examin 
# from home import Home 
# from login_register import Login_Register 
# from patient import Patient
# from page3 import Page3 
# from report import Report


class Report:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Report Page")

        print("helo : " , Examin.ex_p_id_txt_val)
        # Right label frame 
           
        Report_frame=LabelFrame(self.root,bd=2,relief=RIDGE,bg="white",text="Report", font=("times new roman",12,"bold"))
        Report_frame.place( width=1530,height=790)
        
        p_frame=LabelFrame(Report_frame,bd=2,relief=RIDGE,text="Patient Information", font=("times new roman",12,"bold") , bg='#E9D3FF')
        p_frame.place(x=5, y=30, width=1500, height=100)
        
        
        
        rp_frame=LabelFrame(Report_frame,bd=2,relief=RIDGE,text="Examination Report", font=("times new roman",12,"bold"), bg='#E9D3FF')
        rp_frame.place(x=5, y=180 , width=1500, height=530)
        
        
        sv_btn=Button(Report_frame,text="Save",width=17,font=("times new roman", 13 , "bold"),bg="black",fg="white")
        sv_btn.place(x=600 , y= 700 , width =130 ,height=40)
        
          
            
     
        self.p_name ="" 
        self.p_id=""
        self.p_phone=""
        self.p_age =""
        self.p_gender="" 
        self.dr_id=""
        
        
        #get patient data from db
        cred = credentials.Certificate('firebase\cancerdetection-8f9e0-firebase-adminsdk-iqsdf-23750ab0b9.json')
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        # Reference to the 'admin' collection in Firebase
        
        p_ref = db.collection('patients')
        # Check if the patient exists in the patients table
        self.id_val = Examin.ex_p_id_txt_val
        print(self.id_val)
        p_docs = p_ref.where('id', '==', self.id_val).limit(1).get()
        
        self.found = 0 
        
        if  len(p_docs) > 0 : 
            p_doc=p_docs[0]
            print('found')
            self.found = 1
            p_data = p_doc.to_dict()
            print(p_data)
            self.p_name = p_data['name']
            print(self.p_name )
            self.p_id = p_data['id']
            print(self.p_id ) 
            self.p_phone = p_data['phone']
            print( self.p_phone) 
            self.p_age = p_data['age']
            print(self.p_age)
            self.p_gender = p_data['gender']
            print(self.p_name)
            self.dr_id = p_data['dr_id']
            print(self.p_name)
           
        else : 
            print("patient not found")
        
            
        if self.found == 1 : 
            nm_lbl=Label(p_frame , text="Name:",font=("times new roman",12,"bold"),bg='#E9D3FF')
            nm_lbl.grid(row=0,column = 0, padx=2, pady=10, sticky=W) 
        
            nm_val_lbl=Label(p_frame , text=self.p_name,font=("times new roman",12,"bold"),bg='#E9D3FF')
            nm_val_lbl.grid(row=0,column = 2, padx=2, pady=10, sticky=W)  
        
        
            id_lbl=Label(p_frame , text="ID:",font=("times new roman",12,"bold"),bg='#E9D3FF')
            id_lbl.grid(row=0,column = 8, padx=2, pady=10, sticky=W) 
            id_val_lbl=Label(p_frame , text= self.p_id,font=("times new roman",12,"bold"),bg='#E9D3FF')
            id_val_lbl.grid(row=0,column = 10, padx=2, pady=10, sticky=W)  
        
        
            age_lbl=Label(p_frame , text="Age:",font=("times new roman",12,"bold"),bg='#E9D3FF')
            age_lbl.grid(row=0,column = 16, padx=2, pady=10, sticky=W)
        
            age_val_lbl=Label(p_frame , text=self.p_age,font=("times new roman",12,"bold"),bg='#E9D3FF')
            age_val_lbl.grid(row=0,column = 18, padx=2, pady=10, sticky=W)
            
            
            gen_lbl=Label(p_frame , text="Gender:",font=("times new roman",12,"bold"),bg='#E9D3FF')
            gen_lbl.grid(row=0,column = 23, padx=2, pady=10, sticky=W)
        
            gen_val_lbl=Label(p_frame , text=self.p_gender,font=("times new roman",12,"bold"),bg='#E9D3FF')
            gen_val_lbl.grid(row=0,column = 25, padx=2, pady=10, sticky=W)
            
            
            phn_lbl=Label(p_frame , text="Phone:",font=("times new roman",12,"bold"),bg='#E9D3FF')
            phn_lbl.grid(row=0,column = 31, padx=2, pady=10, sticky=W)
        
            phn_val_lbl=Label(p_frame , text=self.p_phone,font=("times new roman",12,"bold"),bg='#E9D3FF')
            phn_val_lbl.grid(row=0,column = 33, padx=2, pady=10, sticky=W)
            
            
            phn_lbl=Label(p_frame , text="DrId:",font=("times new roman",12,"bold"),bg='#E9D3FF')
            phn_lbl.grid(row=0,column = 39, padx=2, pady=10, sticky=W)
        
            phn_val_lbl=Label(p_frame , text=self.dr_id,font=("times new roman",12,"bold"),bg='#E9D3FF')
            phn_val_lbl.grid(row=0,column = 41, padx=2, pady=10, sticky=W)
            
            
        
        else : 
            nm_lbl=Label(p_frame , text="Patient not found",font=("times new roman",12,"bold"),bg='#E9D3FF')
            nm_lbl.grid(row=0,column = 0, padx=2, pady=10, sticky=W) 
            
            add_p_btn = Button(p_frame,text="Add patient",width=13)
            add_p_btn.grid(row=0,column = 5, padx=2, pady=10, sticky=W) 
            
        
        print("set ")
        print(Examin.pre_set) 
        self.Ex_set = Examin.pre_set 
        
        Heading_txt="Microscopic Examination and Diagnosis"
        
#         Early_txt='''
        
#         Early-ALL cells  :  Found
        
#         The examination shows irregular cell shapes and an abnormal nuclear-to-cytoplasmic ratio. In addition,             there is an increased number of immature and abnormal cells and decreased numbers of normal blood cells.           Also, cells tend to form clusters or aggregates in the peripheral blood, indicating their tendency to             associate with each other and potentially leading to the obstruction of blood vessels.
   
   
#         '''
        
#         pre_txt='''
        
#         Pre-ALL cells  :  Found
        
#        Some nuclei appear to be round and others are slightly irregular, The chromatin pattern is coarse,
#        in addition to the presence of an Abnormal proliferation of immature B-cell progenitors, as well as the            presence of a significant number of blast cells,lymphoblasts where the large number of blast cells  leads          to a reduction in the number of normal blood cells which leads to anemia, thrombocytopenia, and decreased          mature white blood cells. 
       

#         '''
        
        
#         pro_txt='''
        
#        Pro-ALL cells  :  Found 
       
#        Here appear immature cellular features, including large nuclei, fine chromatin pattern, prominent nucleoli,        and scant cytoplasm. The nuclear shape is rounded and irregular, with a fine granular chromatin pattern            and dispersed chromatin clumps. There is a lack of cytoplasmic granules, as well as an increased number of        blasts and a high nucleocytoplasmic ratio, indicating the presence of immature cells and the presence of          ribosomes and other protein synthesis machinery in the cytoplasm.
       
       
#         '''
            
            
#         benign_txt='''
        
#        Begnin-Cancer cells:  Found
       
#        The cellular composition appears normal with small, round lymphocytes, including more fragile cells known          as 'smudge cells.' There is also an increased number of platelets; however, the platelets themselves may          appear normal in morphology. Additionally, there is an increased number of red blood cells.
       
       
#         '''
        
#         rec_txt='''
        
#       Recommendations: 
       
#       It is recommended to start following up with a hematologist in order to manage the treatment plan and             coordinate care. In addition, it is important to start chemotherapy as soon as possible to avoid any               progression in the proposed case. Also, supportive care measures must be implemented to manage and minimize       treatment-related side effects. Emotional support and counseling should be provided to facilitate the             treatment process.


#       Remember, 
#         "You never know how strong you are until being strong is your only choice.
        
        
#       '''

        Early_txt = "Early-ALL cells  :  Found\n\nThe examination shows irregular cell shapes and an abnormal nuclear-to-cytoplasmic ratio. In addition, there is an increased number of immature and abnormal cells and decreased numbers of normal blood cells. Also,\n cells tend to form clusters or aggregates in the peripheral blood, indicating their tendency to associate with each other and potentially leading to the obstruction of blood vessels.\n"

        pre_txt = "Pre-ALL cells  :  Found\n\nSome nuclei appear to be round and others are slightly irregular. The chromatin pattern is coarse. In addition, there is an abnormal proliferation of immature\n B-cell progenitors, as well as a significant number of blast cells (lymphoblasts), leading to a reduction in the number of normal blood cells.\n This reduction can cause anemia, thrombocytopenia, and decreased mature white blood cells.\n"

        pro_txt = "Pro-ALL cells  :  Found\n\nHere, immature cellular features are observed, including large nuclei, fine chromatin pattern, prominent nucleoli, and scant cytoplasm.\n The nuclear shape is rounded and irregular, with a fine granular chromatin pattern and dispersed chromatin clumps.\n There is a lack of cytoplasmic granules, as well as an increased number of blasts and a high nucleocytoplasmic ratio, indicating the presence of immature cells \nand the presence of ribosomes and other protein synthesis machinery in the cytoplasm.\n"

        benign_txt = "Benign-Cancer cells:  Found\n\nThe cellular composition appears normal with small, round lymphocytes, including more fragile cells known as 'smudge cells.'\n There is also an increased number of platelets; however, the platelets themselves may appear normal in morphology. Additionally, there is an increased number of red blood cells.\n"

        rec_txt = "Recommendations:\n\nIt is recommended to start following up with a hematologist in order to manage the treatment plan and coordinate care. In addition, it is important to start chemotherapy as soon as possible to avoid any progression\n in the proposed case.\n Also, supportive care measures must be implemented to manage and minimize treatment-related side effects. \nEmotional support and counseling should be provided to facilitate the treatment process.\n\nRemember,\n\"You never know how strong you are until being strong is your only choice.\""
        
        l_r=0
        hd_lbl=Label(rp_frame , text=Heading_txt,font=("times new roman",12,"bold"),bg='#E9D3FF' , justify='left',anchor='w')
        hd_lbl.grid(row=l_r,column = 0, padx=2, pady=10, sticky=W)  
        l_r+=6
        
        if 'Early' in self.Ex_set : 
            e_lbl=Label(rp_frame , text=Early_txt,font=("times new roman",12,"bold"),bg='#E9D3FF', justify='left',anchor='w')
            e_lbl.grid(row=l_r,column =0, padx=2, pady=10, sticky=W)  
            l_r+=6
        if 'Pre' in self.Ex_set : 
            pre_lbl=Label(rp_frame , text=pre_txt,font=("times new roman",12,"bold"),bg='#E9D3FF', justify='left',anchor='w')
            pre_lbl.grid(row=l_r,column =0, padx=2, pady=10, sticky=W)  
            l_r+=6
            
        if 'Pro' in self.Ex_set : 
            pro_lbl=Label(rp_frame , text=pro_txt,font=("times new roman",12,"bold"),bg='#E9D3FF', justify='left',anchor='w')
            pro_lbl.grid(row=l_r,column =0, padx=2, pady=10, sticky=W)  
            l_r+=6 
            
        if 'Benign' in self.Ex_set : 
            b_lbl=Label(rp_frame , text=benign_txt,font=("times new roman",12,"bold"),bg='#E9D3FF', justify='left',anchor='w')
            b_lbl.grid(row=l_r,column =0, padx=2, pady=10, sticky=W)  
            l_r+=6     
        
        rec_lbl=Label(rp_frame , text=rec_txt,font=("times new roman",12,"bold"),bg='#E9D3FF', justify='left',anchor='w')
        rec_lbl.grid(row=l_r,column =0, padx=2, pady=10, sticky=W)      
            
 
if __name__ == "__main__":
    root=tk.Tk()
    rep = Report(root)
    exmn = Examin(root)
    exmn.rep = rep