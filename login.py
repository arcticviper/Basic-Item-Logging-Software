# BILS - BASIC ITEM LOGGING SOFTWARE
# Version 0.1
# Created by Charles Denison
# LOGIN
from tkinter import *
import tkinter.messagebox as tm
import sqlite3
import getpass
import time
import datetime
conn = sqlite3.connect('setup.db')
c = conn.cursor()
unix = time.time()
date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%M-%d %H:%M:%S'))
#user input
class Login(Frame): #create loginframe
    def __init__(self, master):
        super().__init__(master)#inherit base class
        #init labels
        self.labelusr = Label(self, text="Username")
        self.labelpw = Label(self, text="Password")
        #init entry
        self.entryusr = Entry(self)
        self.entrypw = Entry(self, show="*")

        #logo = PhotoImage(file="APC-logo.png")
        #w1 = Label(root, image=logo).grid(row=0,column=0)

        #grid sorting
        self.labelusr.grid(row=1, sticky=E)
        self.labelpw.grid(row=2, sticky=E)
        self.entryusr.grid(row=1, column=1)
        self.entrypw.grid(row=2, column=1)
        self.logbtn = Button(self, text="Login", command = self._login_btn_clickked,bg="#B3B3B3")
        self.logbtn.grid(row=1, column=2, rowspan=2)
        self.logout = Button(self, text="Exit", command = quit,bg="#B3B3B3")
        self.logout.grid(columnspan=2)
        self.pack()
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
        else:
            attempt=attempt+1
            tm.showerror("Login error", "Login failed, please ensure you have typed your details correctly. Otherwise please contact the system adminstrator")
            c.execute("INSERT INTO userlog(Attempt, Email, datestamp,sucessful)VALUES(?,?,?,?)",(attempt,user,date,False))
            c.execute('UPDATE users SET unattempt = unattempt+1 WHERE Email= ?',(user,))
            conn.commit()
root = Tk()
root.configure(bg="#707070")
lf = Login(root)
root.mainloop()
