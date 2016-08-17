# BILS - BASIC ITEM LOGGING SOFTWARE
# Created: 9/07
# Modified: 17/08
# Created by Charles Denison
# ADMIN PANEL
from tkinter import *
import tkinter
import os
import runpy

def logout():
        root.destroy()
        runpy.run_path('Login.py')
def userpanel():
        root.destroy()
        runpy.run_path('userpanel/UserPanel.py')
def usermod():
        root.destroy()
        runpy.run_path('adminpanel/Adminmoduser.py')
def useradd():
        root.destroy()
        runpy.run_path('adminpanel/AdminAddUser.py')
def userlog():
        root.destroy()
        runpy.run_path('adminpanel/AdminLogUser.py')
def itemlog():
        root.destroy()
        runpy.run_path('adminpanel/AdminLogItem.py')
def additem():
        root.destroy()
        runpy.run_path('adminpanel/AdminItemAdd.py')
def moditem():
        root.destroy()
        runpy.run_path('adminpanel/AdminItemMod.py')

class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widget()
        
    def create_widget(self,):
        self.itadButton = Button(root,text="Item Add",width=77,bg="#B3B3B3")
        self.itadButton["command"] = additem
        self.itadButton.grid(row=1,column=0)
        self.itmdButton = Button(root,text="Item Modify",width=77,bg="#B3B3B3")
        self.itmdButton["command"] = moditem
        self.itmdButton.grid(row=2,column=0)
        self.usadButton = Button(root,text="User Add",width=77,bg="#B3B3B3")
        self.usadButton["command"] = useradd
        self.usadButton.grid(row=3,column=0)
        self.usmdButton = Button(root,text="User Modify",width=77,bg="#B3B3B3")
        self.usmdButton["command"] = usermod
        self.usmdButton.grid(row=4,column=0)
        self.usplButton = Button(root,text="User Panel",width=77,bg="#B3B3B3")
        self.usplButton["command"] = userpanel
        self.usplButton.grid(row=5,column=0)
        self.uslgButton = Button(root,text="User Logging",width=77,bg="#B3B3B3")
        self.uslgButton["command"] = userlog
        self.uslgButton.grid(row=6,column=0)
        self.itlgButton = Button(root,text="Item Logging",width=77,bg="#B3B3B3")
        self.itlgButton["command"] = itemlog
        self.itlgButton.grid(row=7,column=0)
        self.lgutButton = Button(root,text="Logout",width=77,bg="#B3B3B3")
        self.lgutButton["command"] = logout
        self.lgutButton.grid(row=8,column=0)
        self.quitButton = Button(root,text="Quit",width=77,bg="#B3B3B3")
        self.quitButton["command"] = quit
        self.quitButton.grid(row=9,column=0)

root = Tk()
root.wm_title("Admin Panel")
root.configure(bg="#4D4D4D")
logo = PhotoImage(master = root,file="APC-logo.gif",width=640)
w1 = Label(root, image=logo).grid(row=0,column=0)
app = Application(root)
root.mainloop
