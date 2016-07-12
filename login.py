# BILS - BASIC ITEM LOGGING SOFTWARE
# Version 0.1
# Created by Charles Denison
# LOGIN
from tkinter import *
import tkinter.messagebox as tm
import tkinter as tk
import sqlite3
import time
import datetime
import runpy
conn = sqlite3.connect('setup.db')
c = conn.cursor()
unix = time.time()
date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%M-%d %H:%M:%S'))
#user input
def admin():
    conn.close()
    root.destroy()
    runpy.run_path('adminpanel.py')
def userpanel():
    conn.close()
    root.destroy()
    runpy.run_path('userpanel.py')
class Login(Frame): #create loginframe
    def __init__(self, master):
        super().__init__(master)#inherit base class
        self.grid()
        self.create_widget()
    def create_widget(self):
        #init labels
        self.labelusr = Label(self, text="Username")
        self.labelpw = Label(self, text="Password")
        #init entry
        self.entryusr = Entry(self)
        self.entrypw = Entry(self, show="*")
        #grid sorting
        self.labelusr.grid(row=1, sticky=E)
        self.labelpw.grid(row=2, sticky=E)
        self.entryusr.grid(row=1, column=1)
        self.entrypw.grid(row=2, column=1)
        self.logbtn = Button(self, text="Login", command = self._login_btn_clickked,bg="#B3B3B3")
        self.logbtn.grid(row=1, column=2, rowspan=2)
        self.logout = Button(self, text="Exit", command = quit,bg="#B3B3B3")
        self.logout.grid(columnspan=2)
        #pack grid
    def _login_btn_clickked(self):
        user = self.entryusr.get()
        password = self.entrypw.get()
        attempt = 1
        #read from users table and ensures that user and password matches with information on database
        #when using different tables ensure that Email  and password matches the table selected (users) and only selecting users who have under 3 incorrect attempts
        c.execute('SELECT * from users WHERE Email="%s" AND password="%s" AND unattempt<3' % (user, password))
        #Mydata = c.execute('SELECT TextString from ControlTable WHERE Group = "Messages" and GroupNum = 1)')
        if c.fetchone() is not None:
            tm.showinfo("Login info", "Welcome")
            c.execute("INSERT INTO userlog(Attempt, Email, datestamp,sucessful)VALUES(?,?,?,?)",(attempt,user,date,True))
            c.execute('UPDATE users SET unattempt = 0 WHERE Email= ?',(user,))
            conn.commit()
            c.execute('SELECT * from users WHERE Email="%s" AND priv=1' % (user))
            if c.fetchone() is not None:
                admin()
            else:
                userpanel()
        else:
            attempt=attempt+1
            tm.showerror("Login error", "Login failed, please ensure you have typed your details correctly. Otherwise please contact the system adminstrator")
            c.execute("INSERT INTO userlog(Attempt, Email, datestamp,sucessful)VALUES(?,?,?,?)",(attempt,user,date,False))
            c.execute('UPDATE users SET unattempt = unattempt+1 WHERE Email= ?',(user,))
            conn.commit()
root = Tk()
root.wm_title("Login")
root.configure(bg="#707070")
#doesn't work on mac or python 3.5.1
logo = PhotoImage(master = root,file="APC-logo.gif")
w1 = Label(root, image=logo).grid(row=0,column=0)
lf = Login(root)
root.mainloop()
