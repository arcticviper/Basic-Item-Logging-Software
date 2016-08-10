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
        #init scrollbar
        self.vsb = Scrollbar(orient="vertical", command=self.OnVsb)
        #init labels
        self.labeluser = Label(self, text="Username")
        self.labeldate = Label(self, text="Date Stamp")
        self.labelname = Label(self, text="Item Name")
        self.labelseri = Label(self, text="Serial")
        self.labelbrrw = Label(self, text="Borrowing")
        self.labelfull = Label(self, text="Full Info")
        self.labelitid = Label(self, text="Log Id")
        self.labeluser2 = Label(self, text="Username")
        self.labeldate2 = Label(self, text="Date Stamp")
        self.labelname2 = Label(self, text="Item Name")
        self.labelseri2 = Label(self, text="Serial")
        self.labelbrrw2 = Label(self, text="Borrowing")
        self.labeldivd = Label(self, text="___________________________________________________________________________________________________________________")
        #init text boxes
        self.entryuser = Entry(self)
        self.entrydate = Entry(self)        
        self.entryname = Entry(self)
        self.entryseri = Entry(self)
        self.entrybrrw = Entry(self)
        self.textitid = Listbox(self, height = 6, width = 7,yscrollcommand=self.vsb.set) #id
        self.textuser = Listbox(self, height = 6, width = 20,yscrollcommand=self.vsb.set) #user
        self.textdate = Listbox(self, height = 6, width = 20,yscrollcommand=self.vsb.set) #date
        self.textname = Listbox(self, height = 6, width = 20,yscrollcommand=self.vsb.set)#name
        self.textseri = Listbox(self, height = 6, width = 20,yscrollcommand=self.vsb.set)#serial no
        self.textbrrw = Listbox(self, height = 6, width = 7,yscrollcommand=self.vsb.set) #successful
        #grid sorting
        self.labeluser.grid(row=1, column=1)
        self.labeldate.grid(row=2, column=1)
        self.labelname.grid(row=3, column=1)
        self.labelseri.grid(row=4, column=1)
        self.labelbrrw.grid(row=5, column=1)
        self.entryuser.grid(row=1, column=2)
        self.entrydate.grid(row=2, column=2)
        self.entryname.grid(row=3, column=2)
        self.entryseri.grid(row=4, column=2)
        self.entrybrrw.grid(row=5, column=2)
        self.labeldivd.grid(row=6, column=1,columnspan=4)
        self.labelitid.grid(row=7, column=0)
        self.labeluser2.grid(row=7, column=1)
        self.labeldate2.grid(row=7, column=2)
        self.labelname2.grid(row=7, column=3)
        self.labelseri2.grid(row=7, column=4)
        self.labelbrrw2.grid(row=7, column=5)
        self.textitid.grid(row=8, column=0,padx=5)
        self.textuser.grid(row=8, column=1,padx=5)
        self.textdate.grid(row=8, column=2,padx=5)
        self.textname.grid(row=8, column=3,padx=5)
        self.textseri.grid(row=8, column=4,padx=5)
        self.textbrrw.grid(row=8, column=5,padx=5)
        self.textitid.bind("<MouseWheel>", self.OnMouseWheel)
        self.textuser.bind("<MouseWheel>", self.OnMouseWheel)
        self.textdate.bind("<MouseWheel>", self.OnMouseWheel)
        self.textname.bind("<MouseWheel>", self.OnMouseWheel)
        self.textseri.bind("<MouseWheel>", self.OnMouseWheel)
        self.textbrrw.bind("<MouseWheel>", self.OnMouseWheel)
        # button functions
        self.srcbtn = Button(self, text="Latest Event", command = self._search_btn_clickked,bg="#B3B3B3",width = 10)
        self.srcbtn.grid(row=1, column=3)
        self.srcbtn = Button(self, text="Full Search", command = self._fullsearch_btn_clickked,bg="#B3B3B3",width = 10)
        self.srcbtn.grid(row=2, column=3)
        self.modbtn = Button(self, text="Clear", command = self._clear_btn_clickked,bg="#B3B3B3",width = 10)
        self.modbtn.grid(row=3, column=3)
        self.logout = Button(self, text="Exit", command = adminpanel,bg="#B3B3B3",width = 10)
        self.logout.grid(row=4, column=3)
        # frame complete
    def OnVsb(self, *args):
        self.textlgid.yview(*args)
        self.textincr.yview(*args)
        self.textuser.yview(*args)
        self.textdate.yview(*args)
        self.textatmp.yview(*args)
    def OnMouseWheel(self, event):
        self.textlgid.yview("scroll",event.delta,"units")
        self.textincr.yview("scroll",event.delta,"units")
        self.textuser.yview("scroll",event.delta,"units")
        self.textdate.yview("scroll",event.delta,"units")
        self.textatmp.yview("scroll",event.delta,"units")
        return "break"
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
                        print (row)
                        itemid,email,dates,name,serial,borrowing=(row)
                        if borrowing == 1:
                                borrowing = 'True'
                        else:
                                borrowing = 'False'
                        self.textitid.insert(END, itemid)
                        self.textitid.insert(END, "\n")
                        self.textuser.insert(END, email)
                        self.textuser.insert(END, "\n")
                        self.textdate.insert(END, dates)
                        self.textdate.insert(END, "\n")
                        self.textname.insert(END, name)
                        self.textname.insert(END, "\n")
                        self.textseri.insert(END, serial)
                        self.textseri.insert(END, "\n")
                        self.textbrrw.insert(END, borrowing)
                        self.textbrrw.insert(END, "\n")
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
        self.textitid.delete(1.0, 'end')
        self.textuser.insert(1.0, 'end')
        self.textdate.insert(1.0, 'end')
        self.textname.insert(1.0, 'end')
        self.textseri.insert(1.0, 'end')
        self.textbrrw.insert(1.0, 'end')
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
