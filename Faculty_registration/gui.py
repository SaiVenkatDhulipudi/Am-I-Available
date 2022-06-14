from email.mime import base
from tkinter import *
from turtle import width
from screeninfo import get_monitors
import aadhar
class gui:
    def __init__(self,root) -> None:
        self.root=root
        self.root.font=("times new roman",30)
        self.width=str(get_monitors()[0].width)
        self.height=str(get_monitors()[0].height)
        self.root.geometry("{}x{}".format(self.width,self.height))
        self.root.title("Employee Registration")
        self.root.resizable(False,False)
        self.root.config(background="white")
        self.name=StringVar()
        self.dept=StringVar()
        self.phoneno=StringVar()
        self.email=StringVar()
        self.dob=StringVar()
        self.aadhar=StringVar()
        self.code=StringVar()
        self.age=StringVar()
        self.password=StringVar()
        self.repassword=StringVar()
        Label(self.root,text="Name :",font=("times new roman",15,'bold'),bg='white').place(x=20,y=60)
        Label(self.root,text="Age :",font=("times new roman",15,'bold'),bg='white').place(x=20,y=100)
        Label(self.root,text="Phone :",font=("times new roman",15,'bold'),bg='white').place(x=20,y=140)
        Label(self.root,text="Email :",font=("times new roman",15,'bold'),bg='white').place(x=20,y=180)
        Label(self.root,text="Date of Birth :",font=("times new roman",15,'bold'),bg='white').place(x=20,y=220)
        Label(self.root,text="Aadhar No :",font=("times new roman",15,'bold'),bg='white').place(x=20,y=260)
        Label(self.root,text="Department :",font=("times new roman",15,'bold'),bg='white').place(x=20,y=300)
        Label(self.root,text="Enter Password :",font=("times new roman",15,'bold'),bg='white').place(x=20,y=340)
        Label(self.root,text="Re-Enter Password :",font=("times new roman",15,'bold'),bg='white').place(x=20,y=380)
        self.options=[
            "CSE",
            "ECE",
            "EEE",
            "CIVIL",
            "MECH",
            "AIDS",
            "BSH",
            "TP",
            "EC"
            ]
        self.clicked = StringVar()
        self.clicked.set("select")
        drop = OptionMenu(self.root , self.clicked , *self.options)
        drop.config(font=("times new roman",15))
        drop.place(x=200,y=300,width=200,height=40)
        Entry(self.root,textvariable=self.name,font=("times new roman",15),bg='white',bd='2').place(x=200,y=60)
        Entry(self.root,textvariable=self.age,font=("times new roman",15),bg='white',bd='2').place(x=200,y=100)
        Entry(self.root,textvariable=self.phoneno,font=("times new roman",15),bg='white',bd='2').place(x=200,y=140)
        Entry(self.root,textvariable=self.email,font=("times new roman",15),bg='white',bd='2').place(x=200,y=180)
        Entry(self.root,textvariable=self.dob,font=("times new roman",15),bg='white',bd='2').place(x=200,y=220)
        Entry(self.root,textvariable=self.aadhar,font=("times new roman",15),bg='white',bd='2').place(x=200,y=260)
        Entry(self.root,textvariable=self.password,font=("times new roman",15),bg='white',bd='2').place(x=200,y=340)
        Entry(self.root,textvariable=self.repassword,font=("times new roman",15),bg='white',bd='2').place(x=200,y=380)
        Button(self.root,text='Submit',command=lambda:None,font=("times new roman",18,'bold'),bg='#6a64d9',fg='white').place(x=70,y=410,width=160,height=35)

        # btn_clr=Button(self.root,text='Clear',command=self.clr,font=("times new roman",18,'bold'),bg='#567',fg='white').place(x=300,y=410,width=140,height=35)

if __name__=="__main__":
    root=Tk()
    gui(root)
    root.mainloop()