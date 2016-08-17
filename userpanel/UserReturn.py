# BILS - BASIC ITEM LOGGING SOFTWARE
# Created: 14/07
# Modified: 17/08
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
date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
id
def userpanel():
        conn.close()
        root.destroy()
        runpy.run_path('userpanel/UserPanel.py')
#user input
class Return(Frame): #create returnframe
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
        result1=c.fetchone()
        result = result1[0] #removes brackets as sometimes may return as tuples
        if result is not None:
                self.entryitemname.insert(END, result)
                tm.showinfo("Search Found", "This item has been found in the database.")
                conn.commit()
        else:
                tm.showerror("Search error", "Search failed, please ensure you have typed the details correctly. Otherwise please contact the system adminstrator.")
                conn.commit()
    def _return_btn_clickked(self):
        c.execute('SELECT Email FROM userlog ORDER BY Email DESC LIMIT 1')
        Email1 = c.fetchone()
        Email = Email1[0] #removes brackets
        print (Email) #debugging
        #potentially fix to allow for multiple logins as this only allows for one login at a time.
        serialno = self.entryserial.get()
        barcodeno = self.entrybarcode.get()
        search = c.execute('SELECT ItemName FROM items WHERE serial="%s" and barcode="%s"' % (serialno,barcodeno))
        self.entryitemname.delete(0, 'end')
        result1=c.fetchone()
        try:
                result = result1[0] #removes brackets
        except:
                tm.showerror("Return error", "Search failed, please ensure you have typed the details correctly. Otherwise please contact the system adminstrator.")
                conn.commit()
        print (result)
        if result is not None:
                c.execute('SELECT Borrower FROM items WHERE serial="%s" and barcode="%s"' % (serialno,barcodeno))
                borchk1 = c.fetchone()
                print (borchk1) #debugging
                borchk = borchk1[0]
                print (borchk) #debugging
                if borchk != None: #prevent people from accidentally returning when item has not been borrowed
                        tm.showinfo("Return complete", "Thank you for returning this item.")
                        self.entryitemname.insert(END, result)
                        c.execute("INSERT INTO itemlog(Email, datestamp, ItemName, serial,borrowing) VALUES(?,?,?,?,?)",(str(Email),date,str(result),serialno,False))
                        c.execute('UPDATE items SET Borrower = NULL WHERE serial="%s" and barcode="%s"' % (serialno,barcodeno))
                        conn.commit()
                else:
                        tm.showerror("Wrong button?", "Did you mean to click on the borrow item? Please contact the system admininstrator if this is not the case.")
                        conn.commit()
        else:
                tm.showerror("Search error", "Search failed, please ensure you have typed the details correctly. Otherwise please contact the system adminstrator.")
                conn.commit()
root = Tk()
root.wm_title("User Retrun")
root.configure(bg="#707070")
logo = PhotoImage(master = root,file="APC-logo.gif")
w1 = Label(root, image=logo).grid(row=0,column=0)
lf = Return(root)
root.mainloop()
