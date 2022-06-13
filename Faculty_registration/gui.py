from email.mime import base
from tkinter import *
from screeninfo import get_monitors
class gui:
    def __init__(self,root) -> None:
        self.root=root
        self.width=str(get_monitors()[0].width)
        self.height=str(get_monitors()[0].height)
        self.root.geometry("{}x{}".format(self.width,self.height))
        self.root.title("Employee Registration")
        self.root.resizable(False,False)
        self.root.config(background="white")
        title=Label(self.root,text="Enter Your Details",font=("times new roman",30),bg='skyBlue',fg='Black').place(x=0,y=0,relwidth=1)
        
if __name__=="__main__":
    root=Tk()
    gui(root)
    root.mainloop()