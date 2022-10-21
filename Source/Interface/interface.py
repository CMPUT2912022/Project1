from tkinter import *
from tkinter import ttk

from Interface.loginViewController import *

class AppUI:
    root = Tk()
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    def __init__(self, app):
        # Frame configuration
        self.root.title("Napster V2")
        self.mainframe.pack()
        lvc = LoginVC(app, self.mainframe)
        lvc.grid()
        return

    def start(self):
        self.root.mainloop()
        return

