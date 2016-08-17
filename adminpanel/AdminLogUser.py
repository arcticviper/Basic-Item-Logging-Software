# BILS - BASIC ITEM LOGGING SOFTWARE
# Created: 18/07
# Modified: 17/08
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
        runpy.run_path('adminpanel/AdminPanel.py')
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
        self.labelincr = Label(self, text="Incorrect attempts")
        self.labeluser = Label(self, text="Username")
        self.labeldate = Label(self, text="Date Stamp")
        self.labelunat = Label(self, text="Successful")
        self.labellgid = Label(self, text="Log ID")
        self.labelincr2 = Label(self, text="Wrong \n attempts")
        self.labeluser2 = Label(self, text="Username")
        self.labeldate2 = Label(self, text="Date Stamp")
        self.labelunat2 = Label(self, text="Successful")
        self.labellgid2 = Label(self, text="Log ID")
        self.labeldivd = Label(self, text="______________________________________________________________________________")
        #init text boxes
        self.entryincr = Entry(self)
        self.entryuser = Entry(self)
        self.entrydate = Entry(self)
        self.entryunat = Entry(self)
        self.textlgid = Listbox(self, height = 6, width = 7,yscrollcommand=self.vsb.set) #id
        self.textincr = Listbox(self, height = 6, width = 7,yscrollcommand=self.vsb.set) #inc att
        self.textuser = Listbox(self, height = 6, width = 45,yscrollcommand=self.vsb.set)#usr
        self.textdate = Listbox(self, height = 6, width = 20,yscrollcommand=self.vsb.set)#date
        self.textatmp = Listbox(self, height = 6, width = 7,yscrollcommand=self.vsb.set)#successful

        #grid sorting
        self.labelincr.grid(row=1, column=1)
        self.labeluser.grid(row=2, column=1)
        self.labeldate.grid(row=3, column=1)
        self.labelunat.grid(row=4, column=1)
        self.entryincr.grid(row=1, column=2)
        self.entryuser.grid(row=2, column=2)
        self.entrydate.grid(row=3, column=2)
        self.entryunat.grid(row=4, column=2)
        self.labeldivd.grid(row=5, column=1,columnspan=3)
        self.labellgid2.grid(row=6, column=0)
        self.labelincr2.grid(row=6, column=1)
        self.labeluser2.grid(row=6, column=2)
        self.labeldate2.grid(row=6, column=3)
        self.labelunat2.grid(row=6, column=4)
        self.textlgid.grid(row=7, column=0,padx=5)
        self.textincr.grid(row=7, column=1,padx=5)
        self.textuser.grid(row=7, column=2,padx=5)
        self.textdate.grid(row=7, column=3,padx=5)
        self.textatmp.grid(row=7, column=4,padx=5)
        self.textlgid.bind("<MouseWheel>", self.OnMouseWheel)
        self.textincr.bind("<MouseWheel>", self.OnMouseWheel)
        self.textuser.bind("<MouseWheel>", self.OnMouseWheel)
        self.textdate.bind("<MouseWheel>", self.OnMouseWheel)
        self.textatmp.bind("<MouseWheel>", self.OnMouseWheel)
        # button functions
        self.srcbtn = Button(self, text="Latest User Login", command = self._search_btn_clickked,bg="#B3B3B3",width = 15)
        self.srcbtn.grid(row=1, column=3)
        self.srcbtn = Button(self, text="Full User Search", command = self._fullsearch_btn_clickked,bg="#B3B3B3",width = 15)
        self.srcbtn.grid(row=2, column=3)
        self.modbtn = Button(self, text="Clear", command = self._clear_btn_clickked,bg="#B3B3B3",width = 15)
        self.modbtn.grid(row=3, column=3)
        self.logout = Button(self, text="Exit", command = adminpanel,bg="#B3B3B3",width = 15)
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
        incatt = self.entryincr.get()
        dated = self.entrydate.get()
        unat = self.entryunat.get()
        self.entryincr.delete(0, 'end')
        self.entrydate.delete(0, 'end')
        self.entryunat.delete(0, 'end')
        #self.textlgid.delete(0.0, 'end')
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
                #use more efficient code in future?
                for row in c.execute('SELECT * FROM userlog WHERE Email="%s"' % (user)):
                        logid,incat,email,dates,sucess=(row)
                        print (sucess)
                        if sucess == 1:
                                sucess = "Yes"
                        else:
                                sucess = "No"
                        self.textlgid.insert(END, logid)
                        self.textincr.insert(END, incat)
                        self.textuser.insert(END, email)
                        self.textdate.insert(END, dates)
                        self.textatmp.insert(END, sucess)
                        
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
        self.textlgid.delete(1.0, 'end')
        self.textincr.delete(1.0, 'end')
        self.textuser.delete(1.0, 'end')
        self.textdate.delete(1.0, 'end')
        self.textatmp.delete(1.0, 'end')
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
