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
        self.labeluser = Label(self, text="Username")
        self.labeldate = Label(self, text="Date Stamp")
        self.labelname = Label(self, text="Item Name")
        self.labelseri = Label(self, text="Serial")
        self.labelbrrw = Label(self, text="Borrowing")
        self.labelfull = Label(self, text="Full Info")
        #init entry
        self.entryuser = Entry(self)
        self.entrydate = Entry(self)        
        self.entryname = Entry(self)
        self.entryseri = Entry(self)
        self.entrybrrw = Entry(self)
        self.textfull = Text(self, width= 60, height = 4)
        #grid sorting
        self.labeluser.grid(row=1, sticky=E)
        self.labeldate.grid(row=2, sticky=E)
        self.labelname.grid(row=3, sticky=E)
        self.labelseri.grid(row=4, sticky=E)
        self.labelbrrw.grid(row=5, sticky=E)
        self.labelfull.grid(row=6, column=1)
        self.entryuser.grid(row=1, column=1)
        self.entrydate.grid(row=2, column=1)
        self.entryname.grid(row=3, column=1)
        self.entryseri.grid(row=4, column=1)
        self.entrybrrw.grid(row=5, column=1)
        self.textfull.grid(row=7, column=0,columnspan=3,rowspan=4)
        self.textfull.grid_columnconfigure(1, weight=1)
        self.srcbtn = Button(self, text="Latest Event", command = self._search_btn_clickked,bg="#B3B3B3",width = 10)
        self.srcbtn.grid(row=1, column=2)
        self.srcbtn = Button(self, text="Full Search", command = self._fullsearch_btn_clickked,bg="#B3B3B3",width = 10)
        self.srcbtn.grid(row=2, column=2)
        self.modbtn = Button(self, text="Clear", command = self._clear_btn_clickked,bg="#B3B3B3",width = 10)
        self.modbtn.grid(row=3, column=2)
        self.logout = Button(self, text="Exit", command = adminpanel,bg="#B3B3B3",width = 10)
        self.logout.grid(row=4, column=2)
        # frame complete
        # button functions
    def _fullsearch_btn_clickked(self):
        user = self.entryuser.get()
        brrw = self.entrybrrw.get()
        dated = self.entrydate.get()
        itemname = self.entryname.get()
        serialno =  self.entryseri.get()
        self.entrydate.delete(0, 'end')
        self.entryname.delete(0, 'end')
        self.entrybrrw.delete(0, 'end')
        self.entryseri.delete(0, 'end')
        
        searchitem = c.execute('SELECT ItemName FROM itemlog WHERE Email="%s" ORDER BY id DESC' % (user))
        result1=c.fetchone()
        print(result1)
        try: #verify user exists
                att = result1[0] #removes brackets
                print(att)
        except:
                #tm.showerror("format error", "Search failed, please ensure you have typed the details correctly.")
                conn.commit()
                att = None
        if att is not None: #grab info using itemname
                self.entryname.insert(END, att)
                c.execute('SELECT serial FROM itemlog WHERE Email="%s" ORDER BY id DESC' % (user))
                getser = c.fetchone()
                self.entryseri.insert(END, getser)
                c.execute('SELECT borrowing FROM itemlog WHERE Email="%s" ORDER BY id DESC' % (user))
                getbrw1 = c.fetchone()
                getbrw = getbrw1[0]
                print(getbrw)
                if getbrw == 1:
                        getbrw = 'True'
                else:
                        getbrw = 'False'
                print(getbrw)
                self.entrybrrw.insert(END, getbrw)
                c.execute('SELECT datestamp FROM itemlog WHERE Email="%s" ORDER BY id DESC' % (user))
                getdate1 = c.fetchone()
                try: #verify user exists
                    getdate = getdate1[0] #removes brackets
                except:
                    tm.showerror("format error", "Search failed, please ensure you have typed the details correctly.")
                    conn.commit()
                self.entrydate.insert(END, getdate)
                for row in c.execute('SELECT * FROM itemlog WHERE Email="%s" ORDER BY id DESC' % (user)):
                    self.textfull.insert(END, row)
                    self.textfull.insert(END, "\n")
                tm.showinfo("Search Found", "This user has been found in the database.")
                conn.commit()
        elif itemname is not None and serialno is not None:
                searchname = c.execute('SELECT ItemName FROM itemlog WHERE serial="%s" ORDER BY id DESC' % (serialno))
                result1=c.fetchone()
                print(result1)
                itemname = result1[0] #removes brackets
                self.entryname.insert(END, itemname)
                c.execute('SELECT serial FROM itemlog WHERE serial="%s" ORDER BY id DESC' % (serialno))
                getser = c.fetchone()
                print(getser)
                self.entryseri.insert(END, getser)
                c.execute('SELECT Email FROM itemlog WHERE serial="%s" ORDER BY id DESC' % (serialno))
                getuser = c.fetchone()
                self.entryuser.insert(END, getuser)
                c.execute('SELECT borrowing FROM itemlog WHERE serial="%s" ORDER BY id DESC' % (serialno))
                getbrw1 = c.fetchone()
                getbrw = getbrw1[0]
                print(getbrw)
                if getbrw == 1:
                        getbrw = 'True'
                else:
                        getbrw = 'False'
                print(getbrw)
                self.entrybrrw.insert(END, getbrw)
                c.execute('SELECT datestamp FROM itemlog WHERE serial="%s" ORDER BY id DESC' % (serialno))
                getdate1 = c.fetchone()
                try: #verify user exists
                    getdate = getdate1[0] #removes brackets
                except:
                    tm.showerror("format error", "Search failed, please ensure you have typed the details correctly.")
                    conn.commit()
                self.entrydate.insert(END, getdate)
                for row in c.execute('SELECT * FROM itemlog WHERE serial="%s" ORDER BY id DESC' % (serialno)):
                    self.textfull.insert(END, row)
                    self.textfull.insert(END, "\n")
                tm.showinfo("Search Found", "This user has been found in the database.")
                conn.commit()
                
        else:
                tm.showerror("Search error", "Search failed, please ensure you have typed the details correctly.")
                conn.commit()
    def _search_btn_clickked(self):
        user = self.entryuser.get()
        brrw = self.entrybrrw.get()
        dated = self.entrydate.get()
        itemname = self.entryname.get()
        serialno =  self.entryseri.get()
        self.entrydate.delete(0, 'end')
        self.entryname.delete(0, 'end')
        self.entrybrrw.delete(0, 'end')
        self.entryseri.delete(0, 'end')
        
        
        searchitem = c.execute('SELECT ItemName FROM itemlog WHERE Email="%s" ORDER BY id DESC' % (user))
        result1=c.fetchone()
        print(result1)
        try: #verify user exists
                att = result1[0] #removes brackets
        except:
                tm.showerror("format error", "Search failed, please ensure you have typed the details correctly.")
                conn.commit()
        if att is not None: #grab info
                self.entryname.insert(END, att)
                c.execute('SELECT serial FROM itemlog WHERE Email="%s" ORDER BY id DESC' % (user))
                getser = c.fetchone()
                self.entryseri.insert(END, getser)
                c.execute('SELECT borrowing FROM itemlog WHERE Email="%s" ORDER BY id DESC' % (user))
                getbrw = c.fetchone()
                self.entrybrrw.insert(END, getbrw)
                c.execute('SELECT datestamp FROM itemlog WHERE Email="%s" ORDER BY id DESC' % (user))
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
        self.entrydate.delete(0, 'end')
        self.entryname.delete(0, 'end')
        self.entrybrrw.delete(0, 'end')
        self.entryseri.delete(0, 'end')
        self.entryname.delete(0, 'end')
        self.entryuser.delete(0, 'end')
        self.textfull.delete(1.0, 'end')
        tm.showinfo("Clear input", "Input has been cleared.")
        conn.commit()
        
        
        
#execute functions
root = Tk()
root.wm_title("Item Logging")
root.configure(bg="#707070")
logo = PhotoImage(master = root,file="APC-logo.gif")
w1 = Label(root, image=logo).grid(row=0,column=0)
lf = Borrow(root)
root.mainloop()
