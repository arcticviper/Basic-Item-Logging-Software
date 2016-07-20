# BILS - BASIC ITEM LOGGING SOFTWARE
# Version 0.1
# Created by Charles Denison
# Item Mod
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
        self.labelseri = Label(self, text="Serial")
        self.labelbarc = Label(self, text="Barcode")
        self.labelname = Label(self, text="Item Name")
        self.labelcate = Label(self, text="Category")
        self.labelquan = Label(self, text="Quantity")
        self.labelnote = Label(self, text="Notes")
        self.labelbrrw = Label(self, text="Borrower")
        self.labelbker = Label(self, text="Booker")
        #init entry
        self.entryseri = Entry(self)
        self.entrybarc = Entry(self)
        self.entryname = Entry(self)
        self.entrycate = Entry(self)
        self.entryquan = Entry(self)
        self.entrynote = Entry(self)
        self.entrybrrw = Entry(self)
        self.entrybker = Entry(self)
        
        #grid sorting
        self.labelseri.grid(row=1, sticky=E)
        self.labelbarc.grid(row=2, sticky=E)
        self.labelname.grid(row=3, sticky=E)
        self.labelcate.grid(row=4, sticky=E)
        self.labelquan.grid(row=5, sticky=E)
        self.labelnote.grid(row=6, sticky=E)
        self.labelbrrw.grid(row=7, sticky=E)
        self.labelbker.grid(row=8, sticky=E)
        self.entryseri.grid(row=1, column=1)
        self.entrybarc.grid(row=2, column=1)
        self.entryname.grid(row=3, column=1)
        self.entrycate.grid(row=4, column=1)
        self.entryquan.grid(row=5, column=1)
        self.entrynote.grid(row=6, column=1)
        self.entrybrrw.grid(row=7, column=1)
        self.entrybker.grid(row=8, column=1)
        

        #buttons
        self.addbtn = Button(self, text="Search Item", command = self._search_btn_clickked,bg="#B3B3B3" ,width = 10)
        self.addbtn.grid(row=1, column=2)
        self.addbtn = Button(self, text="Modify Item", command = self._modify_btn_clickked,bg="#B3B3B3",width = 10)
        self.addbtn.grid(row=2, column=2)
        self.addbtn = Button(self, text="Remove Item", command = self._remove_btn_clickked,bg="#B3B3B3",width = 10)
        self.addbtn.grid(row=3, column=2)
        self.clrbtn = Button(self, text="Clear", command = self._clear_btn_clickked,bg="#B3B3B3",width = 10)
        self.clrbtn.grid(row=4, column=2)
        self.logout = Button(self, text="Exit", command = adminpanel,bg="#B3B3B3",width = 10)
        self.logout.grid(row=5, column=2)
        # frame complete
        # button functions
    def _search_btn_clickked(self):
        itemname = self.entryname.get()
        search = c.execute('SELECT serial FROM items WHERE ItemName="%s"' % (itemname))
        self.entryseri.delete(0, 'end')
        self.entrybarc.delete(0, 'end')
        self.entryname.delete(0, 'end')
        self.entrycate.delete(0, 'end')
        self.entryquan.delete(0, 'end')
        self.entrynote.delete(0, 'end')
        self.entrybrrw.delete(0, 'end')
        self.entrybker.delete(0, 'end')
        
        result1=c.fetchone()
        try: #verify item exists
                serial = result1[0] #removes brackets
        except:
                tm.showerror("format error", "Search failed, please ensure you have typed the details correctly.")
                conn.commit()
        if serial is not None: #grab info
                self.entryseri.insert(END, serial)
                c.execute('SELECT barcode FROM items WHERE serial="%s"' % (serial))
                getbarc = c.fetchone()
                self.entrybarc.insert(END, getbarc)
                c.execute('SELECT ItemName FROM items WHERE serial="%s"' % (serial))
                getname1 = c.fetchone()
                try: 
                        getname = getname1[0] #removes brackets
                except:
                        tm.showerror("format error", "Search failed, please ensure you have typed the details correctly.")
                conn.commit()
                self.entryname.insert(END, getname)
                c.execute('SELECT Category FROM items WHERE serial="%s"' % (serial))
                getcat = c.fetchone()
                self.entrycate.insert(END, getcat)
                c.execute('SELECT Quantity FROM items WHERE serial="%s"' % (serial))
                getquan = c.fetchone()
                self.entryquan.insert(END, getquan)
                c.execute('SELECT Notes FROM items WHERE serial="%s"' % (serial))
                getnote = c.fetchone()
                self.entrynote.insert(END, getnote)
                c.execute('SELECT Borrower FROM items WHERE serial="%s"' % (serial))
                getbrrw = c.fetchone()
                self.entrybrrw.insert(END, getbrrw)
                c.execute('SELECT Booker FROM items WHERE serial="%s"' % (serial))
                getbker = c.fetchone()
                self.entrybker.insert(END, getbker)


                tm.showinfo("Search Found", "This user has been found in the database.")
                
                conn.commit()
        else:
                tm.showerror("Search error", "Search failed, please ensure you have typed the details correctly.")
                conn.commit()
    def _modify_btn_clickked(self):
        try:
            seri = self.entryseri.get()
            barc = self.entrybarc.get()
            name = self.entryname.get()
            cate = self.entrycate.get()
            quan = self.entryquan.get()
            note = self.entrynote.get()
            brrw = self.entrybrrw.get()
            bker = self.entrybker.get()
            quan = int(quan)
            print (seri,barc,name,cate,quan,note,brrw,bker)#debugging
            c.execute('SELECT serial FROM items WHERE ItemName="%s"' % (name))
            tempid1=c.fetchone()
            print(tempid1)
            tempid = tempid1[0] #removes brackets
            print(tempid)
        except:
            tm.showerror("Search error", "Search failed, please ensure you have typed the details correctly.")
            conn.commit()
        print(tempid)
        if seri is not "":
            if barc is not "":
                if name is not "":
                    if cate is not "":
                        if quan > 0:
                            tm.showinfo("Update complete", "The details have been updated.")
                            c.execute('UPDATE items SET barcode = "%s",ItemName = "%s",Category = "%s",Quantity = "%s",Notes = "%s" WHERE serial="%s"' %(barc,name,cate,quan,note,seri))
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
    def _clear_btn_clickked(self):
        self.entryseri.delete(0, 'end')
        self.entrybarc.delete(0, 'end')
        self.entryname.delete(0, 'end')
        self.entrycate.delete(0, 'end')
        self.entryquan.delete(0, 'end')
        self.entrynote.delete(0, 'end')
        self.entrybrrw.delete(0, 'end')
        self.entrybker.delete(0, 'end')
        tm.showinfo("Clear input", "Input has been cleared.")
        conn.commit()
    def _remove_btn_clickked(self):
        seri = self.entryseri.get()
        barc = self.entrybarc.get()
        name = self.entryname.get()
        c.execute('SELECT serial FROM items WHERE barcode="%s" AND serial="%s"' % (barc,seri))
        remit1=c.fetchone()
        try: #verify user exists
                remit = remit1[0] #removes brackets
                print(remit1)
        except:
                tm.showerror("Search error", "Search failed, please ensure you have typed the details correctly.")
                conn.commit()
        print(remit)
        if remit is not None:
            result = tm.askyesno("Delete", 'Do you want to delete item "%s"?' % (name))
            if result == True:
                c.execute('DELETE FROM items WHERE serial="%s"' % (seri))
                conn.commit()
            else:
                return
        
        
        
#execute functions
root = Tk()
root.wm_title("Mod Item")
root.configure(bg="#707070")
logo = PhotoImage(master = root,file="APC-logo.gif")
w1 = Label(root, image=logo).grid(row=0,column=0)
lf = Borrow(root)
root.mainloop()
