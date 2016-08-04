# BILS - BASIC ITEM LOGGING SOFTWARE
# Version 0.1
# Created by Charles Denison
# User Log
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
        self.labelincr = Label(self, text="Incorrect attempts")
        self.labeluser = Label(self, text="Username")
        self.labeldate = Label(self, text="Date Stamp")
        self.labelunat = Label(self, text="Successful")
        self.labelfull = Label(self, text="Full Info")
        #init entry
        self.entryincr = Entry(self)
        self.entryuser = Entry(self)
        self.entrydate = Entry(self)
        self.entryunat = Entry(self)
        self.textfull = Text(self, width= 60, height = 4)
        #grid sorting
        self.labelincr.grid(row=1, sticky=E)
        self.labeluser.grid(row=2, sticky=E)
        self.labeldate.grid(row=3, sticky=E)
        self.labelunat.grid(row=4, sticky=E)
        self.labelfull.grid(row=5, column=1)
        self.entryincr.grid(row=1, column=1)
        self.entryuser.grid(row=2, column=1)
        self.entrydate.grid(row=3, column=1)
        self.entryunat.grid(row=4, column=1)
        self.textfull.grid(row=6, column=0,columnspan=3,rowspan=4)
        self.textfull.grid_columnconfigure(1, weight=1)
        self.srcbtn = Button(self, text="Latest User Login", command = self._search_btn_clickked,bg="#B3B3B3",width = 15)
        self.srcbtn.grid(row=1, column=2)
        self.srcbtn = Button(self, text="Full User Search", command = self._fullsearch_btn_clickked,bg="#B3B3B3",width = 15)
        self.srcbtn.grid(row=2, column=2)
        self.modbtn = Button(self, text="Clear", command = self._clear_btn_clickked,bg="#B3B3B3",width = 15)
        self.modbtn.grid(row=3, column=2)
        self.logout = Button(self, text="Exit", command = adminpanel,bg="#B3B3B3",width = 15)
        self.logout.grid(row=4, column=2)
        # frame complete
        # button functions
    def _fullsearch_btn_clickked(self):
        user = self.entryuser.get()
        incatt = self.entryincr.get()
        dated = self.entrydate.get()
        unat = self.entryunat.get()
        self.entryincr.delete(0, 'end')
        self.entrydate.delete(0, 'end')
        self.entryunat.delete(0, 'end')
        self.textfull.delete(0.0, 'end')
        searchatt = c.execute('SELECT Attempt FROM userlog WHERE Email="%s"' % (user))
        result1=c.fetchone()
        print(result1)
        att = None
        try: #verify user exists
                att = result1[0] #removes brackets
        except:
                tm.showerror("Search error", "Search failed, please ensure you have typed the details correctly.")
                conn.commit()
        if att is not None: #grab info
                self.entryincr.insert(END, att)
                c.execute('SELECT sucessful FROM userlog WHERE Email="%s"' % (user))
                getsuc = c.fetchone()
                self.entryunat.insert(END, getsuc)
                c.execute('SELECT Datestamp FROM userlog WHERE Email="%s"' % (user))
                getdate1 = c.fetchone()
                try: #verify user exists
                    getdate = getdate1[0] #removes brackets
                except:
                    tm.showerror("format error", "Search failed, please ensure you have typed the details correctly.")
                    conn.commit()
                self.entrydate.insert(END, getdate)
                for row in c.execute('SELECT * FROM userlog WHERE Email="%s"' % (user)):
                    self.textfull.insert(END, row)
                    self.textfull.insert(END, "\n")
                tm.showinfo("Search Found", "This user has been found in the database.")
                conn.commit()
        else:
                #tm.showerror("Search error", "Search failed, please ensure you have typed the details correctly.")
                conn.commit()
    def _search_btn_clickked(self):
        user = self.entryuser.get()
        incatt = self.entryincr.get()
        dated = self.entrydate.get()
        unat = self.entryunat.get()
        self.entryincr.delete(0, 'end')
        self.entrydate.delete(0, 'end')
        self.entryunat.delete(0, 'end')
        searchatt = c.execute('SELECT Attempt FROM userlog WHERE Email="%s"' % (user))
        result1=c.fetchone()
        print(result1)
        try: #verify user exists
                att = result1[0] #removes brackets
        except:
                tm.showerror("format error", "Search failed, please ensure you have typed the details correctly.")
                conn.commit()
        if att is not None: #grab info
                self.entryincr.insert(END, att)
                c.execute('SELECT sucessful FROM userlog WHERE Email="%s"' % (user))
                getsuc = c.fetchone()
                self.entryunat.insert(END, getsuc)
                c.execute('SELECT Datestamp FROM userlog WHERE Email="%s"' % (user))
                getdate1 = c.fetchone()
                try: #verify user exists
                    getdate = getdate1[0] #removes brackets
                except:
                    tm.showerror("format error", "Search failed, please ensure you have typed the details correctly.")
                    conn.commit()
                self.entrydate.insert(END, getdate)
                tm.showinfo("Search Found", "This user has been found in the database.")
                conn.commit()
        else:
                tm.showerror("Search error", "Search failed, please ensure you have typed the details correctly.")
                conn.commit()
    def _clear_btn_clickked(self):
        self.entryincr.delete(0, 'end')
        self.entryuser.delete(0, 'end')
        self.entrydate.delete(0, 'end')
        self.entryunat.delete(0, 'end')
        self.entrydate.delete(0, 'end')
        self.textfull.delete(1.0, 'end')
        tm.showinfo("Clear input", "Input has been cleared.")
        conn.commit()
        
        
        
#execute functions
root = Tk()
root.wm_title("User Logging")
root.configure(bg="#707070")
logo = PhotoImage(master = root,file="APC-logo.gif")
w1 = Label(root, image=logo).grid(row=0,column=0)
lf = Borrow(root)
root.mainloop()
