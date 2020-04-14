from Tkinter import *

def save():
    text = e1.get() + "\n"+e2.get() + "\n"+e3.get() 
    with open("test.txt", "w") as f:
        f.writelines(text)

def show():
    with open("test.txt", "r") as f:
        f.readlines()
    e1.get(f.seek(0))
    e2.get(f.seek(1))
    e3.get(f.seek(2))


master = Tk(className = "ABM Inputs")

Label(master, text="RNG Seed").grid(row=0)
Label(master, text="Manipulator Exists 1=yes, 0=no").grid(row=1)
Label(master, text="Number of Investors").grid(row=2)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(master, text='Save', command=save).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )