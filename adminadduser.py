# BILS - BASIC ITEM LOGGING SOFTWARE
# Version 0.1
# Created by Charles Denison
# User Creation
from tkinter import *
import tkinter.messagebox as tm
import sqlite3
import time
import datetime
import runpy
conn = sqlite3.connect('setup.db')
c = conn.cursor()
unix = time.time()
date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
def adminpanel():
        conn.close()
        root.destroy()
        runpy.run_path('adminpanel.py')
#user input
class Borrow(Frame): #create returnframe
    def __init__(self, master):
        super().__init__(master)#inherit base class
        self.grid()
        self.create_widget()
    def create_widget(self):
        #init labels
        self.labeluser = Label(self, text="Username")
        self.labelpass = Label(self, text="Password")
        self.labelpriv = Label(self, text="Privilege")
        #init entry
        self.entryuser = Entry(self)
        self.entrypass = Entry(self)
        self.entrypriv = Entry(self)
        #grid sorting
        self.labeluser.grid(row=1, sticky=E)
        self.labelpass.grid(row=2, sticky=E)
        self.labelpriv.grid(row=3, sticky=E)
        self.entryuser.grid(row=1, column=1)
        self.entrypass.grid(row=2, column=1)
        self.entrypriv.grid(row=3, column=1)
        self.addbtn = Button(self, text="Add User", command = self._add_btn_clickked,bg="#B3B3B3")
        self.addbtn.grid(row=1, column=2)
        self.clrbtn = Button(self, text="Clear", command = self._clear_btn_clickked,bg="#B3B3B3")
        self.clrbtn.grid(row=2, column=2)
        self.logout = Button(self, text="Exit", command = adminpanel,bg="#B3B3B3")
        self.logout.grid(row=3, column=2)
        # frame complete
        # button functions
    def _clear_btn_clickked(self):
        self.entryuser.delete(0, 'end')
        self.entrypass.delete(0, 'end')
        self.entrypriv.delete(0, 'end')
        tm.showinfo("Clear input", "Input has been cleared.")
        conn.commit()
    def _add_btn_clickked(self):
        user = self.entryuser.get()
        pwrd = self.entrypass.get()
        privget = self.entrypriv.get()
        IDGEN = int(0)
        unat = int(0)
        try:
            priv = int(privget)
        except:
            tm.showerror("Privilege error", "Input failed, please ensure you have inserted a 1 for admin and 0 user in the privilege box.")
            conn.commit()
        print (user,pwrd,priv)#debugging
        c.execute('SELECT ID FROM users WHERE Email="%s"' % (user))
        tempid=c.fetchone()
        print(tempid)
        if tempid is None: #check if user exists
            if user is not "":
                if pwrd is not "":
                    if priv == 1 or priv == 0:
                        tm.showinfo("Update complete", "The details have been updated.")
                        c.execute('INSERT INTO users(Email,password,priv,unattempt)VALUES(?,?,?,?)' ,(user,pwrd,priv,unat))
                        conn.commit()
                    else:
                        tm.showerror("Incorrect value", "Please insert a 1 for admin and 0 user.")
                        conn.commit()
                else:
                    tm.showerror("Incorrect value", "Please insert a password.")
                    conn.commit()
            else:
                tm.showerror("Incorrect value", "Please insert a username")
                conn.commit()
        else:
                tm.showerror("Borrow error2", "Search failed, please ensure you have typed the details correctly.")
                conn.commit()
        
        
        
#execute functions
root = Tk()
root.wm_title("New user")
root.configure(bg="#707070")
logo = PhotoImage(master = root,file="APC-logo.gif")
w1 = Label(root, image=logo).grid(row=0,column=0)
lf = Borrow(root)
root.mainloop()
