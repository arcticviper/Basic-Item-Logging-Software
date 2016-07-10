from tkinter import *
import tkinter
import os
import runpy
import runpy
class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widget()
        
    def create_widget(self,):
        self.bttn1 = Button(root,text="Run Panel",width=80,bg="#B3B3B3")
        self.bttn1["command"] = runpy.run_path('adminpanel.py')
        self.bttn1.grid(row=1,column=0)
root = Tk()
root.configure(bg="#4D4D4D")
app1 = Application(root)
root.mainloop
