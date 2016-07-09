def func1():
    import tkinter as tk

    root1 = tk.Tk()

    def kill1():
        root1.destroy()
        from py2 import func2
        func2()

    button1 = tk.Button(root1, bg = 'green', text = 'hit to kill py1 and start py2', command = kill1)
    button1.pack()

    root1.mainloop()

if __name__ == '__main__':
    func1()
