import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import joblib
import pandas as pd


#This function is called when predicted button is clicked!
def callthis():
    #getting the values from text boxes to variables with the help of textvariable in text boxes
    
    a=my_glu.get()
    b=my_bp.get() 
    c=my_skin.get()
    d=my_insulin.get()
    p=my_preg.get()
    k=my_age.get()
    j=my_bmi.get()
    
    
    #Printing the values of textboxes to output screen
    
    print("Myglucose Level: ",a)
    print('My BloodPressure Level: ',b)
    print("Skin Thickness: ",c)
    print("Insulin level: ",d)
    print('Pregnancies: ',p)
    print('Age: ',k)
    print('BMI: ',j)
    
    
    #Loading the prediction model using joblib
    
    model=joblib.load("predictive_model.sav")
    value=model.predict([[a,b,c,d,p,k,j]])
    value=int(value)   #This is the predicted value of given data in text boxes!
    percentage=model.predict_proba([[a,b,c,d,p,k,j]])
    
    #Print the message alert when you are diabetic or not
    #Change the label text when value is 1 or 0
    
    if value==1:
        messagebox.showinfo('Important Message','You Are Diabetic with '+str(float(percentage[:,1]*100//1))
                            +'% symptoms! Please go to Hospital')
        mystring.set('Sorry!.. You are ' +str(float(percentage[:,1]*100//1))+'% Diabetic')
        
    else:
        #messagebox.showinfo('Message','NOT Diabetic')
        mystring.set('Hurray!.. You are '+str(float(percentage[:,0]*100//1))+'%  Not Diabetic ')
        
        
        
    #Loading the newly created excel file for storing the data from textboxes 
    mydata=pd.read_excel('Gui_saved_data.xlsx')
    
    #New Data Frame for storing given values from textboxes
    mydata2=pd.Series({'Glucose':a,'BloodPressure':b,'Skin Thickness':c,'Insulin':d,'Pregnancies':p,'Age':k,'BMI':j,'Outcome':value})
    mydata2=pd.DataFrame(mydata2)
    mydata2=mydata2.transpose()
    
    
    mydata=pd.concat([mydata,mydata2],axis=0)
    mydata.set_index('Glucose')
    writer=pd.ExcelWriter('Gui_saved_data.xlsx')
    mydata.to_excel(writer,index=False)
    writer.save()
    print(mydata2)

    
#Reset the values to 0 after clicking on reset button
def reset():
    my_bp.set(0)
    my_glu.set(0)
    my_skin.set(0)
    my_insulin.set(0)
    my_preg.set(0)
    my_age.set(0)
    my_bmi.set(0.0)
    mystring.set("Output Will be print Here!")
    
        
        
win=Tk()
win.title("The GUI")
win.minsize(510,500)
win.config(background='skyblue')

firstlabel=Label(win,text='Diabetes Predictor',height=2,font=('Bold',25),background='skyblue').grid(row=1,column=2,sticky=W)
lable1=ttk.Label(win,text='Enter Glucose Level ').grid(row=2,column=1,sticky=E,pady=5)
my_glu=tk.IntVar()
glu=Entry(win,width=25,textvariable=my_glu,bd=4).grid(row=2,column=2,sticky=W,pady=5,padx=20)


lable2=ttk.Label(win,text='Enter BloodPressure level ').grid(row=3,column=1,sticky=E,pady=5)
my_bp=tk.IntVar()
bp=Entry(win,width=25,textvariable=my_bp,bd=4).grid(row=3,column=2,sticky=W,pady=5,padx=20)

lable3=ttk.Label(win,text='Enter Skin Thickness  ').grid(row=4,column=1,sticky=E,pady=5)
my_skin=tk.IntVar()
skin=Entry(win,width=25,textvariable=my_skin,bd=4).grid(row=4,column=2,sticky=W,pady=5,padx=20)

lable4=ttk.Label(win,text='Enter Insulin level    ').grid(row=5,column=1,sticky=E,pady=5)
my_insulin=tk.IntVar()
insulin=Entry(win,width=25,textvariable=my_insulin,bd=4).grid(row=5,column=2,sticky=W,pady=5,padx=20)


label5=ttk.Label(win,text='Pregnencies   ').grid(row=6,column=1,sticky=E,pady=5)
my_preg=tk.IntVar()
preg=Entry(win,width=25,textvariable=my_preg,bd=4).grid(row=6,column=2,sticky=W,pady=5,padx=20)

label6=ttk.Label(win,text='Age   ').grid(row=7,column=1,sticky=E,pady=5)
my_age=tk.IntVar()
age=Entry(win,width=25,textvariable=my_age,bd=4).grid(row=7,column=2,sticky=W,pady=5,padx=20)

label7=ttk.Label(win,text='Body Mass Index ( BMI )').grid(row=8,column=1,sticky=E)
my_bmi=tk.DoubleVar()
bmi=Entry(win,width=25,textvariable=my_bmi,bd=4).grid(row=8,column=2,sticky=W,pady=5,padx=20)


button=Button(win,text='Predict',width=15,bd=5,command=callthis,background='lightgreen',cursor='hand2').grid(row=10,column=2,sticky=W,pady=15,padx=35)#.grid(row=9,column=2,sticky=W,pady=5,padx=58)
reset1=Button(win,text='Reset',width=15,bd=4,command=reset,background='pink',cursor='hand2').place(x=350,y=190)
exit=Button(win,text="Exit",width=15,bd=4,command=win.destroy,background='red',cursor='hand2').place(x=350,y=250)

mystring=tk.StringVar()
mystring.set("Output Will be print Here!")
result_label=Label(win,textvariable=mystring,width=40).place(x=100,y=400)#.grid(row=11,column=2,sticky=W,pady=10,ipadx=30)
win.mainloop()


