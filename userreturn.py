# BILS - BASIC ITEM LOGGING SOFTWARE
# Version 0.1
# Created by Charles Denison
# User RETURN
from tkinter import *
import tkinter.messagebox as tm
import sqlite3
import time
import datetime
import runpy
conn = sqlite3.connect('setup.db')
c = conn.cursor()
unix = time.time()
date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%M-%d %H:%M:%S'))
id
def userpanel():
        root.destroy()
        runpy.run_path('userpanel.py')
def exit():
    conn.close()
    root.destroy()
    runpy.run_path('userpanel.py')
#user input
class Return(Frame): #create searchframe
    def __init__(self, master):
        super().__init__(master)#inherit base class
        self.grid()
        self.create_widget()
    def create_widget(self):
        #init labels
        self.labelserial = Label(self, text="Serial")
        self.labelbarcode = Label(self, text="Barcode")
        self.labelitemname = Label(self, text="Item name")
        #init entry
        self.entryserial = Entry(self)
        self.entrybarcode = Entry(self)
        self.entryitemname = Entry(self, textvariable='defaulttext')
        #grid sorting
        self.labelserial.grid(row=1, sticky=E)
        self.labelbarcode.grid(row=2, sticky=E)
        self.labelitemname.grid(row=3, sticky=E)
        self.entryserial.grid(row=1, column=1)
        self.entrybarcode.grid(row=2, column=1)
        self.entryitemname.grid(row=3, column=1)
        self.logbtn = Button(self, text="Search", command = self._search_btn_clickked,bg="#B3B3B3")
        self.logbtn.grid(row=1, column=2)
        self.logbtn = Button(self, text="Return", command = self._return_btn_clickked,bg="#B3B3B3")
        self.logbtn.grid(row=2, column=2)
        self.logout = Button(self, text="Exit", command = userpanel,bg="#B3B3B3")
        self.logout.grid(row=3, column=2)
        #pack grid
    def _search_btn_clickked(self):
        serialno = self.entryserial.get()
        barcodeno = self.entrybarcode.get()
        search = c.execute('SELECT ItemName FROM items WHERE serial="%s" and barcode="%s"' % (serialno,barcodeno))
        self.entryitemname.delete(0, 'end')
        result=c.fetchone()
        #c.fetchone()
        if result is not None:
            tm.showinfo("Search Found", "This item has been found in the database.")
            self.entryitemname.insert(END, result)
            conn.commit()
        else:
            tm.showerror("Search error", "Search failed, please ensure you have typed the details correctly. Otherwise please contact the system adminstrator.")
            conn.commit()
    def _return_btn_clickked(self):
        serial = self.entryserial.get()
        barcode = self.entrybarcode.get()
        #Item = 
        #read from users table and ensures that user and password matches with information on database
        #when using different tables ensure that Email  and password matches the table selected (users) and only selecting users who have under 3 incorrect attempts
        c.execute('SELECT * from users WHERE Email="%s" AND password="%s" AND unattempt<3' % (user, password))
        try:
                if c.fetchone() == None:
                        tm.showinfo("Return info", "Thank you for returning this item")
                        #c.execute("INSERT INTO itemlog(ID, Email, datestamp,ItemName,serial)VALUES(?,?,?,?,?)",(,,,,))            conn.commit()
                        conn.commit()
                else:
                        tm.showerror("Return error", "Return failed, please ensure you have typed the details correctly. Otherwise please contact the system adminstrator")
                        conn.commit()
        except:
                print ("Error has occured")
root = Tk()
root.wm_title("User Retrun")
root.configure(bg="#707070")
logo = PhotoImage(master = root,file="APC-logo.gif")
w1 = Label(root, image=logo).grid(row=0,column=0)
lf = Return(root)
root.mainloop()
