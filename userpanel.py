# BILS - BASIC ITEM LOGGING SOFTWARE
# Version 0.1
# Created by Charles Denison
# User PANEL
from tkinter import *
import tkinter
import os
import runpy

class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        self.bttn1 = Button(root,text="Return Item",width=80,bg="#B3B3B3")
        #self.bttn1["command"] = #open Return Item
        self.bttn1.grid(row=1,column=0)
        self.bttn2 = Button(root,text="Withdraw",width=80,bg="#B3B3B3")
        #self.bttn2["command"] = #open Withdraw
        self.bttn2.grid(row=2,column=0)
        with open("login.py") as f:
            code = compile(f.read(), "login.py", 'exec')
        self.bttn3 = Button(root,text="Logout",width=80,bg="#B3B3B3")
        self.bttn3["command"] = exec(code)
        self.bttn3.grid(row=3,column=0)
        self.bttn4 = Button(root,text="Quit",width=80,bg="#B3B3B3")
        self.bttn4["command"] = quit
        self.bttn4.grid(row=4,column=0)

root = Tk()
root.configure(bg="#4D4D4D")
logo = PhotoImage(file="APC-logo.png")
w1 = Label(root, image=logo).grid(row=0,column=0)
app = Application(root)
root.mainloop
