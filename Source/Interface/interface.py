from tkinter import *
from tkinter import ttk

class AppUI:
    root = Tk()
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    def __init__(self):
        # Frame configuration
        self.root.title("Main")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.init_view()

        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        return

    def start(self):
        self.root.mainloop()
        return

    def init_view(self):
        # member id entry
        mid = StringVar()  # member id
        mid_entry= ttk.Entry(self.mainframe, width=15, textvariable=mid)
        mid_entry.grid(column=2, row=1, sticky=(W, E))
        mid_entry.focus()

        # password entry
        pwd = StringVar()  # member id
        pwd_entry = ttk.Entry(self.mainframe, width=15, textvariable=pwd, show='*')
        pwd_entry.grid(column=2, row=2, sticky=(W, E))
        pwd_entry.focus()

        # login button
        login_button = ttk.Button(self.mainframe, text='Login', command=self.login_action)
        login_button.grid(column=2, row=3)
        

        return

    def login_action(self):
        pass
