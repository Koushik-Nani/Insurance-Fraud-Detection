#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Sep 28, 2023 07:28:12 PM IST  platform: Windows NT

from functools import partial
import sys
import tkinter as tk
from tkinter import StringVar, Toplevel, messagebox
import tkinter.ttk as ttk

from tkinter import *
from tkinter.ttk import *

from tkinter.constants import *
from PIL import ImageTk, Image
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import Gui_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

global size
global Button1

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("954x633+308+124")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Fraud Detection")
        top.iconbitmap("car1.ico")
        top.configure(background="#000000")

        self.top = top

        self.style = ttk.Style()

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.042, rely=0.047, relheight=0.907
                , relwidth=0.477)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="0")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#000000")

        img = ImageTk.PhotoImage(Image.open("car3.jpg"))
        self.Label5 = tk.Label(self.Frame1,image=img)
        #label5 = Label(frame, image = img)
        self.Label5.photo = img
        self.Label5.pack()
        self.Label5.place(relx=0.100, rely=0.0,relheight=1.020, relwidth=0.880)

        self.Frame2 = tk.Frame(self.top)
        self.Frame2.place(relx=0.514, rely=0.047, relheight=0.907
                , relwidth=0.448)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="0")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#141414")

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.198, rely=0.02, height=51, width=300)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#141414")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 28 -weight bold")
        self.Label1.configure(foreground="#5c5c5c")
        self.Label1.configure(text='''Fraud Detection''')
        
        self.Label2 = tk.Label(self.Frame2,font=("Arial", 12))
        self.Label2.place(relx=0.398, rely=0.120, height=21, width=134)
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#141414")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#5c5c5c")
        self.Label2.configure(text='''Enter Details''')
        #self.Label2.grid(row = 1, column = 0)

        self.Label3 = tk.Label(self.Frame2,font=("Arial", 14))
        self.Label3.place(relx=0.098, rely=0.190, height=21, width=100)
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#141414")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#5c5c5c")
        self.Label3.configure(text='''Make''')
        self.option1 = tk.StringVar(self.Frame2)
    

        self.style.map("custom.TMenubutton",foreground=[('pressed', 'red'), ('active', 'blue')],background=[('pressed', '!disabled', 'black'), ('active', 'white')])
        self.style.configure('custom.TMenubutton', font=('Helvetica', 14),relief='flat',highlightthickness=2,
        borderwidth=2,arrowsize=10,arrowcolor="#5c5c5c",arrowpadding=10,background="#141414",foreground="#5c5c5c")
        
        self.op1 = ttk.OptionMenu(self.Frame2, self.option1, "Honda","Honda","Toyota","Ford","Mazda","Chevrolet","Pontiac","Accura","Dodge","Jaguar",style='custom.TMenubutton')


        self.op1.place(relx=0.550, rely=0.190)

        self.Label4 = tk.Label(self.Frame2,font=("Arial", 14))
        self.Label4.place(relx=0.098, rely=0.260, height=21, width=134)
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#141414")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#5c5c5c")
        self.Label4.configure(text='''AccidentArea''')
        self.option2 = tk.StringVar(self.Frame2)
  
        self.op2 =ttk.OptionMenu(self.Frame2, self.option2, "Urban","Urban","Rural",style='custom.TMenubutton')
        self.op2.place(relx=0.550, rely=0.260)


        self.Label5 = tk.Label(self.Frame2,font=("Arial", 14))
        self.Label5.place(relx=0.098, rely=0.330, height=21, width=134)
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#141414")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#5c5c5c")
        self.Label5.configure(text='''Gender''')
        self.option3 = tk.StringVar(self.Frame2)
        self.option3.set("One")
        self.op3 =ttk.OptionMenu(self.Frame2, self.option3, "Male","Male","Female","Other",style='custom.TMenubutton')
        self.op3.place(relx=0.550, rely=0.330)


        self.Label6 = tk.Label(self.Frame2,font=("Arial", 14))
        self.Label6.place(relx=0.098, rely=0.400, height=21, width=134)
        self.Label6.configure(anchor='w')
        self.Label6.configure(background="#141414")
        self.Label6.configure(compound='left')
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#5c5c5c")
        self.Label6.configure(text='''MaritalStatus''')
        self.option4 = tk.StringVar(self.Frame2)
        self.option4.set("One")
        self.op4 =ttk.OptionMenu(self.Frame2, self.option4, "Single","Single","Married",style='custom.TMenubutton')
        self.op4.place(relx=0.550, rely=0.400)


        self.Label7 = tk.Label(self.Frame2,font=("Arial", 14))
        self.Label7.place(relx=0.098, rely=0.470, height=21, width=134)
        self.Label7.configure(anchor='w')
        self.Label7.configure(background="#141414")
        self.Label7.configure(compound='left')
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#5c5c5c")
        self.Label7.configure(text='''Fault''')
        self.option5 = tk.StringVar(self.Frame2)
        self.option5.set("One")
        self.op5 =ttk.OptionMenu(self.Frame2, self.option5, "Policy Holder","Policy Holder","Third Party",style='custom.TMenubutton')
        self.op5.place(relx=0.550, rely=0.470)


        self.Label8 = tk.Label(self.Frame2,font=("Arial", 14))
        self.Label8.place(relx=0.098, rely=0.540, height=21, width=134)
        self.Label8.configure(anchor='w')
        self.Label8.configure(background="#141414")
        self.Label8.configure(compound='left')
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#5c5c5c")
        self.Label8.configure(text='''VehicleCategory''')
        self.option6 = tk.StringVar(self.Frame2)
        self.option6.set("One")
        self.op6 =ttk.OptionMenu(self.Frame2, self.option6, "Sport","Sport","Utility","Sedan",style='custom.TMenubutton')
        self.op6.place(relx=0.550, rely=0.540)



        self.Label10 = tk.Label(self.Frame2,font=("Arial", 14))
        self.Label10.place(relx=0.098, rely=0.680, height=21, width=185)
        self.Label10.configure(anchor='w')
        self.Label10.configure(background="#141414")
        self.Label10.configure(compound='left')
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#5c5c5c")
        self.Label10.configure(text='''PastNumberOfClaims''')
        self.option7 = tk.StringVar(self.Frame2)
        self.option7.set("One")
        self.op7 =ttk.OptionMenu(self.Frame2, self.option7, "1","1","2","3","4","5",style='custom.TMenubutton')
        self.op7.place(relx=0.550, rely=0.680)


        self.Label9 = tk.Label(self.Frame2,font=("Arial", 14))
        self.Label9.place(relx=0.098, rely=0.610, height=21, width=134)
        self.Label9.configure(anchor='w')
        self.Label9.configure(background="#141414")
        self.Label9.configure(compound='left')
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#5c5c5c")
        self.Label9.configure(text='''AgeOfVehicle''')
        self.option8 = tk.StringVar(self.Frame2)
        self.option8.set("One")
        self.op8 =ttk.OptionMenu(self.Frame2, self.option8, "1","1","2","3","4","5","6","7","7<",style='custom.TMenubutton')
        self.op8.place(relx=0.550, rely=0.610)

        self.Label11 = tk.Label(self.Frame2,font=("Arial", 14))
        self.Label11.place(relx=0.098, rely=0.750, height=21, width=134)
        self.Label11.configure(anchor='w')
        self.Label11.configure(background="#141414")
        self.Label11.configure(compound='left')
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#5c5c5c")
        self.Label11.configure(text='''PolicyType''')
        self.option9 = tk.StringVar(self.Frame2)
        self.option9.set("One")
        self.op9 =ttk.OptionMenu(self.Frame2, self.option9, "Sport - Liability","Sport - Liability","Sport - Collision","Sedan - Liability","Sedan - All Perils","Sedan - Collision","Utility - All Perils",style='custom.TMenubutton')
        self.op9.place(relx=0.550, rely=0.750)


        self.option10 = tk.StringVar(self.Frame2)
        self.option10.set("One")

        self.option11 = tk.StringVar(self.Frame2)
        self.option11.set("One")

        self.option12 = tk.StringVar(self.Frame2)
        self.option12.set("One")

        self.option13 = tk.StringVar(self.Frame2)
        self.option13.set("One")

        global Button1
        self.size=26
        self.Button1 = tk.Button(self.Frame2,command=partial(first,[self.option1,self.option2,self.option3,self.option4,self.option5,self.option6,0,0,0,0,self.option7,self.option8,self.option9,0,0,0,0,3,3,0,0]))
        #self.Button1 = tk.Button(self.Frame2,command=expand)
       
        self.Button1.place(relx=0.117, rely=0.906, height=34, width=327)
        self.Button1.configure(activebackground="#E41712")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#141414")
        self.Button1.configure(borderwidth="1")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#5c5c5c")
        self.Button1.configure(highlightbackground="#E41712")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Find''')

def expand():
    global siz
    global Button1
    siz=10

    Button1.config(font=("Helvetica",siz))

def first(test):
    import numpy as np
    import pandas as pd 
    import os
    import tkinter as tk
    from tkinter import ttk
    import matplotlib.pyplot as plt
    #import seaborn as sns
    from sklearn.preprocessing import LabelEncoder
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import f1_score, accuracy_score, confusion_matrix,roc_auc_score
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.utils import resample
    import warnings
    import random
    warnings.filterwarnings("ignore")
    
    df = pd.read_csv("carclaims.csv")

    df.loc[df['FraudFound'] == 'No','FraudFound'] = 0
    df.loc[df['FraudFound'] == 'Yes','FraudFound'] = 1

    df['FraudFound'] = df['FraudFound'].astype(int)

    make = df.groupby('Make')['FraudFound'].sum()
    policyAge = df.groupby('AgeOfPolicyHolder')['FraudFound'].sum()
    gender = df.groupby('Sex')['FraudFound'].sum()
    accidentArea = df.groupby('AccidentArea')['FraudFound'].sum()
    fault = df.groupby('Fault')['FraudFound'].sum()
    cars = df.groupby('NumberOfCars')['FraudFound'].sum()
    fraud = df[df['FraudFound'] == 1]
    le = LabelEncoder()

    #progress_bar.step(10)

    cols = df.select_dtypes('O').columns

    df[cols]= df[cols].apply(le.fit_transform)
    df['Year'] = le.fit_transform(df.Year)

    df_new = df[['Make', 'AccidentArea','Sex',\
       'MaritalStatus','Fault', 'VehicleCategory',\
       'VehiclePrice', 'Year',\
       'DriverRating', 'Days:Policy-Accident', 'Days:Policy-Claim',\
       'PastNumberOfClaims', 'AgeOfVehicle', 'AgeOfPolicyHolder',\
       'PoliceReportFiled', 'WitnessPresent', 'AgentType',\
       'NumberOfSuppliments', 'AddressChange-Claim', 'NumberOfCars',\
       'BasePolicy', 'FraudFound']]

    X = df_new.drop('FraudFound',axis=1)
    y = df_new[['FraudFound']]
    X_train,X_test,y_train,y_test = train_test_split(X,y,stratify=y)
    X_train.shape, X_test.shape, y_train.shape, y_test.shape

    test
    new = [0]*21
    if (test[0] == "Toyota"):
        new[0] = 17
    elif(test[0]== "Pontiac"):
        new[0] = 13

    if(test[1]== 'Urban'):
        new[1] = 1
    elif(test[1]== 'Rural'):
        new[1] = 0

    if(test[2]== 'Male'):
        new[2] = 1
    elif(test[2]== 'Female'):
        new[2] = 0
    elif(test[2]== 'Other'):
        new[2] = 1

    if (test[3] == 'single'):
        new[3] = 2
    elif(test[3]== 'married'):
        new[3] = 1

    if (test[4] == 'Policy Holder'):
        new[4] = 0
    elif(test[4]== 'Third Party'):
        new[4] = 1
    
    if (test[5] == 'Sport'):
        new[5] = 1
    elif(test[5]== 'Utility'):
        new[5] = 2
    elif(test[5]== 'Sedan'):
        new[5] = 0
#past claims
    elif (test[10] == '1'):
        new[10] = 1
    elif(test[10]== '2'):
        new[10] = 2
    elif(test[10]== '3'):
        new[10] = 3
    elif(test[10]== '4'):
        new[10] = 4
    # elif(test[10]== '5'):
    #     test[10] = 5

#vechile age
    if (test[11] == '1'):
        new[11] = 1
    elif(test[11]== '2'):
        new[11] = 2
    elif(test[11]== '3'):
        new[11] = 3
    elif(test[11]== '4'):
        new[11] = 4
    elif(test[11]== '5'):
        new[11] = 5
    elif(test[11]== '6'):
        new[11] = 6

    if (test[12] == 'Sport - Liability'):
        new[12] = 1
    elif(test[12]== 'Sport - Collision'):
        new[12] = 2
    elif(test[12]== 'Sedan - Liability'):
        new[12] = 2
    elif(test[12]== 'Sedan - All Perils'):
        new[12] = 2
    elif(test[12]== 'Sedan - Collision'):
        new[12] = 2
    elif(test[12]== 'Utility - All Perils'):
        new[12] = 2

    print(new) 

    rfc = RandomForestClassifier()
    rfc.fit(X_train,y_train)
    rfc_upscale_pred = rfc.predict([new])
    a =[0,1]
    if (rfc_upscale_pred[0] == 1):
        messagebox.showerror("Result","Its a fraud")
    else:
        messagebox.showerror("Result","Not a fraud")

    # acc_rfc_upscale=accuracy_score(y_test, rfc_upscale_pred)
    # print("Accuracy of thie model:\t\t",acc_rfc_upscale)
    #conf_matrix(y_test,rfc_upscale_pred)

def start_up():
    Gui_support.main()

if __name__ == '__main__':
    Gui_support.main()




