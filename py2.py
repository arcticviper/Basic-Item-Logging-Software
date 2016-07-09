def func2():
    import tkinter as tk

    root2 = tk.Tk()

    def kill2():
        root2.destroy()
        from py1 import func1
        func1()

    button2 = tk.Button(root2, bg = 'red', text = 'hit to kill py2 and start py1', command = kill2)
    button2.pack()

    root2.mainloop()

if __name__ == '__main__':
    func2()
