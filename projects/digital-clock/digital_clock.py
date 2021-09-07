from tkinter import*
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")


def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(100, time)


label = Label(root, font=("JetBrains Mono", 70),
              background="black", foreground="azure")
label.pack(anchor='center')
time()

mainloop()
