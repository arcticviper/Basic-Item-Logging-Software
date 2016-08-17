# BILS - BASIC ITEM LOGGING SOFTWARE
# Created: 14/07
# Modified: 17/08
# Created by Charles Denison
# Loading Screen
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import runpy
import time
def login():
    root2.destroy()
    runpy.run_path('login.py')

def main():
  self = ttk.Frame()
  self.pack(expand=True, fill=tk.BOTH, side=tk.BOTTOM)
  pb_hd = ttk.Progressbar(self, orient='horizontal', mode='determinate')
  pb_hd.pack(expand=True, fill=tk.BOTH, side=tk.BOTTOM)
  pb_hd.start(50)
  root2.wm_title("Loading")
  root2.configure(bg="#707070")
  logo = tk.PhotoImage(file="APC-logo.gif")
  lg = tk.Label(image=logo)
  lg.image = logo
  lg.pack()
  root2.after(4998, login)
  root2.mainloop()

root2 = Tk()
main()
