# BILS - BASIC ITEM LOGGING SOFTWARE
# Version 0.1
# Created by Charles Denison
# User Modify
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
class usermod(Frame): #create returnframe
    def __init__(self, master):
        super().__init__(master)#inherit base class
        self.grid()
        self.create_widget()
    def create_widget(self):
        #init labels
        self.labeluser = Label(self, text="Username")
        self.labelpass = Label(self, text="Password")
        self.labelpriv = Label(self, text="Privilege")
        self.labelunat = Label(self, text="Incorrect attempts")
        #init entry
        self.entryuser = Entry(self)
        self.entrypass = Entry(self)
        self.entrypriv = Entry(self)
        self.entryunat = Entry(self)
        #grid sorting
        self.labeluser.grid(row=1, sticky=E)
        self.labelpass.grid(row=2, sticky=E)
        self.labelpriv.grid(row=3, sticky=E)
        self.labelunat.grid(row=4, sticky=E)
        self.entryuser.grid(row=1, column=1)
        self.entrypass.grid(row=2, column=1)
        self.entrypriv.grid(row=3, column=1)
        self.entryunat.grid(row=4, column=1)
        self.srcbtn = Button(self, text="Search User", command = self._search_btn_clickked,bg="#B3B3B3")
        self.srcbtn.grid(row=1, column=2)
        self.modbtn = Button(self, text="Modify User", command = self._modify_btn_clickked,bg="#B3B3B3")
        self.modbtn.grid(row=2, column=2)
        self.remout = Button(self, text="Remove User", command = self._remove_btn_clickked,bg="#B3B3B3")
        self.remout.grid(row=3, column=2)
        self.logout = Button(self, text="Exit", command = adminpanel,bg="#B3B3B3")
        self.logout.grid(row=4, column=2)
        # frame complete
        # button functions
    def _search_btn_clickked(self):
        user = self.entryuser.get()
        search = c.execute('SELECT password FROM users WHERE Email="%s"' % (user))
        self.entrypass.delete(0, 'end')
        self.entrypriv.delete(0, 'end')
        self.entryunat.delete(0, 'end')
        result1=c.fetchone()
        try: #verify user exists
                password = result1[0] #removes brackets
        except:
                tm.showerror("format error", "Search failed, please ensure you have typed the details correctly.")
                conn.commit()
        if password is not None: #grab info
                self.entrypass.insert(END, password)
                c.execute('SELECT priv FROM users WHERE Email="%s"' % (user))
                getpriv = c.fetchone()
                self.entrypriv.insert(END, getpriv)
                c.execute('SELECT unattempt FROM users WHERE Email="%s"' % (user))
                getinc = c.fetchone()
                self.entryunat.insert(END, getinc)
                tm.showinfo("Search Found", "This user has been found in the database.")
                conn.commit()
        else:
                tm.showerror("Search error", "Search failed, please ensure you have typed the details correctly.")
                conn.commit()
    def _modify_btn_clickked(self):
        try:
            user = self.entryuser.get()
            pwrd = self.entrypass.get()
            privget = self.entrypriv.get()
            unatget = self.entryunat.get()
            priv = int(privget)
            unat = int(unatget)
            print (user,pwrd,priv,unat)#debugging
            c.execute('SELECT ID FROM users WHERE Email="%s"' % (user))
            tempid1=c.fetchone()
            tempid = tempid1[0] #removes brackets
        except:
            tm.showerror("Search error", "Search failed, please ensure you have typed the details correctly.")
            conn.commit()
        print(tempid)
        if tempid is not None: #check if user exists
            if user is not "":
                if pwrd is not "":
                    if priv == 1 or priv == 0:
                        if unat >= 0:
                            tm.showinfo("Update complete", "The details have been updated.")
                            c.execute('UPDATE users SET Email = "%s",password = "%s",priv = "%s",unattempt = "%s" WHERE ID="%s"' % (user,pwrd,priv,unat,tempid))
                            conn.commit()
                        else:
                            tm.showerror("Incorrect value", "Please insert a value above 0 for incorrect attempts.")
                            conn.commit()
                    else:
                        tm.showerror("Incorrect value", "Please insert a 1 for admin and 0 user.")
                        conn.commit()
                else:
                    tm.showerror("Incorrect value", "Please insert a password.")
                    conn.commit()
            else:
                tm.showerror("Incorrect value", "Please insert a username")
                conn.commit()
            print ('test')
        else:
                tm.showerror("Borrow error2", "Search failed, please ensure you have typed the details correctly.")
                conn.commit()
    def _remove_btn_clickked(self):
        user = self.entryuser.get()
        c.execute('SELECT ID FROM users WHERE Email="%s"' % (user))
        remid1=c.fetchone()
        try: #verify user exists
                remid = remid1[0] #removes brackets
                print(remid)
        except:
                tm.showerror("Search error", "Search failed, please ensure you have typed the details correctly.")
                conn.commit()
        print(remid)
        if remid is not None:
            result = tm.askyesno("Delete", 'Do you want to delete user "%s"?' % (user))
            if result == True:
                c.execute('DELETE FROM users WHERE Email="%s"' % (user))
                conn.commit()
            else:
                return
        
        
        
#execute functions
root = Tk()
root.wm_title("User Modification")
root.configure(bg="#707070")
logo = PhotoImage(master = root,file="APC-logo.gif")
w1 = Label(root, image=logo).grid(row=0,column=0)
lf = usermod(root)
root.mainloop()
