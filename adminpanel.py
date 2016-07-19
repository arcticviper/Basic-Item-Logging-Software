# BILS - BASIC ITEM LOGGING SOFTWARE
# Version 0.1
# Created by Charles Denison
# ADMIN PANEL
from tkinter import *
import tkinter
import os
import runpy

def logout():
        root.destroy()
        runpy.run_path('login.py')
def userpanel():
        root.destroy()
        runpy.run_path('userpanel.py')
def usermod():
        root.destroy()
        runpy.run_path('adminmoduser.py')
def useradd():
        root.destroy()
        runpy.run_path('adminadduser.py')
def userlog():
        root.destroy()
        runpy.run_path('adminloguser.py')
def itemlog():
        root.destroy()
        runpy.run_path('adminlogitem.py')

class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widget()
        
    def create_widget(self,):
        self.bttn1 = Button(root,text="Item Add",width=77,bg="#B3B3B3")
        #self.bttn1["command"] = #open item add
        self.bttn1.grid(row=1,column=0)
        self.bttn2 = Button(root,text="Item Modify",width=77,bg="#B3B3B3")
        #self.bttn2["command"] = #open item modify
        self.bttn2.grid(row=2,column=0)
        self.bttn3 = Button(root,text="User Add",width=77,bg="#B3B3B3")
        self.bttn3["command"] = useradd
        self.bttn3.grid(row=3,column=0)
        self.bttn4 = Button(root,text="User Modify",width=77,bg="#B3B3B3")
        self.bttn4["command"] = usermod
        self.bttn4.grid(row=4,column=0)
        self.bttn5 = Button(root,text="User Panel",width=77,bg="#B3B3B3")
        self.bttn5["command"] = userpanel
        self.bttn5.grid(row=5,column=0)
        self.bttn6 = Button(root,text="User Logging",width=77,bg="#B3B3B3")
        self.bttn6["command"] = userlog
        self.bttn6.grid(row=6,column=0)
        self.bttn7 = Button(root,text="Item Logging",width=77,bg="#B3B3B3")
        self.bttn7["command"] = itemlog
        self.bttn7.grid(row=7,column=0)
        self.bttn8 = Button(root,text="Logout",width=77,bg="#B3B3B3")
        self.bttn8["command"] = logout
        self.bttn8.grid(row=8,column=0)
        self.bttn9 = Button(root,text="Quit",width=77,bg="#B3B3B3")
        self.bttn9["command"] = quit
        self.bttn9.grid(row=9,column=0)

root = Tk()
root.wm_title("Admin Panel")
root.configure(bg="#4D4D4D")
logo = PhotoImage(master = root,file="APC-logo.gif",width=640)
w1 = Label(root, image=logo).grid(row=0,column=0)
app = Application(root)
root.mainloop
