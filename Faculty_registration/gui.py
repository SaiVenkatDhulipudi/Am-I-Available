from email.mime import base
from tkinter import *
from screeninfo import get_monitors
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
        emp_name=Label(self.root,text="Name :",font=("times new roman",15,'bold'),bg='white').place(x=20,y=60)
        emp_dept=Label(self.root,text="Age :",font=("times new roman",15,'bold'),bg='white').place(x=20,y=100)
        emp_phno=Label(self.root,text="Phone :",font=("times new roman",15,'bold'),bg='white').place(x=20,y=140)
        emp_email=Label(self.root,text="Email :",font=("times new roman",15,'bold'),bg='white').place(x=20,y=180)
        emp_dob=Label(self.root,text="Date of Birth :",font=("times new roman",15,'bold'),bg='white').place(x=20,y=220)
        emp_code=Label(self.root,text="Aadhar No :",font=("times new roman",15,'bold'),bg='white').place(x=20,y=260)
        emp_code=Label(self.root,text="Department :",font=("times new roman",15,'bold'),bg='white').place(x=20,y=300)
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
        drop = OptionMenu(self.root , self.clicked , *self.options )
        drop.width=20
        drop.place(x=190,y=300)
if __name__=="__main__":
    root=Tk()
    gui(root)
    root.mainloop()