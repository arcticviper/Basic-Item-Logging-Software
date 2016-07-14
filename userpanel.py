# BILS - BASIC ITEM LOGGING SOFTWARE
# Version 0.1
# Created by Charles Denison
# User PANEL
from tkinter import *
import tkinter
import os
import runpy

def logout():
        root.destroy()
        runpy.run_path('login.py')
def userreturn():
        root.destroy()
        runpy.run_path('userreturn.py')
def withdraw():
        root.destroy()
        runpy.run_path('userborrow.py')
def reserve():
        root.destroy()
        runpy.run_path('userreserve.py')

class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        self.bttn1 = Button(root,text="Return Item",width=80,bg="#B3B3B3")
        self.bttn1["command"] = userreturn
        self.bttn1.grid(row=1,column=0)
        self.bttn2 = Button(root,text="Borrow Item",width=80,bg="#B3B3B3")
        self.bttn2["command"] = withdraw
        self.bttn2.grid(row=2,column=0)
        self.bttn3 = Button(root,text="Reserve",width=80,bg="#B3B3B3")
        self.bttn3["command"] = reserve
        self.bttn3.grid(row=3,column=0)
        self.bttn4 = Button(root,text="Logout",width=80,bg="#B3B3B3")
        self.bttn4["command"] = logout
        self.bttn4.grid(row=4,column=0)
        self.bttn5 = Button(root,text="Quit",width=80,bg="#B3B3B3")
        self.bttn5["command"] = quit
        self.bttn5.grid(row=5,column=0)


root = Tk()
root.wm_title("User Panel")
root.configure(bg="#4D4D4D")
logo = PhotoImage(file="APC-logo.gif")
w1 = Label(root, image=logo).grid(row=0,column=0)
app = Application(root)
root.mainloop
