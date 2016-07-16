# BILS - BASIC ITEM LOGGING SOFTWARE
# Version 0.1
# Created by Charles Denison
# Item reserver
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
        runpy.run_path('userpanel.py')
#user input
class Borrow(Frame): #create returnframe
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
        self.logbtn = Button(self, text="Reserve", command = self._reserve_btn_clickked,bg="#B3B3B3")
        self.logbtn.grid(row=2, column=2)
        self.logout = Button(self, text="Exit", command = userpanel,bg="#B3B3B3")
        self.logout.grid(row=3, column=2)
        # frame complete
        # button functions
    def _search_btn_clickked(self):
        serialno = self.entryserial.get()
        barcodeno = self.entrybarcode.get()
        search = c.execute('SELECT ItemName FROM items WHERE serial="%s" and barcode="%s"' % (serialno,barcodeno))
        self.entryitemname.delete(0, 'end')
        result1=c.fetchone()
        try:
                result = result1[0] #removes brackets
        except:
                tm.showerror("Borrow error", "Search failed, please ensure you have typed the details correctly. Otherwise please contact the system adminstrator.")
                conn.commit()
        if result is not None:
                self.entryitemname.insert(END, result)
                tm.showinfo("Search Found", "This item has been found in the database.")
                conn.commit()
        else:
                tm.showerror("Search error", "Search failed, please ensure you have typed the details correctly. Otherwise please contact the system adminstrator.")
                conn.commit()
    def _reserve_btn_clickked(self):
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
                tm.showerror("Borrow error", "Search failed, please ensure you have typed the details correctly. Otherwise please contact the system adminstrator.")
                conn.commit()
        if result is not None:
                bookchk = c.execute('SELECT Booker FROM items WHERE serial="%s" and barcode="%s"' % (serialno,barcodeno))
                resemail1 = c.fetchone()
                resemail = resemail1[0] #removes brackets
                print (resemail) #debugging
                if resemail == Email or resemail is None:
                        c.execute('SELECT Borrower FROM items WHERE serial="%s" and barcode="%s"' % (serialno,barcodeno))
                        retchk1 = c.fetchone()
                        print (retchk1) #debugging
                        retchk = retchk1[0]
                        print (retchk) #debugging
                        if retchk != Email:
                            self.entryitemname.insert(END, result)
                            tm.showinfo("Borrow complete", "Thank you for reserving this item.")
                            c.execute('UPDATE items SET Borrower = "%s",Booker = null WHERE serial="%s" and barcode="%s"' % (Email,serialno,barcodeno))
                            conn.commit()
                        else:
                            tm.showerror("Wrong button?", "Did you mean to click on the return item? Please contact the system admininstrator if this is not the case.")
                            conn.commit()
                else:
                    tm.showerror("Reserved Item", "This item has been reserved by somebody else. Please contact the system admininstrator if this is false.")
                    conn.commit()
        else:
                tm.showerror("Borrow error", "Search failed, please ensure you have typed the details correctly. Otherwise please contact the system adminstrator.")
                conn.commit()
#execute functions
root = Tk()
root.wm_title("User Reserve")
root.configure(bg="#707070")
logo = PhotoImage(master = root,file="APC-logo.gif")
w1 = Label(root, image=logo).grid(row=0,column=0)
lf = Borrow(root)
root.mainloop()
