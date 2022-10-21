from tkinter import *
from tkinter import ttk

from Interface.loginViewController import *

class AppUI:
    root = Tk()
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    def __init__(self):
        # Frame configuration
        self.root.title("Main")
        self.mainframe.pack()
        lvc = LoginVC(self.mainframe)
        lvc.grid()
        return

    def start(self):
        self.root.mainloop()
        return

