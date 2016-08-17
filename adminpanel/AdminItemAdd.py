# BILS - BASIC ITEM LOGGING SOFTWARE
# Created: 19/07
# Modified: 17/08
# Created by Charles Denison
# Item Creation
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
        #init labels
        self.labelseri = Label(self, text="Serial")
        self.labelbarc = Label(self, text="Barcode")
        self.labelname = Label(self, text="Item Name")
        self.labelcate = Label(self, text="Category")
        self.labelquan = Label(self, text="Quantity")
        self.labelnote = Label(self, text="Notes")
        #init entry
        self.entryseri = Entry(self)
        self.entrybarc = Entry(self)
        self.entryname = Entry(self)
        self.entrycate = Entry(self)
        self.entryquan = Entry(self)
        self.entrynote = Entry(self)
        
        #grid sorting
        self.labelseri.grid(row=1, sticky=E)
        self.labelbarc.grid(row=2, sticky=E)
        self.labelname.grid(row=3, sticky=E)
        self.labelcate.grid(row=4, sticky=E)
        self.labelquan.grid(row=5, sticky=E)
        self.labelnote.grid(row=6, sticky=E)
        self.entryseri.grid(row=1, column=1)
        self.entrybarc.grid(row=2, column=1)
        self.entryname.grid(row=3, column=1)
        self.entrycate.grid(row=4, column=1)
        self.entryquan.grid(row=5, column=1)
        self.entrynote.grid(row=6, column=1)

        #buttons
        self.addbtn = Button(self, text="Add Item", command = self._add_btn_clickked,bg="#B3B3B3",height = 2,width = 7)
        self.addbtn.grid(row=1, column=2, rowspan=2)
        self.clrbtn = Button(self, text="Clear", command = self._clear_btn_clickked,bg="#B3B3B3",height = 2,width = 7)
        self.clrbtn.grid(row=3, column=2, rowspan=2)
        self.logout = Button(self, text="Exit", command = adminpanel,bg="#B3B3B3",height = 2,width = 7)
        self.logout.grid(row=5, column=2, rowspan=2)
        # frame complete
        # button functions
    def _clear_btn_clickked(self):
        self.entryseri.delete(0, 'end')
        self.entrybarc.delete(0, 'end')
        self.entryname.delete(0, 'end')
        self.entrycate.delete(0, 'end')
        self.entryquan.delete(0, 'end')
        self.entrynote.delete(0, 'end')
        tm.showinfo("Clear input", "Input has been cleared.")
        conn.commit()
    def _add_btn_clickked(self):
        seri = self.entryseri.get()
        barc = self.entrybarc.get()
        name = self.entryname.get()
        cate = self.entrycate.get()
        quan = self.entryquan.get()
        quan = int(quan)
        note = self.entrynote.get()
        print (seri,barc,name,cate,quan,note)#debugging
        if seri is not "":
            if barc is not "":
                if name is not "":
                    if cate is not "":
                        if quan > 0:
                            tm.showinfo("Insert complete", "The item/s have been added.")
                            c.execute('INSERT INTO items(serial,barcode,ItemName,Category,Quantity,Notes)VALUES(?,?,?,?,?,?)' ,(seri,barc,name,cate,quan,note))
                            conn.commit()
                        else:
                            tm.showerror("Incorrect value", "Please insert the quanitity greater than 0.")
                            conn.commit()
                    else:
                        tm.showerror("Incorrect value", "Please insert the serial number, if there is none, input Misc")
                        conn.commit()
                else:
                    tm.showerror("Incorrect value", "Please insert the Name of the Product, if there is none, input NA")
                    conn.commit()
            else:
                tm.showerror("Incorrect value", "Please insert the barcode, if there is none, input NA")
                conn.commit()
        else:
                tm.showerror("Incorrect value", "Please insert the serial number, if there is none, input NA")
                conn.commit()
        
        
        
#execute functions
root = Tk()
root.wm_title("New Item")
root.configure(bg="#707070")
logo = PhotoImage(master = root,file="APC-logo.gif")
w1 = Label(root, image=logo).grid(row=0,column=0)
lf = Borrow(root)
root.mainloop()
