class branch:
    def __init__(self) -> None:
        self.CSE="11"
        self.CIVIL="12"
        self.MECH="13"
        self.AIDS="14"
        self.ECE="15"
        self.EEE="16"
        self.BSH="17"
        self.TP="18"
        self.EC="19"
        self.principal="10101"
        self.rector="10202"
        self.ceo="10303"

# Import module
from tkinter import *
root = Tk()

def show():
	label.config( text = clicked.get() )
options = [
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday",
	"Sunday"
]

clicked = StringVar()
clicked.set("")
drop = OptionMenu( root , clicked , *options )
drop.pack()
root.mainloop()
